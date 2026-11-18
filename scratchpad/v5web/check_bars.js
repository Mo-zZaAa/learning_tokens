// 매출 층 막대 점검: node scratchpad/v5web/check_bars.js common
const { chromium } = require('playwright'); const path = require('path');
const S = process.argv[2] || 'common';
const U = 'file://' + path.resolve(__dirname, '../../web/v5/index.html');
(async () => {
  const b = await chromium.launch(); const errs = [];
  for (const [w, h, tag, dark] of [[1280, 900, 'pc', false], [390, 844, 'm', false], [1280, 900, 'dark', true]]){
    const c = await b.newContext({ viewport: { width: w, height: h }, colorScheme: dark ? 'dark' : 'light' }); const p = await c.newPage();
    p.on('pageerror', e => errs.push(e.message));
    await p.goto(U + '#' + S); await p.waitForTimeout(400);
    const n = await p.evaluate(() => document.querySelectorAll('.bars').length);
    const first = await p.$('.bars');
    if (first){ await first.scrollIntoViewIfNeeded(); await first.screenshot({ path: path.join(__dirname, `bars_${S}_${tag}.png`) }); }
    console.log(tag, '막대 그림', n, '가로 폭', await p.evaluate(() => [document.documentElement.scrollWidth, document.documentElement.clientWidth]),
      '층', await p.evaluate(() => [...document.querySelectorAll('.lnav a')].map(a => a.textContent).join(' / ')));
    await c.close();
  }
  await b.close(); console.log('오류', errs.length ? errs : '없음');
})();
