// 핵심 포인트와 이동 버튼 점검: node scratchpad/v5web/check_points.js dinari robinhood ...
const { chromium } = require('playwright'); const path = require('path');
const U = 'file://' + path.resolve(__dirname, '../../web/v5/index.html');
(async () => {
  const b = await chromium.launch(); const errs = [];
  const c = await b.newContext({ viewport: { width: 1280, height: 900 } }); const p = await c.newPage();
  p.on('pageerror', e => errs.push(e.message)); p.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
  for (const s of process.argv.slice(2)){
    await p.goto(U + '#' + s); await p.waitForTimeout(400);
    const info = await p.evaluate(() => {
      const first = document.querySelector('.odx .orow .olab, .cbox h3');
      const btns = [...document.querySelectorAll('#main .gobtn')];
      return [first ? first.textContent : null, btns.length];
    });
    let ok = 0, miss = 0;
    const n = info[1];
    for (let i = 0; i < n; i++){
      await p.goto(U + '#' + s); await p.waitForTimeout(250);
      const btn = (await p.$$('#main .gobtn'))[i];
      await btn.evaluate(e => { let d = e.closest('details'); while (d){ d.open = true; d = d.parentElement.closest('details'); } });
      await btn.click(); await p.waitForTimeout(250);
      const moved = await p.evaluate(() => { const f = document.querySelector('.flash'); return !!f; });
      moved ? ok++ : miss++;
    }
    console.log(s, '맨 앞:', info[0], '| 이동 버튼', n, '| 이동됨', ok, '| 못 감', miss);
  }
  await p.goto(U + '#' + process.argv[2]); await p.waitForTimeout(300);
  const first = await p.$('.odx .orow, .cbox'); if (first) await first.screenshot({ path: path.join(__dirname, 'points_' + process.argv[2] + '.png') });
  await b.close(); console.log('오류', errs.length ? errs.slice(0, 3) : '없음');
})();
