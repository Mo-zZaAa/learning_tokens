"""글 조각으로 찾아가는 이동 버튼 [[자세히: 조각]] (md 카드용)."""
from pathlib import Path
p = Path("web/v5/template.html"); s = p.read_text()
old = ".replace(/\\((PM No [0-9][^()]*|"
assert old in s
s = s.replace(old, ".replace(/\\[\\[자세히: ([^\\]]+)\\]\\]/g, '<button type=\"button\" class=\"gobtn\" data-find=\"$1\" title=\"아래 자세한 곳으로 이동\">자세히 ↓</button>')" + old, 1)
old2 = "  const go = t.closest('[data-go]'); if (go){"
assert old2 in s
add = ("  const gf = t.closest('[data-find]'); if (gf){ e.preventDefault(); const frag = gf.dataset.find, home = gf.closest('section, .orow, .cbox');"
       " const el = Array.from(MAIN.querySelectorAll('.ln[id]')).find(x => !(home && home.contains(x)) && x.textContent.includes(frag));"
       " if (el) goTo(cur, view, el.id, ''); else toast('관련 부분을 찾지 못함'); return; }\n")
s = s.replace(old2, add + old2, 1)
p.write_text(s)
print("ok")
