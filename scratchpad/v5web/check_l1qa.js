// 1층 질문 접기 점검: node scratchpad/v5web/check_l1qa.js
const { chromium } = require('playwright'); const path = require('path');
const U = 'file://' + path.resolve(__dirname, '../../web/v5/index.html'); const OUT = __dirname;
(async () => {
  const b = await chromium.launch(); const errs = []; const log = (...a) => console.log(...a);
  const watch = (p, t) => { p.on('console', m => { if (m.type() === 'error') errs.push(t + ' ' + m.text()); }); p.on('pageerror', e => errs.push(t + ' ' + e.message)); };
  const c = await b.newContext({ viewport: { width: 1280, height: 900 }, deviceScaleFactor: 1 }); const p = await c.newPage(); watch(p, 'desktop');
  await p.goto(U + '#ondo'); await p.waitForSelector('.cgrid');
  log('칸:', await p.$$eval('.cgrid .cbox h3', a => a.map(x => x.textContent)), '열:', await p.$eval('.cgrid', g => getComputedStyle(g).gridTemplateColumns.split(' ').length));
  log('큰 불릿:', await p.$$eval('.cgrid .qg', a => a.length), '질문 단추:', await p.$$eval('.cgrid .qtog', a => a.length), '보이는 세부 줄:', await p.$$eval('.cgrid .qas .ln', a => a.filter(x => x.offsetParent).length), '/ 전체', await p.$$eval('.cgrid .qas .ln', a => a.length));
  log('1층 바닥 y(접힘):', await p.$eval('.cgrid', e => Math.round(e.getBoundingClientRect().bottom)), '/ 900');
  log('점선 상자:', await p.$$eval('.cgrid .todo', a => a.map(x => x.textContent)));
  await p.screenshot({ path: path.join(OUT, 'l1_qa_folded.png') });
  await p.click('.cgrid .qtog'); await p.waitForTimeout(150);
  log('하나 펼침 뒤 보이는 세부 줄:', await p.$$eval('.cgrid .qas .ln', a => a.filter(x => x.offsetParent).length), '| 첫 질문:', await p.$eval('.cgrid .qg.open .qq2', e => e.textContent));
  await p.screenshot({ path: path.join(OUT, 'l1_qa_open.png') });
  await p.click('[data-act=qaall]'); await p.waitForTimeout(100);
  log('모두 펼치기 뒤 보이는 세부 줄:', await p.$$eval('.cgrid .qas .ln', a => a.filter(x => x.offsetParent).length), '단추 글:', await p.textContent('[data-act=qaall]'));
  await p.click('[data-act=qaall]'); await p.waitForTimeout(100);
  log('모두 접기 뒤:', await p.$$eval('.cgrid .qas .ln', a => a.filter(x => x.offsetParent).length));
  // 접힌 세부 줄 찾기
  await p.fill('#q', 'MetaMask'); await p.waitForTimeout(400);
  log('찾기 MetaMask:', await p.textContent('#sres .sh'), '|', await p.textContent('#sres .it .loc'));
  await p.click('#sres .it'); await p.waitForTimeout(500);
  log('이동 뒤 펼침과 칠함:', await p.evaluate(() => { const el = document.getElementById(location.hash.slice(1)); return [!!el && !!el.offsetParent, document.querySelectorAll('mark.hit').length]; }));
  // 세부 줄 메모와 용어
  const sub = await p.$('.cgrid .qg.open .qas .ln'); await sub.hover(); await (await sub.$('.mb')).click();
  log('세부 줄 메모 위치:', await p.textContent('#mloc')); await p.click('[data-act=cancel]');
  log('세부 줄 용어 감싼 수:', await p.$$eval('.cgrid .qas .term', a => a.length), '칸 머리 답 꼬리표:', await p.$$eval('.cgrid .abadge', a => a.length));
  await c.close();
  const m = await b.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 1, isMobile: true, hasTouch: true }); const mp = await m.newPage(); watch(mp, 'mobile');
  await mp.goto(U + '#ondo'); await mp.waitForSelector('.cgrid');
  await mp.screenshot({ path: path.join(OUT, 'l1_qa_mobile.png') });
  await mp.tap('[data-act=qaall]'); await mp.waitForTimeout(150);
  log('휴대폰 질문 모두 펼침 가로 폭:', await mp.evaluate(() => [document.documentElement.scrollWidth, document.documentElement.clientWidth]));
  await m.close(); await b.close(); log('콘솔 오류:', errs.length ? errs : '없음');
})().catch(e => { console.error('점검 실패', e); process.exit(1); });
