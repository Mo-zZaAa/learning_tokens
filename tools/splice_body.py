"""v3 본문에서 대분류를 골라 바꿔 v4를 만든다. 사용: splice_body.py 원본 결과 바꿀내용.md
바꿀내용.md는 '## 제목' 단위. 같은 제목이면 교체, '## -제목'은 삭제, 새 제목은 그 자리(@after 제목)에 추가.
'#= 찾을 문구 => 바꿀 문구' 줄은 본문 전체 치환."""
import sys,re
src,dst,patch=sys.argv[1:4]
txt=open(src,encoding='utf-8').read()
head,*secs=re.split(r'(?m)^(?=## )',txt)
secs=[[s.split('\n',1)[0][3:].strip(),s] for s in secs]
p=open(patch,encoding='utf-8').read()
subs=[[x.replace('\\n','\n') for x in l[3:].split(' => ',1)] for l in p.splitlines() if l.startswith('#= ')]
p='\n'.join(l for l in p.splitlines() if not l.startswith('#= '))
for blk in re.split(r'(?m)^(?=## )',p):
    if not blk.startswith('## '):continue
    title=blk.split('\n',1)[0][3:].strip()
    after=None
    m=re.search(r'@after (.+)$',title)
    if m: after=m.group(1).strip(); title=title[:m.start()].strip(); blk='## '+title+'\n'+blk.split('\n',1)[1]
    blk=blk.rstrip('\n')+'\n\n'
    if title.startswith('-'):
        secs=[s for s in secs if s[0]!=title[1:].strip()];continue
    idx=[i for i,s in enumerate(secs) if s[0]==title]
    if idx: secs[idx[0]][1]=blk
    elif after:
        j=[i for i,s in enumerate(secs) if s[0]==after][0]; secs.insert(j+1,[title,blk])
    else: secs.append([title,blk])
out=head+''.join(s[1] for s in secs)
for a,b in subs:
    if a not in out: print('치환 대상 없음:',a,file=sys.stderr)
    out=out.replace(a,b)
open(dst,'w',encoding='utf-8').write(out.rstrip('\n')+'\n')
