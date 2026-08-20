# -*- coding: utf-8 -*-
"""Figuras novas do brandbook. Não tocam na marca: só a usam."""
from kit import (VERDE, AMARELO, AZUL, BRANCO, OSSO, TINTA, CINZA, CINZA_2,
                 CORES, JURA, MONO, largura_tinta, largura_nome, principal,
                 _metricas, _UPM)
from doc_svg import svg


# ------------------------------------------------------ proporção de cor
PROPORCAO = [
    ("Papel", OSSO, 56, TINTA),
    ("Tinta", TINTA, 30, OSSO),
    ("Verde", VERDE, 8, BRANCO),
    ("Azul", AZUL, 4, BRANCO),
    ("Amarelo", AMARELO, 2, TINTA),
]


def proporcao(w=980, h=150):
    """Quanto de cada cor entra numa peça. A soma é 100."""
    barra_h = 74
    y = 8
    x = 0.0
    o = ""
    for nome, cor, pct, tinta in PROPORCAO:
        lar = w * pct / 100
        o += f'<rect x="{x:.1f}" y="{y}" width="{lar:.1f}" height="{barra_h}" fill="{cor}"/>'
        if cor == OSSO:
            o += (f'<rect x="{x+0.5:.1f}" y="{y+0.5}" width="{lar-1:.1f}" '
                  f'height="{barra_h-1}" fill="none" stroke="{CINZA}" '
                  f'stroke-width="1" opacity="0.5"/>')
        if pct >= 8:
            o += (f'<text x="{x+12:.1f}" y="{y+30}" font-family="{MONO}" font-size="13" '
                  f'fill="{tinta}" letter-spacing="1.5">{pct}%</text>'
                  f'<text x="{x+12:.1f}" y="{y+50}" font-family="{MONO}" font-size="11" '
                  f'fill="{tinta}" opacity="0.75">{nome}</text>')
        else:
            o += (f'<text x="{x+lar/2:.1f}" y="{y+barra_h+20}" font-family="{MONO}" '
                  f'font-size="11" fill="{CINZA_2}" text-anchor="middle">{pct}%</text>'
                  f'<text x="{x+lar/2:.1f}" y="{y+barra_h+36}" font-family="{MONO}" '
                  f'font-size="10" fill="{CINZA_2}" text-anchor="middle">{nome}</text>')
        x += lar
    return svg(w, h, o)


# ---------------------------------------------------------- co-branding
def cobranding(w=980, h=230):
    """A marca ao lado de outra. A régua é X, a altura das três listras."""
    S = 30
    t = S * 0.140
    X = 3 * t + 2 * (t * 0.34)
    base = 96
    x0 = 30
    m, _ = principal(x0, base, S)
    lar_marca = largura_nome(S)
    fio_x = x0 + lar_marca + X * 2
    o = f'<rect width="{w}" height="{h}" fill="{BRANCO}"/>'
    o += m
    # fio divisor
    o += (f'<line x1="{fio_x:.1f}" y1="{base-S*0.78:.1f}" x2="{fio_x:.1f}" '
          f'y2="{base+S*0.55:.1f}" stroke="{CINZA}" stroke-width="1"/>')
    # caixa do parceiro
    px = fio_x + X * 2
    o += (f'<rect x="{px:.1f}" y="{base-S*0.78:.1f}" width="150" '
          f'height="{S*1.33:.1f}" fill="none" stroke="{CINZA}" stroke-width="1" '
          f'stroke-dasharray="5 4"/>')
    o += (f'<text x="{px+75:.1f}" y="{base-S*0.05:.1f}" font-family="{MONO}" '
          f'font-size="11" fill="{CINZA_2}" text-anchor="middle">logo do parceiro</text>')
    # cotas
    g = VERDE
    for a, b, rot in ((x0 + lar_marca, fio_x, "2X"), (fio_x, px, "2X")):
        ym = base + S * 1.15
        o += (f'<line x1="{a:.1f}" y1="{ym:.1f}" x2="{b:.1f}" y2="{ym:.1f}" '
              f'stroke="{g}" stroke-width="1"/>'
              f'<line x1="{a:.1f}" y1="{ym-4:.1f}" x2="{a:.1f}" y2="{ym+4:.1f}" '
              f'stroke="{g}" stroke-width="1"/>'
              f'<line x1="{b:.1f}" y1="{ym-4:.1f}" x2="{b:.1f}" y2="{ym+4:.1f}" '
              f'stroke="{g}" stroke-width="1"/>'
              f'<text x="{(a+b)/2:.1f}" y="{ym+18:.1f}" font-family="{MONO}" '
              f'font-size="11" fill="{g}" text-anchor="middle">{rot}</text>')
    o += (f'<text x="{x0}" y="{h-22}" font-family="{MONO}" font-size="11" '
          f'fill="{CINZA_2}">X = altura do conjunto das três listras · a marca vem '
          f'sempre à esquerda do fio</text>')
    return svg(w, h, o)


def placa_obra(w=980, h=530):
    """Placa de obra: a marca dividindo espaço com construtora e projetista."""
    o = f'<rect width="{w}" height="{h}" fill="{OSSO}"/>'
    # a placa
    px, py, pw, ph = 60, 40, w - 120, h - 130
    o += f'<rect x="{px}" y="{py}" width="{pw}" height="{ph}" fill="{BRANCO}" stroke="{CINZA}" stroke-width="1"/>'
    o += f'<rect x="{px}" y="{py}" width="{pw}" height="82" fill="{AZUL}"/>'
    o += (f'<text x="{px+34}" y="{py+50}" font-family="{JURA}" font-weight="300" '
          f'font-size="30" fill="{BRANCO}" letter-spacing="4">RESIDENCIAL VILA NOVA</text>')
    # o miolo da placa, como numa placa real
    dados = [("INCORPORAÇÃO", "—"), ("EXECUÇÃO", "—"),
             ("RESP. TÉCNICO", "CREA 0000000000"), ("ALVARÁ", "0000/2026")]
    for i, (kk, vv) in enumerate(dados):
        dy = py + 156 + i * 32
        o += (f'<text x="{px+34}" y="{dy}" font-family="{MONO}" font-size="11" '
              f'fill="{CINZA_2}" letter-spacing="1.4">{kk}</text>'
              f'<text x="{px+220}" y="{dy}" font-family="{MONO}" font-size="11" '
              f'fill="{CINZA}">{vv}</text>')
    # faixa de fornecedores
    fy = py + ph - 116
    o += (f'<line x1="{px}" y1="{fy}" x2="{px+pw}" y2="{fy}" stroke="{CINZA}" '
          f'stroke-width="1" opacity="0.6"/>')
    o += (f'<text x="{px+34}" y="{fy-28}" font-family="{MONO}" font-size="12" '
          f'fill="{CINZA_2}" letter-spacing="2">ARMADURA CORTADA E DOBRADA POR</text>')
    m, _ = principal(px + 34, fy + 48, 19)
    o += m
    # dois parceiros
    for i, rot in enumerate(("CONSTRUTORA", "PROJETO ESTRUTURAL")):
        cx = px + 420 + i * 250
        o += (f'<rect x="{cx}" y="{fy+18}" width="200" height="46" fill="none" '
              f'stroke="{CINZA}" stroke-width="1" stroke-dasharray="5 4"/>')
        o += (f'<text x="{cx+100}" y="{fy+46}" font-family="{MONO}" font-size="10" '
              f'fill="{CINZA_2}" text-anchor="middle" letter-spacing="1">{rot}</text>')
    return svg(w, h, o)


# ------------------------------------------------- arquitetura de marca
def arquitetura(w=980, h=300):
    """Como nomear o que vem depois."""
    o = ""
    S = 22
    m, _ = principal(30, 46, S)
    o += m
    o += (f'<line x1="30" y1="88" x2="{w-30}" y2="88" stroke="{CINZA}" '
          f'stroke-width="1" opacity="0.5"/>')
    filhos = [("CORTE E DOBRA", "o produto de hoje", True),
              ("TELAS", "se um dia existir", True),
              ("TRELIÇA", "se um dia existir", True),
              ("CASA DIGITAL", "não", False)]
    for i, (nome, obs, ok) in enumerate(filhos):
        x = 30 + i * 236
        cor = VERDE if ok else "#9d3226"
        o += (f'<line x1="{x+8}" y1="88" x2="{x+8}" y2="122" stroke="{CINZA}" '
              f'stroke-width="1" opacity="0.5"/>')
        o += (f'<text x="{x+8}" y="146" font-family="{JURA}" font-weight="300" '
              f'font-size="17" fill="{TINTA}" letter-spacing="2.2">{nome}</text>')
        o += (f'<text x="{x+8}" y="168" font-family="{MONO}" font-size="11" '
              f'fill="{cor}">{obs}</text>')
    o += (f'<text x="30" y="228" font-family="{MONO}" font-size="12" fill="{CINZA_2}">'
          f'O nome do produto vem depois da marca, em Jura Light, e descreve o que '
          f'é — nunca inventa nome próprio.</text>')
    o += (f'<text x="30" y="252" font-family="{MONO}" font-size="12" fill="{CINZA_2}">'
          f'“Casa Brasileira de Aço · Telas” funciona. “Casa Digital” cria uma '
          f'segunda marca para cuidar, e ninguém aqui tem tempo pra isso.</text>')
    return svg(w, h, o)


# ------------------------------------------------------- especímen tipográfico
def especimen(w=980):
    """O jogo de caracteres que a marca usa de verdade, no tamanho em que se enxerga
    o desenho da letra."""
    linhas = [
        (58, TINTA, 0.055, "ABCDEFGHIJKLM"),
        (58, TINTA, 0.055, "NOPQRSTUVWXYZ"),
        (58, VERDE, 0.055, "ÇÃÕÁÉÍÓÚÊÔÀ"),
        (44, CINZA_2, 0.070, "0123456789 Ø × ° · , /"),
    ]
    o = ""
    y = 0.0
    for S, cor, tr, txt in linhas:
        y += S * 1.02
        o += (f'<text x="0" y="{y:.1f}" font-family="{JURA}" font-weight="300" '
              f'font-size="{S}" fill="{cor}" letter-spacing="{S*tr:.2f}">{txt}</text>')
        y += S * 0.34
    # a frase, no corpo em que a marca respira
    y += 26
    o += (f'<line x1="0" y1="{y:.1f}" x2="{w}" y2="{y:.1f}" stroke="{CINZA}" '
          f'stroke-width="1" opacity="0.4"/>')
    y += 74
    o += (f'<text x="0" y="{y:.1f}" font-family="{JURA}" font-weight="300" '
          f'font-size="54" fill="{TINTA}" letter-spacing="3.2">'
          f'ESTRIBO 90° · Ø 10,0 mm · CA-50</text>')
    y += 34
    o += (f'<text x="0" y="{y:.1f}" font-family="{MONO}" font-size="12" '
          f'fill="{CINZA_2}">a linha que a marca escreve mais vezes por dia</text>')
    return svg(w, round(y + 16), o)


def frase(w=980, S=86):
    """A promessa em corpo grande, para a pagina de fecho."""
    linhas = [("SUA OBRA", TINTA), ("NÃO PRECISA", TINTA),
              ("DE LIXADEIRA", VERDE)]
    o = ""
    y = 0.0
    for txt, cor in linhas:
        y += S * 1.06
        o += (f'<text x="0" y="{y:.1f}" font-family="{JURA}" font-weight="300" '
              f'font-size="{S}" fill="{cor}" letter-spacing="{S*0.06:.2f}">{txt}</text>')
        y += S * 0.10
    return svg(w, round(y + S * 0.22), o)
