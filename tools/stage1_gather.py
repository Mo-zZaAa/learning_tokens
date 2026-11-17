"""1단계 1번 모으기: 한 회사의 모든 줄(본문, 브리핑, 핵심, 전략, 비교, 파트별, 질문과 답)과 모든 사실(미사용 포함)을 한 표로.
사용: python3 tools/stage1_gather.py Kraken
"""
import csv, json, re, sys, os
sys.path.insert(0, os.path.dirname(__file__))
import stage0_audit as A  # noqa  (현황표도 같이 다시 셈)
co = sys.argv[1] if len(sys.argv) > 1 else 'Kraken'
pat = dict((n, p) for _, n, _, p in A.COS)[co]
rows = []
for scr, c, loc, sec, t, ids in A.LINES:
    if c == co:
        rows.append(['줄', scr, loc, sec, ' '.join(ids), re.findall(r'(?<!\d)(20[012]\d(?:-\d\d)?)(?!\d)', t)[:3], t])
used = set(re.findall(r'F-\d{4}', A.all_text))
for fid, f in A.FACTS.items():
    if re.search(pat, (f.get('회사') or '') + (f.get('사업 법인') or '')):
        rows.append(['사실', '사용' if fid in used else '미사용', fid, (f.get('틀 항목') or ''), f.get('검증 상태') or '', [f.get('기준일') or f.get('시작(연월)') or ''], (f.get('무엇을') or '') + ' | ' + (f.get('링크') or '')])
out = f'work/STAGE1/{co}_모으기.csv'
with open(out, 'w', encoding='utf-8-sig', newline='') as fh:
    w = csv.writer(fh); w.writerow(['종류', '화면 또는 사용', '위치 또는 번호', '섹션 또는 틀', '근거 번호 또는 검증', '날짜', '글'])
    for r in rows:
        w.writerow(r[:5] + [' '.join(r[5])] + [r[6]])
print(out, len(rows), '줄', sum(1 for r in rows if r[0] == '줄'), '사실', sum(1 for r in rows if r[0] == '사실'), '미사용', sum(1 for r in rows if r[1] == '미사용'))
