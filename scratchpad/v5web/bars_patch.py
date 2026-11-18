"""md 카드의 ```막대 블록을 가로 누적 막대로 그림 + 매출 층(LR) 추가.
블록 모양:
```
막대: 해마다 순매출 구성(억 달러)
2020 | 손님 주문 7.20 | 맡긴 돈 1.77 | 그 밖 0.61 # 순이익 0.07
```
"""
from pathlib import Path
p = Path("web/v5/template.html"); s = p.read_text()

CSS = """
/* 누적 막대(매출 구성) */
.bars{--s1:#2a78d6;--s2:#eb6834;--s3:#1baf7a;--s4:#eda100;--s5:#6250d6;margin:6px 0 10px;font-size:13px}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]) .bars{--s1:#3987e5;--s2:#d95926;--s3:#199e70;--s4:#c98500;--s5:#9085e9}}
:root[data-theme="dark"] .bars{--s1:#3987e5;--s2:#d95926;--s3:#199e70;--s4:#c98500;--s5:#9085e9}
.bars .bt{font-weight:700;margin-bottom:4px}
.bars .lg{display:flex;flex-wrap:wrap;gap:4px 14px;color:var(--muted);margin-bottom:6px}
.bars .lg i{display:inline-block;width:11px;height:11px;border-radius:3px;margin-right:5px;vertical-align:-1px}
.bars .br{display:grid;grid-template-columns:4.2em minmax(0,1fr) minmax(4.5em,max-content);gap:8px;align-items:center;padding:3px 0}
.bars .bl{color:var(--muted);white-space:nowrap}
.bars .bk{display:flex;height:18px;min-width:0}
.bars .bk span{height:100%;margin-right:2px;min-width:2px}
.bars .bk span:last-child{margin-right:0;border-radius:0 4px 4px 0}
.bars .bv{white-space:nowrap;font-variant-numeric:tabular-nums}
.bars .bv small{color:var(--muted);margin-left:6px}
@media (max-width:640px){.bars .br{grid-template-columns:3.6em minmax(0,1fr)}.bars .bv{grid-column:2}}
"""
anchor = "strong.warn{color:var(--warn)}"
assert anchor in s
s = s.replace(anchor, anchor + CSS, 1)

JS = r"""function barsHTML(t){
  const L = t.split('\n').map(x => x.trim()).filter(Boolean);
  const title = L[0].replace(/^막대:\s*/, '');
  const names = [], rows = [];
  for (const ln of L.slice(1)){
    const [main, note] = ln.split('#');
    const parts = main.split('|').map(x => x.trim()).filter(Boolean);
    const segs = parts.slice(1).map(x => { const m = x.match(/^(.*?)\s+(-?[\d.,]+)$/); return m ? {n: m[1].trim(), v: parseFloat(m[2].replace(/,/g, ''))} : null; }).filter(Boolean);
    segs.forEach(g => { if (!names.includes(g.n)) names.push(g.n); });
    rows.push({lab: parts[0], segs, note: (note || '').trim()});
  }
  const tot = r => r.segs.reduce((a, g) => a + Math.max(0, g.v), 0);
  const max = Math.max(...rows.map(tot), 1e-9);
  const col = n => `var(--s${(names.indexOf(n) % 5) + 1})`;
  const fmt = v => (Math.round(v * 100) / 100).toLocaleString('ko-KR');
  let h = `<div class="bars" role="img" aria-label="${esc(title)}"><div class="bt">${esc(title)}</div><div class="lg">${names.map(n => `<span><i style="background:${col(n)}"></i>${esc(n)}</span>`).join('')}</div>`;
  for (const r of rows){
    const T = tot(r);
    h += `<div class="br"><span class="bl">${esc(r.lab)}</span><span class="bk" style="width:${(T / max * 100).toFixed(2)}%">${r.segs.filter(g => g.v > 0).map(g => `<span style="flex:${g.v} 1 0;background:${col(g.n)}" title="${esc(r.lab + ' ' + g.n + ': ' + fmt(g.v) + ' (' + Math.round(g.v / T * 100) + '%)')}"></span>`).join('')}</span><span class="bv">${fmt(T)}${r.note ? `<small>${esc(r.note)}</small>` : ''}</span></div>`;
  }
  return h + '</div>';
}
"""
anchor2 = "function docHTML(doc, kind){"
assert anchor2 in s
s = s.replace(anchor2, JS + anchor2, 1)

old = "  if (it.k === 'pre') return `<div class=\"ln artw\" id=\"${it.id}\"><pre class=\"art\">${esc(it.t)}</pre>${MB}</div>`;"
assert old in s
s = s.replace(old, "  if (it.k === 'pre' && /^막대:/.test(it.t)) return `<div class=\"ln barsw\" id=\"${it.id}\">${barsHTML(it.t)}${MB}</div>`;\n" + old, 1)
s = s.replace("const LAYER_SHORT = {L1: '카드', L2: '쉬운 해설', L3: '개요 문서'};", "const LAYER_SHORT = {L1: '카드', LR: '매출로 본 원인', L2: '쉬운 해설', L3: '개요 문서'};", 1)
p.write_text(s)

b = Path("web/v5/build.py"); t = b.read_text()
old = '        ("L1", "한 화면 카드", "grid", ["kb/cards6/{s}.md"]),\n        ("L2", "쉬운 해설", "easy", ["kb/easy/{s}.md"]),'
assert old in t
t = t.replace(old, '        ("L1", "한 화면 카드", "grid", ["kb/cards6/{s}.md"]),\n        ("LR", "매출로 본 성공 원인", "doc", ["kb/revenue/{s}.md"]),\n        ("L2", "쉬운 해설", "easy", ["kb/easy/{s}.md"]),', 1)
old = '        ("L1", "한 화면 카드", "grid", ["kb/cards6/common.md"]),\n        ("L2", "쉬운 해설", "easy", ["kb/easy/00_기초.md"]),'
assert old in t
t = t.replace(old, '        ("L1", "한 화면 카드", "grid", ["kb/cards6/common.md"]),\n        ("LR", "매출로 본 성공 원인", "doc", ["kb/revenue/00_공통.md"]),\n        ("L2", "쉬운 해설", "easy", ["kb/easy/00_기초.md"]),', 1)
b.write_text(t)
print("ok")
