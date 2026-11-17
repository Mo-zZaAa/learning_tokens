"""kb 원본(사건 카드 json, 구조 표 csv)을 읽어 사람이 보는 md와 연표를 만들고 점검 숫자를 냄.
사용: python3 tools/kb_render.py Kraken
- kb/events/<co>.json에 rows(본문 줄 번호)를 근거 번호로 채움
- kb/events/<co>.md: 사건 카드 읽는 판
- kb/structs/<co>/timeline.csv: 연표(빈 해 표시)
- 점검: 빈 단 수, 빈 해, 지침 4-2의 말, DB에 없는 근거 번호
"""
import csv, json, os, re, sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
co = sys.argv[1] if len(sys.argv) > 1 else 'Kraken'
slug = co.lower()
FOUNDED = {'Kraken': 2011, 'Robinhood': 2013, 'Binance': 2017, 'Coinbase': 2012, 'Dinari': 2021, 'Ondo': 2021}[co]
FACTS = {r['fact_id']: r for r in csv.DictReader(open('db/facts.csv', encoding='utf-8'))}
html = open('web/index.html', encoding='utf-8').read()
D = json.loads(re.search(r'<script id="data" type="application/json">(.*?)</script>', html, re.S).group(1).replace('<\\/', '</'))
BODY = [r for c in D['companies'] if c['slug'] == slug for s in c['sections'] for r in s['rows']]
by_fid = defaultdict(list)
for r in BODY:
    for f in r.get('ids') or []:
        by_fid[f].append(r['id'])

ep = f'kb/events/{slug}.json'
EV = json.load(open(ep, encoding='utf-8'))
BANNED = ['제공', '지원', '확대', '강화', '통합', '연결성', '인프라를 판', '한 벌', '일습', '쇼핑 목록', '지갑판', '추적 증권', '운영사', '발행 대행', '백단']


def unq(t):
    return re.sub(r'"[^"]*"|“[^”]*”|\([^)]*Sethi[^)]*\)', ' ', t or '')


issues = defaultdict(list)
for e in EV:
    e['rows'] = sorted({rid for f in e['fids'] for rid in by_fid.get(f, [])})
    for k in ('what', 'how'):
        if not (e.get(k) or '').strip():
            issues['빈 단(어떻게)' if k == 'how' else '빈 단(무엇)'].append(e['id'])
    if not e['why']:
        issues['빈 단(왜)'].append(e['id'])
    if not (e.get('result') or '').strip():
        issues['빈 단(그래서)'].append(e['id'])
    if e.get('five') and not e.get('kdx'):
        issues['빈 단(KDX에는, 요약 사건)'].append(e['id'])
    if e.get('five') and len(e.get('tails') or []) < 2:
        issues['꼬리 질문 2개 미만(요약 사건)'].append(e['id'])
    txt = ' '.join([e.get('what') or '', e.get('how') or '', e.get('result') or ''] + [w['t'] for w in e['why']] + [(e.get('kdx') or {}).get('t', '')] + [t['a'] for t in e.get('tails') or []])
    for b in BANNED:
        if b in unq(txt):
            issues['지침 4-2의 말'].append(f"{e['id']}:{b}")
    for f in e['fids'] + [x for w in e['why'] for x in w['fids']]:
        if f.startswith('F-') and f not in FACTS:
            issues['DB에 없는 번호'].append(f"{e['id']}:{f}")
    if '1차 자료로 교체 중' in txt:
        issues['위키백과만으로 받친 사건(교체 중)'].append(e['id'])
json.dump(EV, open(ep, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

# 연표
years = defaultdict(list)
for e in EV:
    years[int(e['date']['v'][:4])].append(e)
tl = [['연도', '날짜(종류)', '사건 번호', '사건', '법인']]
empty = []
for y in range(FOUNDED, 2027):
    if not years.get(y):
        empty.append(y)
        tl.append([y, '', '', '(빈 해)', ''])
    for e in years.get(y, []):
        tl.append([y, f"{e['date']['v']}({e['date']['kind']})", e['id'], e['title'], e['ent']])
os.makedirs(f'kb/structs/{slug}', exist_ok=True)
csv.writer(open(f'kb/structs/{slug}/timeline.csv', 'w', encoding='utf-8', newline='')).writerows(tl)

# 읽는 판
L = [f'# {co} 사건 카드 ({len(EV)}건)', '', '자동 생성: tools/kb_render.py. 고치는 곳은 kb/events/' + slug + '_events_src.py', '']
for e in EV:
    L += [f"## {e['id']} {e['date']['v']}({e['date']['kind']}) {e['title']}", f"- 법인: {e['ent']}", f"1. 무엇: {e['what']}"]
    if e.get('how'):
        L.append(f"2. 어떻게: {e['how']}")
    for w in e['why']:
        L.append(f"3. 왜({w['basis']}): {w['t']} [{' '.join(w['fids'])}]")
    if e.get('choice'):
        L.append(f"   - 고른 방식: {e['choice']['picked']}{(' . ' + e['choice']['reason']) if e['choice']['reason'] else ''}".replace(' . ', ', '))
    if e.get('result'):
        L.append(f"4. 그래서: {e['result']}")
    if e.get('kdx'):
        L.append(f"5. KDX에는({e['kdx']['part']}): {e['kdx']['t']}")
    for t in e.get('tails') or []:
        L.append(f"- 한 단계 더: {t['q']} / {t['a']}")
    L.append(f"- 근거: {' '.join(e['fids'])}" + (f" / 본문 줄: {' '.join(e['rows'][:20])}" if e['rows'] else ''))
    L.append('')
open(f'kb/events/{slug}.md', 'w', encoding='utf-8').write('\n'.join(L))

print(f'{co}: 사건 {len(EV)}건, 요약 사건 {sum(1 for e in EV if e.get("five"))}건, 빈 해 {empty or "없음"}')
for k, v in issues.items():
    print(f'  {k}: {len(v)} {v[:12]}')
