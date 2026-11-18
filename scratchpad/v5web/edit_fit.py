"""개요 머리 간격을 줄여 접힌 1층이 900px 한 화면에 들어가게 하는 일회성 편집."""
p = '/home/user/learning_tokens/web/v5/template.html'
s = open(p, encoding='utf-8').read()
a = ".ov .pagehead{margin-bottom:8px}"
b = (".ov .pagehead{margin-bottom:4px;display:flex;flex-wrap:wrap;align-items:baseline;gap:2px 14px}\n"
     ".ov .pagehead .eyebrow{flex-basis:100%}\n"
     ".ov .pagehead h1{font-size:24px}\n"
     ".ov .lnav{padding-block:6px;margin-bottom:0}\n"
     ".ov .layer:first-of-type{margin-top:10px}\n"
     ".ov .cgrid .cbox>h3{margin-bottom:2px}")
assert s.count(a) == 1
s = s.replace(a, b)
open(p, 'w', encoding='utf-8').write(s)
print('ok')
