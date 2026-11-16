"""본문 줄 찾기: python3 tools/find_line.py <회사 접두(kr,rh,bn,cb,dn,on)> <정규식> → 줄 ID, 화면 번호, 문구"""
import sys, re, json
sys.path.insert(0, 'web')
import build as B
pre, pat = sys.argv[1], re.compile(sys.argv[2])
store = json.load(open('web/line_ids.json'))
for base, name, kind, prefix in B.ORDER:
    if prefix != pre: continue
    B.img_key = lambda p: None
    logo, secs = B.parse(B.latest_body(base)); B.assign_ids(prefix, secs, store)
    for s in secs:
        n = 0
        for r in s['rows']:
            n += 1
            t = (r.get('label') or '') + ' : ' + (r.get('text') or '')
            if pat.search(t): print(r['id'], f"{name} {s['code']}-{n}", t[:90])
