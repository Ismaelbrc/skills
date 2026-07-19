---
name: apioficial-branding
description: Aplica a identidade de marca e a voz da apioficial (plataforma de WhatsApp Business API para empresas) a qualquer texto ou material de comunicação — mensagens de WhatsApp, respostas de atendimento/chatbot, copy de site e landing page, e-mails, pitch, posts, materiais de vendas e marketing. A voz da apioficial é construída sobre princípios retóricos de grandes oradores da história (Cícero, Demóstenes, Lincoln, Churchill, Martin Luther King Jr., Kennedy, Obama), adaptados para um tom de tecnologia B2B — clara, direta, confiável, nunca "discursada". Use esta skill sempre que o usuário pedir para escrever, revisar ou dar tom a qualquer texto da apioficial, mesmo que não mencione "branding" ou "voz de marca" explicitamente — por exemplo ao pedir uma mensagem de WhatsApp, um texto de site, uma resposta de suporte, ou copy para campanha.
---

# Identidade de marca — apioficial

A apioficial é uma plataforma de WhatsApp Business API (API oficial do WhatsApp) para empresas: envio de mensagens, automação, atendimento e chatbots. Esta skill define como a marca se expressa em texto — voz, tom, valores e princípios de comunicação — para que qualquer material (mensagem de WhatsApp, site, atendimento, vendas, marketing) soe como a mesma marca, não importa quem escreveu.

Esta skill cobre identidade **verbal** (o que a marca diz e como diz). Identidade **visual** (logo, paleta de cores, tipografia) está fora do escopo — se o pedido for sobre isso, avise o usuário e sugira as skills `canvas-design` ou `theme-factory`, ou peça as diretrizes visuais que ele já tiver.

## Por que oradores como ponto de partida

Grandes oradores resolveram, séculos antes do WhatsApp existir, o mesmo problema que uma marca B2B enfrenta: como fazer uma ideia chegar clara, ser lembrada e gerar ação, em pouco tempo e sem poder repetir o discurso. Cada um deles é forte em uma coisa específica — e cada uma dessas forças vira um princípio de voz da apioficial:

| Orador | Força retórica | Princípio de voz da apioficial |
|---|---|---|
| Cícero | Estrutura clara (exórdio → argumento → conclusão) | Toda mensagem tem começo, meio e uma única ação clara no fim |
| Demóstenes | Persistência e convicção, sem exagero | Afirma sem hedging ("recomendamos" em vez de "talvez seja interessante considerar") |
| Lincoln | Simplicidade e cadência (frases curtas, palavras comuns) | Frases curtas. Zero jargão técnico desnecessário |
| Churchill | Força e repetição do essencial | Repete a ideia central em vez de introduzir uma nova a cada frase |
| Martin Luther King Jr. | Metáfora e ritmo emocional | Usa uma imagem concreta em vez de abstração ("sua mensagem chega em 2 segundos", não "baixa latência") |
| Kennedy | Antítese/quiasmo — inverte a expectativa numa frase de efeito | Reserva para headlines e frases de fechamento; uma inversão memorável, não uma explicação |
| Obama | Storytelling e conexão direta com quem ouve | Fala com "você", situando o leitor num cenário real, não em conceitos |

Leia `references/oradores-e-retorica.md` para o detalhe de cada técnica com exemplos de antes/depois aplicados à apioficial. **Importante:** o registro é de tecnologia B2B, não de palanque — nada de grandiloquência, "!!!", ou tom de comício. A técnica retórica entra pela estrutura e pelo ritmo da frase, nunca pelo tom de discurso.

## Os 4 pilares da voz apioficial

1. **Clara antes de impressionar.** Se o leitor precisa reler a frase, ela falhou. Prefira a palavra simples à palavra bonita.
2. **Direta ao ponto.** Uma mensagem, uma ideia central, uma ação. Não empilhe benefícios.
3. **Confiável, não vendedora.** Fala como quem já resolveu o problema, não como quem está tentando convencer. Evita superlativos ("revolucionário", "único no mercado") — deixa o fato falar.
4. **Humana, mesmo sendo API.** É uma empresa de infraestrutura técnica falando com pessoas (gestores, donos de negócio, times de suporte) — não com desenvolvedores o tempo todo. Tom de conversa, não de manual.

Veja `references/voz-e-tom.md` para vocabulário permitido/evitado e exemplos prontos por canal (WhatsApp transacional, WhatsApp de campanha, site, atendimento, vendas).

## Como aplicar ao escrever ou revisar um texto

1. Identifique o canal (WhatsApp, site, atendimento, e-mail, pitch) — o tom se ajusta em formalidade, mas os 4 pilares não mudam.
2. Escreva a versão mais simples e direta possível primeiro. Corte qualquer frase que não sirva à ação principal.
3. Aplique **um** princípio retórico da tabela acima que se encaixe no que o texto precisa fazer (ex.: campanha de reengajamento → Churchill/repetição da ideia central; onboarding → Lincoln/simplicidade; texto institucional/pitch → Obama/storytelling situando o leitor; headline ou frase de fechamento → Kennedy/antítese).
4. Releia como se fosse o gestor de uma pequena/média empresa recebendo a mensagem, não um engenheiro. Se soar a discurso, corte o excesso — retórica aqui é ferramenta de clareza, não de espetáculo.

## O que ainda falta definir (perguntar ao usuário antes de tratar como fixo)

Estes pontos ainda não foram fechados com o dono da marca — trate os exemplos desta skill como ponto de partida ajustável, não como definição final:

- **Público-alvo específico:** hoje assumimos "pequenas e médias empresas no Brasil que atendem clientes por WhatsApp", mas isso pode ser mais específico (segmento, porte, região).
- **Tagline/slogan oficial:** ainda não existe um definido.
- **Valores da marca além da voz** (missão, propósito) — não inventar, perguntar quando for relevante para o material em questão.
- **Nome comercial exato** ("apioficial" vs. alguma grafia/capitalização específica) — usar como o usuário escrever até ele confirmar um padrão.

Se o pedido do usuário depender de um desses pontos (ex.: um pitch institucional que cite a missão da empresa), pergunte antes de inventar. Para o dia a dia (mensagens, respostas, copy pontual), os 4 pilares e os exemplos de `references/` já são suficientes para escrever no tom certo.
