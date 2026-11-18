import asyncio, json
from playwright.async_api import async_playwright
P='file:///home/user/learning_tokens/web/v5/ondo_deep.html'
O='/home/user/learning_tokens/scratchpad/ondodeep/'
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/opt/pw-browsers/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell')
        res = {}
        for name, w, h, secs in [('mobile', 390, 844, ['S2','S3','S10']), ('pc', 1440, 900, ['S2','S8','S10'])]:
            pg = await b.new_page(viewport={'width': w, 'height': h})
            errs = []
            pg.on('console', lambda m: errs.append(m.text) if m.type == 'error' else None)
            pg.on('pageerror', lambda e: errs.append(str(e)))
            await pg.goto(P); await pg.wait_for_timeout(300)
            sw = await pg.evaluate('document.documentElement.scrollWidth')
            # 넘침: 화면보다 오른쪽으로 나간 요소
            over = await pg.evaluate('''() => { const W = document.documentElement.clientWidth; const out = [];
              document.querySelectorAll('main *').forEach(e => { const r = e.getBoundingClientRect(); if (r.width && r.right > W + 1 && !e.closest('.pop')) out.push(e.tagName + '.' + e.className + ' ' + Math.round(r.right)); });
              return out.slice(0, 10); }''')
            # 펼친 상태 넘침도 확인
            await pg.click('#openall'); await pg.wait_for_timeout(200)
            over2 = await pg.evaluate('''() => { const W = document.documentElement.clientWidth; const out = [];
              document.querySelectorAll('main *').forEach(e => { const r = e.getBoundingClientRect(); if (r.width && r.right > W + 1) out.push(e.tagName + '.' + e.className + ' ' + Math.round(r.right)); });
              return out.slice(0, 10); }''')
            await pg.click('#closeall')
            # 각주, 용어 팝업 동작
            await pg.click('.fn >> nth=0'); pop1 = await pg.is_visible('#pop')
            await pg.keyboard.press('Escape')
            await pg.click('.term >> nth=0'); pop2 = await pg.is_visible('#pop')
            await pg.keyboard.press('Escape')
            await pg.add_style_tag(content='.top{position:static}')
            for s in secs:
                el = pg.locator('#' + s)
                await el.scroll_into_view_if_needed()
                await el.screenshot(path=f'{O}{name}_{s}.png')
            res[name] = dict(scrollWidth=sw, overflow=over, overflow_open=over2, errors=errs, fn_pop=pop1, term_pop=pop2)
            await pg.close()
        # 다크 모드
        pg = await b.new_page(viewport={'width': 390, 'height': 844}, color_scheme='dark')
        await pg.goto(P); await pg.locator('#S3').screenshot(path=f'{O}mobile_dark_S3.png')
        await b.close()
        print(json.dumps(res, ensure_ascii=False, indent=1))
asyncio.run(main())
