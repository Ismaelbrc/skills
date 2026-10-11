# -*- coding: utf-8 -*-
"""BR.AÇO — avatar de WhatsApp, versao final.

Escolhido: BR. com a barra de tres listras embaixo.

O teste de 48 px eliminou o resto:
  marca inteira   5,25:1 nao cabe em circulo. A 48 px vira borrao
  so as listras   vira um risco
  BR. sozinho     le bem, mas perde o amarelo e o azul da marca
  BR. + listras   le a 48 px E mantem as tres cores  <-

A barra de listras aqui nao e o trecho cortado do logo: e a faixa inteira
reescalada para a largura exata do BR., para nao parecer que sobrou pedaco.

LIMITE DA FONTE: isto saiu de uma captura de tela. O logo extraido tem
1108 x 211 px, entao o BR. recortado tem 440 x 132. Para 1000 px ha
ampliacao de 1,55x. Com o vetor original o resultado seria melhor.
"""
import os

from PIL import Image, ImageDraw

VERDE, AMARELO, AZUL, PAPEL = (44, 103, 69), (231, 178, 61), (17, 49, 103), (245, 244, 240)
AQUI = os.path.dirname(os.path.abspath(__file__))
SAIDA = os.path.join(AQUI, "..", "avatar-whatsapp")
LOGO = Image.open(os.path.join(AQUI, "logo-extraido-da-captura.png")).convert("RGB")
W, H = LOGO.size
CORTE, LETRAS = 440, 132

BR = LOGO.crop((0, 0, CORTE, LETRAS))
LISTRAS = LOGO.crop((0, 141, W, H))
MARCA = LOGO


def limpa(im, cores=(VERDE, AMARELO, AZUL, PAPEL), tol=90):
    """Depois de reescalar, joga cada pixel na cor da marca mais proxima.
    Nao redesenha nada — so tira a bordinha cinza que a interpolacao cria."""
    px = im.load()
    w, h = im.size
    for y in range(h):
        for x in range(w):
            r, g, b = px[x, y]
            melhor, dist = None, 1e9
            for c in cores:
                d = (r - c[0]) ** 2 + (g - c[1]) ** 2 + (b - c[2]) ** 2
                if d < dist:
                    dist, melhor = d, c
            px[x, y] = melhor if dist < tol ** 2 else (r, g, b)
    return im


def br_com_listras(larg, respiro_f=0.085, trecho=560):
    """BR. em cima, barra de tres listras embaixo, na mesma largura.

    A barra nao e a faixa inteira espremida: e um TRECHO de 560 px dela,
    ampliado por escala uniforme ate a largura do BR. Assim a espessura de
    cada listra cresce 1,6x e sobrevive aos 48 px — sem achatar nada, que
    seria mexer no desenho de outro."""
    bw, bh = BR.size
    letras = BR.resize((larg, round(bh * larg / bw)), Image.LANCZOS)
    corte = LISTRAS.crop((0, 0, trecho, LISTRAS.height))
    lw, lh = corte.size
    barra = corte.resize((larg, round(lh * larg / lw)), Image.LANCZOS)
    vao = round(larg * respiro_f)
    alt = letras.height + vao + barra.height
    cv = Image.new("RGB", (larg, alt), PAPEL)
    cv.paste(letras, (0, 0))
    cv.paste(barra, (0, letras.height + vao))
    return cv


def avatar(L, peca, larg_f, aro=VERDE, aro_f=0.030, limpar=True):
    cv = Image.new("RGB", (L, L), PAPEL)
    alvo = int(L * larg_f)
    w, h = peca.size
    nova = (alvo, max(1, round(h * alvo / w)))
    if nova[1] > L * 0.78:
        nova = (round(w * L * 0.78 / h), int(L * 0.78))
    p = peca.resize(nova, Image.LANCZOS)
    if limpar:
        p = limpa(p)
    cv.paste(p, ((L - nova[0]) // 2, (L - nova[1]) // 2))
    if aro:
        lar = max(2, round(L * aro_f))
        ImageDraw.Draw(cv).ellipse(
            (lar // 2, lar // 2, L - lar // 2 - 1, L - lar // 2 - 1),
            outline=aro, width=lar)
    return cv


for d in ("png", "jpg"):
    os.makedirs(f"{SAIDA}/{d}", exist_ok=True)

PECAS = [
    ("BRACO-whatsapp",            br_com_listras(900), 0.70),
    ("BRACO-whatsapp-br",         BR,                  0.74),
    ("BRACO-whatsapp-marca",      MARCA,               0.90),
]

for nome, peca, lf in PECAS:
    for S in (1000, 640):
        im = avatar(S, peca, lf)
        im.save(f"{SAIDA}/png/{nome}-{S}.png")
        im.save(f"{SAIDA}/jpg/{nome}-{S}.jpg", "JPEG", quality=95,
                subsampling=0, optimize=True)

print(f"{len(PECAS)} peças · 1000 e 640 px · PNG e JPEG")

# ---------------------------------------------------------------- a prova
UI = (("interface clara", "#FFFFFF"), ("interface escura", "#0B141A"))
TAM = [48, 56, 96, 200]
CEL, lin = 440, 240
prova = Image.new("RGB", (CEL * 2, lin * len(PECAS) + 52), "#9a9a9a")
d = ImageDraw.Draw(prova)
for col, (rot, _) in enumerate(UI):
    d.text((col * CEL + 14, 14), rot.upper(), fill="#111")
y = 40
for nome, _, _ in PECAS:
    src = Image.open(f"{SAIDA}/png/{nome}-1000.png")
    d.text((8, y + 4), nome, fill="#111")
    for col, (_, ui) in enumerate(UI):
        faixa = Image.new("RGB", (CEL, lin - 22), ui)
        x = 16
        for S in TAM:
            mini = src.resize((S, S), Image.LANCZOS)
            masc = Image.new("L", (S, S), 0)
            ImageDraw.Draw(masc).ellipse((0, 0, S - 1, S - 1), fill=255)
            faixa.paste(mini, (x, (lin - 22 - S) // 2), masc)
            x += S + 16
        prova.paste(faixa, (col * CEL, y + 20))
    y += lin
prova.save(f"{SAIDA}/COMO-FICA-NO-APP.png")
print("prova gerada")
