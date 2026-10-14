from pathlib import Path
from xml.etree import ElementTree as ET
from html import escape
ET.register_namespace("", "http://www.w3.org/2000/svg")

ROOT=Path(__file__).resolve().parent
INK='#25231F'; MUTED='#726D65'; FONT="'Noto Sans CJK JP',sans-serif"
# Original geometry. Not copied from upstream icon paths.
GLYPHS={
'user':'<ellipse cx="12" cy="6.9" rx="3.6" ry="3.9"/><path d="M5.4 19.8c.4-3.8 2.6-5.7 6.6-5.7s6.2 1.9 6.6 5.7"/>',
'ellipse':'<ellipse cx="12" cy="12" rx="9.3" ry="6"/>',
'file':'<path d="M6.1 3.2h8.2l4.4 4.5V20q0 .8-.8.8H6.1q-.8 0-.8-.8V4q0-.8.8-.8Z"/><path d="M14.3 3.2v4q0 .5.5.5h3.9"/>',
'server':'<rect x="3.4" y="4.5" width="17.2" height="15" rx="1.4"/><path d="M6.6 7.8h2.1"/>',
'diamond':'<path d="M12 3.1 20.9 12 12 20.9 3.1 12Z"/>',
'bot':'<rect x="4.3" y="7.2" width="15.4" height="12.7" rx="1.7"/><path d="M12 7.2V3.5h2.5"/><path d="M8.7 12.4v2.3m6.6-2.3v2.3"/>',
'folder-git-2':'<path d="M8 7.1V16.2M9.83019 6.19298L15.16981 10.25702"/><circle cx="8" cy="4.8" r="2.3"/><circle cx="8" cy="18.5" r="2.3"/><circle cx="17" cy="11.65" r="2.3"/>',
'cloud':'<path d="M6.1 19h12a3.2 3.2 0 0 0 .7-6.3 5.2 5.2 0 0 0-10.1-2.3A4.4 4.4 0 0 0 6.1 19Z"/>',
'message-square':'<path d="M3.5 4.7h17v12.1H10l-4.6 3v-3H3.5Z"/>',
'laptop':'<rect x="4" y="5.3" width="16" height="10.4" rx=".95"/><path d="m4 15.7-1.5 2.9h19L20 15.7"/>',
'smartphone':'<rect x="6.4" y="2.8" width="11.2" height="18.4" rx="2"/><path d="M10.4 5.3h3.2"/>',
'tablet':'<rect x="4.6" y="2.3" width="14.8" height="19.4" rx="1.7"/>',
}
LABELS={'user':'人','ellipse':'業務','file':'情報','server':'システム','diamond':'判断','bot':'AI','folder-git-2':'リポジトリ','cloud':'外部サービス','message-square':'会話','laptop':'PC','smartphone':'スマホ','tablet':'タブレット'}
SIZES={name:(38 if name in ['user','bot','diamond'] else 30 if name=='ellipse' else 32) for name in GLYPHS}
ORDER=['user','bot','ellipse','diamond','file','server','folder-git-2','cloud','message-square','laptop','smartphone','tablet']
STEPS={
'user':['少し大きめの頭の輪を描く','下に小さめの肩の山を描く'],
'bot':['少し角を丸めた四角い頭を描く','上に短いアンテナを足す','中に縦向きの目を2本描く'],
'ellipse':['横長で少しふっくらした楕円を描く'],
'diamond':['四辺を斜めにつないで菱形にする'],
'file':['角を少し丸め、右上を欠いた紙の輪郭を描く','欠いた角に小さな折り返しを足す'],
'server':['横長の四角い枠を描く','左上に短い状態表示を足す'],
'folder-git-2':['上と下、右の中間の高さに小さな丸を描く','上の丸から下の丸へ縦線を引く','上の丸から右の丸へ斜めの直線を引く'],
'cloud':['水平な底辺と3つの山をつないで雲を描く'],
'message-square':['下に短いしっぽのある四角を描く'],
'laptop':['少し角を丸めた横長の画面を描く','下を広げて底辺につなぐ'],
'smartphone':['角を丸めた細い縦長の四角を描く','上に短線を1本足す'],
'tablet':['角を丸めた幅のある縦長の四角を描く'],
}

# Uniform scale preserves each hand-drawn shape's proportions. Stroke compensation
# cancels the geometric scale, so the effective viewBox stroke stays exactly 1.15.
BALANCE={'user':(1.05,0,.25),'bot':(.96,0,.15),'ellipse':(1.03,0,0),
         'diamond':(.93,0,0),'folder-git-2':(1.08,.4,.25),'cloud':(1,0,-.55)}
def g(name):
    scale,dx,dy=BALANCE.get(name,(1,0,0))
    tx=12*(1-scale)+dx;ty=12*(1-scale)+dy
    transform='' if (scale,dx,dy)==(1,0,0) else f' transform="translate({tx:.5f} {ty:.5f}) scale({scale:.5f})"'
    return f'<g fill="none" stroke="currentColor" stroke-width="{1.15/scale:.9f}" stroke-linecap="round" stroke-linejoin="round"{transform}>{GLYPHS[name]}</g>'
def historical_g(name):
    root=ET.parse(ROOT/'revision-history'/'before-balance'/f'{name}.svg').getroot()
    return ET.tostring(root.find('{http://www.w3.org/2000/svg}g'),encoding='unicode')
def icon(name,x,y,size):
    return f'<svg x="{x}" y="{y}" width="{size}" height="{size}" viewBox="0 0 24 24">{g(name)}</svg>'
def t(x,y,s,size=14,color=INK,anchor='start',weight=400):
    return f'<text x="{x}" y="{y}" fill="{color}" font-family="{FONT}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}">{escape(s)}</text>'
def svg(w,h,p,title):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" style="color:{INK}"><title>{title}</title><rect width="{w}" height="{h}" fill="white"/>'+''.join(p)+'</svg>'

folder=ROOT/'maakbo-handdrawn';folder.mkdir(exist_ok=True)
for name in ORDER:
    (folder/f'{name}.svg').write_text(f'<!-- Original maakbo geometry. Review-ready maakbo hand-drawable family. -->\n<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" style="color:{INK}"><title>{LABELS[name]}</title>{g(name)}</svg>\n')

p=[t(60,50,'maakbo / original diagram icons',16,MUTED),t(60,96,'形はそのまま、大きさの釣り合いを整える。',30,weight=500),t(60,131,'全12種類 · 上は拡大 / 下は実際に使う寸法 · 細線の太さは維持',14,MUTED)]
for i,name in enumerate(ORDER):
    row,col=divmod(i,4);cx=180+280*col;y=161+215*row
    p += [icon(name,cx-28,y,56),t(cx,y+86,LABELS[name],17,anchor='middle')]
    size=SIZES[name]
    p += [icon(name,cx-size/2,y+111,size),t(cx,y+172,f'{size} px',12,MUTED,anchor='middle')]
p += ['<path d="M60 808h1080" stroke="#E5E1DA"/>',t(60,849,'リポジトリは上から下へ。右の丸は中間。前後の追加線なし。',14,MUTED),t(60,877,'24×24 viewBox / effective 1.15 stroke / neutral #25231F / original geometry',12,MUTED)]
(ROOT/'full-set.svg').write_text(svg(1200,900,p,'maakbo 大きさの釣り合いを整えた全12種類'))

p=[t(20,37,'maakbo · 12種類の実寸',20,weight=500),t(20,65,'390px幅 / 現行のノード寸法 / 下ラベル',12,MUTED)]
for i,name in enumerate(ORDER):
    row,col=divmod(i,3);cx=65+130*col;y=109+122*row;size=SIZES[name]
    p += [icon(name,cx-size/2,y,size),t(cx,y+61,LABELS[name],12,anchor='middle'),t(cx,y+82,f'{size} px',11,MUTED,anchor='middle')]
p += [t(20,623,'細部より、輪郭と短いラベルで区別する。',12,MUTED)]
(ROOT/'mobile-full-set.svg').write_text(svg(390,655,p,'390px幅での全12アイコン実寸'))

p=[t(40,44,'業務の楕円 · ごく小さな調整',25,weight=500),t(40,79,'横幅はそのまま、縦の丸みだけ少し増やす。',14,MUTED)]
for x,ry,label in [(210,5.55,'変更前'),(590,6,'変更後')]:
    p += [f'<svg x="{x-60}" y="111" width="120" height="120" viewBox="0 0 24 24"><ellipse cx="12" cy="12" rx="9.3" ry="{ry}" fill="none" stroke="{INK}" stroke-width="1.15"/></svg>',t(x,269,label,17,anchor='middle'),t(x,298,f'ry {ry:.2f}',13,MUTED,anchor='middle')]
    p += [f'<svg x="{x-15}" y="333" width="30" height="30" viewBox="0 0 24 24"><ellipse cx="12" cy="12" rx="9.3" ry="{ry}" fill="none" stroke="{INK}" stroke-width="1.15"/></svg>',t(x,390,'実寸30px',12,MUTED,anchor='middle')]
p += [t(40,440,'実寸で高さは約1.13px増。大きな形の変更ではありません。',13,MUTED)]
(ROOT/'ellipse-refinement.svg').write_text(svg(800,475,p,'業務の楕円の変更前後'))

rows='\n'.join('| '+LABELS[n]+' | `'+n+'.svg` | '+str(SIZES[n])+'px | '+' → '.join(f'{i+1}. {step}' for i,step in enumerate(STEPS[n]))+' |' for n in ORDER)
(ROOT/'handwriting-guide.md').write_text('# maakbo — 手書きの順序\n\n線の揺れや角の丸みを揃える必要はありません。輪郭と種類の違いを残せれば十分です。\n\n| 記号 | ファイル | 現行サイズ | 1〜3ステップの描き方 |\n| --- | --- | --- | --- |\n'+rows+'\n\n「ステップ」は形を作る動作の単位です。一筆の回数ではありません。人の頭と雲は意味を保つため曲線を使い、その他は四角と短線を土台にします。業務は横長の楕円を保ち、わずかに縦へふっくらさせます。\n\nシステムは短い状態表示、リポジトリは3つの小さな丸と枝、会話はしっぽ、PCは底辺、スマホは細い縦長と短線、タブレットは幅のある縦長で区別します。端末は少し角を丸め、タブレットを縦横比約0.76、PC画面を横長にします。ホームボタンやメーカー固有のノッチ、ロゴは入れません。雲の中に接続やダウンロードの矢印は足さず、外部サービスという意味を保ちます。\n')

# Keep the hand-drawing steps stable; display sizes are a separate review choice.
guide=ROOT/'handwriting-guide.md'
guide.write_text(guide.read_text()+'\nリポジトリは上から下、右の丸は上下の中間、上下の追加線なしで確定。全12の見た目のサイズ調整は[サイズ調整表](optical-balance.md)を参照。形のパーツや描き順は変えていません。\n')

cards=''.join(f'<div class="glyph"><svg viewBox="0 0 24 24" role="img" aria-label="{LABELS[n]}">{g(n)}</svg><span>{LABELS[n]}</span><small>{len(STEPS[n])}ステップ</small></div>' for n in ORDER)
html='''<!doctype html><html lang="ja"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>maakbo · 手書きの12記号</title><style>*{box-sizing:border-box}body{margin:0;padding:32px 20px;color:#25231F;background:#fff;font-family:'Noto Sans CJK JP',sans-serif;line-height:1.7}main{max-width:1100px;margin:auto}h1{font-size:30px;font-weight:500}h2{font-size:22px;font-weight:500}p,small{color:#726D65}p{font-size:14px}.icons{display:grid;grid-template-columns:repeat(4,1fr);gap:36px 20px;padding:36px 0}.glyph{display:flex;flex-direction:column;align-items:center;gap:8px}.glyph svg{width:var(--icon-size,38px);height:var(--icon-size,38px)}.glyph small{font-size:12px}label{display:flex;gap:12px;align-items:center;flex-wrap:wrap}input{accent-color:#726D65}img{width:100%;height:auto;display:block}a{color:#25231F}section{padding:26px 0;border-top:1px solid #E5E1DA}.links{display:flex;gap:20px;flex-wrap:wrap}@media(max-width:480px){h1{font-size:23px}.icons{grid-template-columns:repeat(3,1fr);gap:32px 6px}.glyph span{font-size:12px}}</style><main><p>maakbo / original diagram icons · selected symbol family</p><h1>四角を基本に、さっと描ける。</h1><p>情報はBの紙、システムはAの状態表示付き枠。手で描き直せる12種類へ統一し、大きさの釣り合いを整えました。業務の楕円は、気持ちだけ縦にふっくらさせました。AIの目は縦線に、全体の線は少し細く、端末の角はやわらかく調整しています。人は頭を大きめ・肩を小さめに、AI・情報は少し角を丸めた試案です。リポジトリはフォルダを外し、小さな丸3つと枝分かれへ変更しました。時間は上から下へ。右の丸を上と下の中間の高さにし、上の丸から2つの丸へ直線でつないでいます。</p><label for="size">表示サイズ<input id="size" type="range" min="24" max="64" value="38"><output id="value">38 px</output></label><div class="icons">'''+cards+'''</div><section><h2>全12種類と実寸</h2><img src="full-set.svg" alt="全12アイコンの拡大図と現行サイズ"></section><section><h2>実寸の大きさを整える</h2><img src="balance-review.svg" alt="全12種類の現行と大きさ調整後を実寸で比較"></section><section><h2>図での釣り合い</h2><img src="balance-context.svg" alt="人・業務・情報・システム・リポジトリの同じ図を実寸で比較"></section><section><h2>上から下・右の丸は中間へ（比較履歴・追加線なしを採用）</h2><img src="repository-topdown-continuation.svg" alt="中間の高さに丸を配置し、上下の短い継続線を加えるか比較（追加線なし採用済み）"></section><section><h2>リポジトリの枝を直線に（前段階）</h2><img src="repo-straight-branch.svg" alt="丸の配置と大きさを保ち、枝だけ曲線から直線へ変えた比較"></section><section><h2>リポジトリの丸を小さく（前段階）</h2><img src="repo-circle-refinement.svg" alt="枝分かれ案の丸を半径2.9から2.3へ小さくした比較"></section><section><h2>人・AI・リポジトリ・情報の試案（前段階）</h2><img src="four-icon-refinement.svg" alt="直前の4種類と大きめ頭・軽い角丸の比較"></section><section><h2>目・線幅・端末の調整</h2><img src="detail-refinement.svg" alt="AIの目、線幅、PC・スマホ・タブレットの変更前後"></section><section><h2>楕円の変更前後</h2><img src="ellipse-refinement.svg" alt="縦半径5.55から6への小さな調整"></section><p class="links"><a href="full-set.png">全12種類PNG</a><a href="mobile-full-set.png">390px実寸PNG</a><a href="handwriting-guide.md">手書きの順序</a><a href="comparison.svg">最初のA/B比較</a></p></main><script>const s=document.querySelector('#size');s.addEventListener('input',()=>{document.documentElement.style.setProperty('--icon-size',s.value+'px');document.querySelector('#value').textContent=s.value+' px';});</script></html>'''
(ROOT/'index.html').write_text(html)
for p in folder.glob('*.svg'):ET.parse(p)
for name in ['full-set','mobile-full-set','ellipse-refinement']:ET.parse(ROOT/f'{name}.svg')

# The previous review geometry is kept here only for the before/after board.
BEFORE={
'bot':'<rect x="4.3" y="7.2" width="15.4" height="12.7" rx="1.1"/><path d="M12 7.2V3.5h2.5"/><path d="M8 13.6h1.5m5 0H16"/>',
'laptop':'<rect x="5" y="4.8" width="14" height="11.2" rx=".6"/><path d="m5 16-2.6 3.2h19.2L19 16"/>',
'smartphone':'<rect x="6.4" y="2.8" width="11.2" height="18.4" rx="1.2"/><path d="M10.4 5.3h3.2"/>',
'tablet':'<rect x="3.5" y="2.8" width="17" height="18.4" rx="1.2"/>',
}
p=[t(60,54,'maakbo / detail refinement',16,MUTED),t(60,99,'目を起こして、線と角をやわらかく。',30,weight=500),t(60,136,'上：前の案 1.35　下：今回の案 1.15　下部に実寸を併記',14,MUTED)]
for col,name in enumerate(BEFORE):
    cx=180+280*col
    p += [t(cx,190,LABELS[name],18,anchor='middle')]
    p += [f'<svg x="{cx-40}" y="218" width="80" height="80" viewBox="0 0 24 24"><g fill="none" stroke="{INK}" stroke-width="1.35" stroke-linecap="round" stroke-linejoin="round">{BEFORE[name]}</g></svg>',t(cx,330,'変更前',13,MUTED,anchor='middle')]
    p += [f'<svg x="{cx-40}" y="380" width="80" height="80" viewBox="0 0 24 24">{historical_g(name)}</svg>',t(cx,492,'変更後',13,MUTED,anchor='middle')]
    size=SIZES[name]
    p += [f'<svg x="{cx-size/2}" y="526" width="{size}" height="{size}" viewBox="0 0 24 24">{historical_g(name)}</svg>',t(cx,592,f'実寸{size}px',12,MUTED,anchor='middle')]
p += [t(60,643,'AIは横棒から縦の目に。端末は角丸と縦横比を調整し、ロゴや細部は加えない。',14,MUTED),t(60,682,'全12種類の線幅を1.15に統一。1.35より約15%細く。',14,MUTED)]
(ROOT/'detail-refinement.svg').write_text(svg(1200,720,p,'AIの目・線幅・端末の変更前後'))
ET.parse(ROOT/'detail-refinement.svg')

# Four saved SVG originals are the unchanged previous revision for this comparison.
p=[t(50,52,'maakbo / four-icon refinement',16,MUTED),t(50,96,'頭を大きめに。角を、ほんの少し丸く。',29,weight=500),t(50,131,'直前の案と今回の試案 · 4種類のみ変更 / 線幅1.15は共通',14,MUTED),t(345,184,'直前の案',18,anchor='middle'),t(795,184,'今回の試案',18,anchor='middle')]
for row,name in enumerate(['user','bot','folder-git-2','file']):
    y=225+row*182;size=SIZES[name]
    previous=ET.parse(ROOT/'revision-history'/'before-four-icon-review'/f'{name}.svg').getroot()
    oldgroup=ET.tostring(previous.find('{http://www.w3.org/2000/svg}g'),encoding='unicode')
    newgroup=historical_g(name)
    if name=='folder-git-2':
        saved=ET.parse(ROOT/'revision-history'/'before-repository-adoption'/f'{name}.svg').getroot()
        newgroup=ET.tostring(saved.find('{http://www.w3.org/2000/svg}g'),encoding='unicode')
    p += [t(50,y+48,LABELS[name],17),f'<svg x="301" y="{y}" width="88" height="88" viewBox="0 0 24 24">{oldgroup}</svg>',f'<svg x="751" y="{y}" width="88" height="88" viewBox="0 0 24 24">{newgroup}</svg>']
    p += [f'<svg x="{345-size/2}" y="{y+102}" width="{size}" height="{size}" viewBox="0 0 24 24">{oldgroup}</svg>',f'<svg x="{795-size/2}" y="{y+102}" width="{size}" height="{size}" viewBox="0 0 24 24">{newgroup}</svg>']
    p += [t(345,y+156,f'実寸{size}px',11,MUTED,anchor='middle'),t(795,y+156,f'実寸{size}px',11,MUTED,anchor='middle')]
p += [t(50,988,'人は輪郭だけで表す。AIの縦の目、フォルダの枝、紙の折り返しは残す。',13,MUTED)]
(ROOT/'four-icon-refinement.svg').write_text(svg(1100,1020,p,'4種類の直前案と軽い角丸の試案'))
ET.parse(ROOT/'four-icon-refinement.svg')

# Selected branch, reduced circles. The earlier repository comparison remains unchanged.
(ROOT/'candidate-repository'/'branch.svg').write_text((folder/'folder-git-2.svg').read_text())
previous=ET.parse(ROOT/'revision-history'/'before-repository-adoption'/'branch.svg').getroot()
oldgroup=ET.tostring(previous.find('{http://www.w3.org/2000/svg}g'),encoding='unicode')
p=[t(50,50,'maakbo / repository circle refinement',16,MUTED),t(50,95,'丸を小さく、枝を自然に。',29,weight=500),t(50,131,'候補2を採用 · 丸の半径 2.90 → 2.30 / 線幅1.15は同じ',14,MUTED)]
saved=ET.parse(ROOT/'revision-history'/'before-straight-branch'/'folder-git-2.svg').getroot()
small_curved_group=ET.tostring(saved.find('{http://www.w3.org/2000/svg}g'),encoding='unicode')
for x,mark,title in [(280,oldgroup,'縮小前'),(820,small_curved_group,'今回の採用案')]:
    p += [t(x,199,title,20,anchor='middle'),f'<svg x="{x-60}" y="230" width="120" height="120" viewBox="0 0 24 24">{mark}</svg>',t(x,385,'リポジトリ',17,anchor='middle'),f'<svg x="{x-16}" y="435" width="32" height="32" viewBox="0 0 24 24">{mark}</svg>',t(x,505,'実寸32px',12,MUTED,'middle')]
p += [t(50,568,'丸を約21%小さく。縦線と枝は丸の縁に合わせ、丸の中に線を通さない。',14,MUTED)]
(ROOT/'repo-circle-refinement.svg').write_text(svg(1100,610,p,'リポジトリの丸の縮小前後'))
ET.parse(ROOT/'repo-circle-refinement.svg')

# Change only the branch to a straight line; circle size and positions are unchanged.
previous=ET.parse(ROOT/'revision-history'/'before-straight-branch'/'folder-git-2.svg').getroot()
oldgroup=ET.tostring(previous.find('{http://www.w3.org/2000/svg}g'),encoding='unicode')
p=[t(50,50,'maakbo / straight branch refinement',16,MUTED),t(50,95,'枝を曲げず、まっすぐつなぐ。',29,weight=500),t(50,131,'丸3つの位置と大きさ・全体寸法・線幅は同じ。枝だけ変更。',14,MUTED)]
saved=ET.parse(ROOT/'revision-history'/'before-topdown-adoption'/'folder-git-2.svg').getroot()
straight_old_group=ET.tostring(saved.find('{http://www.w3.org/2000/svg}g'),encoding='unicode')
for x,mark,title in [(280,oldgroup,'直前 · 曲線の枝'),(820,straight_old_group,'今回 · 直線の枝')]:
    p += [t(x,199,title,20,anchor='middle'),f'<svg x="{x-60}" y="230" width="120" height="120" viewBox="0 0 24 24">{mark}</svg>',t(x,385,'リポジトリ',17,anchor='middle'),f'<svg x="{x-16}" y="435" width="32" height="32" viewBox="0 0 24 24">{mark}</svg>',t(x,505,'実寸32px',12,MUTED,'middle')]
p += [t(50,568,'縦の幹の途中から、右上の丸の左下の縁へ、斜めの直線を1本。',14,MUTED)]
(ROOT/'repo-straight-branch.svg').write_text(svg(1100,610,p,'リポジトリの曲線と直線の枝比較'))
ET.parse(ROOT/'repo-straight-branch.svg')

# Selected top-down timeline. Optional continuation ticks are a separate review candidate.
(ROOT/'candidate-repository'/'top-down-midpoint.svg').write_text((folder/'folder-git-2.svg').read_text())
continuation=historical_g('folder-git-2').replace('</g>','<path d="M8 1V2.5M8 20.8V22.3"/></g>')
(ROOT/'candidate-repository'/'top-down-continuation.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" style="color:{INK}"><title>リポジトリ・継続線の候補</title>{continuation}</svg>\n')
p=[t(50,50,'maakbo / top-down continuation review',16,MUTED),t(50,95,'上から下へ。右の丸は、中間の高さに。',28,weight=500),t(50,131,'同じ3点の配置で、履歴が前後に続く短線を比べる。',14,MUTED)]
for x,mark,title in [(280,historical_g('folder-git-2'),'基本案 · 追加線なし'),(820,continuation,'比較案 · 前後に短い線')]:
    p += [t(x,199,title,20,anchor='middle'),f'<svg x="{x-60}" y="230" width="120" height="120" viewBox="0 0 24 24">{mark}</svg>',t(x,385,'リポジトリ',17,anchor='middle'),f'<svg x="{x-16}" y="435" width="32" height="32" viewBox="0 0 24 24">{mark}</svg>',t(x,505,'実寸32px',12,MUTED,'middle')]
p += [t(50,568,'右の丸は上4.80と下18.50の中間11.65。追加線は上下とも長さ1.50。',14,MUTED)]
(ROOT/'repository-topdown-continuation.svg').write_text(svg(1100,610,p,'上から下の中間配置と前後の継続線比較'))
ET.parse(ROOT/'repository-topdown-continuation.svg')
ET.parse(ROOT/'candidate-repository'/'top-down-continuation.svg')

# Compare every icon at its real Mermaid node size, preserving each node canvas.
p=[t(50,50,'maakbo / optical balance review',16,MUTED),t(50,94,'実際に使う大きさで、釣り合いを比べる。',28,weight=500),t(50,129,'各欄の左：調整前 / 右：調整後 · 枠の寸法と細線の太さは同じ',14,MUTED)]
for i,name in enumerate(ORDER):
    row,col=divmod(i,3);base=40+390*col;y=169+146*row;size=SIZES[name]
    p += [t(base+190,y,LABELS[name],17,anchor='middle')]
    p += [f'<svg x="{base+105-size/2}" y="{y+26}" width="{size}" height="{size}" viewBox="0 0 24 24">{historical_g(name)}</svg>',icon(name,base+275-size/2,y+26,size)]
    p += [t(base+105,y+91,'前',11,MUTED,'middle'),t(base+275,y+91,'後',11,MUTED,'middle')]
    factor,dx,dy=BALANCE.get(name,(1,0,0))
    caption=f'{size}px枠 / 形の倍率 {factor:.2f}'
    if dy:caption+=' / 重心を微調整'
    p += [t(base+190,y+119,caption,11,MUTED,'middle')]
p += [t(50,799,'頭と肩の比率・端末の縦横比は維持。丸や角を増やさず、形全体だけを穏やかに拡縮。',13,MUTED)]
(ROOT/'balance-review.svg').write_text(svg(1200,830,p,'全12アイコンの調整前後実寸比較'))

# A synthetic business-centered diagram, identical nodes and relations in both rows.
p=[t(50,50,'maakbo / balance in context',16,MUTED),t(50,94,'同じ図で、形と関係の釣り合いを見る。',27,weight=500),t(50,128,'人・情報・システム・リポジトリが、中央の業務へつながる一場面。',14,MUTED)]
for row,balanced in enumerate([False,True]):
    offset=175+row*315
    p += [t(50,offset+18,'調整後' if balanced else '調整前',17)]
    nodes=[('user','担当者',250,offset+24),('ellipse','確認する',600,offset+110),('file','確認情報',930,offset+24),('server','申請管理',250,offset+200),('folder-git-2','リポジトリ',930,offset+200)]
    for name,label,cx,cy in [nodes[0],nodes[2],nodes[3],nodes[4]]:
        lx=cx+27 if cx<600 else cx-27
        endx=570 if cx<600 else 630
        p += [f'<path d="M{lx} {cy}L{endx} {offset+110}" fill="none" stroke="#9E988E" stroke-width=".75"/>']
    for name,label,cx,cy in nodes:
        size=SIZES[name];mark=g(name) if balanced else historical_g(name)
        p += [f'<svg x="{cx-size/2}" y="{cy-size/2}" width="{size}" height="{size}" viewBox="0 0 24 24">{mark}</svg>',t(cx,cy+44,label,14,anchor='middle')]
p += [t(50,793,'ノード枠は現行の寸法。関係線0.75px、ラベルは共通。',12,MUTED)]
(ROOT/'balance-context.svg').write_text(svg(1200,825,p,'同じ関係図でのサイズバランス比較'))
for name in ['balance-review','balance-context']:ET.parse(ROOT/f'{name}.svg')
print('12 optically balanced icons and 10 review SVGs generated and parsed.')
