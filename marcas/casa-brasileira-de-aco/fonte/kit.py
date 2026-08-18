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


# ------------------------------------------------- ajuste optico de DE ACO
def _vao(a, b, track=TRACK):
    """Vao de tinta entre dois glifos vizinhos, em fracao do corpo."""
    adv_a, _, xmax_a = _metricas(a)
    _, lsb_b, _ = _metricas(b)
    return ((adv_a - xmax_a) + lsb_b) / _UPM + track


def _pares(texto):
    return [(texto[i], texto[i + 1]) for i in range(len(texto) - 1)
            if " " not in (texto[i], texto[i + 1])]


def _vao_palavra(a, b, track=TRACK):
    adv_a, _, xmax_a = _metricas(a)
    _, lsb_b, _ = _metricas(b)
    adv_sp, _, _ = _metricas(" ")
    return ((adv_a - xmax_a) + adv_sp + lsb_b) / _UPM + 2 * track


# ritmo de referencia: a media dos vaos de CASA BRASILEIRA
VAO = sum(_vao(a, b) for a, b in _pares("CASA BRASILEIRA")) / len(_pares("CASA BRASILEIRA"))
VAO_PALAVRA = _vao_palavra("A", "B")


def kern(texto, track=TRACK):
    """Correcao por par, em fracao do corpo, para o vao optico de `texto`
    bater com o ritmo de CASA BRASILEIRA.

    D, E, C e O tem lateral mais larga na Jura: com a mesma entreletra
    numerica o vao de tinta sai maior. Isto devolve o vao, nao o numero.
    """
    fora = [0.0]
    for i in range(len(texto) - 1):
        a, b = texto[i], texto[i + 1]
        if a == " ":
            continue
        if b == " ":
            c = texto[i + 2]
            fora.append(VAO_PALAVRA - _vao_palavra(a, c, track))
        else:
            fora.append(VAO - _vao(a, b, track))
    return fora


def _tspans(texto, S, track=TRACK):
    """Os glifos de `texto` com o dx de correcao optica em cada par."""
    dx = kern(texto, track)
    saida, j = [], 0
    for c in texto:
        if c == " ":
            saida.append(" ")
            continue
        d = dx[j]
        saida.append(c if j == 0 or abs(d) < 1e-9
                     else f'<tspan dx="{d*S:.3f}">{c}</tspan>')
        j += 1
    return "".join(saida)


def nome(x, y, S, c1=None, c2=None, track=TRACK):
    """O nome inteiro em um <text>. CASA BRASILEIRA sai na entreletra pura;
    DE ACO leva o ajuste optico para o vao bater com ela."""
    c1 = c1 or TINTA
    c2 = c2 or VERDE
    # a correcao do vao entre BRASILEIRA e DE entra no primeiro glifo do DE
    d0 = VAO_PALAVRA - _vao_palavra("A", "D", track)
    abre = f'<tspan dx="{d0*S:.3f}">D</tspan>' if abs(d0) > 1e-9 else "D"
    resto = _tspans("DE AÇO", S, track)[1:]      # tudo depois do D
    return (f'<text x="{x}" y="{y}" font-family="{JURA}" font-weight="300" '
            f'font-size="{S}" fill="{c1}" letter-spacing="{S*track:.3f}" '
            f'xml:space="preserve">CASA BRASILEIRA '
            f'<tspan fill="{c2}">{abre}{resto}</tspan></text>')


def largura_kern(texto, S, track=TRACK):
    """Largura de tinta de `texto` com o ajuste optico aplicado."""
    return largura_tinta(texto, S, track) + sum(kern(texto, track)) * S


def largura_nome(S, track=TRACK):
    """Largura de tinta do nome inteiro — do C ao O — com o ajuste optico."""
    k = S / _UPM
    _, lsb_c, _ = _metricas("C")
    _, lsb_d, _ = _metricas("D")
    d0 = VAO_PALAVRA - _vao_palavra("A", "D", track)
    return (avanco("CASA BRASILEIRA ", S, track) + d0 * S + lsb_d * k
            + largura_kern("DE AÇO", S, track) - lsb_c * k)


def avanco_nome(S, track=TRACK):
    """Avanco de CASA BRASILEIRA + espaco, ja com a correcao do vao seguinte."""
    d0 = VAO_PALAVRA - _vao_palavra("A", "D", track)
    return avanco("CASA BRASILEIRA ", S, track) + d0 * S


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
    o = nome(x, y, S, c1, c2)
    lst, alt = listras(x0, y + S * 0.32, lar, S, cores, esp_f, resp_f)
    return o + lst, alt


# ---------------------------------------------------- 1 · HORIZONTAL
def de_aco(x, y, S, cor, track=TRACK, anchor=None):
    """DE ACO isolado, com o mesmo ajuste optico da assinatura principal."""
    a = f' text-anchor="{anchor}"' if anchor else ""
    return (f'<text x="{x}" y="{y}" font-family="{JURA}" font-weight="300" '
            f'font-size="{S}" fill="{cor}" letter-spacing="{S*track:.3f}" '
            f'xml:space="preserve"{a}>{_tspans("DE AÇO", S, track)}</text>')


def horizontal(x, y, S, c1=TINTA, c2=VERDE, cores=CORES):
    alt = S * 1.62
    bl, L = listras_bloco(x + S * 1.62, y, alt, cores)
    tx = x + L + S * 0.95
    o = bl
    o += (f'<text x="{tx}" y="{y - S*0.30:.2f}" font-family="{JURA}" font-weight="300" '
          f'font-size="{S}" fill="{c1}" letter-spacing="{S*TRACK:.3f}">CASA BRASILEIRA</text>')
    o += de_aco(tx, y + S * 0.65, S, c2)
    return o


# ---------------------------------------------------- 2 · VERTICAL
def vertical(cx, y, S, c1=TINTA, c2=VERDE, cores=CORES):
    alt = S * 1.62
    bl, L = listras_bloco(cx, y, alt, cores)
    o = bl
    o += (f'<text x="{cx}" y="{y + alt*0.62 + S*1.05:.2f}" font-family="{JURA}" '
          f'font-weight="300" font-size="{S}" fill="{c1}" text-anchor="middle" '
          f'letter-spacing="{S*TRACK:.3f}">CASA BRASILEIRA</text>')
    o += de_aco(cx, y + alt * 0.62 + S * 2.00, S, c2, anchor="middle")
    return o


# ---------------------------------------------------- 3 · UMA LINHA
def uma_linha(x, y, S, c1=TINTA, c2=VERDE, cores=CORES):
    alt = S * 1.30
    bl, L = listras_bloco(x + alt * 1.0, y, alt, cores)
    tx = x + L + S * 0.85
    o = bl
    o += nome(tx, y + S * 0.33, S, c1, c2)
    return o
