"""웹 화면 "브리핑" 탭 데이터: 엑셀 내보내기(tools/export_briefs_xlsx.py)와 같은 구성과 사진 배치.
사진은 web/brief_img/*.jpg로 줄여 두고 상대 경로로 참조(게시 때 files로 함께 올림)."""
import glob, os, re, sys
from PIL import Image as PILImage

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
_cwd = os.getcwd()
import export_briefs_xlsx as X  # noqa: E402  (모듈이 ROOT로 이동해 DB를 읽음)
os.chdir(_cwd)

IMG_DIR = os.path.join(ROOT, 'web', 'brief_img')


def web_img(path):
    os.makedirs(IMG_DIR, exist_ok=True)
    src = os.path.join(ROOT, path)
    name = os.path.basename(path).rsplit('.', 1)[0] + '.jpg'
    out = os.path.join(IMG_DIR, name)
    with PILImage.open(src) as im:
        w, h = im.size
        if not os.path.exists(out):
            s = min(900 / w, 1.0)
            im.convert('RGB').resize((int(w * s), int(h * s)), PILImage.LANCZOS).save(out, 'JPEG', quality=78, optimize=True)
    return 'brief_img/' + name


def img_block(path, what, note):
    return {'t': 'img', 'src': web_img(path), 'what': X.degap(what), 'note': X.degap(note)}


def line_block(level, text, ids, urls, hl):
    return {'t': 'p', 'lv': level, 'x': text.strip(), 'ids': ids, 'u': list(dict.fromkeys(urls)), 'hl': hl}


def company(co):
    md = open(os.path.join(ROOT, f'briefs/{co}.md'), encoding='utf-8').read()
    out, placed = [], set()
    pillar_caps = sorted(p for p in glob.glob(os.path.join(ROOT, 'captures/pillars/*.png')) if os.path.basename(p).startswith(co + '_'))
    pillar_caps = [os.path.relpath(p, ROOT) for p in pillar_caps]

    def flush():
        todo = [p for p in pillar_caps if p not in placed]
        if not todo:
            return
        out.append({'t': 'h4', 'x': '전략 틀 원문 캡처'})
        for p in sorted(todo, key=lambda p: X.PILLAR_ORDER.get(os.path.basename(p)[:-4], 99)):
            placed.add(p)
            k = os.path.basename(p)[:-4]
            out.append(img_block(p, X.PILLAR_DESC.get(k, k), X.NOTES.get(k, '')))

    in3 = False
    for raw in md.split('\n'):
        line = raw.rstrip()
        if not line.strip() or line.startswith('# '):
            continue
        if line.startswith('## '):
            if in3:
                flush(); in3 = False
            out.append({'t': 'h2', 'x': line[3:].strip()})
            continue
        if line.startswith('### '):
            if in3:
                flush()
            in3 = line[4:].strip().startswith('3.')
            out.append({'t': 'h3', 'x': line[4:].strip()})
            continue
        if line.startswith('|'):
            cells = [c.strip() for c in line.strip('|').split('|')]
            if all(re.fullmatch(r':?-{2,}:?', c) for c in cells if c):
                continue
            text, ids, urls, hl = X.clean('  |  '.join(cells))
            out.append(line_block('표', text, ids, urls, hl))
            continue
        m = re.match(r'^(\s*)-\s+(.*)$', line)
        if m:
            depth = len(m.group(1)) // 2
            level = ['•', '-', '--'][min(depth, 2)]
            text, ids, urls, hl = X.clean(m.group(2))
        else:
            level, (text, ids, urls, hl) = '', X.clean(line)
        out.append(line_block(level, text, ids, urls, hl or text.strip().startswith('축 :')))
        for fid in ids:
            for cap in X.CAP_OF_FACT.get(fid, []):
                if cap in placed or '/pillars/' in cap:
                    continue
                placed.add(cap)
                out.append(img_block(cap, X.CAP_TITLE.get(cap, os.path.basename(cap)),
                                     f'{fid} : ' + (X.FACTS.get(fid, {}).get('무엇을') or '')[:300]))
    if in3:
        flush()
    rest = []
    for fid, caps in X.CAP_OF_FACT.items():
        if not any((X.FACTS.get(fid, {}).get('회사') or '').startswith(k) for k in X.CO_KEYS[co]):
            continue
        rest += [(fid, c) for c in caps if c not in placed and '/pillars/' not in c]
    left = [p for p in pillar_caps if p not in placed]
    if rest or left:
        out.append({'t': 'h2', 'x': '참고 캡처'})
        for p in left:
            placed.add(p)
            k = os.path.basename(p)[:-4]
            out.append(img_block(p, X.PILLAR_DESC.get(k, k), X.NOTES.get(k, '')))
        for fid, cap in rest:
            if cap in placed:
                continue
            placed.add(cap)
            out.append(img_block(cap, X.CAP_TITLE.get(cap, os.path.basename(cap)),
                                 f'{fid} : ' + (X.FACTS.get(fid, {}).get('무엇을') or '')[:300]))
    return out


def table(md_path, start, end):
    t = open(os.path.join(ROOT, md_path), encoding='utf-8').read()
    if start in t:
        t = t[t.index(start):]
    if end and end in t:
        t = t[:t.index(end)]
    rows = [[X.clean(c.strip())[0] for c in l.strip('|').split('|')] for l in t.split('\n') if l.startswith('|')]
    return [r for r in rows if not all(re.fullmatch(r':?-{2,}:?', c) for c in r if c)]


def ats():
    out = []
    for name, md, pre in X.ATS:
        out.append({'t': 'h2', 'x': name})
        p = os.path.join(ROOT, f'work/PILLARS/{md}.md')
        if os.path.exists(p):
            for l in open(p, encoding='utf-8').read().split('\n'):
                if not l.startswith('|'):
                    continue
                cells = [c.strip() for c in l.strip('|').split('|')]
                if all(re.fullmatch(r':?-{2,}:?', c) for c in cells if c):
                    continue
                text, ids, urls, hl = X.clean('  |  '.join(cells))
                text = re.sub(r'(?:확인하지 못함|확인 못 함|공개 없음|미확인|찾지 못함)[^|]*', '', text)
                text = re.sub(r'(?:금액|매출|수치)?\s*비공개,?\s*', '', text)
                urls = urls + re.findall(r'https?://[^\s)]+', text)
                text = re.sub(r'\(?https?://[^\s)]+\)?', '', text).replace('()', '')
                out.append(line_block('표', text, ids, urls, False))
        for cap in sorted(glob.glob(os.path.join(ROOT, f'captures/pillars/{pre}_*.png')), key=lambda x: X.PILLAR_ORDER.get(os.path.basename(x)[:-4], 99)):
            k = os.path.basename(cap)[:-4]
            out.append(img_block(os.path.relpath(cap, ROOT), X.PILLAR_DESC.get(k, k), X.NOTES.get(k, '')))
    return out


def build():
    cwd = os.getcwd()
    os.chdir(ROOT)
    try:
        pt = open('briefs/00_전략틀_비교.md', encoding='utf-8').read()
        read = []
        if '## 읽는 법' in pt:
            read = [x[2:] for x in pt[pt.index('## 읽는 법'):].split('## 주요 캡처')[0].split('\n') if x.startswith('- ')]
        return {
            'axes': table('axes.md', '## 승인된 축', '\n---\n'),
            'pillars': table('briefs/00_전략틀_비교.md', '## 한눈에', '## 읽는 법'),
            'pillars_read': read,
            'cos': [{'name': c, 'blocks': company(c)} for c in X.COS],
            'ats': ats(),
        }
    finally:
        os.chdir(cwd)


if __name__ == '__main__':
    d = build()
    print({c['name']: (len(c['blocks']), sum(1 for b in c['blocks'] if b['t'] == 'img')) for c in d['cos']}, len(os.listdir(IMG_DIR)))
