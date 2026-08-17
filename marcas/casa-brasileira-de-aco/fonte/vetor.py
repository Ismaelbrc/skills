# -*- coding: utf-8 -*-
"""Exporta a marca com o texto em curvas — independente da fonte instalada."""
import os
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from kit import (VERDE, AMARELO, AZUL, BRANCO, OSSO, TINTA, CORES, JURA, TRACK,
                 largura_tinta, avanco, _F, _UPM, _CMAP, _metricas, listras,
                 listras_bloco)

GS = _F.getGlyphSet()


def curvas(texto, x, y, S, track=TRACK):
    """Retorna (path_d, x_final). y = linha de base."""
    k = S / _UPM
    d = []
    for ch in texto:
        pen = SVGPathPen(GS)
        GS[_CMAP[ord(ch)]].draw(TransformPen(pen, (k, 0, 0, -k, x, y)))
        c = pen.getCommands()
        if c:
            d.append(c)
        x += _metricas(ch)[0] * k + S * track
    return " ".join(d), x


def bloco_nome(x, y, S, c1, c2, track=TRACK):
    """CASA BRASILEIRA em c1 + DE AÇO em c2, em curvas."""
    d1, x2 = curvas("CASA BRASILEIRA ", x, y, S, track)
    d2, xf = curvas("DE AÇO", x2, y, S, track)
    return (f'<path d="{d1}" fill="{c1}"/><path d="{d2}" fill="{c2}"/>'), xf


def marca(S=64, bg=None, c1=TINTA, c2=VERDE, cores=CORES, pad_f=0.9):
    """Composicao principal: listra sob CASA BRASILEIRA, ate a tinta do A."""
    pad = S * pad_f
    base = S * 1.28
    corpo, xf = bloco_nome(pad, base, S, c1, c2)
    lar = largura_tinta("CASA BRASILEIRA", S)
    x0 = pad + _metricas("C")[1] * (S / _UPM)
    lst, _ = listras(x0, base + S * 0.32, lar, S, cores)
    W = round(avanco("CASA BRASILEIRA ", S) + largura_tinta("DE AÇO", S) + 2 * pad)
    H = round(S * 2.40)
    fundo = f'<rect width="{W}" height="{H}" fill="{bg}"/>' if bg else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
            f'viewBox="0 0 {W} {H}">{fundo}{corpo}{lst}</svg>')


def marca_h(S=48, bg=None, c1=TINTA, c2=VERDE, cores=CORES, pad_f=0.9):
    """Alternativa 1 — listras a esquerda, nome em duas linhas."""
    pad = S * pad_f
    alt = S * 1.62
    cy = pad + alt / 2 + S * 0.30
    bl, L = listras_bloco(pad + alt * 1.0, cy, alt, cores)
    tx = pad + alt * 1.0 - L / 2 + L + S * 0.95
    d1, _ = curvas("CASA BRASILEIRA", tx, cy - S * 0.30, S)
    d2, _ = curvas("DE AÇO", tx, cy + S * 0.65, S, track=0.435)
    W = round(tx + largura_tinta("CASA BRASILEIRA", S) + pad)
    H = round(cy + S * 0.95 + pad)
    fundo = f'<rect width="{W}" height="{H}" fill="{bg}"/>' if bg else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
            f'viewBox="0 0 {W} {H}">{fundo}{bl}'
            f'<path d="{d1}" fill="{c1}"/><path d="{d2}" fill="{c2}"/></svg>')


def marca_v(S=48, bg=None, c1=TINTA, c2=VERDE, cores=CORES, pad_f=1.0):
    """Alternativa 2 — listras em cima, nome centralizado."""
    pad = S * pad_f
    alt = S * 1.62
    lar1 = largura_tinta("CASA BRASILEIRA", S)
    lar2 = largura_tinta("DE AÇO", S, track=0.435)
    W = round(lar1 + 2 * pad)
    cx = W / 2
    cy = pad + alt / 2
    bl, _ = listras_bloco(cx, cy, alt, cores)
    b1 = cy + alt * 0.62 + S * 1.05
    b2 = cy + alt * 0.62 + S * 2.00
    d1, _ = curvas("CASA BRASILEIRA", cx - lar1 / 2, b1, S)
    d2, _ = curvas("DE AÇO", cx - lar2 / 2, b2, S, track=0.435)
    H = round(b2 + S * 0.30 + pad)
    fundo = f'<rect width="{W}" height="{H}" fill="{bg}"/>' if bg else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
            f'viewBox="0 0 {W} {H}">{fundo}{bl}'
            f'<path d="{d1}" fill="{c1}"/><path d="{d2}" fill="{c2}"/></svg>')


def marca_l(S=48, bg=None, c1=TINTA, c2=VERDE, cores=CORES, pad_f=0.9):
    """Alternativa 3 — tudo em uma linha."""
    pad = S * pad_f
    alt = S * 1.30
    cy = pad + alt / 2
    bl, L = listras_bloco(pad + alt * 1.0, cy, alt, cores)
    tx = pad + alt * 1.0 - L / 2 + L + S * 0.85
    corpo, xf = bloco_nome(tx, cy + S * 0.33, S, c1, c2)
    W = round(xf - S * TRACK + pad)
    H = round(cy + alt / 2 + pad)
    fundo = f'<rect width="{W}" height="{H}" fill="{bg}"/>' if bg else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
            f'viewBox="0 0 {W} {H}">{fundo}{bl}{corpo}</svg>')


# ------------------------------------------------------------------ export
OUT = "marca"
os.makedirs(OUT, exist_ok=True)

MONO_P = (TINTA, TINTA, TINTA)
MONO_B = (BRANCO, BRANCO, BRANCO)
REV = (BRANCO, AMARELO, BRANCO)

ARQ = [
    ("CBA-principal-cor",        marca(96, None,  TINTA,  VERDE,   CORES)),
    ("CBA-principal-papel",      marca(96, OSSO,  TINTA,  VERDE,   CORES)),
    ("CBA-principal-branco",     marca(96, BRANCO, TINTA, VERDE,   CORES)),
    ("CBA-principal-reversa-azul",  marca(96, AZUL,  BRANCO, AMARELO, REV)),
    ("CBA-principal-reversa-preto", marca(96, TINTA, BRANCO, AMARELO, CORES)),
    ("CBA-principal-mono-preto", marca(96, None,  TINTA,  TINTA,   MONO_P)),
    ("CBA-principal-mono-branco", marca(96, TINTA, BRANCO, BRANCO,  MONO_B)),
    ("CBA-alt1-horizontal",      marca_h(72, None, TINTA, VERDE,   CORES)),
    ("CBA-alt2-vertical",        marca_v(72, None, TINTA, VERDE,   CORES)),
    ("CBA-alt3-uma-linha",       marca_l(72, None, TINTA, VERDE,   CORES)),
]

for nome, svg in ARQ:
    open(os.path.join(OUT, nome + ".svg"), "w", encoding="utf-8").write(svg)
print("svg:", len(ARQ))
