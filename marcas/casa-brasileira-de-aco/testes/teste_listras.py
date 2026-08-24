# -*- coding: utf-8 -*-
"""TESTE — não entra no manual.

Escrever a palavra com as tres listras: os glifos da Jura Light fatiados em
tres faixas horizontais nas cores da marca. Duas variantes:

  justo   as tres faixas encostadas — a letra fica inteira, so a cor muda
  respiro as tres faixas separadas na proporcao da marca (respiro 0,34 da
          espessura) — a letra fica cortada e voce ve tres listras passando

A proporcao das faixas nao foi escolhida a olho: e a mesma da assinatura.
Tres listras com respiro 0,34 somam 3t + 2(0,34t) = 3,68t. Entao a faixa
vale altura_da_maiuscula / 3,68.
"""
import os
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from kit import (VERDE, AMARELO, AZUL, BRANCO, OSSO, TINTA, CINZA_2, CORES,
                 MONO, TRACK, _F, _UPM, _CMAP, _metricas, largura_tinta, kern)

GS = _F.getGlyphSet()
CAP = 0.72          # altura da maiuscula da Jura, em fracao do corpo
RESP = 0.34         # respiro entre listras, fracao da espessura — regra da marca


def curvas(texto, x, y, S, track=TRACK, kerning=False):
    """Contornos do texto. y = linha de base."""
    k = S / _UPM
    dx = kern(texto, track) if kerning else None
    d, j = [], 0
    for ch in texto:
        if ch == " ":
            x += _metricas(" ")[0] * k + S * track
            continue
        if dx and j:
            x += dx[j] * S
        pen = SVGPathPen(GS)
        GS[_CMAP[ord(ch)]].draw(TransformPen(pen, (k, 0, 0, -k, x, y)))
        c = pen.getCommands()
        if c:
            d.append(c)
        x += _metricas(ch)[0] * k + S * track
        j += 1
    return " ".join(d), x


_uid = [0]


def fatiado(texto, S, track=TRACK, respiro=RESP, cores=CORES, x=0, y=None,
            kerning=False):
    """O texto escrito com as tres listras. Devolve (svg_interno, largura, altura)."""
    y = y if y is not None else S * CAP
    alto = S * CAP
    if respiro:
        t = alto / (3 + 2 * respiro)
        g = t * respiro
    else:
        t = alto / 3
        g = 0.0
    d, xf = curvas(texto, x, y, S, track, kerning)
    _uid[0] += 1
    uid = _uid[0]
    o = "<defs>"
    for i in range(3):
        y0 = y - alto + i * (t + g)
        o += (f'<clipPath id="f{uid}_{i}">'
              f'<rect x="{x-S:.1f}" y="{y0:.2f}" width="{xf-x+2*S:.1f}" '
              f'height="{t:.2f}"/></clipPath>')
    o += "</defs>"
    for i, cor in enumerate(cores):
        o += f'<g clip-path="url(#f{uid}_{i})"><path d="{d}" fill="{cor}"/></g>'
    return o, largura_tinta(texto, S, track), alto


# ------------------------------------------------------------------ prancha
alto_rot = 30

AMOSTRAS = [
    # (rotulo, texto, corpo, entreletra, respiro, cores, fundo)
    ("CASA BRASILEIRA · faixas encostadas",
     "CASA BRASILEIRA", 96, TRACK, 0.0, CORES, OSSO),
    ("CASA BRASILEIRA · respiro 0,34 da espessura (regra da marca)",
     "CASA BRASILEIRA", 96, TRACK, 0.34, CORES, OSSO),
    ("CASA BRASILEIRA · respiro 0,20 — faixa mais cheia",
     "CASA BRASILEIRA", 96, TRACK, 0.20, CORES, OSSO),
    ("CASA BRASILEIRA · respiro 0,34 sobre fundo escuro",
     "CASA BRASILEIRA", 96, TRACK, 0.34, (BRANCO, AMARELO, BRANCO), TINTA),
    ("CBA · faixas encostadas",
     "CBA", 210, TRACK, 0.0, CORES, OSSO),
    ("CBA · respiro 0,34 da espessura (regra da marca)",
     "CBA", 210, TRACK, 0.34, CORES, OSSO),
    ("CBA · respiro 0,34 e entreletra apertada, 0,06",
     "CBA", 210, 0.06, 0.34, CORES, OSSO),
    ("CBA · respiro 0,34 sobre fundo escuro",
     "CBA", 210, TRACK, 0.34, (BRANCO, AMARELO, BRANCO), TINTA),
]

W = 1180
PAD = 44
pecas, y = [], 0
for rot, texto, S, track, respiro, cores, bg in AMOSTRAS:
    alto = S * CAP
    h = alto + PAD * 2 + alto_rot
    inner, lar, _ = fatiado(texto, S, track, respiro, cores,
                            x=PAD, y=y + alto_rot + PAD + alto)
    pecas.append(
        f'<rect x="0" y="{y}" width="{W}" height="{h:.1f}" fill="{bg}"/>'
        f'<text x="{PAD}" y="{y+22}" font-family="{MONO}" font-size="12" '
        f'fill="{CINZA_2 if bg != TINTA else "#8b8e95"}" letter-spacing="1.4">'
        f'{rot}</text>' + inner)
    y += h + 10

H = y
svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H:.0f}" '
       f'viewBox="0 0 {W} {H:.0f}">'
       f'<rect width="{W}" height="{H:.0f}" fill="#d8d6d0"/>{"".join(pecas)}</svg>')

os.makedirs("testes", exist_ok=True)
open("testes/teste_listras.svg", "w", encoding="utf-8").write(svg)
import cairosvg
cairosvg.svg2png(url="testes/teste_listras.svg",
                 write_to="testes/teste_listras.png", scale=2)
print("prancha:", W, "x", round(H), "·", len(AMOSTRAS), "amostras")
