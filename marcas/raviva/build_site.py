# -*- coding: utf-8 -*-
import base64, os

BASE = "/tmp/claude-0/-home-user-skills/9b00c726-1271-5e08-a488-cbad7d5f439a/scratchpad/raviva"
FONT_DIR = "/root/.claude/skills/canvas-design/canvas-fonts"

def b64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("ascii")

POIRET = b64(os.path.join(FONT_DIR, "PoiretOne-Regular.ttf"))
OUTFIT_REG = b64(os.path.join(FONT_DIR, "Outfit-Regular.ttf"))
OUTFIT_BOLD = b64(os.path.join(FONT_DIR, "Outfit-Bold.ttf"))
DMMONO = b64(os.path.join(FONT_DIR, "DMMono-Regular.ttf"))

with open(os.path.join(BASE, "final", "icon_symbol_light.txt"), encoding="utf-8") as f:
    ICON_LIGHT = f.read()
with open(os.path.join(BASE, "final", "icon_symbol_dark.txt"), encoding="utf-8") as f:
    ICON_DARK = f.read()

# The two icon fragments were generated with identical geometry (only stroke/fill
# colour differs) -- confirmed byte-length-identical in brand_kit. We wrap each in
# a <symbol> once and every instance on the page is a <use>, so there is no way
# for two renders to drift apart.
SYMBOL_DEFS = f'''<svg width="0" height="0" style="position:absolute" aria-hidden="true">
<defs>
<symbol id="ic-light" viewBox="0 0 450 450">{ICON_LIGHT}</symbol>
<symbol id="ic-dark" viewBox="0 0 450 450">{ICON_DARK}</symbol>
</defs>
</svg>'''

CSS = '''
/* ============================================================
   RAVIVA — Defesa & Manual de Marca
   Documento de marca de tema único e deliberado: as cores claras
   e escuras abaixo pertencem ao conteudo (capitulos "dia" e
   "brasa" da propria marca), nao ao tema do visualizador -- por
   isso nao ha media query de dark mode aqui. O objetivo e mostrar
   a marca exatamente como ela e, em qualquer maquina.
   ============================================================ */

@font-face { font-family: 'Poiret One'; src: url(data:font/ttf;base64,__POIRET__) format('truetype'); font-weight: 400; font-display: swap; }
@font-face { font-family: 'Outfit'; src: url(data:font/ttf;base64,__OUTFIT_REG__) format('truetype'); font-weight: 400; font-display: swap; }
@font-face { font-family: 'Outfit'; src: url(data:font/ttf;base64,__OUTFIT_BOLD__) format('truetype'); font-weight: 700; font-display: swap; }
@font-face { font-family: 'DM Mono'; src: url(data:font/ttf;base64,__DMMONO__) format('truetype'); font-weight: 400; font-display: swap; }

:root{
  --carvao: #20140D;
  --carvao-2: #2c1c12;
  --carvao-3: #3a2517;
  --papel: #FCF8F1;
  --papel-2: #F3ECDF;
  --papel-line: #e7dcc9;
  --tinta: #3A2317;
  --tinta-suave: #6b5645;
  --brasa: #C9491F;
  --brasa-suave: #E2A98C;
  --sol: #E8A63C;
  --claro: #F3E9DC;
  --claro-suave: #c9b3a0;

  --serif-display: 'Poiret One', 'Outfit', sans-serif;
  --sans: 'Outfit', -apple-system, sans-serif;
  --mono: 'DM Mono', ui-monospace, monospace;

  --wrap: 1180px;
  --gap: clamp(1.25rem, 2.5vw, 2.5rem);
}

*{ box-sizing:border-box; }
html{ scroll-behavior:smooth; }
@media (prefers-reduced-motion: reduce){
  html{ scroll-behavior:auto; }
  *{ animation-duration:0.001ms !important; animation-iteration-count:1 !important; transition-duration:0.001ms !important; }
}

@media print{
  @page{ size:A4; margin:14mm; }
  .dial{ display:none; }
  .reveal{ opacity:1 !important; transform:none !important; }
  .cover{ min-height:auto; padding-block:3rem; }
  .cover .scroll-cue{ display:none; }
  .closing{ min-height:auto; padding-block:3rem; }
  .panel{ padding-block:2.2rem; }
  .chapter-head, .sig-card, .avoid-card, .voice-card, .app-card, .swatch, .specimen, .timeline li, blockquote.pull{
    break-inside:avoid;
  }
  section{ break-before:auto; }
  #defesa{ break-before:page; }
  #manual{ break-before:page; }
  #aplicacoes{ break-before:page; }
  body{ -webkit-print-color-adjust:exact; print-color-adjust:exact; }
}

body{
  margin:0;
  background:var(--carvao);
  color:var(--claro);
  font-family:var(--sans);
  font-size:16px;
  line-height:1.6;
  -webkit-font-smoothing:antialiased;
}

::selection{ background:var(--brasa); color:var(--claro); }

a{ color:inherit; }

.container{ max-width:var(--wrap); margin:0 auto; padding-inline:clamp(1.25rem, 4vw, 3rem); }

.eyebrow{
  font-family:var(--mono); font-size:0.78rem; letter-spacing:0.22em; text-transform:uppercase;
}

h1,h2,h3{ text-wrap:balance; margin:0; font-weight:400; }

.h-display{ font-family:var(--serif-display); }

/* ---------- shelf / panel rhythm ---------- */

.panel{ position:relative; padding-block:clamp(4rem, 9vw, 7.5rem); }
.panel-light{ background:var(--papel); color:var(--tinta); }
.panel-dark{ background:var(--carvao); color:var(--claro); }

.panel-light .eyebrow{ color:var(--brasa); }
.panel-dark .eyebrow{ color:var(--sol); }

.rule{ border:none; border-top:1px solid var(--papel-line); margin:0; }
.panel-dark .rule{ border-top-color:#4a3323; }

/* ---------- chapter dial (fixed nav) ---------- */

.dial{
  position:fixed; right:clamp(0.75rem, 2vw, 1.75rem); top:50%; transform:translateY(-50%);
  z-index:40; display:flex; flex-direction:column; align-items:center; gap:0.9rem;
}
.dial-ring{ width:38px; height:38px; }
.dial-ring circle{ fill:none; stroke:var(--claro-suave); stroke-width:2; opacity:0.35; }
.dial-ring .prog{ stroke:var(--sol); stroke-width:2.5; stroke-linecap:round; transition:stroke-dashoffset .25s linear; opacity:1; }
.dial-dots{ display:flex; flex-direction:column; gap:0.55rem; }
.dial-dot{
  width:9px; height:9px; border-radius:50%; border:1.5px solid var(--claro-suave); background:transparent;
  cursor:pointer; padding:0; transition:background .2s, border-color .2s, transform .2s;
}
.dial-dot:hover{ transform:scale(1.15); }
.dial-dot.active{ background:var(--sol); border-color:var(--sol); }
.dial-dot:focus-visible{ outline:2px solid var(--sol); outline-offset:3px; }
@media (max-width: 860px){ .dial{ display:none; } }

/* ---------- cover ---------- */

.cover{ min-height:100svh; display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center; gap:clamp(1.5rem,4vw,2.5rem); padding-block:6rem; }
.cover .icon-wrap{ width:clamp(150px,22vw,230px); animation:rise-in .9s cubic-bezier(.2,.8,.2,1) both; }
.cover .icon-wrap svg{ width:100%; height:auto; display:block; }
.cover .wordmark{ font-family:var(--serif-display); font-size:clamp(2.6rem,9vw,5.6rem); letter-spacing:0.14em; color:var(--claro); animation:rise-in .9s .12s cubic-bezier(.2,.8,.2,1) both; }
.cover .tagline{ font-family:var(--sans); font-weight:500; font-size:clamp(0.85rem,1.6vw,1.05rem); letter-spacing:0.32em; text-transform:uppercase; color:var(--sol); animation:rise-in .9s .22s cubic-bezier(.2,.8,.2,1) both; }
.cover .doc-title{ font-family:var(--mono); font-size:0.85rem; letter-spacing:0.14em; color:var(--claro-suave); margin-top:1.5rem; animation:rise-in .9s .3s cubic-bezier(.2,.8,.2,1) both; }
.cover .scroll-cue{ position:absolute; bottom:2.4rem; left:50%; transform:translateX(-50%); font-family:var(--mono); font-size:0.72rem; letter-spacing:0.2em; color:var(--claro-suave); display:flex; flex-direction:column; align-items:center; gap:0.5rem; }
.cover .scroll-cue::after{ content:''; width:1px; height:34px; background:linear-gradient(var(--sol), transparent); animation:pulse-line 2s ease-in-out infinite; }

@keyframes rise-in{ from{ opacity:0; transform:translateY(18px); } to{ opacity:1; transform:none; } }
@keyframes pulse-line{ 0%,100%{ opacity:.3; } 50%{ opacity:1; } }

/* ---------- chapter heading block ---------- */

.chapter-head{ display:grid; grid-template-columns:auto 1fr; gap:clamp(1rem,3vw,2.5rem); align-items:end; margin-bottom:clamp(2.5rem,5vw,4rem); }
.chapter-num{ font-family:var(--mono); font-size:clamp(2.6rem,6vw,4rem); line-height:1; opacity:0.25; }
.chapter-title{ font-family:var(--serif-display); font-size:clamp(2.1rem,5vw,3.4rem); letter-spacing:0.02em; }
.chapter-kicker{ font-family:var(--mono); font-size:0.78rem; letter-spacing:0.2em; margin-bottom:0.6rem; display:block; }

.lede{ max-width:62ch; font-size:clamp(1.05rem,1.6vw,1.25rem); }
.panel-light .lede{ color:var(--tinta-suave); }
.panel-dark .lede{ color:var(--claro-suave); }

/* ---------- reveal on scroll ----------
   Progressive enhancement only: content is fully visible by default so the
   file works with JavaScript off, blocked, or stripped by a file previewer.
   The animated hide/reveal only switches on once html.js is present. */
html.js .reveal{ opacity:0; transform:translateY(16px); transition:opacity .7s ease, transform .7s ease; }
html.js .reveal.in{ opacity:1; transform:none; }

/* ---------- pull quote ---------- */
.pull{ font-family:var(--serif-display); font-size:clamp(1.7rem,3.6vw,2.8rem); line-height:1.3; max-width:18ch; margin-block:clamp(1.5rem,4vw,3rem); }
.panel-light .pull{ color:var(--brasa); }
.panel-dark .pull{ color:var(--sol); }

/* ---------- section 1: defesa ---------- */

.defesa-block{ display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1.3fr); gap:clamp(2rem,5vw,4.5rem); align-items:start; margin-block:clamp(3rem,6vw,5rem); }
@media (max-width:820px){ .defesa-block{ grid-template-columns:1fr; } }
.defesa-block .label{ font-family:var(--mono); font-size:0.78rem; letter-spacing:0.2em; }
.panel-light .defesa-block .label{ color:var(--brasa); }
.panel-dark .defesa-block .label{ color:var(--sol); }
.defesa-block h3{ font-family:var(--serif-display); font-size:clamp(1.5rem,3vw,2.1rem); margin-block:0.5rem 1rem; }
.defesa-block p + p{ margin-top:1rem; }
.defesa-block p{ max-width:60ch; }

/* ---------- timeline (o caminho ate aqui) ---------- */

.timeline{ list-style:none; margin:0; padding:0; border-top:1px solid #4a3323; }
.timeline li{ display:grid; grid-template-columns:5.5rem 1fr; gap:clamp(1rem,3vw,2.5rem); padding-block:1.6rem; border-bottom:1px solid #4a3323; }
.timeline .t-num{ font-family:var(--mono); font-size:0.85rem; color:var(--sol); letter-spacing:0.08em; padding-top:0.15rem; }
.timeline .t-tag{ display:inline-block; font-family:var(--mono); font-size:0.7rem; letter-spacing:0.14em; text-transform:uppercase; padding:0.15rem 0.55rem; border:1px solid #5a3f2c; border-radius:3px; margin-bottom:0.5rem; color:var(--claro-suave); }
.timeline .t-tag.kept{ border-color:var(--sol); color:var(--sol); }
.timeline h4{ font-family:var(--sans); font-weight:700; font-size:1.05rem; margin:0 0 0.35rem; color:var(--claro); }
.timeline p{ margin:0; max-width:60ch; color:var(--claro-suave); }

/* ---------- typography / voice sample rows ---------- */

.specimen{ display:flex; align-items:baseline; gap:clamp(1.2rem,3vw,2.4rem); flex-wrap:wrap; padding-block:1.8rem; border-bottom:1px solid var(--papel-line); }
.specimen:first-of-type{ border-top:1px solid var(--papel-line); }
.specimen .glyphs{ font-family:var(--serif-display); font-size:clamp(3rem,6vw,4.5rem); line-height:1; min-width:5.5rem; }
.specimen .meta{ flex:1; min-width:220px; }
.specimen .meta .name{ font-family:var(--mono); font-size:0.78rem; letter-spacing:0.16em; color:var(--brasa); display:block; margin-bottom:0.4rem; }
.specimen .meta p{ margin:0; color:var(--tinta-suave); max-width:52ch; }

/* ---------- signature versions grid ---------- */

.sig-grid{ display:grid; grid-template-columns:repeat(3,1fr); gap:clamp(1rem,2vw,1.5rem); margin-top:clamp(2rem,4vw,3rem); }
.sig-card{ background:var(--papel-2); border:1px solid var(--papel-line); padding:clamp(1.5rem,3vw,2.2rem); display:flex; flex-direction:column; align-items:center; justify-content:center; gap:1.2rem; min-height:280px; text-align:center; }
.sig-card.span2{ grid-column:span 2; }
.sig-card.dark{ background:var(--carvao); border-color:#4a3323; }
.sig-card .cap{ font-family:var(--mono); font-size:0.72rem; letter-spacing:0.14em; color:var(--tinta-suave); margin-top:auto; }
.sig-card.dark .cap{ color:var(--claro-suave); }
.sig-card svg.icon-s{ width:clamp(70px,10vw,110px); }
.sig-card .wm{ font-family:var(--serif-display); font-size:clamp(1.3rem,2.4vw,1.8rem); letter-spacing:0.12em; }
.sig-card .tg{ font-family:var(--sans); font-weight:500; font-size:0.62rem; letter-spacing:0.2em; text-transform:uppercase; color:var(--brasa); margin-top:-0.7rem; }
.sig-card.dark .wm{ color:var(--claro); }
.sig-card.dark .tg{ color:var(--sol); }
.sig-row{ display:flex; align-items:center; gap:1.4rem; }
.sig-row .divider{ width:1px; align-self:stretch; background:var(--papel-line); }
.sig-card.dark .sig-row .divider{ background:#4a3323; }
@media (max-width:760px){ .sig-grid{ grid-template-columns:1fr 1fr; } .sig-card.span2{ grid-column:span 2; } }
@media (max-width:520px){ .sig-grid{ grid-template-columns:1fr; } .sig-card.span2{ grid-column:span 1; } }

/* ---------- clear space diagram ---------- */

.clearspace{ display:flex; justify-content:center; margin-block:clamp(2.5rem,5vw,4rem); }
.clearspace .box{ position:relative; border:1.5px dashed var(--brasa); padding:3.2rem 2.6rem; display:flex; flex-direction:column; align-items:center; gap:1rem; }
.clearspace svg.icon-m{ width:120px; }
.clearspace .wm{ font-family:var(--serif-display); font-size:1.7rem; letter-spacing:0.12em; }
.clearspace .tg{ font-family:var(--sans); font-weight:500; font-size:0.6rem; letter-spacing:0.22em; color:var(--brasa); margin-top:-0.6rem; }
.min-sizes{ display:flex; gap:clamp(2rem,5vw,4rem); justify-content:center; flex-wrap:wrap; margin-top:2.5rem; }
.min-sizes figure{ margin:0; display:flex; flex-direction:column; align-items:center; gap:0.8rem; }
.min-sizes figcaption{ font-family:var(--mono); font-size:0.7rem; letter-spacing:0.1em; color:var(--tinta-suave); text-align:center; }

/* ---------- colour palette ---------- */

.palette{ display:grid; grid-template-columns:repeat(3,1fr); gap:clamp(1rem,2vw,1.5rem); margin-top:clamp(2rem,4vw,3rem); }
.swatch{ display:flex; flex-direction:column; }
.swatch .chip{ height:140px; border:1px solid var(--papel-line); }
.swatch .info{ padding-top:0.8rem; font-family:var(--mono); font-size:0.78rem; }
.swatch .info .nm{ font-family:var(--sans); font-weight:700; font-size:0.95rem; letter-spacing:0.02em; margin-bottom:0.3rem; }
.swatch .info .use{ font-family:var(--sans); color:var(--tinta-suave); margin-top:0.35rem; font-size:0.85rem; }
.swatch .info .vals{ font-variant-numeric:tabular-nums; color:var(--tinta-suave); }
@media (max-width:760px){ .palette{ grid-template-columns:repeat(2,1fr); } }
@media (max-width:480px){ .palette{ grid-template-columns:1fr; } }

/* ---------- dos and donts ---------- */

.avoid-grid{ display:grid; grid-template-columns:repeat(3,1fr); gap:clamp(1rem,2vw,1.5rem); margin-top:clamp(2rem,4vw,3rem); }
.avoid-card{ position:relative; background:var(--papel-2); border:1px solid var(--papel-line); aspect-ratio:1; display:flex; align-items:center; justify-content:center; overflow:hidden; }
.avoid-card svg.icon-w{ width:46%; }
.avoid-card .no{ position:absolute; inset:14%; border:5px solid var(--brasa); border-radius:50%; opacity:0.85; }
.avoid-card .no::after{ content:''; position:absolute; inset:0; margin:auto; width:2px; height:141%; background:var(--brasa); transform:rotate(45deg); top:-20.5%; }
.avoid-card .cap{ position:absolute; bottom:0; left:0; right:0; padding:0.7rem 0.8rem; font-family:var(--mono); font-size:0.68rem; letter-spacing:0.08em; text-align:center; background:linear-gradient(transparent, rgba(0,0,0,.08) 40%); color:var(--tinta-suave); }
@media (max-width:760px){ .avoid-grid{ grid-template-columns:repeat(2,1fr); } }
@media (max-width:480px){ .avoid-grid{ grid-template-columns:1fr; } }

/* ---------- voice pillars ---------- */

.voice-grid{ display:grid; grid-template-columns:repeat(2,1fr); gap:clamp(1.5rem,3vw,3rem); margin-top:clamp(2rem,4vw,3rem); }
@media (max-width:760px){ .voice-grid{ grid-template-columns:1fr; } }
.voice-card .dot{ width:8px; height:8px; border-radius:50%; background:var(--sol); margin-bottom:0.9rem; }
.voice-card h4{ font-family:var(--mono); font-size:0.85rem; letter-spacing:0.14em; margin:0 0 0.6rem; color:var(--claro); }
.voice-card p{ color:var(--claro-suave); margin:0 0 1rem; max-width:46ch; }
.voice-card .example{ font-family:var(--serif-display); font-size:1.35rem; color:var(--sol); }

/* ---------- applications ---------- */

.app-grid{ display:grid; grid-template-columns:1fr 1fr; gap:clamp(1.5rem,3vw,3rem); margin-top:clamp(2rem,4vw,3rem); }
@media (max-width:820px){ .app-grid{ grid-template-columns:1fr; } }
.app-card{ display:flex; flex-direction:column; gap:1.2rem; }
.app-stage{ background:var(--carvao-2); border:1px solid #4a3323; display:flex; align-items:center; justify-content:center; padding:clamp(2rem,5vw,3.2rem); min-height:340px; }
.app-cap{ font-family:var(--mono); font-size:0.78rem; letter-spacing:0.1em; color:var(--claro-suave); }
.app-cap b{ color:var(--claro); font-weight:400; font-family:var(--sans); font-size:0.95rem; letter-spacing:0; display:block; margin-bottom:0.3rem; }

/* agenda mockup */
.mock-agenda{ width:220px; aspect-ratio:3/4; background:linear-gradient(160deg,var(--carvao) 0%,#2a1a10 100%); position:relative; box-shadow:0 30px 60px -20px rgba(0,0,0,.6), 0 0 0 1px #4a3323; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:1rem; }
.mock-agenda::before{ content:''; position:absolute; left:16px; top:0; bottom:0; width:1px; background:rgba(232,166,60,.25); }
.mock-agenda svg{ width:56px; }
.mock-agenda .wm{ font-family:var(--serif-display); font-size:1rem; letter-spacing:0.16em; color:var(--sol); }
.mock-agenda .band{ position:absolute; right:14px; top:0; bottom:0; width:10px; background:var(--brasa); opacity:0.9; }

/* website mockup */
.mock-browser{ width:100%; max-width:420px; background:var(--papel); border:1px solid #4a3323; box-shadow:0 30px 60px -20px rgba(0,0,0,.6); }
.mock-browser .chrome{ display:flex; align-items:center; gap:0.5rem; padding:0.6rem 0.8rem; background:var(--papel-2); border-bottom:1px solid var(--papel-line); }
.mock-browser .dots{ display:flex; gap:0.32rem; }
.mock-browser .dots span{ width:8px; height:8px; border-radius:50%; background:#d8c8b0; }
.mock-browser .addr{ flex:1; background:var(--papel); border:1px solid var(--papel-line); border-radius:20px; padding:0.25rem 0.9rem; font-family:var(--mono); font-size:0.68rem; color:var(--tinta-suave); }
.mock-browser .hero{ padding:2.6rem 1.5rem; display:flex; flex-direction:column; align-items:center; gap:0.8rem; text-align:center; }
.mock-browser .hero svg{ width:52px; }
.mock-browser .hero .wm{ font-family:var(--serif-display); font-size:1.4rem; letter-spacing:0.14em; color:var(--tinta); }
.mock-browser .hero .tg{ font-family:var(--sans); font-weight:500; font-size:0.62rem; letter-spacing:0.2em; color:var(--brasa); }
.mock-browser .hero .cta{ margin-top:0.6rem; font-family:var(--mono); font-size:0.68rem; letter-spacing:0.08em; color:var(--papel); background:var(--brasa); padding:0.55rem 1.1rem; }

/* mug mockup */
.mock-mug{ width:190px; display:flex; flex-direction:column; align-items:center; }
.mock-mug svg{ width:100%; height:auto; }

/* tee mockup */
.mock-tee{ width:260px; }
.mock-tee svg{ width:100%; height:auto; }

/* ---------- closing ---------- */
.closing{ min-height:70svh; display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center; gap:2rem; }
.closing svg{ width:110px; }
.closing .wm{ font-family:var(--serif-display); font-size:clamp(1.8rem,4vw,2.6rem); letter-spacing:0.14em; }
.closing .tg{ font-family:var(--sans); font-weight:500; font-size:0.78rem; letter-spacing:0.28em; text-transform:uppercase; color:var(--sol); }
.closing .meta{ font-family:var(--mono); font-size:0.75rem; color:var(--claro-suave); letter-spacing:0.1em; margin-top:1rem; }

footer.doc-footer{ text-align:center; padding-block:3rem 4rem; font-family:var(--mono); font-size:0.72rem; letter-spacing:0.1em; color:var(--claro-suave); }
'''

CSS = (CSS
    .replace("__POIRET__", POIRET)
    .replace("__OUTFIT_REG__", OUTFIT_REG)
    .replace("__OUTFIT_BOLD__", OUTFIT_BOLD)
    .replace("__DMMONO__", DMMONO)
)

def icon(variant="light", cls="icon-s"):
    # width/height pinned to the symbol's own viewBox so <use> never falls back
    # to an ambiguous default viewport -- the only thing allowed to resize the
    # mark afterwards is the outer <svg>'s CSS width (height:auto keeps ratio).
    return f'<svg viewBox="0 0 450 450" class="{cls}" aria-hidden="true"><use href="#ic-{variant}" width="450" height="450"/></svg>'

NAV_HTML = f'''
<nav class="dial" aria-label="Navegacao de capitulos">
  <svg class="dial-ring" viewBox="0 0 38 38" aria-hidden="true">
    <circle cx="19" cy="19" r="16"/>
    <circle class="prog" id="dialProg" cx="19" cy="19" r="16" pathLength="100" stroke-dasharray="100" stroke-dashoffset="100" transform="rotate(-90 19 19)"/>
  </svg>
  <div class="dial-dots">
    <button class="dial-dot" data-target="capa" aria-label="Capa"></button>
    <button class="dial-dot" data-target="defesa" aria-label="Defesa da marca"></button>
    <button class="dial-dot" data-target="manual" aria-label="Manual de marca"></button>
    <button class="dial-dot" data-target="aplicacoes" aria-label="Aplicacoes"></button>
  </div>
</nav>
'''

COVER_HTML = f'''
<section class="cover panel-dark" id="capa">
  <div class="icon-wrap">{icon("dark")}</div>
  <h1 class="wordmark">R A V I V A</h1>
  <p class="tagline">Acenda a fa&iacute;sca</p>
  <p class="doc-title">DEFESA DE MARCA &amp; MANUAL DE IDENTIDADE &mdash; VERS&Atilde;O 1.0, 2026</p>
  <div class="scroll-cue">ROLAR</div>
</section>
'''

TIMELINE = [
    ("01", "DESCARTADO", "Fogo + sol, colados",
     "Testamos combina&ccedil;&otilde;es diretas em latim, grego, n&oacute;rdico antigo e s&acirc;nscrito &mdash; Ignisol, Pyrhelio, Eldsol, Fosol. Nomeavam o conceito, mas soavam a nome montado, n&atilde;o a nome encontrado."),
    ("02", "MANTIDO", "Raviva",
     "<em>Ravi</em> (sol, s&acirc;nscrito) escondido dentro de <em>avivar</em> (reacender, portugu&ecirc;s). Vence por parecer uma palavra real antes de parecer um nome inventado."),
    ("03", "VALIDADO", "Busca de registro",
     "O &uacute;nico registro ativo do nome &eacute; de um vinho americano &mdash; categoria e mercado sem sobreposi&ccedil;&atilde;o com o uso pretendido aqui."),
    ("04", "DESCARTADO", "S&iacute;mbolo v1 &mdash; Sol Semente",
     "Sunburst geom&eacute;trico com uma gota de fogo pingando do centro. Lia como &iacute;cone de previs&atilde;o do tempo, n&atilde;o como marca pr&oacute;pria."),
    ("05", "DESCARTADO", "S&iacute;mbolo v2 &mdash; Brasa Cont&iacute;nua",
     "Chama em tra&ccedil;o &uacute;nico, com uma brasa pulsando dentro. O contorno perdia qualidade em tamanhos pequenos &mdash; n&atilde;o passava no teste do favicon."),
    ("06", "BASE", "S&iacute;mbolo v3 &mdash; Ciclo Solar",
     "Um anel: raios de sol na metade de cima, pontas de fogo na metade de baixo, Poiret One por baixo. Primeira vers&atilde;o que pareceu selo, n&atilde;o clip-art &mdash; vira a base de tudo o que vem depois."),
    ("07", "ARQUIVADO", "Dire&ccedil;&atilde;o Centelha",
     "Wordmark autoral em fundo escuro, com o ponto do &ldquo;i&rdquo; virando uma centelha de quatro pontas. N&atilde;o virou a pe&ccedil;a final, mas essa forma volta mais adiante, quando o s&iacute;mbolo precisou soltar uma fa&iacute;sca de verdade."),
    ("08", "INCORPORADO", "Entra a madeira",
     "O s&iacute;mbolo vira um corte transversal de tronco: cada anel de crescimento, um ano de sol guardado. N&atilde;o &eacute; met&aacute;fora nova &mdash; &eacute; o pr&oacute;prio conceito, desenhado com precis&atilde;o de dendrocronologia."),
    ("09", "INCORPORADO", "Madeira real + leveza do selo",
     "O corte de tronco ganha a irregularidade de uma amostra real &mdash; casca imperfeita, m&eacute;dula fora do centro, rachadura &mdash; mas volta a viver dentro da leveza clara do Ciclo Solar."),
    ("10", "APROVADO", "Volta &agrave; origem, com imperfei&ccedil;&atilde;o",
     "Fechamos na estrutura exata do Ciclo Solar (06) &mdash; mas os dois c&iacute;rculos deixam de ser geom&eacute;tricos e ganham a imprecis&atilde;o de um tra&ccedil;o &agrave; m&atilde;o. A fa&iacute;sca, que tinha virado desenho em 07, volta a ser palavra: &ldquo;acenda a fa&iacute;sca&rdquo;."),
    ("11", "APROVADO", "Uma fra&ccedil;&atilde;o fixa do raio",
     "Cada raio de sol, cada ponta de chama, o ponto central &mdash; tudo passou a ser calculado como fra&ccedil;&atilde;o do raio do s&iacute;mbolo, nunca em pixels fixos. Em qualquer tamanho, a mesma forma exata, ao mil&eacute;simo."),
]

def timeline_item(num, tag, title, body):
    kept = "kept" if tag in ("MANTIDO", "BASE", "APROVADO", "VALIDADO", "INCORPORADO") else ""
    return f'''<li>
      <div class="t-num">{num}</div>
      <div>
        <span class="t-tag {kept}">{tag}</span>
        <h4>{title}</h4>
        <p>{body}</p>
      </div>
    </li>'''

TIMELINE_HTML = "\n".join(timeline_item(*row) for row in TIMELINE)

DEFESA_HTML = f'''
<section class="panel panel-light" id="defesa">
  <div class="container">
    <div class="chapter-head">
      <span class="chapter-num">01</span>
      <div>
        <span class="chapter-kicker" style="color:var(--brasa)">DEFESA DE MARCA</span>
        <h2 class="chapter-title h-display">Por que Raviva &eacute; Raviva</h2>
      </div>
    </div>
    <p class="lede reveal">Toda marca boa devia poder se explicar sem enrola&ccedil;&atilde;o. Este cap&iacute;tulo &eacute; essa explica&ccedil;&atilde;o &mdash; do porqu&ecirc; do nome ao porqu&ecirc; de cada tra&ccedil;o do s&iacute;mbolo.</p>

    <div class="defesa-block reveal">
      <div><span class="label">O NOME</span><h3 class="h-display">Uma palavra escondida dentro de outra</h3></div>
      <div>
        <p><strong>Ravi</strong> &eacute; sol, em s&acirc;nscrito. <strong>Avivar</strong> &eacute; um verbo portugu&ecirc;s comum &mdash; reacender, atear uma chama. Escondido dentro da terceira pessoa desse verbo &mdash; &ldquo;ele avi<strong>va</strong>&rdquo; &mdash; mora exatamente esse sol. Raviva n&atilde;o &eacute; a jun&ccedil;&atilde;o de duas palavras coladas em latim ou grego: &eacute; um achado dentro de uma palavra que j&aacute; existia.</p>
        <p>Evitamos de prop&oacute;sito a rota mais &oacute;bvia &mdash; nomes como Ignisol, Pyrhelio ou Eldsol, colando ra&iacute;zes de fogo e sol em l&iacute;nguas diferentes. Soam a nome de startup de energia, fabricado na hora. Raviva soa como uma palavra que sempre existiu, porque ela quase existia mesmo.</p>
        <p>Antes de fechar, checamos registro de marca: o &uacute;nico ativo com esse nome &eacute; de um vinho nos Estados Unidos &mdash; categoria e mercado diferentes, sem conflito para o uso pretendido aqui.</p>
      </div>
    </div>

    <div class="defesa-block reveal">
      <div><span class="label">O CONCEITO</span><h3 class="h-display">Fogo &eacute; sol estocado</h3></div>
      <div>
        <p>N&atilde;o &eacute; for&ccedil;a de express&atilde;o &mdash; &eacute; o processo f&iacute;sico, sem atalho po&eacute;tico. Uma planta captura luz solar por fotoss&iacute;ntese e a guarda, c&eacute;lula a c&eacute;lula, na pr&oacute;pria madeira. Cada anel de crescimento de uma &aacute;rvore &eacute;, literalmente, um ano inteiro de sol condensado &mdash; &eacute; assim que a dendrocronologia data uma &aacute;rvore s&oacute; de olhar seus an&eacute;is.</p>
        <p>Fogo &eacute; a devolu&ccedil;&atilde;o dessa energia: o momento em que o sol guardado h&aacute; anos volta a ser luz e calor de uma vez. A Raviva nasce desse princ&iacute;pio &mdash; energia que n&atilde;o se perde, apenas espera.</p>
      </div>
    </div>

    <blockquote class="pull reveal">Fogo &eacute; sol estocado.</blockquote>
  </div>
</section>

<section class="panel panel-dark">
  <div class="container">
    <span class="eyebrow reveal">O CAMINHO AT&Eacute; AQUI</span>
    <h3 class="h-display reveal" style="font-size:clamp(1.6rem,3.4vw,2.4rem); margin-top:0.6rem; max-width:20ch;">Onze decis&otilde;es, uma marca</h3>
    <p class="lede reveal" style="margin-top:1rem;">Nada aqui chegou pronto de primeira. O registro abaixo &eacute; o que foi testado, o que foi descartado e por qu&ecirc; &mdash; na ordem em que aconteceu.</p>
    <ol class="timeline reveal">
      {TIMELINE_HTML}
    </ol>
  </div>
</section>

<section class="panel panel-light">
  <div class="container">
    <div class="defesa-block reveal">
      <div><span class="label">O SLOGAN</span><h3 class="h-display">Acenda a fa&iacute;sca</h3></div>
      <div>
        <p>&Eacute; um verbo no imperativo &mdash; uma instru&ccedil;&atilde;o, n&atilde;o uma descri&ccedil;&atilde;o. Fa&iacute;sca &eacute; a menor unidade de energia liberada: o ponto exato em que o combust&iacute;vel guardado come&ccedil;a a virar fogo. &Eacute; o verbo <em>avivar</em> &mdash; que j&aacute; mora dentro do nome &mdash; dito em voz alta.</p>
        <p>Curto o suficiente para caber embaixo do wordmark em qualquer aplica&ccedil;&atilde;o, de embalagem a assinatura de e-mail, e forte o suficiente para funcionar sozinho, sem precisar do s&iacute;mbolo ao lado.</p>
      </div>
    </div>

    <div class="defesa-block reveal">
      <div><span class="label">A TIPOGRAFIA</span><h3 class="h-display">Poiret One, Outfit, DM Mono</h3></div>
      <div>
        <p>Poiret One &eacute; uma fonte art d&eacute;co francesa dos anos 1920, constru&iacute;da sobre c&iacute;rculos e tra&ccedil;os finos &mdash; a mesma l&oacute;gica geom&eacute;trica do s&iacute;mbolo, n&atilde;o uma tipografia gen&eacute;rica de energia, pesada e t&eacute;cnica. Em caixa alta e bem espa&ccedil;ada, ela l&ecirc; como selo &mdash; o que &eacute;, literalmente, o s&iacute;mbolo ao lado dela.</p>
        <p>Outfit entra para todo texto de apoio: neutra, geom&eacute;trica, leg&iacute;vel em qualquer tamanho, sem competir com o wordmark. DM Mono assina dados t&eacute;cnicos e legendas, emprestando a autoridade de um caderno de campo a uma marca que gosta de falar de processo com o p&eacute; no ch&atilde;o.</p>
      </div>
    </div>

    <blockquote class="pull reveal">Uma marca s&oacute; est&aacute; pronta quando consegue se explicar sozinha.</blockquote>
    <p class="lede reveal">A Raviva consegue: o nome esconde o sol, o s&iacute;mbolo desenha o ano em que ele foi guardado, e o slogan diz exatamente o que fazer com ele. Nada aqui &eacute; decora&ccedil;&atilde;o &mdash; &eacute; o conceito, redesenhado at&eacute; virar identidade.</p>
  </div>
</section>
'''

SWATCHES = [
    ("Tinta", "#3A2317", "58, 35, 23", "0, 40, 60, 77", "texto principal, wordmark", True),
    ("Brasa", "#C9491F", "201, 73, 31", "0, 64, 85, 21", "cor de marca &mdash; s&iacute;mbolo, tagline, links", True),
    ("Brasa Suave", "#E2A98C", "226, 169, 140", "0, 25, 38, 11", "anel interno, tra&ccedil;os de apoio", False),
    ("Sol", "#E8A63C", "232, 166, 60", "0, 28, 74, 9", "acentos sobre fundo escuro", False),
    ("Papel", "#FCF8F1", "252, 248, 241", "0, 2, 4, 1", "fundo claro padr&atilde;o", False),
    ("Carv&atilde;o", "#20140D", "32, 20, 13", "0, 38, 59, 87", "fundo escuro / vers&atilde;o reversa", True),
]

def swatch_html(name, hexv, rgb, cmyk, use, dark_text):
    color = "var(--claro)" if dark_text else "var(--tinta)"
    border = "border:1px solid var(--papel-line);" if hexv == "#FCF8F1" else ""
    return f'''<div class="swatch reveal">
      <div class="chip" style="background:{hexv};{border}"></div>
      <div class="info">
        <div class="nm">{name}</div>
        <div class="vals">{hexv.upper()}<br>RGB {rgb}<br>CMYK {cmyk}</div>
        <div class="use">{use}</div>
      </div>
    </div>'''

PALETTE_HTML = "\n".join(swatch_html(*s) for s in SWATCHES)

AVOID = [
    ("esticar ou achatar", "transform:scaleX(1.6) scaleY(0.6);"),
    ("girar o s&iacute;mbolo", "transform:rotate(28deg);"),
    ("trocar a cor de marca", "filter:hue-rotate(150deg) saturate(1.3);"),
    ("adicionar sombra / relevo", "filter:drop-shadow(10px 14px 8px rgba(0,0,0,.55));"),
    ("baixo contraste de fundo", None),
    ("sobrepor s&iacute;mbolo e tipografia", None),
]

def avoid_card(label, style):
    if label == "baixo contraste de fundo":
        return f'''<div class="avoid-card reveal" style="background:var(--brasa);">
      {icon("light","icon-w")}
      <div class="no"></div>
      <div class="cap" style="color:var(--claro)">{label}</div>
    </div>'''
    if label.startswith("sobrepor"):
        return f'''<div class="avoid-card reveal">
      <div style="position:relative; width:60%;">
        {icon("light","icon-w")}
        <span class="h-display" style="position:absolute; inset:0; display:flex; align-items:center; justify-content:center; font-size:1.1rem; letter-spacing:0.1em; color:var(--tinta);">RAVIVA</span>
      </div>
      <div class="no"></div>
      <div class="cap">{label}</div>
    </div>'''
    return f'''<div class="avoid-card reveal">
      <div style="{style}">{icon("light","icon-w")}</div>
      <div class="no"></div>
      <div class="cap">{label}</div>
    </div>'''

AVOID_HTML = "\n".join(avoid_card(l, s) for l, s in AVOID)

VOICE = [
    ("DIRETO", "Frases curtas, sem jarg&atilde;o corporativo de energia.", "&ldquo;Fogo &eacute; sol guardado.&rdquo;"),
    ("QUENTE, N&Atilde;O INSTITUCIONAL", "Fala como quem cuida do fogo, n&atilde;o como uma concession&aacute;ria.", "&ldquo;Acenda a fa&iacute;sca.&rdquo;"),
    ("DEIXA A MET&Aacute;FORA RESPIRAR", "N&atilde;o explica demais &mdash; confia que a imagem j&aacute; comunica.", "&ldquo;Cada anel, um ano de sol.&rdquo;"),
    ("ORGULHO T&Eacute;CNICO DISCRETO", "Ao falar de processo, usa tom de caderno de campo, n&atilde;o de folheto.", "&ldquo;Amostra 01 &mdash; sol guardado.&rdquo;"),
]

VOICE_HTML = "\n".join(f'''<div class="voice-card reveal">
  <div class="dot"></div>
  <h4>{t}</h4>
  <p>{d}</p>
  <div class="example h-display">{e}</div>
</div>''' for t, d, e in VOICE)

MANUAL_HTML = f'''
<section class="panel panel-light" id="manual">
  <div class="container">
    <div class="chapter-head">
      <span class="chapter-num">02</span>
      <div>
        <span class="chapter-kicker" style="color:var(--brasa)">MANUAL DE MARCA</span>
        <h2 class="chapter-title h-display">Como usar a assinatura</h2>
      </div>
    </div>
    <p class="lede reveal">Cinco composi&ccedil;&otilde;es cobrem a maioria dos usos. O s&iacute;mbolo &eacute; sempre o mesmo desenho, em qualquer tamanho &mdash; nunca recompor com outro espa&ccedil;amento, cor ou propor&ccedil;&atilde;o.</p>

    <span class="eyebrow reveal" style="display:block; margin-top:3.5rem; color:var(--brasa);">VERS&Otilde;ES DA ASSINATURA</span>
    <div class="sig-grid">
      <div class="sig-card span2 reveal">
        {icon("light","icon-s")}
        <div class="wm h-display">R A V I V A</div>
        <div class="tg">Acenda a fa&iacute;sca</div>
        <div class="cap">VERTICAL &mdash; USO PRINCIPAL</div>
      </div>
      <div class="sig-card reveal">
        {icon("light","icon-s")}
        <div class="cap">S&Iacute;MBOLO / FAVICON</div>
      </div>
      <div class="sig-card reveal">
        <div class="wm h-display">R A V I V A</div>
        <div class="tg">Acenda a fa&iacute;sca</div>
        <div class="cap">WORDMARK ISOLADO</div>
      </div>
      <div class="sig-card span2 reveal">
        <div class="sig-row">
          <svg viewBox="0 0 450 450" class="icon-s" style="width:64px;" aria-hidden="true"><use href="#ic-light" width="450" height="450"/></svg>
          <div class="divider"></div>
          <div>
            <div class="wm h-display" style="font-size:1.3rem;">R A V I V A</div>
            <div class="tg" style="font-size:0.55rem;">Acenda a fa&iacute;sca</div>
          </div>
        </div>
        <div class="cap">HORIZONTAL &mdash; CABE&Ccedil;ALHOS</div>
      </div>
      <div class="sig-card dark reveal" style="grid-column:1/-1; flex-direction:row; justify-content:center; gap:2rem;">
        {icon("dark","icon-s")}
        <div>
          <div class="wm h-display">R A V I V A</div>
          <div class="tg">Acenda a fa&iacute;sca</div>
        </div>
        <div class="cap" style="position:absolute; bottom:1.5rem; left:0; right:0; text-align:center;">VERS&Atilde;O REVERSA &mdash; FUNDOS ESCUROS OU FOTOGR&Aacute;FICOS</div>
      </div>
    </div>

    <span class="eyebrow reveal" style="display:block; margin-top:5.5rem; color:var(--brasa);">&Aacute;REA DE PROTE&Ccedil;&Atilde;O</span>
    <p class="lede reveal" style="margin-top:0.8rem;">Nenhum elemento pode invadir o espa&ccedil;o livre ao redor da assinatura.</p>
    <div class="clearspace reveal">
      <div class="box">
        {icon("light","icon-m")}
        <div class="wm h-display">R A V I V A</div>
        <div class="tg">Acenda a fa&iacute;sca</div>
      </div>
    </div>
    <p class="lede reveal" style="text-align:center; margin-inline:auto;">X = raio do s&iacute;mbolo. Use X como respiro m&iacute;nimo em qualquer aplica&ccedil;&atilde;o.</p>
    <div class="min-sizes reveal">
      <figure><svg viewBox="0 0 450 450" style="width:80px;"><use href="#ic-light" width="450" height="450"/></svg><figcaption>USO CONFORT&Aacute;VEL</figcaption></figure>
      <figure><svg viewBox="0 0 450 450" style="width:48px;"><use href="#ic-light" width="450" height="450"/></svg><figcaption>M&Iacute;NIMO DIGITAL &mdash; 32PX</figcaption></figure>
      <figure><svg viewBox="0 0 450 450" style="width:32px;"><use href="#ic-light" width="450" height="450"/></svg><figcaption>M&Iacute;NIMO IMPRESSO &mdash; 10MM</figcaption></figure>
    </div>

    <span class="eyebrow reveal" style="display:block; margin-top:5.5rem; color:var(--brasa);">PALETA DE CORES</span>
    <div class="palette">{PALETTE_HTML}</div>

    <span class="eyebrow reveal" style="display:block; margin-top:5.5rem; color:var(--brasa);">TIPOGRAFIA</span>
    <div class="specimen reveal">
      <div class="glyphs h-display">Aa</div>
      <div class="meta"><span class="name">POIRET ONE</span><p>Wordmark e t&iacute;tulos de destaque. Sempre em caixa alta e bem rastreada, nunca condensada.</p></div>
    </div>
    <div class="specimen reveal">
      <div class="glyphs" style="font-family:var(--sans); font-weight:700;">Aa</div>
      <div class="meta"><span class="name">OUTFIT</span><p>Regular para texto de apoio, Medium para tags e bot&otilde;es, Bold para destaques curtos.</p></div>
    </div>
    <div class="specimen reveal">
      <div class="glyphs" style="font-family:var(--mono); font-size:2.6rem;">01</div>
      <div class="meta"><span class="name">DM MONO</span><p>Dados t&eacute;cnicos, legendas de diagrama, rodap&eacute;s &mdash; tom de caderno de campo.</p></div>
    </div>

    <span class="eyebrow reveal" style="display:block; margin-top:5.5rem; color:var(--brasa);">O QUE EVITAR</span>
    <p class="lede reveal" style="margin-top:0.8rem;">Seis desvios comuns. Na d&uacute;vida, volte &agrave; vers&atilde;o vertical padr&atilde;o.</p>
    <div class="avoid-grid">{AVOID_HTML}</div>
  </div>
</section>

<section class="panel panel-dark">
  <div class="container">
    <span class="eyebrow reveal">TOM DE VOZ</span>
    <h3 class="h-display reveal" style="font-size:clamp(1.6rem,3.4vw,2.4rem); margin-top:0.6rem;">Como a Raviva soa em texto</h3>
    <div class="voice-grid">{VOICE_HTML}</div>
  </div>
</section>
'''

MUG_SVG = f'''<svg viewBox="0 0 300 260" class="mock-mug" aria-hidden="true">
  <defs>
    <linearGradient id="mugShade" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#000" stop-opacity="0.12"/>
      <stop offset="0.5" stop-color="#000" stop-opacity="0"/>
      <stop offset="1" stop-color="#000" stop-opacity="0.16"/>
    </linearGradient>
  </defs>
  <ellipse cx="140" cy="238" rx="95" ry="12" fill="#000" opacity="0.35"/>
  <path d="M 55 60 L 225 60 L 213 210 Q 210 224 196 224 L 84 224 Q 70 224 67 210 Z" fill="#FCF8F1"/>
  <path d="M 213 90 C 268 90 268 175 213 178" fill="none" stroke="#FCF8F1" stroke-width="18"/>
  <path d="M 55 60 L 225 60 L 213 210 Q 210 224 196 224 L 84 224 Q 70 224 67 210 Z" fill="url(#mugShade)"/>
  <ellipse cx="140" cy="60" rx="85" ry="11" fill="#e9e0cf"/>
  <g transform="translate(140 150) scale(0.36)"><g transform="translate(-225 -225)"><use href="#ic-light" width="450" height="450"/></g></g>
</svg>'''

TEE_PATH = ("M 150 30 L 118 30 L 60 65 L 78 128 L 108 108 L 108 270 L 192 270 "
            "L 192 108 L 222 128 L 240 65 L 182 30 L 150 30 Z")
TEE_COLLAR = "M 128 30 Q 150 52 172 30"

TEE_SVG = f'''<svg viewBox="0 0 300 300" class="mock-tee" aria-hidden="true">
  <path d="{TEE_PATH}" fill="#20140D" stroke="#4a3323" stroke-width="2" stroke-linejoin="round"/>
  <path d="{TEE_COLLAR}" fill="none" stroke="#4a3323" stroke-width="2"/>
  <g transform="translate(150 168) scale(0.185)"><g transform="translate(-225 -225)"><use href="#ic-dark" width="450" height="450"/></g></g>
  <text x="150" y="236" text-anchor="middle" font-family="Poiret One" font-size="17" letter-spacing="3" fill="#F3E9DC">RAVIVA</text>
</svg>'''

APPS_HTML = f'''
<section class="panel panel-dark" id="aplicacoes">
  <div class="container">
    <div class="chapter-head">
      <span class="chapter-num">03</span>
      <div>
        <span class="chapter-kicker" style="color:var(--sol)">APLICA&Ccedil;&Otilde;ES</span>
        <h2 class="chapter-title h-display">A marca fora da tela</h2>
      </div>
    </div>
    <p class="lede reveal">Quatro objetos, a mesma assinatura &mdash; sem recompor nada, s&oacute; trocando a escala.</p>

    <div class="app-grid">
      <div class="app-card reveal">
        <div class="app-stage">
          <div class="mock-agenda">
            {icon("dark","")}
            <div class="wm h-display">RAVIVA</div>
            <div class="band"></div>
          </div>
        </div>
        <div class="app-cap"><b>Agenda</b>S&iacute;mbolo isolado, baixo-relevo dourado na capa &mdash; vers&atilde;o reversa, fundo carv&atilde;o.</div>
      </div>

      <div class="app-card reveal">
        <div class="app-stage">
          <div class="mock-browser">
            <div class="chrome"><div class="dots"><span></span><span></span><span></span></div><div class="addr">raviva.com.br</div></div>
            <div class="hero">
              {icon("light","")}
              <div class="wm h-display">R A V I V A</div>
              <div class="tg">Acenda a fa&iacute;sca</div>
              <div class="cta">CONHECER A RAVIVA &rarr;</div>
            </div>
          </div>
        </div>
        <div class="app-cap"><b>Site</b>Lockup vertical completo no topo da p&aacute;gina, sobre fundo claro padr&atilde;o.</div>
      </div>

      <div class="app-card reveal">
        <div class="app-stage">{MUG_SVG}</div>
        <div class="app-cap"><b>Caneca</b>S&iacute;mbolo centralizado em escala confort&aacute;vel, sem wordmark &mdash; superf&iacute;cie curva pede o m&iacute;nimo poss&iacute;vel de elementos.</div>
      </div>

      <div class="app-card reveal">
        <div class="app-stage">{TEE_SVG}</div>
        <div class="app-cap"><b>Camiseta</b>Lockup vertical reduzido, centralizado no peito, vers&atilde;o reversa sobre tecido escuro.</div>
      </div>
    </div>
  </div>
</section>
'''

CLOSING_HTML = f'''
<section class="closing panel-dark">
  {icon("dark")}
  <div class="wm h-display">R A V I V A</div>
  <div class="tg">Acenda a fa&iacute;sca</div>
  <hr class="rule" style="width:140px;">
  <div class="meta">DEFESA DE MARCA &amp; MANUAL DE IDENTIDADE &mdash; VERS&Atilde;O 1.0 &mdash; 2026</div>
</section>
<footer class="doc-footer">RAVIVA &mdash; TODO O SISTEMA VISUAL DESTE DOCUMENTO SEGUE AS REGRAS DESCRITAS NELE MESMO.</footer>
'''

print("apps + closing ok")

SCRIPT_JS = '''
<script>
(function(){
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // reveal on scroll
  var items = document.querySelectorAll('.reveal');
  if (reduced || !('IntersectionObserver' in window)) {
    items.forEach(function(el){ el.classList.add('in'); });
  } else {
    var io = new IntersectionObserver(function(entries){
      entries.forEach(function(e){ if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    items.forEach(function(el){ io.observe(el); });
  }

  // chapter dial: active dot + scroll progress ring
  var dots = document.querySelectorAll('.dial-dot');
  var sections = Array.prototype.map.call(dots, function(d){ return document.getElementById(d.dataset.target); }).filter(Boolean);
  dots.forEach(function(d){
    d.addEventListener('click', function(){
      var target = document.getElementById(d.dataset.target);
      if (target) target.scrollIntoView({ behavior: reduced ? 'auto' : 'smooth' });
    });
  });

  var prog = document.getElementById('dialProg');
  function onScroll(){
    var doc = document.documentElement;
    var max = doc.scrollHeight - doc.clientHeight;
    var pct = max > 0 ? (doc.scrollTop || document.body.scrollTop) / max : 0;
    if (prog) prog.style.strokeDashoffset = String(100 - Math.min(100, Math.max(0, pct*100)));

    var current = sections[0];
    sections.forEach(function(s){ if (s.getBoundingClientRect().top < window.innerHeight*0.5) current = s; });
    dots.forEach(function(d){ d.classList.toggle('active', current && d.dataset.target === current.id); });
  }
  document.addEventListener('scroll', onScroll, { passive:true });
  onScroll();
})();
</script>
'''

HTML = f'''<title>Raviva &mdash; Defesa &amp; Manual de Marca</title>
<script>document.documentElement.classList.add('js');</script>
<style>{CSS}</style>
{SYMBOL_DEFS}
{NAV_HTML}
{COVER_HTML}
{DEFESA_HTML}
{MANUAL_HTML}
{APPS_HTML}
{CLOSING_HTML}
{SCRIPT_JS}
'''

out_path = os.path.join(BASE, "RAVIVA_defesa_e_manual.html")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(HTML)

print("WROTE", out_path, "size:", len(HTML), "bytes(approx chars)")
