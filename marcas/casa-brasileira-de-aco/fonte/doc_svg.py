# -*- coding: utf-8 -*-
"""Fragmentos SVG usados no manual — todos gerados pela mesma metrica da marca."""
from kit import *
from kit import _metricas, _UPM


def svg(w, h, inner, bg=None):
    fundo = f'<rect width="{w}" height="{h}" fill="{bg}"/>' if bg else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
            f'style="width:100%;height:auto;display:block" role="img">{fundo}{inner}</svg>')


def marca(S=64, bg=None, c1=TINTA, c2=VERDE, cores=CORES, pad_f=0.55):
    lar = avanco("CASA BRASILEIRA ", S) + largura_tinta("DE AÇO", S)
    pad = S * pad_f
    w = lar + 2 * pad
    h = S * 2.05
    corpo, _ = principal(pad, S * 1.12, S, c1, c2, cores)
    return svg(round(w), round(h), corpo, bg)


def marca_alt(tipo, S=40, bg=None, c1=TINTA, c2=VERDE, cores=CORES):
    """Largura derivada das metricas reais — nada estimado."""
    nome_2l = max(largura_tinta("CASA BRASILEIRA", S), largura_tinta("DE AÇO", S))
    nome_1l = avanco("CASA BRASILEIRA ", S) + largura_tinta("DE AÇO", S)
    if tipo == "horizontal":
        bloco_L = (S * 1.62) * 2.0
        w = S * 0.5 + bloco_L + S * 0.95 + nome_2l + S * 0.7
        h = S * 3.0
        inner = horizontal(S * 0.5, h / 2, S, c1, c2, cores)
    elif tipo == "vertical":
        w = max(nome_2l, (S * 1.62) * 2.0) + S * 1.6
        h = S * 4.5
        inner = vertical(w / 2, S * 1.30, S, c1, c2, cores)
    else:
        bloco_L = (S * 1.30) * 2.0
        w = S * 0.5 + bloco_L + S * 0.85 + nome_1l + S * 0.7
        h = S * 2.4
        inner = uma_linha(S * 0.5, h / 2, S, c1, c2, cores)
    return svg(round(w), round(h), inner, bg)


# ------------------------------------------------------------ construcao
def construcao(S=62):
    lar = largura_tinta("CASA BRASILEIRA", S)
    _, lsb0, _ = _metricas("C")
    k = S / _UPM
    pad = S * 0.9
    x = pad
    x0 = x + lsb0 * k
    base = S * 1.35
    w = avanco("CASA BRASILEIRA ", S) + largura_tinta("DE AÇO", S) + 2 * pad
    h = S * 2.85
    corpo, alt = principal(x, base, S)
    o = corpo
    # cotas
    g = "#C0392B"
    o += (f'<line x1="{x0:.1f}" y1="{base-S*1.05:.1f}" x2="{x0:.1f}" y2="{base+S*1.15:.1f}" '
          f'stroke="{g}" stroke-width="1" stroke-dasharray="4 4"/>'
          f'<line x1="{x0+lar:.1f}" y1="{base-S*1.05:.1f}" x2="{x0+lar:.1f}" '
          f'y2="{base+S*1.15:.1f}" stroke="{g}" stroke-width="1" stroke-dasharray="4 4"/>')
    o += (f'<line x1="{x0:.1f}" y1="{base-S*0.92:.1f}" x2="{x0+lar:.1f}" '
          f'y2="{base-S*0.92:.1f}" stroke="{g}" stroke-width="1"/>')
    o += (f'<text x="{x0+lar/2:.1f}" y="{base-S*1.02:.1f}" font-family="{MONO}" '
          f'font-size="{S*0.20:.1f}" fill="{g}" text-anchor="middle">L = tinta de CASA BRASILEIRA</text>')
    # espessura
    t = S * 0.140
    yb = base + S * 0.32
    o += (f'<line x1="{x0+lar+S*0.25:.1f}" y1="{yb:.1f}" x2="{x0+lar+S*0.25:.1f}" '
          f'y2="{yb+t:.1f}" stroke="{g}" stroke-width="1.5"/>')
    o += (f'<text x="{x0+lar+S*0.42:.1f}" y="{yb+t*0.9:.1f}" font-family="{MONO}" '
          f'font-size="{S*0.19:.1f}" fill="{g}">t = 0,140 × corpo</text>')
    return svg(round(w), round(h), o)


def protecao(S=52):
    lar_total = avanco("CASA BRASILEIRA ", S) + largura_tinta("DE AÇO", S)
    _, lsb0, _ = _metricas("C")
    k = S / _UPM
    t = S * 0.140
    alt_listras = 3 * t + 2 * (t * 0.34)
    X = alt_listras                       # unidade de protecao
    pad = X * 1.6
    x = pad
    base = pad + S * 0.78
    w = lar_total + 2 * pad
    h = base + S * 0.32 + alt_listras + pad
    corpo, _ = principal(x, base, S)
    o = corpo
    o += (f'<rect x="{x + lsb0*k - X:.1f}" y="{base - S*0.72 - X:.1f}" '
          f'width="{lar_total + 2*X - lsb0*k:.1f}" '
          f'height="{S*0.72 + S*0.32 + alt_listras + 2*X:.1f}" fill="none" '
          f'stroke="{VERDE}" stroke-width="1.4" stroke-dasharray="7 6"/>')
    o += (f'<text x="{x + lsb0*k - X + 6:.1f}" y="{base - S*0.72 - X - 8:.1f}" '
          f'font-family="{MONO}" font-size="{S*0.21:.1f}" fill="{VERDE}">'
          f'respiro mínimo = X</text>')
    return svg(round(w), round(h), o)


def escala():
    tamanhos = [46, 32, 22, 15, 11]
    pad = 26
    x = pad
    linhas = []
    for S in tamanhos:
        corpo, _ = principal(x, 74, S)
        linhas.append(corpo)
        linhas.append(f'<text x="{x}" y="104" font-family="{MONO}" font-size="11" '
                      f'fill="{CINZA_2}">{S} px</text>')
        x += avanco("CASA BRASILEIRA ", S) + largura_tinta("DE AÇO", S) + 34
    return svg(round(x + pad), 126, "".join(linhas))


# ------------------------------------------------------------ aplicacoes
def etiqueta(w=520, h=380):
    o = f'<rect width="{w}" height="{h}" fill="{OSSO}" stroke="{CINZA}" stroke-width="1"/>'
    o += f'<rect x="0" y="0" width="{w}" height="76" fill="{AZUL}"/>'
    m, _ = principal(24, 44, 15, BRANCO, AMARELO, (BRANCO, AMARELO, BRANCO))
    o += m
    linhas = [("OBRA", "RESIDENCIAL VILA NOVA"), ("ELEMENTO", "VIGA V-12"),
              ("ROMANEIO", "2026 / 0431"), ("POSIÇÃO", "N5"),
              ("BITOLA", "Ø 10,0 mm · CA-50"), ("FORMATO", "ESTRIBO 90°"),
              ("QUANTIDADE", "48 PEÇAS"), ("COMPRIMENTO", "C = 245 cm")]
    for i, (kk, v) in enumerate(linhas):
        y = 124 + i * 31
        o += (f'<text x="24" y="{y}" font-family="{MONO}" font-size="11.5" fill="{CINZA_2}" '
              f'letter-spacing="1.6">{kk}</text>'
              f'<text x="176" y="{y}" font-family="{MONO}" font-size="13" fill="{TINTA}">{v}</text>')
    return svg(w, h, o)


def frota(w=620, h=300):
    o = f'<rect width="{w}" height="{h}" fill="{OSSO}"/>'
    # bau
    o += f'<rect x="40" y="70" width="430" height="150" rx="6" fill="{AZUL}"/>'
    # cabine
    o += f'<path d="M 470 220 L 470 120 L 540 120 L 578 168 L 578 220 Z" fill="{AZUL}"/>'
    o += f'<rect x="486" y="130" width="52" height="34" rx="3" fill="{OSSO}" opacity="0.85"/>'
    for cx in (120, 300, 420, 540):
        o += f'<circle cx="{cx}" cy="{224}" r="26" fill="{TINTA}"/>'
        o += f'<circle cx="{cx}" cy="{224}" r="11" fill="{CINZA}"/>'
    m, _ = principal(78, 148, 22, BRANCO, AMARELO, (BRANCO, AMARELO, BRANCO))
    o += m
    return svg(w, h, o)


def cartao(w=520, h=300):
    o = f'<rect width="{w}" height="{h}" fill="{OSSO}"/>'
    o += f'<rect x="20" y="20" width="230" height="130" fill="{BRANCO}" stroke="{CINZA}" stroke-width="1"/>'
    m, _ = principal(38, 62, 11)
    o += m
    o += (f'<text x="38" y="110" font-family="{MONO}" font-size="8.5" fill="{CINZA_2}">'
          f'corte e dobra de vergalhão</text>')
    o += f'<rect x="270" y="20" width="230" height="130" fill="{AZUL}"/>'
    m2, _ = principal(288, 62, 11, BRANCO, AMARELO, (BRANCO, AMARELO, BRANCO))
    o += m2
    # papel timbrado
    o += f'<rect x="20" y="170" width="480" height="110" fill="{BRANCO}" stroke="{CINZA}" stroke-width="1"/>'
    m3, _ = principal(42, 206, 12)
    o += m3
    for i in range(4):
        o += (f'<rect x="42" y="{232+i*13}" width="{300 - i*38}" height="3" '
              f'fill="{CINZA}" opacity="0.35"/>')
    return svg(w, h, o)


def site(w=620, h=340):
    o = f'<rect width="{w}" height="{h}" fill="{OSSO}"/>'
    o += f'<rect x="20" y="20" width="580" height="300" fill="{BRANCO}" stroke="{CINZA}" stroke-width="1"/>'
    o += f'<rect x="20" y="20" width="580" height="34" fill="{OSSO}"/>'
    for i, c in enumerate(["#d9d6cf", "#d9d6cf", "#d9d6cf"]):
        o += f'<circle cx="{40+i*16}" cy="37" r="5" fill="{c}"/>'
    m, _ = principal(44, 92, 15)
    o += m
    for i, t in enumerate(["CORTE E DOBRA", "TELAS", "ORÇAMENTO"]):
        o += (f'<text x="{330+i*90}" y="92" font-family="{MONO}" font-size="9" '
              f'fill="{CINZA_2}" letter-spacing="1">{t}</text>')
    o += f'<rect x="20" y="118" width="580" height="1" fill="{CINZA}" opacity="0.3"/>'
    o += (f'<text x="44" y="182" font-family="{JURA}" font-weight="300" font-size="34" '
          f'fill="{TINTA}" letter-spacing="2.4">O AÇO JÁ CHEGA PRONTO.</text>')
    o += (f'<text x="44" y="216" font-family="{MONO}" font-size="11" fill="{CINZA_2}">'
          f'Cortado, dobrado e identificado — na medida da sua obra.</text>')
    o += f'<rect x="44" y="240" width="150" height="34" fill="{VERDE}"/>'
    o += (f'<text x="119" y="262" font-family="{MONO}" font-size="10" fill="{BRANCO}" '
          f'text-anchor="middle" letter-spacing="1">PEDIR ORÇAMENTO</text>')
    return svg(w, h, o)


# ------------------------------------------------------------ usos errados
def erro(tipo, S=17, w=300, h=110):
    inner = f'<rect width="{w}" height="{h}" fill="{OSSO}"/>'
    if tipo == "esticar":
        m, _ = principal(0, 0, S)
        inner += f'<g transform="translate(22 {h/2-4}) scale(1.35 0.72)">{m}</g>'
    elif tipo == "listra_longa":
        lar = avanco("CASA BRASILEIRA ", S) + largura_tinta("DE AÇO", S)
        m = (f'<text x="22" y="{h/2}" font-family="{JURA}" font-weight="300" font-size="{S}" '
             f'fill="{TINTA}" letter-spacing="{S*TRACK:.2f}" xml:space="preserve">'
             f'CASA BRASILEIRA <tspan fill="{VERDE}">DE AÇO</tspan></text>')
        t = S * 0.140
        g = t * 0.34
        for i, c in enumerate(CORES):
            m += (f'<rect x="24" y="{h/2 + S*0.32 + i*(t+g):.1f}" width="{lar:.1f}" '
                  f'height="{t:.1f}" fill="{c}"/>')
        inner += m
    elif tipo == "cor_errada":
        m, _ = principal(22, h / 2, S, TINTA, "#B02418", ("#B02418", "#E08A00", "#5A2D82"))
        inner += m
    elif tipo == "girar":
        m, _ = principal(0, 0, S)
        inner += f'<g transform="translate({w/2} {h/2}) rotate(-9) translate(-{w/2-22} 0)">{m}</g>'
    elif tipo == "fundo_ruim":
        inner = f'<rect width="{w}" height="{h}" fill="{AMARELO}"/>'
        m, _ = principal(22, h / 2, S, TINTA, VERDE)
        inner += m
    elif tipo == "trocar_fonte":
        lar = largura_tinta("CASA BRASILEIRA", S)
        m = (f'<text x="22" y="{h/2}" font-family="Work Sans" font-weight="700" '
             f'font-size="{S}" fill="{TINTA}" letter-spacing="1" xml:space="preserve">'
             f'CASA BRASILEIRA <tspan fill="{VERDE}">DE AÇO</tspan></text>')
        t = S * 0.140
        g = t * 0.34
        for i, c in enumerate(CORES):
            m += (f'<rect x="24" y="{h/2 + S*0.32 + i*(t+g):.1f}" width="{lar*1.02:.1f}" '
                  f'height="{t:.1f}" fill="{c}"/>')
        inner += m
    # marca de proibido
    inner += (f'<circle cx="{w-40}" cy="{h-34}" r="15" fill="none" stroke="#C0392B" '
              f'stroke-width="2.4"/>'
              f'<line x1="{w-50}" y1="{h-24}" x2="{w-30}" y2="{h-44}" stroke="#C0392B" '
              f'stroke-width="2.4"/>')
    return svg(w, h, inner)
