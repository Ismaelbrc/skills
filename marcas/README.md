# Marcas

Identidades desenvolvidas nesta sessão. Cada pasta traz o documento de defesa e
manual em HTML e PDF, os arquivos da marca e o código que gera tudo.

## casa-brasileira-de-aco

**Identidade 1.0 · definida.** Corte e dobra de vergalhão para construção civil.

Três listras paralelas nas cores do Brasil em tom grave, sob CASA BRASILEIRA —
terminando exatamente na tinta do A final. Tipografia Jura Light.

Dois documentos, com funções diferentes. `CASA_BRASILEIRA_brandbook.pdf` é o
documento para **ler**: 34 páginas em oito partes, do negócio à voz, escrito na
primeira pessoa por Théo Sampaio, o publicitário que assina o projeto (o
personagem está descrito em `fonte/autor.md`). `ESPECIFICACAO.md` é o documento
para **consultar**: a ficha técnica com cor, tipografia e geometria, **gerada pelo
próprio código que desenha a marca**. Corrija o código e rode `fonte/spec.py` de
novo — nunca edite a ficha à mão, senão ela e o desenho se separam.

- `marca/` — 35 arquivos em vetor com o texto em curvas, mais PNG em 8000 px e
  1600 px, PDF para gráfica e o símbolo em seis tamanhos de ícone
- `SHA256SUMS.txt` — `sha256sum -c` confere qualquer arquivo que tenha circulado
- `marca/FOLHA-DE-CONFERENCIA.pdf` — as 35 aplicações numa folha

Três coisas que dão errado se ninguém avisar: a listra é **calculada**, não
desenhada; ela **nunca** passa sob DE AÇO; e DE AÇO carrega ajuste óptico por par
de letras, então redigitar o nome num editor perde o ajuste.

## raviva

Marca de luz e ideias, do conceito "fogo é sol estocado".
Slogan: Acenda a faísca.
