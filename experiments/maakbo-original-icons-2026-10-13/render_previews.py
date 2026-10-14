from pathlib import Path
from playwright.sync_api import sync_playwright
import base64
ROOT=Path(__file__).resolve().parent
with sync_playwright() as p:
    browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
    page=browser.new_page(device_scale_factor=1)
    for name,width,height in [('full-set',1200,900),('mobile-full-set',390,655),('ellipse-refinement',800,475),('detail-refinement',1200,720),('four-icon-refinement',1100,1020),('repo-circle-refinement',1100,610),('repo-straight-branch',1100,610),('repository-topdown-continuation',1100,610),('balance-review',1200,830),('balance-context',1200,825)]:
        page.set_viewport_size({'width':width,'height':height})
        page.set_content('<style>body{margin:0}</style>'+ (ROOT/f'{name}.svg').read_text())
        page.screenshot(path=str(ROOT/f'{name}.png'),full_page=True)
    page.set_viewport_size({'width':390,'height':800})
    html=(ROOT/'index.html').read_text()
    for name in ['full-set','ellipse-refinement','detail-refinement','four-icon-refinement','repo-circle-refinement','repo-straight-branch','repository-topdown-continuation','balance-review','balance-context']:
        html=html.replace(f'src="{name}.svg"','src="data:image/svg+xml;base64,'+base64.b64encode((ROOT/f'{name}.svg').read_bytes()).decode()+'"')
    page.set_content(html)
    page.locator('#size').fill('32')
    page.locator('#size').dispatch_event('input')
    assert page.locator('#value').inner_text()=='32 px'
    assert page.locator('.glyph svg').first.evaluate('(e)=>getComputedStyle(e).width')=='32px'
    assert page.locator('.glyph').count()==12
    assert page.evaluate('document.documentElement.scrollWidth <= window.innerWidth')
    page.screenshot(path=str(ROOT/'mobile-browser.png'),full_page=True)
    browser.close()
print('10 PNG previews rendered; live size control and 390px no-overflow check passed.')
