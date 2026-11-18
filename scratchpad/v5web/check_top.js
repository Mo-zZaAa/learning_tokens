// 카드 맨 위 "먼저 볼 질문" 점검: node scratchpad/v5web/check_top.js kraken
const { chromium } = require('playwright'); const path = require('path');
const S = process.argv[2] || 'kraken';
const U = 'file://' + path.resolve(__dirname, '../../web/v5/index.html');
(async () => {
  const b = await chromium.launch(); const errs = [];
  for (const [w, h, tag] of [[1280, 900, 'pc'], [390, 844, 'm']]){
    const c = await b.newContext({ viewport: { width: w, height: h } }); const p = await c.newPage();
    p.on('pageerror', e => errs.push(e.message));
    await p.goto(U + '#' + S); await p.waitForSelector('.odx');
    const r = await p.evaluate(() => { const row = document.querySelector('.odx .orow'); return [row.querySelector('.olab').textContent, row.classList.contains('hot'), row.querySelectorAll('mark.em').length, document.documentElement.scrollWidth]; });
    console.log(tag, r);
    const row = await p.$('.odx .orow'); await row.screenshot({ path: path.join(__dirname, `top_${S}_${tag}.png`) });
    await c.close();
  }
  await b.close(); console.log('오류', errs.length ? errs : '없음');
})();
