from pathlib import Path
from xml.etree import ElementTree as E
from math import hypot
ROOT=Path(__file__).resolve().parent
INK='#25231F';MUTED='#726D65';FONT="'Noto Sans CJK JP',sans-serif";RADIUS=2.3
E.register_namespace('', 'http://www.w3.org/2000/svg')
POINTS={'top-down':[(8,4.8),(8,18.5),(17,14)],'left-right':[(4.8,12),(18.5,12),(14.5,5.5)]}
def boundary_edge(a,b):
    dx,dy=b[0]-a[0],b[1]-a[1];length=hypot(dx,dy)
    start=(a[0]+RADIUS*dx/length,a[1]+RADIUS*dy/length)
    end=(b[0]-RADIUS*dx/length,b[1]-RADIUS*dy/length)
    assert abs(hypot(start[0]-a[0],start[1]-a[1])-RADIUS)<1e-10
    assert abs(hypot(end[0]-b[0],end[1]-b[1])-RADIUS)<1e-10
    return f'M{start[0]:.5f} {start[1]:.5f}L{end[0]:.5f} {end[1]:.5f}'
def g(name):
    points=POINTS[name]
    paths=''.join(boundary_edge(points[0],c) for c in points[1:])
    circles=''.join(f'<circle cx="{x}" cy="{y}" r="{RADIUS}"/>' for x,y in points)
    return f'<g fill="none" stroke="currentColor" stroke-width="1.15" stroke-linecap="round" stroke-linejoin="round"><path d="{paths}"/>{circles}</g>'
def t(x,y,s,size=14,color=INK,anchor='start'):return f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" fill="{color}" text-anchor="{anchor}">{s}</text>'
def icon(mark,x,y,size):return f'<svg x="{x}" y="{y}" width="{size}" height="{size}" viewBox="0 0 24 24">{mark}</svg>'
for name,points in POINTS.items():
    axis=1 if name=='top-down' else 0
    assert all(c[axis]>points[0][axis] for c in points[1:])
    assert points[1][axis]!=points[2][axis]
folder=ROOT/'candidate-repository'
for name in POINTS:
    (folder/f'{name}.svg').write_text(f'<!-- Original maakbo timeline exploration; direction not selected. -->\n<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" style="color:{INK}"><title>リポジトリ</title>{g(name)}</svg>\n')
old=E.parse(ROOT/'revision-history/before-topdown-adoption/folder-git-2.svg').getroot()
oldgroup=E.tostring(old.find('{http://www.w3.org/2000/svg}g'),encoding='unicode')
p=[t(50,50,'maakbo / repository timeline exploration',16,MUTED),t(50,95,'先の1点から、後の2点へ。',29),t(50,132,'時間の向きを揃え、後続の2点は同じ位置に揃えない。',14,MUTED)]
for x,mark,title,direction in [(190,oldgroup,'現行 · 下から上','時間の読み方が曖昧'),(570,g('top-down'),'候補A · 上から下','先の点が上。後続2点は別の高さ'),(950,g('left-right'),'候補B · 左から右','先の点が左。後続2点は別の横位置')]:
    p += [t(x,196,title,20,anchor='middle'),icon(mark,x-54,237,108),t(x,382,'リポジトリ',17,anchor='middle'),t(x,416,direction,13,MUTED,'middle'),icon(mark,x-16,466,32),t(x,536,'実寸32px',12,MUTED,'middle')]
p += [t(50,602,'祖先の丸から2つの後続へ直線でつなぐ。幹の途中に見えない分岐点を置かない。',14,MUTED),t(50,638,'時間順を助ける概略記号。実際のGitコミット時刻や間隔を表す図ではない。',14,MUTED)]
(ROOT/'repo-timeline-options.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="1140" height="680" viewBox="0 0 1140 680" style="color:{INK}"><title>リポジトリの時間方向比較</title><rect width="1140" height="680" fill="white"/>'+''.join(p)+'</svg>')
for name in POINTS:E.parse(folder/f'{name}.svg')
E.parse(ROOT/'repo-timeline-options.svg')
print('Two timeline candidates: SVG parse, circle-edge contacts and monotonic time-axis checks passed.')
