# -*- coding: utf-8 -*-
"""Brandbook da Casa Brasileira de Aço — escrito por Théo Sampaio.

A marca não muda: cor, geometria e tipografia saem de kit.py e doc_svg.py
sem um decimal de diferença do que foi aprovado. Aqui muda o texto e a
ordem em que as coisas são contadas.
"""
import base64, os
import doc_svg as D
from bb_css import CSS as CSS_BRUTO
from bb_texto import (LIXO, NOMES, DIZ, NAO_DIZ, TROCAS, GLOSSARIO, PERGUNTAS,
                      PROMESSA, SUSTENTA, NAO_FACA)
import bb_svg as V
from kit import (VERDE, AMARELO, AZUL, BRANCO, OSSO, TINTA, CINZA, CINZA_2,
                 VAO, kern)

FDIR = "/root/.fonts"


def b64(n):
    with open(os.path.join(FDIR, n), "rb") as f:
        return base64.b64encode(f.read()).decode("ascii")


CSS = (CSS_BRUTO
       .replace("__JURA__", b64("Jura-Light.ttf"))
       .replace("__MONO__", b64("IBMPlexMono-Regular.ttf"))
       .replace("__WS__", b64("WorkSans-Regular.ttf"))
       .replace("__WSB__", b64("WorkSans-Bold.ttf"))
       .replace("__VERDE__", VERDE).replace("__AMARELO__", AMARELO)
       .replace("__AZUL__", AZUL).replace("__TINTA__", TINTA)
       .replace("__OSSO__", OSSO).replace("__CINZA__", CINZA)
       .replace("__CINZA2__", CINZA_2))


# --------------------------------------------------------------- montadores
def parte(n, rotulo, titulo, linha):
    return f"""
<section class="parte"><div class="wrap">
  <div class="num">{n}</div>
  <div class="rot">{rotulo}</div>
  <h2>{titulo}</h2>
  <p>{linha}</p>
</div></section>"""


_n = [0]


def cap(olho, titulo, corpo, larga=False):
    """O numero do capitulo e automatico: renumerar a mao ja deu erro tres vezes."""
    _n[0] += 1
    olho = f"{_n[0]:02d} · {olho}"
    w = "wrap-larga" if larga else "wrap"
    return f"""
<section><div class="{w}">
  <span class="olho">{olho}</span>
  <h2>{titulo}</h2>
  {corpo}
</div></section>"""


def indice(partes):
    linhas = "".join(
        f'<div class="ix"><span class="ix-n">{n}</span>'
        f'<span class="ix-t">{t}</span>'
        f'<span class="ix-l">{linha}</span></div>'
        for n, _, t, linha in partes)
    return f"""
<section><div class="wrap">
  <span class="olho">O caminho</span>
  <h2>Oito partes.</h2>
  <p class="entrada">As três primeiras são argumento. As cinco últimas são regra. Se
  você só vai ler uma, leia a seis.</p>
  <div class="indice">{linhas}</div>
</div></section>"""


def nao_faca(chave, titulo="Não faça"):
    itens = "".join(f"<li>{x}</li>" for x in NAO_FACA[chave])
    return (f'<div class="nfaca"><h4>{titulo}</h4><ul>{itens}</ul></div>')


def hex2rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))


def rgb2cmyk(r, g, b):
    if (r, g, b) == (0, 0, 0):
        return (0, 0, 0, 100)
    rf, gf, bf = r/255, g/255, b/255
    k = 1 - max(rf, gf, bf)
    if k >= 1:
        return (0, 0, 0, 100)
    return tuple(round(v*100) for v in
                 ((1-rf-k)/(1-k), (1-gf-k)/(1-k), (1-bf-k)/(1-k), k))


PALETA = [
    ("Verde Casa", VERDE, "DE AÇO, a listra de cima, botão, link. É a cor que assina."),
    ("Amarelo Ouro", AMARELO, "A listra do meio. Acento. Nunca texto sobre fundo claro."),
    ("Azul Profundo", AZUL, "A listra de baixo. Fundo institucional e a cor do caminhão."),
    ("Tinta", TINTA, "CASA BRASILEIRA e todo o texto corrido."),
    ("Papel", OSSO, "O fundo padrão. Branco puro é frio demais pra uma marca de obra."),
    ("Branco", BRANCO, "Fundo alternativo e a marca em reverso."),
]


def swatch(nome, hx, uso):
    r, g, b = hex2rgb(hx)
    c, m, y, k = rgb2cmyk(r, g, b)
    borda = "border:1px solid var(--linha);" if hx in (BRANCO, OSSO) else ""
    return f"""<div class="sw">
  <div class="chip" style="background:{hx};{borda}"></div>
  <div class="sw-nome">{nome}</div>
  <div class="sw-val">{hx.upper()}<br>RGB {r} · {g} · {b}<br>CMYK {c} · {m} · {y} · {k}</div>
  <div class="sw-uso">{uso}</div>
</div>"""


SELO = {"fora": ("fora", "no lixo"), "meio": ("fora", "quase"),
        "dentro": ("dentro", "de pé")}

LIXO_HTML = "".join(f"""<li>
  <div class="n">{n}</div>
  <div>
    <span class="selo {SELO[s][0]}">{SELO[s][1]}</span>
    <h4>{t}</h4>
    <p>{d}</p>
  </div></li>""" for n, s, t, d in LIXO)

NOMES_HTML = "".join(
    f'<tr><td>{n}</td><td class="{"" if ok else "x"}">'
    f'{"pode" if ok else "não dá"}</td><td>{d}</td></tr>'
    for n, ok, d in NOMES)

DIZ_HTML = "".join(f"<li>{x}</li>" for x in DIZ)
NAO_HTML = "".join(f"<li>{x}</li>" for x in NAO_DIZ)

TROCAS_HTML = "".join(f"""<div class="troca">
  <div class="par">
    <div class="antes"><div class="rot">como chegou</div>
      <div class="txt">{a}</div></div>
    <div class="depois"><div class="rot">como sai</div>
      <div class="txt">{b}</div></div>
  </div>
  <div class="por">{p}</div>
</div>""" for a, b, p in TROCAS)

GLOSS_HTML = "".join(f"""<div class="item">
  <div class="t">{t}</div><div class="d">{d}</div></div>""" for t, d in GLOSSARIO)

PERG_HTML = "".join(f"""<div class="pg">
  <div class="q">— {q}</div>
  <div class="r">{r}</div></div>""" for q, r in PERGUNTAS)

K = kern("DE AÇO")

PARTES = [
    ("01", "Parte um", "O negócio",
     "O que está sendo vendido aqui não é o que está escrito na nota fiscal."),
    ("02", "Parte dois", "O nome",
     "Ele já existia quando eu cheguei. Meu trabalho foi entender por que é bom."),
    ("03", "Parte três", "A ideia",
     "Um desenho que diz duas coisas ao mesmo tempo, sem contar piada."),
    ("04", "Parte quatro", "O lixo",
     "Todo brandbook finge que a marca nasceu pronta na terceira página do caderno. "
     "É mentira em todos eles."),
    ("05", "Parte cinco", "As peças",
     "A partir daqui é manual. Menos opinião, mais medida."),
    ("06", "Parte seis", "As regras",
     "Odeio manual de marca. Trabalhei doze anos com eles e nunca abri um por "
     "vontade própria. Então vou ser breve."),
    ("07", "Parte sete", "No mundo",
     "Onde tudo isso encosta em papel, chapa e tinta."),
    ("08", "Parte oito", "A voz",
     "Metade do que estraga marca de indústria não é o logo. É o texto."),
]
PARTE = {p[0]: p for p in PARTES}

import bb_caps as C

ERROS = [("esticar", "Esticar ou achatar"),
         ("listra_longa", "Estender a listra sob DE AÇO"),
         ("cor_errada", "Trocar as cores da listra"),
         ("girar", "Inclinar a assinatura"),
         ("fundo_ruim", "Fundo que anula o amarelo"),
         ("trocar_fonte", "Trocar a tipografia")]
ERROS_HTML = "".join(f'<figure class="err">{D.erro(k)}<figcaption>{v}</figcaption></figure>'
                     for k, v in ERROS)
PALETA_HTML = "".join(swatch(*s) for s in PALETA)

# ====================================================================== capa
CAPA = f"""
<section class="capa"><div class="wrap">
  <div class="capa-topo">BRANDBOOK · EDIÇÃO 1 · 2026</div>
  <div class="capa-meio">
    <div class="logo">{D.marca(64)}</div>
    <div class="capa-fio"></div>
    <div class="capa-titulo">Como esta marca foi feita,<br>e como não estragá-la.</div>
  </div>
  <div class="capa-pe">
    <span>Escrito por Théo Sampaio</span>
    <span>Corte e dobra de vergalhão</span>
    <span>São Paulo</span>
  </div>
</div></section>"""

AUTOR = """
<section><div class="wrap">
  <span class="olho">Antes de tudo</span>
  <h2>Quem escreveu isso.</h2>
  <div class="autor">
    <div class="cracha">
      <div class="nm">Théo Sampaio</div>
      <dl>
        <dt>Ofício</dt><dd>Publicitário. Estúdio de três pessoas na Vila Buarque.</dd>
        <dt>Antes</dt><dd>Dez anos escrevendo filme de banco e de cerveja em agência
          grande.</dd>
        <dt>Antes ainda</dt><dd>Balcão do depósito de material de construção do meu pai,
          em Contagem.</dd>
        <dt>Neste projeto</dt><dd>Sete meses. Oito tentativas. Cinco no lixo.</dd>
      </dl>
    </div>
    <div>
      <p class="entrada">Eu não sabia nada sobre vergalhão quando comecei. Sabia sobre o
      balcão, o que é diferente.</p>
      <p>Cresci ouvindo mestre de obras discutir preço de barra de aço com meu pai. Eu
      tinha treze anos e minha função era carregar. O que eu aprendi ali, sem querer, foi
      que aquele senhor de camisa suja não estava comprando material. Estava comprando não
      ter dor de cabeça na segunda-feira.</p>
      <p>Depois fui fazer publicidade e passei dez anos longe daquilo, escrevendo coisas
      bonitas para bancos. Este projeto foi a primeira vez em que as duas metades da minha
      vida se falaram.</p>
      <p>Escrevi cada linha deste documento. Onde tem opinião, é minha. Onde tem regra,
      ela está aqui porque eu já vi o estrago de não ter — em outros clientes, com outras
      marcas, sempre com alguém de pressa e um mouse na mão.</p>
      <p>Não tem “DNA da marca” aqui dentro. Não tem jornada, não tem ecossistema, não tem
      solução completa. Se alguma dessas palavras aparecer numa peça da Casa daqui pra
      frente, não fui eu.</p>
      <div class="firma">
        <div class="rubrica">Théo Sampaio</div>
        <div class="local">São Paulo · março de 2026</div>
      </div>
    </div>
  </div>
</div></section>"""

MANIFESTO = """
<section class="manifesto"><div class="wrap">
  <p>Aço é commodity.</p>
  <p>Barra de doze metros é <span class="destaque">igual em toda usina do país</span>.
  Mesma norma, mesma bitola, mesmo preço de tabela.</p>
  <p>A Casa não vende aço.</p>
  <p class="miudo">Vende a barra já cortada no tamanho da viga, já dobrada no formato do
  estribo, já contada e já etiquetada com a posição que o projeto pediu. Vende a serra que
  sai do canteiro e o pedaço de barra que não sobra no chão.</p>
</div></section>"""

FECHO = """
<section class="fecho"><div class="wrap">
  <span class="olho" style="color:var(--amarelo)">Fecho</span>
  <h2>O combinado.</h2>
  <p>Marca não é o logo. Marca é a soma de todas as vezes que alguém encostou na empresa:
  a etiqueta que chegou certa, o caminhão que estava limpo, a proposta sem erro de
  português, a barra que veio na medida.</p>
  <p>O logo é a assinatura embaixo disso. Ele não conserta nada e não promete nada
  sozinho. Serve para que todas essas vezes sejam reconhecidas como sendo da mesma
  gente.</p>
  <p>Uma etiqueta torta hoje sai mais barato de consertar que mil etiquetas tortas em
  cinco anos. É por isso que este documento tem tabela, número e uma regra que eu pedi de
  joelhos.</p>
  <p>Fiz a minha parte. As três listras param na tinta do A e não passam de lá.</p>
  <div class="firma">
    <div class="rubrica">Théo Sampaio</div>
    <div class="local">São Paulo · março de 2026 · edição 1</div>
  </div>
  <div class="colofao">CASA BRASILEIRA DE AÇO · BRANDBOOK · EDIÇÃO 1 · 2026 ·
  A MARCA NÃO MUDA SEM ESTA PÁGINA MUDAR JUNTO</div>
</div></section>"""

# ------------------------------------------------------------- capítulos com figura
C05 = C.C05_A + f"""
  <figure class="fig">{D.construcao()}
    <figcaption>A listra nasce da largura de tinta de CASA BRASILEIRA. Ela não foi
    desenhada por cima do nome: foi calculada a partir dele.</figcaption></figure>
"""

C03 = C.C03 + f"""
  <figure class="fig">{D.etiqueta()}
    <figcaption>A peça mais importante do sistema. Tudo aqui foi desenhado pra caber nela
    primeiro, e depois em todo o resto.</figcaption></figure>
"""

C08 = f"""
  <p class="entrada">Uma principal e três alternativas. Não são opções de gosto: cada uma
  resolve uma proporção de espaço diferente.</p>
  <figure class="fig">{D.marca(52)}
    <figcaption>Principal. É essa que se usa. As outras três existem para quando o espaço
    não deixar.</figcaption></figure>
  <div class="g2">
    <figure class="fig">{D.marca_alt("horizontal", 34)}
      <figcaption>Alternativa 1 · horizontal. Espaço largo e baixo, onde a principal
      ficaria pequena demais.</figcaption></figure>
    <figure class="fig">{D.marca_alt("vertical", 30)}
      <figcaption>Alternativa 2 · vertical. Espaço estreito e alto: banner lateral,
      lombada, sacola.</figcaption></figure>
    <figure class="fig">{D.marca_alt("uma_linha", 26)}
      <figcaption>Alternativa 3 · uma linha. Faixa muito baixa: cabeçalho de site, rodapé,
      assinatura de e-mail.</figcaption></figure>
    <figure class="fig" style="background:{AZUL};border-color:{AZUL}">
      {D.marca(30, AZUL, BRANCO, AMARELO, (BRANCO, AMARELO, BRANCO))}
      <figcaption style="color:#c9cbd2">Reversa. Sobre qualquer fundo escuro a listra vira
      branco, amarelo, branco.</figcaption></figure>
  </div>
  <p>Existe também o símbolo isolado, as três listras sozinhas em quadrado, para avatar de
  rede social, favicon e adesivo. Nesses lugares o nome aparece do lado, escrito pela
  própria plataforma. Em proposta, etiqueta, nota e placa de obra, não: três listras sem
  nome não se apresentam.</p>
"""

C11 = f"""
  <p class="entrada">A listra é calculada, não desenhada. Quem mudar o corpo ou a
  entreletra precisa recalcular a largura, senão ela desalinha do A.</p>
  <div class="rolagem"><table>
    <tr><th>Parâmetro</th><th>Valor</th><th>Observação</th></tr>
    <tr><td>Tipografia</td><td class="v">Jura Light</td><td>caixa alta</td></tr>
    <tr><td>Entreletra</td><td class="v">0,155 × corpo</td>
      <td>valor base, nas duas partes do nome</td></tr>
    <tr><td>Vão óptico</td><td class="v">{VAO:.3f} × corpo</td>
      <td>DE AÇO é corrigido par a par até bater com ele</td></tr>
    <tr><td>Espessura da listra</td><td class="v">0,140 × corpo</td>
      <td>as três iguais</td></tr>
    <tr><td>Respiro entre listras</td><td class="v">0,34 × espessura</td>
      <td>é ele que separa vergalhão de bandeira</td></tr>
    <tr><td>Topo da listra</td><td class="v">0,32 × corpo</td>
      <td>abaixo da linha de base</td></tr>
    <tr><td>Início da listra</td><td class="v">tinta do C</td>
      <td>não o avanço do glifo</td></tr>
    <tr><td>Fim da listra</td><td class="v">tinta do A</td>
      <td>último A de BRASILEIRA</td></tr>
    <tr><td>Cor de DE AÇO</td><td class="v">{VERDE}</td><td>sempre fora da listra</td></tr>
    <tr><td>Sobre fundo escuro</td><td class="v">branco · amarelo · branco</td>
      <td>o verde cai a 2,7:1 e o azul a 1,3:1</td></tr>
  </table></div>
  <h3>O detalhe que ninguém vê e todo mundo sente</h3>
  <p>A entreletra numérica é a mesma nas duas partes do nome. Mesmo assim, DE AÇO parecia
  mais solto que CASA BRASILEIRA. E estava: os glifos D, E, Ç e O têm lateral mais larga
  na Jura, então com o mesmo número o vão de tinta saía 8% maior.</p>
  <p>O que se iguala é o vão, não o número. Cada par de DE AÇO leva uma correção calculada
  a partir da lateral real do glifo: D-E {K[1]:+.3f}, espaço {K[2]:+.3f}, A-Ç {K[3]:+.3f},
  Ç-O {K[4]:+.3f}, em fração do corpo.</p>
  <p>Isso está aqui por um motivo prático. Se alguém redigitar o nome num editor em vez de
  usar os arquivos entregues, perde o ajuste. Use os arquivos.</p>
"""

C11B = f"""
  <p class="entrada">Duas perguntas que ninguém faz e todo mundo erra.</p>
  <h3>Respiro</h3>
  <p>Marca precisa de ar em volta. Não é frescura: logo colado na borda de um anúncio,
  ou encostado num bloco de texto, é a assinatura visual de quem não tem manual. Quem vê
  sente antes de saber o motivo.</p>
  <p>A medida é X, e X é a altura do conjunto das três listras. Um X de folga em todos os
  lados, sempre. Se está apertado e não cabe com o respiro, o problema não é o respiro. É
  o tamanho da marca naquele lugar.</p>
  <figure class="fig">{D.protecao()}
    <figcaption>X é a altura do conjunto das três listras. Respiro mínimo em volta: um X,
    dos quatro lados.</figcaption></figure>
  <h3>Escala</h3>
  <p>Corpo 15 px em tela. Corpo 9 mm impresso. Abaixo disso a espessura da listra fica
  menor que um pixel, as três cores se fundem e a marca vira uma mancha marrom. Fica
  ilegível, e fica feia de um jeito que parece defeito de impressão.</p>
  <p>Se você precisa de menor que isso, não diminua. Troque para a alternativa 3, que é
  mais baixa, ou use o símbolo com o nome escrito ao lado em texto normal. Encolher além
  do mínimo é a forma mais boba de estragar isso, porque ninguém decidiu — só foi
  acontecendo.</p>
  <figure class="fig">{D.escala()}
    <figcaption>Do maior ao menor. O quinto, em corpo 11, está abaixo do mínimo de
    propósito: é pra você ver o que acontece.</figcaption></figure>
"""

C12 = f"""
  <p class="entrada">Todas eu já vi acontecer. Nenhuma por má-fé: foi sempre alguém com
  pressa, um prazo e um mouse.</p>
  <div class="g3">{ERROS_HTML}</div>
  <p style="margin-top:1.8rem">A segunda é a grave. As outras cinco deixam a marca feia, e
  feio se conserta na próxima tiragem. Estender a listra sob DE AÇO desfaz a única regra
  de significado da identidade, e isso não se conserta: só se refaz.</p>
"""

C13 = f"""
  <p class="entrada">Quatro lugares onde a marca vive de verdade. Nenhum deles é
  apresentação.</p>
  <div class="g2">
    <figure class="fig">{D.etiqueta()}
      <figcaption>Etiqueta de romaneio. A peça número um do sistema: é ela que a pessoa
      que decide a recompra lê todo dia.</figcaption></figure>
    <figure class="fig">{D.frota()}
      <figcaption>Frota. Reversa sobre o azul institucional. O caminhão é o único outdoor
      que esta marca precisa ter.</figcaption></figure>
    <figure class="fig">{D.cartao()}
      <figcaption>Papelaria. Cartão e timbrado, para proposta e contrato.</figcaption></figure>
    <figure class="fig">{D.site()}
      <figcaption>Site. Cabeçalho e chamada. Uma frase, um botão.</figcaption></figure>
  </div>
"""


SUSTENTA_HTML = "".join(f"""<div class="prova">
  <div class="pn">{i+1:02d}</div>
  <div><h4>{t}</h4><p>{d}</p></div></div>"""
  for i, (t, d) in enumerate(SUSTENTA))

PROMESSA_HTML = f"""
<section class="promessa"><div class="wrap">
  <span class="olho" style="color:var(--amarelo)">A promessa</span>
  <p class="frase">{PROMESSA}</p>
  <p class="rodape-frase">Uma frase. Se ela não for verdade numa segunda-feira
  qualquer, nada aqui dentro salva a marca.</p>
</div></section>"""

C_SUSTENTA = C.C_SUSTENTA_A + f'<div class="provas">{SUSTENTA_HTML}</div>' + C.C_SUSTENTA_B

C_ESPECIMEN = C.C_ESPECIMEN + f"""
  <figure class="fig plain">{V.especimen()}</figure>
  <p class="nota" style="margin-top:1.6rem">Caixa alta sempre. Os acentos em verde
  não são enfeite: Ç, Ã e Õ são os caracteres que quebram fonte importada, e é por
  isso que eles estão aqui — para conferir antes de comprar licença de qualquer
  substituta. A última linha é a frase que a Casa escreve mais vezes por dia.</p>
"""

C_PLACA = C.C_COBRANDING_A + f"""
  <figure class="fig">{V.placa_obra()}
    <figcaption>A marca entra na faixa de fornecedores, no mesmo tamanho dos outros
    e menor que o nome da obra. Sair maior que a construtora é o caminho mais curto
    pra sair da placa.</figcaption></figure>
"""

C_COBRANDING = C.C_COBRANDING_B + f"""
  <figure class="fig">{V.cobranding()}
    <figcaption>Fio a 2X da marca, parceiro a 2X do fio. X é a altura do conjunto
    das três listras.</figcaption></figure>
"""

C_ARQUITETURA = C.C_ARQUITETURA_A + f"""
  <figure class="fig">{V.arquitetura()}</figure>
""" + C.C_ARQUITETURA_B

C_FIM = C.C_FIM + f"""
  <figure class="fig plain" style="margin-top:2.4rem">{V.frase()}</figure>
"""

# ====================================================================== corpo
BODY = "".join([
    CAPA, AUTOR, indice(PARTES), MANIFESTO, PROMESSA_HTML,
    parte(*PARTE["01"]),
    cap("a promessa", "Uma frase que dê pra cumprir.", C.C_PROMESSA),
    cap("o que a sustenta", "Quatro provas.", C_SUSTENTA),
    cap("o produto de verdade", "A barra deixa de ser genérica.", C.C01),
    cap("o problema honesto", "Ninguém se apaixona por vergalhão. Ótimo.", C.C02),
    cap("onde a marca mora", "Ela vive numa etiqueta suja.", C03),
    parte(*PARTE["02"]),
    cap("a palavra que salva o nome", "Casa não é casinha.",
        C.C04_A + NOMES_HTML + C.C04_B),
    parte(*PARTE["03"]),
    cap("o símbolo", "Um desenho, duas leituras.", C05),
    cap("a regra que carrega o significado", "Por que a listra para no A.", C.C06),
    parte(*PARTE["04"]),
    cap("oito tentativas", "O que eu joguei fora.",
        C.C07_A + LIXO_HTML + C.C07_B),
    parte(*PARTE["05"]),
    cap("a assinatura", "A marca e suas quatro formas.",
        C08 + nao_faca("peças"), larga=True),
    cap("a cor", "Cores do Brasil, em tom grave.",
        C.C09_A + PALETA_HTML + C.C09_B + f"""
        <h3>Quanto de cada uma</h3>
        <p>Ter a cor certa não basta: erra-se mais na dose que no tom. Uma peça da
        Casa é quase toda papel e tinta. As três cores da listra entram como acento,
        somando um sétimo do que se vê — e o amarelo é o menor de todos, porque é o
        mais barulhento.</p>
        <figure class="fig">{V.proporcao()}
          <figcaption>A dose, numa peça média. Não é lei de milímetro, é ordem de
          grandeza: se a sua peça está mais colorida que isto, ela está errada.
          </figcaption></figure>
        """ + nao_faca("cor")),
    cap("a tipografia", "Jura Light, e por que não as outras sete.", C.C10),
    cap("especímen", "A letra, no tamanho dela.", C_ESPECIMEN, larga=True),
    parte(*PARTE["06"]),
    cap("construção", "Dez linhas que geram a marca.", C11),
    cap("respiro e escala", "Onde ela encosta e até onde encolhe.", C11B),
    cap("uso incorreto", "Seis maneiras de estragar isso.", C12, larga=True),
    parte(*PARTE["07"]),
    cap("aplicações", "A marca em uso.", C13, larga=True),
    cap("placa de obra", "Onde a marca é fornecedor, não estrela.",
        C_PLACA, larga=True),
    cap("ao lado de outra marca", "A régua do co-branding.", C_COBRANDING),
    parte(*PARTE["08"]),
    cap("tom", "Como a Casa fala.",
        C.C14_A + DIZ_HTML + C.C14_B + NAO_HTML + C.C14_C),
    cap("na prática", "Antes e depois.",
        C.C15_A + TROCAS_HTML + nao_faca("voz")),
    cap("vocabulário", "Glossário do canteiro.",
        C.C16_A + GLOSS_HTML + "</div>"),
    cap("defesa", "Perguntas que vão te fazer.", C.C17_A + PERG_HTML),
    cap("o que vem depois", "Como nomear o próximo produto.",
        C_ARQUITETURA, larga=True),
    cap("a frase, de novo", "Sua obra não precisa de serra.", C_FIM, larga=True),
    FECHO,
])

TITULO = "Casa Brasileira de Aço — Brandbook"

HTML = f"""<!doctype html>
<html lang="pt-BR"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{TITULO}</title>
<meta name="author" content="Théo Sampaio">
<style>{CSS}</style>
</head><body>{BODY}</body></html>"""

open("CASA_BRASILEIRA_brandbook.html", "w", encoding="utf-8").write(HTML)
print("brandbook html:", len(HTML), "bytes")

ART = f"""<title>Casa Brasileira de Aço</title>
<style>{CSS}</style>
{BODY}"""
open("CASA_BRASILEIRA_brandbook_artifact.html", "w", encoding="utf-8").write(ART)
print("artifact:", len(ART), "bytes")
