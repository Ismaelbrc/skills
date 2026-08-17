# -*- coding: utf-8 -*-
"""Monta o documento: defesa + manual de marca, HTML autocontido."""
import base64, os
import doc_svg as D
from kit import (VERDE, AMARELO, AZUL, BRANCO, OSSO, TINTA, CINZA, CINZA_2,
                 CORES, largura_tinta, avanco)

FDIR = "/root/.fonts"


def b64(nome):
    with open(os.path.join(FDIR, nome), "rb") as f:
        return base64.b64encode(f.read()).decode("ascii")


JURA_B = b64("Jura-Light.ttf")
MONO_B = b64("IBMPlexMono-Regular.ttf")
WS_B = b64("WorkSans-Regular.ttf")
WSB_B = b64("WorkSans-Bold.ttf")


# ------------------------------------------------------------------ cores
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
    c = (1-rf-k)/(1-k); m = (1-gf-k)/(1-k); y = (1-bf-k)/(1-k)
    return tuple(round(v*100) for v in (c, m, y, k))


PALETA = [
    ("Verde Casa", VERDE, "cor principal · DE AÇO, listra superior, botões"),
    ("Amarelo Ouro", AMARELO, "listra do meio · acento, nunca texto sobre claro"),
    ("Azul Profundo", AZUL, "listra inferior · fundo institucional, frota"),
    ("Tinta", TINTA, "CASA BRASILEIRA e texto corrido"),
    ("Papel", OSSO, "fundo claro padrão"),
    ("Branco", BRANCO, "fundo alternativo e marca reversa"),
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


PALETA_HTML = "".join(swatch(*s) for s in PALETA)

# ------------------------------------------------------------- percurso
PERCURSO = [
    ("01", "descartado", "Letras de vergalhão",
     "Um alfabeto autoral em que cada letra era uma barra dobrada, com a nervura "
     "deformando o contorno. Tecnicamente correto, visualmente errado: lia como fonte "
     "rústica, não como precisão industrial."),
    ("02", "descartado", "Casa de uma barra",
     "Uma casa traçada por uma única barra contínua. Clichê de construtora — contorno "
     "de casinha é território de milhares de marcas."),
    ("03", "descartado", "Estribo como emblema",
     "O produto do setor virando brasão. Um retângulo com ganchos lê como moldura "
     "genérica para quem não é do ramo."),
    ("04", "descartado", "Monograma CBA",
     "Barrado por pesquisa: CBA é a Companhia Brasileira de Alumínio, do Grupo "
     "Votorantim, listada na B3. Colidir com uma marca estabelecida em setor vizinho "
     "de metais seria erro grave."),
    ("05", "descartado", "O Ç com gancho",
     "O cedilha desenhado como o gancho a 90° que a NBR especifica para estribos. "
     "Conceito sólido, execução rejeitada."),
    ("06", "base", "Três barras",
     "As cores do Brasil como três barras paralelas. A primeira versão ainda lia como "
     "bandeira: grossas demais e juntas demais."),
    ("07", "aprovado", "A calibragem",
     "Afinar e afastar as barras foi o que separou as duas leituras. Com respiro entre "
     "elas, deixam de ser faixa de bandeira e passam a ser vergalhões alinhados."),
    ("08", "aprovado", "A listra sob o nome",
     "A composição final: a listra vive sob CASA BRASILEIRA e termina na tinta do A "
     "final. DE AÇO fica livre, em verde."),
]

PERC_HTML = "".join(f"""<li>
  <div class="p-num">{n}</div>
  <div>
    <span class="tag {'ok' if s in ('aprovado','base') else ''}">{s}</span>
    <h4>{t}</h4>
    <p>{d}</p>
  </div></li>""" for n, s, t, d in PERCURSO)

# ------------------------------------------------------------- usos errados
ERROS = [
    ("esticar", "Esticar ou achatar"),
    ("listra_longa", "Estender a listra sob DE AÇO"),
    ("cor_errada", "Trocar as cores da listra"),
    ("girar", "Inclinar a assinatura"),
    ("fundo_ruim", "Fundo que anula o amarelo"),
    ("trocar_fonte", "Trocar a tipografia"),
]
ERROS_HTML = "".join(f'<figure class="err">{D.erro(k)}<figcaption>{v}</figcaption></figure>'
                     for k, v in ERROS)

# ------------------------------------------------------------------ voz
VOZ = [
    ("DIRETO", "Medida, prazo e quantidade. Sem adjetivo de folheto.",
     "“48 estribos, posição N5, entrega quarta.”"),
    ("TÉCNICO SEM ARROGÂNCIA", "Usa a língua da obra — romaneio, posição, bitola — "
     "sem transformar isso em jargão de vendedor.",
     "“Chega etiquetado por posição.”"),
    ("A FAVOR DE QUEM RECEBE", "Fala do ganho no canteiro, não da máquina que temos.",
     "“Menos perda, menos serra na obra.”"),
    ("BRASILEIRO SEM UFANISMO", "A brasilidade está na cor e no nome. O texto não "
     "precisa repetir isso.",
     "“Aço brasileiro, cortado aqui.”"),
]
VOZ_HTML = "".join(f"""<div class="voz">
  <div class="dot"></div><h4>{t}</h4><p>{d}</p><div class="ex">{e}</div></div>"""
                   for t, d, e in VOZ)

CSS = """
@font-face{font-family:'Jura';src:url(data:font/ttf;base64,__JURA__) format('truetype');font-weight:300;font-display:swap}
@font-face{font-family:'PlexMono';src:url(data:font/ttf;base64,__MONO__) format('truetype');font-weight:400;font-display:swap}
@font-face{font-family:'WorkSans';src:url(data:font/ttf;base64,__WS__) format('truetype');font-weight:400;font-display:swap}
@font-face{font-family:'WorkSans';src:url(data:font/ttf;base64,__WSB__) format('truetype');font-weight:700;font-display:swap}

:root{
  --verde:__VERDE__; --amarelo:__AMARELO__; --azul:__AZUL__;
  --tinta:__TINTA__; --papel:__OSSO__; --branco:#fff;
  --cinza:__CINZA__; --cinza2:__CINZA2__; --linha:#dcdad3;
  --display:'Jura','WorkSans',sans-serif;
  --corpo:'WorkSans',-apple-system,sans-serif;
  --mono:'PlexMono',ui-monospace,monospace;
  --wrap:1080px;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}
 *{animation-duration:.001ms!important;transition-duration:.001ms!important}}

body{margin:0;background:var(--papel);color:var(--tinta);
 font-family:var(--corpo);font-size:16px;line-height:1.62;-webkit-font-smoothing:antialiased}
::selection{background:var(--verde);color:#fff}

.wrap{max-width:var(--wrap);margin:0 auto;padding-inline:clamp(1.4rem,5vw,3rem)}
section{padding-block:clamp(3.2rem,7vw,5.6rem);border-top:1px solid var(--linha)}
section:first-of-type{border-top:none}

.eyebrow{font-family:var(--mono);font-size:.74rem;letter-spacing:.24em;
 text-transform:uppercase;color:var(--verde);display:block;margin-bottom:.9rem}
h1,h2,h3,h4{margin:0;font-weight:400;text-wrap:balance}
h2{font-family:var(--display);font-weight:300;font-size:clamp(1.9rem,4.4vw,3rem);
 letter-spacing:.06em;margin-bottom:1.4rem}
h3{font-family:var(--display);font-weight:300;font-size:clamp(1.3rem,2.6vw,1.8rem);
 letter-spacing:.05em;margin:2.6rem 0 .7rem}
h4{font-family:var(--corpo);font-weight:700;font-size:1rem;margin-bottom:.3rem}
p{margin:0 0 1rem;max-width:66ch}
strong{font-weight:700}
.lead{font-size:clamp(1.05rem,1.7vw,1.2rem);color:var(--cinza2);max-width:62ch}
.small{font-family:var(--mono);font-size:.78rem;color:var(--cinza2);letter-spacing:.04em}

/* capa */
.capa{min-height:88svh;display:flex;flex-direction:column;justify-content:center;
 gap:2.4rem;border-top:none}
.capa .logo{max-width:760px}
.capa .meta{font-family:var(--mono);font-size:.8rem;letter-spacing:.18em;color:var(--cinza2)}
.capa .rule{height:1px;background:var(--linha);margin-block:.4rem}

/* blocos de figura */
figure{margin:0}
.fig{background:var(--branco);border:1px solid var(--linha);padding:clamp(1.2rem,3vw,2.2rem);
 margin-block:1.6rem}
.fig.plain{background:transparent;border:none;padding:0}
figcaption{font-family:var(--mono);font-size:.76rem;color:var(--cinza2);
 letter-spacing:.06em;margin-top:.7rem}

.grid2{display:grid;grid-template-columns:repeat(2,1fr);gap:clamp(1rem,2.4vw,1.8rem)}
.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:clamp(1rem,2.4vw,1.8rem)}
@media(max-width:760px){.grid2,.grid3{grid-template-columns:1fr}}

/* paleta */
.paleta{display:grid;grid-template-columns:repeat(3,1fr);gap:1.4rem;margin-top:1.8rem}
@media(max-width:760px){.paleta{grid-template-columns:repeat(2,1fr)}}
@media(max-width:460px){.paleta{grid-template-columns:1fr}}
.chip{height:104px;margin-bottom:.7rem}
.sw-nome{font-weight:700;font-size:.95rem}
.sw-val{font-family:var(--mono);font-size:.76rem;color:var(--cinza2);
 line-height:1.55;margin-top:.2rem;font-variant-numeric:tabular-nums}
.sw-uso{font-size:.84rem;color:var(--cinza2);margin-top:.4rem}

/* percurso */
.percurso{list-style:none;margin:1.6rem 0 0;padding:0;border-top:1px solid var(--linha)}
.percurso li{display:grid;grid-template-columns:3.6rem 1fr;gap:1.4rem;
 padding-block:1.3rem;border-bottom:1px solid var(--linha)}
.p-num{font-family:var(--mono);font-size:.85rem;color:var(--verde);padding-top:.15rem}
.tag{display:inline-block;font-family:var(--mono);font-size:.66rem;letter-spacing:.13em;
 text-transform:uppercase;border:1px solid var(--linha);border-radius:2px;
 padding:.1rem .5rem;color:var(--cinza2);margin-bottom:.45rem}
.tag.ok{border-color:var(--verde);color:var(--verde)}
.percurso p{margin:0;color:var(--cinza2)}

/* erros */
.err svg{display:block}
.err figcaption{color:#9d3226}

/* voz */
.voz .dot{width:7px;height:7px;border-radius:50%;background:var(--verde);margin-bottom:.7rem}
.voz p{color:var(--cinza2);margin-bottom:.7rem}
.voz .ex{font-family:var(--display);font-weight:300;font-size:1.15rem;color:var(--verde);
 letter-spacing:.03em}

/* tabela de regras */
table{width:100%;border-collapse:collapse;margin-top:1.2rem;font-size:.9rem}
th,td{text-align:left;padding:.62rem .5rem;border-bottom:1px solid var(--linha);
 vertical-align:top}
th{font-family:var(--mono);font-size:.72rem;letter-spacing:.12em;text-transform:uppercase;
 color:var(--cinza2);font-weight:400}
td.v{font-family:var(--mono);color:var(--verde);white-space:nowrap;
 font-variant-numeric:tabular-nums}

.callout{border-left:2px solid var(--verde);padding:.2rem 0 .2rem 1.2rem;margin-block:1.6rem}
.callout p:last-child{margin-bottom:0}

footer{padding-block:3rem 4rem;text-align:center;font-family:var(--mono);
 font-size:.74rem;letter-spacing:.1em;color:var(--cinza2);border-top:1px solid var(--linha)}

@media print{
  @page{size:A4;margin:15mm 14mm 16mm}
  /* a folha e estreita, mas as grades do impresso nao colapsam */
  .grid2{grid-template-columns:repeat(2,1fr)}
  .grid3{grid-template-columns:repeat(3,1fr)}
  .paleta{grid-template-columns:repeat(3,1fr);gap:1rem}
  body{-webkit-print-color-adjust:exact;print-color-adjust:exact;font-size:10pt;
   line-height:1.55}
  .wrap{max-width:none;padding-inline:0}

  /* um capitulo por folha */
  section{padding-block:0 1.4rem;break-before:page;border-top:none}
  h2{break-after:avoid;font-size:1.55rem;margin-bottom:.9rem}
  h3{break-after:avoid;font-size:1.1rem;margin:1.5rem 0 .5rem}
  .lead{font-size:1.02rem}
  p{max-width:none}

  /* capa ocupa a folha inteira */
  .capa{min-height:238mm;break-before:auto;break-inside:avoid;padding-block:0;
   border-top:none;justify-content:center}
  .capa .logo{max-width:100%}

  .fig{margin-block:1rem;padding:1rem}
  .chip{height:62px}
  .percurso{margin-top:.9rem}
  .percurso li{padding-block:.36rem;gap:1rem;grid-template-columns:2.4rem 1fr}
  .percurso h4{font-size:.92rem;margin-bottom:.12rem}
  .percurso p{font-size:.83rem;line-height:1.4}
  .percurso .tag{font-size:.6rem;padding:.05rem .4rem;margin-bottom:.18rem}
  .tag{margin-bottom:.25rem}
  table{font-size:.84rem;margin-top:.9rem}
  th,td{padding:.42rem .4rem}
  .fig,.sw,.percurso li,.err,.voz>div,table,figure,.callout{break-inside:avoid}
  footer{padding-block:1.6rem 0;break-inside:avoid}
}
"""

CSS = (CSS.replace("__JURA__", JURA_B).replace("__MONO__", MONO_B)
          .replace("__WS__", WS_B).replace("__WSB__", WSB_B)
          .replace("__VERDE__", VERDE).replace("__AMARELO__", AMARELO)
          .replace("__AZUL__", AZUL).replace("__TINTA__", TINTA)
          .replace("__OSSO__", OSSO).replace("__CINZA__", CINZA)
          .replace("__CINZA2__", CINZA_2))

# ------------------------------------------------------------------ corpo
S = 64
lar_listra = largura_tinta("CASA BRASILEIRA", S)
lar_total = avanco("CASA BRASILEIRA ", S) + largura_tinta("DE AÇO", S)

BODY = f"""
<section class="capa"><div class="wrap">
  <div class="logo">{D.marca(64)}</div>
  <div class="rule"></div>
  <div class="meta">DEFESA DE MARCA &amp; MANUAL DE IDENTIDADE · VERSÃO 1.0 · 2026</div>
</div></section>

<section><div class="wrap">
  <span class="eyebrow">01 · O negócio</span>
  <h2>Corte e dobra não vende aço.</h2>
  <p class="lead">Vende a peça certa, na medida certa, na quantidade certa — e já
  identificada.</p>
  <p>A barra sai da usina com 12 metros e é genérica: serve para qualquer obra. Depois do
  corte e dobra ela deixa de ser genérica. Vira a <strong>posição N5</strong> de uma viga
  específica, de um projeto específico, com comprimento, bitola e formato definidos pelo
  cálculo estrutural.</p>
  <p>Essa transformação é o produto. O cliente não está comprando aço — está comprando a
  eliminação do corte e da dobra dentro do canteiro: menos perda de ponta de barra, menos
  serra e bancada na obra, menos erro de medida, menos tempo.</p>
  <div class="callout">
    <p><strong>O ponto de contato real da marca é a etiqueta.</strong> Cada peça ou feixe
    chega na obra com obra, elemento, romaneio, desenho, posição, bitola, formato e
    quantidade. É ali que a marca é vista todo dia — não em outdoor.</p>
  </div>
</div></section>

<section><div class="wrap">
  <span class="eyebrow">02 · O nome</span>
  <h2>Casa é instituição, não moradia.</h2>
  <p>“Casa” aqui tem o sentido de estabelecimento especializado — como Casa da Moeda.
  Casa Brasileira de Aço é a casa do aço: o lugar que domina o assunto. Essa leitura muda
  o registro da marca inteira. Não pede telhado nem casinha; pede autoridade.</p>

  <h3>O que a pesquisa de nome mostrou</h3>
  <table>
    <tr><th>Nome</th><th>Situação</th></tr>
    <tr><td>Aço Brasileiro</td><td>Genérico — descreve literalmente aço feito no Brasil.
      Registro frágil no INPI e impossível de defender contra concorrentes.</td></tr>
    <tr><td>Aço Brasil</td><td>Ocupado. Existe como distribuidora e, mais sério, é o nome
      do Instituto Aço Brasil, entidade da indústria siderúrgica nacional.</td></tr>
    <tr><td>CBA</td><td>Ocupado. É a Companhia Brasileira de Alumínio, do Grupo
      Votorantim, listada na B3 (CBAV3). Por isso a marca <strong>não</strong> usa
      monograma de iniciais.</td></tr>
    <tr><td>Casa Brasileira de Aço</td><td>Distintivo. “Casa” dá ao conjunto a
      particularidade que “Aço Brasileiro” não teria.</td></tr>
  </table>
  <p class="small" style="margin-top:1rem">Busca em fontes públicas não substitui a
  consulta formal ao INPI. Antes de registrar, verificar nas classes NCL 6 (produtos de
  metal) e NCL 40 (tratamento de materiais).</p>
</div></section>

<section><div class="wrap">
  <span class="eyebrow">03 · O símbolo</span>
  <h2>Três barras, duas leituras.</h2>
  <p>As cores do Brasil na ordem da bandeira — verde, amarelo, azul — desenhadas como três
  barras paralelas. Para quem olha rápido, é a bandeira: diz <strong>Casa Brasileira</strong>.
  Para quem é do ramo, são três vergalhões alinhados: diz <strong>de Aço</strong>. As duas
  leituras cabem no mesmo desenho, sem ilustração e sem metáfora forçada.</p>

  <h3>A calibragem é o conceito</h3>
  <p>Barras grossas e encostadas leem como faixa de bandeira. Com espessura reduzida e
  respiro entre elas, passam a ler como barras separadas. Não é ajuste estético — é o que
  decide qual das duas leituras domina.</p>

  <figure class="fig">{D.construcao()}
    <figcaption>A listra é calculada a partir da largura de tinta de CASA BRASILEIRA.</figcaption></figure>

  <h3>Por que a listra para no A</h3>
  <p>A listra vive sob <strong>CASA BRASILEIRA</strong> e termina na tinta do A final.
  <strong>DE AÇO</strong> fica fora dela, em verde. A razão é de significado: as cores do
  Brasil sublinham exatamente a parte brasileira do nome. Estendê-las sob “DE AÇO”
  dissolveria essa relação e devolveria a marca ao território de bandeira.</p>
</div></section>

<section><div class="wrap">
  <span class="eyebrow">04 · A tipografia</span>
  <h2>Jura Light.</h2>
  <p>Geométrica, de desenho quase instrumental, e fina. Foi escolhida entre oito
  alternativas — incluindo Italiana, Poiret One, Outfit, Work Sans e Arsenal SC — por ser a
  única que entrega sofisticação sem sair do registro técnico.</p>
  <p>Italiana era mais elegante, mas seu contraste alto pertence a moda e joalheria.
  Poiret One era fina demais para placa de frota e bordado. As grotescas neutras não
  erravam, mas também não marcavam.</p>
  <div class="callout">
    <p>Em caixa alta e bem rastreada, a Jura Light dá ao nome a cadência de uma inscrição —
    o que serve a uma marca que se chama “Casa”.</p>
  </div>
</div></section>

<section><div class="wrap">
  <span class="eyebrow">05 · A cor</span>
  <h2>Cores do Brasil, em tom grave.</h2>
  <p>A paleta não usa os valores oficiais da bandeira, e essa é uma decisão deliberada.
  Os oficiais — verde #009C3B, amarelo #FFDF00, azul #002776 — puxam a marca para o
  registro esportivo. Os tons desta identidade são mais escuros e mais quentes: mantêm a
  leitura “Brasil” e ganham peso industrial.</p>
  <p>Há também uma razão física. Amarelo puro tem luminância altíssima: sobre fundo claro
  ele praticamente desaparece. O #F2B705 desta paleta resolve o problema no próprio tom, em
  vez de exigir contorno ou sombra.</p>
  <div class="paleta">{PALETA_HTML}</div>
  <p class="small" style="margin-top:1.4rem">Conversão de tela para impressão é sempre
  aproximada. Para pintura de frota e impressão offset, fechar o Pantone equivalente com a
  gráfica a partir do CMYK acima.</p>
</div></section>

<section class="quebra"><div class="wrap">
  <span class="eyebrow">06 · O percurso</span>
  <h2>Oito passos até aqui.</h2>
  <p class="lead">Nada disso saiu certo de primeira. O registro abaixo é o que foi testado,
  o que foi descartado e por quê.</p>
  <ol class="percurso">{PERC_HTML}</ol>
</div></section>

<section class="quebra"><div class="wrap">
  <span class="eyebrow">07 · Assinatura</span>
  <h2>A marca e suas versões.</h2>
  <figure class="fig">{D.marca(58)}
    <figcaption>Principal · listra sob CASA BRASILEIRA</figcaption></figure>
  <div class="grid2">
    <figure class="fig">{D.marca_alt("horizontal", 30)}
      <figcaption>Alternativa 1 · horizontal</figcaption></figure>
    <figure class="fig">{D.marca_alt("vertical", 26)}
      <figcaption>Alternativa 2 · vertical</figcaption></figure>
    <figure class="fig">{D.marca_alt("uma_linha", 26)}
      <figcaption>Alternativa 3 · uma linha</figcaption></figure>
    <figure class="fig" style="background:{AZUL};border-color:{AZUL}">
      {D.marca(30, None, BRANCO, AMARELO, (BRANCO, AMARELO, BRANCO))}
      <figcaption style="color:#b9c4d4">Reversa · fundo institucional</figcaption></figure>
  </div>
</div></section>

<section class="quebra"><div class="wrap">
  <span class="eyebrow">08 · Construção</span>
  <h2>As regras que geram a marca.</h2>
  <p>A listra é <strong>calculada</strong>, não desenhada. Quem mudar o corpo ou o
  entreletra precisa recalcular a largura — senão ela desalinha do A.</p>
  <table>
    <tr><th>Parâmetro</th><th>Valor</th><th>Observação</th></tr>
    <tr><td>Tipografia</td><td class="v">Jura Light</td><td>caixa alta</td></tr>
    <tr><td>Entreletra</td><td class="v">0,155 × corpo</td><td>igual nas duas partes do nome</td></tr>
    <tr><td>Espessura da listra</td><td class="v">0,140 × corpo</td><td>as três iguais</td></tr>
    <tr><td>Respiro entre listras</td><td class="v">0,34 × espessura</td><td></td></tr>
    <tr><td>Topo da listra</td><td class="v">0,32 × corpo</td><td>abaixo da linha de base</td></tr>
    <tr><td>Início da listra</td><td class="v">tinta do C</td><td>não o avanço do glifo</td></tr>
    <tr><td>Fim da listra</td><td class="v">tinta do A</td><td>último A de BRASILEIRA</td></tr>
    <tr><td>Cor de DE AÇO</td><td class="v">{VERDE}</td><td>sempre fora da listra</td></tr>
  </table>

  <h3>Área de proteção</h3>
  <figure class="fig">{D.protecao()}
    <figcaption>X = altura do conjunto das três listras. Respiro mínimo em volta = X.</figcaption></figure>

  <h3>Escala</h3>
  <figure class="fig">{D.escala()}
    <figcaption>Mínimo recomendado: corpo 15 px em tela, 9 mm impresso. Abaixo disso a
    listra fecha e as três cores viram uma mancha.</figcaption></figure>
</div></section>

<section><div class="wrap">
  <span class="eyebrow">09 · Uso incorreto</span>
  <h2>O que não fazer.</h2>
  <p>Seis desvios que quebram a marca. O segundo é o mais importante: estender a listra sob
  “DE AÇO” desfaz a única regra de significado da identidade.</p>
  <div class="grid3">{ERROS_HTML}</div>
</div></section>

<section class="quebra"><div class="wrap">
  <span class="eyebrow">10 · Aplicações</span>
  <h2>A marca em uso.</h2>
  <div class="grid2">
    <figure class="fig">{D.etiqueta()}
      <figcaption>Etiqueta de romaneio · o ponto de contato diário</figcaption></figure>
    <figure class="fig">{D.frota()}
      <figcaption>Frota · versão reversa sobre azul</figcaption></figure>
    <figure class="fig">{D.cartao()}
      <figcaption>Papelaria · cartão e timbrado</figcaption></figure>
    <figure class="fig">{D.site()}
      <figcaption>Site · cabeçalho e chamada</figcaption></figure>
  </div>
</div></section>

<section><div class="wrap">
  <span class="eyebrow">11 · Tom de voz</span>
  <h2>Como a Casa fala.</h2>
  <div class="grid2">{VOZ_HTML}</div>
</div></section>

<footer>CASA BRASILEIRA DE AÇO · DEFESA DE MARCA E MANUAL DE IDENTIDADE · VERSÃO 1.0 · 2026</footer>
"""

HTML = f"""<!doctype html>
<html lang="pt-BR"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Casa Brasileira de Aço — Defesa &amp; Manual de Marca</title>
<style>{CSS}</style>
</head><body>{BODY}</body></html>"""

with open("CASA_BRASILEIRA_manual.html", "w", encoding="utf-8") as f:
    f.write(HTML)
print("html:", len(HTML), "bytes")

# ------------------------------------------------- versao para publicacao
# O host embrulha o arquivo em <html><head><body>, entao aqui vai so o miolo.
ART = f"""<title>Casa Brasileira de Aço</title>
<style>{CSS}</style>
{BODY}"""

with open("CASA_BRASILEIRA_manual_artifact.html", "w", encoding="utf-8") as f:
    f.write(ART)
print("artifact:", len(ART), "bytes")
