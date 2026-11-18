"""답 꼬리표를 칸 머리마다 하나(개수 표시)로 묶고, 휴대폰 위 막대 줄 수를 줄이는 일회성 편집."""
p = '/home/user/learning_tokens/web/v5/template.html'
s = open(p, encoding='utf-8').read()


def rep(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:80])
    s = s.replace(a, b)


rep('.abadge::after{content:"답"}', '.abadge::after{content:"답"}\n.abadge[data-n]::after{content:"답 " attr(data-n)}')
rep("""function addBadge(el, mid){
  if (el.querySelector(`:scope .abadge[data-amid="${CSS.escape(mid)}"]`)) return;""",
    """function addBadge(el, mid, n){
  if (el.querySelector(`:scope .abadge[data-amid="${CSS.escape(mid)}"]`)) return;""")
rep("""b.setAttribute('aria-label', '이 메모의 답 보기');
  host.appendChild(b);""",
    """b.setAttribute('aria-label', n > 1 ? `이 칸 메모 답 ${n}건 보기` : '이 메모의 답 보기'); if (n > 1) b.dataset.n = n;
  host.appendChild(b);""")
rep("""  for (const m of allMemos()){
    if (normCo(m.co) !== cur || VIEW_KEY[normView(m.view)] !== view) continue;
    const a = ANS[m.mid], el = m.anchor ? document.getElementById(m.anchor) : null;
    if (el){ el.classList.add(a ? 'ha' : 'hm'); if (a) addBadge(el, m.mid); }
    else if (a){ const s = secEl(m.sec); if (s) addBadge(s, m.mid); }
  }""",
    """  const bySec = new Map();
  for (const m of allMemos()){
    if (normCo(m.co) !== cur || VIEW_KEY[normView(m.view)] !== view) continue;
    const a = ANS[m.mid], el = m.anchor ? document.getElementById(m.anchor) : null;
    if (el){ el.classList.add(a ? 'ha' : 'hm'); if (a) addBadge(el, m.mid); }
    else if (a){ const s = secEl(m.sec); if (s){ if (!bySec.has(s)) bySec.set(s, []); bySec.get(s).push(m.mid); } }
  }
  bySec.forEach((mids, s) => addBadge(s, mids[0], mids.length));  // 줄을 모르는 답은 칸 머리에 하나로 모음""")
rep("  .seg{order:2}.search{order:3;flex-basis:120px}.memobtn{order:4}",
    "  .seg{order:2}.search{order:3;flex-basis:70px}.memobtn{order:4;gap:4px}")
open(p, 'w', encoding='utf-8').write(s)

c = '/home/user/learning_tokens/scratchpad/v5web/check.js'
t = open(c, encoding='utf-8').read()
a = "  const fref = await page.$('.ev .fids .ref');"
if a in t:
    t = t.replace(a, "  await page.evaluate(() => { document.querySelectorAll('[id$=\"-r-sec-ref\"], [id$=\"-r-sec-ev\"]').forEach(d => d.open = true); });\n" + a)
open(c, 'w', encoding='utf-8').write(t)
print('ok')
