# -*- coding: utf-8 -*-
"""Avatar redondo para o WhatsApp.

O que decide um avatar nao e como ele fica grande na tela de perfil. E como
ele fica com 48 px na lista de conversas, que e onde a pessoa realmente ve.
Entao: monta as opcoes, renderiza no tamanho real contra a interface clara e
a escura do WhatsApp, e deixa a evidencia escolher.

A geometria da listra nao muda: espessura e respiro saem do mesmo bloco das
alternativas 1, 2 e 3 — respiro 0,34 da espessura.
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
    """O mesmo bloco solto das alternativas: tres listras com respiro 0,34."""
    comp = L * comp_f
    alt = comp / 2.0                       # comprimento = 2,0 x a altura
    t = alt * esp_f
    g = t * resp_f
    k = alt / (3 * t + 2 * g)               # normaliza para a altura pedida
    t, g = t * k, g * k
    y = (L - (3 * t + 2 * g)) / 2
    x = (L - comp) / 2
    o = ""
    for i, c in enumerate(cores):
        o += (f'<rect x="{x:.2f}" y="{y + i*(t+g):.2f}" width="{comp:.2f}" '
              f'height="{t:.2f}" fill="{c}"/>')
    return o


def avatar(L, fundo, cores, aro=None, comp_f=0.64):
    """Circulo de bordo a bordo: o WhatsApp recorta em circulo de qualquer jeito."""
    o = f'<circle cx="{L/2}" cy="{L/2}" r="{L/2}" fill="{fundo}"/>'
    if aro:
        r = L / 2 - L * 0.012
        o += (f'<circle cx="{L/2}" cy="{L/2}" r="{r:.1f}" fill="none" '
              f'stroke="{aro}" stroke-width="{L*0.016:.1f}"/>')
    o += listras(L, cores, comp_f)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{L}" height="{L}" '
            f'viewBox="0 0 {L} {L}">{o}</svg>')


# a opcao que leva o nome junto, so para provar que nao serve
def avatar_com_nome(L, fundo, cores, cor_nome):
    comp = L * 0.62
    alt = comp / 2.0
    t = alt * 0.28
    g = t * 0.34
    k = alt / (3 * t + 2 * g)
    t, g = t * k, g * k
    bloco = 3 * t + 2 * g
    y = L * 0.30
    x = (L - comp) / 2
    o = f'<circle cx="{L/2}" cy="{L/2}" r="{L/2}" fill="{fundo}"/>'
    for i, c in enumerate(cores):
        o += (f'<rect x="{x:.2f}" y="{y + i*(t+g):.2f}" width="{comp:.2f}" '
              f'height="{t:.2f}" fill="{c}"/>')
    S = L * 0.072
    o += (f'<text x="{L/2}" y="{y + bloco + L*0.13:.1f}" text-anchor="middle" '
          f'font-family="sans-serif" font-size="{S:.1f}" fill="{cor_nome}" '
          f'letter-spacing="{S*0.14:.2f}">CASA BRASILEIRA</text>')
    o += (f'<text x="{L/2}" y="{y + bloco + L*0.225:.1f}" text-anchor="middle" '
          f'font-family="sans-serif" font-size="{S:.1f}" fill="{VERDE}" '
          f'letter-spacing="{S*0.14:.2f}">DE AÇO</text>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{L}" height="{L}" '
            f'viewBox="0 0 {L} {L}">{o}</svg>')


L = 1000
OPCOES = [
    ("01-papel",        "listras sobre papel",            avatar(L, OSSO, CORES)),
    ("02-branco",       "listras sobre branco",           avatar(L, BRANCO, CORES)),
    ("03-papel-aro",    "papel com aro verde",            avatar(L, OSSO, CORES, aro=VERDE)),
    ("04-tinta",        "sobre preto, regra de fundo escuro", avatar(L, TINTA, REV)),
    ("05-tinta-cor",    "sobre preto, mantendo as 3 cores",   avatar(L, TINTA, CORES)),
    ("06-azul",         "sobre azul institucional",       avatar(L, AZUL, REV)),
    ("07-papel-grande", "papel, listra maior (0,74)",     avatar(L, OSSO, CORES, comp_f=0.74)),
    ("08-com-nome",     "com o nome — para provar que não serve",
     avatar_com_nome(L, OSSO, CORES, TINTA)),
]

for nome, _, svg in OPCOES:
    open(f"{SAIDA}/svg/{nome}.svg", "w", encoding="utf-8").write(svg)
    cairosvg.svg2png(url=f"{SAIDA}/svg/{nome}.svg",
                     write_to=f"{SAIDA}/{nome}.png", scale=1.0)

print(f"{len(OPCOES)} opções em {L}x{L}")

# ------------------------------------------------- a prova no tamanho real
UI_CLARA, UI_ESCURA = "#FFFFFF", "#0B141A"     # fundos reais do WhatsApp
TAMANHOS = [48, 56, 96, 200]
CEL_W = 260
linha_h = 150

prova = Image.new("RGB", (CEL_W * 2, linha_h * len(OPCOES) + 40), "#9a9a9a")
d = ImageDraw.Draw(prova)
y = 30
for nome, rot, _ in OPCOES:
    src = Image.open(f"{SAIDA}/{nome}.png").convert("RGBA")
    for col, ui in enumerate((UI_CLARA, UI_ESCURA)):
        faixa = Image.new("RGB", (CEL_W, linha_h), ui)
        x = 14
        for S in TAMANHOS:
            mini = src.resize((S, S), Image.LANCZOS)
            # recorte circular, como o WhatsApp faz
            masc = Image.new("L", (S, S), 0)
            ImageDraw.Draw(masc).ellipse((0, 0, S - 1, S - 1), fill=255)
            faixa.paste(mini.convert("RGB"), (x, (linha_h - S) // 2), masc)
            x += S + 12
        prova.paste(faixa, (col * CEL_W, y))
    d.text((6, y - 16), f"{nome} · {rot}", fill="#111")
    y += linha_h

prova.save(f"{SAIDA}/_prova_48px.png")
print("prova em 48, 56, 96 e 200 px, sobre a interface clara e a escura")
