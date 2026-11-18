import re,sys
from html.parser import HTMLParser
p='/home/user/learning_tokens/web/v5/ondo_deep.html'
h=open(p,encoding='utf-8').read()
print('긴 줄표', h.count('—'), '가운뎃점', h.count('·'), '제공', h.count('제공'), '미정/미확인/확인 필요', len(re.findall('미정|미확인|확인 필요',h)))
print('외부 주소(src/href=http, link 태그)', len(re.findall(r'<(?:script|link|img)[^>]+(?:src|href)="https?:',h)))
class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.stack=[]; s.res=[]
    def handle_starttag(s,t,a):
        a=dict(a); c=a.get('class','')
        if t in('li','p','dd') and c.split() and c.split()[0] in('f','jd','x','nof'):
            s.stack.append([t,c.split()[0],0,''])
        elif t in ('li','p','dd'):
            s.stack.append([t,None,0,''])
        if t=='button' and 'fn' in c.split():
            for x in s.stack: x[2]+=1
    def handle_endtag(s,t):
        if t in ('li','p','dd') and s.stack:
            x=s.stack.pop(); 
            if x[1]: s.res.append(x)
    def handle_data(s,d):
        for x in s.stack: x[3]+=d
q=P(); q.feed(h)
f=[x for x in q.res if x[1]=='f']; jd=[x for x in q.res if x[1]=='jd']; ex=[x for x in q.res if x[1]=='x']; nof=[x for x in q.res if x[1]=='nof']
bad=[x for x in f if x[2]==0]
badjd=[x for x in jd if not x[3].strip().startswith('(판단)') and '(판단)' not in x[3]]
print('사실 줄',len(f),'각주 없는 사실 줄',len(bad),'| 판단 줄',len(jd),'(판단) 표기 빠진 판단 줄',len(badjd),'| 설명 줄',len(ex),'| 분류 없는 줄',len(nof))
for x in bad+badjd+nof: print('  !',x[1],x[3][:80])
