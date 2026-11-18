// 회사별 A4 양식 JSON(kb/a4/<slug>.json) → Word. 양식(inputs/a4_261118/A4양식_1.docx)의 글꼴, 색, 표 모양을 따름
// 사용법: node kb/a4/render.js kraken robinhood binance coinbase  → deliverables/KDX_회사별A4_4개사_261118.docx 와 회사별 파일
const fs = require('fs'); const path = require('path');
const D = require('docx');
const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType, ShadingType, AlignmentType,
  LevelFormat, BorderStyle, VerticalAlign, PageBreak, TableLayoutType } = D;
const ROOT = path.resolve(__dirname, '../..');
const FONT = 'Pretendard Medium';
const C = { own: 'FBE5D6', h1: 'F2F2F2', h2: 'D9D9D9', accent: 'D04A02', gray: '808080', line: 'BFBFBF' };
const W = 11906 - 850 - 850;   // 본문 폭(DXA)
const SZ = { body: 18, small: 16, sec: 22, title: 28 };   // 반 포인트

function runs(text, o = {}) {
  // **굵게**, ==강조==(굵게+주황), (판단) 회색
  const out = []; const re = /(\*\*[^*]+\*\*|==[^=]+==|\(판단\)|\(계산\)|\(매체 추정\)|\(회사 주장\))/g;
  let last = 0, m; const s = String(text || '');
  const base = { font: FONT, size: o.size || SZ.body, color: o.color, bold: o.bold };
  while ((m = re.exec(s))) {
    if (m.index > last) out.push(new TextRun({ ...base, text: s.slice(last, m.index) }));
    const t = m[0];
    if (t.startsWith('**')) out.push(new TextRun({ ...base, text: t.slice(2, -2), bold: true }));
    else if (t.startsWith('==')) out.push(new TextRun({ ...base, text: t.slice(2, -2), bold: true, color: C.accent }));
    else out.push(new TextRun({ ...base, text: t, color: C.gray }));
    last = re.lastIndex;
  }
  if (last < s.length) out.push(new TextRun({ ...base, text: s.slice(last) }));
  return out;
}

let inst = 0;
function bulletBlock(b) {
  const ps = [];
  const head = [];
  if (b.label) head.push(new TextRun({ font: FONT, size: SZ.body, bold: true, text: b.label + (b.text ? ': ' : '') }));
  ps.push(new Paragraph({ numbering: { reference: 'bul', level: 0 }, spacing: { before: 60, after: 20 }, children: [...head, ...runs(b.text)] }));
  const walk = (kids, lv) => {
    if (!kids || !kids.length) return;
    const numInst = ++inst;
    for (const k of kids) {
      const num = k.num ? { reference: 'num', level: Math.min(lv, 3), instance: numInst } : { reference: 'bul', level: Math.min(lv, 3) };
      ps.push(new Paragraph({ numbering: num, spacing: { before: 0, after: 10 }, children: runs(k.text) }));
      walk(k.kids, lv + 1);
    }
  };
  walk(b.kids, 1);
  return ps;
}

const border = { style: BorderStyle.SINGLE, size: 4, color: C.line };
const borders = { top: border, bottom: border, left: border, right: border };
function cell(children, width, o = {}) {
  return new TableCell({
    width: { size: width, type: WidthType.DXA }, columnSpan: o.span || 1, borders,
    shading: o.fill ? { type: ShadingType.CLEAR, color: 'auto', fill: o.fill } : undefined,
    margins: { top: 40, bottom: 40, left: 70, right: 70 }, verticalAlign: o.v || VerticalAlign.TOP,
    children: Array.isArray(children) ? children : [children],
  });
}
const P = (t, o = {}) => new Paragraph({ alignment: o.center ? AlignmentType.CENTER : undefined, spacing: { before: 0, after: 0 }, children: runs(t, { size: o.size || SZ.small, bold: o.bold, color: o.color }) });

function chainTable(b) {
  const area = 1300, col = Math.floor((W - area) / 7); const cols = [area, col, col, col, col, col, col, W - area - col * 6];
  const hdr1 = new TableRow({ tableHeader: true, children: [
    cell(P(''), cols[0], { fill: C.h1 }), cell(P('상품', { center: true, bold: true }), cols[1], { fill: C.h1 }),
    cell(P('1차 거래: 발행사와 직접', { center: true, bold: true }), cols[2] + cols[3], { fill: C.h1, span: 2 }),
    cell(P('2차 거래: 투자자끼리', { center: true, bold: true }), cols[4] + cols[5] + cols[6] + cols[7], { fill: C.h1, span: 4 })] });
  const names = ['사업 영역', '상품 만들기', '발행', '1차 판매', '주문 접수', '체결', '청산, 결제', '보관'];
  const hdr2 = new TableRow({ tableHeader: true, children: names.map((n, i) => cell(P(n, { center: true, bold: true }), cols[i], { fill: C.h2 })) });
  const rows = [hdr1, hdr2];
  for (const r of b.rows || []) {
    const cs = [cell(P(r.area, { bold: true }), cols[0])]; let ci = 1;
    for (const c of r.cells || []) {
      const span = c.span || 1; const w = cols.slice(ci, ci + span).reduce((a, x) => a + x, 0); ci += span;
      const kids = [P(c.t || '')];
      if (c.money) kids.push(new Paragraph({ spacing: { before: 20, after: 0 }, children: runs(c.money.replace(/^●\s*/, ''), { size: SZ.small }).length ? [new TextRun({ font: FONT, size: SZ.small, color: C.accent, text: '● ' }), ...runs(c.money.replace(/^●\s*/, ''), { size: SZ.small, color: C.accent })] : [] }));
      cs.push(cell(kids, w, { fill: c.own ? C.own : undefined, span }));
    }
    rows.push(new TableRow({ cantSplit: true, children: cs }));
  }
  return new Table({ width: { size: W, type: WidthType.DXA }, columnWidths: cols, layout: TableLayoutType.FIXED, rows });
}

function gridTable(head, widths, rows) {
  const t = [new TableRow({ tableHeader: true, children: head.map((h, i) => cell(P(h, { bold: true }), widths[i], { fill: C.h2 })) })];
  for (const r of rows || []) t.push(new TableRow({ cantSplit: true, children: r.map((x, i) => cell(P(x), widths[i], { fill: i === 0 ? C.h1 : undefined })) }));
  return new Table({ width: { size: W, type: WidthType.DXA }, columnWidths: widths, layout: TableLayoutType.FIXED, rows: t });
}
const MONEY_W = [1500, 1000, 1700, 2500]; MONEY_W.push(W - MONEY_W.reduce((a, x) => a + x, 0));
const WHY_W = [2400, 2000, 3200]; WHY_W.push(W - WHY_W.reduce((a, x) => a + x, 0));

function labelPara(label, note) {
  return new Paragraph({ numbering: { reference: 'bul', level: 0 }, spacing: { before: 100, after: 40 }, keepNext: true,
    children: [new TextRun({ font: FONT, size: SZ.body, bold: true, text: label }), ...(note ? [new TextRun({ font: FONT, size: SZ.small, color: C.gray, text: '  ' + note })] : [])] });
}

function companyChildren(d, first) {
  const out = [];
  if (!first) out.push(new Paragraph({ children: [new PageBreak()] }));
  out.push(new Paragraph({ spacing: { before: 0, after: 40 }, children: [new TextRun({ font: FONT, size: SZ.title, bold: true, text: d.name })] }));
  if (d.view) out.push(new Paragraph({ spacing: { before: 0, after: 120 }, border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: C.accent, space: 4 } }, children: runs(d.view, { size: SZ.body, color: C.gray }) }));
  for (const s of d.sections || []) {
    out.push(new Paragraph({ spacing: { before: 200, after: 80 }, keepNext: true, border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: C.line, space: 2 } },
      children: [new TextRun({ font: FONT, size: SZ.sec, bold: true, text: s.title })] }));
    for (const b of s.blocks || []) {
      if (b.type === 'bullet') out.push(...bulletBlock(b));
      else if (b.type === 'para') out.push(new Paragraph({ spacing: { before: 40, after: 40 }, children: runs(b.text) }));
      else if (b.type === 'chain') { out.push(labelPara(b.label || '밸류체인 지도', b.note || '주황 칸 = 이 회사 그룹(법인, 직접 또는 인수), 흰 칸 = 다른 회사, ● = 이 회사가 돈을 받는 칸')); out.push(chainTable(b)); }
      else if (b.type === 'money') { out.push(labelPara(b.label || '우리가 봐야 할 사업 영역별 어떻게 돈 버는지', b.note)); out.push(gridTable(['사업 영역', '비중', '내는 사람', '무엇의 대가로, 언제', '왜 내나(원래 목적 → 돈 내고 얻는 것)'], MONEY_W, b.rows)); }
      else if (b.type === 'why') { out.push(labelPara(b.label || '잘 된 이유와 방식', b.note)); out.push(gridTable(['잘 된 이유', '방식(Build, Buy, Partner)', '왜 그 방식', '그 뒤 숫자'], WHY_W, b.rows)); }
    }
  }
  return out;
}

function numbering() {
  const bulletChars = ['•', '-', '◦', '▪'];
  const ind = lv => ({ left: 300 + lv * 300, hanging: 220 });
  return { config: [
    { reference: 'bul', levels: bulletChars.map((ch, lv) => ({ level: lv, format: LevelFormat.BULLET, text: ch, alignment: AlignmentType.LEFT, style: { paragraph: { indent: ind(lv) }, run: { font: FONT } } })) },
    { reference: 'num', levels: [0, 1, 2, 3].map(lv => ({ level: lv, format: LevelFormat.DECIMAL, text: `%${lv + 1})`, alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 300 + lv * 300 + 60, hanging: 280 } }, run: { font: FONT } } })) },
  ] };
}

function doc(children) {
  return new Document({
    styles: { default: { document: { run: { font: FONT, size: SZ.body } } } },
    numbering: numbering(),
    sections: [{ properties: { page: { size: { width: 11906, height: 16838 }, margin: { top: 760, right: 850, bottom: 700, left: 850 } } }, children }],
  });
}

(async () => {
  const slugs = process.argv.slice(2);
  const outDir = path.join(ROOT, 'deliverables'); fs.mkdirSync(outDir, { recursive: true });
  const all = [];
  for (const [i, s] of slugs.entries()) {
    const d = JSON.parse(fs.readFileSync(path.join(ROOT, `kb/a4/${s}.json`), 'utf8'));
    all.push(...companyChildren(d, i === 0));

    const one = await Packer.toBuffer(doc(companyChildren(d, true)));
    fs.writeFileSync(path.join(outDir, `KDX_A4_${s}_261118.docx`), one);
  }

  const buf = await Packer.toBuffer(doc(all));
  const f = path.join(outDir, 'KDX_회사별A4_4개사_261118.docx'); fs.writeFileSync(f, buf);
  console.log('ok', f);
})();
