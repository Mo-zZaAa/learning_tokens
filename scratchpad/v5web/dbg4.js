const { chromium } = require('playwright'); const path = require('path');
(async () => {
  const b = await chromium.launch();
  const m = await b.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 1, isMobile: true, hasTouch: true });
  const p = await m.newPage();
  for (const H of ['#kraken', '#common']) {
    await p.goto('file://' + path.resolve(__dirname, '../../web/v5/index.html') + H); await p.waitForSelector('.layer');
    await p.evaluate(() => document.querySelectorAll('details').forEach(d => d.open = true)); await p.waitForTimeout(200);
    console.log(H, await p.evaluate(() => { const out=[document.documentElement.scrollWidth]; const tw=document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT); const r=document.createRange(); while(tw.nextNode()){ const n=tw.currentNode; if (n.parentElement.closest('.cos,script')) continue; r.selectNodeContents(n); const b=r.getBoundingClientRect(); if (b.right>392) out.push(Math.round(b.right)+' '+n.parentElement.tagName+'.'+n.parentElement.className+' | '+n.nodeValue.slice(0,80)); if(out.length>6) break; } return out; }));
  }
  await b.close();
})();
