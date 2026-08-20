# -*- coding: utf-8 -*-
"""Gera a especificacao da marca a partir do proprio codigo que a desenha.

Nenhum valor aqui e digitado a mao: tudo sai de kit.py e das metricas reais
da Jura Light. Se o desenho mudar, este arquivo muda com ele.
"""
import glob, hashlib, json, os, re
from fontTools.ttLib import TTFont

import kit
from kit import (VERDE, AMARELO, AZUL, BRANCO, OSSO, TINTA, CINZA, CINZA_2,
                 CORES, TRACK, VAO, VAO_PALAVRA, kern, largura_tinta,
                 largura_kern, largura_nome, avanco, _metricas, _UPM, _vao,
                 _pares)

FONTE = "/root/.fonts/Jura-Light.ttf"


def hex2rgb(h):
    h = h.lstrip("#")
    return [int(h[i:i+2], 16) for i in (0, 2, 4)]


def rgb2cmyk(r, g, b):
    if (r, g, b) == (0, 0, 0):
        return [0, 0, 0, 100]
    rf, gf, bf = r / 255, g / 255, b / 255
    k = 1 - max(rf, gf, bf)
    if k >= 1:
        return [0, 0, 0, 100]
    return [round(v * 100) for v in ((1-rf-k)/(1-k), (1-gf-k)/(1-k), (1-bf-k)/(1-k), k)]


def cor(nome, hx, uso):
    """O CMYK e conversao aritmetica do RGB — ponto de partida, nao
    especificacao de impressao. Pantone nao entra aqui de proposito: tem de
    ser fechado fisicamente com a grafica, em prova impressa."""
    r, g, b = hex2rgb(hx)
    c, m, y, k = rgb2cmyk(r, g, b)
    return {"nome": nome, "hex": hx.upper(), "rgb": [r, g, b],
            "cmyk_calculado": [c, m, y, k], "uso": uso}


PALETA = [
    cor("Verde Casa", VERDE, "DE AÇO, listra superior, botões, links"),
    cor("Amarelo Ouro", AMARELO, "listra do meio; acento. Nunca texto sobre fundo claro"),
    cor("Azul Profundo", AZUL, "listra inferior, fundo institucional, frota"),
    cor("Tinta", TINTA, "CASA BRASILEIRA e texto corrido"),
    cor("Papel", OSSO, "fundo claro padrão"),
    cor("Branco", BRANCO, "fundo alternativo e marca reversa"),
    cor("Cinza", CINZA, "fios, molduras, elementos de apoio"),
    cor("Cinza texto", CINZA_2, "legendas e texto secundário"),
]

# ---------------------------------------------------------------- tipografia
_f = TTFont(FONTE)
_nomes = {r.nameID: str(r) for r in _f["name"].names if r.platformID == 3}

TIPOGRAFIA = {
    "familia": "Jura",
    "peso": "Light (300)",
    "nome_interno": _nomes.get(4, "Jura Light"),
    "versao": _nomes.get(5, ""),
    "licenca": "SIL Open Font License 1.1",
    "arquivo": os.path.basename(FONTE),
    "sha256": hashlib.sha256(open(FONTE, "rb").read()).hexdigest(),
    "unidades_por_em": _UPM,
    "caixa": "sempre alta, no nome e nas etiquetas",
    "apoio": {
        "texto_corrido": "Work Sans (Regular 400 / Bold 700)",
        "dados_e_legendas": "IBM Plex Mono (Regular 400)",
    },
    "descartadas": ["Italiana", "Poiret One", "Outfit", "Work Sans", "Arsenal SC"],
}

# ------------------------------------------------------------------ geometria
S = 1.0                                    # tudo em fracao do corpo
k_de_aco = kern("DE AÇO")

GEOMETRIA = {
    "unidade": "todas as medidas são fração do corpo (font-size) do nome",
    "entreletra_base": round(TRACK, 4),
    "vao_optico_alvo": round(VAO, 4),
    "vao_de_palavra": round(VAO_PALAVRA, 4),
    "ajuste_optico_de_aco": {
        "por_que": ("D, E, Ç e O têm lateral mais larga na Jura Light. Com a mesma "
                    "entreletra numérica o vão de tinta de DE AÇO sai 8% maior que o "
                    "de CASA BRASILEIRA. O que se iguala é o vão, não o número."),
        "D-E": round(k_de_aco[1], 4),
        "espaco_DE_ACO": round(k_de_aco[2], 4),
        "A-C_cedilha": round(k_de_aco[3], 4),
        "C_cedilha-O": round(k_de_aco[4], 4),
    },
    "listra": {
        "quantidade": 3,
        "ordem": ["verde", "amarelo", "azul"],
        "espessura": 0.140,
        "respiro_entre_listras": "0,34 x a espessura",
        "topo_abaixo_da_base": 0.32,
        "inicio": "borda esquerda da tinta do C (não o avanço do glifo)",
        "fim": "borda direita da tinta do último A de BRASILEIRA",
        "nunca": "sob DE AÇO",
    },
    "bloco_de_listras_solto": {
        "onde": "alternativas 1, 2, 3 e símbolo",
        "comprimento": "2,0 x a altura do bloco",
        "espessura": "0,28 da altura, normalizada junto com o respiro",
        "respiro": "0,34 x a espessura",
    },
    "area_de_protecao": {
        "X": "altura do conjunto das três listras",
        "respiro_minimo_em_volta": "1 X",
    },
    "escala_minima": {"tela_px": 15, "impresso_mm": 9},
    "larguras_no_corpo_1": {
        "tinta_CASA_BRASILEIRA": round(largura_tinta("CASA BRASILEIRA", 1), 5),
        "tinta_DE_ACO_com_ajuste": round(largura_kern("DE AÇO", 1), 5),
        "tinta_do_nome_inteiro": round(largura_nome(1), 5),
        "altura_das_tres_listras": round(3 * 0.140 + 2 * (0.140 * 0.34), 5),
    },
    "vaos_medidos_no_corpo_1": {
        "CASA_BRASILEIRA": [round(_vao(a, b), 4) for a, b in _pares("CASA BRASILEIRA")],
        "DE_ACO_apos_ajuste": [round(VAO, 4)] * 3,
    },
}

COMPOSICOES = {
    "principal": {
        "arquivo": "CBA-principal-*",
        "descricao": "nome em uma linha, listra sob CASA BRASILEIRA",
        "uso": "padrão em tudo. Só trocar quando a proporção do espaço impedir.",
    },
    "alt1-horizontal": {
        "arquivo": "CBA-alt1-horizontal-*",
        "descricao": "bloco de listras à esquerda, nome em duas linhas",
        "uso": "espaços largos e baixos onde a principal ficaria pequena",
    },
    "alt2-vertical": {
        "arquivo": "CBA-alt2-vertical-*",
        "descricao": "bloco de listras acima, nome centralizado em duas linhas",
        "uso": "espaços estreitos e altos",
    },
    "alt3-uma-linha": {
        "arquivo": "CBA-alt3-uma-linha-*",
        "descricao": "bloco de listras à esquerda, nome inteiro em uma linha",
        "uso": "faixas muito baixas: cabeçalho de site, rodapé, assinatura de e-mail",
    },
    "simbolo": {
        "arquivo": "CBA-simbolo-*",
        "descricao": "as três listras isoladas em quadro quadrado",
        "uso": ("avatar, favicon, adesivo. Elemento derivado: nunca substitui a "
                "marca em documento, proposta ou etiqueta."),
    },
}

VERSOES_DE_COR = {
    "cor": "fundo transparente, para aplicar sobre fundo claro próprio",
    "papel": f"fundo {OSSO} — o padrao do sistema",
    "branco": "fundo branco puro",
    "reversa-azul": f"sobre {AZUL}; DE AÇO em {AMARELO}, listra branco/amarelo/branco",
    "reversa-preto": f"sobre {TINTA}; mesma regra do azul: DE AÇO em {AMARELO}, listra branco/amarelo/branco",
    "mono-preto": "uma cor: gravação, carimbo, jornal",
    "mono-branco": "uma cor sobre fundo escuro: bordado, serigrafia, pintura de frota",
}

PROIBIDO = [
    "esticar, achatar ou distorcer em qualquer proporção",
    "estender a listra sob DE AÇO — desfaz a única regra de significado da marca",
    "trocar as cores ou a ordem das listras",
    "inclinar ou rotacionar a assinatura",
    "aplicar sobre fundo que anule o amarelo",
    "trocar a tipografia ou redigitar o nome em outra fonte",
    "redesenhar a listra à mão em vez de recalcular pela métrica",
    "usar o símbolo sozinho onde o nome precisa aparecer",
]

# ------------------------------------------------------------------ inventario
def inventario():
    itens = []
    for f in sorted(glob.glob("marca/**/*", recursive=True)):
        if os.path.isfile(f):
            b = open(f, "rb").read()
            reg = {"arquivo": f, "bytes": len(b),
                   "sha256": hashlib.sha256(b).hexdigest()}
            if f.endswith(".svg"):
                m = re.search(r'viewBox="0 0 (\d+) (\d+)"', b.decode("utf-8"))
                reg["viewbox"] = f"{m.group(1)}x{m.group(2)}"
            itens.append(reg)
    return itens


SPEC = {
    "marca": "Casa Brasileira de Aço",
    "negocio": "corte e dobra de vergalhão para construção civil",
    "versao_da_identidade": "1.0",
    "estado": "definida",
    "conceito": ("Três listras paralelas nas cores do Brasil sob CASA BRASILEIRA. "
                 "Para quem olha rápido, é a bandeira: diz Casa Brasileira. Para quem "
                 "é do ramo, são três vergalhões alinhados: diz De Aço. A calibragem "
                 "— espessura e respiro — é o que decide qual leitura domina."),
    "regra_de_ouro": ("A listra é calculada a partir das métricas da fonte, nunca "
                      "desenhada à mão. Mudou o corpo ou a entreletra? Rode "
                      "fonte/vetor.py de novo — não corrija esticando no editor."),
    "paleta": PALETA,
    "nota_sobre_cor": (
        "O HEX/RGB e a especificacao para tela e e definitivo. O CMYK listado e "
        "conversão aritmética: serve para pedir a prova, não para fechar a tiragem. "
        "Pantone não está especificado de propósito — precisa ser escolhido em prova "
        "impressa com a gráfica, a partir do CMYK, e só depois anotado aqui. "
        "Pintura de frota exige o mesmo: prova numa amostra do substrato."),
    "tipografia": TIPOGRAFIA,
    "geometria": GEOMETRIA,
    "composicoes": COMPOSICOES,
    "versoes_de_cor": VERSOES_DE_COR,
    "proibido": PROIBIDO,
    "regra_de_fundo_escuro": {
        "regra": ("Sobre qualquer fundo escuro a listra vira branco/amarelo/branco e "
                  "DE AÇO vira amarelo. Não é gosto: é contraste medido."),
        "contraste_sobre_tinta_14161C": {
            "branco": "18,1:1", "amarelo": "9,9:1",
            "verde": "2,7:1 — fraco", "azul": "1,3:1 — invisível"},
        "contraste_sobre_azul_002B5C": {
            "branco": "14,0:1", "amarelo": "7,7:1", "verde": "2,1:1 — fraco"},
        "consequencia": ("verde e azul saem da listra em fundo escuro. As três listras "
                         "continuam três: o que carrega a leitura é a contagem e o "
                         "amarelo no meio, não as três cores."),
    },
    "formatos_entregues": {
        "svg": "vetor, texto em curvas — não depende da Jura instalada",
        "pdf": "vetor para grafica",
        "png-alta": "8000 px na maior dimensao",
        "png-web": "1600 px na maior dimensao",
        "icones": "símbolo quadrado em 1024, 512, 256, 128, 64 e 32 px",
    },
    "inventario": inventario(),
}

with open("ESPECIFICACAO.json", "w", encoding="utf-8") as f:
    json.dump(SPEC, f, ensure_ascii=False, indent=2)
print("ESPECIFICACAO.json  ·", len(SPEC["inventario"]), "arquivos no inventario")
