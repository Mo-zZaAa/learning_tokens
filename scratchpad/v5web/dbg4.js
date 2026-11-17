const { chromium } = require('playwright'); const path=require('path');
(async()=>{ const b=await chromium.launch(); const m=await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:1,isMobile:true,hasTouch:true}); const p=await m.newPage();
for (const H of ['#kraken','#common']){ await p.goto('file://'+path.resolve(__dirname,'../../web/v5/index.html')+H); await p.waitForSelector('.layer'); await p.evaluate(()=>document.querySelectorAll('details').forEach(d=>d.open=true)); await p.waitForTimeout(200);
console.log(await p.evaluate(()=>{ const e=document.getElementById('kraken-o-sce0c4'); const out=[]; let x=e.querySelector('.term'); while(x && x!==document.body){ const r=x.getBoundingClientRect(); const cs=getComputedStyle(x); out.push(x.tagName+'.'+x.className+' w='+Math.round(r.width)+' disp='+cs.display+' ws='+cs.whiteSpace+' maxw='+cs.maxWidth); x=x.parentElement;} return out; }));
} await b.close();})();
