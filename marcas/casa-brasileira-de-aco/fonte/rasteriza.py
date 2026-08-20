# -*- coding: utf-8 -*-
"""Rasteriza a marca: PNG em alta, PNG web, PDF vetorial e icones quadrados."""
import glob, os, re
import cairosvg

D = "marca"
ALTA = 8000        # px na maior dimensao
WEB = 1600
ICONES = (1024, 512, 256, 128, 64, 32)

for sub in ("png-alta", "png-web", "pdf", "icones"):
    os.makedirs(f"{D}/{sub}", exist_ok=True)

n_marca = n_icone = 0
for f in sorted(glob.glob(f"{D}/CBA-*.svg")):
    nome = os.path.basename(f)[:-4]
    s = open(f, encoding="utf-8").read()
    w, h = (int(v) for v in re.search(r'viewBox="0 0 (\d+) (\d+)"', s).groups())
    cairosvg.svg2pdf(url=f, write_to=f"{D}/pdf/{nome}.pdf")
    if w == h:                                    # simbolo: jogo de icones
        for L in ICONES:
            cairosvg.svg2png(url=f, write_to=f"{D}/icones/{nome}-{L}.png",
                             scale=L / w)
        n_icone += 1
    else:
        maior = max(w, h)
        cairosvg.svg2png(url=f, write_to=f"{D}/png-alta/{nome}.png", scale=ALTA / maior)
        cairosvg.svg2png(url=f, write_to=f"{D}/png-web/{nome}.png", scale=WEB / maior)
        n_marca += 1
print(f"assinaturas: {n_marca} · simbolos: {n_icone} · icones: {n_icone*len(ICONES)}")
