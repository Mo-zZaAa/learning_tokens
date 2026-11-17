import sys,re,html
p=sys.argv[1]
t=open(p,encoding='utf-8',errors='replace').read()
t=re.sub(r'(?is)<(script|style|noscript)[^>]*>.*?</\1>',' ',t)
t=re.sub(r'(?i)<br\s*/?>','\n',t)
t=re.sub(r'(?i)</(p|div|h\d|li|tr|section|article)>','\n',t)
t=re.sub(r'<[^>]+>',' ',t)
t=html.unescape(t)
t=re.sub(r'[ \t\xa0]+',' ',t)
t=re.sub(r'\n\s*\n+','\n',t)
out=p.rsplit('.',1)[0]+'.txt'
open(out,'w',encoding='utf-8').write(t)
print(out,len(t))
