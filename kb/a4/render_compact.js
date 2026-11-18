// 사용자 Robinhood A4(inputs/a4_261118/사용자_Robinhood_A4.docx) 모양 그대로 찍는 렌더러
// 사용법: node kb/a4/render_compact.js kraken binance coinbase  → deliverables/KDX_A4_간결_<slug>_261118.docx
const fs = require('fs'); const path = require('path');
const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType, ShadingType, AlignmentType,
  LevelFormat, BorderStyle, VerticalAlign, TableLayoutType } = require('docx');
const ROOT = path.resolve(__dirname, '../..');
const FONT = '맑은 고딕';
const C = { own: 'FBE5D6', h1: 'F2F2F2', h2: 'D9D9D9', accent: 'D04A02', gray: '808080', line: 'BFBFBF' };
const SZ = { t: 13, p: 15, title: 24 };
const SP = { after: 10, line: 232 };

function runs(text, o = {}) {
  const out = []; const re = /(\*\*[^*]+\*\*|●|\(판단\)|\(계산\)|\(매체 추정\)|\(회사 주장\))/g;
  const s = String(text || ''); let last = 0, m;
  const base = { font: FONT, size: o.size || SZ.p, bold: o.bold, color: o.color };
  while ((m = re.exec(s))) {
    if (m.index > last) out.push(new TextRun({ ...base, text: s.slice(last, m.index) }));
    const t = m[0];
    if (t.startsWith('**')) out.push(new TextRun({ ...base, text: t.slice(2, -2), bold: true }));
    else if (t === '●') out.push(new TextRun({ ...base, text: '●', bold: true, color: C.accent }));
    else out.push(new TextRun({ ...base, text: t, color: C.gray }));
    last = re.lastIndex;
  }
  if (last < s.length) out.push(new TextRun({ ...base, text: s.slice(last) }));
  return out;
}
const para = (t, o = {}) => new Paragraph({ spacing: { after: o.after ?? SP.after, line: SP.line }, numbering: o.num, indent: o.indent, children: runs(t, o) });
const lines = (t, o = {}) => String(t || '').split('\n').map(x => para(x, { ...o, after: 0 }));

const border = { style: BorderStyle.SINGLE, size: 4, color: C.line };
const borders = { top: border, bottom: border, left: border, right: border };
function cell(children, width, o = {}) {
  return new TableCell({ width: { size: width, type: WidthType.DXA }, columnSpan: o.span || 1, borders,
    shading: o.fill ? { type: ShadingType.CLEAR, color: 'auto', fill: o.fill } : undefined,
    margins: { top: 10, bottom: 10, left: 45, right: 45 }, verticalAlign: VerticalAlign.TOP,
    children: Array.isArray(children) ? children : [children] });
}
const CH = [1250, 1050, 1250, 1350, 1750, 1500, 1350, 1206];
const MW = [1413, 1037, 2250, 6006];
const W = CH.reduce((a, x) => a + x, 0);

function chain(rows) {
  const tp = (t, o = {}) => new Paragraph({ alignment: o.center ? AlignmentType.CENTER : undefined, spacing: { after: 0, line: 200 }, children: runs(t, { size: SZ.t, bold: o.bold, color: o.color }) });
  const out = [
    new TableRow({ children: [cell(tp(''), CH[0], { fill: C.h1 }), cell(tp('상품', { center: true, bold: true }), CH[1], { fill: C.h1 }),
      cell(tp('1차 거래: 발행사와 직접', { center: true, bold: true }), CH[2] + CH[3], { fill: C.h1, span: 2 }),
      cell(tp('2차 거래: 투자자끼리', { center: true, bold: true }), CH[4] + CH[5] + CH[6] + CH[7], { fill: C.h1, span: 4 })] }),
    new TableRow({ children: ['사업 영역', '상품 만들기', '발행', '1차 판매', '주문 접수', '체결', '청산, 결제', '보관'].map((n, i) => cell(tp(n, { center: i > 0, bold: true }), CH[i], { fill: C.h2 })) }),
  ];
  for (const r of rows) {
    const [a, sub] = String(r.area).split('||');
    const first = [tp(a, { bold: true })]; if (sub) first.push(...sub.split('\n').map(x => tp(x, { color: C.gray })));
    const cs = [cell(first, CH[0])]; let ci = 1;
    for (const c of r.cells) {
      const span = c.span || 1; const w = CH.slice(ci, ci + span).reduce((x, y) => x + y, 0); ci += span;
      const kids = String(c.t || '').split('\n').map(x => tp(x));
      if (c.money) kids.push(...String(c.money).split('\n').map(x => tp('● ' + x.replace(/^●\s*/, ''))));
      cs.push(cell(kids, w, { fill: c.own ? C.own : undefined, span }));
    }
    out.push(new TableRow({ cantSplit: true, children: cs }));
  }
  return new Table({ width: { size: W, type: WidthType.DXA }, columnWidths: CH, layout: TableLayoutType.FIXED, rows: out });
}

function money(rows) {
  const tp = (t, o = {}) => new Paragraph({ spacing: { after: 0, line: 200 }, children: runs(t, { size: SZ.t, bold: o.bold, color: o.color }) });
  const out = [new TableRow({ children: ['사업 영역', '비중', '내는 사람', '무엇의 대가로, 언제 → 왜 내나 → 왜 오르내렸나'].map((h, i) => cell(tp(h, { bold: true }), MW[i], { fill: C.h2 })) })];
  for (const r of rows) {
    const [a, sub] = String(r[0]).split('||');
    const first = [...a.split('\n').map((x, i) => tp(x, { bold: i === 0 }))]; if (sub) first.push(...sub.split('\n').map(x => tp(x, { color: C.gray })));
    out.push(new TableRow({ cantSplit: true, children: [cell(first, MW[0]), ...r.slice(1).map((x, i) => cell(String(x).split('\n').map(y => tp(y)), MW[i + 1]))] }));
  }
  return new Table({ width: { size: W, type: WidthType.DXA }, columnWidths: MW, layout: TableLayoutType.FIXED, rows: out });
}

function build(d) {
  const ch = [];
  ch.push(new Paragraph({ spacing: { after: 20 }, children: [new TextRun({ font: FONT, size: SZ.title, bold: true, text: d.title })] }));
  ch.push(para(d.intro, { after: 60 }));
  ch.push(new Paragraph({ indent: { left: 200 }, spacing: { after: 10 }, children: [new TextRun({ font: FONT, size: SZ.p, bold: true, text: '어떻게 컸나' })] }));
  for (const g of d.grow) {
    ch.push(new Paragraph({ numbering: g.num ? { reference: 'n', level: 0 } : { reference: 'b', level: 0 }, spacing: SP,
      children: [new TextRun({ font: FONT, size: SZ.p, bold: true, text: g.label + ': ' }), ...runs(g.text)] }));
    for (const k of g.kids || []) ch.push(para(k, { num: { reference: 'b', level: 1 } }));
  }
  ch.push(new Paragraph({ spacing: { before: 80, after: 30 }, children: [new TextRun({ font: FONT, size: SZ.p, bold: true, text: '밸류체인 지도 ' }), ...runs(d.chain_note, { color: C.gray })] }));
  ch.push(chain(d.chain));
  ch.push(new Paragraph({ spacing: { before: 100, after: 30 }, children: [new TextRun({ font: FONT, size: SZ.p, bold: true, text: '우리가 봐야 할 사업 영역별 돈 버는 법 ' }), ...runs(d.money_basis, { color: C.gray })] }));
  ch.push(money(d.money));
  ch.push(new Paragraph({ spacing: { before: 100, after: 20 }, children: [new TextRun({ font: FONT, size: SZ.p, bold: true, text: d.points_head })] }));
  for (const p of d.points) {
    ch.push(new Paragraph({ spacing: SP, children: [new TextRun({ font: FONT, size: SZ.p, bold: true, text: p.title + ' ' }), ...runs(p.text)] }));
    for (const k of p.kids || []) ch.push(para('- ' + k));
  }
  if (d.drop) ch.push(new Paragraph({ spacing: SP, children: [new TextRun({ font: FONT, size: SZ.p, bold: true, text: d.drop })] }));
  return new Document({
    styles: { default: { document: { run: { font: FONT, size: 16 } } } },
    numbering: { config: [
      { reference: 'b', levels: [{ level: 0, format: LevelFormat.BULLET, text: '-', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 560, hanging: 200 } } } },
                                 { level: 1, format: LevelFormat.BULLET, text: '◦', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 860, hanging: 200 } } } }] },
      { reference: 'n', levels: [{ level: 0, format: LevelFormat.DECIMAL, text: '%1.', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 860, hanging: 260 } } } }] },
    ] },
    sections: [{ properties: { page: { size: { width: 11906, height: 16838 }, margin: { top: 480, right: 600, bottom: 440, left: 600 } } }, children: ch }],
  });
}

(async () => {
  for (const s of process.argv.slice(2)) {
    const d = JSON.parse(fs.readFileSync(path.join(ROOT, `kb/a4/compact/${s}.json`), 'utf8'));
    const f = path.join(ROOT, `deliverables/KDX_A4_간결_${s}_261118.docx`);
    fs.writeFileSync(f, await Packer.toBuffer(build(d)));
    console.log('ok', f);
  }
})();
