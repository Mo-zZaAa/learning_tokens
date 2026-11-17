"""0단계 현황표: 내용은 고치지 않고 세기만 함.
입력: web/index.html의 내장 데이터(D), briefs/*.md, db/facts.csv, discussion/log.jsonl
출력: work/STAGE0/*.csv, work/STAGE0/STAGE0_현황표.xlsx, 요약 숫자는 표준 출력
"""
import csv, glob, json, os, re, sys
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
OUT = 'work/STAGE0'
os.makedirs(OUT, exist_ok=True)

html = open('web/index.html', encoding='utf-8').read()
D = json.loads(re.search(r'<script id="data" type="application/json">(.*?)</script>', html, re.S).group(1).replace('<\\/', '</'))
FACTS = {r['fact_id']: r for r in csv.DictReader(open('db/facts.csv', encoding='utf-8'))}

COS = [('kraken', 'Kraken', 2011, r'Kraken|Payward'), ('robinhood', 'Robinhood', 2013, r'Robinhood'),
       ('binance', 'Binance', 2017, r'Binance'), ('coinbase', 'Coinbase', 2012, r'Coinbase'),
       ('dinari', 'Dinari', 2021, r'Dinari'), ('ondo', 'Ondo', 2021, r'Ondo')]
CO_OF = {s: n for s, n, _, _ in COS}


def wcsv(name, head, rows):
    with open(f'{OUT}/{name}.csv', 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f); w.writerow(head); w.writerows(rows)
    return name, head, rows


def strip_q(t):
    """인용부호 안 글자는 뺌(원문 인용은 규칙 대상 아님)"""
    return re.sub(r'"[^"]*"|“[^”]*”|‘[^’]*’', ' ', t or '')


# ---------- 화면별 글줄 모으기 ----------
LINES = []  # (화면, 회사, 위치, 섹션, 글)
for c in D['companies']:
    if c['slug'] not in CO_OF:
        continue
    for sec in c['sections']:
        for r in sec['rows']:
            t = ((r.get('label') or '') + ' : ' + (r.get('text') or '')).strip(' :')
            LINES.append(('본문', CO_OF[c['slug']], r['id'], sec['code'], t, r.get('ids') or []))
BRIEF_FILES = {n: f'briefs/{n}.md' for _, n, _, _ in COS}
DOCS = {'핵심': 'briefs/00_브리핑_핵심_261117.md', '회사별 전략': 'briefs/00_전략_한눈에.md', '거래소 3곳 비교': 'briefs/KDX_가상자산거래소3곳_비교브리핑_261117.md',
        '파트별 해외 사례': 'briefs/KDX_스토리라인_파트별_해외사례_261117.md', '질문과 답': 'briefs/PM_질문과_짚을점_261117.md'}


def co_of_text(t, default=''):
    hits = [n for _, n, _, pat in COS if re.search(pat, t)]
    return hits[0] if len(hits) == 1 else default


for n, p in BRIEF_FILES.items():
    sec = ''
    for i, l in enumerate(open(p, encoding='utf-8').read().split('\n'), 1):
        if l.startswith('#'):
            sec = l.lstrip('#').strip()[:30]
            continue
        if l.strip():
            LINES.append(('브리핑', n, f'{p}:{i}', sec, l.strip(), re.findall(r'F-\d{4}', l)))
for scr, p in DOCS.items():
    sec, cur = '', ''
    for i, l in enumerate(open(p, encoding='utf-8').read().split('\n'), 1):
        m = re.match(r'^(?:#+\s*)?(?:\d+\.\s+)?(Kraken|Binance|Coinbase|Robinhood|Dinari|Ondo)\b', l)
        if m and (l.startswith('#') or scr == '핵심'):
            cur = m.group(1)
        if l.startswith('#'):
            sec = l.lstrip('#').strip()[:30]
        if l.strip():
            LINES.append((scr, co_of_text(l, cur), f'{p}:{i}', sec, l.strip(), re.findall(r'F-\d{4}', l)))

# ---------- 1) 미사용 사실 ----------
Dx = {k: v for k, v in D.items() if k != 'facts'}
all_text = json.dumps(Dx, ensure_ascii=False) + ''.join(open(p, encoding='utf-8').read() for p in glob.glob('briefs/*.md') + glob.glob('kb/*.md') + glob.glob('kb/*.csv'))
used = set(re.findall(r'F-\d{4}', all_text))
unused = []
for fid, f in FACTS.items():
    if fid in used:
        continue
    co = co_of_text(f.get('회사') or '', (f.get('회사') or '')[:20])
    topic = (f.get('틀 항목') or '').split('>')[0].strip() or (f.get('밸류체인 위치') or '').strip() or '(분류 없음)'
    unused.append([fid, co, topic, f.get('기준일') or f.get('시작(연월)') or '', (f.get('무엇을') or '')[:160], f.get('검증 상태') or '', (f.get('링크') or '')[:120]])
unused.sort(key=lambda r: (r[1], r[2], r[0]))
T_UNUSED = wcsv('1_미사용사실', ['사실 번호', '회사', '주제(틀 항목)', '날짜', '무엇을', '검증 상태', '링크'], unused)
unused_by_co = Counter(r[1] for r in unused)

# ---------- 2) 연도별 행 수와 빈 해 ----------
year_rows = []
gap_rows = []
for slug, n, founded, _ in COS:
    body = [l for l in LINES if l[0] == '본문' and l[1] == n]
    cnt = Counter(); only_recent = 0; with_year = 0
    for l in body:
        ys = {int(y) for y in re.findall(r'(?<!\d)(20[01]\d|202[0-6])(?!\d)', l[4])}
        if ys:
            with_year += 1
            if ys <= {2025, 2026}:
                only_recent += 1
        for y in ys:
            cnt[y] += 1
    allscr = Counter()
    for l in LINES:
        if l[1] == n:
            for y in {int(y) for y in re.findall(r'(?<!\d)(20[01]\d|202[0-6])(?!\d)', l[4])}:
                allscr[y] += 1
    for y in range(founded, 2027):
        year_rows.append([n, y, cnt.get(y, 0), allscr.get(y, 0)])
    empty = [y for y in range(founded, 2027) if not cnt.get(y)]
    empty_all = [y for y in range(founded, 2027) if not allscr.get(y)]
    gap_rows.append([n, founded, with_year, only_recent, f'{only_recent / max(with_year, 1) * 100:.0f}%', ', '.join(map(str, empty)) or '없음', ', '.join(map(str, empty_all)) or '없음'])
T_YEAR = wcsv('2a_연도별_행수', ['회사', '연도', '본문 행 수', '모든 화면 행 수'], year_rows)
T_GAP = wcsv('2b_빈해', ['회사', '설립', '연도가 적힌 본문 행', '2025, 2026만 다룬 행', '비율', '본문에 한 줄도 없는 해', '모든 화면에 한 줄도 없는 해'], gap_rows)

# ---------- 3) 리서치 지침 4-2의 말 ----------
WORDS = ['제공', '지원', '인프라', '확대', '강화', '통합', '연결', '플랫폼', '서비스', '확보']
TRANS = ['지갑판', '한 벌', '일습', '쇼핑 목록', '추적 증권']
word_rows = []; word_cnt = defaultdict(Counter)
for scr, co, loc, sec, t, _ in LINES:
    if not co:
        continue
    tt = strip_q(t)
    if re.match(r'^\s*(①|원문|- 원문)', t):
        continue
    hit = [w for w in WORDS + TRANS if w in tt]
    if hit:
        for w in hit:
            word_cnt[(co, scr)][w] += 1
        word_rows.append([co, scr, loc, sec, ', '.join(hit), t[:180]])
T_WORDS = wcsv('3_지침4-2의_말', ['회사', '화면', '줄 번호 또는 파일:줄', '섹션', '나온 말', '문장'], word_rows)
wsum = [[co, scr] + [word_cnt[(co, scr)].get(w, 0) for w in WORDS + TRANS] for (co, scr) in sorted(word_cnt)]
T_WSUM = wcsv('3b_말_집계', ['회사', '화면'] + WORDS + TRANS, wsum)

# ---------- 4) 같은 주제가 흩어진 곳과 값이 갈리는 곳 ----------
TOPICS = {
    'Kraken': ['Backed', 'NinjaTrader', 'Nasdaq', 'Bitnomial', 'Small Exchange', 'Crypto Facilities', 'Reap', '키프로스', 'GTN', 'Payward Services', 'SPDI', 'Saldo', 'LSE', 'xPO', '독일거래소'],
    'Binance': ['bStocks', 'JEX', 'ADGM|아부다비', '고팍스', 'MGX', 'Alpaca', '무기한선물'],
    'Coinbase': ['Base', 'USDC', 'Deribit', 'FairX', 'Keystone', '청산소', 'Kalshi', 'Apex'],
    'Robinhood': ['Bitstamp', 'MIAXdx', 'Kalshi', 'WonderFi', 'TradePMR', 'X1', 'Gold', '지갑판', 'RVI', 'Robinhood Chain'],
    'Dinari': ['tZERO', 'Alpaca', '명의개서', 'Broadridge', '카카오페이', 'DFN|Dinari Financial Network', 'Flow Traders'],
    'Ondo': ['OUSG', 'USDY', 'Oasis Pro', 'BVI|Global Markets', 'Ondo Network', 'Perps', 'Ondo Chain', 'BUIDL'],
}
MONEY = re.compile(r'(\d[\d,.]*\s?(?:억|조|만)\s?달러|\d[\d,.]*\s?(?:billion|million))')
DATE = re.compile(r'(?<!\d)(20[012]\d-\d\d)(?!\d)')
spread_rows, value_rows = [], []
for co, tops in TOPICS.items():
    for tp in tops:
        pat = re.compile(tp)
        hits = [l for l in LINES if l[1] == co and pat.search(l[4])]
        if not hits:
            continue
        by_scr = Counter(l[0] for l in hits)
        secs = {(l[0], l[3]) for l in hits}
        body_ids = [l[2] for l in hits if l[0] == '본문']
        spread_rows.append([co, tp, len(hits), len(secs), ', '.join(f'{k} {v}' for k, v in by_scr.most_common()),
                            len({l[3] for l in hits if l[0] == '본문'}), ' '.join(body_ids[:40])])
        # 같은 주제 줄의 날짜와 금액(같은 줄 안). 화면마다 집합을 비교
        dates, money = defaultdict(set), defaultdict(set)
        for l in hits:
            for d in DATE.findall(l[4]):
                dates[d].add(l[0])
            for m in MONEY.findall(l[4]):
                money[re.sub(r'\s', '', m)].add(l[0])
        for kind, dd in (('날짜', dates), ('금액', money)):
            for v, scrs in sorted(dd.items()):
                value_rows.append([co, tp, kind, v, len(scrs), ', '.join(sorted(scrs)), '모든 화면' if len(scrs) == len(by_scr) else ''])
T_SPREAD = wcsv('4a_주제별_흩어짐', ['회사', '주제', '언급 줄 수', '걸친 (화면, 섹션) 수', '화면별 줄 수', '본문 섹션 수', '본문 줄 번호'], spread_rows)
T_VALUES = wcsv('4b_주제별_날짜와_금액', ['회사', '주제', '종류', '값', '나온 화면 수', '나온 화면', '비고'], value_rows)

# ---------- 5) 부록 B의 엇갈림 확인 ----------
def find(pat, scr=None, co=None):
    return [(l[0], l[2], l[4][:150]) for l in LINES if re.search(pat, l[4]) and (scr is None or l[0] == scr) and (co is None or l[1] == co)]
X = []
for code, desc, pat, co in [
    ('X1', 'Kraken 인가 목적 인수 수(6건 중 4건, 5건)', r'(6건 중 4건|인가 목적.{0,10}\d건|인가가 주목적인 인수가 \d건|인수 \d건)', None),
    ('X2', 'Robinhood 선물 중개 확보 방식(직접 2024-10, 인수)', r'(선물 중개|FCM).{0,40}(2024|인수|직접)|(2024-10).{0,30}선물', 'Robinhood'),
    ('X3', 'Kraken 거래 비중 표현(거래 기반 48%, 거래 수수료 48%)', r'(거래 기반|거래 수수료|거래).{0,6}48%', 'Kraken'),
    ('X4', 'Coinbase 앱 주식 2026-02(출시, 전체 공개)', r'2026-02.{0,40}(주식|종목)|(주식|종목).{0,40}2026-02', 'Coinbase'),
    ('X5', 'Coinbase 청산소 등록 시점', r'청산소.{0,40}(20\d\d)|(20\d\d).{0,20}청산소', 'Coinbase'),
    ('E1', '부록: Kraken 키프로스 날짜', r'키프로스', 'Kraken'),
    ('E5', '부록: Kraken GTN 방향', r'GTN', 'Kraken'),
]:
    for scr, loc, t in find(pat, co=co):
        X.append([code, desc, scr, loc, t])
T_X = wcsv('5_엇갈림_후보', ['번호', '내용', '화면', '위치', '문장'], X)

# ---------- 6) 부록 A 질문별 지금 위치 ----------
QS = [
    ('Kraken', 'K1', '자체 지표 세 구분(거래, 자산, 접근 기반)', r'자산 기반|접근 기반|거래 기반|TPM|총플랫폼'),
    ('Kraken', 'K2', '2011~2018 무엇을 팔았나', r'(?<!\d)201[1-8](?!\d)'),
    ('Kraken', 'K3', 'Binance에 밀린 이유와 확장 전환 시점', r'(Binance).{0,40}(점유율|밀|앞서)|점유율.{0,30}(하락|밀)'),
    ('Kraken', 'K4', 'Crypto Facilities 인가와 기초자산', r'Crypto Facilities'),
    ('Kraken', 'K5', '세 곳을 산 이유, 직접 안 만든 이유, 오래 걸린 이유', r'Bitnomial|Small Exchange|NinjaTrader'),
    ('Kraken', 'K6', '와이오밍 인가', r'SPDI|와이오밍'),
    ('Kraken', 'K7', '인수 기준 문장', r'쇼핑 목록|인수 기준|정량'),
    ('Kraken', 'K8', '다른 회사에 판다는 것(Payward Services, Embed)', r'Payward Services|Embed|기업용 인프라|B2B'),
    ('Kraken', 'K9', 'xStocks 법인과 브랜드, 주식 매입 자금', r'xStocks.{0,40}(법인|브랜드|발행)|기초.{0,10}(주식|증권).{0,20}(매입|사서|보관)'),
    ('Kraken', 'K10', 'Nasdaq 투자와 시장감시', r'Nasdaq'),
    ('Kraken', 'K11', 'xPO와 IPO', r'xPO|IPO Access|공모'),
    ('Kraken', 'K12', 'GTN과 방향', r'GTN'),
    ('Kraken', 'K13', '키프로스 날짜', r'키프로스|MiFID'),
    ('Kraken', 'K14', 'LSE 건', r'LSE'),
    ('Kraken', 'K16', 'CoinDesk 인터뷰 네 영역과 만들기, 사기, 제휴', r'코인데스크|CoinDesk|네 기둥|4축|사업 4'),
    ('Robinhood', 'R1', '지갑판', r'지갑판|Wallet'),
    ('Robinhood', 'R2', 'Funded Customers 정의', r'펀디드|Funded'),
    ('Robinhood', 'R3', '예측시장 주문 흐름', r'Kalshi|MIAXdx|예측시장'),
    ('Robinhood', 'R4', 'Bitstamp에서 얻은 것', r'Bitstamp'),
    ('Robinhood', 'R5', 'WonderFi', r'WonderFi'),
    ('Robinhood', 'R6', 'TradePMR', r'TradePMR'),
    ('Robinhood', 'R8', '자체 블록체인 용도', r'Robinhood Chain|자체 (블록)?체인|L2'),
    ('Robinhood', 'R9', '주문 대가 흐름', r'PFOF|주문 대가|시장조성자'),
    ('Binance', 'B1', '1위가 된 요인(2017~2020)', r'(?<!\d)20(17|18|19|20)(?!\d)'),
    ('Binance', 'B2', '수익 구성', r'매출|수익|수수료'),
    ('Binance', 'B3', 'bStocks와 xStocks 차이, 담보, 공시', r'bStocks'),
    ('Coinbase', 'C1', '인가를 사 모은 이유', r'인수.{0,30}(이유|목적)|(이유|목적).{0,30}인수'),
    ('Coinbase', 'C2', '선물, 무기한선물, 옵션의 법인과 지역', r'선물|옵션'),
    ('Coinbase', 'C3', 'Deribit', r'Deribit'),
    ('Coinbase', 'C4', 'Base 위 토큰의 발행 법인', r'Base'),
    ('Coinbase', 'C5', '2018 수탁 인가', r'신탁|수탁|Custody'),
    ('Coinbase', 'C6', 'USDC와 Circle', r'USDC|Circle'),
    ('Coinbase', 'C7', '실제 주식과 주식 토큰', r'주식'),
    ('Coinbase', 'C8', '앱 주식 날짜와 종목 수', r'(3,000|8,000)종'),
    ('Dinari', 'D1', '기술 회사인가 증권사인가, 지배 관계', r'Dinari Securities|Dinari, Inc|증권사|자회사'),
    ('Dinari', 'D2', '미국 밖 판매의 현지 인가', r'파트너.{0,30}(인가|라이선스)|현지 인가'),
    ('Dinari', 'D3', '카카오페이증권 방향', r'카카오페이'),
    ('Dinari', 'D4', '수수료 흐름', r'2,000달러|0\.20달러|수수료'),
    ('Dinari', 'D5', '2차 거래 장소', r'Hyperliquid|2차|거래소에서|이전'),
    ('Dinari', 'D6', 'tZERO', r'tZERO'),
    ('Dinari', 'D8', '미국 밖판 권리', r'청구권|채권|권리'),
    ('Dinari', 'D9', 'Broadridge', r'Broadridge'),
    ('Ondo', 'O1', '만드는가 운용하는가', r'운용|발행|OUSG|USDY'),
    ('Ondo', 'O2', '법인 구조와 이름', r'BVI|Global Markets|Ondo I LP|Flux|재단|법인'),
    ('Ondo', 'O3', '무엇으로 버나', r'운용보수|수수료|이자|매출'),
    ('Ondo', 'O4', '1위는 누구인가', r'Franklin|1위'),
    ('Ondo', 'O5', '거래소와 지갑 관계', r'Bitget|OKX|Trust Wallet|HTX'),
    ('Ondo', 'O6', '정규장 밖 가격', r'정규장|24시간|시장조성|호가'),
    ('Ondo', 'O7', 'Oasis Pro 전후', r'Oasis'),
    ('Ondo', 'O8', '미국 판매 여부', r'미국 (밖|안|투자자|거주자|인)|US Person|보관형'),
]
q_rows = []
for co, qid, q, pat in QS:
    pr = re.compile(pat)
    hits = [l for l in LINES if l[1] == co and pr.search(l[4])]
    body = [l for l in hits if l[0] == '본문']
    scr = Counter(l[0] for l in hits)
    q_rows.append([co, qid, q, len(body), len({l[3] for l in body}), '있음' if scr.get('핵심') else '없음',
                   ', '.join(f'{k} {v}' for k, v in scr.most_common()), ' '.join(l[2] for l in body[:30])])
T_Q = wcsv('6_부록A_질문별_위치', ['회사', '번호', '질문', '본문 줄 수', '본문 섹션 수', '핵심 화면', '화면별 줄 수', '본문 줄 번호(앞 30개)'], q_rows)

# ---------- 7) 지난 메모 처리 기록 ----------
LOG = [json.loads(l) for l in open('discussion/log.jsonl', encoding='utf-8') if l.strip()]
kinds = Counter(); per_co = Counter()
for g in LOG:
    per_co[g.get('company', '')] += 1
    for ch in g.get('changes') or [{}]:
        b, a = (ch.get('before') or '').strip(), (ch.get('after') or '').strip()
        if a in ('(삭제)', '') or a.endswith('삭제') or '지움' in a or '지웠' in a:
            kinds['삭제'] += 1
        elif '추가' in a or not b:
            kinds['세부 줄 추가'] += 1
        elif b and a:
            kinds['문장 수정'] += 1
        else:
            kinds['기타'] += 1
T_LOG = wcsv('7_메모처리_기록', ['구분', '건수'], [['처리 기록', len(LOG)]] + [['회사 ' + k, v] for k, v in per_co.items()] + [['변경 ' + k, v] for k, v in kinds.most_common()])

# ---------- 엑셀 ----------
try:
    from openpyxl import Workbook
    from openpyxl.styles import Font, Alignment, PatternFill
    wb = Workbook(); wb.remove(wb.active)
    for name, head, rows in [T_GAP, T_YEAR, T_UNUSED, T_WSUM, T_WORDS, T_SPREAD, T_VALUES, T_X, T_Q, T_LOG]:
        ws = wb.create_sheet(name[:31]); ws.append(head)
        for r in rows:
            ws.append(r)
        for c in ws[1]:
            c.font = Font(bold=True); c.fill = PatternFill('solid', fgColor='E6EDF8')
        ws.freeze_panes = 'A2'
        for i, h in enumerate(head, 1):
            ws.column_dimensions[ws.cell(1, i).column_letter].width = min(60, max(8, len(str(h)) * 2 + 2))
    wb.save(f'{OUT}/STAGE0_현황표.xlsx')
except Exception as e:
    print('엑셀 생략:', e)

print('미사용 사실', len(unused), dict(unused_by_co.most_common(8)))
print('빈 해', [(r[0], r[5], r[4]) for r in gap_rows])
print('지침 4-2 말이 나온 줄', len(word_rows))
print('부록 B 후보 줄', Counter(r[0] for r in X))
print('질문 수', len(q_rows), '본문 0줄 질문', [r[1] for r in q_rows if r[3] == 0], '핵심 화면에 없음', sum(1 for r in q_rows if r[5] == '없음'))
print('메모 기록', len(LOG), dict(kinds))
