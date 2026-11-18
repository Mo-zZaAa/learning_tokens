// 한눈에 보기(비전) 점검: node scratchpad/v5web/check_vision.js
const { chromium } = require('playwright'); const path = require('path');
const U = 'file://' + path.resolve(__dirname, '../../web/v5/index.html');
(async () => {
  const b = await chromium.launch(); const errs = [];
  const c = await b.newContext({ viewport: { width: 1280, height: 900 } }); const p = await c.newPage();
  p.on('pageerror', e => errs.push(e.message)); p.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
  for (const s of ['kraken', 'binance', 'coinbase', 'robinhood', 'dinari', 'ondo', 'common']){
    await p.goto(U + '#' + s); await p.waitForTimeout(300);
    const r = await p.evaluate(() => {
      const first = document.querySelector('.odx .orow .olab') || document.querySelector('.cbox h3') || document.querySelector('.sec h2');
      const hl = document.querySelector('.odx .orow') ? document.querySelectorAll('.odx .orow:first-of-type mark.em, .odx .orow mark.em').length : document.querySelectorAll('.cbox mark.em').length;
      return [first ? first.textContent : null, hl];
    });
    console.log(s, '맨 앞:', r[0], '형광펜 수:', r[1]);
  }
  await p.goto(U + '#kraken'); await p.waitForSelector('.odx');
  await p.screenshot({ path: path.join(__dirname, 'vision_kraken.png') });
  const nas = await p.evaluate(() => { const x = [...document.querySelectorAll('.odx .tx')].find(e => e.textContent.startsWith('실제로 한 일')); if (!x) return null; let d = x.closest('details'); while (d){ d.open = true; d = d.parentElement.closest('details'); } x.scrollIntoView({block: 'start'}); return true; });
  await p.waitForTimeout(150);
  console.log('Nasdaq 역할 표 찾음:', nas);
  await p.screenshot({ path: path.join(__dirname, 'kraken_nasdaq.png') });
  await c.close();
  const m = await b.newContext({ viewport: { width: 390, height: 844 }, isMobile: true }); const mp = await m.newPage();
  await mp.goto(U + '#coinbase'); await mp.waitForSelector('.odx');
  console.log('휴대폰 가로 폭', await mp.evaluate(() => [document.documentElement.scrollWidth, document.documentElement.clientWidth]));
  await b.close(); console.log('오류', errs.length ? errs.slice(0, 3) : '없음');
})();
