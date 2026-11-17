const { chromium } = require('playwright'); const path=require('path');
(async()=>{ const b=await chromium.launch(); const m=await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:1,isMobile:true,hasTouch:true}); const p=await m.newPage();
await p.goto('file://'+path.resolve(__dirname,'../../web/v5/index.html')+'#common'); await p.waitForSelector('.layer');
console.log(await p.evaluate(()=>{ const W=document.documentElement.clientWidth; const out=[]; for (const e of document.querySelectorAll('body *')){ const r=e.getBoundingClientRect(); if (r.right>W+1 && !e.closest('.tblw,.art,.cos') && e.tagName!=='SPAN' && e.tagName!=='STRONG') { let a=[],x=e; for(let i=0;i<4&&x;i++){a.push(x.tagName+'.'+x.className);x=x.parentElement;} out.push(a.join(' < ')+' w='+Math.round(r.width)+' left='+Math.round(r.left)); } } return out.slice(0,12); }));
await b.close();})();
