// 세 층 개요 점검: node scratchpad/v5web/check_layers.js
const { chromium } = require('playwright'); const path = require('path');
const U = 'file://' + path.resolve(__dirname, '../../web/v5/index.html'); const OUT = __dirname;
(async () => {
  const b = await chromium.launch(); const errs = []; const log = (...a) => console.log(...a);
  const watch = (p, t) => { p.on('console', m => { if (m.type() === 'error') errs.push(t + ' ' + m.text()); }); p.on('pageerror', e => errs.push(t + ' ' + e.message)); };
  const c = await b.newContext({ viewport: { width: 1280, height: 900 }, deviceScaleFactor: 1 }); const p = await c.newPage(); watch(p, 'desktop');
  await p.goto(U + '#kraken'); await p.waitForSelector('.layer');
  log('층:', await p.$$eval('.layer .lhead', a => a.map(x => x.textContent.replace(/\s+/g, ' ').trim())));
  log('층 단추:', await p.$$eval('.lnav a', a => a.map(x => x.textContent + (x.classList.contains('off') ? '(없음)' : ''))));
  log('1층 상자:', await p.$$eval('.cgrid .cbox h3', a => a.map(x => x.textContent)), '열 수:', await p.$eval('.cgrid', g => getComputedStyle(g).gridTemplateColumns.split(' ').length));
  log('준비 중 상자:', await p.$$eval('.ov .ready', a => a.map(x => x.textContent.replace(/\s+/g, ' ').slice(0, 60))));
  log('1층 용어 감싼 수:', await p.$$eval('.cgrid .term', a => a.length));
  await p.screenshot({ path: path.join(OUT, 'layers_desktop.png') });
  await p.click('.lnav a:nth-child(3)'); await p.waitForTimeout(500);
  log('3층 바로 가기 뒤 해시:', await p.evaluate(() => location.hash), '3층 머리 위치:', await p.$eval('#kraken-o-L3', e => Math.round(e.getBoundingClientRect().top)));
  // 찾기: 1층 글
  const w = await p.$eval('.cgrid .cbox .ln .tx', e => e.textContent.trim().split(/\s+/).slice(0, 2).join(' '));
  await p.fill('#q', w); await p.waitForTimeout(400);
  log('찾기', JSON.stringify(w), ':', await p.textContent('#sres .sh'), '| 첫 결과 위치:', await p.textContent('#sres .it .loc'));
  await p.click('#sres .it'); await p.waitForTimeout(500); log('칠함:', await p.$$eval('mark.hit', a => a.length));
  // 메모: 1층 줄
  await p.evaluate(() => window.scrollTo(0, 0));
  const ln = await p.$('.cgrid .ln'); await ln.hover(); await (await ln.$('.mb')).click();
  log('메모 위치:', await p.textContent('#mloc')); await p.fill('#mtext', '층 점검 메모'); await p.click('#mform button[type=submit]');
  log('저장된 메모 anchor:', await p.evaluate(() => JSON.parse(localStorage.getItem('kdx-v5-memos')).memos.slice(-1)[0].anchor));
  // 공통
  await p.click('#cos [data-co=common]'); await p.waitForTimeout(300);
  log('공통 층:', await p.$$eval('.layer', a => a.map(x => x.querySelector('h2').textContent + ' 부분 ' + x.querySelectorAll('.part').length)));
  log('공통 3층 부분:', await p.$$eval('#common-o-L3 .part', a => a.map(x => (x.querySelector('.ptitle h3') || {}).textContent + (x.querySelector('.ready') ? '(준비 중)' : ''))));
  log('2층 글 그림 수:', await p.$$eval('#common-o-L2 pre.art', a => a.length), '셀프 테스트 답 접힘:', await p.$$eval('#common-o-L2 details.ans', a => a.length + '개, 열린 것 ' + a.filter(x => x.open).length));
  await p.click('#common-o-L2 details.ans summary'); await p.waitForTimeout(100);
  log('답 하나 펼침:', await p.$$eval('#common-o-L2 details.ans[open]', a => a.map(x => x.textContent.slice(0, 50))));
  await p.click('#views [data-view=r]'); await p.waitForTimeout(200);
  log('공통 raw:', (await p.textContent('.cnote')).replace(/\s+/g, ' ').slice(0, 80));
  await c.close();
  for (const [hash, name] of [['#kraken', 'layers_mobile_kraken.png'], ['#common', 'layers_mobile_common.png']]) {
    const m = await b.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 1, isMobile: true, hasTouch: true }); const mp = await m.newPage(); watch(mp, 'mobile');
    await mp.goto(U + hash); await mp.waitForSelector('.layer');
    await mp.evaluate(() => document.querySelectorAll('details').forEach(d => d.open = true)); await mp.waitForTimeout(200);
    log('휴대폰', hash, '가로 폭(scroll, client):', await mp.evaluate(() => [document.documentElement.scrollWidth, document.documentElement.clientWidth]), '1층 열 수:', await mp.$eval('.cgrid', g => getComputedStyle(g).gridTemplateColumns.split(' ').length).catch(() => '1층 없음'));
    await mp.evaluate(() => { document.querySelectorAll('details').forEach(d => d.open = false); window.scrollTo(0, 0); }); await mp.waitForTimeout(100);
    await mp.screenshot({ path: path.join(OUT, name) }); await m.close();
  }
  await b.close(); log('콘솔 오류:', errs.length ? errs : '없음');
})().catch(e => { console.error('점검 실패', e); process.exit(1); });
