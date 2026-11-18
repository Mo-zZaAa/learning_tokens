import csv,sys,re
rows=[r for r in csv.DictReader(open('db/facts.csv',encoding='utf-8-sig')) if r['회사'].startswith('Ondo')]
for q in sys.argv[1:]:
    pats=q.split('&')
    hits=[r for r in rows if all(re.search(p,(r['무엇을']+' '+r['원문 근거 문장']+' '+r['값']+' '+r['기준일']),re.I) for p in pats)]
    print('##',q,len(hits))
    for r in hits[:3]:
        print('  ',r['fact_id'],r['기준일'],'|',r['무엇을'][:80],'|',r['원문 근거 문장'][:110],'|',r['링크'][:80])
