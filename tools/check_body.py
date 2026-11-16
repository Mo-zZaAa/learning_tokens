"""본문 점검(2026-11-16 개정: 글자 수, 줄 수 규칙 해제).
사용: python3 -I tools/check_body.py <md 파일들>
- 줄 종류: ●, ★, ①②③, - (세부 불렛, "  - " 들여쓰기)
- 근거 필수: 사실 번호 [F-..] (검증 상태 1차 출처 확인, 교차 확인, 등록부 대조 대기, 회사 주장), [TP-..], 조문 ID, 사건 ID(1차, 교차), 또는 본문 줄 링크 {xx-0000}
- 근거 없어도 되는 줄: 그림 줄, 인용 ①②③(원문, 번역), 머리 ●(콜론 없음), "뜻 :" 용어 풀이 줄
- 금지: 긴 줄표(—), 가운뎃점(·), 물결(~)을 구어체로 쓴 것은 사람이 확인
"""
import re, sys, csv, os
facts = {r['fact_id']: r['검증 상태'] for r in csv.DictReader(open('db/facts.csv', encoding='utf-8'))}
laws = {r['law_id'] for r in csv.DictReader(open('db/laws.csv', encoding='utf-8'))}
cases = {r['case_id'] for r in csv.DictReader(open('db/cases.csv', encoding='utf-8')) if r.get('검증 상태') in ('1차 출처 확인', '교차 확인')}
tps = {r['tp_id'] for r in csv.DictReader(open('db/third_party.csv', encoding='utf-8'))} if os.path.exists('db/third_party.csv') else set()
OK = ('1차 출처 확인', '교차 확인', '등록부 대조 대기', '회사 주장')
LINK = re.compile(r'\{[a-z]{2}-[0-9a-z]+\}')
for p in sys.argv[1:]:
    bad = []
    for n, line in enumerate(open(p, encoding='utf-8'), 1):
        s = line.strip()
        if not s or s.startswith('#') or s.startswith('!['):
            continue
        if s[0] not in '●★①②③-':
            continue
        body = s
        if s[0] in '①②' or ('원문 :' in s[:8] or '번역 :' in s[:8]):
            continue
        if '—' in body or '·' in body:
            bad.append(f'{p}:{n} 금지 기호')
        ids = re.findall(r'\[([^\]]+)\]', body)
        label = body[1:].strip().split(' : ', 1)[0] if ' : ' in body else ''
        if body.startswith('●') and ' : ' not in body:
            continue
        if label in ('뜻',):
            continue
        if s[0] == '③' and not ids:
            continue
        if not ids and not LINK.search(body):
            bad.append(f'{p}:{n} 근거 없음: {body[:50]}')
        for i in ids:
            if i.startswith('F-'):
                st = facts.get(i)
                if st not in OK: bad.append(f'{p}:{n} {i} 상태 {st}')
            elif i.startswith('TP-'):
                if i not in tps: bad.append(f'{p}:{n} {i} 제3자 표에 없음')
            elif i in cases or i in laws:
                pass
            else:
                bad.append(f'{p}:{n} {i} 알 수 없는 근거')
    print('\n'.join(bad) if bad else f'{p} OK')
