"""PM 질문 29개가 Ondo 개요 카드(ondo_overview.json)와 빌드된 화면 데이터(web/v5/index.html)에서 찾아지는지 확인.

실행: python3 scratchpad/v5web/coverage_check.py
결과: inputs/ondo_overview_261118/coverage_check.csv
판정: 줄 이름(무엇을 하나 등)이 카드에 있고, 가리킨 불렛(첫째, 둘째, 셋째 또는 낱말로 찾은 불렛)과
     세부, 그림, 표가 실제로 있으며, 그 줄들이 빌드된 화면 데이터에 줄 id와 함께 들어갔는지 봄.
"""
import csv
import json
import re
from pathlib import Path

ROOT = Path('/home/user/learning_tokens')
PKG = ROOT / 'inputs/ondo_overview_261118'
card = json.load(open(PKG / 'content/ondo_overview.json', encoding='utf-8'))
flows = card['flows']
rows = {r['label']: r for r in card['card']['rows']}

html = (ROOT / 'web/v5/index.html').read_text(encoding='utf-8')
m = re.search(r'<script id="data" type="application/json">(.*?)</script>', html, re.S)
D = json.loads(m.group(1).replace('<\\/', '</'))
odx = next(p['odx'] for L in D['C']['ondo']['ov']['layers'] for p in L['parts'] if p.get('odx'))
built = {r['label']: r for r in odx['card']['rows']}


def text_of(it):
    s = (it.get('k', '') + ' ' + it.get('k2', '') + ' ' + it.get('t', '')).strip()
    tb = it.get('table')
    if tb:
        s += ' ' + ' '.join(tb.get('head', []) + [c for r in tb.get('rows', []) for c in r])
    for x in it.get('sub', []) + it.get('kids', []):
        s += ' ' + text_of(x)
    if it.get('flow'):
        s += ' 그림 ' + it['flow'] + ' ' + flows[it['flow']].get('title', '')
    return s


def has_id(it):
    return bool(it.get('id')) and all(has_id(x) for x in it.get('sub', []) + it.get('kids', []))


ORD = {'첫': 0, '둘째': 1, '셋째': 2}
STOP = {'세부', '불렛', '첫', '둘째', '셋째', '줄', '각', '상품', '전체', '+', '표', '그림'}


def check_part(part, prev=''):
    part = part.strip()
    if '>' not in part and re.sub(r'\s*(전체|\+.*)$', '', part).strip() not in rows and prev:
        names = [x.strip() for x in re.sub(r'\s*세부.*$', '', part).split(',') if x.strip()]
        res = [check_part(f'{prev} > {n} 세부') for n in names]
        return all(r[0] for r in res), ' / '.join(r[1] for r in res)
    m2 = re.match(r'^(.+?)(?:\s*>\s*(.+))?$', part)
    label, hint = m2.group(1).strip(), (m2.group(2) or '').strip()
    label = label.replace(' 전체', '').strip()
    extra = re.findall(r'\+\s*(.+)$', label)
    label = re.sub(r'\s*\+.*$', '', label).strip()
    if label not in rows:
        return False, f'줄 이름 없음: {label}'
    row = rows[label]
    items = row.get('items') or row.get('path') or []
    brow = built.get(label)
    if not brow or not all(has_id(x) for x in (brow.get('items') or brow.get('path') or [])):
        return False, f'{label}: 화면 데이터에 줄 id 없음'
    notes = [f'{label}: 불렛 {len(items)}개']
    if hint:
        main, _, fig = hint.partition('+')
        fig = (fig.strip() + ' ' + ' '.join(extra)).strip()
        pick = None
        mo = re.match(r'^(첫|둘째|셋째)\s*불렛', main.strip())
        if mo:
            idx = ORD[mo.group(1)]
            if idx >= len(items):
                return False, f'{label}: {mo.group(1)} 불렛 없음'
            pick = items[idx]
        else:
            words = [w for w in re.split(r'[\s(),]+', re.sub(r'\(.*?\)', ' ', main)) if w and w not in STOP and len(w) >= 2]
            flat = lambda it: re.sub(r'\(.*?\)', '', text_of(it)).lower() + ' ' + text_of(it).lower()
            cands = [it for it in items if all(w.lower() in flat(it) for w in words)] if words else items
            if not cands:
                return False, f'{label}: 낱말 {words} 를 담은 불렛 없음'
            pick = cands[0]
        if '세부' in main and not (pick.get('kids') or pick.get('table') or pick.get('sub')):
            return False, f'{label}: 고른 불렛에 세부 없음'
        inner = re.findall(r'\((.*?)\)', main)
        if inner:
            miss = [w for w in re.split(r'[,\s]+', inner[0]) if len(w) >= 2 and w not in STOP and w.lower() not in text_of(pick).lower()]
            notes.append('괄호 낱말 중 원문에 그대로 없는 것: ' + ', '.join(miss) if miss else '괄호 낱말 모두 있음')
        notes.append('고른 불렛: ' + (pick.get('t') or pick.get('k'))[:40])
        for f in re.findall(r'그림\s+(\w+)', fig):
            if f not in flows:
                return False, f'그림 {f} 없음'
            notes.append(f'그림 {f} 있음')
        if '돈을 버는 시점' in hint + ' '.join(extra) and 'revenue' not in flows:
            return False, '돈을 버는 시점 표 없음'
    return True, '; '.join(notes)


out = []
for r in csv.DictReader(open(PKG / 'content/pm_question_coverage.csv', encoding='utf-8-sig')):
    loc = r['카드에서 답한 곳']
    res, prev = [], ''
    for p in re.split(r'\s/\s', loc):
        res.append(check_part(p, prev))
        prev = p.split('>')[0].strip() if '>' in p else prev
    ok = all(x[0] for x in res)
    out.append({'번호': r['번호'], 'PM 질문': r['PM 질문'], '카드에서 답한 곳': loc, '결과': '찾음' if ok else '못 찾음',
                '확인 내용': ' / '.join(x[1] for x in res)})
with open(PKG / 'coverage_check.csv', 'w', encoding='utf-8-sig', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(out[0].keys()))
    w.writeheader()
    w.writerows(out)
print('찾음', sum(o['결과'] == '찾음' for o in out), '/', len(out))
for o in out:
    if o['결과'] != '찾음' or '그대로 없는' in o['확인 내용']:
        print(o['번호'], o['결과'], o['확인 내용'][:220])
