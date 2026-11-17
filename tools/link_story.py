"""브리핑(회사 전략)의 [F-xxxx], [CASE-xxx] 표기를 db의 원문 링크로 바꾼다(이미 링크된 것은 그대로).
사용: python3 tools/link_story.py briefs/Kraken.md"""
import csv, re, sys
R = {r['fact_id']: r for r in csv.DictReader(open('db/facts.csv', encoding='utf-8-sig'))}
C = {}
for r in csv.DictReader(open('db/cases.csv', encoding='utf-8-sig')):
    C[r[list(r.keys())[0]]] = r
def url_of(k):
    if k.startswith('F-'):
        v = (R.get(k, {}).get('링크') or '').split()
        return v[0].split(';')[0] if v else ''
    return next((v for v in C.get(k, {}).values() if v and str(v).startswith('http')), '')
for p in sys.argv[1:]:
    t = open(p, encoding='utf-8').read()
    miss = [k for k in re.findall(r'\[((?:F|CASE)-\d{3,4})\](?!\()', t) if (k.startswith('F-') and k not in R)]
    def rep(m):
        u = url_of(m.group(1))
        return f'[{m.group(1)}]({u})' if u.startswith('http') else m.group(1)
    t = re.sub(r'\[((?:F|CASE)-\d{3,4})\](?!\()', rep, t)
    open(p, 'w', encoding='utf-8').write(t)
    print(p, 'DB에 없는 번호:', miss or '없음')
