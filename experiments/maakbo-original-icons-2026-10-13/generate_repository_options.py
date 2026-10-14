from pathlib import Path
from xml.etree import ElementTree as E
ROOT=Path(__file__).resolve().parent
INK='#25231F'; MUTED='#726D65'; FONT="'Noto Sans CJK JP',sans-serif"
# Original geometry: edges terminate at circle boundaries, no white fill masks.
GLYPHS={
'linear':'<path d="M6.9 12h2.2m5.8 0h2.2"/><circle cx="4" cy="12" r="2.9"/><circle cx="12" cy="12" r="2.9"/><circle cx="20" cy="12" r="2.9"/>',
'branch':'<path d="M7 9.9v5.2m0-2.2c0-3 10-1.2 10-3"/><circle cx="7" cy="7" r="2.9"/><circle cx="7" cy="18" r="2.9"/><circle cx="17" cy="7" r="2.9"/>',
}
E.register_namespace('', 'http://www.w3.org/2000/svg')
current=E.parse(ROOT/'revision-history/before-repository-adoption/folder-git-2.svg').getroot()
CURRENT=E.tostring(current.find('{http://www.w3.org/2000/svg}g'),encoding='unicode')
def g(name):return f'<g fill="none" stroke="currentColor" stroke-width="1.15" stroke-linecap="round" stroke-linejoin="round">{GLYPHS[name]}</g>'
def icon(mark,x,y,size):return f'<svg x="{x}" y="{y}" width="{size}" height="{size}" viewBox="0 0 24 24">{mark}</svg>'
def t(x,y,s,size=14,color=INK,anchor='start'):return f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" fill="{color}" text-anchor="{anchor}">{s}</text>'
folder=ROOT/'candidate-repository';folder.mkdir(exist_ok=True)
for name in GLYPHS:
    (folder/f'{name if name=='linear' else 'branch-original'}.svg').write_text(f'<!-- Original maakbo repository exploration; not adopted. -->\n<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" style="color:{INK}"><title>リポジトリ</title>{g(name)}</svg>\n')
p=[t(50,50,'maakbo / repository exploration',16,MUTED),t(50,95,'フォルダから、丸と線の記号へ。',29),t(50,130,'リポジトリの比較候補 · 線幅1.15 / 透明背景 / 実寸32px',14,MUTED)]
for x,title,shape,desc in [(190,'現行 · フォルダ',CURRENT,'置き場所としての意味が強い'),(570,'候補1 · 直線の履歴',g('linear'),'3つの丸を、まっすぐつなぐ'),(950,'候補2 · 枝分かれ',g('branch'),'履歴と分岐を、丸と線で表す')]:
    p += [t(x,190,title,19,anchor='middle'),icon(shape,x-48,225,96),t(x,360,'リポジトリ',17,anchor='middle'),t(x,393,desc,13,MUTED,'middle'),icon(shape,x-16,445,32),t(x,515,'実寸32px',12,MUTED,'middle')]
p += [t(50,577,'推奨は候補2。分岐が「履歴を持つリポジトリ」の手がかりになる。',15),t(50,610,'直線は手順や関係図にも見えるため、どちらも下ラベルとセットで使う。',14,MUTED)]
(ROOT/'repo-refinement.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" width="1140" height="650" viewBox="0 0 1140 650" style="color:'+INK+'"><title>リポジトリの丸と線の比較</title><rect width="1140" height="650" fill="white"/>'+''.join(p)+'</svg>')
for name in ['linear','branch-original']:E.parse(folder/f'{name}.svg')
E.parse(ROOT/'repo-refinement.svg')
print('2 original repository candidates and comparison SVG generated and parsed.')
