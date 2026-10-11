# -*- coding: utf-8 -*-
"""Avatar de WhatsApp — arquivos finais.

Escolhido: circulo VERDE #006B3C com listra branco/amarelo/branco.

Por que este, e nao outro:
  · e literalmente verde e amarelo, que foi o pedido
  · funciona com 48 px nos dois temas do WhatsApp, que e o unico requisito
    que de fato elimina opcao. O preto some contra a interface escura; o
    papel claro some contra a clara
  · sobre o verde, branco da 6,63:1 e amarelo 3,65:1. Azul (2,11) e preto
    (2,73) nao passam — mesma logica da regra de fundo escuro da marca
  · verde e a cor que assina, pela propria especificacao

Entrega em quadrado de bordo a bordo: o WhatsApp recorta em circulo, e com
a cor preenchendo a tela inteira o recorte sai limpo em qualquer variacao.
"""
import os

import cairosvg
from PIL import Image

VERDE, AMARELO, AZUL = "#006B3C", "#F2B705", "#002B5C"
BRANCO, OSSO, TINTA = "#FFFFFF", "#F5F4F0", "#14161C"
CORES = (VERDE, AMARELO, AZUL)
REV = (BRANCO, AMARELO, BRANCO)

SAIDA = ("/tmp/claude-0/-home-user-skills/9b00c726-1271-5e08-a488-cbad7d5f439a"
         "/scratchpad/AVATAR_WHATSAPP")
for d in ("svg", "png", "jpg"):
    os.makedirs(f"{SAIDA}/{d}", exist_ok=True)


def listras(L, cores, comp_f=0.64):
    """O bloco solto da marca: respiro 0,34 da espessura."""
    comp = L * comp_f
    alt = comp / 2.0
    t = alt * 0.28
    g = t * 0.34
    k = alt / (3 * t + 2 * g)
    t, g = t * k, g * k
    y = (L - (3 * t + 2 * g)) / 2
    x = (L - comp) / 2
    return "".join(
        f'<rect x="{x:.2f}" y="{y + i*(t+g):.2f}" width="{comp:.2f}" '
        f'height="{t:.2f}" fill="{c}"/>' for i, c in enumerate(cores))


def quadrado(L, fundo, cores, comp_f=0.64):
    """Quadrado de bordo a bordo — o recorte circular do app sai limpo."""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{L}" height="{L}" '
            f'viewBox="0 0 {L} {L}">'
            f'<rect width="{L}" height="{L}" fill="{fundo}"/>'
            f'{listras(L, cores, comp_f)}</svg>')


def circulo(L, fundo, cores, aro=None, comp_f=0.64):
    """Circulo com canto transparente — para outros usos."""
    o = f'<circle cx="{L/2}" cy="{L/2}" r="{L/2}" fill="{fundo}"/>'
    if aro:
        lar = L * 0.034
        o += (f'<circle cx="{L/2}" cy="{L/2}" r="{L/2 - lar/2:.1f}" fill="none" '
              f'stroke="{aro}" stroke-width="{lar:.1f}"/>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{L}" height="{L}" '
            f'viewBox="0 0 {L} {L}">{o}{listras(L, cores, comp_f)}</svg>')


L = 1000
PECAS = [
    # (nome, svg, tem_transparencia)
    ("CBA-whatsapp-verde",            quadrado(L, VERDE, REV), False),
    ("CBA-whatsapp-verde-circulo",    circulo(L, VERDE, REV), True),
    # as duas alternativas que tambem passaram no teste de 48 px
    ("CBA-whatsapp-azul",             quadrado(L, AZUL, REV), False),
    ("CBA-whatsapp-papel-aro",        quadrado(L, OSSO, CORES), False),
    ("CBA-whatsapp-papel-aro-circulo", circulo(L, OSSO, CORES, aro=VERDE), True),
]

TAMANHOS = (1000, 640)
for nome, svg, transp in PECAS:
    open(f"{SAIDA}/svg/{nome}.svg", "w", encoding="utf-8").write(svg)
    for S in TAMANHOS:
        png = f"{SAIDA}/png/{nome}-{S}.png"
        cairosvg.svg2png(url=f"{SAIDA}/svg/{nome}.svg", write_to=png,
                         output_width=S, output_height=S)
        if not transp:          # JPEG so onde nao ha transparencia a perder
            im = Image.open(png).convert("RGB")
            im.save(f"{SAIDA}/jpg/{nome}-{S}.jpg", "JPEG", quality=95,
                    subsampling=0, optimize=True)

n_png = len(os.listdir(f"{SAIDA}/png"))
n_jpg = len(os.listdir(f"{SAIDA}/jpg"))
print(f"{len(PECAS)} peças · {n_png} PNG · {n_jpg} JPEG · SVG vetor")
print("tamanhos: 1000 e 640 px")
