"""Check companies/*.md against 8절 rules. usage: python3 -I tools/check_body.py <md files>"""
import re, sys, csv
facts = {r['fact_id']: r['검증 상태'] for r in csv.DictReader(open('db/facts.csv', encoding='utf-8'))}
laws = {r['law_id'] for r in csv.DictReader(open('db/laws.csv', encoding='utf-8'))}
for p in sys.argv[1:]:
    sec, cnt, bad = None, 0, []
    for n, line in enumerate(open(p, encoding='utf-8'), 1):
        s = line.rstrip('\n')
        if s.startswith('##'):
            sec = None; continue
        if s.strip().startswith('●'):
            if sec and cnt > 4: bad.append(f'{p}:{sec[0]} 중분류 줄 수 {cnt}')
            sec, cnt = (n, s.strip()), 0
            body = s.strip()
        elif s.strip().startswith(('★', '①', '②', '③')):
            cnt += 1; body = s.strip()
        else:
            continue
        ids = re.findall(r'\[([^\]]+)\]', body)
        if body.startswith('!['): continue
        if any(k in body for k in ('원문 :', '번역 :', '해석 :')) and body[0] in '①②③': continue
        if 'http' in body and body.startswith('★'):
            ids = re.findall(r'\[([^\]]+)\]', body)
            if not ids: bad.append(f'{p}:{n} 근거 ID 없음')
            continue
        if not any(k in body for k in ('원문 :', '번역 :', '해석 :', '발언 :')):
            text = re.sub(r'\[[^\]]+\]', '', body)
            text = re.sub(r'\([^)]*\)', '', text)
            text = text.split(' : ', 1)[-1].strip() if ' : ' in text else text.lstrip('●★①②③ ').strip()
            if len(text) > 40: bad.append(f'{p}:{n} {len(text)}자: {text}')
        if (body.startswith('●') and ':' not in body) or body.startswith(('★ 쟁점', '★ 비교 항목')):
            continue
        if not ids: bad.append(f'{p}:{n} 근거 ID 없음')
        for i in ids:
            if i.startswith('F-'):
                st = facts.get(i)
                if st not in ('1차 출처 확인', '교차 확인', '등록부 대조 대기'): bad.append(f'{p}:{n} {i} 상태 {st}')
            elif i not in laws: bad.append(f'{p}:{n} {i} 미등록 law_id')
        if '—' in body or '·' in body: bad.append(f'{p}:{n} 금지 기호')
    if sec and cnt > 4: bad.append(f'{p}:{sec[0]} 중분류 줄 수 {cnt}')
    print('\n'.join(bad) if bad else f'{p} OK')
