"""work/TP-*/third_party.csv를 db/third_party.csv로 합친다(tp_id 중복은 뒤엣것 무시). 사용: python3 -I tools/merge_tp.py"""
import csv, glob
H = ['tp_id','자료 코드','발행처','발행처 입장','자료 제목','발간일','기준일','쪽','구분','대상 회사','내용','원문','링크','캡처 파일']
rows, seen = [], set()
for p in sorted(glob.glob('work/TP-*/third_party.csv')):
    for r in csv.DictReader(open(p, encoding='utf-8-sig')):
        if r.get('tp_id') and r['tp_id'] not in seen:
            seen.add(r['tp_id']); rows.append({k: r.get(k, '') for k in H})
rows.sort(key=lambda r: r['tp_id'])
with open('db/third_party.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, H); w.writeheader(); w.writerows(rows)
print('third_party', len(rows))
