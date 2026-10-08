<!-- converted from oo-na-pratica.html by henriquefy.ingest.html_to_md on 2026-10-08; see kb/courses/README.md for provenance and license -->

HB Network · Documentação de curso

# Orientação a Objetos na Prática

As 23 aulas, a modelagem do Banco Imobiliário e o código real do simulador — lido, executado e comentado linha a linha.

Instrutor: **Henrique Bastos** · Canal [HB Network](https://www.youtube.com/@hbnetworkoficial) · Playlist: [Orientação a Objetos na Prática](https://www.youtube.com/watch?v=lrQOL7Lpdtw&list=PLeKXYyZCJHxemNCYYvDUw0wRsMiN7aX1m) · Repositório: [github.com/henriquebastos/monopoly](https://github.com/henriquebastos/monopoly)

Documento elaborado a partir das transcrições automáticas das 23 aulas (536.317 caracteres de legenda, ~11.600 marcações de tempo), da leitura integral do código-fonte do repositório e da execução real da suíte de testes e do simulador de Monte Carlo.

## 1. Visão geral do curso

“Orientação a Objetos na Prática” é uma série de **23 aulas**, publicadas em 14 de setembro de 2023, que somam **28.842 segundos — 8 horas e 42 segundos** de material. As 23 aulas acumulavam, na data da coleta, **2.637 visualizações**. O curso não é uma introdução à sintaxe de classes: é uma reconstrução do paradigma desde a motivação histórica até a implementação completa de um simulador de Banco Imobiliário em Python, construído ao vivo, guiado por testes.

O que distingue esta série do material introdutório comum é a ordem. As quatro primeiras aulas tratam de *programação “no metal”*, GOTO, rotinas sem pilha de chamada, funções reentrantes, alocação dinâmica, ALGOL e Simula — ou seja, o aluno precisa entender *o que doía* antes de aprender o que a orientação a objetos resolve. Só na aula #14 começa o estudo de caso, e a implementação só começa na #18. As cinco últimas aulas são codificação ao vivo, refatoração e simulação estatística.

| Dimensão | Valor | Observação |
|---|---|---|
| Aulas | 23 | Playlist completa, numerada de #01 a #23. |
| Duração total | 28.842 s (8h 00min 42s) | Soma das durações informadas pelos metadados de cada vídeo. |
| Aula mais curta / mais longa | 197 s (#02) / 2.759 s (#21) | A #21 — *turn e game.py* — é também a mais experimental. |
| Visualizações (coleta) | 2.637 | Distribuição desigual: a #01 tem 384; a #21, apenas 25. |
| Transcrições | 23 de 23 disponíveis | Legenda *automática* em português; não há legenda humana. |
| Código do projeto | 7 módulos · 5.857 bytes | Mais 4 arquivos de teste com 40 testes. A seção 21 reconstrói o módulo que a aula #23 escreve ao vivo, elevando a suíte a 53 testes. |
| Bloco prático | aulas #18 a #23 | Da primeira linha de `player.py` ao simulador de 10.000 partidas. |

O curso termina com um simulador estatístico: 10.000 partidas de Banco Imobiliário disputadas por quatro estratégias automáticas, com o tabuleiro gerado por distribuição normal. É uma escolha pedagógica forte — o aluno não vê um programa de exemplo, vê *um experimento* que produz um resultado numérico inesperado e discutível.

Nota de método: este documento separa rigorosamente duas fontes. A **narrativa das aulas** vem das transcrições — as citações são literais, com as marcas da legenda automática preservadas. A **análise de código** vem do repositório público, clonado e lido integralmente: todo trecho citado traz arquivo e número de linha, e todo número de teste ou de simulação é saída real de terminal desta sessão. A seção 21 leva isso adiante: reconstrói o único módulo que a aula escreve e o repositório não publica, e o verifica por execução — inclusive contra o próprio repositório.

## 2. Filosofia e método de ensino

O curso tem um método declarado, e ele aparece na fala do instrutor antes de aparecer no código. São seis decisões pedagógicas que atravessam as 23 aulas.

### 2.1 “Pensamento positivo” sobre o código

O ciclo de trabalho é escrever primeiro o que se quer que exista — o teste — e deixar que os nomes ainda não existam. Na aula #06 ele descreve o efeito prático disso no editor:

> “veja que o meu pai Charme o meu editor ele tá aqui marcando essa cobrinha por debaixo dos nomes porque ele não reconhece esses nomes não tem problema eu ignoro isso eu tô aqui fazendo uma espécie de pensamento positivo sobre o código dessa maneira eu não me distraio com os detalhes de implementação e o foco em descobrir precisamente as interfaces que eu desejo” Aula #06, 1:41 — “pai Charme” é corrupção da legenda para PyCharm.

### 2.2 De dentro para fora: “comendo pelas beiradas”

A implementação não começa pela integração, e sim pelas folhas do sistema — as entidades com responsabilidade única e poucas relações. É o inverso do instinto de quem quer “ver funcionando”:

> “Eu quero começar comendo comendo pelas beiradas né indo pelas folhas né pelas folhas do sistema me organizar Aqui” Aula #18, 0:16.

E ele explica por que o caminho é esse: *“eu vou fazer de dentro para fora né que é pegando o jogador pegando a propriedade Porque eles estão com responsabilidades únicas e poucas relações”* (aula #18, 1:46).

### 2.3 A regra mais simples, e a decisão postergada

Duas regras aparecem na modelagem (#16) e são cobradas na implementação: escolher a regra *mais simples* entre as possíveis, e *postergar decisões* enquanto o entendimento cresce. Na aula #18 ele aplica a primeira de forma explícita, mudando a especificação da aula #16: *“não é mais fácil quando o cara não tem dinheiro para pagar ninguém recebe nada e o cara sai do jogo simplesmente isso entendeu ninguém recebe nada o cara sai do jogo”* (11:39).

### 2.4 O português é a ferramenta de modelagem

A afirmação mais forte do curso está na aula #16, e é uma afirmação sobre linguagem, não sobre notação:

> “por isso que eu sempre digo que a ferramenta mais importante de modelagem ao português” Aula #16, 0:28 — legenda automática registra “ao português”; a fala é “é o português”.

A decupagem — reescrever o texto do cliente parágrafo por parágrafo, em frases curtas e sem ambiguidade — é apresentada como etapa *anterior* à modelagem. E é nela que ele encontra um erro no vocabulário do próprio cliente (a aula #16 discute “rodada” versus “turno”).

### 2.5 Contra a notação formal: UML, BDD e o “arquiteto astronauta”

O curso é explicitamente crítico de três coisas. Sobre UML, na aula #13: *“o ML apesar de você poder usar ele com o diagrama Zinho para poder explicar e orientar uma boa conversa se propõe a ser uma linguagem mas não tem nem condicional”* (0:14) — a crítica é precisa: **uma notação sem condicional não modela fluxo**. Sobre BDD: *“o programador vira babá de Project Manager Com certeza absoluta o bdd é um convite para isso”* (4:18). E, na aula #11, o inimigo declarado da modelagem tem nome:

> “o maior desafio quando o assunto é modelagem de software é o que a gente conhece como síndrome do arquiteto astronauta” Aula #11, 2:26 — o desenho de soluções imaginárias antes do contato com o problema.

### 2.6 Não é um showcase de Python

Decisão de escopo declarada na aula #18, que muda como o código deve ser lido: *“não é fazer um show case de Python seleção aqui é resolver um problema orientado objeto eu vou usar Python por acaso”* (1:06). É por isso que o repositório evita decoradores exóticos, metaclasses e genéricos avançados — as quatro estratégias do jogo são quatro `@staticmethod` com uma linha cada, para que a ideia seja transportável a Java, C# ou Ruby.

## 3. Os cinco pilares conceituais

Estes cinco conceitos são enunciados nas aulas teóricas e depois *verificados* no código real. Vale lê-los com o repositório ao lado — cada um tem uma linha correspondente no projeto.

### 3.1 Indireção

É o pilar central, e a aula #09 é dedicada a ele. Definição dada no curso, e a origem da palavra:

> “se você procurar no dicionário você não vai encontrar exatamente essa palavra você encontra indireto mas não encontra em direção isso porque em direção é um termo que vende indirection da Ciência da Computação” Aula #09, 0:27 — “em direção” é a legenda automática lendo “indireção”.

> “a definição mais simples é que é a capacidade de referenciar algo usando um nome referência o continente ao invés do valor em si” Aula #09, 0:39.

A metáfora usada para materializá-la é o **barramento** de uma CPU: em vez de ligar cada chip a todos os outros, cria-se uma via comum com uma unidade de controle que decide quem fala com quem. O ganho é converter amarração estática em **amarração dinâmica** em tempo de execução — *“é como se tivesse em vez de ter uma uma amarração estática sobre o que tá acontecendo a gente faz uma amarração dinâmica em tempo de execução”* (aula #09, 6:29). A fonte externa citada é o material de Ben Eater sobre o barramento de 8 bits.

### 3.2 Troca de mensagens

A afirmação mais contraintuitiva do curso, na aula #05: os objetos não são a sacada.

> “Não dá para evitar isso completamente, mas o que a gente não quer é que isso aconteça com todas as partes do código. A grande sacada da orientação objetos não foram os objetos, foi o sistema de mensagem. Exatamente. Na orientação objetos não existe mais chamada de função. O que existe são trocas de mensagens.” Aula #05, 7:31.

E a consequência prática, formulada na aula #10: como o emissor envia a mensagem *sem saber* como o receptor vai interpretá-la, a decisão migra para o receptor. Por isso o fecho do curso sobre o paradigma é a expressão **“programação imperativa, porém cooperativa”** (aula #10, 14:03) — imperativa porque se controla o fluxo; cooperativa porque o controle é distribuído entre os objetos.

### 3.3 Complexidade e entropia

A razão de existir do paradigma, segundo a aula #05: cenários em que “o todo é muito maior do que a soma das partes”. E o diagnóstico de por que um sistema se degrada:

> “Não existem dois softwares iguais no mundo. Se fossem iguais, você poderia simplesmente copiá-los. Então, mesmo quando o software faz a mesma coisa, o fato de serem implementações diferentes faz com que sejam sistemas complexos completamente diferentes.” Aula #05, 1:16.

Na aula #17, a análise da própria modelagem é descrita como *“uma análise de complexidade ciclomática do modelo”*, e o critério de qualidade é geométrico: **o modelo deve evitar ciclos e tender a uma árvore**.

### 3.4 Localidade

O critério que decide *onde* cada responsabilidade mora. Na aula #15, ele é imposto como regra de trabalho:

> “modelagem orientada objetos a gente não olha globalmente gente olha localmente contextual” Aula #15, 0:22.

E a advertência simétrica, na aula #12: *“quando você tá modelando o sistema de objetos você não pode pensar Global se você pensar Global você vai impor uma visão um pressuposto em cima do problema e isso vai deformar a sua modelagem você tem que pensar local”* (1:38).

### 3.5 Responsabilidade única

Citada explicitamente na aula #15 — *“princípio da responsabilidade única que ajuda você a reduzir o acoplamento”* (8:34) — e aplicada com severidade: o jogador termina como “quase uma conta bancária”, sem posição e sem coleção de propriedades, porque *“a responsabilidade do jogador é lidar com dinheiro é isso então esse jogador ele é quase igual uma conta bancária”* (aula #17, 3:25).

## 4. O arco histórico: de 1960 a Alan Kay

Três aulas inteiras (#02, #03, #04) são dedicadas à história, e isso não é digressão: é a tese do curso. Quem não sente a dor do contexto anterior não entende por que o paradigma tem a forma que tem.

### 4.1 O “quando” antes do “por quê”

> “objeto surgiu na década de 60 e amadureceram na década de 70 onde de fato se estabeleceu na estação objetos como a gente conhece hoje” Aula #02, 0:13.

O retrato da época inclui computadores do tamanho de uma sala, a ARPA, o *time sharing* e a padronização tardia de texto: *“para você ter uma noção nada era padronizado tanto que cada computador tinha sua forma de representar texto e só em 1963 surgiu a tabela asic que conseguiu dar alguma ordem nesse caos”* (aula #02, 1:40 — “asic” é ASCII).

### 4.2 O que existia antes: a dor concreta

A aula #03 é a mais técnica do bloco histórico e descreve os três estágios anteriores. Programar “no metal”:

> “antes de surgir natação objetos programar era uma atividade revmetal literalmente você tinha que ir direto no metal fazer um monte de coisa os computadores eram enormes e caríssimos” Aula #03, 0:00 — “revmetal” é a legenda colando “era uma atividade … no metal”.

Sem gerenciamento de memória, dados globais: *“essa falta de gerenciamento de memória na formação imperativa ela tem consequências muito grandes porque significa que todos os seus dados são globais e qualquer área do código pode tocar aquele mesmo endereço”* (1:02). Daí o problema clássico da reentrância (2:16). Depois, a programação estruturada traz blocos e escopo via pilha de chamada; a tipagem estática traz verificação, mas engessa — *“todas as funções todos os endereços de memória onde as funções começam e terminam eles são definidos em tempo de compilação isso é como se seu código fosse costurado fisicamente na hora que você compila ele”* (6:02).

O ponto de virada é uma pergunta de Kristen Nygaard, diante de uma simulação de reator nuclear com dados de naturezas distintas: *“e se eu conseguisse colocar o código associado com dado”* (7:47). E o resultado: *“e foi dessa maneira que o símbolo implementou a orientação objeto pela primeira vez mas de uma maneira estéticamente duvidosa porque ainda não tinha ali todo o poder da natação objetos o que tinha ali ela quer a semente fundamental”* (9:11 — “o símbolo” = Simula).

### 4.3 A descoberta: *outsight*, não *insight*

A aula #04 reconstrói o caminho de Alan Kay por referências externas, e o vocabulário é deliberado:

> “foi que o alenquei teve o que ele chama de outside em Oposição a Insight porque ele não teve uma epifania interna mas na verdade ele foi alimentado externamente de referências que fizeram com que o que ele tava vendo fora dele mesmo tivesse sentido” Aula #04, 2:21 — a palavra é *outsight*.

As referências listadas: a álgebra e a morfogênese, os computadores Burroughs B220 e B5000, o Sketchpad de Ivan Sutherland, o artigo de Gordon Moore, a linguagem Logo de Seymour Papert e o NLS de Douglas Engelbart. O princípio comum a todas é o mesmo da seção anterior — **indireção**. A síntese de Kay, citada na aula:

> “Isso culmina numa das frases mais difíceis de entender do lancay quando ele fala que orientação objetos é quando você para de olhar o software como código e começa a entender que o seu software é composto de múltiplos pequenos computadores com o mesmo poder de um computador normal” Aula #04, 11:15.

O elo que liga tudo é citado como princípio de design recursivo, atribuído a Bob Barton: *“o princípio básico de um design recursivo é fazer com que as partes têm o mesmo poder do todo”* (aula #04, 9:32). O desfecho histórico é o Smalltalk como sistema vivo:

> “que implementou o conceito do software como organismo vivo onde você tem o próprio sistema operacional com seus objetos que permite você enquanto está explorando e usando o sistema alterar o seu próprio comportamento mudando o código durante o tempo de execução” Aula #04, 20:42.

A mesma indireção que o curso ensina como técnica aparece, aqui, como mecanismo histórico: a linguagem foi inventada para referenciar comportamento por nome, e não por posição fixa — e é exatamente essa propriedade que o simulador do Banco Imobiliário vai usar.

## 5. As 23 aulas em uma tabela

Duração, alcance e função de cada aula no arco do curso. As visualizações são a fotografia da coleta e ajudam a localizar o ponto em que a série perde audiência: o bloco prático (#18–#23) tem, em média, menos da metade do público das aulas teóricas.

| # | Título | Duração | Views | Função no arco |
|---|---|---|---|---|
| 01 | O Peixe que não sabe que existe água | 4:00 | 384 | Diagnóstico: o problema é de percepção, não de sintaxe. |
| 02 | Por que surgiu a Orientação a Objetos? | 3:17 | 212 | Os anos 60, a ARPA, o ASCII, Simula, Alan Kay. |
| 03 | O que existia antes da Orientação a Objetos? | 9:29 | 135 | Do “metal” a ALGOL: globais, reentrância, tipagem estática. |
| 04 | A descoberta da essência da Orientação à Objetos | 22:34 | 158 | *Outsight*, indireção, Smalltalk, Dynabook. |
| 05 | Solucionando a Complexidade | 13:22 | 137 | Entropia, acoplamento, ADTs e o primado da mensagem. |
| 06 | Métodos não são Funções | 23:31 | 207 | Primeiro código: *bound method*, `getattr`, polimorfismo. |
| 07 | O Poder Polimórfico das Hierarquias de Classes | 39:21 | 160 | Inteiros binários: acoplamento → `Factory` → registro. |
| 08 | Evitando a Programação Procedural com Objetos | 10:59 | 89 | `IntervalMap`: vazamento de responsabilidade e ADTs de Liskov. |
| 09 | Uma Análise Direta Sobre Indireção | 22:28 | 79 | O barramento como metáfora; amarração dinâmica. |
| 10 | Quando Procedural Vira Orientado à Objetos? | 14:34 | 59 | O efeito do movimento; o objeto como *proxy*. |
| 11 | O que é Modelagem? | 10:29 | 200 | Arquiteto astronauta; pensar local; as 5 ferramentas. |
| 12 | Mentalidade POO | 6:56 | 62 | Modelo mental: *time frame* eventual; a tia Cotinha. |
| 13 | Técnicas de Modelagem | 7:07 | 60 | Crítica a UML e BDD; os CRC cards entram em cena. |
| 14 | O Banco Imobiliário | 32:10 | 104 | Primeira passada no enunciado; substantivos, verbos, “outros”. |
| 15 | Banco Imobiliário: Modelagem CRC | 42:00 | 123 | CRC ao vivo; nasce e morre a classe `Competidores`. |
| 16 | Banco Imobiliário: A Decupagem | 28:05 | 80 | Glossário do domínio; o erro de “rodada” versus “turno”. |
| 17 | Banco Imobiliário: Revisando a Modelagem | 18:28 | 122 | Reorganização por temas; ciclos, árvore, inversão de dependência. |
| 18 | players.py | 39:40 | 93 | TDD pelas folhas; exceções de domínio; composição. |
| 19 | realstate.py | 19:10 | 36 | A propriedade como mediadora; inversão de dependência. |
| 20 | board.py | 14:36 | 41 | Dicionário jogador→posição; `divmod` e a volta. |
| 21 | turn e game.py | 45:59 | 25 | O turno não é objeto; `Game.run()`; `itertools.cycle`. |
| 22 | simulation.py | 12:07 | 36 | Monte Carlo, distribuição normal, multiprocessing. |
| 23 | competitors.py | 40:20 | 35 | Refatoração guiada por dívida técnica; exclusão lógica. |

**Leitura da tabela.** O pico de audiência está na aula #01 (384) e o fundo, na #21 (25) — uma queda de 93%. O ponto de inflexão está na #10 (59): é ali que o curso deixa de ser “o que é OO” e passa a ser “como se pensa em OO”, e o público cai à metade. Isso é coerente com a tese da aula #01: o material mais valioso — a mecânica interna do paradigma — é justamente o que menos gente assiste. Note também a assimetria das aulas práticas: a #21, que contém a decisão de design mais interessante do projeto (a recusa em criar um objeto `Turno`), é a menos vista de todas.

## 6. Parte I — A pré-história e a descoberta (aulas #01–#04)

Quatro aulas, 39 minutos, nenhuma linha de código. O objetivo é instalar o problema antes de oferecer a solução.

Aula 01

### O Peixe que não sabe que existe água

240 s · video_id `lrQOL7Lpdtw` · 384 views · 34 likes · [assistir](https://www.youtube.com/watch?v=lrQOL7Lpdtw)

O diagnóstico de abertura: a dificuldade com orientação a objetos não é de sintaxe, é de **percepção**. Quem nasceu num mundo onde o paradigma já existia não consegue enxergá-lo — é o peixe que não sabe que existe água. A metáfora vem da irmã, 16 anos mais nova, que cresceu com internet: tem desempenho superior em ferramentas, mas quando algo falha não consegue localizar a falha nas camadas, porque opera num nível de abstração alto demais. Somam-se duas causas: o ensino por alegorias (animal, cachorro, gato) e um problema de *mentalidade* — o programador entra no mercado como consumidor de tecnologia e abandona os fundamentos.

- `[0:09]` A metáfora-central: o problema é o do peixe que não sabe que existe água.
- `[0:40]` O desempenho alto com abstração alta: falha sem saber onde falhou.
- `[1:18]` Transposição do diagnóstico para a OO: usa-se a linguagem sem saber se é o certo.
- `[2:16]` Segunda causa: problema de mentalidade — virar consumidor de tecnologia.
- `[2:57]` O estigma de que compilador e parser são “coisa de outro mundo”.

> “mas quando alguma coisa não sai como esperado aí que a coisa fica difícil porque ela tá num nível tão elevado de abstração que ela não consegue entender onde em todo o processo em todas as camadas onde pode estar falha possível” 1:40

> “mas os conceitos os fundamentos essenciais para a gente compreender o porquê das coisas a gente tem que perseguir” 3:20

Aula 02

### Por que surgiu a Orientação a Objetos?

197 s · video_id `KCelJnHLKos` · 212 views · 16 likes · [assistir](https://www.youtube.com/watch?v=KCelJnHLKos)

A resposta começa pelo *quando*: as ideias nasceram nos anos 60 e amadureceram nos 70. O retrato da década — Guerra Fria, crise dos mísseis, ditadura no Brasil, Tropicália, computadores do tamanho de uma sala, *time sharing*, ARPA, chips — explica as condições que permitiram a invenção. A primeira linguagem a implementar a essência foi o **Simula**, criada por dois autores noruegueses que precisavam simular a construção do primeiro reator nuclear do país. Quem cunhou o termo e formalizou os detalhes foi **Alan Kay**, com publicação em 1972.

- `[0:29]` A década de 60 no mundo: Guerra Fria, Cuba, ditadura, festivais.
- `[0:44]` Computadores enormes, caríssimos, sem sistema de arquivos.
- `[1:15]` *Time sharing*: vários terminais para um computador — a inovação da época.
- `[1:40]` Nada padronizado até o ASCII, em 1963.
- `[2:36]` Alan Kay formaliza e publica; depois vieram muitas linguagens.

> “a coisa mais moderna que deixou todo mundo animado na época era o time sharing a capacidade de várias pessoas conseguirem interagir com o mesmo computador através de terminais quero Na verdade uma espécie de máquina de escrever ligada no fim” 1:15

Atenção a um detalhe que a legenda automática destrói por completo: **Smalltalk** aparece grafado como “malth”, “mau toque”, “mortal” e “súmula” ao longo do arquivo; os autores noruegueses, Kristian Nygaard e Ole-Johan Dahl, aparecem como “Cristian negard e Oleiro”. Nenhum identificador desta aula pode ser lido da transcrição — a única fonte confiável é a literatura.

Aula 03

### O que existia antes da Orientação a Objetos?

569 s · video_id `4y64J_Buw9Y` · 135 views · 15 likes · [assistir](https://www.youtube.com/watch?v=4y64J_Buw9Y)

A aula mais técnica do bloco histórico, e a que mais paga dividendos depois. Descreve três estágios anteriores ao paradigma e a dor concreta de cada um: **programação no metal** (sem sistema operacional mediando, dados globais, reaproveitamento nulo); **programação estruturada** (blocos, hierarquia, escopo via pilha de chamada — o que torna possíveis funções, reentrância e recursividade); **tipagem estática** (o compilador verifica, mas engessa, porque endereços de função são fixados em tempo de compilação). O ponto de virada é a pergunta de Nygaard, diante de uma simulação com dados de naturezas distintas.

- `[0:00]` Programar “no metal”: a máquina inteira para si, um programa por vez.
- `[1:02]` Sem gerência de memória, tudo é global e qualquer código toca qualquer endereço.
- `[2:16]` O problema clássico da reentrância.
- `[2:49]` Programação estruturada: blocos, hierarquia, pilha de chamada.
- `[5:38]` Tipagem estática: verificação em troca de engessamento.
- `[7:47]` “E se eu conseguisse colocar o código associado com dado?”
- `[9:11]` Simula implementa a OO pela primeira vez, “esteticamente duvidosa”.

> “um problema clássico gerado por esse estilo de programação é o problema da reentrância onde eu não consigo chamar a mesma rotina duas vezes em segurança concorrentemente” 2:16

> “todas as funções todos os endereços de memória onde as funções começam e terminam eles são definidos em tempo de compilação isso é como se seu código fosse costurado fisicamente na hora que você compila ele” 6:02

**Por que esta aula importa para o resto do curso.** A reentrância e a pilha de chamada são exatamente o que explica, mais tarde, por que os objetos podem ter estado interno: o estado deixa de ser global e passa a viver numa região de memória com dono. E a frase “código costurado fisicamente na hora que você compila” é a definição operacional do acoplamento estático que a indireção (aula #09) vai desfazer.

Aula 04

### A descoberta da essência da Orientação à Objetos

1.354 s · video_id `0mAnNpjBbIw` · 158 views · 16 likes · [assistir](https://www.youtube.com/watch?v=0mAnNpjBbIw)

A aula mais longa da parte teórica reconstrói o caminho intelectual de Alan Kay. A tese é que a OO emerge de uma mudança de ponto de vista sobre o mesmo problema — software fácil de mudar, fácil de crescer, muito valor com pouco código — e que Kay não teve *insight*, teve ***outsight***: foi alimentado de fora por referências que deram sentido ao que ele via. As referências: álgebra, morfogênese, Burroughs B220/B5000, o Sketchpad de Ivan Sutherland, o artigo de Gordon Moore, o Logo de Seymour Papert, o NLS de Douglas Engelbart. Em todas, o mesmo princípio: **indireção**.

- `[0:41]` Ponto de vista distinto sobre o mesmo problema: mudar, crescer, gerar valor.
- `[2:21]` *Outsight* em oposição a *insight*.
- `[5:35]` Utah, financiamento militar, dados migrando entre sistemas.
- `[9:32]` Bob Barton: design recursivo é fazer as partes terem o poder do todo.
- `[11:15]` “Múltiplos pequenos computadores com o mesmo poder de um computador normal”.
- `[15:08]` Kay conserta um “ALGOL” e descobre que era um Simula.
- `[20:42]` Smalltalk como organismo vivo, alterável em tempo de execução.

> “que o princípio básico de um design recursivo é fazer com que as partes têm o mesmo poder do todo” 9:32 — atribuída a Bob Barton.

> “que implementou o conceito do software como organismo vivo onde você tem o próprio sistema operacional com seus objetos que permite você enquanto está explorando e usando o sistema alterar o seu próprio comportamento mudando o código durante o tempo de execução” 20:42

**Recursos externos citados nesta aula** (os únicos links de conteúdo da série que não são do próprio canal): [The Early History of Smalltalk](http://worrydream.com/EarlyHistoryOfSmalltalk/), [Ivan Sutherland e o Sketchpad](https://www.youtube.com/watch?v=6orsmFndx_o), [Douglas Engelbart, “a mãe de todas as demos”](https://www.youtube.com/watch?v=B6rKUf9DWRI) e [Squeak](https://squeak.org/) para experimentar Smalltalk.

O teste de compreensão que ele propõe no fim da aula é o que dá liga a todo o bloco prático: quantos dos sistemas orientados a objetos que você programou permitem alterar o próprio comportamento em tempo de execução? A resposta, para quase todo mundo, é nenhum — e é essa distância entre o paradigma ensinado e o praticado que o curso inteiro tenta fechar.

## 7. Parte II — A mecânica do paradigma (aulas #05–#10)

Seis aulas, 114 minutos. Aqui o curso sai da história e entra no funcionamento interno: complexidade, mensagens, *bound methods*, hierarquias, indireção, e a fronteira entre procedural e OO. Este bloco contém o único código dos inteiros — um exercício que vai e volta três vezes entre as aulas #07, #08 e #10 — e é onde a audiência começa a cair.

Aula 05

### Solucionando a Complexidade

802 s · video_id `_DdACEdhYY8` · 137 views · 15 likes · [assistir](https://www.youtube.com/watch?v=_DdACEdhYY8)

A OO existe para resolver o problema da complexidade — cenários em que o todo é maior que a soma das partes. O software está sempre nesse cenário, e três fatores agravam: o fator humano, a maleabilidade total do software e a variabilidade. O desafio é conter a entropia, porque quanto mais as partes se relacionam, mais o sistema caminha para o caos. A infraestrutura que contém isso é a indireção, guiada pelo princípio da modularização. E a conclusão mais forte da aula inverte o senso comum: **a grande sacada não foram os objetos, foi o sistema de troca de mensagens** — motivo pelo qual os exemplos escolares (animais, automóveis) são ruins.

- `[0:20]` Objetivo: resolver a complexidade; o todo maior que a soma das partes.
- `[1:16]` Variabilidade: não existem dois softwares iguais.
- `[4:56]` Estruturas amarradas a tipo; surgem os tipos de dados abstratos.
- `[7:31]` Não há mais chamada de função: há troca de mensagens.
- `[9:19]` Por que os exemplos de OO são ruins: ênfase em álgebra.
- `[12:45]` O objeto figura não sabe quem desenha: sabe seu tipo, e há um mecanismo que acha o código.

> “Por que os exemplos de orientação a objetos são tão ruins? E a resposta é direta. O grande problema é que todos esses exemplos de animais, né, de automóveis e tudo mais que a gente vê na na faculdade ou vê numa introdução à orientação a objetos, são São com alta ênfase em álgebra.” 9:19

> “Então a figura em si, o objeto figura, ele não sabe quem é o código desenha. O que ele sabe é qual é o tipo dele. Então quando ele recebe uma mensagem desenha, existe todo um mecanismo que vai encontrar qual é o código associado àquele tipo para ser executado no contexto da figura em questão.” 12:48

**A inversão que a aula propõe.** No exemplo do desenho, o objeto não carrega o algoritmo: carrega o *tipo*. O código é localizado pelo tipo em tempo de execução. É a definição de despacho dinâmico apresentada sem o nome técnico — que só aparece na aula #09. E é por isso que “uma única chamada substitui todos os `if`”: o condicional sobre o tipo desaparece porque o mecanismo de descoberta assume o seu lugar.

Aula 06

### Métodos não são Funções

1.411 s · video_id `fTq0OeHtYjA` · 207 views · 19 likes · [assistir](https://www.youtube.com/watch?v=fTq0OeHtYjA)

Primeira aula com código: o exemplo das geometrias (retângulo e ponto), reproduzido para investigar o que acontece por baixo. O método é escrever o teste antes e ignorar as marcas de erro do editor. Ao implementar, aparece uma **violação de interface**: o retângulo acessa os detalhes internos do ponto (`top_left.x`, `bottom_right.y`) e calcula o centro por conta própria — funciona, mas está altamente acoplado. A correção é delegar ao ponto, implementando `__add__` e `__truediv__`. No terminal, ele demonstra que `r.center` não é chamada de função, mas **envio de mensagem**: o nome é resolvido por `getattr`, sobe a hierarquia e produz um *bound method* que carrega a instância (`__self__`) e a função (`__func__`).

- `[3:26]` Os testes falham porque `Rect` não existe; o ponto vem antes — relação de composição.
- `[8:08]` `center` calculado com os atributos internos do ponto: os testes passam.
- `[9:30]` O diagnóstico: “invadindo a privacidade” do ponto, código altamente acoplado.
- `[12:06]` Refatoração: `__add__` recebe ponto, `__truediv__` recebe número — renomeado para *escalar*.
- `[17:59]` Inspeção: `r.center` é um *bound method* de `Rect.center` naquele retângulo.
- `[22:23]` Passagem de mensagem com descoberta do código em tempo de execução (ao contrário de Java).

> “ele tá invadindo a privacidade do Top Life sendo completamente deselegante pegando o x dentro do top left pegando o x dentro top White fazendo uma conta e a partir daí pegando esse resultado e jogando aqui para esse novo ponto que ele tá criando o código funciona mas está altamente acoplado” 9:30 — “Top Life” é `top_left`.

> “o que eu preciso que você entenda que você compreenda é que chamada de método não é apenas uma chamada de uma função como que a gente dá para essa infraestrutura para essa capacidade chance polimorfismo e esse Super Poder da orientação objetos” 22:48.

**O que o terminal prova.** A distinção entre `Rect.center` (função, com ID e endereço próprios) e `r.center` (*bound method*, que carrega `__self__` e `__func__` e é executado por `__call__`) é a materialização do “sistema de mensagens” da aula #05. O código da aula está em [gist.github.com/henriquebastos](https://gist.github.com/henriquebastos/5bb246853b9d7cc26317fb9ab35e4a28).

Aula 07

### O Poder Polimórfico das Hierarquias de Classes

2.361 s · video_id `TIpFGBqzvCw` · 160 views · 17 likes · [assistir](https://www.youtube.com/watch?v=TIpFGBqzvCw)

A aula mais longa da série teórica e a mais importante sobre herança. O experimento mental: um computador ao qual se retirou a aritmética, restando operações sobre bits. Herança e polimorfismo existem para **reconstruir conceitos de alto nível** sobre uma infraestrutura de mensagens — não são um fim. Ele reconstrói `Int8`, `Int16`, `Int24` e `Int32` escrevendo os testes antes, constata o acoplamento em cadeia e o resolve em três etapas: extrair a repetição para `select`, transformá-lo em `classmethod` (`Factory`), e inverter a dependência com um registro. A tese final é a mais importante do curso sobre design.

- `[1:50]` A abordagem do C e o problema do *overflow*.
- `[6:17]` `Byte`, `Word`, `TriByte`, `DoubleWord` e os chips `FullAdder` e `Multiplier`.
- `[10:56]` `Int8` com `__add__`, `__eq__`, `__mul__`; repete para 16, 24 e 32 bits.
- `[22:07]` Diagnóstico: cada classe depende da outra, numa cadeia só de expansão.
- `[27:38]` Classe abstrata `Integer` com `ABC`; `select` vira `classmethod`.
- `[32:27]` Dependência circular invertida com `Integer.register(upper_bound, class)`.
- `[38:42]` Tarefa de casa: implementar subtração e divisão.

> “as implementação claramente tem um problema muito sério um problema de acoplamento veja que agora cada classe está dependendo uma da outra diretamente” 22:07.

> “Originalmente a orientação objetos Era exatamente assim os esquemas de classe não era feito para herança mas sim mas sim para criar camada de em direção para passagem de mensagens” 25:55 — “em direção” é “indireção”.

> “simplifica baixa a bola implementa alguma coisa e faz com que o código te mostre o caminho um bom design vem de você eliminar o excesso” 38:28.

**A regra de design que sai daqui** — e que reaparece na modelagem do Banco Imobiliário: *“Não começa do básico começa replicando o código e deixa o código pedir para você uma generalização”* (26:51). A generalização não se projeta; ela emerge da análise e da síntese. Código em [gist.github.com/henriquebastos](https://gist.github.com/b2bacae88c3a7d2b58229fa5dd6ed4b3); apoio citado: [circuito aritmético](https://pt.wikipedia.org/wiki/Circuito_aritm%C3%A9tico). **Atenção ao escopo desse gist:** ele publica apenas a camada de bits, não a hierarquia — que foi reconstruída e verificada na **seção 24**, junto com o `select`, o `Factory` e o `register`.

Aula 08

### Evitando a Programação Procedural com Objetos

659 s · video_id `Ihvy0sLZZrg` · 89 views · 10 likes · [assistir](https://www.youtube.com/watch?v=Ihvy0sLZZrg)

A aula é a autópsia de um erro cometido na aula anterior. O `Factory` que processa um dicionário de intervalos é um **vazamento de responsabilidade**: a semântica não está nem no dicionário nem no `Integer`. A correção é o `IntervalMap`, uma extensão de `dict` que encapsula a lógica de intervalos. No caminho, a descoberta mais didática: o código funcionava **por acaso**, porque dependia da ordem de inserção do `dict` do Python — o que só se percebe ao testar. A lição: muito `list` e `dict` com laços de processamento é sinal de que falta um objeto que expresse melhor o comportamento desejado.

- `[0:00]` Premissa: todos escorregam para procedural com classe.
- `[0:33]` Diagnóstico do vazamento de responsabilidade no laço do `Factory`.
- `[0:59]` As estruturas nativas são ADTs — crítica ao uso, não à estrutura.
- `[1:49]` A sacada dos ADTs é atribuída a Barbara Liskov, ganhadora do prêmio Turing.
- `[4:25]` `class IntervalMap(dict)` sobrescrevendo `get` e `__setitem__`.
- `[6:50]` Alerta: o código funciona por acaso, por causa da ordem de inserção.
- `[9:43]` Estrutura interna mudou por completo; comportamento, não.

> “não tem jeito independente do quanto você programa orientado objetos eventualmente você vai dar uma escorregada e vai cair na programação procedural com classe” 0:00.

> “a gente mexeu em toda a estrutura interna da classe mudamos completamente como ela está implementada mas não alteramos o seu comportamento” 9:50 — a definição prática de encapsulamento.

**Como detectar o sintoma no seu código.** O sinal de alerta não é usar `dict`: é o *laço de processamento sobre a estrutura* dentro de outra classe. Quando a lógica de manipulação mora fora da estrutura de dados, as dependências passam a existir fora do código e da sintaxe — estão na semântica, como a aula #10 vai formalizar. Código: [gist.github.com/henriquebastos](https://gist.github.com/henriquebastos/cb033cab3f0710ec73b6f12cfad7c5c8).

Aula 09

### Uma Análise Direta Sobre Indireção

1.348 s · video_id `kvcpWrawXns` · 79 views · 9 likes · [assistir](https://www.youtube.com/watch?v=kvcpWrawXns)

O pilar central ganha uma aula própria. Indireção é apresentada como termo da Ciência da Computação (*indirection*), e a metáfora física é o **barramento** de uma CPU: em vez de amarrar cada chip a todos os outros — explosão exponencial de ligações — cria-se uma via comum com uma unidade de controle que chaveia quem fala com quem, quando. O ganho conceitual é passar de **amarração estática** para **amarração dinâmica em tempo de execução**. Ele então revisita o código dos inteiros para mostrar as duas indireções ali presentes: o `Factory` como barramento de instanciação e o polimorfismo (*dynamic dispatch*). O fecho é um alerta de maturidade.

- `[0:27]` “Indireção” não está no dicionário; é *indirection*, termo da Computação.
- `[1:53]` Em linguagem compilada, a chamada amarra o endereço; a alternativa é o ponteiro de função.
- `[3:24]` O esquemático da CPU: clock, RAM, *program counter*, ULA, unidade de controle.
- `[4:53]` A solução de via única: o barramento.
- `[8:43]` Padrões de projeto como estratégias de indireção — sem sair correndo atrás deles.
- `[12:09]` As duas indireções do código dos inteiros.
- `[15:19]` *Dynamic dispatch*: o despachante dinâmico.

> “é como se tivesse em vez de ter uma uma amarração estática sobre o que tá acontecendo a gente faz uma amarração dinâmica em tempo de execução” 6:29.

> “essa dinâmica do polimorfismo ela ela é uma estratégia em direção né a gente chama de da emenda que desperte é o despachante dinâmico” 15:17 — “da emenda que desperte” é *dynamic dispatch*.

**O alerta que fecha a aula** é o mais útil: o objetivo não é deixar o código “absolutamente indireto”, porque indireção em excesso destrói a legibilidade. O alvo é conter a complexidade, não exibi-la. Fonte externa indicada na descrição: [Ben Eater — o barramento da CPU de 8 bits](https://eater.net/8bit/bus).

Aula 10

### Quando Procedural Vira Orientado à Objetos?

874 s · video_id `pbwBkJ1BBZ8` · 59 views · 6 likes · [assistir](https://www.youtube.com/watch?v=pbwBkJ1BBZ8)

A pergunta é se apenas *mover* um procedimento de um lugar para outro o transforma em OO. A resposta é não — o que importa é o **efeito** do movimento. Ele compara as duas versões do código dos inteiros e mostra que a *sintaxe é idêntica*: o `Factory` manda uma mensagem ao `types` ou ao `IntervalMap`, e o `register` manda outra. A diferença é que na primeira versão a lógica de manipulação está fora da estrutura, dependente de ser um dicionário e da ordem de inserção; na segunda, ela vaza para dentro do objeto, que passa a ser um ***proxy*** do mundo exterior.

- `[0:06]` Procedural foca etapas: entrada, processamento, saída.
- `[1:26]` Os dois lados lado a lado: `dict` puro versus `IntervalMap`.
- `[3:45]` OO é *imperativa*; contraste com lógica e com declarativa.
- `[5:00]` A sutileza: enviar mensagem sem saber como o outro interpreta.
- `[7:26]` A diferença não é usar `dict`: é *como você se relaciona* com a estrutura.
- `[11:40]` O `Factory` vira *proxy* para o mundo exterior.
- `[14:03]` Fecho: “programação imperativa porém cooperativa”.

> “a sutileza se dá exatamente no fato de que eu envio uma mensagem sem saber como outra parte vai interpretar ela de fato Ou seja a forma como objeto que recebe mensagem vai administrar a receber essa mensagem tomar decisão Em cima disso não parte do emissor parte do receptor” 5:09 — a definição operacional de troca de mensagens.

> “o problema não está no uso do digite no uso da lista no uso dos tipos de dados é padrão da sua linguagem não é esse o problema o problema é como você usa essa estrutura de dados” 7:45.

**A distinção que a aula consagra.** Encapsulamento *não é premissa, é consequência* (6:13). O critério de OO não é ter classes nem usar `dict`: é se a lógica que manipula o estado vive fora dele ou dentro dele. Documento de apoio: [Google Docs da aula](https://docs.google.com/document/d/1kyz61BdfBL6OBGvegenPu8jcU9XmTOY25pyK8wMh2LQ/edit).

## 8. Parte III — Modelagem: técnica e mentalidade (aulas #11–#13)

Três aulas curtas (24 minutos no total) que preparam o estudo de caso. São a ponte entre a mecânica do paradigma e o Banco Imobiliário.

Aula 11

### O que é Modelagem?

629 s · video_id `1JUmoLSLFuI` · 200 views · 9 likes · [assistir](https://www.youtube.com/watch?v=1JUmoLSLFuI)

Modelagem é um ato naturalmente humano — toda criança aprende modelando, imitando, copiando — e todo modelo é limitado: é o *fazer* que revela as falhas. O maior inimigo é a **síndrome do arquiteto astronauta**, que desenha soluções imaginárias em UML rebuscado. O erro estrutural de uma geração foi **separar modelagem de programação** — sendo que programar é um ato de modelagem. A diferença entre modelar procedural e OO é o olhar: no procedural pensa-se globalmente (a cabeça já vai para o `for`); na OO pensa-se **localmente**, nas partes e nas suas restrições. E as cinco ferramentas de modelagem não são aplicativos de desenho.

- `[0:31]` As restrições delimitam o possível.
- `[2:24]` A síndrome do arquiteto astronauta: caixinhas, setinhas, sensação de ordem.
- `[3:32]` Para fluxo seriam necessários diagrama de sequência e de estado.
- `[3:58]` O erro: separar modelagem de informação — programar já é modelar.
- `[6:07]` No procedural, a preocupação é o todo e o primeiro reflexo é o `for`.
- `[7:33]` Ferramentas: **fala, escrita, visão, tato e código**.

> “modelagem de software não é sobre desenhar o software mas sobre você dominar e compreender profundamente as relações daquilo que será o seu software” 5:40 — a definição central do curso.

> “você não pensa no todo você pensa nas partes confiando que no tempo o todo vai ser muito maior do que a soma das partes” 7:10.

**A lista das cinco ferramentas** — fala, escrita, visão, tato, código — merece ser lida literalmente: são os sentidos e as linguagens do corpo. A técnica, diz ele, *molda o comportamento* e evita retrabalho. É a justificativa de por que a decupagem (#16) e os CRC cards (#15) são exercícios de mesa, com papel e conversa, e não de ferramenta CASE.

Aula 12

### Mentalidade POO

416 s · video_id `VFWCMRGCrJE` · 62 views · 4 likes · [assistir](https://www.youtube.com/watch?v=VFWCMRGCrJE)

O contraste dos dois modelos mentais, de forma quase esquemática. O procedural é imperativo, exerce controle, exige visão **global** e pensamento **sequencial** (causa e consequência — “grava na memória, aí grava o disco”). A OO é o inverso: exige pensamento **local** (a célula no microscópio, que sozinha não faz nada) e o *time frame* é **eventual** — não se sabe quando algo acontece, só interessa o que acontece quando aquilo acontece. A sequência de execução *emerge* da interação; desenhar pela sequência produz “código procedural com classe”.

- `[0:51]` Design procedural é visão global: o que cada coisa faz, como conversam, onde ficam.
- `[1:33]` Na OO, pensar global impõe pressuposto e *deforma* a modelagem.
- `[2:29]` *Time frame*: sequencial no procedural, eventual na OO.
- `[3:13]` “A sequência da execução emerge da interação entre os objetos”.
- `[4:28]` A resposta ao enigma: a tia Cotinha, professora de alfabetização.

> “a sequência da execução ela emerge da interação entre os objetos então se você não faltar o design pela interação dos objetos você está subvertendo o que seria orientador objetos a algo procedural E aí que você vê um monte de código procedural com classe” 3:17.

> “o entendimento da estrutura gramatical do português é a maior ferramenta que você vai ter para programar na tela do objeto isso é surreal surreal por quê Porque você só consegue expressar aquilo que você entende” 5:50 — “na tela do objeto” é “na orientação a objetos”.

**O desfecho inesperado.** A aula termina com uma homenagem à tia Cotinha, professora que ensinou o alfabeto e deu de presente um dicionário e uma gramática, e com a tese de que sujeito, predicado, objeto e adjuntos são o andaime do design: *“conseguindo pensar em extrair história de usuários bem concisa que vão refletir literalmente nos nomes das suas classes nos nomes dos seus métodos”* (6:30). Nomes de classe e de método são sintaxe da frase, e a frase revela quem faz o quê a quem — a base da modelagem CRC da aula #15.

Aula 13

### Técnicas de Modelagem

427 s · video_id `ApMUQxhSrQ4` · 60 views · 5 likes · [assistir](https://www.youtube.com/watch?v=ApMUQxhSrQ4)

A aula encerra o bloco demoliendo a ideia de que notação formal resolve o problema. O UML, apesar de apoiar uma boa conversa, não é linguagem de computação — **não tem condicional**, só modela relações e estados — e por isso desatualiza rápido e vira papel A3 jogado fora. A direção correta é invertida: não se parte do diagrama para o código, parte-se da necessidade de entender o código para depois refletir isso em diagrama. O BDD leva a mesma crítica de custo: exige infraestrutura para transformar texto em testes, e sua estrutura nasceu em inglês. O objetivo de qualquer técnica é **transferência de conhecimento** — e a última apresentada, os **CRC cards** (1989), não é técnica: é ferramenta lúdica para aprender a pensar dentro do objeto.

- `[0:03]` A lista de “técnicas de design”: UML, DDD, BDD, CRC.
- `[0:14]` UML não tem sequer condicional.
- `[0:45]` Conectar símbolos (agregação? pertencimento?) é “perda de energia absurda”.
- `[1:00]` A direção é do código para o diagrama, nunca o contrário.
- `[2:29]` BDD: o custo de infraestrutura não contabilizado.
- `[6:10]` CRC: cenário → 3 a 5 classes → responsabilidades → colaboradores.
- `[7:44]` O tabuleiro de cartas é disposto por proximidade de colaboração e sugere módulos.

> “o ML apesar de você poder usar ele com o diagrama Zinho para poder explicar e orientar uma boa conversa se propõe a ser uma linguagem mas não tem nem condicional” 0:14 — “o ML” é UML.

> “no final é qual é o objetivo é transferência de conhecimento como é que conhecimento estudando junto discutindo debatendo modelando” 3:57.

**O procedimento CRC que o curso vai executar.** Nas próximas três aulas, o método anunciado aqui é seguido à risca: escolher um cenário, listar de 3 a 5 classes, escrever as responsabilidades de cada uma (“o que sabe ou faz”) e os colaboradores, e então *dispor fisicamente os cartões* — a proximidade entre eles revela os módulos. O documento de referência está em [Google Docs da aula](https://docs.google.com/document/d/1WIuVUyK8Nm49PE9AfvgcJyDBlw4rbSRkdkoC6OFD7co/edit).

## 9. Parte IV — O Banco Imobiliário: do enunciado ao CRC (aulas #14–#17)

Quatro aulas, 121 minutos, dedicadas a modelar — e nenhuma linha de código. O estudo de caso é um desafio de Banco Imobiliário que chegou ao instrutor vindo de um aluno, extraído de um processo de entrevista. O arco é rigoroso: ler o enunciado (#14), construir os cartões CRC (#15), decupar o texto (#16), reorganizar por temas e revisar a modelagem (#17).

Aula 14

### O Banco Imobiliário

1.930 s · video_id `sAt7foLKbqE` · 104 views · 9 likes · [assistir](https://www.youtube.com/watch?v=sAt7foLKbqE)

Leitura coletiva do enunciado, com o objetivo explícito de **compreender**, não de resolver. O ritual é a “primeira passada”: ler em voz alta enquanto a turma separa substantivos, verbos e “outras coisas”, expondo ambiguidades. O enunciado — como o pedido de um cliente — descreve o problema, não define a implementação, e foi escrito de propósito com ordem quase sequencial e alternâncias que fazem perder o contexto. Toda antecipação de decisão de código durante a modelagem é **design precoce**. A moral: o exercício testa se o candidato sabe *organizar ideias*.

- `[1:16]` A primeira passada: coluna de substantivos, coluna de verbos, coluna de “outras coisas”.
- `[2:22]` O enunciado: 300 de saldo, ordem sorteada, 20 propriedades, custo, aluguel, proprietário.
- `[4:17]` Os quatro comportamentos: impulsivo, exigente (aluguel > 50), cauteloso (reserva de 80), aleatório (50%).
- `[5:17]` O autor embaralha de propósito: ordem quase sequencial com alternâncias.
- `[13:53]` A advertência clássica: modelar o software como o mundo real não funciona.

> “a ordem em que ele vai descrevendo as coisas ela é quase sequencial com algumas alternância que faz com que a pessoa perca o contexto então ele cria confusões de propósito” 5:29.

> “se você tentar modelar o software como o mundo real não vai funcionar entendeu porque você vai complicar as coisas” 13:53 — a tese que separa modelagem de mimetismo.

**O que a aula deixa aberto de propósito.** A questão central do domínio fica sem resposta nesta aula, e é a mais importante do projeto: *“um jogador ativamente vai lá e compra ou a propriedade vai lá e se oferece pro jogador ou alguma outra coisa intermedia essa relação”* (14:28). É exatamente essa indeterminação que a modelagem CRC da aula #15 vai resolver.

Aula 15

### Banco Imobiliário: Modelagem CRC

2.520 s · video_id `97u7gzfcAd0` · 123 views · 5 likes · [assistir](https://www.youtube.com/watch?v=97u7gzfcAd0)

Construção ao vivo do CRC sobre um tabuleiro de cartões, com a turma guiando as classes. A regra imposta de saída é dura: em OO **não se olha globalmente, olha-se localmente e contextualmente** — começar pela classe `Jogo` produziria um “proceduralzão”, porque a construção iria de fora para dentro. Daí os dois problemas crônicos: interpretar uma classe como **ator** (o jogador “joga o dado”, o tabuleiro “move o jogador”) e especular sem ter escolhido o caso de uso. A partilha final é por **localidade**: o tabuleiro é só localidade; a propriedade sabe preço, aluguel e proprietário e por isso *medeia* a relação; o jogador é uma conta bancária; a rodada é um Controller; o dado é um gerador de números.

- `[0:06]` Cartão CRC = nome da classe + responsabilidades + colaboradores.
- `[0:46]` Pressupor `Jogo` faria tudo cair dentro dela: “você começou de fora para dentro”.
- `[1:36]` Limite de cinco classes para o exercício.
- `[4:37]` Problema crônico 1: interpretar classe como ator — “você está se imaginando jogando o jogo”.
- `[6:24]` Quem é íntimo do jogador é só a propriedade; o que ele tem de fato é *saldo*.
- `[8:34]` Responsabilidade única como redutora de acoplamento.

> “tu vai fazer um [ __ ] proceduralzão porque você começou de fora para dentro ao invés de dentro para fora” 0:46.

> “exato você não pode se imaginar jogando o jogo porque você não está modelando o mundo real é um evento” 5:42.

**O resultado desta aula — o CRC completo.**

| Classe | Responsabilidades | Destino no código |
|---|---|---|
| `Jogador` | Saldo, pagar, receber, decidir investimento via estratégia, saber se está no jogo. Não sabe posição nem suas propriedades. | Implementado na #18 como `Player`. |
| `Propriedade` | Valor de compra, de venda, aluguel, proprietário; decide como interagir com o visitante; sabe se pode ser comprada. | Implementado na #19 como `RealState`. |
| `Tabuleiro` | Possui as 20 propriedades, conhece a sequência e a posição dos jogadores, move N casas, detecta a volta, remove o jogador, libera propriedades. | Implementado na #20 como `Board`. |
| `Dado` | Sortear 1 a 6. | Rebaixado a `Game.dice()` — nunca virou classe. |
| `Rodada` | Executa a jogada de cada jogador, conhece a ordem cíclica, pede movimento ao tabuleiro, oferece a propriedade. | Deslocado para `Board.turn()` na #21; a aula decide que **não** merece ser objeto. |
| `Estratégia` | Decide a compra (recebe propriedade, saldo e valores); quatro variações. Renomeada de “comportamento”. | Implementada na #18; recebe `balance`, `price` e `rent`, não a propriedade. |
| `Competidores` | Sabe quem são os jogadores e a ordem, elimina quem zerou, chama o próximo. | **Criada e eliminada nesta mesma aula** — ressurge com outro desenho na #23. |
| `Jogo` | — | **Deliberadamente não criada** (“classe Deus”): o jogo deve *emergir*. |
| `Simulador` | — | Apenas mencionado; implementado na #22. |

Duas observações sobre esta tabela. Primeiro: `Competidores` e `Dado` são as duas classes que a modelagem criou e o código não manteve naquele formato — e nas duas o motivo é o mesmo, excesso de cerimônia para o comportamento que precisavam expressar. Segundo: a classe que mais aparece no CRC é `Jogo`, e é justamente a única que se decide *não* criar.

Aula 16

### Banco Imobiliário: A Decupagem

1.685 s · video_id `_LfwW4u6zoU` · 80 views · 4 likes · [assistir](https://www.youtube.com/watch?v=_LfwW4u6zoU)

Nasce o conceito-título: **decupagem** — pegar o texto do cliente parágrafo por parágrafo e reescrevê-lo em frases curtas e sem ambiguidade. Não é tradução para código: é etapa *posterior ao enunciado e anterior à modelagem*, e serve para explicitar o que estava implícito, oculto ou espalhado, criando um **glossário de domínio**. Nesse exercício ele encontra um erro no vocabulário do próprio cliente (a definição de “rodada”) e descobre que a ordem dos termos — quem paga o quê a quem, em que momento — determina a localidade do código.

- `[0:02]` O enunciado equivale ao cliente contando um problema: “você acolhe, mas não trata isso como verdade”.
- `[0:57]` O exercício: refrasear em frases específicas, diretas, claras e curtas.
- `[1:32]` O erro encontrado: “os jogadores se alternam em rodadas”.
- `[1:48]` Rodada é o conjunto de turnos; um turno é uma partida. Por isso o curso adota *turno*.
- `[3:33]` Em vermelho, o que ele explicita e não estava no texto.
- `[13:04]` A pergunta que o texto não responde: de onde vem o dinheiro pago?

> “eu chamo de a decoupagem é quando eu pego o texto parágrafo parágrafo e eu vou refraseando em frases específicas diretas sem anuidade” 1:02 — “sem anuidade” é “sem ambiguidade”.

> “o que que foi feito do dinheiro que ele pagou cria de dinheiro dinheiro desaparece o o proprietário recebe parte né isso não tá definido” 13:04 — o vazio que a decupagem expõe.

**As decisões “arbitrárias” que a decupagem obriga a tomar.** Como o texto não define, ele decide e *marca que decidiu*: o proprietário recebe o valor integral (ou seja, o dinheiro é criado); o saldo negativo só pode acontecer no aluguel; o aluguel é 50% do valor de compra; o jogador paga antes de ser eliminado. E consolida a restrição que estrutura o código: **o aluguel é a única transferência entre jogadores**. Duas decisões desta aula serão revistas mais tarde — o destino do dinheiro (#18) e a natureza da rodada (#21).

Aula 17

### Banco Imobiliário: Revisando a Modelagem

1.108 s · video_id `8DWlhnpLI6Y` · 122 views · 3 likes · [assistir](https://www.youtube.com/watch?v=8DWlhnpLI6Y)

Depois da decupagem, ele **reorganiza a lista por temas** — jogo, jogador, simulador, propriedade, turno, tabuleiro — e só então reflete isso no CRC, deixando claro que não é mapeamento de classes nem ferramenta de modelo. A reflexão central é que a modelagem deve **evitar ciclos** (o ideal é uma descrição em árvore) e que cada entidade deve ter **uma e apenas uma responsabilidade**. Por isso o jogador fica como conta bancária e a propriedade passa a ser o nó que *media* a relação entre jogadores — ela conhece o próprio estado e por isso se oferece para venda ou cobra aluguel.

- `[0:08]` Reorganização por temas; “não é o mapeamento de classe”.
- `[2:36]` O exercício é uma análise de complexidade ciclomática do modelo.
- `[2:51]` “Um modelo que evita ciclos”; a forma-alvo é a árvore.
- `[3:25]` “A responsabilidade do jogador é lidar com dinheiro”.
- `[5:15]` A modelagem não precisa refletir o mundo real.

> “o ideal é que a gente tem um modelo que evita ciclos o modelo geralmente ele tem uma descrição de árvore” 2:51.

> “a modelagem do código orientador do objetos ela não precisa refletir o mundo real você não está fazendo uma simulação de Matrix modelando átomos” 5:15.

**O CRC revisado — e o que muda em relação à #15.** Três decisões se firmam aqui e sobrevivem até o código final: a **inversão de dependência** (o jogo *recebe* os jogadores prontos, não os gera — o que na #22 se materializa em `game_factory()`); a **propriedade como mediadora** (analogia do cartório: ela conhece o próprio estado e por isso se oferece ou cobra); e o hábito de **deixar a classe mais abstrata por último**. A geração e o controle ficam separados — é o papel do `Factory` que a #21 vai criar dentro do próprio `Player`.

## 10. Parte V — A implementação (aulas #18–#23)

Seis aulas, 172 minutos — mais da metade do tempo total do curso. É a parte em que tudo o que foi modelado encontra o compilador, e onde aparecem as divergências mais interessantes: três decisões tomadas com papel e caneta são revertidas quando o código é escrito.

Aula 18

### players.py

2.380 s · video_id `VOJG-rajSmA` · 93 views · 8 likes · [assistir](https://www.youtube.com/watch?v=VOJG-rajSmA)

Implementação guiada por testes, começando pelas folhas do sistema. O ciclo é curto: escrever o teste, ver falhar, implementar o mínimo, passar. Duas decisões marcam a aula. Primeira: trocar booleanos e `if` por **exceções específicas do domínio** — `OutOfMoney` quando o pagamento quebra o jogador, distinta da exceção de saldo insuficiente para investir. Segunda: escolher deliberadamente a regra mais simples, mesmo contrariando a especificação da #16. No fim, ele discute composição *versus* herança para as estratégias — e valida a resposta de um aluno que usou herança.

- `[0:14]` Começar “comendo pelas beiradas, indo pelas folhas do sistema”.
- `[1:01]` “Não é fazer um showcase de Python.”
- `[1:14]` O coração: jogador, propriedade, estratégia.
- `[4:09]` O primeiro teste: `assert balance == 300`.
- `[11:39]` A regra mais simples: “ninguém recebe nada e o cara sai do jogo”.
- `[17:23]` Discussão de composição *versus* herança para as estratégias.

> “não é fazer um show case de Python seleção aqui é resolver um problema orientado objeto eu vou usar Python por acaso” 1:06.

> “não é mais fácil quando o cara não tem dinheiro para pagar ninguém recebe nada e o cara sai do jogo simplesmente isso entendeu ninguém recebe nada o cara sai do jogo” 11:39 — a regra que revoga a decisão da #16.

**A divergência que esta aula cria.** A #16 tinha decidido que o proprietário recebe o valor integral, criando dinheiro. A #18 decide o oposto: quem não pode pagar não paga ninguém — sai do jogo. Não é um bug de implementação, é uma *revisão de regra de negócio* feita no momento em que ela virou código, e justificada por simplicidade. Esta é a primeira das três reversões documentadas na seção 11.

Aula 19

### realstate.py

1.150 s · video_id `zLLijrckZhM` · 36 views · 3 likes · [assistir](https://www.youtube.com/watch?v=zLLijrckZhM)

A propriedade, terceiro elemento do miolo do jogo. Ele monta o “feijão com arroz” — preço, aluguel e dono com `None` como padrão — e discute ao vivo a **inversão de dependência**. A descoberta da aula é que a decisão entre **vender** e **alugar** pertence à própria propriedade: concentrar essa lógica no `RealState` faz dele o mediador da relação proprietário/inquilino, deixando o `Player` com pouquíssimas APIs conhecidas. Duas correções vêm dos alunos: o nome semântico do dono e a exceção movida para o ponto mais localizado.

- `[2:14]` Inversão de dependência: o valor-padrão sai do módulo para o parâmetro.
- `[5:10]` Reordenação dos testes: do simples ao complexo.
- `[6:47]` Aluno questiona a semântica do dono — o nome é trocado.
- `[9:53]` A guarda: se a propriedade já tem dono, a venda deve abortar.
- `[11:22]` Por que concentrar venda *e* aluguel na propriedade.
- `[17:04]` Uma falha real descoberta no console.

> “esse fato do teu Self Control aqui é o que justifica todo esse lance de concentrar lógica da venda e do aluguel dentro do próprio do próprio cara” 11:22.

> “o único conhecimento que que o Will Street faz do player são nas suas apis públicas” 17:52 — “Will Street” é `RealState`.

Aula 20

### board.py

876 s · video_id `5io4mj-JloU` · 41 views · 3 likes · [assistir](https://www.youtube.com/watch?v=5io4mj-JloU)

Com os três primeiros elementos prontos, a aula ataca o tabuleiro — a peça que “amarra” o resto. O `Board` recebe jogadores, propriedades e o bônus da volta, e descobre ao vivo que os jogadores **não podem** ficar numa lista: precisam estar num dicionário jogador→posição, porque posição é estado do tabuleiro. Daí nasce a mecânica central: mover N casas, detectar a volta pagando bônus, remover quem faliu. O momento mais didático é a ida ao console para experimentar o **módulo** como resposta à natureza cíclica do tabuleiro.

- `[0:57]` O board recebe jogadores, propriedades e o bônus.
- `[2:42]` O drama de decidir quem são os jogadores.
- `[5:10]` A descoberta: lista não serve, tem de ser dicionário.
- `[8:37]` Aluno contesta a “gambiarra” do `-1`; ele defende a escolha.
- `[9:06]` A virada conceitual: se algo é cíclico, existe um módulo.
- `[11:00]` `divmod` substitui o cálculo manual da volta.
- `[12:24]` Sugestão de aluno: `Board.__len__`.

> “tem que ser a posição dele é -1 quando começa o jogo Porque como a lista aqui de propriedade O primeiro é zero” 5:02 — a justificativa da posição inicial fora do tabuleiro.

> “então agora sim New Lap New position vai ser div mod desse cara com o lem de self.propriet” 11:00.

**O detalhe de implementação que vale ouro.** Usar o jogador como *chave* de dicionário funciona porque objetos são hashiáveis por identidade no Python — *“então ele tá usando como hashi aí dentro o ID do cara show de bola a identidade Tá funcionando”* (6:32). É um uso do sistema de objetos da linguagem que só faz sentido por causa da aula #06: a identidade é propriedade do objeto, não um número que alguém atribui.

Aula 21

### turn e game.py

2.759 s · video_id `lAvfyLdetHQ` · 25 views · 3 likes · [assistir](https://www.youtube.com/watch?v=lAvfyLdetHQ)

A aula mais longa e mais experimental do curso. Henrique discute se o **turno** merece ser um objeto e conclui que não — não guarda estado, é uma sequência de ações — então ele começa como método e é deslocado para dentro do `Board`. A aula alterna entre “implementar por fora” e “trazer para dentro”, usando testes para decidir cada movimento: o turno coordena o fluxo e as exceções, o `Game` assume vencedor e empate, e nasce o **Factory** de jogadores dentro do próprio `Player`. No meio, um experimento no terminal com `itertools.cycle` revela que remover durante a iteração não funciona — a semente da exclusão lógica da aula #23.

- `[0:09]` O turno precisa ser objeto? “Acho que não” — não tem estado.
- `[3:03]` O teste `board.turn(player, steps=1)`, com o dado de fora.
- `[8:21]` As exceções do turno entram com `try/except ... pass`.
- `[15:36]` A estranheza: `players` existe no game *e* no board.
- `[21:18]` A tese da turma: gerar o jogo não é papel do jogo.
- `[26:04]` `Game.leader` como propriedade.
- `[36:50]` “Quem é o próximo?” testado no console.
- `[37:50]` O `del` durante a iteração quebra — nasce a exclusão lógica.

> “acho que não precisa ter um objeto turno porque ele seria um método estático basicamente ele não tem um estado” 0:09 — a decisão de design mais discutida do curso.

> “algo que não tá cheirando bem Nisso porque o gametv instanciar os Players e sortear a ordem players Não fora o game deveria instanciar tudo bem” 16:07 — o *code smell* que gera o Factory.

> “em outras linguagens isso seria uma outra classe separada que teria essa lógica mas como o pai também o classe método e classes pagam…” 24:17 — “como o Python tem classe-método e classes são objetos”.

**O que esta aula decide.** Três coisas, todas verificáveis no código final. O turno virou `Board.turn()`, não uma classe. O dado virou `Game.dice()`, estático — a classe `Dado` do CRC morreu. E a geração dos jogadores saiu do `Game` para o `Player.from_strategies()`, cumprindo a inversão de dependência que a #17 tinha prescrito.

Aula 22

### simulation.py

727 s · video_id `QSPi6YZJsZo` · 36 views · 3 likes · [assistir](https://www.youtube.com/watch?v=QSPi6YZJsZo)

A aula fecha a implementação construindo o simulador: um `Simulation` que recebe a população, cria um `Game` por simulação via Factory e devolve um relatório com o percentual de vitórias por estratégia. Ele detalha a geração aleatória do tabuleiro com **distribuição normal** (`random.gauss`, média 5, desvio 1), arredondada e escalada para preços e aluguéis, e acelera tudo com **multiprocessing**. O trecho mais rico é o comparativo: trocando o tabuleiro sorteado por um **tabuleiro fixo**, a distribuição muda por completo.

- `[0:43]` O `run` usa o Factory de jogo.
- `[1:28]` Sequência de estratégias embaralhada para os jogadores.
- `[2:01]` `random.gauss` com média 5 e desvio 1.
- `[2:17]` Vinte propriedades, valores flutuando entre 1 e 9.
- `[3:23]` Escala de preço (×20) e de aluguel.
- `[4:24]` Multiprocessing para rodar milhares de jogos.
- `[9:55]` O experimento do tabuleiro fixo: a intuição era certa.

> “aqui o balance Inicial dele é 300 pronto então com isso eu vou ter um game para cada simulação” 4:09.

> “muito bem analisado Será que você vai mudar um pouco o comportamento vamos ver ficou mais balanceado tá vendo caramba bem mais balanceado” 8:34 — depois da correção sugerida por um aluno: devolver as propriedades do eliminado.

> “A modelagem nunca é definitiva mas ela vai nos ajudando a separar responsabilidade para que a gente conseguir evoluir progredir com um…” 11:13 — a conclusão do curso.

**Um bug encontrado por um aluno, na hora.** A primeira execução “ficou mais balanceado” justamente porque a correção trouxe um comportamento que faltava: ao eliminar um jogador, o board deve **liberar as propriedades dele** — ou seja, o `remove` precisa percorrer as propriedades e tirar o dono. É a única correção do curso que muda materialmente o resultado estatístico, e ela vem da turma, não do instrutor. O código final tem exatamente esse laço.

Aula 23

### competitors.py

2.420 s · video_id `gesJl9NsLks` · 35 views · 5 likes · [assistir](https://www.youtube.com/watch?v=gesJl9NsLks)

Um exercício completo de **refatoração guiada por dívida técnica**. Começa com uma lição de método — “deixar o código descansar” — e diagnostica no `Game.run` um sintoma clássico: a mesma informação (os jogadores) vive em dois lugares (`Game` e `Board`), criando ambiguidade de estado e acessos encadeados. A resposta é uma **nova entidade** que encapsule a coleção: descartado o nome `PlayerCollection`, ele inventa o conceito de **competidores**, nascido de um arquivo de teste escrito antes da implementação. A interface é desenhada pelo que o `Board` já exigia — `__getitem__`, `__setitem__`, `__delitem__`, `__len__`, `__iter__` — e sofisticada com **exclusão lógica**.

- `[0:00]` A técnica fundamental: deixar o código descansar.
- `[1:10]` Débito técnico: o que compromete a capacidade futura de alterar.
- `[3:30]` Diagnóstico: os jogadores em dois lugares.
- `[4:58]` Sintoma: encadeamento de pontos indica alto acoplamento.
- `[7:40]` O nome: descartado `PlayerCollection`, criado “competidores”.
- `[8:55]` Estratégia: primeiro o arquivo de teste, para desenhar a interface.
- `[16:41]` Exclusão lógica (“delete virtual”) dos eliminados.
- `[26:24]` A pegadinha do `itertools.cycle`.
- `[31:53]` O líder migra para dentro da coleção.
- `[38:26]` Desafio final: desacoplar a simulação.

> “existe uma técnica fundamental quando você programa em qualquer paradigma sobre objetos não é diferente essa técnica é deixar o código descansar” 0:00.

> “em vez de ter um triângulo entre games jogadores e board né tudo conectado misturado a gente vai eliminar esse triângulo” 6:59 — o diagnóstico geométrico do acoplamento.

> “Deus não funcionou o que tá acontecendo aqui aqui existe uma pegadinha um drama” 26:26 — “Deus” é a legenda automática lendo “de novo”.

> “O líder do game é só um proxy para que você não expõe o complexo na sua lógica lá no simulador” 33:35 — “o complexo” é a classe `Competitors`.

**A aula que não está no repositório.** Esta é a única aula cujo arquivo central — `competitors.py` — não existe no repositório público: o repositório tem um único commit (“Import”) com 7 módulos, e o arquivo que a #23 constrói ao vivo ficou como exercício. A última decisão de design do curso — a coleção com exclusão lógica — existe apenas no vídeo, e a análise da seção 19 cobre o estado do código *anterior* a ela. A seção 21 fecha essa lacuna: reconstrói o módulo a partir do que a aula especifica e o verifica por execução, comparando-o com o repositório original.

## 11. Divergências entre a modelagem e o código

Esta é, provavelmente, a seção mais útil do documento. O curso modela por quatro aulas e implementa por seis — e **três decisões tomadas no papel são revertidas quando viram código**. Nada disso é erro: é a demonstração empírica da tese da aula #22, de que “a modelagem nunca é definitiva”. A tabela abaixo cruza o que foi decidido (#15–#17) com o que existe no código final.

| Decisão | Na modelagem | No código | Justificativa dada |
|---|---|---|---|
| Destino do dinheiro de quem faliu | #16: o proprietário recebe o valor integral — o dinheiro é criado. | #18: revogada. Quem não pode pagar sai do jogo e ninguém recebe. | Escolher a regra mais simples. |
| Nome do conceito de decisão de compra | #15: “comportamento”. | #18: estratégia (`Strategy`). | Semântica: a decisão é delegada a um objeto próprio. |
| O que a estratégia recebe | #15: propriedade, saldo e valores. | #18: apenas `balance`, `price` e `rent`. | Ponto de contato único: a propriedade não é necessária para decidir. |
| Vocabulário do tempo | #15: “rodada”. | #16/#21: turno — rodada é o conjunto de turnos. | Erro encontrado no texto do cliente durante a decupagem. |
| Classe `Competidores` | #15: criada com responsabilidades de ordem e eliminação. | #15: eliminada na mesma aula; renasce na #23 com outro desenho — ausente do repositório, **reconstruída na seção 21**. | Excesso de cerimônia; a ordem migra para a lista que o turno recebe. |
| Classe `Dado` | #15: sabe sortear de 1 a 6. | #21: nunca virou classe — é `Game.dice()`, estático. | Não guarda estado; um objeto seria pura cerimônia. |
| Classe `Rodada` | #15: Controller com o mínimo de código. | #21: não criada — virou `Board.turn(player, steps)`. | “Ele não tem um estado.” |
| Classe `Jogo` | #15: deliberadamente não criada; o jogo deve emergir. | #21: criada como `Game`, mas só coordena — zero regra de negócio. | Era necessária uma raiz que sequenciasse sem decidir. |
| Quem gera os jogadores | #17: o jogo *recebe* os jogadores (inversão de dependência). | #21: mantida — `Player.from_strategies()` gera; o `Game` recebe. | “Gerar o jogo não é papel do jogo.” |
| Parâmetros do simulador | #22: `Simulation` recebe população e passos; entrada em `main.py`. | divergente: recebe `population` e `pool`; a entrada é `__main__.py`. | Não discutida no vídeo — o código publicado tem outra assinatura. |

**Como ler esta tabela.** Note o padrão: *todas* as classes que a modelagem criou e o código abandonou são objetos que não guardam estado — `Dado`, `Rodada` e a primeira `Competidores`. A regra que emerge não está escrita em nenhuma aula, mas é consistente em três casos: **comportamento sem estado mora em método; estado sem comportamento vira método burro; só o que tem estado *e* decisão merece ser classe.** É a versão prática do “métodos não são funções” da aula #06 — invertida: um objeto que não tem estado não precisa existir para carregar comportamento.

As duas divergências que a tabela marca como não justificadas no vídeo (#22) são as que exigem mais cuidado ao usar o repositório como referência: o simulador publicado não é literalmente o que a aula escreve na tela. São pequenas — um parâmetro a menos e um arquivo de entrada com outro nome — mas é exatamente o tipo de detalhe em que uma documentação construída só a partir da transcrição erraria.

## 12. Princípios que atravessam toda a série

Dez regras que o instrutor formula explicitamente e aplica repetidamente ao longo das 23 aulas. Todas vêm de fala transcrita — nenhuma é inferência deste documento.

#### 1. Deixe o código descansar

Antes de refatorar, dê tempo ao entendimento. É a primeira técnica da aula #23 e a razão de o curso ter quatro aulas de modelagem antes de qualquer linha de código.

#### 2. Não projete a generalização — deixe o código pedi-la

*“Não começa do básico começa replicando o código e deixa o código pedir para você uma generalização”* (#07, 26:51). Repetição primeiro, abstração depois, e só quando a repetição doer.

#### 3. Escolha a regra mais simples

Dito na #16, aplicado na #18 (a regra do dinheiro) e na #21 (o dado como `randint`). Simplicidade vence a elegância da especificação original.

#### 4. Postergue decisões enquanto o entendimento cresce

A razão declarada de a decupagem (#16) vir antes do CRC (#17), e de a classe mais abstrata ser deixada por último.

#### 5. Pense localmente, nunca globalmente

*“se você pensar Global você vai impor uma visão um pressuposto em cima do problema e isso vai deformar a sua modelagem”* (#12, 1:38).

#### 6. Uma responsabilidade por identidade

O jogador é uma conta bancária e nada mais. No código: `Player` tem saldo, estratégia e três métodos — e nenhuma referência a posição ou propriedade.

#### 7. Evite ciclos; busque a árvore

O modelo bom é o que não tem ciclos (#17). No código, isso aparece como uma direção de dependência: `Player` não conhece `Board`; `RealState` conhece `Player`; `Board` conhece os dois.

#### 8. Componha em vez de herdar — quando puder

A #18 implementa as estratégias por composição, com o `Player` recebendo um objeto de estratégia. Mas o instrutor valida explicitamente a solução de um aluno que usou herança: o critério é o efeito, não a regra.

#### 9. Prefira exceções específicas a booleanos e `if`

Três exceções de domínio em `player.py` — `OutOfMoney`, `NotEnoughMoney`, `AbortInvestment` — distinguem três desfechos que, com um booleano, seriam indistinguíveis.

#### 10. O código é a interface

*“Encontrar a abstração correta abre campo para ir…”* (#23). E a consequência: um nome ruim no código denuncia uma abstração mal encontrada — é por isso que `PlayerCollection` virou `Competitors`.

## 13. Citações-chave do curso

Doze falas que resumem a série, com aula e marcação de tempo. As citações são transcrições literais da legenda automática: as marcas de oralidade e os erros de reconhecimento de fala foram preservados de propósito, porque alterá-los seria inventar fala.

| Aula | Tempo | Citação |
|---|---|---|
| #01 | 0:09 | “Eu acho que o nosso problema para compreender ainda são objetos é um problema do peixe que não sabe que existe água” |
| #03 | 0:00 | “antes de surgir natação objetos programar era uma atividade revmetal literalmente você tinha que ir direto no metal” |
| #04 | 2:21 | “foi que o alenquei teve o que ele chama de outside em Oposição a Insight porque ele não teve uma epifania interna” |
| #05 | 7:31 | “A grande sacada da orientação objetos não foram os objetos, foi o sistema de mensagem… não existe mais chamada de função. O que existe são trocas de mensagens.” |
| #06 | 9:30 | “ele tá invadindo a privacidade do Top Life… o código funciona mas está altamente acoplado” |
| #07 | 38:28 | “simplifica baixa a bola implementa alguma coisa e faz com que o código te mostre o caminho um bom design vem de você eliminar o excesso” |
| #09 | 0:39 | “a definição mais simples é que é a capacidade de referenciar algo usando um nome referência o continente ao invés do valor em si” |
| #11 | 5:40 | “modelagem de software não é sobre desenhar o software mas sobre você dominar e compreender profundamente as relações daquilo que será o seu software” |
| #12 | 3:17 | “a sequência da execução ela emerge da interação entre os objetos… E aí que você vê um monte de código procedural com classe” |
| #15 | 0:46 | “tu vai fazer um proceduralzão porque você começou de fora para dentro ao invés de dentro para fora” |
| #18 | 1:06 | “não é fazer um show case de Python seleção aqui é resolver um problema orientado objeto eu vou usar Python por acaso” |
| #23 | 0:00 | “existe uma técnica fundamental quando você programa em qualquer paradigma sobre objetos não é diferente essa técnica é deixar o código descansar” |

## 14. A evolução técnica, aula a aula

O que efetivamente *entra* no sistema a cada aula, do zero ao simulador. É o mapa de leitura mais prático do curso: se você quiser reproduzir o projeto, esta é a ordem em que ele cresce.

| Fase | Aulas | O que existe no fim da fase | Decisão estrutural da fase |
|---|---|---|---|
| Teoria | #01–#10 | Nenhum código do projeto. O exemplo das geometrias (#06) e o dos inteiros binários (#07, #08, #10). | Indireção como princípio unificador. |
| Modelagem | #11–#13 | Método definido: CRC, decupagem, cinco ferramentas. | O português é a ferramenta principal. |
| Estudo de caso | #14–#17 | Glossário, restrições, CRC revisado. Zero código. | Evitar ciclos; uma responsabilidade por identidade. |
| Folhas | #18–#19 | `player.py` + `realstate.py` e seus 26 testes. | Exceções de domínio; composição; a propriedade media a relação. |
| Amarras | #20 | `board.py` e 8 testes. | Dicionário jogador→posição; `divmod` para a volta. |
| Coordenação | #21 | `game.py` e 6 testes. | O turno é método; o Factory sai do jogo para o `Player`. |
| Experimento | #22 | `simulation.py`, `__main__.py`. Total: 40 testes. | Monte Carlo com distribuição normal e multiprocessing. |
| Refatoração | #23 | `competitors.py` — ausente do repositório, **reconstruído na seção 21**. | Exclusão lógica; coleção com protocolos da linguagem. |
| Além do curso | — | O motor desacoplado: `report.py`, `cli.py`, `api.py`, `GameSpec` — **seção 23**. | Semente reprodutível; duas interfaces sobre o mesmo motor. |

**O gráfico de crescimento é revelador.** Vinte e três aulas de teoria e modelagem para 5.857 bytes de código — e o melhor sistema de arquivos de todo o projeto (a coleção de competidores) fica fora do repositório publicado. O curso é, nesse sentido, fiel ao seu próprio argumento: *o tempo de pensar é onde está o valor*, e a última refatoração, que nunca foi commitada, é a prova de que modelar não termina com a entrega.

## 15. Arsenal técnico demonstrado no curso

| Recurso | Onde aparece | Para que serve no argumento |
|---|---|---|
| `getattr` e *bound methods* | #06 | Provar que a chamada de método é *envio de mensagem*: o objeto carrega `__self__` e `__func__`. |
| Dunder methods como protocolos | #06, #07, #23 | `__add__`, `__eq__`, `__truediv__`, `__getitem__`, `__iter__` — a linguagem fala com os objetos por protocolos. |
| Classes abstratas (`ABC`) | #07 | Reconstruir hierarquia *depois* da repetição, não antes. |
| `classmethod` como Factory | #07, #21 | Inverter a dependência: quem é instanciado não conhece quem instancia. |
| Mecanismo de registro (`register`) | #07 | Quebrar a dependência circular entre as classes de inteiros. |
| Herança de `dict` | #08 | Criar o ADT que falta: `IntervalMap` encapsula a semântica de intervalos. |
| Dicionário com objeto como chave | #20 | Posição como estado do tabuleiro, usando a identidade do jogador como hash. |
| `divmod` | #20 | Duas informações de uma vez: onde parou e se completou a volta. |
| `itertools.cycle` | #21, #23 | Sequência cíclica de turnos — e sua limitação com estado mutável, que gera a exclusão lógica. |
| `multiprocessing.Pool` | #22 | Rodar 10.000 partidas em segundos. |
| `random.gauss` | #22 | Tabuleiro realista por distribuição normal, em vez de valores uniformes. |
| `Counter` + ordenação por frequência | #22 | Transformar partidas em percentuais de vitória por estratégia. |
| `pytest` com `raises` e *mock* | #18, #20, #21 | Especificar os três desfechos do turno e controlar o dado e o `random.choice`. |
| Exceções de domínio | #18 | Trocar booleanos e `if` por três desfechos nomeados. |
| Exclusão lógica (*delete* virtual) | #23 | Remover da coleção sem quebrar a iteração em curso. |

Uma observação sobre escopo: o arsenal é intencionalmente estreito. Não há decoradores próprios, metaclasses, genéricos nem bibliotecas de terceiros além do `pytest` — coerente com a decisão declarada na aula #18 de “usar Python por acaso”, para que a ideia seja transportável.

## 16. Glossário do curso

| Termo | Definição como usada no curso | Aula |
|---|---|---|
| **Indireção** | Referenciar algo por nome, referência ou continente, em vez do valor em si — *indirection*. | #09 |
| **Barramento** | Via única que substitui a amarração de todos com todos; a metáfora física da indireção. | #09 |
| **Amarração dinâmica** | Resolver *o que executa* em tempo de execução, em vez de compilação. | #09 |
| **Despacho dinâmico** | O mecanismo que encontra o código associado ao tipo do objeto que recebeu a mensagem. | #09 |
| **Decupagem** | Reescrever o texto do cliente parágrafo por parágrafo em frases curtas e sem ambiguidade. Anterior à modelagem. | #16 |
| **Glossário de domínio** | Vocabulário consolidado que a decupagem produz, corrigindo o vocabulário do próprio cliente. | #16 |
| **Cartão CRC** | Nome da classe + responsabilidades (“o que sabe ou faz”) + colaboradores. Ferramenta lúdica, de 1989. | #13, #15 |
| **Vazamento de responsabilidade** | Semântica que não está em lugar nenhum: nem na estrutura de dados, nem no objeto que a usa. | #08, #15 |
| **Classe Deus** | Objeto que concentra tudo. É o motivo declarado de não se criar a classe `Jogo` na #15. | #15 |
| **Design precoce** | Antecipar decisões de código durante a modelagem, contaminando a compreensão. | #14 |
| **Síndrome do arquiteto astronauta** | Desenhar soluções imaginárias antes do contato com o problema. | #11 |
| ***Outsight*** | Compreensão alimentada de fora, por referências externas — em oposição a epifania interna. | #04 |
| **Tipo de dado abstrato (ADT)** | `list`, `dict`, `set`, `tuple`: genéricos por natureza, sem semântica de alto nível. Sacada atribuída a Barbara Liskov. | #08 |
| **Débito técnico** | O que compromete a capacidade futura de alterar o código com facilidade. | #23 |
| **Exclusão lógica** | Marcar em vez de apagar, para não quebrar a iteração em curso. | #23 |
| **Turno / rodada** | Turno é a jogada de um jogador; rodada é o conjunto de turnos de todos. | #16 |
| **Pensamento positivo** | Escrever o teste antes da implementação, ignorando as marcas de erro do editor. | #06 |
| **Localidade** | Critério de alocação de responsabilidade: decide-se olhando o contexto, não o sistema. | #12, #15 |
| **Programação imperativa cooperativa** | O fecho conceitual do curso: controla-se o fluxo, mas a decisão pertence ao receptor da mensagem. | #10 |

## 17. Perguntas & respostas que o curso responde

#### Por que é tão difícil aprender orientação a objetos?

Porque o problema é de percepção, não de sintaxe: quem nasceu num mundo onde o paradigma já existia não consegue enxergá-lo. É o peixe que não sabe que existe água (#01).

#### O que existia antes, e o que doía?

Programação no metal: dados globais, sem gerência de memória, sem reentrância, reaproveitamento nulo. Depois, tipagem estática engessando endereços em tempo de compilação. A dor concreta foi modelar uma simulação de reator nuclear com dados de naturezas distintas (#03).

#### Herança é o principal da orientação a objetos?

Não. O principal é a troca de mensagens. Herança e polimorfismo existem para reconstruir conceitos de alto nível sobre a infraestrutura de mensagens (#05, #07).

#### Por que os exemplos de faculdade (animal, cachorro, gato) são ruins?

Porque enfatizam álgebra e classificação, não o mecanismo: o que importa é que o objeto conhece seu tipo e há um mecanismo que localiza o código — não a taxonomia do mundo real (#05).

#### Mover um procedimento para dentro de uma classe o torna OO?

Não. A sintaxe pode ser idêntica. O que decide é o *efeito* do movimento: se a lógica de manipulação do estado passou a viver dentro dele, sim; se continua fora, é procedural com classe (#10).

#### Preciso desenhar UML antes de programar?

Não — e a direção é o inverso. O UML não tem sequer condicional, logo não modela fluxo. Ele serve para formalizar algo já compreendido, depois do código (#13).

#### Como começo a implementar um sistema orientado a objetos?

Pelas folhas: as entidades com responsabilidade única e poucas relações. “Comendo pelas beiradas, de dentro para fora” (#18).

#### Vale criar uma classe para o dado? E para o turno?

Não, em ambos os casos. As duas não guardam estado. O dado virou um método estático e o turno virou `Board.turn()` (#21).

#### Modelar é espelhar o mundo real?

Não. *“se você tentar modelar o software como o mundo real não vai funcionar”* (#14) e *“você não está fazendo uma simulação de Matrix modelando átomos”* (#17). Modela-se a simulação, não o mundo.

#### A modelagem fica pronta algum dia?

Não. *“A modelagem nunca é definitiva mas ela vai nos ajudando a separar responsabilidade”* (#22) — e o próprio curso reverte três decisões de modelagem ao implementá-las (seção 11).

## 18. Repositórios e recursos

### 18.1 O código do curso

| Recurso | Descrição |
|---|---|
| [github.com/henriquebastos/monopoly](https://github.com/henriquebastos/monopoly) | Repositório oficial do projeto. 7 módulos, 4 arquivos de teste, 40 testes. Um único commit (“Import”). É a fonte de toda a análise de código da seção 19. |

### 18.2 Trechos de código publicados nas aulas

| Aula | Recurso | Conteúdo |
|---|---|---|
| #06 | [Gist da aula](https://gist.github.com/henriquebastos/5bb246853b9d7cc26317fb9ab35e4a28) | Geometrias (ponto, retângulo) e a demonstração de *bound method*. |
| #07 | [Gist da aula](https://gist.github.com/b2bacae88c3a7d2b58229fa5dd6ed4b3) | Inteiros binários: `Byte`, `Word`, `FullAdder`, `Multiplier`, a hierarquia e o registro. |
| #08 | [Gist da aula](https://gist.github.com/henriquebastos/cb033cab3f0710ec73b6f12cfad7c5c8) | `IntervalMap` e a correção do vazamento de responsabilidade. |

### 18.3 Material de apoio citado

| Referência | Assunto |
|---|---|
| [Documento das aulas #10, #11 e #12](https://docs.google.com/document/d/1kyz61BdfBL6OBGvegenPu8jcU9XmTOY25pyK8wMh2LQ/edit) | Material de apoio sobre indireção, modelagem e mentalidade. |
| [Documento da aula #13](https://docs.google.com/document/d/1WIuVUyK8Nm49PE9AfvgcJyDBlw4rbSRkdkoC6OFD7co/edit) | Versão final do documento de técnicas de modelagem. |
| [The Early History of Smalltalk](http://worrydream.com/EarlyHistoryOfSmalltalk/) (Alan Kay) | A fonte primária da aula #04. |
| [Ivan Sutherland e o Sketchpad](https://www.youtube.com/watch?v=6orsmFndx_o) | Uma das referências do *outsight* de Kay. |
| [Douglas Engelbart — “a mãe de todas as demos”](https://www.youtube.com/watch?v=B6rKUf9DWRI) | O NLS e a interação humano-computador. |
| [Ben Eater — o barramento](https://eater.net/8bit/bus) | A base da metáfora da aula #09. |
| [Circuito aritmético (Wikipédia)](https://pt.wikipedia.org/wiki/Circuito_aritm%C3%A9tico) | Apoio para os chips da aula #07. |
| [Squeak](https://squeak.org/) | Ambiente Smalltalk para experimentar a alteração em tempo de execução. |

### 18.4 Canais do instrutor

| Recurso | Descrição |
|---|---|
| [Playlist do curso](https://www.youtube.com/playlist?list=PLeKXYyZCJHxemNCYYvDUw0wRsMiN7aX1m) | As 23 aulas na ordem. |
| [Canal HBNetwork](https://www.youtube.com/@hbnetworkoficial) | Demais playlists de treinamento (Django, Python, Refatoração, APIs). |
| [Discord HBNetwork](https://discord.gg/pTAr89EHMz) | Comunidade de dúvidas e discussão. |
| [Blog do instrutor](https://henriquebastos.net/) | Artigos e material complementar. |

Nota de escopo: os cursos “Design de API na Prática” (9 aulas) e “Orientação a Objetos na Prática” (23 aulas) são séries distintas, mas compartilham o mesmo instrutor e a mesma régua de design — acoplamento, fronteiras e responsabilidade. Estudá-las em conjunto dá uma visão consistente de como Henrique Bastos pensa arquitetura de software.

## 19. Análise linha a linha: os sete módulos do repositório real

Esta seção é o resultado de clonar e ler o código-fonte do repositório. Todos os trechos abaixo são **código real**, copiado dos arquivos, com o caminho e o número de linha indicados — não são ilustrações. O projeto inteiro tem **5.857 bytes de código-fonte** distribuídos em 7 módulos, o que permite reproduzi-lo na íntegra aqui.

### 19.0 A organização

```
monopoly/
├── __init__.py      5 linhas     reexporta Player, RealState, Board, Game, Simulation
├── __main__.py      5 linhas     entry point: roda 10.000 simulações e imprime o relatório
├── player.py       68 linhas     jogador + as três exceções + as 4 estratégias + Factory
├── realstate.py    32 linhas     propriedade: venda, aluguel, retomada, o despachante deal()
├── board.py        39 linhas     posições, voltas, bônus, remoção, turn()
├── game.py         40 linhas     loop do jogo, dado, líder, fim de jogo
├── simulation.py   44 linhas     erro gaussiano do tabuleiro + Monte Carlo em multiprocessing
└── competitors.py  80 linhas     a coleção de jogadores — AUSENTE do repositório, reconstruída na seção 21
tests/
├── test_player.py    91 linhas    15 testes
├── test_realstate.py 84 linhas    11 testes
├── test_board.py     76 linhas     8 testes
├── test_game.py      58 linhas     6 testes
└── test_competitors.py 133 linhas  13 testes — também reconstruídos (seção 21)
```

**Leitura da estrutura:** a árvore é rasa e o acoplamento tem direção única em quase todo o projeto — `player` não importa ninguém do projeto, `realstate` também não, `board` importa de `player`, `game` importa de `board`, `simulation` importa de todos. É exatamente a “descrição em árvore” que a aula #17 prescreveu. Há uma única aresta que contraria a hierarquia, e ela aparece em 19.3.

### 19.1 `player.py` — composição, exceções de domínio e um Factory

**Arquivo:** `monopoly/player.py` — as exceções e as estratégias (linhas 1 a 37)

```
import random

class OutOfMoney(Exception):
    pass

class NotEnoughMoney(Exception):
    pass

class AbortInvestment(Exception):
    pass

class Strategy:
    def __str__(self):
        return self.__class__.__name__

class Impulsive(Strategy):
    @staticmethod
    def should_buy(balance, price, rent):
        return True

class Demanding(Strategy):
    @staticmethod
    def should_buy(balance, price, rent):
        return rent > 50

class Cautious(Strategy):
    @staticmethod
    def should_buy(balance, price, rent):
        return balance - price >= 80

class Gambler(Strategy):
    @staticmethod
    def should_buy(balance, price, rent):
        return random.choice((True, False))

STRATEGIES = (Impulsive(), Demanding(), Cautious(), Gambler())
```

**Leitura linha a linha:**

- **Linhas 4–11 — três exceções de domínio.** É a decisão da aula #18: em vez de devolver `False` ou levantar `Exception`, o sistema nomeia três desfechos distintos. `OutOfMoney` é falência; `NotEnoughMoney` é não ter saldo para a compra; `AbortInvestment` é a estratégia ter dito não. Sem essa separação, o `turn()` do tabuleiro não conseguiria distinguir “não comprou” de “faliu” — e é justamente essa distinção que decide se o jogador sai do jogo.
- **Linhas 13–15 — a classe base só sabe se apresentar.** `__str__` devolvendo o nome da classe é um detalhe pequeno e decisivo: é ele que permite à simulação agrupar os vencedores por estratégia, sem que a simulação conheça as estratégias. Note que a base não declara `should_buy` — não há contrato formal, só convenção.
- **Linhas 17–35 — quatro subclasses, um único critério cada.** Impulsivo compra sempre; Exigente exige aluguel > 50; Cauteloso exige folga de 80; Jogador sorteia. Cada regra do enunciado da aula #14 está aqui em uma linha.
- **Linha 37 — a tupla de instâncias.** `STRATEGIES` guarda *objetos*, não classes. Isso é o que permite ao Factory instanciar jogadores sem decidir nada.
- **Todas são `@staticmethod`.** A consequência é que a estratégia não guarda estado algum: é comportamento puro. Isso explica *por que* as quatro instâncias podem ser compartilhadas globalmente — e é coerente com a recusa do curso em criar objetos sem estado (#21).

**Arquivo:** `monopoly/player.py` — a classe `Player` (linhas 39 a 68)

```
class Player:
    def __init__(self, initial_balance, strategy=Impulsive()):
        self.balance = initial_balance
        self.strategy = strategy

    def pay(self, amount):
        if amount > self.balance:
            raise OutOfMoney(repr(self))

        self.balance -= amount
        return amount

    def receive(self, amount):
        self.balance += amount

    def invest(self, price, rent):
        if price > self.balance:
            raise NotEnoughMoney(f'{self!r} can not aford {price}.')

        if not self.strategy.should_buy(self.balance, price, rent):
            raise AbortInvestment(f'{self!r} aborted the investment.')

        return self.pay(price)

    def __str__(self):
        return str(self.strategy)

    @classmethod
    def from_strategies(cls, balance):
        return [cls(balance, strategy=s) for s in STRATEGIES]
```

**Leitura linha a linha:**

- **Linha 40 — `strategy=Impulsive()` como valor padrão.** Um objeto mutável como default é, em geral, um cheiro de código em Python. Aqui é seguro por acidente feliz: as estratégias são *stateless* (todas as regras são `@staticmethod`), então compartilhar a instância não vaza estado. Se alguém transformasse `should_buy` em método de instância com atributo, este default passaria a ser um bug silencioso.
- **Linhas 44–49 — `pay` devolve o valor pago.** É a linha mais importante do arquivo. Não é enfeite: é o que permite ao recebedor compor a transferência sem tocar no saldo alheio — `self.owner.receive(player.pay(self.rent))`, em `realstate.py`. O método *cobra e devolve*, e quem chamou decide para onde vai o dinheiro.
- **Linha 46 — a exceção carrega o jogador.** `repr(self)` é usado no construtor da exceção; como `__str__` devolve o nome da estratégia, a mensagem final é `'Impulsive'`. Ou seja: o erro da falência se identifica pela estratégia, que é o que interessa estatisticamente.
- **Linhas 54–61 — `invest` verifica duas coisas em ordem.** Primeiro o dinheiro (`NotEnoughMoney`), depois a decisão da estratégia (`AbortInvestment`), e só então chama `pay`. A ordem importa: um jogador sem saldo nunca consulta a estratégia — o que mantém as estatísticas de “abortou” restritas a quem *poderia* comprar.
- **Linha 56 — um erro de digitação no texto.** `'can not aford'` (falta o “f” de *afford*). Registro porque é código real publicado — e porque a mensagem aparece em tracebacks.
- **Linha 61 — `return self.pay(price)`.** `invest` devolve o valor pago, propagando o contrato de `pay`. É a composição em duas camadas que o `sell_to` vai usar.
- **Linhas 66–68 — o Factory é um `classmethod`.** Exatamente o que a aula #21 decide ao vivo: como classes são objetos em Python e existe `classmethod`, não é preciso uma classe `PlayerFactory`. Note que ele usa `cls`, não `Player` — subclasses ganham o Factory de graça.

**Onde está a “conta bancária”.** O `Player` tem dois atributos e três métodos de negócio. Não há posição, não há lista de propriedades, não há referência ao tabuleiro. É a prescrição da aula #17 (*“a responsabilidade do jogador é lidar com dinheiro”*) cumprida literalmente.

### 19.2 `realstate.py` — a propriedade como mediadora

**Arquivo:** `monopoly/realstate.py` (na íntegra, 32 linhas)

```
class RealState:
    def __init__(self, price, rent, owner=None):
        self.price = price
        self.rent = rent
        self.owner = owner

    def has_owner(self):
        return self.owner is not None

    def owner_is(self, player):
        return self.owner is player

    def foreclose(self):
        self.owner = None

    def sell_to(self, player):
        assert not self.has_owner()

        player.invest(self.price, self.rent)
        self.owner = player

    def rent_to(self, player):
        if self.owner_is(player):
            return

        self.owner.receive(player.pay(self.rent))

    def deal(self, player):
        if self.has_owner():
            self.rent_to(player)
        else:
            self.sell_to(player)
```

**Leitura linha a linha:**

- **Linha 2 — `owner=None`.** É a inversão de dependência discutida na aula #19: a propriedade não cria um dono nem conhece quem vai ser; recebe `None` e espera.
- **Linhas 10–11 — `owner_is` usa `is`, não `==`.** Comparação por *identidade*, coerente com a decisão da aula #20 de usar o jogador como chave de dicionário: no domínio, dois jogadores não são “iguais”, são *este* e *aquele*. Não há `__eq__` em `Player`, e portanto `==` cairia na identidade de qualquer forma — mas o `is` explicita a intenção.
- **Linha 17 — `assert not self.has_owner()`.** A regra de negócio “não se vende duas vezes” é garantida por **`assert`**, não por uma exceção de domínio. Duas consequências: (a) o teste `test_sell_error` espera `AssertionError`, uma exceção genérica da linguagem, e não algo como `AlreadyOwned`; (b) executando o Python com `-O`, a verificação **desaparece** e a venda passa a sobrescrever o dono silenciosamente. É a única regra de negócio do projeto protegida por `assert`.
- **Linha 26 — a linha mais elegante do projeto.** `self.owner.receive(player.pay(self.rent))` contém três mensagens em uma: o jogador paga, o pagamento é devolvido como valor, o proprietário o recebe. Nenhum objeto toca o saldo de outro — a transferência *emerge* da composição. É a tese de *Tell, don't ask* reduzida a uma linha, e a razão de `pay()` devolver o valor.
- **Linhas 22–24 — a guarda do dono.** Cair na própria propriedade não gera aluguel. Retorna cedo, sem efeito colateral — e é isto que faz o teste `test_rent_player_is_owner` passar com saldo intacto.
- **Linhas 28–32 — `deal` é o despachante.** Ele decide entre alugar e vender *dentro da propriedade*. É a resposta operacional à pergunta deixada em aberto na aula #14 (“um jogador ativamente vai lá e compra, ou a propriedade se oferece?”): a propriedade decide. Com isso, o `Board` nunca precisa perguntar se a casa tem dono.

**Onde está a mediação.** A propriedade é o único objeto do sistema que conhece *dois* jogadores simultaneamente — o dono e o visitante — e o resultado é uma transferência. É exatamente o papel que a aula #17 lhe atribui, com a analogia do cartório.

### 19.3 `board.py` — posição, ciclo e o `divmod`

**Arquivo:** `monopoly/board.py` (na íntegra, 39 linhas)

```
from monopoly.player import AbortInvestment, NotEnoughMoney, OutOfMoney

BONUS = 100

class Board:
    def __init__(self, players, properties, bonus=BONUS):
        self.players = {p: -1 for p in players}
        self.properties = properties
        self.bonus = bonus

    def move(self, player, steps):
        cur_pos = self.players[player]
        new_lap, new_pos = divmod(cur_pos + steps, len(self))
        self.players[player] = new_pos

        if new_lap:
            player.receive(self.bonus)

        return self.properties[new_pos]

    def __len__(self):
        return len(self.properties)

    def remove(self, player):
        for rs in self.properties:
            if rs.owner_is(player):
                rs.foreclose()

        del self.players[player]

    def turn(self, player, steps):
        real_state = self.move(player, steps)

        try:
            real_state.deal(player)
        except (AbortInvestment, NotEnoughMoney):
            pass
        except OutOfMoney:
            self.remove(player)
```

**Leitura linha a linha:**

- **Linha 1 — a única aresta invertida do projeto.** `board.py` importa três exceções *de* `player`. Tecnicamente correto — o tabuleiro precisa distingui-las — mas é um acoplamento que contraria a árvore prescrita na aula #17: a camada de orquestração conhece detalhes da camada mais folha. Com a classe `Competitors` da #23, o `Board` ganhou ainda mais razões para conhecer o jogador. É o ponto do projeto onde a modelagem prescrita e o código publicado mais se afastam.
- **Linha 3 — `BONUS = 100` no módulo.** O valor da volta como constante de módulo, usado como default na linha 6. Note que a #23 vai eliminar esse *magic number* transformando-o em parâmetro — o que indica que o instrutor considerou a constante insuficiente.
- **Linha 7 — `{p: -1 for p in players}`.** A decisão central da aula #20: dicionário jogador→posição, com `-1` significando “fora do tabuleiro”. É o `-1` que um aluno contestou como “gambiarra” na aula — e que se justifica porque a lista de propriedades começa em zero.
- **Linha 13 — `divmod`.** Uma única operação devolve *duas* informações: quantas voltas completou (`new_lap`) e onde parou (`new_pos`). Toda a contabilidade de “deu a volta?” desaparece do código. É a resposta literal à natureza cíclica do tabuleiro, como discutido em #20.
- **Linha 17 — `player.receive(self.bonus)`.** O bônus vai direto ao jogador; o tabuleiro não mexe em saldo.
- **Linhas 24–29 — `remove` libera propriedades.** Este é o laço que *não existia* na primeira versão e que foi sugerido pela turma na aula #22 — e que mudou materialmente o resultado da simulação. O `del` do dicionário acontece *depois* de mover as propriedades de volta para o mercado.
- **Linhas 34–39 — o tratamento de exceções é o coração do turno.** Três desfechos, três caminhos: `AbortInvestment` e `NotEnoughMoney` caem no mesmo `pass` (não comprou, nada muda); `OutOfMoney` remove o jogador. Note que a ordem dos `except` é significativa em geral, mas aqui as três classes são irmãs (`Exception` direto), então não há hierarquia entre elas.
- **O que o `turn` não faz:** não rola o dado (recebe os passos de fora), não decide quem joga, não verifica fim de jogo. Ele é puramente a execução de uma jogada — e é isso que permite ao `Game` controlar o dado nos testes.

**Verificação empírica dos casos-limite.** Executando o código sem alterá-lo: `Board([], []).turn(Player(10), 1)` levanta `KeyError` (linha 12, o jogador não está no dicionário); `b.move(p, 0)` devolve a propriedade da posição atual sem pagar bônus, e `len(board)` devolve `len(self.properties)`, como o teste `test_len` especifica.

### 19.4 `game.py` — coordenação sem regra de negócio

**Arquivo:** `monopoly/game.py` (na íntegra, 40 linhas)

```
import random
from itertools import cycle

from monopoly import Board

class Game:
    INITIAL_BALANCE = 300

    def __init__(self, players, properties):
        self.players = players
        self.board = Board(self.players, properties)

    @property
    def leader(self):
        return sorted(self.players,
                      key=lambda p: p.balance,
                      reverse=True)[0]

    @staticmethod
    def dice():
        return random.randint(1, 6)

    def run(self, counter=0):
        turn_count = counter

        for p in cycle(self.players):
            if p not in self.board.players:
                continue

            self.board.turn(p, self.dice())
            turn_count += 1

            if len(self.board.players) == 1:
                break

            if turn_count >= 1000:
                break

        return self.leader
```

**Leitura linha a linha:**

- **Linha 4 — `from monopoly import Board`.** O `Game` importa do pacote, não do módulo (`monopoly.board`). Funciona, mas cria uma dependência do `__init__.py` — que por sua vez importa `Simulation`, que importa `Game`. É a segunda aresta fora da árvore, e é o tipo de ciclo que a aula #17 prescreve evitar.
- **Linha 8 — `INITIAL_BALANCE = 300` é código morto.** Verifiquei por execução: o atributo existe e vale 300, mas **nenhuma linha do projeto o lê**. O saldo inicial real vem do literal `300` em `simulation.py`, linha 19 (`generate_players(300)`) e dos testes. A aula #21 havia decidido que “cada jogador ganha a grana inicial” dentro do `Game`; o código publicado não faz isso — o `__init__` não recebe saldo nenhum. É a constante que sobrou de uma decisão abandonada.
- **Linhas 14–18 — `leader` ordena a lista inteira para pegar o primeiro.** Semanticamente correto, e o desempate é determinístico e favorável a quem aparece antes na lista — é isso que faz `test_leader_tie` esperar `players[0]`. O instrutor menciona a tentação de usar `max` e conclui que ele não serve porque `max` pega o primeiro máximo mas não ordena. Custo: O(n log n) para uma consulta que é O(n).
- **Verificação empírica: `Game([], []).leader` levanta `IndexError`** — a lista vazia não é tratada (linha 18, `[0]` sobre uma lista ordenada vazia). O código nunca chega a esse estado porque o jogo termina quando resta um jogador (`len(...) == 1`), mas a propriedade não tem guarda.
- **Linhas 24–25 — `run(counter=0)`.** O parâmetro permite começar com o contador adiantado — e é exatamente assim que o teste de empate força o fim por limite de rodadas: `g.run(998)`. É um parâmetro que existe para o teste, um exemplo honesto de *testability* influenciando a API.
- **Linha 27 — `cycle(self.players)` sobre a lista completa.** Aqui está a raiz da dívida técnica que a aula #23 ataca: o `cycle` percorre *todos* os jogadores, inclusive os eliminados — por isso a linha 28 precisa do `continue` com uma consulta ao `board`. O `Game` mantém a lista; o `Board` mantém o dicionário; e a mesma informação existe em dois lugares, com o `if p not in self.board.players` como sintoma.
- **Linhas 34–38 — as duas condições de parada.** Um jogador restante, ou mil turnos. O limite de 1000 é um *magic number* no corpo do método — e é o segundo que a aula #23 transforma em constante com default.
- **O que o `Game` não tem:** nenhuma regra de negócio. Não cobra aluguel, não debita, não decide compra, não conhece dinheiro. Apenas sequencia e devolve o líder. É a prova de que o encapsulamento funcionou — e o contraste com a “classe Deus” que a aula #15 proibiu.

### 19.5 `simulation.py` — o gerador e o Monte Carlo

**Arquivo:** `monopoly/simulation.py` (na íntegra, 44 linhas)

```
import random
from collections import Counter
from multiprocessing import Pool

from monopoly import Game, Player, RealState

def generate_players(balance):
    players = Player.from_strategies(balance)
    random.shuffle(players)
    return tuple(players)

def generate_properties(how_many, median=5, stdv=1, price_scale=20, rent_scale=10):
    distribution = (round(random.gauss(median, stdv)) for _ in range(how_many))
    params = ((value * price_scale, value * rent_scale) for value in distribution)
    return tuple(RealState(price, rent) for price, rent in params)

def game_factory():
    return Game(generate_players(300), generate_properties(20))

class Simulation:
    def __init__(self, population, pool=5):
        self.population = population
        self.pool = pool
        self.stats = {}

    def run(self):
        with Pool(self.pool) as p:
            winners = p.map(self.exercise, (n for n in range(self.population)))

        self.stats = Counter(winners)

    @staticmethod
    def exercise(_):
        game = game_factory()
        winner = game.run()
        return str(winner)

    def __str__(self):
        output = [f'Simulations: {self.population}']
        output += [f'- {k}: {v} {v / self.population * 100:.1f}%'
                   for k, v in sorted(self.stats.items(), key=lambda t: t[-1], reverse=True)]
        return '\n'.join(output)
```

**Leitura linha a linha:**

- **Linhas 8–11 — `random.shuffle` embaralha as posições.** As quatro estratégias são sempre as mesmas; o que varia é *quem começa*. Fixado o tabuleiro, isso permite medir o efeito da ordem de turno — e o experimento da aula #22 conclui que ele é pequeno.
- **Linha 13 — os cinco parâmetros de escala.** `median=5`, `stdv=1`, `price_scale=20`, `rent_scale=10`. Aqui está a explicação numérica do fracasso da estratégia Exigente: os valores de `gauss(5, 1)` arredondados concentram-se em 4, 5 e 6; multiplicados por 10, os aluguéis típicos ficam entre 40 e 60. O critério `rent > 50` cai exatamente na mediana da distribuição — ou seja, a Exigente rejeita aproximadamente metade das compras disponíveis.
- **Linha 14 — o gerador é *lazy*.** `distribution` é um gerador consumido dentro da linha 15, que também é gerador. Sem problema aqui porque o consumo é imediato na linha 16 — mas é um detalhe que só funciona porque a compreensão é avaliada no mesmo instante.
- **Linha 19 — `game_factory()` com o literal `300`.** É o saldo inicial real do projeto, e o motivo de `Game.INITIAL_BALANCE` ser código morto. Note que a fábrica não recebe parâmetros: cada simulação gera jogadores e um tabuleiro novos.
- **Linha 23 — `pool=5` como default, fixo no código.** O número está escrito no programa, não derivado da máquina. Verifiquei o efeito: numa máquina de 2 CPUs, `pool=2` e `pool=5` levam praticamente o mesmo tempo (2,325 s contra 2,376 s para 5.000 partidas) — o paralelismo satura. Ou seja, o valor embutido é arbitrário para o hardware típico.
- **Linhas 28–32 — `run` usa `pool.map` com um gerador.** O resultado é uma lista de strings (o `str()` do vencedor); `Counter` agrupa. A informação “qual estratégia venceu” viaja como *texto*, dependendo do `__str__` de `Strategy`. Se alguém renomeasse uma estratégia, o relatório mudaria as chaves — e o teste `test_str` protege exatamente isso.
- **Linha 35 — `exercise(_)` ignora o argumento.** O `map` exige uma função de um argumento; o número da partida não é usado. É idiomático, mas o `_` mostra que o dado da iteração é cerimônia.
- **Linhas 40–44 — o relatório.** Ordenação por frequência decrescente (`t[-1]`) e percentual com uma casa decimal. Note o `t[-1]` em vez de `t[1]`: funciona, mas é frágil — se o `Counter` virasse um dicionário de tuplas, `t[-1]` apontaria para o campo errado.

### 19.6 `__init__.py` e `__main__.py`

**Arquivos:** `monopoly/__init__.py` (5 linhas) e `monopoly/__main__.py` (5 linhas)

```
# __init__.py
from .player import Player
from .realstate import RealState
from .board import Board
from .game import Game
from .simulation import Simulation

# __main__.py
from .simulation import Simulation

sim = Simulation(10000)
sim.run()
print(str(sim))
```

**Leitura:** o `__init__.py` reexporta tudo, o que dá ao consumidor a API `from monopoly import Player`. É elegante para quem usa, mas cria a cadeia `game → monopoly → simulation → game`: importar `Game` arrasta `multiprocessing` e todo o simulador. Já o `__main__.py` é a decisão mais limpa do projeto: como ele é o entry point de pacote, `python -m monopoly` roda 10.000 partidas sem arquivo `main.py` nem `if __name__ == '__main__'` — e as quantidades viram parâmetros óbvios do experimento.

A aula #22 menciona um `main.py`; o repositório usa `__main__.py`. Segunda divergência entre a fala e o código publicado.

### 19.7 Os testes

Os quatro arquivos de teste são a especificação executável do sistema. O que cada um cobre:

| Arquivo | Testes | O que especifica |
|---|---|---|
| `test_player.py` | 15 | Saldo inicial e estratégia padrão; `pay` devolve o valor; `receive`; a transferência entre dois jogadores; `OutOfMoney`; as quatro estratégias com seus desfechos; o mock de `random.choice`; `str(p)`; e a ordem do Factory. |
| `test_realstate.py` | 11 | Preço e aluguel; `has_owner`; `owner_is`; `foreclose`; venda e venda indevida (`AssertionError`); aluguel; o dono caindo na própria casa; e os dois ramos de `deal`. |
| `test_board.py` | 8 | Inicialização com dicionário vazio; movimento com bônus; `len`; remoção; e os quatro desfechos do turno: sucesso, investimento abortado, dinheiro insuficiente e falência. |
| `test_game.py` | 6 | Inicialização; líder; empate de líder; o dado no intervalo; vitória por eliminação; e vitória por limite de rodadas. |

**Leitura das escolhas de teste.** Três padrões valem nota. Primeiro: **os testes são a única fonte da especificação que a transcrição não dá** — por exemplo, `test_pay` declara literalmente que `p.pay(10) == 10`, confirmando o contrato de “pagar e devolver”. Segundo: **os valores-limite escolhidos nos testes são o critério da estratégia exposto** — `Demanding` é testada com `rent=51` (compra) e `rent=50` (aborta), fixando a fronteira em `> 50`; `Cautious`, com saldo 180 (compra, sobra 80) e 100 (aborta), fixando a fronteira em `>= 80`. Terceiro: **`test_invest_gambler` é o único lugar do projeto que precisa de mock** (`mocker.patch('random.choice')`), porque é a única decisão não determinística — o que é uma medida indireta de bom acabamento do design.

Um caso notável: `test_sell_error` espera `pytest.raises(AssertionError)`, e não uma exceção de domínio. É a única regra de negócio do sistema verificada por `assert` — e portanto a única que desaparece sob `python -O`, como observado em 19.2.

### 19.8 Síntese: o que o código real ensina

#### O que o código confirma do que foi ensinado

- **Jogador como conta bancária** (#17) — `Player` tem saldo e estratégia, nada mais.
- **A propriedade como mediadora** (#15, #17) — `rent_to` e `deal` concentram toda a interação entre jogadores.
- **Composição em vez de herança** para as estratégias (#18) — o jogador *tem* uma estratégia.
- **Exceções como fluxo de negócio** (#18) — três exceções nomeadas, uma por desfecho.
- **Inversão de dependência** (#17) — o `Game` recebe jogadores prontos; o Factory mora no `Player`.
- **O turno não é objeto** (#21) — é `Board.turn()`, sem estado.
- **Zero regra de negócio no `Game`** — o encapsulamento funcionou.

#### O que o código real deixa em aberto

- **`competitors.py` não existe no repositório** — a refatoração final do curso (aula #23) ficou como exercício, e toda a análise desta seção é do estado *anterior* a ela. A seção 21 reconstrói o módulo e o verifica por execução; a dinâmica do jogo permanece idêntica, mas o *vencedor declarado* muda em raras partidas — porque a refatoração conserta um defeito do `leader` original (seção 21.6).
- **`Game.INITIAL_BALANCE = 300` é código morto** — verificado por execução: ninguém lê o atributo; o saldo vem de um literal em `simulation.py`.
- **O `Board` importa exceções do `Player`** — acoplamento na direção contrária à árvore prescrita na #17.
- **Uma regra de negócio protegida por `assert`** — `sell_to` perde a verificação sob `python -O`.
- **`leader` sem guarda de lista vazia** — `IndexError` verificado em execução; inalcançável pelo fluxo, mas exposto na API.
- **`pool=5` fixo no código** — sem relação com o hardware; em 2 CPUs, `pool=2` entrega o mesmo tempo.
- **O `requirements.txt` não roda como está** — ver seção 20.

## 20. Execução real: os 40 testes e o Monte Carlo

Esta seção não é análise de leitura — é o resultado de executar o repositório clonado. Os números e saídas abaixo são **saída real de terminal** desta sessão, não reconstrução.

### 20.1 Ambiente de execução

| Item | Ambiente A | Ambiente B |
|---|---|---|
| Python | 3.10.21 | 3.12.3 |
| pytest | 7.4.4 | 9.1.1 |
| Resultado | 40 passed em 0,05 s | 40 passed |

Máquina de execução: **2 CPUs**, 1.889 MB de RAM total. Nenhuma linha do código do repositório foi alterada — apenas o ambiente foi preparado.

### 20.2 Os 40 testes, arquivo por arquivo

```
$ .venv310/bin/pytest -q
........................................                                 [100%]
40 passed in 0.05s
```

| Arquivo | Testes | Nomes |
|---|---|---|
| `test_player.py` | 15 | `init`, `pay`, `receive`, `transfer`, `outofmoney`, `invest_impulsive`, `invest_without_money`, `invest_demanding`, `invest_demanding_abort`, `invest_cautious`, `invest_cautious_abort`, `invest_gambler`, `invest_gambler_abort`, `str`, `factory` |
| `test_realstate.py` | 11 | `init`, `not_has_owner`, `has_owner`, `owned_by`, `foreclose`, `sell`, `sell_error`, `rent`, `rent_player_is_owner`, `deal_sell`, `deal_rent` |
| `test_board.py` | 8 | `init`, `move`, `len`, `remove`, `turn_success`, `turn_abort_investment`, `turn_not_enough_money`, `turn_out_of_money` |
| `test_game.py` | 6 | `init`, `leader`, `leader_tie`, `dice`, `run_winner`, `run_tie` |

**O contraste com o curso de APIs** é instrutivo: lá, a suíte crescia com o nível de maturidade (de 2 a 22 testes conforme o projeto evoluía). Aqui a distribuição é o inverso — o maior bloco de testes (15) está no módulo mais folha (`player.py`), e o menor (6) na raiz (`game.py`). Isso não é acidente: é a assinatura de um método que começa de dentro para fora. A parte mais independente é a mais bem especificada, porque foi a primeira a ser escrita e a única que não depende de ninguém.

### 20.3 Um achado de execução: o repositório não roda como se apresenta

O `requirements.txt` pina `pytest==6.1.2`. Em **Python 3.10**, essa combinação quebra na coleta:

```
TypeError: required field "lineno" missing from alias
```

É o `pytest` 6.1.2 manipulando a AST de uma versão de Python mais nova do que ele suporta. A suíte só roda instalando um `pytest` mais recente (7.4.4 foi o usado aqui, e 9.1.1 no Python 3.12). **Como o repositório se apresenta, ele não executa** — precisa de um ajuste de versão. É o mesmo tipo de atrito de ambiente encontrado no projeto do curso de APIs, o que reforça uma lição prática: *pins de dependência são parte do design, e envelhecem*.

### 20.4 O Monte Carlo, executado

O entry point do projeto roda 10.000 partidas. Esta é a saída literal:

```
$ time .venv310/bin/python -m monopoly
Simulations: 10000
- Impulsive: 3963 39.6%
- Cautious: 3773 37.7%
- Gambler: 1677 16.8%
- Demanding: 587 5.9%

real    0m4.754s
user    0m9.313s
sys     0m0.028s
```

Como o experimento é estocástico, repeti em três volumes diferentes para testar a estabilidade do resultado:

| População | Tempo | Impulsive | Cautious | Gambler | Demanding |
|---|---|---|---|---|---|
| 2.000 | 0,95 s | 39,9% | 38,7% | 15,2% | 6,2% |
| 10.000 (execução 1) | 4,81 s | 38,8% | 39,1% | 16,3% | 5,8% |
| 10.000 (execução 2, entry point) | 4,75 s | 39,6% | 37,7% | 16,8% | 5,9% |
| 20.000 | 9,38 s | 39,7% | 39,2% | 15,4% | 5,7% |

**Leitura dos números.** O resultado é notavelmente estável: em quatro execuções independentes, a faixa da Impulsiva é 38,8%–39,9% e a da Cautelosa é 37,7%–39,2% — as duas empatam tecnicamente na liderança, e a ordem entre elas *troca* entre execuções. Isso não é ruído a ser corrigido: é o resultado honesto do experimento, e significa que **ser impulsivo e ser cauteloso são estratégias estatisticamente equivalentes neste tabuleiro**. As duas conclusões robustas são: o Jogador aleatório ganha cerca de uma vez em seis (≈16%), e a Exigente perde feio, com menos de 6%.

E há uma explicação numérica precisa para o fracasso da Exigente, que sai direto do código: o critério é `rent > 50` (`player.py`, linha 25), mas o tabuleiro é gerado com `gauss(5, 1)` multiplicado por `rent_scale=10` (`simulation.py`, linha 13). Os aluguéis típicos ficam entre 40 e 60 — ou seja, o critério está *exatamente na mediana da distribuição*, e rejeita cerca de metade das compras disponíveis. Não é uma estratégia ruim por conceito; é uma estratégia cujo limiar foi calibrado por acidente contra a distribuição de aluguéis do próprio simulador.

### 20.5 A escala do paralelismo

Como o `pool=5` está fixo no código, testei se o valor faz sentido para o hardware:

```
população=5000
pool=1  tempo=4.504s
pool=2  tempo=2.325s
pool=5  tempo=2.376s
```

**Leitura:** o ganho de paralelismo satura em `pool=2`, exatamente o número de CPUs da máquina — e `pool=5` é fração de segundo *mais lento* que `pool=2`, pelo custo de gerenciar processos ociosos. O default de 5 é arbitrário e não se adapta ao ambiente; um `os.cpu_count()` seria mais honesto, e é exatamente o tipo de *magic number* que a aula #23 começou a eliminar (o limite de turnos e o bônus), mas que sobreviveu no simulador.

### 20.6 Verificação cruzada dos casos-limite

Para checar as conclusões da seção 19 contra o comportamento real (sem alterar o código):

```
$ python - <<'PY'
from monopoly import Player, RealState, Game, Board
print("Game.INITIAL_BALANCE existe?", hasattr(Game,'INITIAL_BALANCE'), "->", Game.INITIAL_BALANCE)
try:
    g = Game([], []); print("Game([],[]).leader ->", g.leader)
except Exception as e:
    print("Game([],[]).leader ->", type(e).__name__, ":", e)
try:
    b = Board([], []); print("Board([],[]).turn ->", b.turn(Player(10), 1))
except Exception as e:
    print("Board([],[]).turn ->", type(e).__name__)
p = Player(100); r = RealState(100,10); b = Board([p],[r])
print("move 0 casas devolve a propriedade:", b.move(p,0) is r, "| len(board):", len(b))
print("pay devolve o valor:", p.pay(30), "| saldo:", p.balance, "| receive devolve:", p.receive(30), "| saldo:", p.balance)
PY
```

```
Game.INITIAL_BALANCE existe? True -> 300
Game([],[]).leader -> IndexError : list index out of range
Board([],[]).turn -> KeyError
move 0 casas devolve a propriedade: True | len(board): 1
pay devolve o valor: 30 | saldo: 170 | receive devolve: None | saldo: 200
```

**O que esta verificação estabelece.** Primeiro: `Game.INITIAL_BALANCE` existe e vale 300, mas é código morto (nenhuma linha do projeto o consulta) — a constante sobreviveu à decisão que a criou. Segundo: as duas APIs expostas sem guarda falham com exceções genéricas da linguagem (`IndexError`, `KeyError`), não com exceções de domínio — coerente com o padrão do projeto, que reserva exceções nomeadas para as regras de negócio, não para os erros de uso. Terceiro: o contrato de `pay` é confirmado na prática — ele devolve o valor pago (30), enquanto `receive` devolve `None`; essa assimetria é deliberada e é o que torna possível a linha de transferência em `realstate.py`.

### 20.7 O contraste em uma linha

Vinte e três aulas, 8 horas de vídeo, 4 aulas de modelagem, 5.857 bytes de código — e um experimento que produz um empate estatístico entre a estratégia mais simples possível (comprar sempre) e a mais criteriosa das quatro. O curso não esconde o resultado: ele o comenta ao vivo, estranha, testa variações e conclui que a modelagem cumpriu seu papel — *separar responsabilidades para que evoluir seja possível*. O valor do projeto não está no vencedor do Banco Imobiliário, e sim no fato de que trocar a regra da Estratégia Exigente, ou a distribuição do tabuleiro, exige alterar exatamente uma linha em um dos dois arquivos — e nada mais.

## 21. A reconstrução do `competitors.py` — fechando a aula #23

A aula #23 é a única do curso cujo arquivo central não foi publicado: o repositório tem 7 módulos e nenhum `competitors.py`. Esta seção reconstrói esse módulo a partir do que a aula especifica — a interface ditada pelos testes, a exclusão lógica, o ciclo que para quando resta um jogador — e depois o **verifica por execução**, inclusive contra o próprio repositório original.

O resultado é um módulo novo, **13 testes** novos e uma suíte de **53 testes** passando em dois ambientes de Python. E, no caminho, um achado: a refatoração da aula #23 **conserta um defeito do código original sem que a aula mencione que ele existe** — o `leader` do repositório coroa jogadores já eliminados (seção 21.6).

### 21.1 O que a aula especifica

Tudo abaixo vem da fala transcrita da aula #23. É a especificação a que a reconstrução teve de obedecer.

| Elemento | O que a aula diz | Como a reconstrução resolve |
|---|---|---|
| O diagnóstico | A mesma informação (os jogadores) vive no `Game` e no `Board`: “um triângulo entre game, jogadores e board… tudo conectado misturado” (6:59). | Uma única coleção, `Competitors`, dona do estado dos jogadores. |
| O nome | Descartado `PlayerCollection` — “achei que ficou muito misturado, então decidi criar um conceito novo” (7:40). | Classe `Competitors`, no arquivo `competitors.py`. |
| O método | “Primeiro o arquivo de teste”, para desenhar a interface antes da implementação (8:55). | `tests/test_competitors.py` escrito antes de `competitors.py`. |
| A interface | Acesso por colchete, atribuição, remoção, `len`, iteração — tudo o que o `Board` já exigia. | `__getitem__`, `__setitem__`, `__delitem__`, `__len__`, `__iter__`. |
| A exclusão | “Estratégia de *delete* virtual dos nossos players” (16:41) — marcar em vez de apagar. | `self.removed = set()`; a iteração pula quem está marcado. |
| O ciclo | “Criar um método `cycle` para encapsular” (23:27); deve parar “quando sobrar um jogador” (23:48). | `cycle()` com `return` quando `len(self) == 1`. |
| O líder | “O líder do game é só um *proxy*” (33:35) — a decisão migra para a coleção. | `Competitors.leader` como `@property`; o `Game` apenas delega. |
| Os magic numbers | O limite de 1000 turnos vira constante; o bônus de 100 vira parâmetro com default (34:22). | `MAX_TURNS = 1000`; `Board(..., bonus=BONUS)`. |

### 21.2 O módulo reconstruído

**Arquivo:** `monopoly/competitors.py` — reconstruído a partir da aula #23. Código completo:

```
"""A coleção de jogadores — a abstração que a aula #23 constrói ao vivo."""
from itertools import cycle as _cycle

class Competitors:
    """Coleção de jogadores com posição, exclusão lógica e ciclo de turnos."""

    def __init__(self, players=()):
        # Posição -1 = fora do tabuleiro. O dicionário usa o jogador como chave:
        # objetos são hashiáveis por identidade no Python (aula #20).
        self.players = {player: -1 for player in players}
        # Aula #23: "delete virtual" — o conjunto dos que saíram do jogo.
        self.removed = set()

    # --- protocolos da linguagem: a interface que o Board exige -------------

    def __getitem__(self, player):
        return self.players[player]

    def __setitem__(self, player, position):
        self.players[player] = position

    def __delitem__(self, player):
        # Exclusão LÓGICA: marca em vez de apagar. O `self.players` continua
        # com todos — é isso que permite ao game não perder o controle de
        # quem eram os competidores originais.
        self.removed.add(player)

    def __len__(self):
        return len(self.players) - len(self.removed)

    def __iter__(self):
        # Gerador direto, sem classe iteradora separada (aula #23).
        # A iteração só contempla quem ainda está no jogo.
        for player in self.players:
            if player in self.removed:
                continue
            yield player

    # --- o ciclo de turnos --------------------------------------------------

    def cycle(self):
        """Ciclo infinito de turnos, interrompido quando resta um competidor."""
        for player in _cycle(self.players):
            if player in self.removed:
                continue

            yield player

            # Sobrou um: o jogo acabou, e o ciclo tem de parar.
            if len(self) == 1:
                return

    # --- estado derivado ----------------------------------------------------

    @property
    def leader(self):
        """Quem tem o maior saldo entre os competidores ainda no jogo."""
        return max(self, key=lambda p: p.balance)
```

### 21.3 O desenho da interface — o que cada protocolo resolve

| Protocolo | Por que existe | O que substitui |
|---|---|---|
| `__getitem__` | O `Board` pergunta a posição com `competitors[player]`. Sem ele, o erro é literalmente *“não é subscriptável”*. | `self.players[player]` do antigo `Board`. |
| `__setitem__` | O movimento escreve a nova posição. É a última peça que o `move()` precisava. | A escrita direta no dicionário do tabuleiro. |
| `__delitem__` | **Não apaga** — marca em `self.removed`. É a exclusão lógica. | O `del self.players[player]` do `Board`, que destruía a informação. |
| `__len__` | Devolve quantos *ainda jogam*. É o critério de fim de jogo, e o `Board` não precisa mais saber quem foi removido. | `len(self.board.players)`, que contava o dicionário cru. |
| `__iter__` | Gerador que percorre só os ativos. Feito como gerador direto, sem uma classe iteradora separada. | A lista paralela do `Game` — a raiz da ambiguidade de estado. |
| `cycle()` | O ciclo de turnos com parada automática. Encapsula a regra do fim do jogo. | `itertools.cycle(self.players)` mais o `if p not in board.players: continue` dentro do `Game.run`. |
| `leader` | Estado derivado: o maior saldo. Como `@property`, é sempre recalculado — nunca fica obsoleto. | O `Game.leader`, que ordenava a lista inteira de jogadores. |

**A pegadinha do ciclo.** A aula registra o momento em que o ciclo falha: o `itertools.cycle` guarda os itens numa cache interna e **não enxerga o estado alterado durante a iteração**. Por isso a reconstrução percorre o dicionário bruto e consulta `self.removed` a cada volta — a pergunta que o `cycle` do Python não faz sozinho. É a lição que a aula resume como *“veja a importância do teste”* (26:52), e o teste `test_cycle_skips_removed_mid_iteration` existe para travá-la.

### 21.4 O que muda no `Board` e no `Game`

O refactor não acrescenta uma classe — *substitui* a posse do estado. As duas mudanças essenciais:

```
# ANTES — monopoly/board.py (repositório original)
class Board:
    def __init__(self, players, properties, bonus=BONUS):
        self.players = {p: -1 for p in players}   # o Board era dono do estado
        ...
    def __len__(self):                            # e de quem está no jogo
        return len(self.properties)               # <- ambíguo: len do tabuleiro

# DEPOIS — a coleção passa a ser dona do estado
class Board:
    def __init__(self, competitors, properties, bonus=BONUS):
        self.competitors = competitors
        ...
    def remove(self, player):
        for rs in self.properties:
            if rs.owner_is(player):
                rs.foreclose()
        del self.competitors[player]              # exclusão lógica, não del
```

```
# ANTES — monopoly/game.py (repositório original)
def run(self, counter=0):
    for p in cycle(self.players):                 # a lista completa
        if p not in self.board.players:           # <- o sintoma do acoplamento
            continue
        self.board.turn(p, self.dice())
        ...
        if len(self.board.players) == 1:
            break

# DEPOIS — o Game deixa de gerenciar quem jogou
def run(self, counter=0):
    for player in self.competitors.cycle():       # a coleção decide quem joga
        self.board.turn(player, self.dice())
        ...
        if len(self.competitors) == 1:
            break
```

**Leitura do diff.** O `if p not in self.board.players: continue` desaparece — era o sintoma que o instrutor diagnostica como *code smell* (“algo não tá cheirando bem”, 16:07). O `Game.run` perde duas responsabilidades: não sabe mais quem foi eliminado nem quando o jogo termina. E o `Game.leader` vira uma linha, delegando à coleção.

### 21.5 A verificação: 53 testes em dois ambientes

Os 40 testes originais continuam intactos — o refactor é transparente para eles, exceto pela assinatura do `Board`, que agora recebe um `Competitors` em vez de uma lista. Somam-se os 13 testes novos.

```
$ .venv310/bin/pytest -q          # Python 3.10.21 + pytest 7.4.4
.....................................................                    [100%]
53 passed in 0.12s

$ .venv312/bin/pytest -q          # Python 3.12.3 + pytest 9.1.1
.....................................................                    [100%]
53 passed in 0.10s
```

| Arquivo | Testes | Origem |
|---|---|---|
| `test_player.py` | 15 | Repositório original |
| `test_realstate.py` | 11 | Repositório original |
| `test_board.py` | 8 | Original, com o `Board` adaptado à coleção |
| `test_game.py` | 6 | Repositório original — **passam sem alteração** |
| `test_competitors.py` | 13 | Reconstruídos (seção 21) |
| **Total** | **53** | 40 originais + 13 novos |

**O detalhe mais importante desta tabela** é a linha do `test_game.py`: os seis testes do jogo passaram *sem uma única alteração*. Eram eles que exercitavam o comportamento de fim de jogo que a refatoração moveu de lugar — e continuam válidos porque o comportamento observável não mudou. É a demonstração de que o encapsulamento foi preservado, e o mesmo vale para `test_player.py` e `test_realstate.py`, que nem sabem que a coleção existe.

### 21.6 O experimento de equivalência: 397 de 400 partidas — e um defeito do original

Para verificar se a reconstrução preserva o comportamento, rodei o **mesmo experimento nos dois códigos**: 400 partidas sequenciais, sem multiprocessing, com a mesma semente (`random.seed(1234)`) e a mesma política de geração de jogadores e tabuleiro. O resultado:

|  | Partidas idênticas | Divergências | Natureza da divergência |
|---|---|---|---|
| Original × Reconstrução | **397 / 400** | 3 (partidas 102, 324 e 359) | Todas em *quem é declarado vencedor* — nunca na dinâmica |

**Por que se pode afirmar que a dinâmica é idêntica.** Cada partida consome números aleatórios da mesma sequência compartilhada; se qualquer decisão de jogo divergisse — uma compra, um sorteio de dado — o consumo de aleatoriedade se desalinharia e *todas* as partidas seguintes divergiriam em cascata. Como apenas 3 partidas de 400 divergem, e nenhuma delas altera o fluxo da seguinte, a conclusão é que a sequência de eventos é a mesma; o que muda é apenas o valor **reportado** no fim.

E a causa é precisa. Os três casos têm a mesma estrutura — há jogadores eliminados com saldo positivo:

| Partida | Eliminados (saldo final) | Original declara | Reconstrução declara | Maior saldo *entre todos* |
|---|---|---|---|---|
| 102 | Impulsive 10 · Cautious 40 · Demanding 20 | Cautious (eliminado) | Gambler (sobrevivente) | Cautious |
| 324 | Demanding 10 · Impulsive 50 · Cautious 40 | Impulsive (eliminado) | Gambler (sobrevivente) | Impulsive |
| 359 | Impulsive 40 · Demanding 40 · Cautious 30 | Impulsive (eliminado) | Gambler (sobrevivente) | Impulsive |

**O defeito do original.** O `Game.leader` do repositório ordena *todos* os jogadores — inclusive os que já saíram do jogo:

```
# REPOSITÓRIO ORIGINAL — coroa um eliminado
@property
def leader(self):
    return sorted(self.players, key=lambda p: p.balance, reverse=True)[0]

# RECONSTRUÇÃO — itera apenas quem ainda está no jogo
@property
def leader(self):
    return max(self, key=lambda p: p.balance)
```

Como a falência por `OutOfMoney` pode acontecer com saldo **positivo** — basta o aluguel exceder o saldo, sem zerá-lo —, um jogador eliminado pode terminar com mais dinheiro que o sobrevivente. Nas três partidas acima, o original coroa justamente esse jogador. A refatoração da aula #23 corrige o problema *de graça*: ao mover o líder para dentro da coleção, e ao fazer a coleção iterar somente os ativos, o critério passa a ser “maior saldo **entre os que ainda jogam**”. A aula toca no assunto de passagem, na frase sobre o líder ser *“só um proxy”* (33:35), mas não registra que estava consertando um defeito.

#### O que este achado significa para o curso

Não é um erro de ensino: é a demonstração mais concreta da tese que atravessa as 23 aulas. A aula #23 diagnostica uma *ambiguidade de estado* — os jogadores em dois lugares — sem saber que ela produzia um resultado errado. Ao eliminar a ambiguidade, o defeito desaparece como consequência. É exatamente o que a aula #17 previu ao dizer que se deve *evitar ciclos* e que a boa abstração *abre campo*: o código deixa de ser capaz de expressar o erro.

### 21.7 O que é reconstrução fiel e o que é inferência

Como a legenda automática corrompe identificadores, três decisões não puderam ser lidas da fala e foram tomadas por engenharia. Registro cada uma, para que ninguém confunda reconstrução com transcrição.

| Ponto | A aula diz | Decisão da reconstrução | Grau de certeza |
|---|---|---|---|
| `leader` | A legenda sugere `max(self.players, ...)` — o que reproduziria o defeito. | `max(self, ...)`, iterando só os ativos. | **Inferência.** É a única mudança de comportamento; os testes a especificam e o experimento 21.6 a expõe. |
| `initial_balance` | A aula #21 creditava 300 dentro do `Game`. | `initial_balance=None` por padrão — creditar de novo dobraria o saldo e quebraria `test_init`. | **Inferência.** O parâmetro existe e funciona quando passado explicitamente. |
| `MAX_TURNS` | Constante com default, eliminando o magic number de 1000. | `MAX_TURNS = 1000` no módulo `game.py`. | **Fiel** ao que a aula descreve. |
| Exclusão lógica via `set` | “Estratégia de *delete* virtual”, conjunto de removidos, `len` descontando. | `self.removed = set()`; `__len__` devolve `total − removidos`. | **Fiel.** Os testes travam o comportamento descrito. |
| `cycle()` com parada | Encapsular o ciclo e parar quando resta um jogador. | `return` quando `len(self) == 1`. | **Fiel.** |

O repositório original permanece intacto: todo o trabalho foi feito numa cópia separada, justamente para que a comparação da seção 21.6 não fosse contaminada. O código reconstruído está reproduzido na íntegra em 21.2 e foi publicado como arquivo separado, junto dos 13 testes, para quem quiser executá-lo.

## 22. Os gists do curso, executados

**Correção — ver §24.** Esta seção afirmava que o gist da aula #07 publicava apenas a camada de bits. **Estava errado:** o gist traz também `integers.py`, com a hierarquia completa e os testes do autor. A contagem de testes executados passa de 11 para **31** (2 + 14 + 15). Detalhamento e errata completa na §24.

O curso publica três trechos de código em gists: as geometrias da aula #06, os inteiros binários da #07 e o `IntervalMap` da #08. Até aqui, este documento os descrevia *pela fala* — como as seções 6 e 7 deixam claro. Esta seção faz o que faltava: baixa os três, executa e compara o que eles de fato contêm com o que as aulas descrevem.

Os três rodam e passam: **11 testes**, todos verdes, em Python 3.10 com pytest 7.4.4. Mas a comparação com a transcrição revela algo mais interessante do que a execução em si — e é o achado desta seção.

### 22.1 O que foi executado

```
$ pytest -q aula06_geometria.py aula07_binarios.py aula08_intervalmap.py
...........                                                              [100%]
11 passed in 0.17s
```

| Aula | Arquivo | Conteúdo real do gist | Testes |
|---|---|---|---|
| #06 | `aula06_geometria.py` | `Point` com `__eq__`, `__add__`, `__truediv__`, `__repr__`; `Rect` com `center()`. | 2 |
| #07 | `aula07_binarios.py` | `Bits` (subclasse de `bytes`), `Byte`/`Word`/`Tribyte`/`DoubleWord`, `fulladder`, `adder`, `multiplier`. | 7 |
| #08 | `aula08_intervalmap.py` | `IntervalMap` com `limits` ordenado, `__setitem__` e `get` que levanta `KeyError` no limite. | 1 (9 asserções) |

### 22.2 O achado: o gist da aula #07 não contém o conteúdo da aula #07

A aula #07 é, segundo a transcrição, dedicada a construir `Int8`, `Int16`, `Int24` e `Int32`, diagnosticar o acoplamento em cadeia, extrair a repetição para `select`, transformá-lo em `classmethod` e inverter a dependência com `Integer.register`. Busquei cada um desses identificadores nos três gists:

| Identificador citado na aula #07 | Está no gist? |
|---|---|
| `Int8`, `Int16`, `Int24`, `Int32` | Ausente |
| `class Integer` (a classe abstrata com `ABC`) | Ausente |
| `Factory` (o `classmethod`) | Ausente |
| `register` (o mecanismo de registro que quebra o ciclo) | Ausente |
| `select` (a função extraída da repetição) | Ausente |
| `ABC` | Ausente |

**O que o gist contém, então?** O estágio *anterior*: a camada de bits (`Bits`, `Byte`, `Word`, `Tribyte`, `DoubleWord`) e os circuitos aritméticos (`fulladder`, `adder`, `multiplier`). Ou seja, o gist publica a **infraestrutura sobre a qual a hierarquia de inteiros é construída** — e não a hierarquia, que é justamente o objeto da aula. A parte mais importante da aula #07 (o diagnóstico de acoplamento e a inversão de dependência) existe apenas no vídeo.

#### O que isso significa para este documento

A descrição da hierarquia `Int8`…`Integer` na seção 7 permanecia, até a seção 24, baseada **apenas na transcrição** — e o mesmo valia para o `select` e o `register`. Não era possível verificar aqueles trechos como se verifica o `monopoly`, porque o código não foi publicado. Era a *segunda* lacuna da série, ao lado do `competitors.py`, e provavelmente a maior: o `monopoly` é código de produção com testes; o material dos inteiros é didático, publicado pela metade. A **seção 24 reconstrói a hierarquia e a verifica por execução** — e a ponte que ela estabelece com a aula #08 demonstra, em código, o defeito de ordem que a aula #08 vem corrigir.

### 22.3 O gist da aula #06 é a versão já refatorada

A aula #06 discute em detalhe um código **acoplado**: o retângulo acessando `top_left.x` e `bottom_right.y` para calcular o centro por conta própria. Mas o gist publicado não tem esse código — ele tem o resultado da correção:

```
class Rect:
    def __init__(self, topLeft, botRight):
        self.topLeft = topLeft
        self.botRight = botRight

    def center(self):
        return (self.topLeft + self.botRight) / 2      # delega ao Point
```

**Leitura:** o centro é calculado por uma única expressão que *delega* ao ponto — usa o `__add__` e o `__truediv__` de `Point`, sem tocar em coordenada nenhuma. É exatamente o desfecho da refatoração descrita na aula. O gist, portanto, é o *estado final*, não o *estado discutido*. Duas observações adicionais: o código usa **camelCase** (`topLeft`, `botRight`), ao contrário do snake_case do `monopoly`; e `center` é um **método** (`r.center()`), não uma propriedade — o que explica por que a aula inspeciona `r.center` no terminal: ali se discute o *bound method*, e a chamada é o argumento.

### 22.4 O `IntervalMap` publicado é o corrigido — mas isolado

O gist da aula #08 traz o `IntervalMap` na forma final: `limits` mantido ordenado a cada atribuição e `get` percorrendo os limites até achar o intervalo — a correção do “funciona por acaso” que a aula diagnostica ao vivo. O que ele *não* traz é o contexto: não há `Integer`, não há `types`, não há o `Factory`, nem o `select`. O gist publica **a estrutura de dados isolada**, sem o sistema que a motivou — que é o mesmo padrão da #07: o artefato sem o argumento.

#### O padrão dos três gists

Os três publicam o *pedaço autocontido* — a geometria, a camada de bits, o mapa de intervalos — e omitem *o sistema que dá sentido ao pedaço*: a refatoração que revela o acoplamento (#06), a hierarquia que revela a inversão de dependência (#07), a classe que usa o mapa (#08). É o oposto do `monopoly`, que é publicado inteiro, com testes e simulador. A lição prática para quem estuda a série é desconfortável, mas precisa ser dita: **para as aulas #06, #07 e #08, o vídeo é a única fonte do argumento central** — o gist confirma a sintaxe, não a tese.

## 23. O desafio final resolvido: o motor desacoplado

A aula #23 termina deixando um desafio em aberto (38:26): desacoplar a simulação, para que ela possa ser dirigida por outra interface — ele menciona a linha de comando e chega a citar GraphQL como possibilidade. Esta seção resolve o desafio e verifica a solução por execução.

### 23.1 O acoplamento que o curso deixa

No repositório, o motor de simulação concentra quatro responsabilidades que não são dele:

| Responsabilidade | Onde estava | Por que é um problema |
|---|---|---|
| Formatação do relatório | `Simulation.__str__` | O motor conhece o layout do texto; para uma API, ele é inútil. |
| Decisão de quanto rodar | `__main__.py` com `10.000` literal | O número está no código, não vem de fora. |
| Configuração da partida | `game_factory()` com `300` e `20` literais | Não há como variar tabuleiro ou saldo sem editar o módulo. |
| Número de processos | `pool=5` fixo | Achado da seção 19.5: `5` é arbitrário para o hardware. |

### 23.2 A arquitetura da solução

Quatro módulos, cada um com uma responsabilidade, e **duas** interfaces independentes sobre o mesmo motor:

```
monopoly/
├── simulation.py    o MOTOR      roda N partidas, devolve estatísticas. Não formata, não imprime.
├── report.py        a APRESENTAÇÃO  formata texto e estrutura de dados, fora do motor.
├── cli.py           FRONT-END 1  linha de comando: lê argv, decide o formato, imprime.
├── api.py           FRONT-END 2  programática: recebe dict, devolve dict. Sem argv, sem print.
└── __main__.py      o atalho: python -m monopoly
```

**O núcleo do motor** — note o que ele devolve e o que ele *não* faz:

```
class Simulation:
    def __init__(self, population, pool=None, seed=None, spec=None):
        self.population = population
        self.pool = pool if pool is not None else os.cpu_count()   # nao mais o 5 fixo
        self.seed = seed
        self.spec = spec if spec is not None else GameSpec()
        self.stats = Counter()

    def run(self):
        args = ((index, self.seed, self.spec) for index in range(self.population))
        with Pool(self.pool) as p:
            winners = p.map(_play, args)

        self.stats = Counter(winners)
        return self.stats            # devolve dados — nao imprime relatorio

    def records(self):
        return [{'strategy': name, 'wins': wins,
                 'share': round(wins / self.population * 100, 2)}
                for name, wins in sorted(self.stats.items(),
                                         key=lambda item: item[1], reverse=True)]
```

**A configuração injetada.** O que antes era literal dentro de `game_factory` vira um objeto que a interface monta:

```
class GameSpec:
    """A configuracao de uma partida — o que uma interface externa fornece."""
    def __init__(self, balance=DEFAULT_BALANCE, properties=DEFAULT_PROPERTIES):
        self.balance = balance
        self.properties = properties

    def build(self):
        return Game(generate_players(self.balance),
                    generate_properties(self.properties))
```

**O segundo front-end.** A prova de que o desacoplamento é real não é a existência da CLI — é a existência de uma segunda interface radicalmente diferente que usa o mesmo motor sem que ele saiba disso:

```
def run_simulation(population=10_000, pool=None, seed=None, balance=300, properties=20):
    """O que um resolver GraphQL chamaria: recebe dict, devolve dict."""
    spec = GameSpec(balance=balance, properties=properties)
    simulation = Simulation(population, pool=pool, seed=seed, spec=spec)

    return {
        'population': population, 'seed': seed, 'pool': simulation.pool,
        'spec': {'balance': balance, 'properties': properties},
        'results': as_records(simulation.run(), population),
    }
```

### 23.3 Uma correção que veio de graça: semente reprodutível

Ao desacoplar a execução, apareceu um defeito que a seção 21 já havia esbarrado: **o resultado não era reproduzível com `pool > 1`**. A versão do curso deixa cada processo herdar o estado global do `random` via *fork*, e o resultado passa a depender de quantos processos rodaram. A correção é semear cada partida a partir do seu índice:

```
def _play(args):
    index, seed, spec = args
    if seed is not None:
        random.seed(seed + index)     # cada partida, sua propria semente
    return str(spec.build().run())
```

Com isso, o resultado é **idêntico independentemente do número de processos** — verificado, com 3.000 partidas:

```
pool=1: {'Cautious': 1181, 'Impulsive': 1215, 'Demanding': 170, 'Gambler': 434}
pool=5: {'Cautious': 1181, 'Impulsive': 1215, 'Demanding': 170, 'Gambler': 434}
IDENTICOS? True
```

É a diferença entre um experimento e uma anedota. Sem isso, cada mudança no ambiente de execução mudaria as conclusões estatísticas — e a seção 20.4, que precisou rodar quatro vezes para argumentar que as diferenças eram ruído, seria impossível de escrever.

### 23.4 As duas interfaces, em execução

```
$ python -m monopoly -n 5000 -p 2 --seed 2024
Simulations: 5000
- Impulsive: 2031 40.6%
- Cautious: 1935 38.7%
- Gambler: 753 15.1%
- Demanding: 281 5.6%

$ python -m monopoly -n 5000 -p 2 --seed 2024 --json
[{"strategy": "Impulsive", "wins": 2031, "share": 40.62},
 {"strategy": "Cautious", "wins": 1935, "share": 38.7}, ...]
```

```
>>> from monopoly.api import run_simulation
>>> run_simulation(population=5000, pool=2, seed=2024)
{'population': 5000, 'seed': 2024, 'pool': 2,
 'spec': {'balance': 300, 'properties': 20},
 'results': [{'strategy': 'Impulsive', 'wins': 2031, 'share': 40.62},
             {'strategy': 'Cautious', 'wins': 1935, 'share': 38.7},
             {'strategy': 'Gambler', 'wins': 753, 'share': 15.06},
             {'strategy': 'Demanding', 'wins': 281, 'share': 5.62}]}
```

**Leitura:** as duas interfaces produzem exatamente os mesmos números (2031 / 1935 / 753 / 281) porque chamam o mesmo motor com a mesma semente — uma imprime texto, a outra devolve estrutura. E a API não escreve nada em `stdout`: há um teste que verifica isso, porque um motor que imprime é um motor que não pode ser embutido em outro programa.

### 23.5 A verificação: 69 testes, nos dois ambientes

```
$ .venv310/bin/pytest -q     # Python 3.10.21 + pytest 7.4.4
.....................................................................  [100%]
69 passed in 2.85s

$ .venv312/bin/pytest -q     # Python 3.12.3 + pytest 9.1.1
.....................................................................  [100%]
69 passed in 1.61s
```

Os 16 testes novos cobrem o desacoplamento, não a mecânica do jogo: reprodutibilidade com semente, **identidade entre pools diferentes**, o formato dos registros, a separação entre motor e relatório, e as duas interfaces (parsing da CLI, saída `--json`, recusa de população inválida, e a ausência de saída da API). Dois deles têm valor documental:

- `test_deterministic_across_pool_sizes` — trava a correção da seção 23.3. Se alguém voltar a depender do estado global do `random`, ele falha.
- `test_report_is_outside_the_engine` — verifica que `str(sim)` *não* contém `'Simulations:'` e que o relatório aparece em `report.py`. É o teste que impede o acoplamento de voltar.

### 23.6 O que o desafio revela sobre o método do curso

O desafio final não era um exercício de estilo: era o teste de consistência da série inteira. Tudo o que as 23 aulas prescrevem — responsabilidade única, localidade, evitar ciclos, deixar a abstração emergir — aplica-se ao próprio simulador. E ao aplicá-lo aparece o que a seção 21 já insinuava: as duas coisas que sobraram de acoplado no projeto final (`__str__` no motor e `pool=5` fixo) eram, as duas, decisões que ninguém tinha revisitado. O desafio do instrutor é exatamente o convite para revisitar.

Esta seção é trabalho **além do curso**: o repositório publicado termina antes dela, e a solução aqui apresentada é uma proposta verificada, não um estado publicado pelo autor. O desenho dos módulos — quatro arquivos, duas interfaces, `GameSpec` injetável — é decisão desta reconstrução; o que a aula prescreve é apenas a *intenção* de desacoplar.

## 24. A hierarquia de inteiros — o código publicado (aula #07)

**Errata — corrigindo esta própria documentação.** A seção 22 afirmava que o gist da aula #07 publicava *apenas* a camada de bits (`binary.py`), e não a hierarquia `Int8`→`Integer`. **Isso estava errado.** O gist `b2bacae88c3a7d2b58229fa5dd6ed4b3`, de 01/07/2020, publica `binary.py` *e* `integers.py` — com a hierarquia completa, os testes do próprio autor e `__mul__`.

A causa do erro é metodológica, e vale registrar: a URL `gist.githubusercontent.com/<user>/<id>/raw/` **sem nome de arquivo** devolve somente o *primeiro* arquivo do gist. Baixei `binary.py`, não vi `integers.py` na resposta e concluí que ele não existia. Um gist é um *conjunto* de arquivos: a listagem vem da API (`/gists/<id>`), nunca do atalho `raw`.

A consequência é direta: a versão anterior desta seção era uma *reconstrução* de um código publicado desde julho de 2020 que eu simplesmente não tinha lido. Esta versão substitui a reconstrução pelo código **verbatim** — e **mantém a comparação**, porque as divergências entre as duas versões são a parte mais útil do episódio: uma transcrição automática corrompe identificadores, e reconstruir a partir dela inventa fatos.

### 24.1 O que o gist publica

| Arquivo | Bytes | Conteúdo |
|---|---|---|
| `binary.py` | 4.418 | `Bits`, `Byte`, `Word`, `Tribyte`, `DoubleWord` + `fulladder`/`adder`/`multiplier` + 7 testes |
| `integers.py` | 3.058 | a hierarquia `Integer`→`Int8…Int32`, o `factory`, o `register`, a função `Int()` + 6 testes |
| `pytest.ini` | 29 | configuração |

Sete arquivos assim distribuídos — e note o detalhe que derruba a minha conclusão anterior: o pacote de bits que eu baixei tinha 3.506 bytes e o publicado tem **4.418**. Nem o arquivo que eu *achei* que havia baixado estava completo: os testes inline do autor (7 funções) vinham embutidos, e eu os perdi.

### 24.2 `integers.py`, na íntegra

```
from abc import ABC

import pytest

from binary import Byte, adder, multiplier, Word, Tribyte, DoubleWord

class Integer(ABC):
    STORAGE = bytes
    types = {}

    def __init__(self, n):
        self.value = self.STORAGE(n)

    def __add__(self, other):
        return self.factory(adder(self.value, other.value))

    def __eq__(self, other):
        return self.value == other.value

    def __mul__(self, other):
        return self.factory(multiplier(self.value, other.value))

    def __repr__(self):
        return f'{self.__class__.__name__}({self.value!r})'

    @classmethod
    def factory(cls, n):
        for upper_bound, klass in cls.types.items():
            if n < upper_bound:
                break

        return klass(n)

    @classmethod
    def register(cls, upper_bound, klass):
        cls.types[upper_bound] = klass

def Int(n):
    return Integer.factory(n)

class Int8(Integer):
    STORAGE = Byte

class Int16(Integer):
    STORAGE = Word

class Int24(Integer):
    STORAGE = Tribyte

class Int32(Integer):
    STORAGE = DoubleWord

Integer.register(256, Int8)
Integer.register(65536, Int16)
Integer.register(16_777_216, Int24)
Integer.register(4_294_967_296, Int32)
```

### 24.3 A hierarquia reconstruída × a hierarquia real

| Aspecto | Minha reconstrução | Código publicado | Veredito |
|---|---|---|---|
| Armazenamento | `storage()` com `@abstractmethod` | `STORAGE = bytes`, atributo de classe sobrescrito por cada subclasse | divergiu |
| Método que escolhe o tipo | `Factory` | `factory` | divergiu |
| Função de entrada | `int(n)` | `Int(n)` | divergiu |
| `__eq__` | compara `.to_number()` | compara os objetos de armazenamento | divergiu |
| `__hash__` | presente | ausente | inventei |
| Nome do parâmetro | `up_bound` | `upper_bound` | cosmético |
| Registro é um `dict` simples | sim | sim | acertou |
| `register(limite, classe)` com dois parâmetros | sim | sim | acertou |
| A retração de tipo existe | demonstrada | confirmada por `test_scale_down` | acertou |
| O `dict` torna a ordem significativa | demonstrada | é o defeito que a aula #08 corrige | acertou |

Saldo: das três "correções" que a transcrição me inspirou, **duas estavam certas** (o `dict` e o `register` de dois parâmetros) e **uma estava errada** — eu "corrigi" `Int(n)` para `int(n)` para casar com o que a fala parecia dizer, e o código publicado usa `Int(n)`. Também inventei um `@abstractmethod` e um `__hash__`. Nada disso é grave no código do exercício; é grave na documentação, que afirmava ser fiel.

### 24.4 A ponte #07→#08 é literalmente um diff

A seção 22 tratava como hipótese o fato de a aula #08 vir "consertar" o registro da #07. Não é hipótese: os dois gists foram publicados com **1h26 de diferença** na madrugada de 01/07/2020, e a mudança está no arquivo. A aula #08 troca o `dict` por um `IntervalMap` — que ordena os limites na inserção — e com isso pode substituir a busca linear com `break` por uma consulta direta. O "funciona por acaso" ganha, aqui, o seu diff.

```
--- integers.py  gist #07  (2020-07-01 06:22)
+++ integers.py  gist #08  (2020-07-01 07:48)
@@ -3,4 +3,5 @@
 import pytest

+from adt import IntervalMap
 from binary import Byte, adder, multiplier, Word, Tribyte, DoubleWord

@@ -8,5 +9,5 @@
 class Integer(ABC):
     STORAGE = bytes
-    types = {}
+    types = IntervalMap()

     def __init__(self, n):
@@ -27,8 +28,5 @@
     @classmethod
     def factory(cls, n):
-        for upper_bound, klass in cls.types.items():
-            if n < upper_bound:
-                break
-
+        klass = cls.types.get(n)
         return klass(n)

```

### 24.5 Execução: três gists, 31 testes

| Aula | Gist | Arquivos | Comando | Resultado |
|---|---|---|---|---|
| #06 | `5bb2468` | geometry.py, pytest.ini | `pytest -q` | 2 passed in 0.01s |
| #07 | `b2bacae` | binary.py, integers.py, pytest.ini | `pytest -q` | 14 passed in 0.07s |
| #08 | `cb033ca` | adt.py, binary.py, integers.py, pytest.ini | `pytest -q` | 15 passed in 0.08s |

Os testes não são meus: **são do autor**, escritos dentro dos próprios arquivos publicados. É a diferença entre testemunho e prova — antes eu tinha 11 testes que escrevi contra um código truncado; agora são 31 que o instrutor publicou com o código.

### 24.6 O comportamento, agora sobre o código real

```
Int8(255) + Int8(255)    -> Int16(510)          # expandiu
Int8(255) + Int8(1)      -> Int16(256)          # expandiu
Int16(1) + Int16(1)      -> Int8(2)             # RETRAIU
Int16(254) + Int16(1)    -> Int8(255)           # retraiu
Int(4_000_000_000)       -> Int32(4000000000)   # despacho pelo factory
Int(8)                   -> Int8(8)             # o menor tipo possível
```

E a retração não é interpretação minha: o autor a testa explicitamente.

```
def test_int8():
    assert isinstance(Int8(0), Int8)
    assert isinstance(Int8(255), Int8)
    with pytest.raises(ValueError):
        Int8(256)

    assert Int8(0) + Int8(0) == Int8(0)
    assert Int8(1) + Int8(1) == Int8(2)
    assert Int8(254) + Int8(1) == Int8(255)

    assert Int8(127) * Int8(2) == Int8(254)

def test_int16():
    assert isinstance(Int16(0), Int16)
    assert isinstance(Int16(65535), Int16)
    with pytest.raises(ValueError):
        Int16(65536)

    assert Int16(0) + Int16(0) == Int16(0)
    assert Int16(255) + Int16(1) == Int16(256)

    assert Int16(256) * Int16(2) == Int16(512)

def test_int24():
    assert isinstance(Int24(0), Int24)
    assert isinstance(Int24(16_777_215), Int24)
    with pytest.raises(ValueError):
        Int24(16_777_216)

    assert Int24(0) + Int24(0) == Int24(0)
    assert Int24(65535) + Int24(1) == Int24(65536)

    assert Int24(65536) * Int24(2) == Int24(131_072)

def test_int32():
    assert isinstance(Int32(0), Int32)
    assert isinstance(Int32(4_294_967_295), Int32)
    with pytest.raises(ValueError):
        Int32(4_294_967_296)

    assert Int32(0) + Int32(0) == Int32(0)
    assert Int32(16_777_215) + Int32(1) == Int32(16_777_216)

    assert Int32(16_777_216) * Int32(2) == Int32(33_554_432)

def test_scale_up():
    assert Int8(255) + Int8(1) == Int16(256)
    assert Int8(128) * Int8(2) == Int16(256)

    assert Int16(65535) + Int16(1) == Int24(65536)
    assert Int16(32_768) * Int16(2) == Int24(65536)

    assert Int24(16_777_215) + Int24(1) == Int32(16_777_216)
    assert Int24(8_388_608) * Int24(2) == Int32(16_777_216)

def test_scale_down():
    assert isinstance(Int8(254) + Int8(1), Int8)

    assert isinstance(Int16(254) + Int16(1), Int8)

    assert isinstance(Int24(65534) + Int24(1), Int16)

    assert isinstance(Int32(16_777_214) + Int32(1), Int24)
```

## 25. Inventário dos artefatos públicos — o que a série deixou no chão

Esta é a resposta empírica à terceira lacuna: não "quais aulas eu consigo documentar", mas **quais aulas deixaram código no mundo**. Método: enumeração completa, via API do GitHub, dos **64 gists** (duas páginas) e dos **61 repositórios** do autor, filtrados pela janela temporal da série (junho a novembro de 2020) e pela correspondência temática; cada candidato verificado por download e execução.

| Aulas | Artefato público | Data | Verificação |
|---|---|---|---|
| #01 – #05 | nenhum | — | sem código publicado |
| #06 | gist `5bb2468` — geometry.py | 30/06/2020 | 2 testes ✓ |
| #07 | gist `b2bacae` — binary.py, integers.py | 01/07/2020 | 14 testes ✓ |
| #08 | gist `cb033ca` — adt.py, binary.py, integers.py | 01/07/2020 | 15 testes ✓ |
| #09 – #17 | nenhum | — | sem código publicado |
| #18 – #23 | repo `monopoly`, commit único `bffb0c2` | 06/11/2020 | 40 testes ✓ |

**O inventário termina aqui.** Entre 30/06/2020 e 08/12/2020 o autor publicou exatamente três gists — todos nos dias 30/06 e 01/07, correspondendo às aulas #06, #07 e #08 — e, meses depois, um único repositório com um único commit de importação. Não há gist, repositório, pasta ou anexo público para as outras quatorze aulas.

Duas pistas foram seguidas e ambas morreram, e por isso ficam registradas em vez de omitidas. Primeiro: os dois documentos Google citados nos vídeos — `1kyz61B…` e `1WIuVUy…` — **foram deletados pelo autor**; o Drive responde "the file you have requested has been deleted". Segundo: o rastro dos gists é real, mas cobre só a primeira metade do arco procedural — a série publicava código *enquanto* ensinava mecânica de classes e operadores, e deixou de publicar quando passou a modelar e implementar o Banco Imobiliário.

A leitura honesta é esta: **14 das 23 aulas existem apenas como transcrição**. Sobre elas eu sei o que foi *dito*, não o que foi *escrito*, e nenhuma quantidade de busca muda isso. É exatamente por isso que a seção 24 precisou ser reescrita: quando o artefato não existe, a única saída é reconstruir — e reconstruir, três vezes em quatro tentativas, produziu uma divergência.

Documentação elaborada a partir das transcrições automáticas das 23 aulas da playlist “Orientação a Objetos na Prática”, de Henrique Bastos (HB Network), complementada pela leitura integral do repositório público `monopoly` e pela execução real dos testes e da simulação no sandbox. Os trechos de código são reproduções fiéis dos arquivos do repositório, com arquivo e linha. As citações reproduzem falas do instrutor capturadas nas transcrições: por serem legendas geradas automaticamente, carregam erros de reconhecimento de fala, preservados de propósito e anotados quando evidentes. Números de testes, tempos de execução e percentuais de vitória são saída de terminal desta sessão; o simulador é estocástico, e as variações entre execuções estão reportadas na seção 20.4. A aula #23 constrói um arquivo (`competitors.py`) que não está no repositório publicado; a seção 21 o reconstrói a partir do que a aula especifica e o verifica por execução — e o texto deixa explicitamente marcado, na seção 21.7, o que é reconstrução fiel e o que é inferência de engenharia. A seção 22 executa os três gists publicados pelo curso e registra o que eles *não* contêm; a seção 23 resolve o desafio final da aula #23 e é trabalho além do curso, marcado como proposta verificada; a seção 24 reconstrói a hierarquia de inteiros da aula #07, não publicada em gist, e marca em 24.5 o que é fiel e o que é inferência. Conteúdo de caráter educativo.
