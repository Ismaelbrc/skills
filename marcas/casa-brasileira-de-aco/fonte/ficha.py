# -*- coding: utf-8 -*-
"""Escreve a ficha tecnica legivel a partir do ESPECIFICACAO.json."""
import json

d = json.load(open("ESPECIFICACAO.json", encoding="utf-8"))
L = []
w = L.append

w("# CASA BRASILEIRA DE AÇO — ficha técnica da marca\n")
w(f"Identidade **{d['versao_da_identidade']} · {d['estado']}**. "
  f"{d['negocio'].capitalize()}.\n")
w("> Este arquivo é **gerado** por `fonte/spec.py` a partir do código que desenha")
w("> a marca. Não edite à mão: corrija o código e rode de novo, senão a ficha e")
w("> o desenho se separam.\n")
w("## Conceito\n")
w(d["conceito"] + "\n")
w(f"**Regra de ouro.** {d['regra_de_ouro']}\n")

w("## Cor\n")
w("| Nome | HEX | RGB | CMYK calculado | Uso |")
w("|---|---|---|---|---|")
for c in d["paleta"]:
    w(f"| {c['nome']} | `{c['hex']}` | {' · '.join(map(str, c['rgb']))} | "
      f"{' · '.join(map(str, c['cmyk_calculado']))} | {c['uso']} |")
w("")
w("⚠️ " + d["nota_sobre_cor"] + "\n")

w("## Tipografia\n")
t = d["tipografia"]
w(f"- **{t['familia']} {t['peso']}** — {t['caixa']}")
w(f"- arquivo `{t['arquivo']}`, {t['unidades_por_em']} unidades por em")
w(f"- versão `{t['versao']}`")
w(f"- licença: {t['licenca']}")
w(f"- SHA-256 da fonte: `{t['sha256']}`")
w(f"- texto corrido: {t['apoio']['texto_corrido']}")
w(f"- dados e legendas: {t['apoio']['dados_e_legendas']}")
w(f"- descartadas no caminho: {', '.join(t['descartadas'])}\n")
w("O SHA-256 acima existe para um motivo: se alguém no futuro instalar outra")
w("Jura e o desenho mudar, é assim que se descobre. Os arquivos em `marca/`")
w("já estão em curvas e não dependem da fonte.\n")

w("## Geometria\n")
g = d["geometria"]
w(f"*{g['unidade']}.*\n")
w("| Parâmetro | Valor |")
w("|---|---|")
w(f"| Entreletra base | {g['entreletra_base']} |")
w(f"| Vão óptico alvo | {g['vao_optico_alvo']} |")
w(f"| Vão de palavra | {g['vao_de_palavra']} |")
li = g["listra"]
w(f"| Espessura da listra | {li['espessura']} |")
w(f"| Respiro entre listras | {li['respiro_entre_listras']} |")
w(f"| Topo da listra abaixo da base | {li['topo_abaixo_da_base']} |")
w(f"| Início da listra | {li['inicio']} |")
w(f"| Fim da listra | {li['fim']} |")
w(f"| Listra nunca | {li['nunca']} |")
lg = g["larguras_no_corpo_1"]
for kk, vv in lg.items():
    w(f"| {kk.replace('_', ' ')} (corpo 1) | {vv} |")
ap = g["area_de_protecao"]
w(f"| X | {ap['X']} |")
w(f"| Respiro mínimo em volta | {ap['respiro_minimo_em_volta']} |")
em = g["escala_minima"]
w(f"| Mínimo em tela | {em['tela_px']} px de corpo |")
w(f"| Mínimo impresso | {em['impresso_mm']} mm de corpo |")
w("")

a = g["ajuste_optico_de_aco"]
w("### Ajuste óptico de DE AÇO\n")
w(a["por_que"] + "\n")
w("| Par | Correção (fração do corpo) |")
w("|---|---|")
for kk in ("D-E", "espaco_DE_ACO", "A-C_cedilha", "C_cedilha-O"):
    w(f"| {kk.replace('_', ' ')} | {a[kk]:+.4f} |")
w("")
bl = g["bloco_de_listras_solto"]
w("### Bloco de listras solto\n")
w(f"Usado em {bl['onde']}. Comprimento {bl['comprimento']}; "
  f"espessura {bl['espessura']}; respiro {bl['respiro']}.\n")

w("## Composições\n")
for kk, v in d["composicoes"].items():
    w(f"**{kk}** — `{v['arquivo']}`  ")
    w(f"{v['descricao']}. {v['uso']}\n")

w("## Versões de cor\n")
for kk, v in d["versoes_de_cor"].items():
    w(f"- **{kk}** — {v}")
w("")

w("## Formatos\n")
for kk, v in d["formatos_entregues"].items():
    w(f"- **{kk}** — {v}")
w("")

w("## Nunca\n")
for x in d["proibido"]:
    w(f"- {x}")
w("")

inv = d["inventario"]
w("## Inventário\n")
w(f"{len(inv)} arquivos. O SHA-256 de cada um está em `ESPECIFICACAO.json` e em")
w("`SHA256SUMS.txt`. Para conferir se um arquivo que circulou por aí ainda é o")
w("original:\n")
w("```")
w("sha256sum -c SHA256SUMS.txt")
w("```\n")
w("### Assinaturas em vetor\n")
w("| Arquivo | viewBox |")
w("|---|---|")
for i in inv:
    if i["arquivo"].endswith(".svg"):
        w(f"| `{i['arquivo'].split('/')[-1]}` | {i['viewbox']} |")
w("")

open("ESPECIFICACAO.md", "w", encoding="utf-8").write("\n".join(L))
print("ESPECIFICACAO.md ·", len("\n".join(L)), "bytes")

# manifesto de checksums, formato do sha256sum
linhas = [f"{i['sha256']}  {i['arquivo']}" for i in inv]
open("SHA256SUMS.txt", "w", encoding="utf-8").write("\n".join(linhas) + "\n")
print("SHA256SUMS.txt ·", len(linhas), "linhas")
