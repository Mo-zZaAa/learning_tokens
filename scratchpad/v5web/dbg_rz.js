const { chromium } = require('playwright'); const path = require('path');
const U = 'file://' + path.resolve(__dirname, '../../web/v5/index.html');
(async () => {
  const b = await chromium.launch(); const p = await (await b.newContext({ viewport: { width: 1280, height: 900 } })).newPage();
  await p.goto(U + '#kraken'); await p.waitForSelector('.odx');
  const tb = await p.$('.odx details.omore[open] table.tbl'); await tb.scrollIntoViewIfNeeded();
  const th = (await tb.$$('thead th'))[1]; const h = await th.$('.rzh'); const hb = await h.boundingBox();
  console.log('handle box', hb);
  console.log('at point', await p.evaluate(([x, y]) => { const e = document.elementFromPoint(x, y); return e ? e.className + ' ' + e.tagName : null; }, [hb.x + hb.width / 2, hb.y + hb.height / 2]));
  await p.evaluate(() => { window.__ev = []; ['pointerdown', 'pointermove', 'pointerup'].forEach(t => document.addEventListener(t, e => window.__ev.push(t + ':' + (e.target.className || e.target.tagName)), true)); });
  await p.mouse.move(hb.x + 4, hb.y + hb.height / 2); await p.mouse.down(); await p.mouse.move(hb.x + 100, hb.y + hb.height / 2, { steps: 4 }); await p.mouse.up();
  console.log((await p.evaluate(() => window.__ev)).slice(0, 8), 'width', (await th.boundingBox()).width, await tb.evaluate(t => t.className + ' ' + t.style.width));
  await b.close();
})();
