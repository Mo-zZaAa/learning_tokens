"""1층 카드: 큰 불릿은 늘 보이고 세부 불릿(질문 → 답)은 접힘. 일회성 편집."""
ROOT = '/home/user/learning_tokens/web/v5/'

p = ROOT + 'build.py'
s = open(p, encoding='utf-8').read()
a = '''        if art and SELFTEST_RE.search(s["h"]):
            mark_answers(s["items"])'''
b = '''        if art and SELFTEST_RE.search(s["h"]):
            mark_answers(s["items"])
        if mode == "grid":  # 1층 카드: 세부 줄 "질문 → 답"을 나눠 둠
            for it in s["items"]:
                if it["k"] == "li" and it.get("d", 0) >= 1 and " → " in it["t"]:
                    q, a_ = it["t"].split(" → ", 1)
                    it["qa2"] = [q.strip(), a_.strip()]'''
assert s.count(a) == 1
s = s.replace(a, b)
open(p, 'w', encoding='utf-8').write(s)

p = ROOT + 'template.html'
s = open(p, encoding='utf-8').read()


def rep(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:80])
    s = s.replace(a, b)


rep(".cbox .li.d0 .tx strong{font-weight:700}", """.cbox .li.d0 .tx strong{font-weight:700}
.qg:not(.open)>.qas{display:none}
.qas{margin:2px 0 6px 14px;padding-left:8px;border-left:2px solid var(--line);display:grid;gap:2px}
.qas .li{padding-block:2px}
.qas .li .bul{width:8px}
.qtog{border:1px solid var(--line);background:var(--bg);color:var(--accent);border-radius:999px;font-size:11px;line-height:1.2;padding:1px 7px;margin-left:5px;vertical-align:1px;white-space:nowrap}
.qg.open>.ln .qtog{background:var(--accent);border-color:var(--accent);color:var(--panel)}
.qtog.hasans{box-shadow:inset 0 0 0 2px var(--ok)}
.qq2{font-weight:700;color:var(--accent)}
.qarr{color:var(--faint);margin:0 3px}
.lhead .qall{margin-left:auto;border:1px solid var(--line);background:var(--panel);border-radius:7px;padding:2px 10px;font-size:12.5px}""")

rep("function docHTML(doc, kind){", r"""function gridItems(list){
  let out = '', grp = null;
  const flush = () => { if (!grp) return; const n = grp.subs.length, isQ = grp.subs.some(x => x.qa2);
    const tog = n ? `<button type="button" class="qtog" data-qtog aria-expanded="false">${isQ ? '질문' : '세부'} ${n}</button>` : '';
    out += `<div class="qg">${grp.head.replace('<!--QTOG-->', tog)}${n ? `<div class="qas">${grp.subs.map(subHTML).join('')}</div>` : ''}</div>`; grp = null; };
  const subHTML = it => it.qa2
    ? `<div class="ln li d0" id="${it.id}"><span class="bul"></span><div class="tx"><span class="qq2">${inl(it.qa2[0])}</span><span class="qarr">→</span>${inl(it.qa2[1])}</div>${MB}</div>`
    : itemHTML(Object.assign({}, it, {d: Math.max(0, (it.d || 1) - 1)}));
  for (const it of (list || [])){
    if (it.k === 'li' && !(it.d > 0)){ flush(); grp = {head: `<div class="ln li d0${it.n ? ' ol' : ''}" id="${it.id}"><span class="bul">${it.n ? esc(it.n) + '.' : ''}</span><div class="tx">${inl(it.t)}<!--QTOG--></div>${MB}</div>`, subs: []}; }
    else if (it.k === 'li' && grp) grp.subs.push(it);
    else { flush(); out += itemHTML(it); }
  }
  flush();
  return out;
}
function docHTML(doc, kind){""")
rep("""  if (kind === 'grid') return h + `<div class="cgrid">${doc.secs.map(s => `<section class="cbox gblk" id="${s.id}" data-sec="카드: ${esc(s.h)}"><h3>${inl(s.h)}</h3>${items(s.items)}</section>`).join('')}</div>`;""",
    """  if (kind === 'grid') return h + `<div class="cgrid">${doc.secs.map(s => `<section class="cbox gblk" id="${s.id}" data-sec="카드: ${esc(s.h)}"><h3>${inl(s.h)}</h3>${gridItems(s.items)}</section>`).join('')}</div>`;""")
rep("""<h2>${esc(L.label)}</h2>${L.parts.length === 1 ? `<code>${esc(L.parts[0].path)}</code>` : ''}</div>`;""",
    """<h2>${esc(L.label)}</h2>${L.parts.length === 1 ? `<code>${esc(L.parts[0].path)}</code>` : ''}${L.kind === 'grid' && L.parts.some(P => P.doc && P.doc.secs.some(x => x.items.some(it => it.k === 'li' && it.d > 0))) ? '<button type="button" class="qall" data-act="qaall">질문 모두 펼치기</button>' : ''}</div>`;""")
rep("function openUp(el){ for (let p = el; p; p = p.parentElement) if (p.tagName === 'DETAILS' && !p.open) p.open = true; }",
    "function openUp(el){ for (let p = el; p; p = p.parentElement){ if (p.tagName === 'DETAILS' && !p.open) p.open = true; if (p.classList && p.classList.contains('qg') && !p.classList.contains('open')) setQg(p, true); } }\n"
    "function setQg(g, on){ g.classList.toggle('open', on); const b = g.querySelector(':scope > .ln .qtog'); if (b) b.setAttribute('aria-expanded', String(on)); }")
rep("    if (a === 'openall') $$('details.sec', MAIN).forEach(d => d.open = true);",
    """    if (a === 'qaall'){ const gs = $$('.qg', act.closest('.layer') || MAIN).filter(g => g.querySelector('.qas')); const on = gs.some(g => !g.classList.contains('open')); gs.forEach(g => setQg(g, on)); act.textContent = on ? '질문 모두 접기' : '질문 모두 펼치기'; }
    if (a === 'openall') $$('details.sec', MAIN).forEach(d => d.open = true);""")
rep("  const mb = t.closest('[data-mb]'); if (mb){ openMemo(ctxFrom(mb)); return; }",
    """  const qt = t.closest('[data-qtog]'); if (qt){ const g = qt.closest('.qg'); setQg(g, !g.classList.contains('open')); return; }
  const mb = t.closest('[data-mb]'); if (mb){ openMemo(ctxFrom(mb)); return; }""")
# 답 꼬리표가 접힌 세부 줄에 있으면 "질문 n" 단추에 초록 테두리
rep("  bySec.forEach((mids, s) => addBadge(s, mids[0], mids.length));  // 줄을 모르는 답은 칸 머리에 하나로 모음",
    "  bySec.forEach((mids, s) => addBadge(s, mids[0], mids.length));  // 줄을 모르는 답은 칸 머리에 하나로 모음\n"
    "  $$('.qtog', MAIN).forEach(b => b.classList.toggle('hasans', !!b.closest('.qg').querySelector('.qas .ha')));")
# 글 그림과 같은 이유로 단추 글자는 메모 인용과 찾기 칠하기에서 빠져야 함: 단추는 button이라 이미 빠짐
open(p, 'w', encoding='utf-8').write(s)
print('ok')
