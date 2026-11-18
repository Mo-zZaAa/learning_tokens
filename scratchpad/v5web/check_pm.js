// Robinhood 1층, 2층 강조 점검: node scratchpad/v5web/check_pm.js
const { chromium } = require('playwright'); const path = require('path');
const U = 'file://' + path.resolve(__dirname, '../../web/v5/index.html');
(async () => {
  const b = await chromium.launch(); const errs = [];
  const c = await b.newContext({ viewport: { width: 1280, height: 900 } }); const p = await c.newPage();
  p.on('pageerror', e => errs.push(e.message)); p.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
  await p.goto(U + '#robinhood'); await p.waitForSelector('.odx');
  await p.evaluate(() => document.querySelectorAll('.odx details.omore').forEach(d => d.open = true));
  const cnt = (sel) => p.evaluate((s) => document.querySelectorAll(s).length, sel);
  console.log('1층 질문 표시', await cnt('.odx .pmq'), '형광펜', await cnt('.odx mark.em'), '빨간', await cnt('.odx strong.warn'));
  const rows = await p.$$('.odx .orow');
  await rows[1].screenshot({ path: path.join(__dirname, 'rh_pm_l1.png') });
  const l2 = await p.evaluate(() => {
    const root = document.querySelector('[id$="robinhood-o-L2"]');
    if (!root) return 'L2 없음';
    root.querySelectorAll('details').forEach(d => d.open = true);
    return [root.querySelectorAll('.pmq').length, root.querySelectorAll('mark.em').length, root.querySelectorAll('pre').length, root.querySelectorAll('table').length, root.querySelectorAll('strong.warn').length];
  });
  console.log('2층 질문 표시, 형광펜, 코드, 표, 빨간', l2);
  const sec = await p.$('[id$="robinhood-o-L2"] .sec:nth-of-type(6)');
  if (sec) { await sec.scrollIntoViewIfNeeded(); await sec.screenshot({ path: path.join(__dirname, 'rh_pm_l2.png') }); }
  await c.close();
  const m = await b.newContext({ viewport: { width: 390, height: 844 }, isMobile: true }); const mp = await m.newPage();
  await mp.goto(U + '#robinhood'); await mp.waitForSelector('.odx');
  await mp.evaluate(() => document.querySelectorAll('details').forEach(d => { d.open = true; }));
  await mp.waitForTimeout(200);
  console.log('휴대폰 가로 폭', await mp.evaluate(() => [document.documentElement.scrollWidth, document.documentElement.clientWidth]));
  await b.close(); console.log('오류', errs.length ? errs.slice(0, 3) : '없음');
})();
