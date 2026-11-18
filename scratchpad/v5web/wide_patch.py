from pathlib import Path
p = Path("web/v5/template.html"); s = p.read_text()
old = "<section class=\"cbox gblk\" id=\"${s.id}\""
assert old in s
s = s.replace(old, "<section class=\"cbox gblk${s.h === '핵심 포인트' ? ' wide hot' : s.h === '한눈에 보기' ? ' wide' : ''}\" id=\"${s.id}\"", 1)
s = s.replace(".orow.hot .olab{color:var(--hl-ink)}", ".orow.hot .olab{color:var(--hl-ink)}\n.cbox.wide{grid-column:1/-1}\n.cbox.hot{background:color-mix(in srgb,var(--hl) 28%,var(--panel));box-shadow:inset 5px 0 0 #e6b800}", 1)
p.write_text(s)
print("ok")
