"""스토리라인 문체 점검: python3 tools/check_story.py briefs/Kraken.md
금지 표현, 긴 줄표, 가운뎃점, 근거 없는 줄(해석 줄 제외)을 찾는다."""
import re, sys
BAN = ['한 벌','통째','넘봄','넘보','깜.','빡센','빡세','야무지','재미를','재미 좀','굴러가','꽂는','꽂아','길목','돈이 되','짝을 맞','팔아 보니','무엇을 파나','누가 쓰나','어떻게 굴리나','1단계','2단계','3단계']
for p in sys.argv[1:]:
    t = open(p, encoding='utf-8').read()
    if '## 스토리라인' in t:
        t = t[t.index('## 스토리라인'):t.index('## 1층') if '## 1층' in t else len(t)]
    bad = 0
    L = t.split('\n')
    for i, l in enumerate(L, 1):
        nxt = L[i] if i < len(L) else ''
        for w in BAN:
            if w in l: print(f'{p}:{i} 금지 표현 "{w}": {l.strip()[:80]}'); bad += 1
        if '—' in l or '·' in l: print(f'{p}:{i} 긴 줄표 또는 가운뎃점'); bad += 1
        s = l.strip()
        if s.startswith('- ') and not re.search(r'\[(F|CASE)-\d', s) and not s.startswith('- 해석') and not s.endswith(('중','음')) and len(s) > 40 and not l.startswith('  - ') and not nxt.startswith('  - '):
            print(f'{p}:{i} 근거 없음: {s[:80]}'); bad += 1
    print(p, 'OK' if not bad else f'{bad}건')
