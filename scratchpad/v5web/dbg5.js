const { chromium } = require('playwright'); const path=require('path');
(async()=>{ const b=await chromium.launch(); const p=await (await b.newContext({viewport:{width:1280,height:900},deviceScaleFactor:1})).newPage(); const errs=[]; p.on('pageerror',e=>errs.push(e.message));
await p.goto('file://'+path.resolve(__dirname,'../../web/v5/index.html')+'#kraken'); await p.waitForSelector('.layer');
console.log('1층 바닥 y:', await p.$eval('.cgrid', e=>Math.round(e.getBoundingClientRect().bottom)), '/ 화면 900');
console.log('kraken 2층 글 그림:', await p.$$eval('#kraken-o-L2 pre.art', a=>a.length), '답 접힘:', await p.$$eval('#kraken-o-L2 details.ans', a=>a.length+'개, 열림 '+a.filter(x=>x.open).length), 'pm_q2 칸:', await p.$$eval('#kraken-o-L3 .lpart', a=>a.map(x=>(x.querySelector('.ptitle h3')||{}).textContent)));
await p.click('.lnav a:nth-child(2)'); await p.waitForTimeout(400); await p.screenshot({path:path.join(__dirname,'layers_desktop_easy.png')}); console.log('오류', errs); await b.close();})();
