# -*- coding: utf-8 -*-
"""Organiza o pacote da Raviva.

O material estava todo numa pasta só: entrega misturada a umas sessenta
capturas de QA do processo. Nada e jogado fora — o que e trabalho vai para
trabalho/ e para de competir com o que e entrega.

Duas lacunas preenchidas de passagem:
  · nao havia versao transparente. Os seis logos tinham o fundo embutido
    num <rect> unico, entao da para extrair.
  · nao havia JPEG.
"""
import os
import re
import shutil

import cairosvg
from PIL import Image

ORIG = "/home/user/skills/marcas/raviva"
DEST = "/tmp/claude-0/-home-user-skills/9b00c726-1271-5e08-a488-cbad7d5f439a/scratchpad/RAVIVA"
LOGOS = f"{ORIG}/final/RAVIVA_logo_arquivos"
ALTA = 6000
QUALIDADE = 95

for d in ("marca/svg", "marca/png-alta", "marca/jpg-alta", "pranchas",
          "fonte", "trabalho"):
    os.makedirs(f"{DEST}/{d}", exist_ok=True)

# ---------------------------------------------------------------- documentos
for f, destino in (("RAVIVA_defesa_e_manual.html", "."),
                   ("final/RAVIVA_defesa_e_manual.pdf", "."),
                   ("final/RAVIVA_manual_de_marca.pdf", ".")):
    shutil.copy2(f"{ORIG}/{f}", f"{DEST}/{destino}/{os.path.basename(f)}")

# -------------------------------------------------------------------- marca
RECT_FUNDO = re.compile(r'\s*<rect\s+width="\d+"\s+height="\d+"\s+fill="#[0-9A-Fa-f]{6}"\s*/>')
fundos, transparentes = [], []

for f in sorted(os.listdir(LOGOS)):
    if not f.endswith(".svg"):
        continue
    nome = f[:-4]
    s = open(f"{LOGOS}/{f}", encoding="utf-8").read()
    w, h = (int(x) for x in re.search(r'viewBox="0 0 (\d+) (\d+)"', s).groups())
    escala = ALTA / max(w, h)

    # com o fundo que ja tinha
    shutil.copy2(f"{LOGOS}/{f}", f"{DEST}/marca/svg/{nome}.svg")
    cairosvg.svg2png(url=f"{LOGOS}/{f}",
                     write_to=f"{DEST}/marca/png-alta/{nome}.png", scale=escala)
    cor = re.search(r'fill="(#[0-9A-Fa-f]{6})"', s).group(1)
    im = Image.open(f"{DEST}/marca/png-alta/{nome}.png").convert("RGB")
    im.save(f"{DEST}/marca/jpg-alta/{nome}.jpg", "JPEG", quality=QUALIDADE,
            subsampling=0, optimize=True, progressive=True)
    fundos.append((nome, cor))

    # sem o fundo — o rect e unico, entao sai limpo
    sem, n = RECT_FUNDO.subn("", s, count=1)
    if n != 1:
        print(f"  ATENCAO: {nome} nao tinha o rect de fundo esperado, pulado")
        continue
    alvo = f"{nome}-transparente"
    open(f"{DEST}/marca/svg/{alvo}.svg", "w", encoding="utf-8").write(sem)
    cairosvg.svg2png(bytestring=sem.encode("utf-8"),
                     write_to=f"{DEST}/marca/png-alta/{alvo}.png", scale=escala)
    transparentes.append(alvo)

# ----------------------------------------------------------------- pranchas
for f in sorted(os.listdir(f"{ORIG}/final")):
    if re.match(r"0\d_.+\.(svg|png|pdf)$", f):
        shutil.copy2(f"{ORIG}/final/{f}", f"{DEST}/pranchas/{f}")

# -------------------------------------------------------------------- fonte
for f in ("brand_kit.py", "build_site.py"):
    shutil.copy2(f"{ORIG}/{f}", f"{DEST}/fonte/{f}")

# ----------------------------------------------------------------- trabalho
ENTREGA = re.compile(r"^(0\d_|RAVIVA_)")
n_trab = 0
for f in sorted(os.listdir(f"{ORIG}/final")):
    cam = f"{ORIG}/final/{f}"
    if os.path.isfile(cam) and not ENTREGA.match(f):
        shutil.copy2(cam, f"{DEST}/trabalho/{f}")
        n_trab += 1

print(f"marca:     {len(fundos)} com fundo + {len(transparentes)} transparentes")
print(f"           {len(fundos)} JPEG")
print(f"pranchas:  {len(os.listdir(f'{DEST}/pranchas'))}")
print(f"trabalho:  {n_trab} capturas do processo")
print("\nfundo embutido em cada logo:")
for nome, cor in fundos:
    print(f"  {nome:32} {cor}")
