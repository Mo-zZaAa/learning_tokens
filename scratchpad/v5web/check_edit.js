// 표 너비 조절과 화면에서 고치기 점검: node scratchpad/v5web/check_edit.js
const { chromium } = require('playwright'); const path = require('path');
const U = 'file://' + path.resolve(__dirname, '../../web/v5/index.html');
(async () => {
  const b = await chromium.launch(); const errs = [];
  const c = await b.newContext({ viewport: { width: 1280, height: 900 } }); const p = await c.newPage();
  p.on('pageerror', e => errs.push(e.message)); p.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
  await p.goto(U + '#kraken'); await p.waitForSelector('.odx');
  console.log('PM 표시 남은 수(1층):', await p.evaluate(() => document.querySelectorAll('.odx .pmq').length));
  // 표 너비
  const tb = await p.$('.odx details.omore[open] table.tbl');
  const th = (await tb.$$('thead th'))[1];
  await th.evaluate(e => e.scrollIntoView({block: 'center'})); const before = (await th.boundingBox()).width;
  const hb = await (await th.$('.rzh')).boundingBox();
  await p.mouse.move(hb.x + hb.width / 2, hb.y + hb.height / 2); await p.mouse.down();
  await p.mouse.move(hb.x + 160, hb.y + hb.height / 2, { steps: 8 }); await p.mouse.up();
  const after = (await th.boundingBox()).width;
  console.log('칸 너비', Math.round(before), '→', Math.round(after));
  await tb.scrollIntoViewIfNeeded(); await p.screenshot({ path: path.join(__dirname, 'edit_resize.png') });
  // 고치기
  await p.click('#edBtn');
  const ln = (await p.$$('.odx .orow .oi'))[0];
  const id = await ln.getAttribute('id');
  await ln.click({ position: { x: 40, y: 8 } });
  console.log('편집 창 열림:', await p.isVisible('#edlg'), '| 처음 글:', (await p.inputValue('#etext')).slice(0, 40));
  await p.fill('#etext', '==고친 줄== 시험');
  await p.click('#eform button[type=submit]'); await p.waitForTimeout(200);
  console.log('줄 바뀜:', await p.$eval('#' + id + ' .tx', e => e.innerHTML.slice(0, 60)));
  // 표 칸 고치기
  const td = await p.$('.odx details.omore[open] table.tbl tbody tr.ln td:nth-child(2)');
  await td.click(); await p.fill('#etext', '칸을 고침'); await p.click('#eform button[type=submit]'); await p.waitForTimeout(200);
  console.log('칸 바뀜:', await td.innerText());
  // 줄 지우기
  const ln2 = (await p.$$('.odx .orow'))[1] ? await (await p.$$('.odx .orow'))[1].$('.oi') : null; const id2 = await ln2.getAttribute('id');
  await ln2.click({ position: { x: 40, y: 8 } }); await p.click('[data-eact="del"]'); await p.waitForTimeout(150);
  await p.click('[data-eact="off"]');
  console.log('지운 줄 숨김:', await p.$eval('#' + id2, e => getComputedStyle(e.closest('li')).display), '| 고친 곳 수:', await p.textContent('#ecount'));
  // 다시 열기: 남아 있나
  await p.reload(); await p.waitForSelector('.odx');
  console.log('다시 연 뒤 줄:', await p.$eval('#' + id + ' .tx', e => e.textContent.slice(0, 20)), '| 너비 유지:', Math.round((await (await (await p.$('.odx details.omore[open] table.tbl')).$$('thead th'))[1].boundingBox()).width));
  // 원래대로
  await p.click('#edBtn'); await (await p.$('#' + id)).click({ position: { x: 40, y: 8 } }); await p.click('[data-eact="reset"]'); await p.waitForTimeout(150);
  console.log('원래대로:', await p.$eval('#' + id + ' .tx', e => e.textContent.slice(0, 30)));
  await c.close();
  const m = await b.newContext({ viewport: { width: 390, height: 844 }, isMobile: true }); const mp = await m.newPage();
  await mp.goto(U + '#robinhood'); await mp.waitForSelector('.odx');
  await mp.evaluate(() => document.querySelectorAll('details').forEach(d => { d.open = true; }));
  console.log('휴대폰 가로 폭', await mp.evaluate(() => [document.documentElement.scrollWidth, document.documentElement.clientWidth]), '머리 칸 손잡이 보임', await mp.evaluate(() => [...document.querySelectorAll('.rzh')].filter(x => x.offsetParent).length));
  await b.close(); console.log('오류', errs.length ? errs.slice(0, 3) : '없음');
})();
