# -*- coding: utf-8 -*-
"""Qual dos dois caminhos sobrevive pequeno.

A marca vive em etiqueta térmica de galpão, não em apresentação. Então o
critério que decide não é qual fica mais bonito grande — é qual ainda se lê
em corpo 15 px, que é o mínimo que o manual já estabelece.

Mede o elemento mais fino de cada caminho e renderiza a escada.
"""
import os
from fontTools.pens.boundsPen import BoundsPen
from kit import (VERDE, AMARELO, AZUL, BRANCO, OSSO, TINTA, CINZA_2, CORES,
                 MONO, TRACK)
from teste_listras2 import fatiada, vazada, cap_altura, tinta, fonte, contorno

RESP = 0.34


def traco_fino(arq, ch="I"):
    """Espessura do traco vertical da fonte, em fracao do em. Mede o I."""
    _, gs, upm, cmap, _, _, _ = fonte(arq)
    bp = BoundsPen(gs)
    gs[cmap[ord(ch)]].draw(bp)
    return (bp.bounds[2] - bp.bounds[0]) / upm if bp.bounds else 0


CAND = [
    ("A · fatiada", "Outfit-Bold.ttf", "Outfit Bold"),
    ("A · fatiada", "BigShoulders-Bold.ttf", "Big Shoulders Bold"),
    ("B · vazada", "Jura-Light.ttf", "Jura Light — a da marca"),
    ("B · vazada", "Outfit-Bold.ttf", "Outfit Bold"),
]

print("elemento mais fino de cada caminho, em fracao do corpo\n")
print(f"{'caminho':14} {'fonte':26} {'traço':>8} {'faixa':>8} {'respiro':>8}  "
      f"{'morre em':>10}")
print("-" * 84)
LIMITE = {}
for via, arq, nome in CAND:
    cap = cap_altura(arq, "CASA BRASILEIRA")
    t = cap / (3 + 2 * RESP)
    g = t * RESP
    tr = traco_fino(arq)
    # na fatiada o que fecha primeiro e o respiro entre faixas. Na vazada
    # tem de sobreviver o respiro E o traco da letra recortada: vale o menor.
    critico = g if via.startswith("A") else min(g, tr)
    morre = 1.0 / critico          # corpo em que o elemento critico vale 1 px
    LIMITE[(via, arq)] = morre
    print(f"{via:14} {nome:26} {tr:8.4f} {t:8.4f} {g:8.4f}  {morre:9.0f} px")

print("\n'morre em' = corpo em que o elemento mais fino chega a 1 px.")
print("O manual estabelece mínimo de 15 px de corpo em tela.\n")

# ----------------------------------------------------------------- a escada
W, PAD, ROT = 1280, 46, 34
TAM = [96, 48, 30, 20, 15, 11]
pecas, y = [], 0


def secao(t, sub=""):
    global y
    h = 62 if sub else 46
    pecas.append(
        f'<rect x="0" y="{y}" width="{W}" height="{h}" fill="{TINTA}"/>'
        f'<text x="{PAD}" y="{y+28}" font-family="{MONO}" font-size="13" '
        f'fill="{AMARELO}" letter-spacing="3">{t}</text>'
        + (f'<text x="{PAD}" y="{y+50}" font-family="{MONO}" font-size="11" '
           f'fill="#8b8e95" letter-spacing="1">{sub}</text>' if sub else ""))
    y += h + 8


for via, arq, nome in CAND:
    secao(f"{via.upper()} · {nome.upper()}",
          f"o elemento crítico chega a 1 px em corpo {LIMITE[(via,arq)]:.0f}")
    alto_max = cap_altura(arq, "CASA BRASILEIRA") * TAM[0]
    h = alto_max * 1.9 + PAD * 2 + ROT
    pecas.append(f'<rect x="0" y="{y}" width="{W}" height="{h:.1f}" fill="{OSSO}"/>')
    x = PAD
    for S in TAM:
        a = cap_altura(arq, "CASA BRASILEIRA") * S
        base = y + ROT + PAD + alto_max
        if via.startswith("A"):
            inner, _ = fatiada(arq, "CASA BRASILEIRA", S, TRACK, RESP, CORES, x, base)
            lar = tinta(arq, "CASA BRASILEIRA", S, TRACK)
        else:
            pb = a * 0.42
            inner, _, _, bw, _ = vazada(arq, "CASA BRASILEIRA", S, TRACK, RESP,
                                        CORES, x + pb, base, fundo=OSSO)
            lar = bw
        pecas.append(inner)
        pecas.append(f'<text x="{x}" y="{base+26:.0f}" font-family="{MONO}" '
                     f'font-size="10" fill="{CINZA_2}">{S} px</text>')
        x += lar + 26
    y += h + 8

H = y
svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H:.0f}" '
       f'viewBox="0 0 {W} {H:.0f}">'
       f'<rect width="{W}" height="{H:.0f}" fill="#c9c7c1"/>{"".join(pecas)}</svg>')
os.makedirs("testes", exist_ok=True)
open("testes/teste_escala.svg", "w", encoding="utf-8").write(svg)
import cairosvg
cairosvg.svg2png(url="testes/teste_escala.svg",
                 write_to="testes/teste_escala.png", scale=2)
print("escada:", W, "x", round(H))
