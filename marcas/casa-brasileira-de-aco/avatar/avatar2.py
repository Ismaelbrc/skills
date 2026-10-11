# -*- coding: utf-8 -*-
"""Segunda rodada: resolver o conflito entre "verde e amarela" e funcionar.

A primeira rodada mostrou que:
  · circulo claro some contra a interface clara do WhatsApp
  · sobre preto o azul e o verde da listra morrem (ja era regra medida)
  · o azul institucional funciona nos dois temas, mas nao tem verde

Entao testa o que a primeira rodada nao tinha: o circulo na cor da marca.
Verde #006B3C e a cor que assina. Com listra branco/amarelo/branco vira um
avatar verde e amarelo que separa de fundo claro e de fundo escuro.
"""
import os

import cairosvg
from PIL import Image, ImageDraw

VERDE, AMARELO, AZUL = "#006B3C", "#F2B705", "#002B5C"
BRANCO, OSSO, TINTA = "#FFFFFF", "#F5F4F0", "#14161C"
CORES = (VERDE, AMARELO, AZUL)
REV = (BRANCO, AMARELO, BRANCO)

SAIDA = "/tmp/claude-0/-home-user-skills/9b00c726-1271-5e08-a488-cbad7d5f439a/scratchpad/avatar"
os.makedirs(f"{SAIDA}/svg", exist_ok=True)


def listras(L, cores, comp_f=0.64, esp_f=0.28, resp_f=0.34):
    comp = L * comp_f
    alt = comp / 2.0
    t = alt * esp_f
    g = t * resp_f
    k = alt / (3 * t + 2 * g)
    t, g = t * k, g * k
    y = (L - (3 * t + 2 * g)) / 2
    x = (L - comp) / 2
    return "".join(
        f'<rect x="{x:.2f}" y="{y + i*(t+g):.2f}" width="{comp:.2f}" '
        f'height="{t:.2f}" fill="{c}"/>' for i, c in enumerate(cores))


def avatar(L, fundo, cores, aro=None, aro_f=0.030, comp_f=0.64):
    o = f'<circle cx="{L/2}" cy="{L/2}" r="{L/2}" fill="{fundo}"/>'
    if aro:
        lar = L * aro_f
        r = L / 2 - lar / 2
        o += (f'<circle cx="{L/2}" cy="{L/2}" r="{r:.1f}" fill="none" '
              f'stroke="{aro}" stroke-width="{lar:.1f}"/>')
    o += listras(L, cores, comp_f)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{L}" height="{L}" '
            f'viewBox="0 0 {L} {L}">{o}</svg>')


L = 1000
OPCOES = [
    ("A-verde",      "círculo VERDE + listra branco/amarelo/branco",
     avatar(L, VERDE, REV)),
    ("B-verde-cor",  "círculo verde + listra amarelo/branco/amarelo",
     avatar(L, VERDE, (AMARELO, BRANCO, AMARELO))),
    ("C-papel-aro",  "papel + aro verde grosso + as 3 cores",
     avatar(L, OSSO, CORES, aro=VERDE, aro_f=0.034)),
    ("D-azul",       "azul institucional + branco/amarelo/branco",
     avatar(L, AZUL, REV)),
    ("E-tinta",      "preto + branco/amarelo/branco",
     avatar(L, TINTA, REV)),
    ("F-verde-maior", "círculo verde, listra maior (0,74)",
     avatar(L, VERDE, REV, comp_f=0.74)),
]

for nome, _, svg in OPCOES:
    open(f"{SAIDA}/svg/{nome}.svg", "w", encoding="utf-8").write(svg)
    cairosvg.svg2png(url=f"{SAIDA}/svg/{nome}.svg",
                     write_to=f"{SAIDA}/{nome}.png", scale=1.0)

# ------------------------------------------------- a prova no tamanho real
UI = (("interface clara", "#FFFFFF"), ("interface escura", "#0B141A"))
TAMANHOS = [48, 56, 96, 200]
CEL_W = 420
linha_h = 230

prova = Image.new("RGB", (CEL_W * 2, linha_h * len(OPCOES) + 52), "#9a9a9a")
d = ImageDraw.Draw(prova)
for col, (rot, cor) in enumerate(UI):
    d.text((col * CEL_W + 14, 14), rot.upper(), fill="#111")
y = 40
for nome, rot, _ in OPCOES:
    src = Image.open(f"{SAIDA}/{nome}.png").convert("RGBA")
    d.text((8, y + 4), f"{nome} · {rot}", fill="#111")
    for col, (_, ui) in enumerate(UI):
        faixa = Image.new("RGB", (CEL_W, linha_h - 22), ui)
        x = 16
        for S in TAMANHOS:
            mini = src.resize((S, S), Image.LANCZOS)
            masc = Image.new("L", (S, S), 0)
            ImageDraw.Draw(masc).ellipse((0, 0, S - 1, S - 1), fill=255)
            faixa.paste(mini.convert("RGB"), (x, (linha_h - 22 - S) // 2), masc)
            x += S + 16
        prova.paste(faixa, (col * CEL_W, y + 20))
    y += linha_h

prova.save(f"{SAIDA}/_prova2.png")
print(f"{len(OPCOES)} opções · prova em 48, 56, 96 e 200 px nos dois temas")
