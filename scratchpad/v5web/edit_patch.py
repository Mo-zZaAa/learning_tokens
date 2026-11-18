from pathlib import Path
p = Path("web/v5/template.html"); s = p.read_text()
CSS = """
/* 표 너비 조절 */
.fw-tb th{position:relative}
.rzh{position:absolute;top:0;right:-4px;width:8px;height:100%;cursor:col-resize;z-index:3;touch-action:none}
.rzh::after{content:"";position:absolute;top:20%;bottom:20%;left:3px;width:2px;border-radius:2px;background:var(--line)}
.rzh:hover::after,.rzing .rzh::after{background:var(--pmq)}
table.rz{table-layout:fixed}
table.rz th{white-space:normal;overflow:hidden}
table.rz td{max-width:none;min-width:0}
body.rzing{cursor:col-resize;user-select:none}
/* 화면에서 고치기 */
.edbtn[aria-pressed="true"]{background:var(--pmq-bg);color:var(--pmq);border-color:var(--pmq)}
body.editing main .ln[id]{cursor:text}
body.editing main .ln[id]:not(tr):hover,body.editing main tr.ln td:not(.mc):hover{outline:1.5px dashed var(--pmq);outline-offset:1px;border-radius:4px}
.eded:not(tr){box-shadow:inset 3px 0 0 var(--pmq)}
td.eded{box-shadow:inset 0 0 0 1.5px var(--pmq)}
body:not(.editing) .edel{display:none!important}
body.editing .edel{opacity:.45;text-decoration:line-through}
.edbar{position:fixed;left:50%;transform:translateX(-50%);bottom:14px;z-index:60;display:flex;gap:8px;align-items:center;flex-wrap:wrap;justify-content:center;background:var(--panel);border:1px solid var(--pmq);border-radius:14px;padding:7px 10px 7px 14px;box-shadow:0 8px 24px var(--shade);font-size:13.5px;max-width:calc(100vw - 24px)}
.edbar button{border:1px solid var(--line);background:var(--panel);border-radius:8px;padding:4px 10px;font-size:13px}
.ehint{font-size:12.5px;color:var(--muted);margin:0}
.mbtns .left{margin-right:auto}
@media (max-width:760px){.rzh{display:none}table.rz{width:auto!important;table-layout:auto}}
"""
anchor = "strong.warn{color:var(--warn)}"
assert anchor in s
s = s.replace(anchor, anchor + CSS, 1)
btn_anchor = '<button type="button" id="memoBtn"'
assert btn_anchor in s
s = s.replace(btn_anchor, '<button type="button" id="edBtn" class="memobtn edbtn" aria-pressed="false" title="줄이나 표 칸을 눌러 직접 고치거나 지움">고치기 <b id="ecount">0</b></button>\n    ' + btn_anchor, 1)
DLG = """
<div id="edlg" class="modal" hidden>
  <form id="eform" class="mbox" role="dialog" aria-modal="true" aria-labelledby="edT">
    <h2 id="edT">고치기</h2>
    <div class="mloc" id="eloc"></div>
    <textarea id="etext" rows="7"></textarea>
    <p class="ehint">==형광펜==, **굵게**, !!빨간 글자!! 표시를 그대로 쓸 수 있음. 저장하면 이 페이지를 여는 사람 모두에게 보이고, 원래대로를 누르면 처음 글로 돌아감</p>
    <div class="mbtns"><button type="button" class="left" data-eact="del">지우기</button><button type="button" class="left" data-eact="delrow" hidden>이 행 지우기</button><button type="button" data-eact="reset">원래대로</button><button type="button" data-eact="cancel">취소</button><button type="submit" class="primary">저장</button></div>
  </form>
</div>
<div id="edbar" class="edbar" hidden><span>고치기 켜짐: 줄이나 표 칸을 누르면 고침</span><span>고친 곳 <b id="ecount2">0</b></span><button type="button" data-eact="dl">고친 곳 내려받기</button><button type="button" data-eact="off">끄기</button></div>
"""
dlg_anchor = '<div id="toast" class="toast" role="status" hidden></div>'
assert dlg_anchor in s
s = s.replace(dlg_anchor, dlg_anchor + DLG, 1)
JS = r"""
/* ---------- 표 너비 조절(엑셀처럼 머리 칸 오른쪽 끝을 끌기, 두 번 누르면 되돌림) ---------- */
const RZK = 'kdx-v5-colw';
let RZ = {}; try { RZ = JSON.parse(localStorage.getItem(RZK) || '{}') || {}; } catch(e){ RZ = {}; }
function tblKey(tb){ if (tb.id) return tb.id; const r = tb.querySelector('tr.ln[id]'); if (r) return 't:' + r.id; return 'h:' + cur + ':' + $$('th', tb).map(x => x.textContent).join('|').slice(0, 120); }
function rzSave(){ try { localStorage.setItem(RZK, JSON.stringify(RZ)); } catch(e){} }
function freezeTbl(tb){
  if (tb.classList.contains('rz')) return;
  const ths = $$('thead th', tb);
  const ws = ths.map(th => th.getBoundingClientRect().width);
  ths.forEach((th, i) => { th.style.width = ws[i] + 'px'; });
  tb.style.width = ws.reduce((a, b) => a + b, 0) + 'px';
  tb.classList.add('rz');
}
function addResizers(root){
  $$('table.tbl, table.fw-tb', root).forEach(tb => {
    const ths = $$('thead th', tb);
    ths.forEach(th => { if (th.classList.contains('mc') || th.querySelector('.rzh')) return; const h = document.createElement('span'); h.className = 'rzh'; h.title = '끌어서 너비 조절, 두 번 누르면 되돌림'; th.appendChild(h); });
    const ws = RZ[tblKey(tb)];
    if (ws && ws.length === ths.length){ ths.forEach((th, i) => { th.style.width = ws[i] + 'px'; }); tb.style.width = ws.reduce((a, b) => a + b, 0) + 'px'; tb.classList.add('rz'); }
  });
}
let rzD = null;
document.addEventListener('pointerdown', e => {
  const h = e.target.closest && e.target.closest('.rzh'); if (!h) return;
  e.preventDefault(); e.stopPropagation();
  const th = h.parentElement, tb = th.closest('table');
  freezeTbl(tb);
  rzD = {th, tb, x: e.clientX, w: parseFloat(th.style.width), tw: parseFloat(tb.style.width)};
  try { h.setPointerCapture(e.pointerId); } catch(err){}
  document.body.classList.add('rzing');
}, true);
document.addEventListener('pointermove', e => {
  if (!rzD) return;
  const w = Math.max(48, rzD.w + e.clientX - rzD.x);
  rzD.th.style.width = w + 'px'; rzD.tb.style.width = (rzD.tw + w - rzD.w) + 'px';
});
document.addEventListener('pointerup', () => {
  if (!rzD) return;
  const tb = rzD.tb; rzD = null; document.body.classList.remove('rzing');
  RZ[tblKey(tb)] = $$('thead th', tb).map(th => Math.round(parseFloat(th.style.width) || th.getBoundingClientRect().width));
  rzSave();
});
document.addEventListener('dblclick', e => {
  const h = e.target.closest && e.target.closest('.rzh'); if (!h) return;
  const tb = h.closest('table'); tb.classList.remove('rz'); tb.style.width = ''; $$('thead th', tb).forEach(th => { th.style.width = ''; });
  delete RZ[tblKey(tb)]; rzSave();
});

/* ---------- 화면에서 고치기: 줄 id(표는 행 id|칸 번호)마다 고친 글 또는 지움을 저장 ---------- */
const EKEY = 'kdx-v5-edits';
let ED = {}; try { ED = JSON.parse(localStorage.getItem(EKEY) || '{}') || {}; } catch(e){ ED = {}; }
let editing = false, EK = null, RAW = null, RAWco = null;
const OH = {};
function edPersist(){ try { localStorage.setItem(EKEY, JSON.stringify(ED)); } catch(e){} }
function edDocId(k){ return 'e_' + k.replace(/[^A-Za-z0-9_-]/g, c => '_' + c.charCodeAt(0).toString(16)); }
function edCount(){ const n = Object.keys(ED).length; $('#ecount').textContent = n; $('#ecount2').textContent = n; }
function rawIdx(){
  if (RAW && RAWco === cur) return RAW;
  RAW = {}; RAWco = cur;
  const seen = new Set();
  const walk = o => {
    if (!o || typeof o !== 'object' || seen.has(o)) return; seen.add(o);
    if (Array.isArray(o)){ o.forEach(walk); return; }
    if (typeof o.id === 'string'){ if (typeof o.t === 'string' && !(o.id in RAW)) RAW[o.id] = o.t; else if (Array.isArray(o.c)) RAW[o.id] = o.c; }
    for (const k in o) if (o[k] && typeof o[k] === 'object') walk(o[k]);
  };
  walk(D.C[cur]);
  return RAW;
}
function edTarget(k){
  const i = k.indexOf('|');
  if (i < 0){ const el = document.getElementById(k); return {el, cell: null}; }
  const tr = document.getElementById(k.slice(0, i));
  return {el: tr, cell: tr && tr.cells ? tr.cells[+k.slice(i + 1)] : null};
}
function edBox(el){ return el.classList.contains('oi') && el.parentElement && el.parentElement.tagName === 'LI' ? el.parentElement : el; }
function edSlot(el, cell){
  if (cell){ let cv = cell.querySelector('.cv'); if (!cv){ cell.classList.remove('e'); cv = document.createElement('div'); cv.className = 'cv'; cell.appendChild(cv); } return cv; }
  return el.querySelector('.tx') || el.querySelector('pre') || el;
}
function applyOne(k){
  const e = ED[k]; const {el, cell} = edTarget(k); if (!el || !e) return;
  if (cell){ const cv = edSlot(el, cell); if (!(k in OH)) OH[k] = cv.innerHTML; cv.innerHTML = e.del ? '' : inl(e.t); cell.classList.add('eded'); return; }
  if (e.del){ edBox(el).classList.add('edel'); return; }
  const tx = edSlot(el, null); if (!(k in OH)) OH[k] = tx.innerHTML;
  if (tx.tagName === 'PRE') tx.textContent = e.t; else tx.innerHTML = inl(e.t);
  el.classList.add('eded');
}
function applyEdits(){ for (const k in ED) if (ED[k].co === cur) applyOne(k); }
function unapply(k){
  const {el, cell} = edTarget(k); if (!el) return;
  if (cell){ if (k in OH) edSlot(el, cell).innerHTML = OH[k]; cell.classList.remove('eded'); return; }
  edBox(el).classList.remove('edel'); el.classList.remove('eded');
  if (k in OH){ const tx = edSlot(el, null); tx.innerHTML = OH[k]; }
}
function setEditing(on){
  editing = on; document.body.classList.toggle('editing', on);
  $('#edBtn').setAttribute('aria-pressed', String(on)); $('#edbar').hidden = !on;
  if (on) toast('줄이나 표 칸을 누르면 고칠 수 있음');
}
function openEditor(k){
  const {el, cell} = edTarget(k); if (!el) return;
  const ri = rawIdx(), i = k.indexOf('|');
  let base = i >= 0 ? (Array.isArray(ri[k.slice(0, i)]) ? String(ri[k.slice(0, i)][+k.slice(i + 1)] || '') : '') : (typeof ri[k] === 'string' ? ri[k] : '');
  if (!base){ const src = cell ? cell : (el.querySelector('.tx') || el.querySelector('pre') || el); base = (k in OH ? (() => { const d = document.createElement('div'); d.innerHTML = OH[k]; return d.innerText; })() : src.innerText || '').trim(); }
  const e = ED[k];
  EK = {k, base};
  $('#etext').value = e && !e.del ? e.t : base;
  const sec = el.closest('[data-sec]');
  $('#eloc').textContent = (D.C[cur].name || cur) + (sec ? ' > ' + sec.dataset.sec : '') + (cell ? ' > 표 칸' : '');
  $('[data-eact="del"]').textContent = cell ? '칸 비우기' : '줄 지우기';
  $('[data-eact="delrow"]').hidden = !cell;
  $('[data-eact="reset"]').hidden = !e;
  $('#edlg').hidden = false; $('#etext').focus();
}
function closeEditor(){ $('#edlg').hidden = true; EK = null; }
async function edPut(k, rec){
  if (rec) ED[k] = rec; else delete ED[k];
  edPersist(); edCount();
  const d = await CAP('db');
  if (!d){ toast(rec ? '이 브라우저에만 저장함' : '원래대로 되돌림'); return; }
  try {
    if (rec) await d.collection('edits').doc(edDocId(k)).set(rec);
    else await d.collection('edits').doc(edDocId(k)).delete();
    toast(rec ? '저장함(이 페이지를 여는 사람 모두에게 보임)' : '원래대로 되돌림');
  } catch(err){ toast('공유 저장이 안 돼 이 브라우저에만 남김'); }
}
function edRec(k, t, del){ return {v: 1, k, co: cur, t: t || '', del: !!del, orig: EK && EK.k === k ? EK.base : '', at: Date.now()}; }
$('#eform').addEventListener('submit', e => {
  e.preventDefault(); if (!EK) return;
  const k = EK.k, t = $('#etext').value.trim();
  if (t === EK.base.trim()){ if (ED[k]){ unapply(k); edPut(k, null); } closeEditor(); return; }
  const rec = edRec(k, t, !t); closeEditor(); unapply(k); ED[k] = rec; applyOne(k); edPut(k, rec);
});
$('#edlg').addEventListener('click', e => {
  const b = e.target.closest('[data-eact]'); if (!b){ if (e.target === $('#edlg')) closeEditor(); return; }
  if (!EK) return; const k = EK.k, a = b.dataset.eact;
  if (a === 'cancel'){ closeEditor(); return; }
  if (a === 'reset'){ closeEditor(); unapply(k); edPut(k, null); return; }
  if (a === 'del'){ const rec = edRec(k, '', true); closeEditor(); ED[k] = rec; applyOne(k); edPut(k, rec); return; }
  if (a === 'delrow'){ const rk = k.slice(0, k.indexOf('|')); EK = {k: rk, base: ''}; const rec = edRec(rk, '', true); closeEditor(); ED[rk] = rec; applyOne(rk); edPut(rk, rec); return; }
});
$('#edBtn').addEventListener('click', () => setEditing(!editing));
$('#edbar').addEventListener('click', async e => {
  const b = e.target.closest('[data-eact]'); if (!b) return;
  if (b.dataset.eact === 'off'){ setEditing(false); return; }
  if (b.dataset.eact === 'dl'){
    const dl = await CAP('downloads'); if (!dl){ toast('이 화면에서는 내려받기를 쓸 수 없음'); return; }
    const rows = [['회사', '줄 id', '처음 글', '고친 글', '지움', '시각']].concat(Object.values(ED).sort((a, b) => a.at - b.at).map(x => [x.co, x.k, x.orig || '', x.del ? '' : x.t, x.del ? '예' : '', new Date(x.at).toISOString()]));
    const csv = '﻿' + rows.map(r => r.map(c => '"' + String(c).replace(/"/g, '""') + '"').join(',')).join('\r\n');
    try { await dl.save({filename: 'kdx_고친곳.csv', data: new Blob([csv], {type: 'text/csv'})}); } catch(err){ if (err && err.code !== 'declined') toast('내려받기가 안 됨'); }
  }
});
document.addEventListener('click', e => {
  if (!editing) return;
  const t = e.target;
  if (!MAIN.contains(t) || t.closest('button, summary, a, input, textarea, select, .rzh, [data-tg], [data-mb]')) return;
  let k = null;
  const td = t.closest('tr.ln[id] > td');
  if (td){ if (!td.classList.contains('mc')) k = td.parentElement.id + '|' + td.cellIndex; }
  else { const ln = t.closest('.ln[id]'); if (ln) k = ln.id; }
  if (!k) return;
  e.preventDefault(); e.stopPropagation();
  openEditor(k);
}, true);
CAP('db').then(async d => {
  if (!d) return;
  try {
    const snap = await d.collection('edits').get(); let ch = false;
    snap.docs.forEach(doc => { const r = doc.data(); if (!r || !r.k || !r.co) return; const L = ED[r.k]; if (!L || (r.at || 0) > (L.at || 0)){ ED[r.k] = JSON.parse(JSON.stringify(r)); ch = true; } });
    if (ch){ edPersist(); render(); }
    edCount();
  } catch(e){}
});
edCount();
"""
hook = "window.addEventListener('hashchange', fromHash);"
assert hook in s
s = s.replace(hook, JS + hook, 1)
old = """  MAIN.innerHTML = view === 'o' ? renderOv(C) : renderRaw(C);
  glossIn(MAIN);
  markMemos();"""
assert old in s
s = s.replace(old, """  MAIN.innerHTML = view === 'o' ? renderOv(C) : renderRaw(C);
  applyEdits();
  glossIn(MAIN);
  markMemos();
  addResizers(MAIN);""", 1)
p.write_text(s); print("ok")
