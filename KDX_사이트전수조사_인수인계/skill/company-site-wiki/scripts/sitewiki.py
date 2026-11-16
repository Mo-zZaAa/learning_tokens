#!/usr/bin/env python3
# sitewiki.py
"""기업 공식 사이트 전수 목록화(map) > 읽기 계획(plan) > 마크다운 변환(fetch) > 읽기 묶음(digest) > 메모 검수(verify) > 누락 점검(audit).
장부는 <work>/inventory.csv 한 파일이고 모든 명령은 이어서 다시 실행할 수 있다.
  map    --work W --domain example.com --seed https://example.com [--seed ...] [--max-hosts 25] [--sitemap-cap 1500] [--no-render]
  plan   --work W [--read 'URL패턴'] [--skim ..] [--list ..] [--skip ..] [--add 'https://밖의문서'] [--template-min 40] [--sample 5] [--skim-cap 40] [--read-all-under 300]
  fetch  --work W [--minutes 8] [--only 'URL패턴'] [--limit N] [--render auto|read|all|thin|never] [--click deep|basic] [--refetch 'URL패턴']
  digest --work W [--pack-chars 120000]
  audit  --work W [--wiki 위키폴더]
  verify --work W [--notes 메모폴더]      메모의 근거 구절이 원문에 있는지, 빠진 페이지가 없는지 대조
URL패턴은 * 를 쓰는 전체 일치(예: 'https://example.com/blog/*'). 여러 패턴에 걸리면 list < skim < read < skip 순으로 뒤쪽이 우선. 패턴과 계획 설정은 <work>/overrides.json에 남아 이후 명령에도 적용된다.
plan 값: read=수집 후 정독, skim=수집 후 제목과 첫머리만 표로, list=URL만 기록, skip=수집 안 함(언어판 중복, robots 제외, 수동 제외)"""
import argparse, collections, csv, fnmatch, gzip, hashlib, json, os, re, sys, time
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin, urlsplit, urlunsplit, parse_qsl, urlencode
from urllib import robotparser
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify

UA = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
      'Chrome/130.0 Safari/537.36')
FIELDS = ['url', 'host', 'locale', 'section', 'group', 'source', 'plan', 'status',
          'method', 'chars', 'title', 'file', 'note']
LANGS = set('en ko ja zh de fr es it pt ru tr nl pl vi id th ar uk hi sv da fi no nb cs hu ro el he ms '
            'fil bg hr sk sl lt lv et sr ca'.split())
LOCALE_RE = re.compile(r'^([a-z]{2})(?:[-_]([a-z]{2,4}))?$', re.I)
SKIP_EXT = re.compile(r'[.](png|jpe?g|gif|svg|webp|ico|css|js|mjs|woff2?|ttf|mp4|webm|mp3|zip|gz|dmg|exe|apk|xml|json|rss)$', re.I)
TRACK = re.compile(r'^(utm_|gclid|fbclid|msclkid|mc_|_hs|ga_|af_|anon_id|statsig|original_landing|landing$|pid$|ref$|referrer$|rfr$|redirect$|preferTheme$)', re.I)
PUBLIC = set('www docs doc developers developer blog news support help learn academy ir investors investor status app legal trust security '
             'careers jobs about press newsroom research community partners institutional institutions pro business enterprise wallet pay'.split())
INTERNAL = re.compile(r'(^|[.-])(staging|stage|stg|dev|test|testnet|sandbox|internal|infra|monitor[a-z]*|admin|vpn|preview|qa|uat|private|tailnet|corp|intranet)([.-]|$)')
BLOCK_HINT = re.compile(r'just a moment|cf-chl|captcha|access denied|are you a robot', re.I)
S = requests.Session(); S.headers.update({'User-Agent': UA, 'Accept-Language': 'en-US,en;q=0.9,ko;q=0.8'})
_robots = {}; FENCE = '`' * 3

def norm(url):
    try: p = urlsplit(url.strip())
    except ValueError: return ''
    if p.scheme not in ('http', 'https') or not p.netloc: return ''
    q = urlencode([(k, v) for k, v in parse_qsl(p.query, keep_blank_values=True) if not TRACK.match(k)])
    path = re.sub(r'/{2,}', '/', p.path) or '/'
    if len(path) > 1: path = path.rstrip('/')
    return urlunsplit(('https', p.netloc.lower().split(':')[0], path, q, ''))

def in_scope(host, domains): return any(host == d or host.endswith('.' + d) for d in domains)

def load(work):
    path = os.path.join(work, 'inventory.csv'); rows = collections.OrderedDict()
    if os.path.exists(path):
        with open(path, newline='', encoding='utf-8') as f:
            for r in csv.DictReader(f): rows[r['url']] = r
    return rows

def save(work, rows):
    os.makedirs(work, exist_ok=True); tmp = os.path.join(work, 'inventory.csv.tmp')
    with open(tmp, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=FIELDS); w.writeheader(); w.writerows(rows.values())
    os.replace(tmp, os.path.join(work, 'inventory.csv'))

def add(rows, url, source, domains, ext=None):
    u = norm(url)
    if not u: return False
    host = urlsplit(u).netloc
    if not in_scope(host, domains):
        if ext is not None: ext[host] += 1
        return False
    if u in rows or SKIP_EXT.search(urlsplit(u).path) or '/cdn-cgi/' in u: return False
    rows[u] = dict.fromkeys(FIELDS, ''); rows[u].update(url=u, host=host, source=source); return True

def robots(host):
    if host not in _robots:
        rp = robotparser.RobotFileParser(); sm = []
        try:
            r = S.get(f"https://{host}/robots.txt", timeout=15)
            lines = r.text.splitlines() if r.status_code == 200 and '<html' not in r.text[:300].lower() else []
        except requests.RequestException: lines = []
        rp.parse(lines); sm = [l.split(':', 1)[1].strip() for l in lines if l.lower().startswith('sitemap:')]
        _robots[host] = (rp, sm)
    return _robots[host]

def allowed(url): return robots(urlsplit(url).netloc)[0].can_fetch('*', url)

def _get_sitemap(sm):
    try:
        r = S.get(sm, timeout=30); body = r.content
        if r.status_code != 200: return sm, None
        if body[:2] == bytes([31, 139]): body = gzip.decompress(body)
        return sm, body.decode('utf-8', 'ignore')
    except Exception: return sm, None

def read_sitemaps(host, rows, domains, ext, log, cap=1500):
    queue = list(dict.fromkeys(robots(host)[1] + [f"https://{host}/sitemap.xml", f"https://{host}/sitemap_index.xml"]))
    done = set(); stats = []
    while queue and len(done) < cap:
        batch = [q for q in dict.fromkeys(queue) if q not in done][:min(48, cap - len(done))]; queue = [q for q in queue if q not in batch]
        if not batch: break
        done.update(batch)
        with ThreadPoolExecutor(6) as ex: res = list(ex.map(_get_sitemap, batch))
        for sm, text in res:
            if not text: continue
            locs = [re.sub(r'<![[]CDATA[[]|[]][]]>', '', x).strip().replace('&amp;', '&') for x in re.findall(r'<loc>(.*?)</loc>', text, re.S)]
            if '<sitemapindex' in text[:2000]: queue += locs; continue
            stats.append((sm.rsplit('/', 1)[-1], len(locs), sum(add(rows, u, 'sitemap:' + sm.rsplit('/', 1)[-1], domains, ext) for u in locs)))
    stats.sort(key=lambda x: -x[1])
    for name, a, b in stats[:25]: log.append(f"| {host} | {name} | {a} | {b} |")
    if len(stats) > 25: log.append(f"| {host} | 그 외 사이트맵 파일 {len(stats) - 25}개 | {sum(x[1] for x in stats[25:])} | {sum(x[2] for x in stats[25:])} |")
    left = len([q for q in set(queue) if q not in done])
    if left: log.append(f"| {host} | (주의) 상한 {cap}개에 걸려 못 연 사이트맵 파일 {left}개: --sitemap-cap 을 올려 다시 실행 | 0 | 0 |")

# ---------- 브라우저 렌더링: 스크롤, 메뉴 hover, 탭과 아코디언과 더보기 클릭 ----------
MARK_JS = """([limit, hub, deep]) => { const re=/^(show|view|see|load|read) +(more|all)|^more$|더 *보기|전체 *보기|펼치기|자세히/i; let n=0; const per=new Map();
 const bad=e=>e.closest('form,[role=dialog],[id*=onetrust],[class*=cookie]')||(!hub&&e.closest('header,nav,footer'));
 const vis=e=>{const r=e.getBoundingClientRect(); return r.width>=16&&r.height>=12&&r.width*r.height<innerWidth*innerHeight*0.7;};
 const mark=e=>{ if(n>=limit||e.hasAttribute('data-sw')) return; const p=e.parentElement, c=per.get(p)||0; if(c>=6) return; per.set(p,c+1); e.setAttribute('data-sw','s'+(n++)); };
 // 1) 표준 방식: 아코디언, 탭, 펼침 버튼, 더보기
 for (const e of document.querySelectorAll('details:not([open])>summary,[aria-expanded=false],[role=tab]:not([aria-selected=true]),button,[role=button]')) {
  const a=e.closest('a[href]'); if (a && !(a.getAttribute('href')||'').startsWith('#')) continue;
  const structural=e.matches('summary,[aria-expanded=false],[role=tab]'); const t=(e.innerText||'').trim();
  if (!structural && !re.test(t)) continue;
  if (bad(e)||e.matches('[role=combobox],[aria-haspopup=listbox],[aria-haspopup=dialog]')||!vis(e)) continue; mark(e); }
 // 2) 표시 없이 만든 누르는 요소: 손가락 커서가 시작되는 요소(카드, 칩, 전환 버튼). 링크와 입력 칸은 제외
 if (deep) for (const e of document.querySelectorAll('body *')) { if (n>=limit) break;
  if (getComputedStyle(e).cursor!=='pointer'||(e.parentElement&&getComputedStyle(e.parentElement).cursor==='pointer')) continue;
  if (e.closest('a[href],label,select,input,textarea,video,[data-sw]')||e.querySelector('[data-sw]')||bad(e)||!vis(e)) continue;
  if (!((e.innerText||'').trim()||e.getAttribute('aria-label'))) continue; mark(e); }
 return n; }"""
CLICK_JS = """i => { const e=document.querySelector(`[data-sw=s${i}]`); if(!e) return null; e.scrollIntoView({block:'center'});
 const r=e.getBoundingClientRect(), t=document.elementFromPoint(r.left+r.width/2, r.top+r.height/2); (t&&e.contains(t)?t:e).click();
 return ((e.getAttribute('aria-label')||e.innerText||'').trim().split(String.fromCharCode(10))[0]||'').slice(0,60); }"""

class Browser:
    def __init__(self):
        from playwright.sync_api import sync_playwright
        self.pw = sync_playwright().start(); kw = {'headless': True}
        proxy = os.environ.get('HTTPS_PROXY') or os.environ.get('https_proxy')
        if proxy: kw['proxy'] = {'server': proxy}
        try: self.br = self.pw.chromium.launch(channel='chrome', **kw)
        except Exception: self.br = self.pw.chromium.launch(**kw)
        self.ctx = self.br.new_context(user_agent=UA, locale='en-US', viewport={'width': 1440, 'height': 900})

    def render(self, url, hub=False, clicks=30, deep=True):
        """본문은 처음 열었을 때 화면(스크롤 후). 누르거나 올려서 새로 보인 내용은 extra에 (누른 것 이름, 줄 목록)으로 따로 담는다."""
        pg = self.ctx.new_page(); links = set(); seen = set(); extra = []
        pg.on('popup', lambda p: p.close())
        def snap(ctx=False):
            try:
                links.update(pg.eval_on_selector_all('a[href]', 'e=>e.map(a=>a.href)'))
                lines = [l.strip() for l in pg.inner_text('body').splitlines() if l.strip()]
            except Exception: return []
            idx = [k for k, l in enumerate(lines) if l not in seen]; seen.update(lines)
            if not ctx: return [lines[k] for k in idx]
            return [lines[j] for j in sorted({j for k in idx for j in (k - 1, k) if j >= 0})][:60]  # 값만 바뀌는 칸은 앞줄(항목 이름)을 함께 남김
        try:
            resp = pg.goto(url, wait_until='domcontentloaded', timeout=45000); status = resp.status if resp else 0
            try: pg.wait_for_load_state('networkidle', timeout=4000)
            except Exception: pass
            pg.evaluate('async()=>{for(let y=0;y<document.body.scrollHeight;y+=1000){window.scrollTo(0,y);await new Promise(r=>setTimeout(r,80));}window.scrollTo(0,0);}')
            snap(); html = pg.content(); here = pg.url.split('#')[0]
            if hub:
                for el in pg.query_selector_all('header a, header button, nav a, nav button, [aria-haspopup]')[:25]:
                    try:
                        el.hover(timeout=400); pg.wait_for_timeout(100); new = snap(True)
                        if new: extra.append(('메뉴 ' + (el.inner_text() or '').strip().split('\n')[0][:40], new))
                    except Exception: pass
            n = pg.evaluate(MARK_JS, [clicks, hub, deep]); i = 0; navs = 0
            while i < n:
                try:
                    label = pg.evaluate(CLICK_JS, i); pg.wait_for_timeout(180)
                    if pg.url.split('#')[0] != here:  # 눌렀더니 다른 페이지로 이동: 주소를 링크로 기록하고 돌아옴
                        links.add(pg.url); navs += 1
                        pg.goto(here, wait_until='domcontentloaded', timeout=30000); pg.wait_for_timeout(700)
                        if navs >= 4: break
                        n = pg.evaluate(MARK_JS, [clicks, hub, deep])
                    else:
                        new = snap(True)
                        if new and label is not None: extra.append((label, new))
                except Exception: pass
                i += 1
            return status, html, links, extra, pg.url
        finally: pg.close()

    def close(self):
        try: self.br.close(); self.pw.stop()
        except Exception: pass

# ---------- HTML > 마크다운 ----------
def extract(html, url, extra=()):
    soup = BeautifulSoup(html, 'lxml')
    title = soup.title.get_text(' ', strip=True) if soup.title else ''
    d = soup.find('meta', attrs={'name': 'description'}) or soup.find('meta', attrs={'property': 'og:description'})
    desc = (d.get('content') or '').strip() if d else ''
    links = {urljoin(url, a['href']) for a in soup.find_all('a', href=True)}
    ld = [s.get_text() for s in soup.find_all('script', type='application/ld+json')]
    for t in soup(['script', 'style', 'noscript', 'svg', 'iframe', 'template']): t.decompose()
    for v in soup.find_all(['video', 'audio']): v.replace_with(' [영상] ')
    for img in soup.find_all('img'): img.replace_with(f" [그림: {img.get('alt')}] " if img.get('alt') else '')
    main = soup.find('main') or soup.find(attrs={'role': 'main'}) or soup.find('article')
    if not main:
        main = soup.body or soup
        for t in main.find_all(['header', 'nav', 'footer']): t.decompose()
    for el in main.find_all('a', href=True):
        n = norm(urljoin(url, el['href']))
        if n: el['href'] = n
    md = re.sub(r'\n{3,}', '\n\n', markdownify(str(main), heading_style='ATX')).strip()
    flat = ' '.join(md.split())
    blocks = []; total = 0
    for label, lines in extra:  # 누른 것마다 한 덩어리: 본문에 없는 줄이 하나라도 있을 때만 남김
        if total >= 400 or not any(len(l) > 1 and l not in flat for l in lines): continue
        blocks.append('### ' + (label or '이름 없는 요소') + ' 누른 뒤\n\n' + '\n'.join('- ' + l for l in lines)); total += len(lines)
    if blocks: md += '\n\n## 펼치거나 눌러야 보이던 내용\n\n' + '\n\n'.join(blocks)
    ld = [x.strip() for x in ld if 20 < len(x) < 8000]
    if ld: md += '\n\n## 구조화 데이터(JSON-LD)\n\n' + FENCE + 'json\n' + '\n'.join(ld)[:8000] + '\n' + FENCE
    return title, desc, md, links

def slug(url):
    p = urlsplit(url); s = re.sub(r'[^A-Za-z0-9._-]+', '_', (p.path.strip('/') or 'index').replace('/', '__'))[:120]
    return s + ('_' + hashlib.sha1(p.query.encode()).hexdigest()[:6] if p.query else '')

def write_raw(work, row, title, desc, md, method):
    d = os.path.join(work, 'raw', row['host']); os.makedirs(d, exist_ok=True); name = slug(row['url'])
    head = f"---\nurl: {row['url']}\ntitle: {title}\ndescription: {desc}\nfetched: {time.strftime('%Y-%m-%d')}\nmethod: {method}\nplan: {row['plan']}\n---\n\n"
    path = os.path.join(d, name + '.md'); open(path, 'w', encoding='utf-8').write(head + md)
    row.update(status='ok', method=method, chars=str(len(md)), title=title[:200], file=os.path.relpath(path, work))

def fetch_static(url):
    try: r = S.get(url, timeout=25)
    except requests.RequestException as e: return ('error', str(e)[:120], None)
    return ('ok', '', r)

# ---------- 명령 ----------
def cmd_map(a):
    rows = load(a.work); ext = collections.Counter(); log = []; os.makedirs(a.work, exist_ok=True); sp = os.path.join(a.work, 'scope.json')
    old = json.load(open(sp, encoding='utf-8')) if os.path.exists(sp) else {'domains': [], 'seeds': []}
    domains = list(dict.fromkeys(old['domains'] + a.domain)); json.dump({'domains': domains, 'seeds': list(dict.fromkeys(old['seeds'] + a.seed))}, open(sp, 'w', encoding='utf-8'))
    hosts = list(dict.fromkeys(urlsplit(norm(s)).netloc for s in a.seed)); done = set(); br = None if a.no_render else Browser()
    cands = []; hidden = 0
    for dom in domains:  # 인증서 공개 기록에서 하위 사이트 후보 찾기: 공개용이 분명한 것만 바로 훑고 나머지는 후보로만 기록
        try:
            for e in S.get(f"https://crt.sh/?q=%25.{dom}&output=json", timeout=25).json():
                for h in e.get('name_value', '').lower().split('\n'):
                    if '*' in h or not in_scope(h, domains) or h in hosts or h in cands: continue
                    if INTERNAL.search(h): hidden += 1
                    elif h.split('.')[0] in PUBLIC: hosts.append(h)
                    else: cands.append(h)
        except Exception: pass
    while hosts and len(done) < a.max_hosts:
        host = hosts.pop(0)
        if host in done: continue
        done.add(host); before = len(rows)
        try:
            r = S.get(f"https://{host}/", timeout=8)
            if r.status_code >= 400 and r.status_code not in (401, 403): log.append(f"| {host} | (접속 불가 {r.status_code}) | 0 | 0 |"); continue
        except requests.RequestException: log.append(f"| {host} | (접속 불가) | 0 | 0 |"); continue
        add(rows, f"https://{host}/", 'seed', domains, ext); read_sitemaps(host, rows, domains, ext, log, a.sitemap_cap)
        links = set()
        if br:
            try: links = br.render(f"https://{host}/", hub=True)[2]
            except Exception as e: log.append(f"| {host} | (첫 화면 렌더링 실패 {str(e)[:60]}) | 0 | 0 |")
        else:
            try: links = extract(r.text, r.url)[3]
            except Exception: pass
        n = sum(add(rows, u, 'homepage', domains, ext) for u in links)
        log.append(f"| {host} | 첫 화면과 메뉴 링크 | {len(links)} | {n} |")
        for u in list(rows)[before:]:
            h = rows[u]['host']
            if h not in done and h not in hosts: hosts.append(h)
    if br: br.close()
    save(a.work, rows)
    with open(os.path.join(a.work, 'map_log.md'), 'a', encoding='utf-8') as f:
        f.write(f"\n\n# map 실행 {time.strftime('%Y-%m-%d %H:%M')} (seed: {', '.join(a.seed)})\n\n| 호스트 | 출처 | 발견 URL | 신규 |\n|---|---|---|---|\n" + '\n'.join(log))
        f.write('\n\n## 아직 훑지 않은 하위 사이트 후보 (공개용이면 --seed 로 추가해 map 재실행)\n' + '\n'.join('- ' + h for h in hosts + [c for c in cands if c not in done]))
        f.write(f"\n\n시험용이나 내부용으로 보여 후보에서 뺀 호스트: {hidden}개")
        f.write('\n\n## 사이트가 링크한 외부 호스트(회사 소유 여부 판단 대상)\n' + '\n'.join(f"- {h}: {c}" for h, c in ext.most_common(60)))
    print(f"URL {len(rows)}개, 호스트 {len(done)}개. 상세: {a.work}/map_log.md"); cmd_plan(a)

def settings(a):  # 계획 설정과 URL 패턴 지정을 overrides.json에 남겨 이후 명령에서도 같은 계획이 유지되게 함
    op = os.path.join(a.work, 'overrides.json'); ov = json.load(open(op, encoding='utf-8')) if os.path.exists(op) else {}
    st = ov.setdefault('settings', {})
    for k, dflt in (('template_min', 40), ('sample', 5), ('skim_cap', 40), ('read_all_under', 300), ('locales', ',en-us,en,en-gb,ko-kr,ko')):
        if getattr(a, k, None) is not None: st[k] = getattr(a, k)
        setattr(a, k, st.get(k, dflt))
    for k in ('read', 'skim', 'list', 'skip'):
        for pat in getattr(a, k, None) or []:
            for kk in ('read', 'skim', 'list', 'skip'): ov[kk] = [x for x in ov.get(kk, []) if x != pat]
            ov[k].append(pat)
    os.makedirs(a.work, exist_ok=True); json.dump(ov, open(op, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    return ov

def classify(rows, a):
    ov = settings(a)
    pref = [x.strip().lower() for x in a.locales.split(',')]; keys = collections.defaultdict(list)
    # 언어판과 국가판 접두어 판별: 2글자(또는 xx-yy) 첫 마디 가운데, 그 아래 경로의 절반 이상이 다른 판에도 있는 것
    cand = collections.defaultdict(set); seen = collections.Counter(); parsed = {}
    for r in rows.values():
        segs = [s for s in urlsplit(r['url']).path.split('/') if s]; parsed[r['url']] = segs
        if segs and LOCALE_RE.match(segs[0]): cand[(r['host'], segs[0].lower())].add('/'.join(segs[1:]))
        else: seen[(r['host'], '/'.join(segs))] += 1
    for (h, p), rems in cand.items():
        for x in rems: seen[(h, x)] += 1
    locs = {(h, p) for (h, p), rems in cand.items() if len(rems) >= 3 and sum(seen[(h, x)] >= 2 for x in rems) / len(rems) >= 0.5}
    hosts_with = {h for h, _ in locs}
    locs |= {(h, p) for (h, p) in cand if h in hosts_with and p.split('-')[0].split('_')[0] in LANGS}
    gkey = {}
    for r in rows.values():
        segs = parsed[r['url']]; loc = segs[0].lower() if segs and (r['host'], segs[0].lower()) in locs else ''
        rem = segs[1:] if loc else segs
        r['locale'] = loc; r['section'] = rem[0] if rem else '(home)'; gkey[r['url']] = (r['host'],) + tuple(rem[:-1])
        keys[(r['host'], '/'.join(rem), urlsplit(r['url']).query)].append(r)
    for _ in range(3):  # 같은 틀이 한 단계 더 깊이 반복되는 경우(예: /futures/<자산>/<통화>) 한 묶음으로 합침
        kids = collections.defaultdict(set)
        for k in set(gkey.values()):
            if len(k) > 2: kids[k[:-1]].add(k)
        wide = {p for p, ks in kids.items() if len(ks) >= 20}
        if not wide: break
        gkey = {u: (k[:-1] + ('*',) if len(k) > 2 and k[:-1] in wide and k[-1] != '*' else k) for u, k in gkey.items()}
    rank = lambda r: (pref.index(r['locale']) if r['locale'] in pref else 99, r['url'])
    groups = collections.defaultdict(list)
    for same in keys.values():
        same.sort(key=rank); keep = same[0]; keep['group'] = '/'.join(gkey[keep['url']]) + '/*'
        if keep['note'].startswith('언어판 중복'): keep['note'] = ''
        for r in same[1:]:
            r['group'] = keep['group']
            if not r['status']: r['plan'] = 'skip'; r['note'] = '언어판 중복: ' + keep['url']
        if keep['locale'] and keep['locale'] not in pref and not keep['note']: keep['note'] = f"특정 언어판에만 있는 페이지({keep['locale']})"
        groups[keep['group']].append(keep)
    small = sum(len(rs) for rs in groups.values()) <= a.read_all_under  # 작은 사이트는 전부 정독
    for g, rs in groups.items():
        rs.sort(key=lambda r: r['url']); big = not small and len(rs) >= a.template_min and g.count('/') > 1  # 최상위 바로 아래 페이지는 항상 정독
        pick = {round(i * (len(rs) - 1) / max(a.sample - 1, 1)) for i in range(a.sample)} if big else set()
        for i, r in enumerate(rs):
            if r['status']: continue
            r['plan'] = 'read' if not big or i in pick else 'skim'
        if big:
            for r in [r for r in rs if r['plan'] == 'skim' and not r['status']][a.skim_cap:]: r['plan'] = 'list'
    rx = {k: re.compile('|'.join(fnmatch.translate(p) for p in ov[k])) if ov.get(k) else None for k in ('list', 'skim', 'read', 'skip')}
    for r in rows.values():
        if r['status'] or r['note'].startswith('언어판 중복'): continue
        if r['note'] in ('수동 제외', 'robots.txt 수집 제외'): r['note'] = ''
        for plan in ('list', 'skim', 'read', 'skip'):  # 여러 패턴에 걸리면 뒤쪽이 우선: list < skim < read < skip
            if rx[plan] and rx[plan].match(r['url']):
                r['plan'] = plan
                if plan == 'skip': r['note'] = '수동 제외'
        if r['plan'] in ('read', 'skim') and not allowed(r['url']): r['plan'] = 'skip'; r['note'] = 'robots.txt 수집 제외'

def summary(rows):
    t = collections.defaultdict(collections.Counter)
    for r in rows.values(): t[(r['host'], r['section'])][r['plan'] or '미정'] += 1; t[(r['host'], r['section'])]['done'] += r['status'] == 'ok'
    out = ['| 호스트 | 구역 | 전체 | 정독(read) | 훑기(skim) | 목록만(list) | 제외(skip) | 수집완료 |', '|---|---|---|---|---|---|---|---|']
    for (h, s), c in sorted(t.items(), key=lambda kv: (kv[0][0], -sum(v for k, v in kv[1].items() if k != 'done'))):
        out.append(f"| {h} | {s} | {sum(v for k, v in c.items() if k != 'done')} | {c['read']} | {c['skim']} | {c['list']} | {c['skip']} | {c['done']} |")
    tot = collections.Counter(r['plan'] for r in rows.values())
    out.append(f"| 합계 |  | {len(rows)} | {tot['read']} | {tot['skim']} | {tot['list']} | {tot['skip']} | {sum(r['status'] == 'ok' for r in rows.values())} |")
    return '\n'.join(out)

def cmd_plan(a):
    rows = load(a.work)
    for u in a.add or []:  # 대상 도메인 밖의 문서(외부에 올린 투자설명서 PDF 등)를 낱개로 장부에 추가
        u = norm(u)
        if u and u not in rows: rows[u] = dict.fromkeys(FIELDS, ''); rows[u].update(url=u, host=urlsplit(u).netloc, source='manual')
    classify(rows, a); save(a.work, rows); s = summary(rows)
    open(os.path.join(a.work, 'plan_summary.md'), 'w', encoding='utf-8').write(s); print(s if len(s) < 9000 else s[:9000] + '\n... (전체: plan_summary.md)')

def cmd_fetch(a):
    rows = load(a.work); sp = os.path.join(a.work, 'scope.json')
    domains = a.domain or (json.load(open(sp, encoding='utf-8'))['domains'] if os.path.exists(sp) else sys.exit('scope.json 없음: map을 먼저 실행하거나 --domain 지정'))
    for r in rows.values():  # --refetch: 이미 받은 페이지를 다시 받기(누르기 규칙이 바뀌었거나 내용이 갱신됐을 때)
        if r['status'] and any(fnmatch.fnmatch(r['url'], p) for p in a.refetch or []): r.update(status='', method='', chars='', title='', file='')
    end = time.time() + a.minutes * 60; br = None; n = 0
    def finish(row, r_or_none):
        nonlocal br
        url = row['url']; method = 'static'; extra = []; html = ''; final = url
        if r_or_none is not None:
            r = r_or_none; final = r.url; ct = r.headers.get('content-type', '')
            if 'pdf' in ct or url.lower().endswith('.pdf'):
                fd = os.path.join(a.work, 'files'); os.makedirs(fd, exist_ok=True); fp = os.path.join(fd, slug(url) + '.pdf'); open(fp, 'wb').write(r.content)
                try:
                    from markitdown import MarkItDown
                    write_raw(a.work, row, os.path.basename(url), 'PDF', MarkItDown().convert(fp).text_content, 'pdf')
                except Exception as e: row.update(status='nonhtml', note=f"PDF 저장됨 {fp}, 변환 실패 {str(e)[:60]}")
                return
            if 'html' not in ct: row.update(status='nonhtml', note=ct[:60]); return
            html = r.text; blocked = r.status_code in (401, 403, 429, 503) or (len(html) < 6000 and BLOCK_HINT.search(html))
            if r.status_code == 404 or r.status_code == 410: row.update(status='gone', note=str(r.status_code)); return
        else: blocked = True
        title, desc, md, links = extract(html, final) if html and not blocked else ('', '', '', set())
        depth = len([x for x in urlsplit(url).path.split('/') if x]) - (1 if row['locale'] else 0)
        need = blocked or a.render == 'all' or (a.render == 'read' and row['plan'] == 'read') or len(md) < 500 or (
            a.render == 'auto' and row['plan'] == 'read' and (depth <= 2 or re.search('role=.?tab|load more|show more|view all|더보기', html, re.I)))
        if need and a.render != 'never':
            try:
                br = br or Browser(); st, html2, l2, extra, final = br.render(url, hub=row['section'] == '(home)', deep=a.click == 'deep')
                if st in (401, 403, 429, 503) or (len(html2) < 6000 and BLOCK_HINT.search(html2)): row.update(status='blocked', note=f"HTTP {st}"); return
                t2, d2, md2, l3 = extract(html2, final, extra)
                if len(md2) >= len(md) * 0.8: title, desc, md, method = t2 or title, d2 or desc, md2, 'render'
                links |= set(l2) | l3
            except Exception as e:
                if blocked: row.update(status='blocked', note=str(e)[:80]); return
                row['note'] = (row['note'] + ' 렌더링 실패').strip()
        elif blocked: row.update(status='blocked', note='정적 요청 차단'); return
        if norm(final) != url: row['note'] = (row['note'] + ' 이동: ' + norm(final)).strip()
        write_raw(a.work, row, title, desc, md, method)
        if len(md) < 300: row['status'] = 'thin'
        if sum(add(rows, u, 'link', domains) for u in links): dirty[0] = True
    dirty = [True]; first = [True]
    while time.time() < end:
        pick = lambda: [r for r in rows.values() if r['plan'] in ('read', 'skim') and not r['status'] and (not a.only or any(fnmatch.fnmatch(r['url'], p) for p in a.only))]
        if first[0]: classify(rows, a); first[0] = False; dirty[0] = False
        todo = pick()
        if not todo and dirty[0]: classify(rows, a); dirty[0] = False; todo = pick()
        todo.sort(key=lambda r: (r['plan'] != 'read', r['url']))
        if not todo or (a.limit and n >= a.limit): break
        batch = todo[:min(24, (a.limit - n) if a.limit else 24)]
        with ThreadPoolExecutor(4) as ex: res = list(ex.map(lambda r: fetch_static(r['url']), batch))
        for k, (row, (st, note, r)) in enumerate(zip(batch, res)):
            if time.time() > end: break  # 시간이 다 되면 남은 쪽은 대기로 두고 끝냄
            if st == 'error' and a.render == 'never': row.update(status='error', note=note); continue
            try: finish(row, r)
            except Exception as e: row.update(status='error', note=str(e)[:120])
            n += 1
            if k % 6 == 5: save(a.work, rows)  # 중간에 끊겨도 잃는 양이 적게 자주 저장
        save(a.work, rows); time.sleep(a.delay)
    if br: br.close()
    classify(rows, a); save(a.work, rows); c = collections.Counter(r['status'] or ('대기' if r['plan'] in ('read', 'skim') else '-') for r in rows.values())
    print(f"이번 실행 {n}건. 상태: {dict(c)}. 대기가 남아 있으면 같은 명령을 다시 실행.")

def cmd_digest(a):
    settings(a); rows = load(a.work); pd = os.path.join(a.work, 'packs'); os.makedirs(pd, exist_ok=True)
    for old in os.listdir(pd):  # 이전 묶음 지우고 새로 만듦
        if old.endswith('.md'): os.remove(os.path.join(pd, old))
    idx = ['| 묶음 | 정독 쪽수 | 훑기 쪽수 | 글자수 |', '|---|---|---|---|']
    by = collections.defaultdict(list); dup = {}
    for r in rows.values():
        if r['plan'] != 'skip': by[(r['host'], r['section'])].append(r)
    for (h, s), rs in sorted(by.items()):
        reads = [r for r in rs if r['plan'] == 'read' and r['file']]; skims = [r for r in rs if r['plan'] == 'skim']; lists = [r for r in rs if r['plan'] == 'list']
        parts = [[]]; size = 0
        for r in reads:
            body = open(os.path.join(a.work, r['file']), encoding='utf-8').read(); hsh = hashlib.sha1(body.split('---', 2)[-1].encode()).hexdigest()
            if hsh in dup: body = f"(본문이 {dup[hsh]} 과 같아 생략)"
            else: dup[hsh] = r['url']
            if size + len(body) > a.pack_chars and parts[-1]: parts.append([]); size = 0
            parts[-1].append(f"\n\n<<<PAGE {r['url']}>>>\n{body}"); size += len(body)
        tail = ''
        if skims:
            tail += '\n\n## 훑기 대상(같은 틀의 페이지 묶음): 조사 질문과 관련 있으면 read로 올려 다시 수집\n\n| URL | 제목 | 첫머리 |\n|---|---|---|\n'
            for r in skims:
                first = ''
                if r['file']:
                    t = open(os.path.join(a.work, r['file']), encoding='utf-8').read().split('---', 2)[-1]; first = ' '.join(t.replace('|', ' ').split())[:a.skim_chars]
                tail += f"| {r['url']} | {r['title'].replace('|', ' ')} | {first} |\n"
        if lists: tail += f"\n\n## 목록만 둔 URL {len(lists)}건 (inventory.csv에서 plan=list)\n" + '\n'.join('- ' + r['url'] for r in lists[:15]) + '\n- ...\n'
        for i, p in enumerate(parts):
            if not p and not tail: continue
            name = re.sub(r'[^A-Za-z0-9._()-]+', '_', f"{h}__{s}__{i + 1:02d}.md"); text = f"# 읽기 묶음: {h} / {s} ({i + 1}/{len(parts)})\n" + ''.join(p) + (tail if i == len(parts) - 1 else '')
            open(os.path.join(pd, name), 'w', encoding='utf-8').write(text); idx.append(f"| {name} | {len(p)} | {len(skims) if i == len(parts) - 1 else 0} | {len(text)} |")
    gr = collections.defaultdict(list)
    for r in rows.values():
        if r['plan'] != 'skip': gr[r['group']].append(r)
    gl = ['| 묶음(같은 경로 틀) | 전체 | 정독 | 훑기 | 목록만 | 서로 닮은 정도 | 판단 |', '|---|---|---|---|---|---|---|']
    for g, rs in sorted(gr.items(), key=lambda kv: -len(kv[1])):
        if len(rs) < a.template_min: continue
        got = [r for r in rs if r['file']][:10]; sets = [set(l.strip() for l in open(os.path.join(a.work, r['file']), encoding='utf-8').read().split('---', 2)[-1].splitlines() if len(l.strip()) > 20) for r in got]
        pairs = [len(x & y) / max(len(x | y), 1) for i, x in enumerate(sets) for y in sets[i + 1:]]; sim = sum(pairs) / len(pairs) if pairs else -1
        c = collections.Counter(r['plan'] for r in rs)
        verdict = '미수집' if sim < 0 else '같은 틀: 표본으로 충분' if sim >= 0.5 else '서로 다른 글: 제목 보고 관련 글을 read로 승격' if sim < 0.25 else '중간: 표본 2쪽 비교 후 결정'
        gl.append(f"| {g} | {len(rs)} | {c['read']} | {c['skim']} | {c['list']} | {'' if sim < 0 else round(sim, 2)} | {verdict} |")
    open(os.path.join(pd, '_groups.md'), 'w', encoding='utf-8').write('\n'.join(gl))
    open(os.path.join(pd, '_index.md'), 'w', encoding='utf-8').write('\n'.join(idx)); print('\n'.join(idx[:60])); print('\n'.join(gl[:40]))

def cmd_audit(a):
    rows = load(a.work); wiki = ''
    if a.wiki and os.path.isdir(a.wiki):
        for root, _, files in os.walk(a.wiki):
            for fn in files:
                if fn.endswith('.md'): wiki += open(os.path.join(root, fn), encoding='utf-8').read() + '\n'
    cited = lambda u: u in wiki or u.rstrip('/') + '/' in wiki
    reads = [r for r in rows.values() if r['plan'] == 'read']; out = ['# 수집과 반영 점검', '', summary(rows), '']
    for label, cond in (('수집 대기', lambda r: r['plan'] in ('read', 'skim') and not r['status']), ('차단', lambda r: r['status'] == 'blocked'),
                        ('오류', lambda r: r['status'] == 'error'), ('내용 거의 없음', lambda r: r['status'] == 'thin')):
        hit = [r for r in rows.values() if cond(r)]; out.append(f"## {label}: {len(hit)}건"); out += [f"- {r['url']} {r['note']}" for r in hit[:200]]
    if wiki:
        miss = [r for r in reads if r['status'] in ('ok', 'thin') and not cited(r['url'])]
        out.append(f"## 정독했으나 위키 어디에도 출처로 안 쓰인 페이지: {len(miss)}건 (반영하거나 coverage 메모에 사유 기록)"); out += [f"- {r['url']} ({r['title']})" for r in miss]
    text = '\n'.join(out); open(os.path.join(a.work, 'coverage.md'), 'w', encoding='utf-8').write(text); print(text[:6000])

QUOTES = str.maketrans({'\u2019': "'", '\u2018': "'", '\u201c': '"', '\u201d': '"', '\u2013': '-', '\u2014': '-', '\u00a0': ' ', '\u200b': '', '\u200c': '', '\u200d': '', '\ufeff': ''})
def flat_text(t):
    t = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', t)  # 링크는 보이는 글자만 남김
    return ' '.join(re.sub(r'[*_#>|`\\]', ' ', t).translate(QUOTES).lower().split())

def cmd_verify(a):
    """notes의 근거 구절이 수집한 원문에 실제로 있는지, 묶음의 페이지가 메모에 빠지지 않았는지 대조. 값싼 모델이 쓴 메모의 검수용."""
    rows = load(a.work); nd = a.notes or os.path.join(a.work, 'notes'); pd = os.path.join(a.work, 'packs'); cache = {}
    def page(url):
        r = rows.get(norm(url or ''))
        if not r or not r['file'] or not os.path.exists(os.path.join(a.work, r['file'])): return None
        if r['url'] not in cache: cache[r['url']] = flat_text(open(os.path.join(a.work, r['file']), encoding='utf-8').read())
        return cache[r['url']]
    table = ['| 메모 파일 | 묶음의 페이지 | 메모된 페이지 | 근거 줄 | 원문에 없는 근거 |', '|---|---|---|---|---|']; fails = []; missing = []; tot = bad = 0
    for fn in sorted(os.listdir(nd)) if os.path.isdir(nd) else []:
        if not fn.endswith('.md'): continue
        cur = None; n = b = 0; noted = set()
        for line in open(os.path.join(nd, fn), encoding='utf-8'):
            m = re.match(r'##\s+(https?://\S+)', line)
            if m: cur = norm(m.group(1)); noted.add(cur); continue
            m = re.search(r'근거\s*:\s*["\u201c](.+)["\u201d]\s*$', line.strip())
            if not m: continue
            n += 1; src = page(cur); parts = [flat_text(x) for x in re.split(r'\.\.\.|\u2026', m.group(1)) if len(x.strip()) >= 6]
            if src is None: b += 1; fails.append(f'- {fn} | {cur} | 원문 파일 없음 | "{m.group(1)[:90]}"')
            elif not parts or not all(x in src for x in parts): b += 1; fails.append(f'- {fn} | {cur} | "{m.group(1)[:90]}"')
        inpack = set()
        if os.path.exists(os.path.join(pd, fn)): inpack = {norm(u) for u in re.findall(r'<<<PAGE (\S+?)>>>', open(os.path.join(pd, fn), encoding='utf-8').read())}
        missing += [f'- {fn} | {u}' for u in sorted(inpack - noted)]
        tot += n; bad += b; table.append(f'| {fn} | {len(inpack)} | {len(noted)} | {n} | {b} |')
    text = '\n'.join(['# 메모 검수 (verify)', '', f'근거 줄 {tot}개 가운데 원문에서 못 찾은 것 {bad}개, 메모에 빠진 페이지 {len(missing)}쪽', ''] + table
                     + ['', '## 메모에 빠진 페이지 (묶음에는 있는데 메모에 절이 없음)'] + missing + ['', '## 원문에서 못 찾은 근거 (그 사실은 쓰지 말거나 원문에서 다시 확인)'] + fails)
    open(os.path.join(a.work, 'verify.md'), 'w', encoding='utf-8').write(text); print(text[:5000])

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('cmd', choices=['map', 'plan', 'fetch', 'digest', 'audit', 'verify']); ap.add_argument('--work', required=True)
    ap.add_argument('--domain', action='append', default=[]); ap.add_argument('--seed', action='append', default=[])
    ap.add_argument('--no-render', action='store_true'); ap.add_argument('--max-hosts', type=int, default=25); ap.add_argument('--sitemap-cap', type=int, default=1500)
    ap.add_argument('--locales'); ap.add_argument('--template-min', type=int)
    ap.add_argument('--sample', type=int); ap.add_argument('--read-all-under', type=int); ap.add_argument('--skim-cap', type=int)
    for k in ('read', 'skim', 'list', 'skip'): ap.add_argument('--' + k, action='append')
    ap.add_argument('--render', choices=['auto', 'read', 'thin', 'all', 'never'], default='auto'); ap.add_argument('--only', action='append'); ap.add_argument('--refetch', action='append'); ap.add_argument('--click', choices=['deep', 'basic'], default='deep'); ap.add_argument('--minutes', type=float, default=8)
    ap.add_argument('--limit', type=int, default=0); ap.add_argument('--delay', type=float, default=1.0)
    ap.add_argument('--pack-chars', type=int, default=120000); ap.add_argument('--skim-chars', type=int, default=240); ap.add_argument('--wiki'); ap.add_argument('--notes'); ap.add_argument('--add', action='append')
    a = ap.parse_args()
    try: sys.stdout.reconfigure(encoding='utf-8', errors='replace')  # Windows 콘솔에서 특수문자 출력 오류 방지
    except Exception: pass
    if a.cmd == 'map' and not (a.domain and a.seed): sys.exit('map에는 --domain 과 --seed 가 필요')
    {'map': cmd_map, 'plan': cmd_plan, 'fetch': cmd_fetch, 'digest': cmd_digest, 'audit': cmd_audit, 'verify': cmd_verify}[a.cmd](a)

if __name__ == '__main__': main()
