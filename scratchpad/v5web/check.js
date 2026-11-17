// v5 화면 점검: node scratchpad/v5web/check.js
const { chromium } = require('playwright');
const path = require('path');
const OUT = __dirname;
const URL = 'file://' + path.resolve(__dirname, '../../web/v5/index.html');

(async () => {
  const browser = await chromium.launch();
  const errs = [];
  const log = (...a) => console.log(...a);
  const watch = (page, tag) => {
    page.on('console', m => { if (m.type() === 'error') errs.push(`${tag} console: ${m.text()}`); });
    page.on('pageerror', e => errs.push(`${tag} pageerror: ${e.message}`));
  };

  // ---- 데스크톱 ----
  const ctx = await browser.newContext({ viewport: { width: 1280, height: 900 }, deviceScaleFactor: 1 });
  const page = await ctx.newPage(); watch(page, 'desktop');
  await page.goto(URL); await page.waitForSelector('.ov');
  log('개요 제목:', await page.textContent('.pagehead h1'));
  log('펼친 칸:', await page.$$eval('section.sec.pin h2', a => a.map(x => x.textContent)));
  log('접힌 칸:', await page.$$eval('details.sec', a => a.map(x => x.querySelector('h2').textContent + (x.open ? '(열림)' : ''))));
  log('(판단) 표시:', await page.$$eval('.judge', a => a.length));
  log('용어 감싼 수(보이는 칸):', await page.$$eval('.term', a => a.length), '예:', await page.$$eval('.term', a => a.slice(0, 8).map(x => x.textContent).join(', ')));
  await page.screenshot({ path: path.join(OUT, 'desktop_overview.png') });

  // 용어 풍선
  const t = await page.$('.term');
  await t.hover(); await page.waitForTimeout(150);
  log('풍선 보임:', await page.isVisible('#tip'), '|', (await page.textContent('#tip')).slice(0, 80));
  // APAC 같은 말에 AP가 걸리지 않는지 (정규식 경계 점검)
  await page.evaluate(() => { const d = document.createElement('details'); d.id = 'gtest'; d.innerHTML = '<summary>t</summary><div class="gblk">APAC 지역과 AP(승인 참가자), 총플랫폼마진, 비상장 회사, SECOND와 SEC, 무기한선물과 선물</div>'; document.querySelector('.ov').appendChild(d); d.open = true; });
  await page.waitForTimeout(100);
  log('경계 점검(감싼 말):', await page.$$eval('#gtest .term', a => a.map(x => x.textContent).join(', ')));
  await page.evaluate(() => document.getElementById('gtest').remove());

  // 개요의 근거 번호 → raw 사건 카드
  await page.click('[data-act=openall]');
  let ref = await page.$('.ov .ref');
  if (!ref){ log('개요에 근거 번호 없음(카드 작성 중). raw 질문 항목의 사건 번호로 점검'); await page.click('#views [data-view=r]'); await page.waitForTimeout(200); ref = await page.$('.qa .fids .ref'); }
  const refTxt = await ref.textContent(); await ref.click(); await page.waitForTimeout(600);
  log('근거 번호', refTxt, '→ 보기:', await page.$eval('#views [aria-selected=true]', b => b.textContent), '해시:', await page.evaluate(() => location.hash), '깜빡임:', await page.evaluate(() => { const el = document.getElementById(location.hash.slice(1)); return !!el && el.classList.contains('flash'); }));

  // raw
  log('raw 칸:', await page.$$eval('details.rsec h2', a => a.map(x => x.textContent)));
  const fref = await page.$('.ev .fids .ref');
  const fTxt = await fref.textContent(); await fref.click(); await page.waitForTimeout(600);
  const fOk = await page.evaluate(id => { const el = document.getElementById(location.hash.slice(1)); return el && el.closest('details').open && el.classList.contains('flash'); }, fTxt);
  log('사건 카드 근거', fTxt, '→ 사실 DB 줄 열림과 깜빡임:', fOk);
  await page.screenshot({ path: path.join(OUT, 'desktop_raw.png') });

  // 찾기
  await page.fill('#q', 'NinjaTrader'); await page.waitForTimeout(400);
  const nres = await page.$$eval('#sres .it', a => a.length);
  log('찾기 "NinjaTrader" 결과:', nres, '|', await page.textContent('#sres .sh'));
  log('첫 결과:', (await page.textContent('#sres .it')).slice(0, 100));
  await page.click('#sres .it'); await page.waitForTimeout(700);
  log('찾은 말 칠함:', await page.$$eval('mark.hit', a => a.length), '해시:', await page.evaluate(() => location.hash));
  await page.fill('#q', '스테이킹 보상'); await page.waitForTimeout(400);
  log('찾기 "스테이킹 보상":', await page.textContent('#sres .sh'));
  await page.keyboard.press('Escape');

  // 메모(줄 단추)
  await page.click('#cos [data-co=kraken]'); await page.click('#views [data-view=o]'); await page.waitForTimeout(200);
  const line = await page.$('section.sec.pin .ln');
  await line.hover(); await (await line.$('.mb')).click();
  log('메모 창 열림:', await page.isVisible('#dlg'), '|', await page.textContent('#mloc'));
  await page.check('input[name=mtype][value="고칠 것"]', { force: true });
  await page.fill('#mtext', '점검용 메모: 이 줄의 출발 연도 확인');
  await page.click('#mform button[type=submit]'); await page.waitForTimeout(200);
  const st = await page.evaluate(() => JSON.parse(localStorage.getItem('kdx-v5-memos')));
  log('localStorage 메모:', st.memos.length, JSON.stringify(st.memos[0]).slice(0, 260));
  log('막대 메모 수:', await page.textContent('#mcount'), '줄 표시(hm):', await page.$$eval('.hm', a => a.length));

  // 메모(글 골라)
  await page.evaluate(() => { const el = document.querySelectorAll('section.sec.pin .ln .tx')[1]; const r = document.createRange(); r.selectNodeContents(el); const s = getSelection(); s.removeAllRanges(); s.addRange(r); });
  await page.waitForTimeout(350);
  log('고른 글 메모 단추:', await page.isVisible('#selBtn'));
  await page.click('#selBtn'); await page.fill('#mtext', '고른 글 메모'); await page.click('#mform button[type=submit]'); await page.waitForTimeout(150);

  // 메모 목록
  await page.click('#memoBtn'); await page.waitForTimeout(150);
  log('메모 목록:', (await page.textContent('#pin .pcnt')), '| 항목', await page.$$eval('#pin .mi', a => a.length));
  await ctx.grantPermissions(['clipboard-read', 'clipboard-write']);
  await page.click('[data-act=send]'); await page.waitForTimeout(300);
  const st2 = await page.evaluate(() => JSON.parse(localStorage.getItem('kdx-v5-memos')).memos.map(m => m.st));
  log('모아 보내기 뒤 상태:', st2.join(', '), '| 클립보드 앞부분:', (await page.evaluate(() => navigator.clipboard.readText().catch(() => ''))).slice(0, 60).replace(/\n/g, ' '));
  await page.click('#pin .mi[data-mid]'); await page.waitForTimeout(600);
  log('메모 누르면 그 자리로:', await page.evaluate(() => location.hash));

  // 준비 중 회사
  await page.click('#cos [data-co=ondo]'); await page.waitForTimeout(150);
  log('ondo 개요:', (await page.textContent('.main')).slice(0, 90).replace(/\s+/g, ' '));
  await page.click('#views [data-view=r]'); await page.waitForTimeout(200);
  log('ondo raw 칸 수:', await page.$$eval('details.rsec', a => a.length), '준비 중 상자:', await page.$$eval('.ready', a => a.length));

  // 다시 열어도 메모 유지
  await page.reload(); await page.waitForTimeout(300);
  log('새로 고친 뒤 메모 수:', await page.textContent('#mcount'));
  await ctx.close();

  // ---- 휴대폰 ----
  const m = await browser.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 1, isMobile: true, hasTouch: true });
  const mp = await m.newPage(); watch(mp, 'mobile');
  await mp.goto(URL + '#kraken'); await mp.waitForSelector('.ov');
  const ov = await mp.evaluate(() => [document.documentElement.scrollWidth, document.documentElement.clientWidth]);
  log('휴대폰 개요 가로 폭(scroll, client):', ov);
  await mp.screenshot({ path: path.join(OUT, 'mobile_overview.png') });
  await mp.tap('.term'); await mp.waitForTimeout(150);
  log('휴대폰 용어 누르면 풍선:', await mp.isVisible('#tip'));
  await mp.tap('#views [data-view=r]'); await mp.waitForTimeout(200);
  await mp.evaluate(() => document.querySelectorAll('details').forEach(d => d.open = true)); await mp.waitForTimeout(300);
  const rw = await mp.evaluate(() => [document.documentElement.scrollWidth, document.documentElement.clientWidth]);
  log('휴대폰 raw(모두 펼침) 가로 폭:', rw);
  const wide = await mp.evaluate(() => Array.from(document.querySelectorAll('#main *')).filter(e => e.getBoundingClientRect().right > document.documentElement.clientWidth + 1).slice(0, 5).map(e => e.tagName + '.' + e.className + ' ' + Math.round(e.getBoundingClientRect().right)));
  log('넘치는 요소:', wide);
  await mp.evaluate(() => window.scrollTo(0, 0));
  await m.close();

  await browser.close();
  log('콘솔 오류:', errs.length ? errs : '없음');
})().catch(e => { console.error('점검 실패:', e); process.exit(1); });
