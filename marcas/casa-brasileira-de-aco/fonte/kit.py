# -*- coding: utf-8 -*-
"""Casa Brasileira de Aco — versao aprovada.

Paleta grave (a primeira que indiquei), Jura Light, listras grossas.
Composicao principal: listras sob CASA BRASILEIRA, terminando exatamente
no A final de BRASILEIRA — nunca sob DE ACO.
"""
from fontTools.ttLib import TTFont

# ------------------------------------------------------- paleta (grave)
VERDE   = "#006B3C"
AMARELO = "#F2B705"
AZUL    = "#002B5C"
BRANCO  = "#FFFFFF"
OSSO    = "#F5F4F0"
TINTA   = "#14161C"
CINZA   = "#8A8B90"
CINZA_2 = "#5A5C60"

CORES = (VERDE, AMARELO, AZUL)

JURA = "Jura Light"
MONO = "IBM Plex Mono"

TRACK = 0.155          # entreletra, fracao do corpo

# ------------------------------------------------------- metrica da fonte
_F = TTFont('/root/.fonts/Jura-Light.ttf')
_UPM = _F['head'].unitsPerEm
_CMAP = _F.getBestCmap()
_HMTX = _F['hmtx']
_GLYF = _F['glyf']


def _metricas(ch):
    g = _CMAP[ord(ch)]
    adv, lsb = _HMTX[g]
    gl = _GLYF[g]
    xmax = gl.xMax if gl.numberOfContours else adv
    return adv, lsb, xmax


def largura_tinta(texto, S, track=TRACK):
    """Largura real da tinta: da borda esquerda do 1o glifo a borda direita
    do ultimo. E isso que faz a listra terminar exatamente no A de BRASILEIRA."""
    if not texto:
        return 0.0
    k = S / _UPM
    ls = S * track
    soma = sum(_metricas(c)[0] for c in texto) * k
    soma += ls * (len(texto) - 1)
    _, lsb0, _ = _metricas(texto[0])
    advn, _, xmaxn = _metricas(texto[-1])
    return soma - lsb0 * k - (advn - xmaxn) * k


def avanco(texto, S, track=TRACK):
    """Avanco completo, com o espacamento depois do ultimo glifo."""
    k = S / _UPM
    return sum(_metricas(c)[0] for c in texto) * k + S * track * len(texto)


# --------------------------------------------------------------- listras
def listras(x, y, largura, S, cores=CORES, esp_f=0.140, resp_f=0.34):
    """Tres listras grossas. esp_f = espessura em fracao do corpo;
    resp_f = respiro entre listras, em fracao da espessura."""
    t = S * esp_f
    g = t * resp_f
    o = []
    for i, c in enumerate(cores):
        yy = y + i * (t + g)
        o.append(f'<rect x="{x:.2f}" y="{yy:.2f}" width="{largura:.2f}" '
                 f'height="{t:.2f}" fill="{c}"/>')
    return "".join(o), 3 * t + 2 * g


def listras_bloco(cx, cy, alt, cores=CORES, comp_f=2.0, esp_f=0.28, resp_f=0.34,
                  vert=False):
    """Bloco de listras solto (para as composicoes 1, 2 e 3)."""
    t = alt * esp_f
    g = t * resp_f
    total = 3 * t + 2 * g
    k = alt / total
    t *= k
    g *= k
    L = alt * comp_f
    o = []
    for i, c in enumerate(cores):
        d = (i - 1) * (t + g)
        if vert:
            o.append(f'<rect x="{cx+d-t/2:.2f}" y="{cy-L/2:.2f}" width="{t:.2f}" '
                     f'height="{L:.2f}" fill="{c}"/>')
        else:
            o.append(f'<rect x="{cx-L/2:.2f}" y="{cy+d-t/2:.2f}" width="{L:.2f}" '
                     f'height="{t:.2f}" fill="{c}"/>')
    return "".join(o), L


# ---------------------------------------------------- 4 · PRINCIPAL
def principal(x, y, S, c1=TINTA, c2=VERDE, cores=CORES, esp_f=0.140, resp_f=0.34):
    """Nome em uma linha; listras sob CASA BRASILEIRA, ate o A final.

    y = linha de base do texto.
    """
    lar = largura_tinta("CASA BRASILEIRA", S)
    _, lsb0, _ = _metricas("C")
    x0 = x + lsb0 * (S / _UPM)          # a listra comeca na tinta do C, nao no avanco
    o = (f'<text x="{x}" y="{y}" font-family="{JURA}" font-weight="300" '
         f'font-size="{S}" fill="{c1}" letter-spacing="{S*TRACK:.3f}" '
         f'xml:space="preserve">CASA BRASILEIRA <tspan fill="{c2}">DE AÇO</tspan></text>')
    lst, alt = listras(x0, y + S * 0.32, lar, S, cores, esp_f, resp_f)
    return o + lst, alt


# ---------------------------------------------------- 1 · HORIZONTAL
def horizontal(x, y, S, c1=TINTA, c2=VERDE, cores=CORES):
    alt = S * 1.62
    bl, L = listras_bloco(x + S * 1.62, y, alt, cores)
    tx = x + L + S * 0.95
    o = bl
    o += (f'<text x="{tx}" y="{y - S*0.30:.2f}" font-family="{JURA}" font-weight="300" '
          f'font-size="{S}" fill="{c1}" letter-spacing="{S*TRACK:.3f}">CASA BRASILEIRA</text>'
          f'<text x="{tx}" y="{y + S*0.65:.2f}" font-family="{JURA}" font-weight="300" '
          f'font-size="{S}" fill="{c2}" letter-spacing="{S*0.435:.3f}">DE AÇO</text>')
    return o


# ---------------------------------------------------- 2 · VERTICAL
def vertical(cx, y, S, c1=TINTA, c2=VERDE, cores=CORES):
    alt = S * 1.62
    bl, L = listras_bloco(cx, y, alt, cores)
    o = bl
    o += (f'<text x="{cx}" y="{y + alt*0.62 + S*1.05:.2f}" font-family="{JURA}" '
          f'font-weight="300" font-size="{S}" fill="{c1}" text-anchor="middle" '
          f'letter-spacing="{S*TRACK:.3f}">CASA BRASILEIRA</text>'
          f'<text x="{cx}" y="{y + alt*0.62 + S*2.00:.2f}" font-family="{JURA}" '
          f'font-weight="300" font-size="{S}" fill="{c2}" text-anchor="middle" '
          f'letter-spacing="{S*0.435:.3f}">DE AÇO</text>')
    return o


# ---------------------------------------------------- 3 · UMA LINHA
def uma_linha(x, y, S, c1=TINTA, c2=VERDE, cores=CORES):
    alt = S * 1.30
    bl, L = listras_bloco(x + alt * 1.0, y, alt, cores)
    tx = x + L + S * 0.85
    o = bl
    o += (f'<text x="{tx}" y="{y + S*0.33:.2f}" font-family="{JURA}" font-weight="300" '
          f'font-size="{S}" fill="{c1}" letter-spacing="{S*TRACK:.3f}" '
          f'xml:space="preserve">CASA BRASILEIRA <tspan fill="{c2}">DE AÇO</tspan></text>')
    return o
