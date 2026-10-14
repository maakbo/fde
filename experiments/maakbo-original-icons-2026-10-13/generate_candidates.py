from pathlib import Path
from xml.etree import ElementTree as ET
import json

ROOT = Path(__file__).resolve().parent
INK = '#25231F'
MUTED = '#726D65'
LINE = '#9E988E'
FONT = "'Noto Sans CJK JP',sans-serif"
# Original geometric constructions, independently drawn for this review.
ICONS = {
    'a': {
        'user': '<circle cx="12" cy="6.6" r="3.1"/><path d="M4.4 20.2v-2.4c0-3.4 3.2-5.5 7.6-5.5s7.6 2.1 7.6 5.5v2.4"/>',
        'ellipse': '<ellipse cx="12" cy="12" rx="9.5" ry="5.65"/>',
        'file': '<circle cx="12" cy="10" r="6"/><path d="M6 16h12"/>',
        'server': '<rect x="3.4" y="4.5" width="17.2" height="15" rx="1.4"/><path d="M6.6 7.8h2.1"/>',
        'diamond': '<path d="M12 2.9 21.1 12 12 21.1 2.9 12Z"/>',
    },
    'b': {
        'user': '<ellipse cx="12" cy="6.6" rx="3" ry="3.4"/><path d="M4 20c.4-4.7 3.1-7.1 8-7.1s7.6 2.4 8 7.1"/>',
        'ellipse': '<ellipse cx="12" cy="12" rx="9.3" ry="5.55"/>',
        'file': '<path d="M5.3 3.2h9l4.4 4.5v13.1H5.3Z"/><path d="M14.3 3.2v4.5h4.4"/>',
        'server': '<rect x="3.2" y="4.7" width="17.6" height="14.6" rx="1.1"/><path d="M3.2 8.8h17.6"/>',
        'diamond': '<path d="M12 3.1 20.9 12 12 20.9 3.1 12Z"/>',
    },
}
NAMES = {'user':'人','ellipse':'業務','file':'情報','server':'システム','diamond':'判断'}
SIZES = {'user':38,'ellipse':30,'file':32,'server':32,'diamond':38}
TITLES = {'a':'A · 記号を継ぐ', 'b':'B · 初見に伝わる'}
DESC = {'a':'maakboの採用履歴を継承。円と接する下線を「情報」の共通記号に。', 'b':'文書とアプリの輪郭で意味を伝える。初めて見る人にも説明しやすく。'}

def group(family, name):
    return f'<g fill="none" stroke="currentColor" stroke-width="1.35" stroke-linecap="round" stroke-linejoin="round">{ICONS[family][name]}</g>'

def icon(family, name, x, y, size):
    return f'<svg x="{x}" y="{y}" width="{size}" height="{size}" viewBox="0 0 24 24" aria-label="{NAMES[name]}">{group(family,name)}</svg>'

def text(x,y,value,size=14,color=INK,anchor='start',weight=400):
    return f'<text x="{x}" y="{y}" fill="{color}" font-family="{FONT}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}">{value}</text>'

def svg(w,h,parts,title):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" style="color:{INK}"><title>{title}</title><rect width="{w}" height="{h}" fill="white"/>'+''.join(parts)+'</svg>'

for family, glyphs in ICONS.items():
    folder=ROOT / ('a-symbol' if family=='a' else 'b-outline')
    folder.mkdir(exist_ok=True)
    for name in glyphs:
        value=f'<!-- Original maakbo candidate; independently drawn, not an upstream icon derivative. -->\n<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><title>{NAMES[name]}</title>{group(family,name)}</svg>\n'
        (folder/f'{name}.svg').write_text(value)

parts=[text(60,63,'maakbo / original diagram icons',16,MUTED),text(60,108,'少ない線で、関係を読める。',32,weight=500),text(60,143,'デザイン比較 · 人 / 業務 / 情報 / システム / 判断',14,MUTED)]
for row,family in enumerate(['a','b']):
    y=193+row*260
    parts += [text(60,y,TITLES[family],23,weight=500),text(60,y+28,DESC[family],14,MUTED)]
    for col,name in enumerate(NAMES):
        cx=140+col*226
        parts += [icon(family,name,cx-28,y+52,56),text(cx,y+137,NAMES[name],16,anchor='middle')]
        size=SIZES[name]
        parts += [icon(family,name,cx-size/2,y+158,size),text(cx,y+220,f'{size} px',12,MUTED,anchor='middle')]
parts += ['<path d="M60 712h1080" stroke="#E5E1DA"/>',text(60,752,'関係図での見え方',21,weight=500),text(60,780,'同じ関係・同じラベル。現行の寸法と0.75pxの関係線で比較。',14,MUTED)]
for row,family in enumerate(['a','b']):
    y=806+row*112
    parts.append(text(60,y+29,family.upper(),17,MUTED))
    nodes=[('user','担当者',220),('ellipse','確認する',600),('file','確認情報',980)]
    for index in range(len(nodes)-1):
        parts.append(f'<path d="M{nodes[index][2]+26} {y+22}H{nodes[index+1][2]-26}" fill="none" stroke="{LINE}" stroke-width=".75"/>')
    for name,label,cx in nodes:
        size=SIZES[name]
        parts += [icon(family,name,cx-size/2,y+22-size/2,size),text(cx,y+70,label,14,anchor='middle')]
parts += [text(60,1057,'共通仕様  24×24 viewBox / 1.35 stroke / round cap / neutral ink / 下ラベル',12,MUTED)]
(ROOT/'comparison.svg').write_text(svg(1200,1090,parts,'maakboオリジナルアイコンの比較'))

# Mobile-size inspection: 1 SVG unit == 1 CSS pixel at native width.
parts=[text(20,37,'maakbo · 実寸の読みやすさ',20,weight=500),text(20,64,'390px幅 / 固定サイズ / 下ラベル',12,MUTED)]
for row,family in enumerate(['a','b']):
    y=108+row*173
    parts += [text(20,y,TITLES[family],18,weight=500)]
    for col,name in enumerate(NAMES):
        cx=48+col*73
        size=SIZES[name]
        parts += [icon(family,name,cx-size/2,y+27,size),text(cx,y+91,NAMES[name],12,anchor='middle')]
parts += [text(20,440,'Aの「情報」は凡例で意味を共有する記号。',12,MUTED),text(20,464,'Bの「情報」は文書寄りの意味を持つ輪郭。',12,MUTED)]
(ROOT/'mobile.svg').write_text(svg(390,490,parts,'390px幅での実寸比較'))

# A browser review with a live size slider, without a server or external assets.
cards=''
for family in ICONS:
    glyphs=''.join(f'<div class="glyph"><svg viewBox="0 0 24 24" role="img" aria-label="{NAMES[name]}">{group(family,name)}</svg><span>{NAMES[name]}</span></div>' for name in NAMES)
    cards+=f'<section><h2>{TITLES[family]}</h2><p>{DESC[family]}</p><div class="icons">{glyphs}</div></section>'
html='''<!doctype html><html lang="ja"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>maakbo アイコン比較</title><style>
*{box-sizing:border-box}body{margin:0;padding:36px 24px;color:#25231F;background:#fff;font-family:'Noto Sans CJK JP',sans-serif;line-height:1.65}main{max-width:1100px;margin:auto}h1{font-size:28px;font-weight:500;margin:8px 0}h2{font-weight:500;font-size:22px}p{color:#726D65;font-size:14px}section{padding:24px 0 36px;border-bottom:1px solid #e5e1da}.icons{display:grid;grid-template-columns:repeat(5,1fr);gap:8px;margin:28px 0}.glyph{display:flex;flex-direction:column;align-items:center;gap:12px;font-size:14px}.glyph svg{width:var(--icon-size,38px);height:var(--icon-size,38px)}label{display:flex;gap:12px;align-items:center;flex-wrap:wrap}input{accent-color:#726D65}a{color:#25231F}img{display:block;width:100%;height:auto}.links{display:flex;gap:24px;flex-wrap:wrap}@media(max-width:480px){body{padding:24px 16px}h1{font-size:23px}.glyph{font-size:12px}}
</style><main><p>maakbo / original diagram icons · review candidate</p><h1>少ない線で、関係を読める。</h1><p>2つのデザイン方向を比較。既存スキルのアイコンは変更していません。</p><label for="size">表示サイズ <input id="size" type="range" min="24" max="64" value="38"><output id="value">38 px</output></label>'''+cards+'''<section><h2>図と実寸の比較</h2><p>ここから下は現行のノード寸法を使った固定サイズの比較です。</p><img src="comparison.svg" alt="二方向の一覧、実寸、および同じ関係図での比較"></section><p class="links"><a href="comparison.svg">比較SVG</a><a href="comparison.png">比較PNG</a><a href="mobile.svg">390px実寸SVG</a></p></main><script>const s=document.querySelector('#size');s.addEventListener('input',()=>{document.documentElement.style.setProperty('--icon-size',s.value+'px');document.querySelector('#value').textContent=s.value+' px';});</script></html>'''
(ROOT/'index.html').write_text(html)

for p in ROOT.rglob('*.svg'):
    ET.parse(p)
print('Generated and parsed 12 SVGs (10 original candidates + 2 review sheets).')
