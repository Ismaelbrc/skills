# -*- coding: utf-8 -*-
"""O texto do brandbook, na voz de Théo Sampaio.

Marca inalterada: cor, geometria e tipografia vêm de kit.py sem um decimal
de diferença. O que muda aqui é a escrita e a ordem em que as coisas são
contadas.
"""

# ------------------------------------------------------------------ o lixo
LIXO = [
    ("01", "fora", "Letras de vergalhão",
     "Desenhei um alfabeto inteiro em que cada letra era uma barra dobrada, com a "
     "nervura deformando o contorno por dentro. Tecnicamente estava certo. Fui mostrar "
     "pro meu pai. Ele olhou e falou que parecia corda de sisal. Duas semanas de "
     "trabalho pra descobrir que precisão industrial não se comunica com textura "
     "rústica."),
    ("02", "fora", "A casa de uma barra só",
     "Um contorno de casa traçado por uma única linha contínua, sem levantar a caneta. "
     "Bonito de fazer. Existe em umas quatro mil imobiliárias. Se eu vejo esse logo num "
     "caminhão, não sei se é construtora, financiamento ou seguro residencial."),
    ("03", "fora", "O estribo como brasão",
     "Peguei o estribo — aquele retângulo de barra fina com dois ganchos que amarra a "
     "armadura — e tratei ele como emblema. Quem é do ramo entende na hora. Quem não é, "
     "vê uma moldura torta. Marca não pode depender de o cliente já saber."),
    ("04", "fora", "Monograma CBA",
     "Achei que tinha resolvido: três letras, um selo, fim. Fui pesquisar. CBA é a "
     "Companhia Brasileira de Alumínio, do Grupo Votorantim, listada na B3 com o "
     "ticker CBAV3. Alumínio e aço no mesmo balcão de metais. Não dá. Foi a única "
     "ideia que morreu por advogado e não por gosto."),
    ("05", "fora", "O Ç com gancho",
     "O cedilha de AÇO desenhado como o gancho a 90° que a norma manda fazer na ponta "
     "do estribo. Dessa eu gostei de verdade. Ainda gosto. Mas em corpo pequeno o "
     "gancho fechava e o Ç virava um borrão, e uma marca que só funciona grande não "
     "serve pra etiqueta."),
    ("06", "meio", "Três barras, primeira versão",
     "Cheguei nas três listras nas cores do Brasil e comemorei cedo. Estavam grossas e "
     "encostadas uma na outra. Era faixa de bandeira. Só isso. Passei três dias achando "
     "que o problema era a ideia."),
    ("07", "dentro", "A calibragem",
     "O problema não era a ideia. Era a distância. Afinei as listras e abri respiro "
     "entre elas. Do nada pararam de ser bandeira e passaram a ser três barras deitadas "
     "no chão. Esse foi o dia em que o projeto existiu."),
    ("08", "dentro", "A listra sob o nome",
     "Última decisão: onde a listra vive. Embaixo de CASA BRASILEIRA, terminando "
     "exatamente na tinta do A. DE AÇO fica de fora, em verde. Aí ela para de ser "
     "enfeite e passa a sublinhar uma palavra."),
]

# ------------------------------------------------------- pesquisa de nome
NOMES = [
    ("Aço Brasileiro", False,
     "Descreve literalmente aço feito no Brasil. No INPI isso é o que se chama de "
     "expressão de uso comum: registro frágil, e você não consegue impedir o vizinho "
     "de usar. Pagar advogado pra defender isso é jogar dinheiro fora."),
    ("Aço Brasil", False,
     "É o nome do Instituto Aço Brasil, a entidade que representa a siderurgia "
     "nacional. Além de ocupado, a expressão já circula solta no comércio de aço. "
     "Chegar depois e tentar ser dono não termina bem."),
    ("CBA", False,
     "Companhia Brasileira de Alumínio, Grupo Votorantim, B3, ticker CBAV3. Setor "
     "vizinho, mesmo balcão."),
    ("Casa Brasileira de Aço", True,
     "Distintivo. E é distintivo por causa de uma palavra: “Casa”. Sem ela, o nome é "
     "descrição. Com ela, é nome."),
]

# ------------------------------------------------------------ o que se diz
DIZ = [
    "48 estribos, posição N5, entrega quarta.",
    "Chega etiquetado por posição.",
    "Menos perda de ponta de barra.",
    "A barra sai daqui do tamanho da viga.",
    "Romaneio conferido antes de sair.",
    "Se o projeto mudou, refaz. Avisa.",
]
NAO_DIZ = [
    "Soluções completas em armaduras.",
    "Seu parceiro estratégico em aço.",
    "Excelência e comprometimento.",
    "Referência no mercado nacional.",
    "Tecnologia de ponta a serviço da obra.",
    "Construindo o futuro do Brasil.",
]

# --------------------------------------------------------- antes / depois
TROCAS = [
    ("Com nossa tecnologia de ponta e equipe altamente qualificada, oferecemos "
     "soluções completas em corte e dobra, sendo referência de excelência no "
     "mercado de armaduras para construção civil.",
     "A gente corta e dobra a barra na medida do seu projeto e entrega etiquetada "
     "por posição. Sua obra não precisa de serra.",
     "O primeiro fala da empresa. O segundo fala do problema de quem lê. Cortei "
     "34 palavras e ganhei um argumento."),
    ("Prezado cliente, informamos que sua solicitação foi processada com sucesso "
     "e será atendida em breve por nossa equipe.",
     "Romaneio 2026/0431 fechado. Sai da fábrica quinta, chega na obra sexta de manhã.",
     "“Em breve” não é prazo. Mestre de obras não programa equipe com “em breve”. "
     "Data e número, sempre."),
    ("Trabalhamos com o compromisso de agregar valor a cada etapa da jornada do "
     "nosso cliente, do orçamento à entrega.",
     "Você fala a bitola e o formato. A gente corta, dobra, etiqueta e entrega.",
     "Se a frase cabe em qualquer empresa do Brasil, ela não é sua. Essa aqui só "
     "cabe em quem corta e dobra."),
]

# ------------------------------------------------------- glossário do canteiro
GLOSSARIO = [
    ("romaneio",
     "A lista de tudo que vai no carregamento: peça por peça, com posição, bitola, "
     "formato, comprimento e quantidade. É o documento que o mestre confere na "
     "chegada. Se o romaneio está certo, o dia dele está certo."),
    ("posição",
     "O código que o projeto estrutural dá pra cada conjunto de barras idênticas — "
     "N1, N5, N12. É por posição que a armadura é montada na obra. Escrever “N5” é "
     "falar a língua de quem recebe."),
    ("bitola",
     "O diâmetro da barra, em milímetros: 6,3 · 8,0 · 10,0 · 12,5 · 16,0. Sempre com "
     "o Ø na frente e a vírgula decimal. Nunca “10mm” colado."),
    ("CA-50 e CA-60",
     "As classes de aço para concreto armado da NBR 7480. CA-50 é a barra nervurada "
     "comum; CA-60 é o fio, mais fino e mais resistente, usado em tela e estribo leve. "
     "Não são sinônimos e não se trocam."),
    ("estribo",
     "A barra dobrada em retângulo que abraça as barras longitudinais da viga ou do "
     "pilar. Tem gancho na ponta, a 90° ou a 135°, e é o que impede a armadura de "
     "abrir. Metade do que a Casa produz é estribo."),
    ("ponta de barra",
     "O pedaço que sobra quando você corta uma barra de 12 metros no canteiro. É a "
     "perda que o corte e dobra elimina, porque na fábrica a sobra de um pedido vira "
     "peça de outro. Falar de ponta de barra é falar de dinheiro."),
    ("dobra e desdobra",
     "Dobrar é fácil. Desdobrar barra já dobrada é o que ninguém quer fazer, porque "
     "enfraquece o aço no ponto da dobra. É por isso que o projeto tem que estar certo "
     "antes de a máquina rodar."),
    ("canteiro",
     "O terreno da obra. Não é “site”, não é “empreendimento”, não é “projeto”. "
     "Canteiro. É a palavra que a pessoa usa."),
]

# ----------------------------------------------------------- perguntas
PERGUNTAS = [
    ("Não vai parecer bandeira do Brasil demais?",
     "<p>Vai parecer o suficiente. É a intenção. O que segura a marca do lado de cá da "
     "linha é o respiro: cada listra tem 0,140 do corpo de espessura e o vão entre elas "
     "é 0,34 dessa espessura. Bandeira não tem vão. Se alguém encostar as listras, "
     "vira bandeira na hora e a gente perde metade do significado.</p>"),
    ("Podemos fazer uma versão especial pro Natal? Ou pro Sete de Setembro?",
     "<p>Não.</p><p>No Sete de Setembro principalmente não. A marca já é verde, amarela "
     "e azul o ano inteiro. Vestir a marca de Brasil em setembro é como um vendedor "
     "gritar o próprio nome.</p>"),
    ("O concorrente também usa verde e amarelo.",
     "<p>Todo mundo usa verde e amarelo no Brasil. Padaria, time de futebol, corretora. "
     "A cor não é a marca. A marca é o desenho: três listras que começam na tinta do C "
     "e param na tinta do A de BRASILEIRA, embaixo de um nome em Jura Light. Isso "
     "ninguém tem.</p>"),
    ("A gente pode usar só o símbolo, sem o nome?",
     "<p>Em avatar de rede social, favicon e adesivo, sim — nesses lugares o nome "
     "aparece do lado, escrito pela própria plataforma.</p><p>Em proposta, etiqueta, "
     "nota, placa de obra e camiseta, não. Três listras sozinhas não têm nome. Uma marca "
     "de sete meses não pode se dar ao luxo de ser reconhecida sem se apresentar.</p>"),
    ("Precisa mesmo ser essa fonte? A gente já tem outra na empresa.",
     "<p>Precisa. E não é preciosismo: a largura da listra é calculada a partir da "
     "largura de tinta do nome nessa fonte, nesse peso, nesse espacejamento. Trocar a "
     "fonte desalinha a listra do A, e o alinhamento é o único lugar onde essa marca "
     "guarda significado.</p><p>Para texto corrido, contrato e planilha, use Work Sans "
     "e Plex Mono, que estão especificados. Para o nome, é Jura Light.</p>"),
    ("Quanto tempo essa identidade dura?",
     "<p>A parte de baixo — três listras, cores do Brasil, nome em caixa alta — dura "
     "décadas, porque não depende de moda. A parte de cima, que é como a marca aparece "
     "em site e em rede social, vai envelhecer em uns cinco anos como tudo envelhece.</p>"
     "<p>Quando isso acontecer, mexa na de cima. A de baixo fica.</p>"),
]

# ------------------------------------------------------------- promessa
PROMESSA = "Sua obra não precisa de serra."

SUSTENTA = [
    ("Corte por posição de projeto",
     "Cada peça chega com a posição do projeto estrutural — N5, N12 — e não como "
     "barra genérica. Quem monta a armadura procura pela posição, não pelo "
     "comprimento."),
    ("Romaneio fechado na fábrica",
     "A lista é conferida antes de sair, no galpão, com a peça na mão. Não no barro, "
     "às sete da manhã, com o caminhão esperando."),
    ("A sobra de um pedido vira peça de outro",
     "Ponta de barra é dinheiro no chão. Na fábrica ela entra no pedido seguinte; no "
     "canteiro ela vira sucata."),
    ("Aço com classe e rastreio",
     "CA-50 e CA-60 conforme a NBR 7480, com a corrida rastreável. Se o fiscal da obra "
     "pedir o documento, ele existe."),
]

# --------------------------------------------------- não faça, por capítulo
NAO_FACA = {
    "cor": [
        "Amarelo em texto sobre fundo claro. Ele desaparece.",
        "Inverter a ordem das listras. Verde em cima, sempre.",
        "Verde ou azul na listra sobre fundo escuro.",
        "Inventar um quarto tom “pra variar”.",
    ],
    "voz": [
        "Adjetivo sem número atrás.",
        "“Em breve” onde caberia uma data.",
        "Falar da máquina em vez do ganho no canteiro.",
        "Repetir que a empresa é brasileira. A cor já disse.",
    ],
    "peças": [
        "Símbolo sozinho em proposta, nota ou etiqueta.",
        "Marca dentro de moldura, selo ou balãozinho.",
        "Duas composições diferentes na mesma peça.",
        "Alternativa vertical onde a principal caberia.",
    ],
}
