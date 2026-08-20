# CASA BRASILEIRA DE AÇO — ficha técnica da marca

Identidade **1.0 · definida**. Corte e dobra de vergalhão para construção civil.

> Este arquivo é **gerado** por `fonte/spec.py` a partir do código que desenha
> a marca. Não edite à mão: corrija o código e rode de novo, senão a ficha e
> o desenho se separam.

## Conceito

Três listras paralelas nas cores do Brasil sob CASA BRASILEIRA. Para quem olha rápido, é a bandeira: diz Casa Brasileira. Para quem é do ramo, são três vergalhões alinhados: diz De Aço. A calibragem — espessura e respiro — é o que decide qual leitura domina.

**Regra de ouro.** A listra é calculada a partir das métricas da fonte, nunca desenhada à mão. Mudou o corpo ou a entreletra? Rode fonte/vetor.py de novo — não corrija esticando no editor.

## Cor

| Nome | HEX | RGB | CMYK calculado | Uso |
|---|---|---|---|---|
| Verde Casa | `#006B3C` | 0 · 107 · 60 | 100 · 0 · 44 · 58 | DE AÇO, listra superior, botões, links |
| Amarelo Ouro | `#F2B705` | 242 · 183 · 5 | 0 · 24 · 98 · 5 | listra do meio; acento. Nunca texto sobre fundo claro |
| Azul Profundo | `#002B5C` | 0 · 43 · 92 | 100 · 53 · 0 · 64 | listra inferior, fundo institucional, frota |
| Tinta | `#14161C` | 20 · 22 · 28 | 29 · 21 · 0 · 89 | CASA BRASILEIRA e texto corrido |
| Papel | `#F5F4F0` | 245 · 244 · 240 | 0 · 0 · 2 · 4 | fundo claro padrão |
| Branco | `#FFFFFF` | 255 · 255 · 255 | 0 · 0 · 0 · 0 | fundo alternativo e marca reversa |
| Cinza | `#8A8B90` | 138 · 139 · 144 | 4 · 3 · 0 · 44 | fios, molduras, elementos de apoio |
| Cinza texto | `#5A5C60` | 90 · 92 · 96 | 6 · 4 · 0 · 62 | legendas e texto secundário |

⚠️ O HEX/RGB e a especificacao para tela e e definitivo. O CMYK listado e conversão aritmética: serve para pedir a prova, não para fechar a tiragem. Pantone não está especificado de propósito — precisa ser escolhido em prova impressa com a gráfica, a partir do CMYK, e só depois anotado aqui. Pintura de frota exige o mesmo: prova numa amostra do substrato.

## Tipografia

- **Jura Light (300)** — sempre alta, no nome e nas etiquetas
- arquivo `Jura-Light.ttf`, 2000 unidades por em
- versão `Version 5.106`
- licença: SIL Open Font License 1.1
- SHA-256 da fonte: `c891a381df056b2c4dfe85841e911bf45da0890fa21a7b2692cbe5ea1f505e1e`
- texto corrido: Work Sans (Regular 400 / Bold 700)
- dados e legendas: IBM Plex Mono (Regular 400)
- descartadas no caminho: Italiana, Poiret One, Outfit, Work Sans, Arsenal SC

O SHA-256 acima existe para um motivo: se alguém no futuro instalar outra
Jura e o desenho mudar, é assim que se descobre. Os arquivos em `marca/`
já estão em curvas e não dependem da fonte.

## Geometria

*todas as medidas são fração do corpo (font-size) do nome.*

| Parâmetro | Valor |
|---|---|
| Entreletra base | 0.155 |
| Vão óptico alvo | 0.2698 |
| Vão de palavra | 0.6445 |
| Espessura da listra | 0.14 |
| Respiro entre listras | 0,34 x a espessura |
| Topo da listra abaixo da base | 0.32 |
| Início da listra | borda esquerda da tinta do C (não o avanço do glifo) |
| Fim da listra | borda direita da tinta do último A de BRASILEIRA |
| Listra nunca | sob DE AÇO |
| tinta CASA BRASILEIRA (corpo 1) | 9.8965 |
| tinta DE ACO com ajuste (corpo 1) | 3.97075 |
| tinta do nome inteiro (corpo 1) | 14.51175 |
| altura das tres listras (corpo 1) | 0.5152 |
| X | altura do conjunto das três listras |
| Respiro mínimo em volta | 1 X |
| Mínimo em tela | 15 px de corpo |
| Mínimo impresso | 9 mm de corpo |

### Ajuste óptico de DE AÇO

D, E, Ç e O têm lateral mais larga na Jura Light. Com a mesma entreletra numérica o vão de tinta de DE AÇO sai 8% maior que o de CASA BRASILEIRA. O que se iguala é o vão, não o número.

| Par | Correção (fração do corpo) |
|---|---|
| D-E | -0.0552 |
| espaco DE ACO | +0.0550 |
| A-C cedilha | +0.0203 |
| C cedilha-O | -0.0342 |

### Bloco de listras solto

Usado em alternativas 1, 2, 3 e símbolo. Comprimento 2,0 x a altura do bloco; espessura 0,28 da altura, normalizada junto com o respiro; respiro 0,34 x a espessura.

## Composições

**principal** — `CBA-principal-*`  
nome em uma linha, listra sob CASA BRASILEIRA. padrão em tudo. Só trocar quando a proporção do espaço impedir.

**alt1-horizontal** — `CBA-alt1-horizontal-*`  
bloco de listras à esquerda, nome em duas linhas. espaços largos e baixos onde a principal ficaria pequena

**alt2-vertical** — `CBA-alt2-vertical-*`  
bloco de listras acima, nome centralizado em duas linhas. espaços estreitos e altos

**alt3-uma-linha** — `CBA-alt3-uma-linha-*`  
bloco de listras à esquerda, nome inteiro em uma linha. faixas muito baixas: cabeçalho de site, rodapé, assinatura de e-mail

**simbolo** — `CBA-simbolo-*`  
as três listras isoladas em quadro quadrado. avatar, favicon, adesivo. Elemento derivado: nunca substitui a marca em documento, proposta ou etiqueta.

## Versões de cor

- **cor** — fundo transparente, para aplicar sobre fundo claro próprio
- **papel** — fundo #F5F4F0 — o padrao do sistema
- **branco** — fundo branco puro
- **reversa-azul** — sobre #002B5C; DE AÇO em #F2B705, listra branco/amarelo/branco
- **reversa-preto** — sobre #14161C; mesma regra do azul: DE AÇO em #F2B705, listra branco/amarelo/branco
- **mono-preto** — uma cor: gravação, carimbo, jornal
- **mono-branco** — uma cor sobre fundo escuro: bordado, serigrafia, pintura de frota

## Formatos

- **svg** — vetor, texto em curvas — não depende da Jura instalada
- **pdf** — vetor para grafica
- **png-alta** — 8000 px na maior dimensao
- **png-web** — 1600 px na maior dimensao
- **icones** — símbolo quadrado em 1024, 512, 256, 128, 64 e 32 px

## Nunca

- esticar, achatar ou distorcer em qualquer proporção
- estender a listra sob DE AÇO — desfaz a única regra de significado da marca
- trocar as cores ou a ordem das listras
- inclinar ou rotacionar a assinatura
- aplicar sobre fundo que anule o amarelo
- trocar a tipografia ou redigitar o nome em outra fonte
- redesenhar a listra à mão em vez de recalcular pela métrica
- usar o símbolo sozinho onde o nome precisa aparecer

## Inventário

171 arquivos. O SHA-256 de cada um está em `ESPECIFICACAO.json` e em
`SHA256SUMS.txt`. Para conferir se um arquivo que circulou por aí ainda é o
original:

```
sha256sum -c SHA256SUMS.txt
```

### Assinaturas em vetor

| Arquivo | viewBox |
|---|---|
| `CBA-alt1-horizontal-branco.svg` | 1144x278 |
| `CBA-alt1-horizontal-cor.svg` | 1144x278 |
| `CBA-alt1-horizontal-mono-branco.svg` | 1144x278 |
| `CBA-alt1-horizontal-mono-preto.svg` | 1144x278 |
| `CBA-alt1-horizontal-papel.svg` | 1144x278 |
| `CBA-alt1-horizontal-reversa-azul.svg` | 1144x278 |
| `CBA-alt1-horizontal-reversa-preto.svg` | 1144x278 |
| `CBA-alt2-vertical-branco.svg` | 857x440 |
| `CBA-alt2-vertical-cor.svg` | 857x440 |
| `CBA-alt2-vertical-mono-branco.svg` | 857x440 |
| `CBA-alt2-vertical-mono-preto.svg` | 857x440 |
| `CBA-alt2-vertical-papel.svg` | 857x440 |
| `CBA-alt2-vertical-reversa-azul.svg` | 857x440 |
| `CBA-alt2-vertical-reversa-preto.svg` | 857x440 |
| `CBA-alt3-uma-linha-branco.svg` | 1434x223 |
| `CBA-alt3-uma-linha-cor.svg` | 1434x223 |
| `CBA-alt3-uma-linha-mono-branco.svg` | 1434x223 |
| `CBA-alt3-uma-linha-mono-preto.svg` | 1434x223 |
| `CBA-alt3-uma-linha-papel.svg` | 1434x223 |
| `CBA-alt3-uma-linha-reversa-azul.svg` | 1434x223 |
| `CBA-alt3-uma-linha-reversa-preto.svg` | 1434x223 |
| `CBA-principal-branco.svg` | 1574x230 |
| `CBA-principal-cor.svg` | 1574x230 |
| `CBA-principal-mono-branco.svg` | 1574x230 |
| `CBA-principal-mono-preto.svg` | 1574x230 |
| `CBA-principal-papel.svg` | 1574x230 |
| `CBA-principal-reversa-azul.svg` | 1574x230 |
| `CBA-principal-reversa-preto.svg` | 1574x230 |
| `CBA-simbolo-branco.svg` | 512x512 |
| `CBA-simbolo-cor.svg` | 512x512 |
| `CBA-simbolo-mono-branco.svg` | 512x512 |
| `CBA-simbolo-mono-preto.svg` | 512x512 |
| `CBA-simbolo-papel.svg` | 512x512 |
| `CBA-simbolo-reversa-azul.svg` | 512x512 |
| `CBA-simbolo-reversa-preto.svg` | 512x512 |
| `FOLHA-DE-CONFERENCIA.svg` | 3220x1178 |
