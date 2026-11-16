"""work/SCOPE-*/axis.csv를 회사 × 축 한 칸 한 줄로 합쳐 db/cross_axis.csv와 kb/cross.md 9절을 만든다."""
import csv, glob, re
AX = ['자산(채권)','자산(비상장주식)','자산(펀드)','자산(가상자산)','고객(고액자산가)','고객(기관)','시장(해외)']
CO = ['Kraken','Robinhood','Binance','Coinbase','Dinari','Ondo']
rows = []
for p in sorted(glob.glob('work/SCOPE-*/axis.csv')):
    rows += list(csv.DictReader(open(p, encoding='utf-8-sig')))
cell = {}
for r in rows:
    co = next((c for c in CO if r['회사'].startswith(c)), r['회사'])
    if r['축'] not in AX: continue
    cell.setdefault((co, r['축']), []).append(r)
def key(r):
    m = re.search(r'\d{4}(-\d{2})?', r.get('시점', ''))
    return m.group(0) if m else '9999'
out = []
for co in CO:
    for ax in AX:
        it = sorted(cell.get((co, ax), []), key=key)
        if not it: continue
        parts = []
        for r in it[:3]:
            t = r['한 일(한 줄)'].strip()
            w = r.get('시점', '').strip()
            parts.append(f"{t}({w})" if re.fullmatch(r'[0-9QH ~,\-]+', w or '') and re.search(r'\d{4}', w) and w not in t else t)
        ids = ';'.join(dict.fromkeys(i for r in it for i in re.split(r'[;\s]+', r['fact_ids']) if i))
        how = ', '.join(dict.fromkeys(r.get('확보 방식', '').strip() for r in it if r.get('확보 방식', '').strip()))
        out.append({'회사': co, '축': ax, '한 일(한 줄)': ' → '.join(parts) + (f' 외 {len(it)-3}건' if len(it) > 3 else ''), '시점': '', '확보 방식': how, 'fact_ids': ids})
with open('db/cross_axis.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, ['회사','축','한 일(한 줄)','시점','확보 방식','fact_ids']); w.writeheader(); w.writerows(out)
md = ['## 9. 회사 × KDX 확장 축', '', '칸에는 그 회사가 그 축에서 한 일(시점 순, 세 건까지)과 확보 방식. 빈칸은 한 일이 없거나 1차 자료로 확인되지 않은 것. 원본 db/cross_axis.csv, 근거는 fact_ids.', '',
      '| 회사 | ' + ' | '.join(AX) + ' |', '|' + '---|' * (len(AX) + 1)]
for co in CO:
    cells = []
    for ax in AX:
        r = next((x for x in out if x['회사'] == co and x['축'] == ax), None)
        cells.append(f"{r['한 일(한 줄)']} [{r['확보 방식']}]" if r else '')
    md.append(f'| {co} | ' + ' | '.join(cells) + ' |')
c = open('kb/cross.md', encoding='utf-8').read()
c = re.split(r'\n## 9\. 회사 × KDX 확장 축', c)[0].rstrip('\n')
open('kb/cross.md', 'w', encoding='utf-8').write(c + '\n\n' + '\n'.join(md) + '\n')
print('axis cells', len(out))
