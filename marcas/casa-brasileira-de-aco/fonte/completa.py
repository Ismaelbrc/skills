# -*- coding: utf-8 -*-
"""Completa o pacote: PNG em alta para o simbolo, e JPEG onde JPEG faz sentido.

Duas lacunas encontradas na auditoria:

  1. o simbolo quadrado so tinha o jogo de icones, que para em 1024 px.
     Para adesivo grande e pintura de frota faltava alta resolucao.
  2. nao havia nenhum JPEG.

Sobre JPEG, duas coisas que decidem o formato:

  JPEG nao tem canal alfa. As versoes de fundo transparente (-cor e
  -mono-preto) nao viram JPEG: achatar sobre branco produziria um arquivo
  identico ao -branco mas com nome -cor, e e assim que erro de reproducao
  nasce. Quem precisa de JPEG sobre branco usa o -branco.

  JPEG e compressao com perda e trabalha mal com aresta dura de cor plana:
  gera franja em volta da letra. Fica em qualidade 95 sem subamostragem de
  croma (4:4:4), que e o menor estrago possivel. Onde aceitarem PNG, use PNG.
"""
import glob
import os
import re

import cairosvg
from PIL import Image

MARCA = "/home/user/skills/marcas/casa-brasileira-de-aco/marca"
ALTA = 8000
QUALIDADE = 95

# fundo declarado de cada versao — None quer dizer transparente
FUNDO = {
    "cor": None,
    "papel": "#F5F4F0",
    "branco": "#FFFFFF",
    "reversa-azul": "#002B5C",
    "reversa-preto": "#14161C",
    "mono-preto": None,
    "mono-branco": "#14161C",
}


def versao(nome):
    """Extrai o sufixo de versao do nome do arquivo."""
    for v in sorted(FUNDO, key=len, reverse=True):
        if nome.endswith("-" + v):
            return v
    return None


os.makedirs(f"{MARCA}/jpg-alta", exist_ok=True)

svgs = sorted(f for f in glob.glob(f"{MARCA}/CBA-*.svg"))
novos_png, novos_jpg, pulados = 0, 0, []

for f in svgs:
    nome = os.path.basename(f)[:-4]
    v = versao(nome)
    s = open(f, encoding="utf-8").read()
    w, h = (int(x) for x in re.search(r'viewBox="0 0 (\d+) (\d+)"', s).groups())
    escala = ALTA / max(w, h)

    # 1 · PNG em alta para quem ainda nao tem (o simbolo)
    destino_png = f"{MARCA}/png-alta/{nome}.png"
    if not os.path.exists(destino_png):
        cairosvg.svg2png(url=f, write_to=destino_png, scale=escala)
        novos_png += 1

    # 2 · JPEG so onde existe fundo solido
    if FUNDO[v] is None:
        pulados.append(nome)
        continue
    im = Image.open(destino_png).convert("RGBA")
    chapa = Image.new("RGB", im.size, FUNDO[v])
    chapa.paste(im, mask=im.split()[3])
    chapa.save(f"{MARCA}/jpg-alta/{nome}.jpg", "JPEG",
               quality=QUALIDADE, subsampling=0, optimize=True,
               progressive=True)
    novos_jpg += 1

print(f"PNG em alta criados: {novos_png}")
print(f"JPEG criados:        {novos_jpg}")
print(f"\nsem JPEG de proposito ({len(pulados)}), porque o fundo e transparente:")
for n in pulados:
    print("  ", n)

print("\n--- inventario final")
for d in ("", "png-alta", "png-web", "jpg-alta", "icones", "pdf"):
    cam = f"{MARCA}/{d}" if d else MARCA
    n = len([x for x in os.listdir(cam) if os.path.isfile(os.path.join(cam, x))])
    print(f"  {d or 'svg (raiz)':12} {n}")
