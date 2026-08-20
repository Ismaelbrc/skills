# -*- coding: utf-8 -*-
"""Folha de conferencia: as 35 aplicacoes numa folha so, para bater o olho."""
import glob, os, re

CEL_W, CEL_H = 460, 220
COLS = 7
XADREZ = 14          # quadriculado para enxergar o fundo transparente

arquivos = sorted(glob.glob("marca/CBA-*.svg"))
linhas, i = [], 0
for f in arquivos:
    nome = os.path.basename(f)[:-4]
    s = open(f, encoding="utf-8").read()
    w, h = (int(v) for v in re.search(r'viewBox="0 0 (\d+) (\d+)"', s).groups())
    miolo = s[s.index(">", s.index("<svg")) + 1:s.rindex("</svg>")]
    esc = min((CEL_W - 24) / w, (CEL_H - 46) / h)
    cx, cy = i % COLS, i // COLS
    ox = cx * CEL_W + (CEL_W - w * esc) / 2
    oy = cy * CEL_H + 14
    linhas.append(
        f'<g transform="translate({ox:.1f} {oy:.1f}) scale({esc:.5f})">{miolo}</g>'
        f'<text x="{cx*CEL_W + CEL_W/2:.0f}" y="{cy*CEL_H + CEL_H - 12}" '
        f'font-family="IBM Plex Mono, monospace" font-size="11" fill="#5A5C60" '
        f'text-anchor="middle">{nome}</text>'
        f'<rect x="{cx*CEL_W+8}" y="{cy*CEL_H+8}" width="{CEL_W-16}" '
        f'height="{CEL_H-34}" fill="none" stroke="#c9c7c0" stroke-width="1"/>')
    i += 1

W = COLS * CEL_W
H = ((len(arquivos) + COLS - 1) // COLS) * CEL_H + 78
cab = (f'<text x="24" y="34" font-family="IBM Plex Mono, monospace" font-size="17" '
       f'fill="#14161C" letter-spacing="2">CASA BRASILEIRA DE AÇO · FOLHA DE '
       f'CONFERÊNCIA · {len(arquivos)} ARQUIVOS</text>'
       f'<text x="24" y="56" font-family="IBM Plex Mono, monospace" font-size="11" '
       f'fill="#5A5C60">o quadriculado marca fundo transparente</text>')

svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
       f'viewBox="0 0 {W} {H}">'
       f'<defs><pattern id="x" width="{XADREZ*2}" height="{XADREZ*2}" '
       f'patternUnits="userSpaceOnUse">'
       f'<rect width="{XADREZ*2}" height="{XADREZ*2}" fill="#ffffff"/>'
       f'<rect width="{XADREZ}" height="{XADREZ}" fill="#ebe9e4"/>'
       f'<rect x="{XADREZ}" y="{XADREZ}" width="{XADREZ}" height="{XADREZ}" '
       f'fill="#ebe9e4"/></pattern></defs>'
       f'<rect width="{W}" height="{H}" fill="url(#x)"/>'
       f'<rect width="{W}" height="70" fill="#F5F4F0"/>{cab}'
       f'<g transform="translate(0 74)">{"".join(linhas)}</g></svg>')

open("marca/FOLHA-DE-CONFERENCIA.svg", "w", encoding="utf-8").write(svg)
import cairosvg
cairosvg.svg2png(url="marca/FOLHA-DE-CONFERENCIA.svg",
                 write_to="marca/FOLHA-DE-CONFERENCIA.png", scale=2)
cairosvg.svg2pdf(url="marca/FOLHA-DE-CONFERENCIA.svg",
                 write_to="marca/FOLHA-DE-CONFERENCIA.pdf")
print("folha:", W, "x", H, "·", len(arquivos), "arquivos")
