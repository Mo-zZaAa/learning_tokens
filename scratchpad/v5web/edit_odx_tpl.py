"""template.html: Ondo 1층 ODX 카드. 일회성 편집."""
p = '/home/user/learning_tokens/web/v5/template.html'
s = open(p, encoding='utf-8').read()


def rep(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:80])
    s = s.replace(a, b)


# ---- CSS ----
rep(".qg:not(.open)>.qas{display:none}", """/* ODX 카드(개요 패키지): 왼쪽 줄 이름, 오른쪽 내용 */
.odx{background:var(--panel);border:1px solid var(--line);border-top:4px solid var(--navy);border-radius:14px;padding:16px 22px 18px;max-width:1180px}
.odx-hd{display:flex;flex-wrap:wrap;align-items:baseline;gap:4px 12px;padding-bottom:10px;border-bottom:1px dashed var(--line)}
.odx-hd b{font-size:22px;color:var(--navy);border-bottom:2px dotted var(--navy)}
.odx-hd span{color:var(--muted)}
.orow{display:grid;grid-template-columns:140px minmax(0,1fr);gap:18px;padding:12px 0;border-bottom:1px dashed var(--line)}
.orow:last-child{border-bottom:0}
.olab{margin:0;font-size:15px;font-weight:700;color:var(--navy)}
.orow.danger .olab{color:var(--warn)}
.obody{min-width:0}
.obody ul.omain,.obody ol.omain{margin:0;padding-left:20px}
.obody .omain>li{margin:0 0 6px}
.obody li.strong>.oi>.tx{color:var(--navy);font-weight:700}
.obody ul.osub{margin:4px 0 2px;padding-left:18px}
.obody ul.osub li{margin:2px 0}
.oi{padding-right:28px}
.oi .tx{overflow-wrap:anywhere}
.tg{display:inline-block;font-size:11.5px;line-height:1.5;padding:0 7px;border-radius:5px;margin-left:5px;vertical-align:1px;border:0;cursor:pointer;font-family:var(--sans)}
.tg-s{background:var(--accent-soft);color:var(--accent)}
.tg-n{background:var(--ok-soft);color:var(--ok)}
.tg-i{background:var(--memo-soft);color:var(--memo)}
.tg-e{background:var(--judge-soft);color:var(--judge)}
.tg-u{background:var(--mid-soft);color:var(--mid)}
details.omore,details.ofig{margin:4px 0}
details.omore>summary,details.ofig>summary{cursor:pointer;color:var(--muted);font-size:12.5px;list-style:none;display:inline-block;padding:1px 9px;border:1px solid var(--line);border-radius:999px;background:var(--bg)}
details.omore>summary::-webkit-details-marker,details.ofig>summary::-webkit-details-marker{display:none}
details.omore>summary::before,details.ofig>summary::before{content:"\\25B8  ";color:var(--faint)}
details.omore[open]>summary::before,details.ofig[open]>summary::before{content:"\\25BE  "}
details.ofig>summary{color:var(--memo);border-color:color-mix(in srgb,var(--memo) 35%,var(--line));background:var(--memo-soft)}
.onote{margin:4px 0 6px}
.opath{display:grid;grid-template-columns:100px minmax(0,1fr);gap:8px 14px}
.opk{color:var(--accent);font-weight:700}
.opv{min-width:0}
.opv .k2{text-decoration:underline;text-underline-offset:3px;margin-right:4px}
.tip .rq{margin:4px 0 8px;padding-left:8px;border-left:2px solid var(--line);color:var(--ink);font-size:12.5px;overflow-wrap:anywhere}
.tip .rt{font-weight:600;font-size:12.5px;overflow-wrap:anywhere}
.tip .rf{font-family:var(--mono);font-size:11px;color:var(--faint);margin-left:4px}
.tip.ref{max-height:min(60vh,420px);overflow:auto}
@media (max-width:760px){.odx{padding:12px 14px}.orow{grid-template-columns:1fr;gap:6px}.opath{grid-template-columns:1fr;gap:2px}.opath .opv{margin-bottom:8px}}
/*__FLOW_CSS__*/
.qg:not(.open)>.qas{display:none}""")
rep("--sans:\"Pretendard\"", "--navy:#1f3a6e;\n  --sans:\"Pretendard\"")
rep("--memo:#c9a2f5; --memo-soft:#2b2140; --on-memo:#1d1230; --shade:rgba(0,0,0,.55); --scrim:rgba(0,0,0,.55); color-scheme:dark}}",
    "--memo:#c9a2f5; --memo-soft:#2b2140; --on-memo:#1d1230; --shade:rgba(0,0,0,.55); --scrim:rgba(0,0,0,.55); --navy:#a9c1f2; color-scheme:dark}}")
rep("--memo:#c9a2f5; --memo-soft:#2b2140; --on-memo:#1d1230; --shade:rgba(0,0,0,.55); --scrim:rgba(0,0,0,.55); color-scheme:dark}\n",
    "--memo:#c9a2f5; --memo-soft:#2b2140; --on-memo:#1d1230; --shade:rgba(0,0,0,.55); --scrim:rgba(0,0,0,.55); --navy:#a9c1f2; color-scheme:dark}\n")

# ---- JS: ODX 카드 ----
rep("function docHTML(doc, kind){", r"""const TGK = {s: 'tg-s', n: 'tg-n', i: 'tg-i', e: 'tg-e', u: 'tg-u'};
let ODX = null;   // 지금 그리는 카드(태그 풀이)
function tagsHTML(tags){
  return (tags || []).map(t => { const r = ODX && ODX.tags[t]; const k = r ? r.k : 's'; return `<button type="button" class="tg ${TGK[k] || 'tg-s'}" data-tg="${esc(t)}">${esc(t)}</button>`; }).join('');
}
function odxTable(t){ return tableHTML({cols: t.cols, rows: t.rows}, {gblk: false}); }
function odxKids(list){ return list && list.length ? `<ul class="osub">${list.map(k => odxItem(k, 1)).join('')}</ul>` : ''; }
function odxItem(it, depth){
  let h = `<li class="${it.strong ? 'strong' : ''}"><div class="ln oi" id="${it.id}"><span class="tx">${inl(it.t)}</span>${tagsHTML(it.tags)}${MB}</div>`;
  if (it.flow && it.note) h += `<div class="onote">${ODX.flows[it.flow] || ''}</div>`;
  else if (it.flow) h += `<details class="ofig"><summary>그림: ${esc(ODX.ftitles[it.flow] || it.flow)}</summary>${ODX.flows[it.flow] || ''}</details>`;
  const kids = it.kids || [], n = kids.length + (it.table ? 1 : 0);
  if (depth === 0 && n) h += `<details class="omore"><summary>세부 ${n}</summary>${it.table ? odxTable(it.table) : ''}${odxKids(kids)}</details>`;
  else h += (it.table ? odxTable(it.table) : '') + odxKids(kids);
  return h + '</li>';
}
function odxPath(p){
  let h = `<div class="opk">${esc(p.k)}</div><div class="opv">`;
  if (p.t) h += `<div class="ln oi" id="${p.id}"><span class="tx">${inl(p.t)}</span>${tagsHTML(p.tags)}${MB}</div>`;
  for (const s2 of (p.sub || [])) h += `<div class="ln oi" id="${s2.id}"><span class="tx"><span class="k2">${esc(s2.k2 || '')}</span>${inl(s2.t)}</span>${tagsHTML(s2.tags)}${MB}</div>`;
  const kids = p.kids || [];
  if (kids.length) h += `<details class="omore"><summary>세부 ${kids.length}</summary>${odxKids(kids)}</details>`;
  return h + '</div>';
}
function odxHTML(o){
  ODX = o;
  const c = o.card;
  let h = `<div class="odx"><div class="odx-hd"><b>${esc(c.name)}</b><span>${esc(c.sub || '')}</span></div>`;
  for (const r of c.rows){
    let body;
    if (r.path) body = `<div class="opath">${r.path.map(odxPath).join('')}</div>`;
    else { const tag = r.numbered ? 'ol' : 'ul'; body = `<${tag} class="omain">${(r.items || []).map(it => odxItem(it, 0)).join('')}</${tag}>`; }
    h += `<div class="orow${r.danger ? ' danger' : ''}" id="${r.id}" data-sec="카드: ${esc(r.label)}"><h3 class="olab">${esc(r.label)}</h3><div class="obody gblk">${body}</div></div>`;
  }
  return h + '</div>';
}
function showRefTip(el){
  const t = el.dataset.tg, r = ODX && ODX.tags[t];
  clearTimeout(tipT);
  let body;
  if (!r) body = '<p>풀이 없음</p>';
  else if (r.k === 'i') body = '<p>해석: 공개 자료로 바로 확인되지 않는 풀이(판단)</p>';
  else if (r.k === 'e') body = '<p>추정: 공개 숫자로 직접 계산한 값</p>';
  else if (r.k === 'u') body = '<p>사용자 확인이 필요한 줄</p>';
  else body = (r.items.length ? r.items.map(x => `<div class="rt">${x.url ? link(x.url, x.t || shortUrl(x.url)) : esc(x.t)}${x.f ? `<span class="rf">${esc(x.f)}</span>` : ''}</div>${x.q ? `<div class="rq">"${esc(x.q)}"</div>` : ''}`).join('') : '<p>연결된 원문 없음</p>')
    + (r.k === 's' ? `<div class="ts">옛 화면 본문 줄 ${esc(t)}${r.row ? ': ' + esc(r.row) : ''}</div>` : '<div class="ts">새 출처(개요 패키지 sources_new.csv)</div>');
  TIP.innerHTML = `<div class="tt"><b>${esc(t)}</b></div>${body}`;
  TIP.classList.add('ref'); TIP.hidden = false; tipFor = el;
  const rc = el.getBoundingClientRect(), w = TIP.offsetWidth, hh = TIP.offsetHeight;
  let x = Math.min(Math.max(8, rc.left), window.innerWidth - w - 8), y = rc.bottom + 6;
  if (y + hh > window.innerHeight - 8) y = Math.max(8, rc.top - hh - 6);
  TIP.style.left = x + 'px'; TIP.style.top = y + 'px';
}
function docHTML(doc, kind){""")
rep("""      ph += P.doc ? docHTML(P.doc, L.kind) : ready(P.label, P.path);""",
    """      ph += P.odx ? odxHTML(P.odx) : P.doc ? docHTML(P.doc, L.kind) : ready(P.label, P.path);""")
rep("function hasOv(C){ return C.ov.layers.some(L => L.parts.some(p => p.doc)); }",
    "function hasOv(C){ return C.ov.layers.some(L => L.parts.some(p => p.doc || p.odx)); }")
rep("""<a href="#${L.id}" data-go="${L.id}"${L.parts.some(p => p.doc) ? '' : ' class="off"'}>""",
    """<a href="#${L.id}" data-go="${L.id}"${L.parts.some(p => p.doc || p.odx) ? '' : ' class="off"'}>""")
# 풍선 띄울 때 ref 모양 지우기
rep("  TIP.innerHTML = `<div class=\"tt\"><b>${esc(e[0])}</b>", "  TIP.classList.remove('ref');\n  TIP.innerHTML = `<div class=\"tt\"><b>${esc(e[0])}</b>")
# 태그 누르면 풀이
rep("  const term = t.closest('.term');", "  const tg = t.closest('[data-tg]'); if (tg){ if (tipFor === tg && !TIP.hidden) closeTip(); else showRefTip(tg); return; }\n  const term = t.closest('.term');")
# 마우스가 풍선을 떠날 때 ref 풍선은 닫지 않음(누른 것이라)
rep("document.addEventListener('mouseout', e => { if (e.target.closest && (e.target.closest('.term') || e.target.closest('#tip'))){ clearTimeout(tipT); tipT = setTimeout(closeTip, 260); } });",
    "document.addEventListener('mouseout', e => { if (TIP.classList.contains('ref')) return; if (e.target.closest && (e.target.closest('.term') || e.target.closest('#tip'))){ clearTimeout(tipT); tipT = setTimeout(closeTip, 260); } });")
rep("window.addEventListener('scroll', () => { if (!TIP.hidden && lastPtr === 'mouse') closeTip(); }, {passive: true});",
    "window.addEventListener('scroll', () => { if (!TIP.hidden && lastPtr === 'mouse' && !TIP.classList.contains('ref')) closeTip(); }, {passive: true});")
# 찾기: 카드 줄
rep("""    C.ov.layers.forEach(L => L.parts.forEach(P => { if (!P.doc) return;""",
    """    C.ov.layers.forEach(L => L.parts.forEach(P => { if (P.odx){ const w2 = (it, sec) => { add('o', sec, it.id, (it.k2 ? it.k2 + ' ' : '') + (it.t || '') + ' ' + (it.tags || []).join(' ')); if (it.table) it.table.rows.forEach(r => add('o', sec, r.id, r.c.join(' | '))); (it.sub || []).forEach(x => w2(x, sec)); (it.kids || []).forEach(x => w2(x, sec)); };
      P.odx.card.rows.forEach(r => (r.items || r.path || []).forEach(it => w2(it, `${L.label} > ${r.label}`))); return; }
      if (!P.doc) return;""")
open(p, 'w', encoding='utf-8').write(s)
print('ok')
