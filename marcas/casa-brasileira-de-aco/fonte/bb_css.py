# -*- coding: utf-8 -*-
"""CSS do brandbook. Mesma marca, documento editorial."""

CSS = """
@font-face{font-family:'Jura';src:url(data:font/ttf;base64,__JURA__) format('truetype');font-weight:300;font-display:swap}
@font-face{font-family:'PlexMono';src:url(data:font/ttf;base64,__MONO__) format('truetype');font-weight:400;font-display:swap}
@font-face{font-family:'WorkSans';src:url(data:font/ttf;base64,__WS__) format('truetype');font-weight:400;font-display:swap}
@font-face{font-family:'WorkSans';src:url(data:font/ttf;base64,__WSB__) format('truetype');font-weight:700;font-display:swap}

:root{
  --verde:__VERDE__; --amarelo:__AMARELO__; --azul:__AZUL__;
  --tinta:__TINTA__; --papel:__OSSO__; --branco:#fff;
  --cinza:__CINZA__; --cinza2:__CINZA2__; --linha:#dcdad3;
  --linha-esc:#33363d;
  --display:'Jura','WorkSans',sans-serif;
  --corpo:'WorkSans',-apple-system,sans-serif;
  --mono:'PlexMono',ui-monospace,monospace;
  --wrap:1020px;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}

body{margin:0;background:var(--papel);color:var(--tinta);
 font-family:var(--corpo);font-size:17px;line-height:1.66;
 -webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility}
::selection{background:var(--verde);color:#fff}

.wrap{max-width:var(--wrap);margin:0 auto;padding-inline:clamp(1.4rem,5vw,3.2rem)}
.wrap-larga{max-width:1240px;margin:0 auto;padding-inline:clamp(1.4rem,5vw,3.2rem)}
section{padding-block:clamp(3rem,6.5vw,5.4rem)}

/* ---------------------------------------------------------- tipografia */
h1,h2,h3,h4{margin:0;font-weight:400;text-wrap:balance}
h2{font-family:var(--display);font-weight:300;font-size:clamp(1.85rem,4.2vw,2.9rem);
 letter-spacing:.05em;line-height:1.12;margin-bottom:1.5rem}
h3{font-family:var(--display);font-weight:300;font-size:clamp(1.25rem,2.4vw,1.7rem);
 letter-spacing:.045em;margin:2.8rem 0 .8rem}
h4{font-family:var(--corpo);font-weight:700;font-size:.98rem;margin-bottom:.25rem}
p{margin:0 0 1.15rem;max-width:62ch}
p:last-child{margin-bottom:0}
strong{font-weight:700}
em{font-style:italic}
a{color:var(--verde)}

.olho{font-family:var(--mono);font-size:.72rem;letter-spacing:.24em;
 text-transform:uppercase;color:var(--verde);display:block;margin-bottom:1rem}
.entrada{font-size:clamp(1.1rem,1.8vw,1.32rem);line-height:1.5;color:var(--tinta);
 max-width:44ch;font-family:var(--display);font-weight:300;letter-spacing:.02em;
 margin-bottom:1.8rem}
.nota{font-family:var(--mono);font-size:.78rem;color:var(--cinza2);letter-spacing:.03em}
.curta{max-width:46ch}

/* ------------------------------------------------------------- a capa */
.capa{min-height:92svh;display:flex;flex-direction:column;justify-content:space-between;
 padding-block:clamp(2rem,6vw,4rem)}
.capa-topo{font-family:var(--mono);font-size:.74rem;letter-spacing:.2em;color:var(--cinza2)}
.capa-meio .logo{max-width:820px}
.capa-fio{height:1px;background:var(--linha);margin-block:2rem 1.2rem}
.capa-titulo{font-family:var(--display);font-weight:300;
 font-size:clamp(1.5rem,3.6vw,2.4rem);letter-spacing:.05em;line-height:1.15}
.capa-pe{font-family:var(--mono);font-size:.76rem;letter-spacing:.12em;color:var(--cinza2);
 display:flex;flex-wrap:wrap;gap:.4rem 2rem}

/* ------------------------------------------------ abertura de parte */
.parte{background:var(--tinta);color:var(--papel);min-height:64svh;
 display:flex;flex-direction:column;justify-content:center}
.parte .num{font-family:var(--display);font-weight:300;line-height:.8;
 font-size:clamp(6rem,17vw,12rem);color:var(--verde);letter-spacing:-.02em}
.parte .rot{font-family:var(--mono);font-size:.74rem;letter-spacing:.26em;
 text-transform:uppercase;color:var(--amarelo);margin-top:1.4rem}
.parte h2{color:var(--papel);font-size:clamp(2rem,5.6vw,3.6rem);margin:.6rem 0 0}
.parte p{color:#b9bbc0;max-width:48ch;margin-top:1.6rem}

/* ------------------------------------------------------- manifesto */
.manifesto{background:var(--tinta);color:var(--papel)}
.manifesto p{font-family:var(--display);font-weight:300;
 font-size:clamp(1.5rem,3.9vw,2.7rem);line-height:1.22;letter-spacing:.02em;
 max-width:30ch;margin-bottom:1.5rem}
.manifesto p.miudo{font-family:var(--corpo);font-size:clamp(1rem,1.5vw,1.12rem);
 line-height:1.6;max-width:52ch;color:#b9bbc0;letter-spacing:0}
.manifesto .destaque{color:var(--amarelo)}

/* -------------------------------------------------------- assinatura */
.autor{display:grid;grid-template-columns:1fr 1.35fr;gap:clamp(1.6rem,4vw,3.4rem);
 align-items:start}
@media(max-width:760px){.autor{grid-template-columns:1fr}}
.autor .cracha{border:1px solid var(--linha);background:var(--branco);padding:1.6rem}
.autor .cracha .nm{font-family:var(--display);font-weight:300;font-size:1.5rem;
 letter-spacing:.05em}
.autor .cracha dl{margin:1.2rem 0 0;font-family:var(--mono);font-size:.76rem;
 line-height:1.7;color:var(--cinza2)}
.autor .cracha dt{color:var(--verde);letter-spacing:.1em;text-transform:uppercase;
 font-size:.66rem;margin-top:.8rem}
.autor .cracha dd{margin:0}
.firma{margin-top:2.6rem;padding-top:1.4rem;border-top:1px solid var(--linha)}
.firma .rubrica{font-family:var(--display);font-weight:300;font-size:1.7rem;
 letter-spacing:.06em}
.firma .local{font-family:var(--mono);font-size:.74rem;color:var(--cinza2);
 letter-spacing:.1em;margin-top:.3rem}

/* ---------------------------------------------------------- citação */
.citacao{border-left:2px solid var(--verde);padding:.2rem 0 .2rem 1.5rem;
 margin-block:2.2rem}
.citacao p{font-family:var(--display);font-weight:300;
 font-size:clamp(1.2rem,2.3vw,1.6rem);line-height:1.35;letter-spacing:.02em;
 max-width:38ch}
.citacao .quem{font-family:var(--mono);font-size:.74rem;color:var(--cinza2);
 letter-spacing:.08em;margin-top:.7rem}

/* --------------------------------------------------------- figuras */
figure{margin:0}
.fig{background:var(--branco);border:1px solid var(--linha);
 padding:clamp(1.1rem,2.6vw,2rem);margin-block:1.7rem}
figcaption{font-family:var(--mono);font-size:.74rem;color:var(--cinza2);
 letter-spacing:.05em;margin-top:.8rem;line-height:1.5}
.g2{display:grid;grid-template-columns:repeat(2,1fr);gap:clamp(1rem,2.2vw,1.7rem)}
.g3{display:grid;grid-template-columns:repeat(3,1fr);gap:clamp(1rem,2.2vw,1.7rem)}
@media(max-width:760px){.g2,.g3{grid-template-columns:1fr}}

/* ---------------------------------------------------------- paleta */
.paleta{display:grid;grid-template-columns:repeat(3,1fr);gap:1.5rem;margin-top:2rem}
@media(max-width:760px){.paleta{grid-template-columns:repeat(2,1fr)}}
@media(max-width:440px){.paleta{grid-template-columns:1fr}}
.chip{height:110px;margin-bottom:.8rem}
.sw-nome{font-weight:700;font-size:.95rem}
.sw-val{font-family:var(--mono);font-size:.74rem;color:var(--cinza2);
 line-height:1.6;margin-top:.2rem;font-variant-numeric:tabular-nums}
.sw-uso{font-size:.86rem;color:var(--cinza2);margin-top:.45rem;line-height:1.5}

/* ------------------------------------------------------------- lixo */
.lixo{list-style:none;margin:1.8rem 0 0;padding:0}
.lixo li{display:grid;grid-template-columns:3.2rem 1fr;gap:1.4rem;
 padding-block:1.4rem;border-top:1px solid var(--linha)}
.lixo li:last-child{border-bottom:1px solid var(--linha)}
.lixo .n{font-family:var(--mono);font-size:.82rem;color:var(--cinza2);padding-top:.2rem}
.lixo p{margin:.35rem 0 0;color:var(--cinza2);max-width:58ch}
.selo{display:inline-block;font-family:var(--mono);font-size:.62rem;letter-spacing:.14em;
 text-transform:uppercase;padding:.12rem .5rem;border:1px solid;border-radius:2px;
 margin-bottom:.5rem}
.selo.fora{color:#9d3226;border-color:#d8b3ac}
.selo.dentro{color:var(--verde);border-color:var(--verde)}

/* ------------------------------------------------------------ tabela */
/* tabela larga rola dentro do proprio quadro; a pagina nunca rola de lado */
.rolagem{overflow-x:auto;margin-top:1.4rem;-webkit-overflow-scrolling:touch}
.rolagem table{margin-top:0}
table{width:100%;border-collapse:collapse;margin-top:1.4rem;font-size:.9rem;
 min-width:30rem}
th,td{text-align:left;padding:.65rem .5rem;border-bottom:1px solid var(--linha);
 vertical-align:top}
th{font-family:var(--mono);font-size:.7rem;letter-spacing:.12em;text-transform:uppercase;
 color:var(--cinza2);font-weight:400}
td.v{font-family:var(--mono);color:var(--verde);white-space:nowrap;
 font-variant-numeric:tabular-nums}
td.x{color:#9d3226}

/* -------------------------------------------------------- diz/não diz */
.fala{display:grid;grid-template-columns:1fr 1fr;gap:0;margin-top:1.8rem;
 border:1px solid var(--linha);background:var(--branco)}
@media(max-width:640px){.fala{grid-template-columns:1fr}}
.fala>div{padding:1.4rem 1.5rem}
.fala>div+div{border-left:1px solid var(--linha)}
@media(max-width:640px){.fala>div+div{border-left:none;border-top:1px solid var(--linha)}}
.fala h4{font-family:var(--mono);font-size:.7rem;letter-spacing:.14em;
 text-transform:uppercase;margin-bottom:1rem}
.fala .sim h4{color:var(--verde)}
.fala .nao h4{color:#9d3226}
.fala ul{margin:0;padding-left:1.1rem}
.fala li{margin-bottom:.5rem;font-size:.94rem;line-height:1.55}
.fala .nao li{color:var(--cinza2);text-decoration:line-through;
 text-decoration-color:#d8b3ac}

/* ------------------------------------------------------ antes/depois */
.troca{border-top:1px solid var(--linha);padding-block:1.5rem}
.troca .par{display:grid;grid-template-columns:1fr 1fr;gap:1.5rem}
@media(max-width:640px){.troca .par{grid-template-columns:1fr}}
.troca .rot{font-family:var(--mono);font-size:.66rem;letter-spacing:.14em;
 text-transform:uppercase;margin-bottom:.5rem}
.troca .antes .rot{color:#9d3226}
.troca .depois .rot{color:var(--verde)}
.troca .txt{font-size:.99rem;line-height:1.55}
.troca .antes .txt{color:var(--cinza2)}
.troca .por{font-family:var(--mono);font-size:.76rem;color:var(--cinza2);
 margin-top:1rem;line-height:1.55}

/* -------------------------------------------------------- glossário */
.gloss{margin-top:1.6rem;border-top:1px solid var(--linha)}
.gloss .item{display:grid;grid-template-columns:12rem 1fr;gap:1.4rem;
 padding-block:.9rem;border-bottom:1px solid var(--linha)}
@media(max-width:640px){.gloss .item{grid-template-columns:1fr;gap:.2rem}}
.gloss .t{font-family:var(--mono);font-size:.86rem;color:var(--tinta)}
.gloss .d{font-size:.93rem;color:var(--cinza2);line-height:1.55;max-width:56ch}

/* ------------------------------------------------------------ perguntas */
.pg{border-top:1px solid var(--linha);padding-block:1.5rem}
.pg .q{font-family:var(--display);font-weight:300;font-size:clamp(1.1rem,2vw,1.35rem);
 letter-spacing:.03em;margin-bottom:.7rem;max-width:44ch}
.pg .r{color:var(--cinza2);max-width:58ch}
.pg .r p{color:var(--cinza2)}

/* ---------------------------------------------------------- fecho */
.fecho{background:var(--tinta);color:var(--papel)}
.fecho h2{color:var(--papel)}
.fecho p{color:#b9bbc0;max-width:52ch}
.fecho .firma{border-top:1px solid var(--linha-esc)}
.fecho .rubrica{color:var(--papel)}
.fecho .local{color:#8b8e95}

.colofao{margin-top:3.2rem;padding-top:1.2rem;border-top:1px solid var(--linha-esc);
 font-family:var(--mono);font-size:.68rem;letter-spacing:.1em;color:#7c7f86;
 max-width:44ch;line-height:1.7}

/* =========================================================== impresso */
@media print{
  /* margem vem do page.pdf(), nao daqui: com @page{margin} o Chromium
     escala o layout e mm no CSS deixa de ser mm no papel */
  @page{size:A4}
  body{-webkit-print-color-adjust:exact;print-color-adjust:exact;
   font-size:10pt;line-height:1.55}
  .wrap,.wrap-larga{max-width:none;padding-inline:0}
  .g2,.g3{grid-template-columns:repeat(2,1fr)}
  .g3{grid-template-columns:repeat(3,1fr)}
  .paleta{grid-template-columns:repeat(3,1fr);gap:1rem}
  .fala{grid-template-columns:1fr 1fr}
  .troca .par{grid-template-columns:1fr 1fr}
  .gloss .item{grid-template-columns:11rem 1fr}
  .autor{grid-template-columns:1fr 1.35fr}

  section{padding-block:0 1.4rem;break-before:page;break-inside:avoid}
  h2{font-size:1.6rem;margin-bottom:.9rem;break-after:avoid}
  h3{font-size:1.12rem;margin:1.5rem 0 .5rem;break-after:avoid}
  p{max-width:none}
  .entrada{font-size:1.06rem;max-width:none;margin-bottom:1.2rem}

  /* a folha inteira: proporcao em vez de mm, porque o layout de impressao
     e escalado e mm no CSS nao e mm no papel */
  .capa{min-height:252mm;break-before:auto;padding-block:0;
   justify-content:space-between}
  .capa-meio .logo{max-width:100%}

  /* a parte ocupa a folha inteira, como no impresso de verdade */
  .parte{min-height:252mm;justify-content:center;padding:14mm;break-inside:avoid}
  .parte .num{font-size:8.4rem}
  .parte h2{font-size:2.5rem}

  .manifesto{padding:14mm;min-height:252mm;
   display:flex;flex-direction:column;justify-content:center}
  .manifesto p{font-size:2rem}
  .manifesto p.miudo{font-size:1rem}

  .fecho{padding:14mm;min-height:252mm;
   display:flex;flex-direction:column;justify-content:center}

  .fig{margin-block:1rem;padding:1rem}
  .chip{height:50px}
  .sw-val{font-size:.68rem;line-height:1.5}
  .sw-uso{font-size:.76rem}
  .nota{font-size:.72rem;line-height:1.45}
  .lixo{margin-top:1rem}
  .lixo li{padding-block:.32rem;grid-template-columns:2.3rem 1fr;gap:.9rem}
  .lixo h4{font-size:.9rem;margin-bottom:.05rem}
  .lixo p{font-size:.8rem;line-height:1.38}
  .selo{font-size:.6rem;padding:.04rem .38rem;margin-bottom:.2rem}
  table{font-size:.84rem;margin-top:.9rem;min-width:0}
  .rolagem{overflow:visible}
  th,td{padding:.42rem .4rem}
  .pg{padding-block:.9rem}
  .pg .q{font-size:1.05rem;margin-bottom:.4rem}
  .pg .r p{margin-bottom:.5rem}
  .troca{padding-block:1rem}
  .troca .txt{font-size:.9rem;line-height:1.45}
  .troca .por{font-size:.72rem;margin-top:.6rem}
  .gloss .item{padding-block:.6rem}
  .gloss .d{font-size:.85rem;line-height:1.45}
  .fig,.sw,.lixo li,figure,.citacao,.troca,.pg,.gloss .item,.fala{break-inside:avoid}
  .colofao{margin-top:2rem;font-size:.62rem}
}
"""
