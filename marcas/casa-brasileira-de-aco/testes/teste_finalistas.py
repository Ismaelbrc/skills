# -*- coding: utf-8 -*-
"""TESTE 3 — finalistas. Não entra no manual.

Os quatro que sobraram das duas rodadas, com a marca aprovada no topo para
comparar. Nada aqui substitui a assinatura sem decisão sua.
"""
import os
from kit import (VERDE, AMARELO, AZUL, BRANCO, OSSO, TINTA, CINZA_2, CORES,
                 MONO, TRACK, principal, largura_nome)
from teste_listras2 import fatiada, vazada, cap_altura, tinta

W, PAD, ROT = 1280, 50, 34
pecas, y = [], 0


def secao(t, sub=""):
    global y
    h = 62 if sub else 48
    pecas.append(
        f'<rect x="0" y="{y}" width="{W}" height="{h}" fill="{TINTA}"/>'
        f'<text x="{PAD}" y="{y+28}" font-family="{MONO}" font-size="13" '
        f'fill="{AMARELO}" letter-spacing="3">{t}</text>'
        + (f'<text x="{PAD}" y="{y+50}" font-family="{MONO}" font-size="11" '
           f'fill="#8b8e95" letter-spacing="1">{sub}</text>' if sub else ""))
    y += h + 8


def amostra(rot, inner, alto, bg=OSSO, folga=0):
    global y
    h = alto + PAD * 2 + ROT + folga
    pecas.append(
        f'<rect x="0" y="{y}" width="{W}" height="{h:.1f}" fill="{bg}"/>'
        f'<text x="{PAD}" y="{y+22}" font-family="{MONO}" font-size="12" '
        f'fill="{"#8b8e95" if bg == TINTA else CINZA_2}" letter-spacing="1.4">'
        f'{rot}</text>' + inner)
    y += h + 8


# ---------------------------------------------------------- a marca aprovada
secao("REFERÊNCIA · A ASSINATURA APROVADA",
      "a listra vive sob CASA BRASILEIRA e para na tinta do A")
S = 60
alto = S * 1.5
corpo, _ = principal(PAD, y + ROT + PAD + S * 0.74, S)
amostra("Jura Light · listra sob o nome", corpo, alto)

# ------------------------------------------------------------- A · fatiada
secao("A · LETRA FATIADA",
      "a letra é cortada em três faixas na proporção da marca — respiro 0,34")
for arq, nome, texto, S in (
        ("BigShoulders-Bold.ttf", "Big Shoulders Bold", "CASA BRASILEIRA", 100),
        ("Outfit-Bold.ttf", "Outfit Bold", "CASA BRASILEIRA", 92),
        ("BigShoulders-Bold.ttf", "Big Shoulders Bold", "CBA", 200),
        ("Outfit-Bold.ttf", "Outfit Bold", "CBA", 190)):
    a = cap_altura(arq, texto) * S
    inner, _ = fatiada(arq, texto, S, TRACK, 0.34, CORES,
                       PAD, y + ROT + PAD + a)
    amostra(f"{nome} · {texto}", inner, a)

# -------------------------------------------------------------- B · vazada
secao("B · LETRA VAZADA NAS LISTRAS",
      "as três listras formam o bloco e a palavra é recortada delas — "
      "funciona na Jura Light da marca")
for arq, nome, texto, S, bg in (
        ("Jura-Light.ttf", "Jura Light — a da marca", "CASA BRASILEIRA", 86, OSSO),
        ("Jura-Light.ttf", "Jura Light — a da marca", "CBA", 165, OSSO),
        ("Outfit-Bold.ttf", "Outfit Bold", "CBA", 155, OSSO),
        ("Jura-Light.ttf", "Jura Light · sobre fundo escuro", "CBA", 165, TINTA)):
    a = cap_altura(arq, texto) * S
    pb = a * 0.42
    cores = (BRANCO, AMARELO, BRANCO) if bg == TINTA else CORES
    inner, _, _, _, _ = vazada(arq, texto, S, TRACK, 0.34, cores,
                               PAD + pb, y + ROT + PAD + pb + a, fundo=bg)
    amostra(f"{nome} · {texto}", inner, a, bg, folga=pb * 2)

H = y
svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H:.0f}" '
       f'viewBox="0 0 {W} {H:.0f}">'
       f'<rect width="{W}" height="{H:.0f}" fill="#c9c7c1"/>{"".join(pecas)}</svg>')

os.makedirs("testes", exist_ok=True)
open("testes/teste_finalistas.svg", "w", encoding="utf-8").write(svg)
import cairosvg
cairosvg.svg2png(url="testes/teste_finalistas.svg",
                 write_to="testes/teste_finalistas.png", scale=2)
print("finalistas:", W, "x", round(H))
