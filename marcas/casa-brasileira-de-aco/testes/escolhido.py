# -*- coding: utf-8 -*-
"""O escolhido: A · letra fatiada, Outfit Bold.

Exporta cada lockup em arquivo próprio — vetor e PNG de 8000 px na maior
dimensão, o mesmo padrão do pacote da marca.

Ainda é teste. Não entrou no brandbook.
"""
import os, re
from kit import (VERDE, AMARELO, AZUL, BRANCO, OSSO, TINTA, CORES)
from teste_listras2 import fatiada, cap_altura, tinta

ARQ = "Outfit-Bold.ttf"
TRACK = 0.155
RESP = 0.34
ALTA = 8000

REV = (BRANCO, AMARELO, BRANCO)      # regra de fundo escuro que a marca já tem

LOCKUPS = [
    ("CASA-BRASILEIRA-fatiada-cor",        "CASA BRASILEIRA", None,   CORES),
    ("CASA-BRASILEIRA-fatiada-papel",      "CASA BRASILEIRA", OSSO,   CORES),
    ("CASA-BRASILEIRA-fatiada-branco",     "CASA BRASILEIRA", BRANCO, CORES),
    ("CASA-BRASILEIRA-fatiada-escuro",     "CASA BRASILEIRA", TINTA,  REV),
    ("CASA-BRASILEIRA-fatiada-azul",       "CASA BRASILEIRA", AZUL,   REV),
    ("CBA-fatiada-cor",                    "CBA", None,   CORES),
    ("CBA-fatiada-papel",                  "CBA", OSSO,   CORES),
    ("CBA-fatiada-branco",                 "CBA", BRANCO, CORES),
    ("CBA-fatiada-escuro",                 "CBA", TINTA,  REV),
    ("CBA-fatiada-azul",                   "CBA", AZUL,   REV),
]

S = 200
OUT = "testes/escolhido"
os.makedirs(f"{OUT}/svg", exist_ok=True)
os.makedirs(f"{OUT}/png-alta", exist_ok=True)

import cairosvg
for nome, texto, bg, cores in LOCKUPS:
    alto = cap_altura(ARQ, texto) * S
    lar = tinta(ARQ, texto, S, TRACK)
    pad = alto * 0.40                       # respiro na proporção da marca
    W, H = round(lar + 2 * pad), round(alto + 2 * pad)
    inner, _ = fatiada(ARQ, texto, S, TRACK, RESP, cores, pad, pad + alto)
    fundo = f'<rect width="{W}" height="{H}" fill="{bg}"/>' if bg else ""
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
           f'viewBox="0 0 {W} {H}">{fundo}{inner}</svg>')
    open(f"{OUT}/svg/{nome}.svg", "w", encoding="utf-8").write(svg)
    cairosvg.svg2png(url=f"{OUT}/svg/{nome}.svg",
                     write_to=f"{OUT}/png-alta/{nome}.png",
                     scale=ALTA / max(W, H))
    print(f"{nome:36} viewBox {W}x{H}")

print(f"\n{len(LOCKUPS)} lockups · svg vetor + png {ALTA} px na maior dimensão")
