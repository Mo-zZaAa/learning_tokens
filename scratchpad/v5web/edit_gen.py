"""scratchpad/ondodeep/gen.py: S6 그림을 개요 패키지 flows(web/v5/ondo_card.py)로. 일회성 편집."""
p = '/home/user/learning_tokens/scratchpad/ondodeep/gen.py'
s = open(p, encoding='utf-8').read()

i = s.index("g = [legend([('na', '투자자'), ('co', '회사 쪽'), ('is', '발행 법인'), ('tp', '제3자')]), '<div class=\"flows\">',")
j = s.index("sec('S6', '상품별 돈 흐름(가상 숫자)',")
new = '''# 개요 1층과 같은 그림: inputs/ondo_overview_261118/content/ondo_overview.json의 flows를 web/v5/ondo_card.py로 그림
sys.path.insert(0, str(ROOT / 'web/v5'))
import ondo_card  # noqa: E402
_PK = ondo_card.load()
g = ['<div class="fwlist">'] + [ondo_card.flow_html(_PK['flows'][k], title=True) for k in ('ousg', 'usdy', 'stocks', 'new', 'revenue')] + ['</div>']
'''
s = s[:i] + new + s[j:]
a = "    out = tpl.replace('%%TOC%%', toc).replace('%%BODY%%', '\\n'.join(body))"
assert s.count(a) == 1
s = s.replace(a, a + "\n    out = out.replace('</style>', ondo_card.FLOW_CSS + '.fwlist{display:grid;gap:18px}.fwlist .fw-title{font-size:15px}</style>', 1)")
open(p, 'w', encoding='utf-8').write(s)
print('ok')
