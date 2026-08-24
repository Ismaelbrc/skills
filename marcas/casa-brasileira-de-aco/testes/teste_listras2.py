# -*- coding: utf-8 -*-
"""TESTE 2 — não entra no manual.

A primeira rodada mostrou que fatiar a Jura Light não funciona: o traço é
fino, e fio dividido em três dá três fios, não três listras. Duas saídas:

  A · FATIADA    a letra precisa de corpo. Testando pesos mais cheios.
  B · VAZADA     as três listras formam um bloco e a palavra é recortada
                 delas. Funciona em qualquer peso, inclusive na Jura Light
                 da marca — porque quem carrega a cor é a listra, não a letra.
"""
import os
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen
from kit import (VERDE, AMARELO, AZUL, BRANCO, OSSO, TINTA, CINZA_2, CORES,
                 MONO, TRACK)

FDIR = "/root/.fonts"
RESP = 0.34
_cache, _uid = {}, [0]


def fonte(arq):
    if arq not in _cache:
        f = TTFont(os.path.join(FDIR, arq))
        _cache[arq] = (f, f.getGlyphSet(), f["head"].unitsPerEm,
                       f.getBestCmap(), f["hmtx"], f["glyf"],
                       f["OS/2"].sCapHeight if "OS/2" in f and
                       getattr(f["OS/2"], "sCapHeight", 0) else None)
    return _cache[arq]


def met(arq, ch):
    _, _, upm, cmap, hmtx, glyf, _ = fonte(arq)
    g = cmap[ord(ch)]
    adv, lsb = hmtx[g]
    gl = glyf[g]
    return adv, lsb, (gl.xMax if gl.numberOfContours else adv), \
        (gl.yMax if gl.numberOfContours else 0)


def cap_altura(arq, texto):
    """Altura da maiuscula medida no contorno, nao na tabela do glifo.
    Fonte variavel mente no yMax; o desenho nao."""
    _, gs, upm, cmap, _, _, _ = fonte(arq)
    topo = 0
    for ch in texto:
        if ch == " ":
            continue
        bp = BoundsPen(gs)
        gs[cmap[ord(ch)]].draw(bp)
        if bp.bounds:
            topo = max(topo, bp.bounds[3])
    return topo / upm


def contorno(arq, texto, x, y, S, track):
    _, gs, upm, cmap, _, _, _ = fonte(arq)
    k = S / upm
    d = []
    for ch in texto:
        if ch == " ":
            x += met(arq, " ")[0] * k + S * track
            continue
        pen = SVGPathPen(gs)
        gs[cmap[ord(ch)]].draw(TransformPen(pen, (k, 0, 0, -k, x, y)))
        c = pen.getCommands()
        if c:
            d.append(c)
        x += met(arq, ch)[0] * k + S * track
    return " ".join(d), x


def tinta(arq, texto, S, track):
    k = S / fonte(arq)[2]
    soma = sum(met(arq, c)[0] for c in texto) * k + S * track * (len(texto) - 1)
    return soma - met(arq, texto[0])[1] * k - \
        (met(arq, texto[-1])[0] - met(arq, texto[-1])[2]) * k


# ------------------------------------------------------------- A · fatiada
def fatiada(arq, texto, S, track, respiro, cores, x, base):
    alto = cap_altura(arq, texto) * S
    t = alto / (3 + 2 * respiro) if respiro else alto / 3
    g = t * respiro
    d, xf = contorno(arq, texto, x, base, S, track)
    _uid[0] += 1
    u = _uid[0]
    o = "<defs>"
    for i in range(3):
        o += (f'<clipPath id="a{u}_{i}"><rect x="{x-S:.1f}" '
              f'y="{base-alto+i*(t+g):.2f}" width="{xf-x+2*S:.1f}" '
              f'height="{t:.2f}"/></clipPath>')
    o += "</defs>"
    for i, c in enumerate(cores):
        o += f'<g clip-path="url(#a{u}_{i})"><path d="{d}" fill="{c}"/></g>'
    return o, alto


# -------------------------------------------------------------- B · vazada
def vazada(arq, texto, S, track, respiro, cores, x, base, folga=0.42,
           fundo=OSSO):
    """As tres listras formam o bloco; a palavra e recortada delas."""
    alto = cap_altura(arq, texto) * S
    t = alto / (3 + 2 * respiro) if respiro else alto / 3
    g = t * respiro
    lar = tinta(arq, texto, S, track)
    d, _ = contorno(arq, texto, x, base, S, track)
    pad = alto * folga
    bx, bw = x - pad, lar + 2 * pad
    o = ""
    for i, c in enumerate(cores):
        o += (f'<rect x="{bx:.1f}" y="{base-alto+i*(t+g):.2f}" '
              f'width="{bw:.1f}" height="{t:.2f}" fill="{c}"/>')
    # a palavra recortada: sobreimpressao na cor do fundo. Mask seria mais
    # elegante, mas o cairosvg nao honra, e teste que nao renderiza nao serve.
    o += f'<path d="{d}" fill="{fundo}"/>'
    return o, alto, bx, bw, pad


# ------------------------------------------------------------------ prancha
FONTES = [("Jura-Light.ttf", "Jura Light — a da marca"),
          ("Jura-Medium.ttf", "Jura Medium"),
          ("Outfit-Bold.ttf", "Outfit Bold"),
          ("BigShoulders-Bold.ttf", "Big Shoulders Bold")]

W, PAD, ROT = 1240, 46, 30
pecas, y = [], 0


def faixa(rot, h, bg):
    global y
    cor_rot = "#8b8e95" if bg == TINTA else CINZA_2
    pecas.append(f'<rect x="0" y="{y}" width="{W}" height="{h:.1f}" fill="{bg}"/>'
                 f'<text x="{PAD}" y="{y+21}" font-family="{MONO}" font-size="12" '
                 f'fill="{cor_rot}" letter-spacing="1.4">{rot}</text>')


def secao(titulo):
    global y
    pecas.append(f'<rect x="0" y="{y}" width="{W}" height="46" fill="{TINTA}"/>'
                 f'<text x="{PAD}" y="{y+29}" font-family="{MONO}" font-size="14" '
                 f'fill="{AMARELO}" letter-spacing="3">{titulo}</text>')
    y += 46 + 8


# ---- A: fatiada, quatro pesos
secao("A · LETRA FATIADA — CASA BRASILEIRA, RESPIRO 0,34")
for arq, nome in FONTES:
    S = 92
    alto = cap_altura(arq, "CASA BRASILEIRA") * S
    h = alto + PAD * 2 + ROT
    faixa(nome, h, OSSO)
    inner, _ = fatiada(arq, "CASA BRASILEIRA", S, TRACK, RESP, CORES,
                       PAD, y + ROT + PAD + alto)
    pecas.append(inner)
    y += h + 8

secao("A · LETRA FATIADA — CBA, RESPIRO 0,34")
for arq, nome in FONTES:
    S = 190
    alto = cap_altura(arq, "CBA") * S
    h = alto + PAD * 2 + ROT
    faixa(nome, h, OSSO)
    inner, _ = fatiada(arq, "CBA", S, TRACK, RESP, CORES,
                       PAD, y + ROT + PAD + alto)
    pecas.append(inner)
    y += h + 8

# ---- B: vazada
secao("B · LETRA VAZADA NAS LISTRAS — FUNCIONA NA JURA LIGHT DA MARCA")
for arq, nome in FONTES[:3]:
    for texto, S in (("CASA BRASILEIRA", 82), ("CBA", 150)):
        alto = cap_altura(arq, texto) * S
        pad_b = alto * 0.42
        h = alto + 2 * pad_b + PAD * 1.4 + ROT
        faixa(f"{nome} · {texto}", h, OSSO)
        inner, _, _, _, _ = vazada(arq, texto, S, TRACK, RESP, CORES,
                                   PAD + pad_b, y + ROT + PAD * 0.7 + pad_b + alto)
        pecas.append(inner)
        y += h + 8

H = y
svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H:.0f}" '
       f'viewBox="0 0 {W} {H:.0f}">'
       f'<rect width="{W}" height="{H:.0f}" fill="#c9c7c1"/>{"".join(pecas)}</svg>')

os.makedirs("testes", exist_ok=True)
open("testes/teste_listras2.svg", "w", encoding="utf-8").write(svg)
import cairosvg
cairosvg.svg2png(url="testes/teste_listras2.svg",
                 write_to="testes/teste_listras2.png", scale=2)
print("prancha 2:", W, "x", round(H))
