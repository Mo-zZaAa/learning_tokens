// raw 본문과 메모 답 점검: node scratchpad/v5web/check_body.js
const { chromium } = require('playwright'); const path = require('path');
const U = 'file://' + path.resolve(__dirname, '../../web/v5/index.html'); const OUT = __dirname;
(async () => {
  const b = await chromium.launch(); const errs = []; const log = (...a) => console.log(...a);
  const watch = (p, t) => { p.on('console', m => { if (m.type() === 'error') errs.push(t + ' ' + m.text()); }); p.on('pageerror', e => errs.push(t + ' ' + e.message)); };
  const c = await b.newContext({ viewport: { width: 1280, height: 900 }, deviceScaleFactor: 1 }); const p = await c.newPage(); watch(p, 'desktop');
  for (const co of ['ondo', 'kraken']) {
    const t0 = Date.now(); await p.goto(U + '#' + co + '-raw'); await p.waitForSelector('.raw .body'); const ms = Date.now() - t0;
    const info = await p.evaluate(() => {
      const vis = e => { const r = e.getBoundingClientRect(); return r.top < innerHeight && r.bottom > 0; };
      return { lines: document.querySelectorAll('.body .ol').length, subs: document.querySelectorAll('.fsub').length,
        firstScreenLines: Array.from(document.querySelectorAll('.body .ol')).filter(vis).length,
        firstScreenSubs: Array.from(document.querySelectorAll('.fsub')).filter(vis).length,
        refOpen: document.querySelector('[id$="-r-sec-ref"]').open, terms: document.querySelectorAll('.body .term').length,
        firstSub: (document.querySelector('.fsub') || {}).textContent };
    });
    log(co, '열기 ms', ms, JSON.stringify(info).slice(0, 420));
    await p.screenshot({ path: path.join(OUT, `raw_body_${co}_desktop.png`) });
  }
  // 원문 모두 접기
  await p.click('[data-act=togglesrc]'); log('원문 접기 뒤 보이는 하위 줄:', await p.$$eval('.fsub', a => a.filter(x => x.offsetParent).length));
  await p.click('[data-act=togglesrc]');
  // 더 보기
  const more = await p.$('.more'); if (more) { await more.click(); log('더 보기 펼침:', await p.$eval('.q2', e => !e.hidden)); }
  // 찾기 -> 원문 하위 줄
  await p.fill('#q', 'custody'); await p.waitForTimeout(400);
  log('찾기 custody:', await p.textContent('#sres .sh'));
  const it = await p.$('#sres .it:has(.loc:text("본문 원문"))'); if (it) { await it.click(); await p.waitForTimeout(500); log('원문 줄로 이동:', await p.evaluate(() => location.hash), '칠함', await p.$$eval('mark.hit', a => a.length)); }
  // 메모: 하위 줄
  const sub = await p.$('.fsub'); await sub.hover(); await (await sub.$('.mb')).click();
  log('하위 줄 메모 위치:', await p.textContent('#mloc')); await p.click('[data-act=cancel]');
  // 메모 답(실제 kb/memo_answers.csv)
  log('위 막대 답 수:', await p.textContent('#acount'));
  await p.click('#cos [data-co=ondo]'); await p.click('#views [data-view=o]'); await p.waitForTimeout(300);
  log('ondo 개요 답 꼬리표:', await p.$$eval('.abadge', a => a.length), '답 있는 줄:', await p.$$eval('.ha', a => a.length));
  await p.click('#memoBtn'); await p.waitForTimeout(200);
  log('메모 목록:', await p.textContent('#pin .pcnt'));
  log('답 상자 수:', await p.$$eval('#pin .mans', a => a.length), '| 첫 답:', ((await p.textContent('#pin .mans')) || '').slice(0, 120));
  await p.screenshot({ path: path.join(OUT, 'memo_answers_panel.png') });
  await p.click('[data-act=closepanel]');
  await p.fill('#q', ''); await p.waitForTimeout(100);
  await c.close();
  for (const co of ['ondo', 'kraken']) {
    const m = await b.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 1, isMobile: true, hasTouch: true }); const mp = await m.newPage(); watch(mp, 'mobile');
    await mp.goto(U + '#' + co + '-raw'); await mp.waitForSelector('.raw .body');
    await mp.screenshot({ path: path.join(OUT, `raw_body_${co}_mobile.png`) });
    await mp.evaluate(() => document.querySelectorAll('details').forEach(d => d.open = true)); await mp.waitForTimeout(300);
    log('휴대폰', co, 'raw 모두 펼침 가로 폭:', await mp.evaluate(() => [document.documentElement.scrollWidth, document.documentElement.clientWidth]));
    await m.close();
  }
  await b.close(); log('콘솔 오류:', errs.length ? errs : '없음');
})().catch(e => { console.error('점검 실패', e); process.exit(1); });
