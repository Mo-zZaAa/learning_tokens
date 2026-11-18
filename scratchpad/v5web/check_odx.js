// Ondo 개요 카드(개요 패키지)와 깊이 보기 S6 점검: node scratchpad/v5web/check_odx.js
const { chromium } = require('playwright'); const path = require('path');
const U = 'file://' + path.resolve(__dirname, '../../web/v5/index.html');
const DEEP = 'file://' + path.resolve(__dirname, '../../web/v5/ondo_deep.html');
const OUT = __dirname;
(async () => {
  const b = await chromium.launch(); const errs = []; const log = (...a) => console.log(...a);
  const watch = (p, t) => { p.on('console', m => { if (m.type() === 'error') errs.push(t + ' ' + m.text()); }); p.on('pageerror', e => errs.push(t + ' ' + e.message)); };
  const c = await b.newContext({ viewport: { width: 1280, height: 900 }, deviceScaleFactor: 1 }); const p = await c.newPage(); watch(p, 'pc');
  await p.goto(U + '#ondo'); await p.waitForSelector('.odx');
  log('줄:', await p.$$eval('.odx .olab', a => a.map(x => x.textContent).join(' / ')), '| 한계 색:', await p.$eval('.orow.danger .olab', e => getComputedStyle(e).color));
  log('세부 접기:', await p.$$eval('.odx details.omore', a => a.length + '개, 열린 것 ' + a.filter(d => d.open).length), '그림 접기:', await p.$$eval('.odx details.ofig', a => a.map(d => d.querySelector('summary').textContent.slice(0, 22) + (d.open ? '(열림)' : ''))));
  log('펼친 표(돈 버는 시점):', await p.$$eval('.odx .onote .fw-tb tbody tr', a => a.length), '줄 | 태그:', await p.$$eval('.odx .tg', a => a.length), '| 용어 감싼 수:', await p.$$eval('.odx .term', a => a.length));
  await p.screenshot({ path: path.join(OUT, 'ondo_ov_pc.png') });
  // 세부 열고 닫기
  const s1 = await p.$('.odx details.omore > summary'); await s1.click(); const o1 = await p.$eval('.odx details.omore', d => d.open); await s1.click(); const o2 = await p.$eval('.odx details.omore', d => d.open);
  log('PC 세부 열기/닫기:', o1, o2);
  // 그림 USDY
  const fu = await p.$('.odx details.ofig:has(summary:text("USDY"))'); await (await fu.$('summary')).click(); await p.waitForTimeout(100);
  log('USDY 그림 열림:', await fu.evaluate(d => d.open), '단계', await fu.$$eval('.fw-stage', a => a.length), '배지', await fu.$$eval('.fw-badge', a => a.map(x => x.textContent).join(', ')));
  await fu.scrollIntoViewIfNeeded(); await fu.screenshot({ path: path.join(OUT, 'ondo_ov_flow_usdy.png') });
  await (await fu.$('summary')).click(); log('USDY 그림 닫힘:', !(await fu.evaluate(d => d.open)));
  // 태그 풀이
  await p.click('.odx .tg-s'); await p.waitForTimeout(100);
  log('on- 태그 풀이:', (await p.textContent('#tip')).slice(0, 140));
  await p.evaluate(() => { const b = Array.from(document.querySelectorAll('.odx .tg-n')).find(x => x.offsetParent); b.scrollIntoView({block: 'center'}); b.click(); }); await p.waitForTimeout(150);
  log('N 태그 풀이:', (await p.textContent('#tip')).slice(0, 120), '| 링크', await p.$$eval('#tip a', a => a.length));
  await p.keyboard.press('Escape');
  log('해석 태그 수:', await p.$$eval('.odx .tg-i', a => a.length), '추정:', await p.$$eval('.odx .tg-e', a => a.length));
  // 찾기: 접힌 세부 줄
  await p.fill('#q', 'Nest Exchange'); await p.waitForTimeout(400);
  log('찾기:', await p.textContent('#sres .sh'));
  await p.click('#sres .it'); await p.waitForTimeout(500);
  log('접힌 줄로 이동:', await p.evaluate(() => { const el = document.getElementById(location.hash.slice(1)); return [!!el && !!el.offsetParent, document.querySelectorAll('mark.hit').length, location.hash]; }));
  // Ondo raw 원본 목록의 N
  await p.click('#views [data-view=r]'); await p.waitForTimeout(400);
  log('raw 원본 목록 N:', await p.$$eval('[id^="ondo-r-src-N"]', a => a.length));
  // 메모 줄
  await p.click('#views [data-view=o]'); await p.waitForTimeout(300);
  const ln = await p.$('.odx .oi'); await ln.hover(); await (await ln.$('.mb')).click(); log('카드 줄 메모 위치:', await p.textContent('#mloc')); await p.click('[data-act=cancel]');
  // 글 규칙
  log('카드 화면 글 금지 문자:', await p.$eval('.odx', e => { const t = e.innerText; return { 긴줄표: (t.match(/[—–]/g) || []).length, 가운뎃점: (t.match(/·/g) || []).length, 제공: (t.match(/제공/g) || []).length }; }));
  await c.close();
  // 휴대폰
  const m = await b.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 1, isMobile: true, hasTouch: true }); const mp = await m.newPage(); watch(mp, 'mobile');
  await mp.goto(U + '#ondo'); await mp.waitForSelector('.odx');
  await mp.evaluate(() => document.querySelector('.odx').scrollIntoView()); await mp.waitForTimeout(100);
  await mp.screenshot({ path: path.join(OUT, 'ondo_ov_mobile.png') });
  const ms = await mp.$('.odx details.omore > summary'); await ms.tap(); const mo1 = await mp.$eval('.odx details.omore', d => d.open); await ms.tap(); const mo2 = await mp.$eval('.odx details.omore', d => d.open);
  log('휴대폰 세부 열기/닫기:', mo1, mo2);
  await mp.evaluate(() => document.querySelectorAll('.odx details').forEach(d => d.open = true)); await mp.waitForTimeout(200);
  log('휴대폰 모두 펼침 가로 폭:', await mp.evaluate(() => [document.documentElement.scrollWidth, document.documentElement.clientWidth]),
    '상자 세로 쌓기:', await mp.$eval('.fw-row', e => getComputedStyle(e).flexDirection), '넘친 상자:', await mp.$$eval('.fw-bx', a => a.filter(x => x.getBoundingClientRect().right > document.documentElement.clientWidth).length));
  await m.close();
  // 깊이 보기 S6
  const d = await b.newContext({ viewport: { width: 1280, height: 900 }, deviceScaleFactor: 1 }); const dp = await d.newPage(); watch(dp, 'deep');
  await dp.goto(DEEP + '#S6'); await dp.waitForSelector('#S6');
  log('깊이 보기 S6 그림:', await dp.$$eval('#S6 .fw', a => a.map(x => (x.querySelector('.fw-title') || {}).textContent).join(' / ')));
  const s6 = await dp.$('#S6 .fig'); await s6.screenshot({ path: path.join(OUT, 'ondo_deep_s6.png') });
  await d.close();
  const dm = await b.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 1, isMobile: true, hasTouch: true }); const dmp = await dm.newPage(); watch(dmp, 'deep-mobile');
  await dmp.goto(DEEP + '#S6'); await dmp.waitForSelector('#S6');
  log('깊이 보기 휴대폰 가로 폭:', await dmp.evaluate(() => [document.documentElement.scrollWidth, document.documentElement.clientWidth]));
  await dm.close();
  await b.close(); log('콘솔 오류:', errs.length ? errs : '없음');
})().catch(e => { console.error('점검 실패', e); process.exit(1); });
