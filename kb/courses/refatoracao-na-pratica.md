<!-- written by the henrique-ingest distiller on 2026-10-08 from sources/transcripts/refatoracao-na-pratica/; see kb/courses/README.md for provenance and license -->

HB Network · Documentação de curso

# Refatoração na Prática

As 34 aulas, da definição de refatoração ao plano de 84 tarefas para a matriz, lidas aula a aula a partir das legendas automáticas, com o código do donuts e do wordcount reconstruído a partir do que ele narra.

Instrutor: **Henrique Bastos** · Canal [HB Network](https://www.youtube.com/@hbnetworkoficial) · Playlist: [Refatoração na Prática](https://www.youtube.com/playlist?list=PLeKXYyZCJHxfTqEvicb9dqcbj-eCOFhhj) · Repositório: nenhum publicado para esta série (o fork da matriz é citado na aula #33, mas a URL não consta da transcrição)

Documento elaborado a partir das transcrições automáticas de 33 das 34 aulas (legendas em português, pt-orig, capturadas em 2026-10-08; a aula #34 não tem legenda, título nem duração). O curso não publicou código: tudo que ele digita acontece no PyCharm ao vivo, e os trechos desta documentação são reconstruções a partir do que ele diz, marcadas como tal. Nas aulas #28 a #31 ele não altera o código, apenas dita comentários TODO, e esses TODOs estão transcritos como ele os dita.

## 1. Visão geral do curso

Refatoração na Prática é uma série de **34 aulas** (33 com transcrição) que somam **14.259 segundos, 3 horas, 57 minutos e 39 segundos**. A proposta declarada na abertura não é definir refatoração, mas demonstrar casos e cenários onde se analisam oportunidades de melhoria e se decide o que fazer, quando, como e o que não fazer (aula #01, 0:00:16 a 0:00:33). O curso não quer que o aluno decore nada: quer estimular a sensibilidade para os detalhes que ficam implícitos no código (aula #01, 0:01:14), e repete essa meta ao abrir o bloco de componentes (aula #18, 0:00:13).

O desenho é em cinco blocos. As aulas #01 a #05 são conceituais: a definição de refatoração como melhoria da estrutura interna sem mudar o comportamento com o mundo exterior (aula #02, 0:00:13), a decisão econômica de quando refatorar (aula #03, 0:01:12) e o método de prática mais reflexão (aula #04, 0:02:06). As aulas #06 a #16 trabalham um único exercício de uma linha, o donuts, para mostrar dez oportunidades de refatoração num problema minúsculo (aula #05, 0:01:13), terminando com a extração de um conceito em classe (aula #16). A aula #17 é a teoria dos componentes, de McIlroy a Rube Goldberg. As aulas #18 a #25 refatoram um wordcount legado, cercado por golden files e pytest, até virar um componente do sistema operacional (aula #24, 0:18:07). As aulas #26 a #33 mudam de modo: ele analisa o código de uma matriz de pixels feito por um iniciante e, sem mexer em nada, dita 84 TODOs que viram o plano de refatoração do aluno (aula #32, 0:00:57).

| Dimensão | Valor | Observação |
|---|---|---|
| Aulas | 34 | Playlist completa, numerada de #01 a #34; a #34 não tem título, duração nem legenda no `playlist.json`. |
| Duração total | 14.259 s (3h 57min 39s) | Soma das durações das 33 aulas com metadados (`playlist.json`); a #34 não entra. |
| Aula mais curta / mais longa | 35 s (#33) / 1.295 s (#30) | As cinco aulas de mais de 800 s (#03, #17, #24, #30, #31) são 49% do curso. |
| Datas de publicação | não coletadas | O `playlist.json` desta coleta traz apenas id, título e duração. |
| Visualizações | não coletadas | Idem. |
| Transcrições | 33 de 34 disponíveis | Legenda automática em português (pt-orig); não há legenda humana; a #34 (`4ZOhCPTWrS0`) não tem legenda. |
| Títulos | 30 em português, 4 traduzidos | Os títulos de #02, #03, #06 e #07 chegaram traduzidos automaticamente para o inglês no `playlist.json`; a seção 4 traz a retradução a partir do que a aula diz, marcada como tal. |
| Código do curso | nenhum publicado | Donuts (#06 a #16) e wordcount (#19 a #24) são digitados no PyCharm; a matriz (#27 a #31) é código de um aluno, e o fork com os TODOs (aula #33, 0:00:06) não tem URL na transcrição. |
| Blocos práticos | #06 a #16, #20 a #24, #27 a #31 | Donuts, wordcount e matriz. |

Nota de método: este documento tem uma única fonte, a transcrição automática. Cada afirmação traz aula e timestamp. As citações são paráfrases de legenda, sem aspas, não verificadas contra o vídeo, e os erros de reconhecimento de fala ficam anotados entre colchetes quando precisam aparecer. A legenda grafa refatoração quase sempre como refaturação ou fatoração, PyCharm como pai Charme, pytest como Pie teste ou pai teste, e cada bloco da seção 5 registra as formas ouvidas dos termos daquela aula. Os trechos de código da seção 5 são reconstruções do que ele narra, nunca cópias de um arquivo publicado; a seção 13 resume os limites dessas reconstruções e a seção 14 registra que nada foi executado.

## 2. Filosofia e método de ensino

### 2.1 Não decorar; desenvolver sensibilidade

O objetivo do programa não é fazer o aluno decorar absolutamente nada, e sim estimular a sensibilidade para os detalhes implícitos no código, para reconhecer oportunidades, priorizar, saber até onde ir e como se comportar durante o processo (aula #01, 0:01:14 a 0:01:41). Os três obstáculos de aprendizagem que ele lista são a abordagem teórica, a busca por regras e a explosão combinatória de uns 30 casos de refatoração, uns 30 padrões e uns 30 cheiros que raramente aparecem sozinhos (aula #02, 0:05:58 a 0:08:18); o que decide é o repertório da prática e da vivência (aula #02, 0:09:07). O bloco de componentes reabre na mesma nota: não decorar técnicas, sensibilizar para um processo de observação e organização (aula #18, 0:00:13).

### 2.2 Conceituar antes, praticar depois, e nunca pressupor

Ele começa conceituando para haver acordos sobre termos e visões, e só então explora casos (aula #01, 0:00:49 a 0:01:06). Os materiais sobre refatoração partem de um degrau acima e pressupõem sensibilidade para organização de código; ele não quer pressupor absolutamente nada e espera se surpreender com sutilezas não catalogadas (aula #04, 0:00:00 a 0:00:43). O processo de decisão que busca independe de quantos anos a pessoa programa, embora o repertório varie (aula #04, 0:00:55).

### 2.3 Programar em terceira pessoa

A estratégia para dominar refatoração é prática mais reflexão sobre a prática; o aluno deve registrar a própria reflexão para comparar e complementar (aula #04, 0:01:52 a 0:02:08). A imagem é programar em terceira pessoa: escrever o código refletindo sobre o próprio processo de escrever o código, e por isso ele narra a resolução exatamente como trabalha no dia a dia (aula #04, 0:02:15 a 0:02:44). No bloco da matriz, a mesma narração vira uma dinâmica de code review ditada em TODOs (aula #32, 0:00:45).

### 2.4 Implemente antes de ver a solução dele

Em todos os exercícios ele pede que o aluno pause e implemente antes de ver as análises: no donuts (aula #06, 0:00:00), no wordcount, com pedido do link do GitHub nos comentários (aula #19, 0:01:23 e 0:03:48), e no fecho do wordcount, com um vídeo no Loom de 5 a 10 minutos analisando um código próprio (aula #25, 0:02:02). Ele coleciona as respostas dos alunos e não as trata como equívocos: o que importa é o que a pessoa estava pensando e tentando alcançar (aula #05, 0:00:40 e 0:01:31).

### 2.5 Pequenos passos com os testes rodando

Toda mudança, por menor que seja, é seguida de uma execução dos testes: ele faz só uma pequena mudança e roda os testes, e avisa que vai fazer isso o tempo inteiro (aula #06, 0:05:44); até uma mudança só de estilo exige rodar (aula #08, 0:01:28). Não tente resolver tudo ao mesmo tempo; passo a passo, uma coisa de cada vez (aula #10, 0:02:18; aula #25, 0:01:50). Quando não há testes, o primeiro passo é cercar o programa por fora com golden files e `diff`, depois com pytest (aula #20, 0:05:08 a 0:09:52).

### 2.6 Analisar sem mexer, e decidir em equipe

O bloco da matriz é inteiro de análise: ele anota TODOs em vez de alterar o código, e a análise, sem mexer, revela um desenho possível (aula #30, 0:21:12). Os 84 TODOs são sugestões, não obrigações, porque a propriedade do código é da equipe que cuida dele, não de quem escreve; a sugestão provoca diálogo sobre o porquê, e as decisões são tomadas em equipe mesmo quando ele é o líder (aula #32, 0:01:20 a 0:02:09). A decisão de até onde ir considera a experiência da equipe, culturas diferentes e o domínio local (aula #12, 0:02:47 a 0:03:30).

## 3. Pilares conceituais

### 3.1 Refatorar é mudar a estrutura, não o comportamento

Refatorar é melhorar a estrutura interna do código sem mudar o comportamento com o mundo exterior; nem toda mudança com intenção de melhorar é refatoração (aula #02, 0:00:13 a 0:00:41), e reescrever tudo não é refatorar (aula #02, 0:02:02). Corrigir um bug durante a refatoração viola esse princípio; achou bug, para, volta, conserta e estabiliza (aula #03, 0:03:01 a 0:03:24). Daí os chapéus: implementar funcionalidade, refatorar e otimizar são momentos distintos (aula #03, 0:04:52). O pressuposto é código estável: nunca se refatora código instável (aula #02, 0:05:42; aula #06, 0:01:02).

### 3.2 A decisão é econômica

A justificativa comum, qualidade, ninguém define; a decisão de refatorar precisa ser econômica, não estética, vinculada ao desempenho da equipe, porque a única certeza sobre software é que ele vai mudar (aula #02, 0:02:13 a 0:03:51). Refatore quando precisar ajustar o código para acolher uma mudança; priorize o que muda com frequência; não refatore só por estética em contexto profissional (aula #03, 0:01:12 a 0:02:57). O custo do atraso é exponencial, uma tsunami sem tempo de reagir (aula #03, 0:09:02 a 0:10:14), e a relação econômica com a sustentabilidade do projeto reabre a aula de componentes (aula #17, 0:00:11).

### 3.3 O código expressa o domínio, linearmente

A primeira coisa a observar é a relação do código com o domínio do problema (aula #06, 0:02:37); nomes vêm do domínio, não da implementação, e não se economiza nos nomes (aula #10, 0:00:40 e 0:01:59). O código deve ser o mais linear, direto e sequencial possível, entrando por uma porta e saindo por outra (aula #07, 0:02:00 e 0:03:45), organizado em entrada, processamento e saída, uma divisão que é fractal e vale dentro da função (aula #07, 0:04:39; aula #11, 0:01:33). Explícito é melhor que implícito: todo `if` tem um `else`, e dois caminhos válidos pedem os dois ramos escritos (aula #12, 0:00:12 e 0:01:45).

### 3.4 Componentes, não partes

Componentes podem ser substituídos e padronizados, e trabalham cooperativamente compondo coisas mais complexas; a máquina de Rube Goldberg tem partes, não componentes (aula #17, 0:06:35 e 0:08:12). A natureza do que é processado define o que encaixa com o quê, e transformar número em string já mexe em naturezas diferentes (aula #17, 0:09:27 e 0:10:56). Componentes têm natureza fractal: pequenos se agrupam em maiores (aula #18, 0:02:09), do comando da linguagem ao programa inteiro como componente do sistema operacional (aula #24, 0:18:07; aula #25, 0:01:32). Não é regra: componentes emergem do contexto (aula #17, 0:14:04).

### 3.5 Orientação a objetos é tornar evidente o conceito

O pecado capital de quem estuda orientação a objetos é olhar classe, atributo, público e privado; a essência é a interação entre objetos, a troca de mensagens (aula #16, 0:01:02). Há conceitos manifestos mas não expressos, óbvios mas não evidentes, e o trabalho é evidenciá-los (aula #16, 0:00:42): a quantidade do donuts vira `Quantity` (aula #16, 0:02:02), as conversões de índice da matriz pedem um objeto Coordenada (aula #30, 0:06:42), e sempre que há repetição ou muitos `if`s a pergunta é se aquilo não é um conceito (aula #16, 0:11:44). Algoritmos usam a interface da estrutura; não se entulha a classe com eles (aula #30, 0:18:46; aula #31, 0:12:54).

### 3.6 Planejar é escolher o que não fazer

Não dá para fazer tudo; o desafio é descobrir a coisa certa a fazer agora, e do conflito entre o ideal e o possível nascem estratégias intermediárias boas o bastante (aula #26, 0:00:26 a 0:02:08). Listar é muito mais rápido que fazer; primeiro listar, depois escolher o que executar e, principalmente, o que não fazer, sem cair em discussões do sexo dos anjos (aula #32, 0:03:39 a 0:04:28). Refatoração elimina ruído, e a área de trabalho se arruma antes do problema, não o terreno inteiro (aula #03, 0:12:52; aula #21, 0:11:38).

## 4. As aulas em uma tabela

Os títulos de #02, #03, #06 e #07 chegaram traduzidos para o inglês no `playlist.json`; a retradução entre parênteses é deste documento, a partir do que a aula diz.

| # | Título | Duração | Foco em uma linha |
|---|---|---|---|
| 01 | Refatoração na Prática #01: Seja bem-vindo! | 106 s | Não definir, demonstrar; o que fazer, quando, como e o que não fazer; nada para decorar. |
| 02 | Refactoring in Practice #02: Why Refactor? (Por que refatorar?) | 564 s | Definição; reescrever não é refatorar; decisão econômica; Fowler e o antídoto contra o envelhecimento; três obstáculos de aprendizagem. |
| 03 | Refactoring in Practice #03: When to Refactor? (Quando refatorar?) | 806 s | Saliência; quando e quando não; bug para tudo; chapéus; montinho de areia; curva de custo; ruído e ressaca cognitiva. |
| 04 | Refatoração na Prática #04: O processo | 166 s | Não pressupor nada; prática mais reflexão; programar em terceira pessoa. |
| 05 | Refatoração na Prática #05: Simples, mas não simplório | 116 s | Dez oportunidades de refatoração num problema de uma linha. |
| 06 | Refactoring in Practice #06: Respect the Problem Domain (Respeite o domínio do problema) | 388 s | Enunciado do donuts; pytest; o `count < 10` que inverte o enunciado; telefone sem fio. |
| 07 | Refactoring in Practice #07: Avoiding Mazes (Evitando labirintos) | 351 s | Código pulga; um único `return`; entrada, processamento e saída. |
| 08 | Refatoração na Prática #08: Siga um estilo | 102 s | Indentação, PEP 8, linters; mantenha a regra; rode os testes mesmo assim. |
| 09 | Refatoração na Prática #09: Não se repita... nem se espalhe | 341 s | Repetição de propósito; `+=` que espalha; shotgun surgery; a variável transporta. |
| 10 | Refatoração na Prática #10: Nomes modelam a realidade | 143 s | `t` é péssimo nome; `qty`; renomear pela IDE; uma coisa de cada vez. |
| 11 | Refatoração na Prática #11: Simetria de tipos | 188 s | Inteiro e string no mesmo contexto; conversão implícita por acaso; `str(count)` como transformação. |
| 12 | Refatoração na Prática #12: Explícito é melhor que implícito | 224 s | Todo `if` tem `else`; valor default é para exceção; forma e função; equipe e cultura. |
| 13 | Refatoração na Prática #13: Quando menos não é mais | 202 s | Não sobrescreva o input; funções sem efeito colateral; enxugar custa legibilidade. |
| 14 | Refatoração na Prática #14: Números mágicos | 175 s | `limite = 10`; parâmetro com valor padrão; muitos parâmetros é outro cheiro. |
| 15 | Refatoração na Prática #15: Não seja um espertalhão | 158 s | Tudo numa linha funciona e não se recomenda; pragmatismo. |
| 16 | Refatoração na Prática #16: Torne evidente o que é óbvio | 761 s | Classe `Quantity` guiada por testes; `__str__`; `@property`; objetos expressam interações. |
| 17 | Refatoração na Prática #17: O Que Não Te Contaram Sobre Componentes | 872 s | McIlroy e 1968; design versus arquitetura; Rube Goldberg, dominós, eletrônica; dimensões do componente. |
| 18 | Refatoração na Prática #18: O Desafio de Entender Componentes | 149 s | Ajuste de relevância; o fluxo de execução está implícito; componentes fractais. |
| 19 | Refatoração na Prática #19: Testando O Que Não Tem Testes | 244 s | Funcionar, direito e rápido no mesmo fluxo; enunciado do wordcount. |
| 20 | Refatoração na Prática #20: A Herança Maldita | 602 s | Código legado é entropia; executar antes de ler; golden files, `diff`, pytest com `capsys` e `monkeypatch`. |
| 21 | Refatoração na Prática #21: Explorando o Ambiente | 778 s | Comentário é sintoma; nomes locais curtos; convenção sobre configuração; fechar recursos; arrumar a área de trabalho. |
| 22 | Refatoração na Prática #22: Desfiando O Novelo de Lã | 502 s | Vazamento de responsabilidades; `with`; transformar a coleção inteira; inversão de lógica; docstring. |
| 23 | Refatoração na Prática #23: Cada Macaco No Seu Galho | 623 s | Interfaces uniformes; `items()`; funções retornam em vez de imprimir; `main` cuida da saída. |
| 24 | Refatoração na Prática #24: Componentes Em Toda Parte | 1.105 s | Extrações; estratégia injetada; dicionário de opções; `defaultdict`; stdin com `-`; early return; componente do sistema. |
| 25 | Refatoração na Prática #25: Refatoração Vista Do Alto | 188 s | Recapitulação em cinco etapas cíclicas; exercício no Loom. |
| 26 | Refatoração na Prática #26: Veja o Invisível | 222 s | Planejar; a coisa certa agora; bom o bastante; ver oportunidade, não legado. |
| 27 | Refatoração na Prática #27: Desafio da Matriz Movente | 289 s | Código de iniciante; executar os comandos do README; intervalo inclusivo; falta de uniformidade. |
| 28 | Refatoração na Prática #28: Puxando o Fio da Meada | 727 s | Começar pelo entry point; `main` conhece demais; `except` genérico; TODOs. |
| 29 | Refatoração na Prática #29: Separação de Entrada e Saída | 602 s | `read_seq` e `print_board`; funciona por coincidência; parser que devolve objeto comando; `__str__`. |
| 30 | Refatoração na Prática #30: Organização Potencializa a Composição | 1.295 s | Comandos como métodos do board; Coordenada; Região; um único algoritmo para linhas e bloco. |
| 31 | Refatoração na Prática #31: Boas Estruturas Ajudam Bons Algorítimos | 953 s | `__contains__`; comparações ricas; fill genérico sobre a interface do board; `save`. |
| 32 | Refatoração na Prática #32: A Moral da História | 282 s | 84 TODOs; code review; código coletivo; listar antes de fazer; o que não fazer. |
| 33 | Refatoração na Prática #33: Tem Mais Uma Coisa... | 35 s | Fork com as tarefas; comentar o que não concorda e por quê. |
| 34 | (sem título) | desconhecida | Sem legenda, título ou duração no `playlist.json`. |

## 5. Resumo por aula

Cada bloco segue o passe por aula do distiller: resumo, linha do tempo (até 12 entradas; quando duas entradas foram fundidas, os dois timestamps ficam na mesma linha), princípios enunciados com timestamp, código reconstruído e paráfrases da legenda sem aspas. Os termos mal ouvidos pelo reconhecedor ficam anotados entre colchetes na primeira ocorrência de cada aula.

### Aula #01: Seja bem-vindo!

Vídeo: https://www.youtube.com/watch?v=TCVpXFm80gU · 106 s

Abertura do curso. Ele explica que a proposta não é definir refatoração, mas demonstrar casos e cenários onde se analisam oportunidades de melhoria e se reflete sobre o que fazer, quando, como e o que não fazer (0:00:16 a 0:00:33). O objetivo declarado é eliminar a burocracia por trás de assuntos abstratos da computação e desenvolver a intuição do aluno (0:00:36 a 0:00:49). Ele vai começar conceituando, para haver acordos sobre termos e visões, e depois explorar casos (0:00:49 a 0:01:06). Nada deve ser decorado: a meta é estimular a sensibilidade para os detalhes implícitos no código, para reconhecer oportunidades, priorizar, saber até onde ir e como se comportar durante o processo (0:01:14 a 0:01:41).

Linha do tempo:

- [0:00:00] Boas-vindas; vai explicar como as coisas acontecem no curso.
- [0:00:16] A ideia não é só explicar o que é refatoração, mas demonstrar diversos casos e cenários.
- [0:00:30] Refletir sobre o que fazer, quando fazer, como fazer e o que não fazer.
- [0:00:36] Eliminar a burocracia dos assuntos sofisticados e abstratos; desenvolver intuição sobre o que melhorar e como e quando agir.
- [0:00:49] Começar conceituando para ter acordos sobre termos e visões.
- [0:01:01] Com o mapa desenhado, explorar casos para montar a percepção das oportunidades.
- [0:01:14] O programa não é para decorar nada; é para estimular a sensibilidade aos detalhes implícitos no código.
- [0:01:29] Priorizar o que fazer primeiro, até onde progredir numa refatoração e como se comportar durante o processo.

Princípios enunciados:

- Refatorar envolve decidir o que fazer, quando, como e também o que não fazer (0:00:30).
- A meta é intuição sobre o que melhorar e, principalmente, como e quando agir (0:00:44).
- Não decore nada; desenvolva sensibilidade para o que fica implícito no código (0:01:14).

Código: nenhum.

Paráfrases da legenda (não verificadas):

- a minha ideia desse treinamento não é apenas explicar o que é fatoração [refatoração] mas demonstrar diversos casos, diversos cenários, onde a gente vai começar a analisar as oportunidades de melhoria (0:00:16)
- você vai desenvolver a sua intuição sobre o que melhorar e principalmente como e quando agir (0:00:44)
- o objetivo desse programa não é fazer você decorar absolutamente nada, o que eu quero é estimular sua sensibilidade para você começar a perceber os detalhes que ficam implícitos no código (0:01:14)

### Aula #02: Por que refatorar?

Vídeo: https://www.youtube.com/watch?v=CGju-o7vTeo · 564 s

Título no `playlist.json`: Refactoring in Practice #02: Why Refactor? (tradução automática); retradução a partir de 0:02:13, vamos entender porque refaturar algum código.

Define refatoração como melhorar a estrutura interna do código sem mudar o comportamento com o mundo exterior, e avisa que nem toda mudança com intenção de melhorar é refatoração (0:00:13 a 0:00:41). Evoca o projeto campo minado e a tentação de reescrever tudo, que costuma ser muito mais cara e arrasta troca de tecnologia; reescrever tudo não é refatorar (0:00:48 a 0:02:10). A justificativa comum, qualidade, ninguém define; a decisão de refatorar precisa ser econômica, não estética, e vinculada a melhoria no desempenho da equipe, porque a única certeza sobre software é que ele vai mudar (0:02:13 a 0:03:51). Cita o livro de Martin Fowler e a origem no grupo do Manifesto Ágil, posiciona refatoração como um dos três componentes do antídoto contra o envelhecimento do código (cheiros de código, padrões de projeto, refatoração) e fixa o pressuposto de código estável (0:04:09 a 0:05:56). Fecha com três obstáculos de aprendizagem: abordagem teórica, busca por regras e explosão combinatória; o que decide é o repertório da prática (0:05:58 a 0:09:21).

Linha do tempo:

- [0:00:13] Definição: melhorar a estrutura interna sem mudar o comportamento com o mundo exterior.
- [0:00:31] Nem toda mudança com intenção de melhorar é refatoração; a restrição é específica.
- [0:00:48] O projeto campo minado: mexe num troço, quebra outro; comichão de reescrever tudo.
- [0:01:37] Reescrever tudo costuma ser muito mais caro; as pessoas aproveitam para trocar tecnologia, framework, linguagem.
- [0:02:02] Reescrever tudo não é refatorar.
- [0:02:13] Qualidade ninguém define; cilada da estética; a decisão precisa ser econômica.
- [0:03:37] Refatoração torna o código mais fácil de mudar; a única certeza é que o software vai mudar.
- [0:04:09] Livro de Martin Fowler [legenda: marketing falller]; discussões do pessoal do Manifesto Ágil.
- [0:04:47] Três componentes do antídoto contra o envelhecimento: cheiros de código, padrões de projeto, refatoração.
- [0:05:42] Pressuposto: não refatorar sistema instável.
- [0:05:58] Três obstáculos de aprendizagem: abordagem teórica (0:06:16), busca por regras (0:07:12), explosão combinatória (0:08:03).
- [0:09:07] Não adianta decorar: o repertório da prática e da vivência enriquece a decisão.

Princípios enunciados:

- Refatorar é melhorar a estrutura interna do código sem mudar o comportamento com o mundo exterior (0:00:13).
- Nem toda mudança com intenção de melhorar é refatoração (0:00:31).
- Reescrever tudo não é refatorar (0:02:02).
- A decisão de refatorar precisa ser econômica, não estética (0:02:48).
- Decisões de refatoração se vinculam a melhorias no desempenho da equipe, não só no projeto (0:03:27).
- A única certeza sobre o software é que ele vai mudar; refatoração existe para tornar a mudança mais fácil (0:03:43).
- Refatoração é um dos três componentes do antídoto contra o envelhecimento do código, com cheiros de código e padrões de projeto (0:04:47).
- Não se refatora sistema instável; refatoração acontece em código estável (0:05:42).
- Não se aprende refatoração só lendo; as técnicas foram mapeadas da prática (0:06:58).
- Boas práticas não são regras; priorize o terreno da realidade sobre o mapa do ideal (0:07:12).
- Explosão combinatória: não dá para mapear tudo; o repertório da prática é o que decide (0:08:03).

Código: nenhum.

Paráfrases da legenda (não verificadas):

- refaturar [refatorar] é melhorar a estrutura interna do seu código sem mudar o comportamento com o mundo exterior (0:00:13)
- reescrever tudo não é refaturar [refatorar] (0:02:02)
- não me interessa o sistema que você fez, a única certeza que eu tenho é que ele vai mudar (0:03:45)
- na prática a teoria é outra e a gente sempre precisa priorizar o terreno da realidade através do mapa do ideal (0:08:01)

### Aula #03: Quando refatorar?

Vídeo: https://www.youtube.com/watch?v=DkLSqfIutoU · 806 s

Título no `playlist.json`: Refactoring in Practice #03: When to Refactor? (tradução automática); retradução a partir de 0:01:10, então quando refaturar.

Abre com cognição: pensar fora da caixa é reconfigurar a saliência, mudar o foco para os limites do contexto, e é isso que a prática com cenários concretos permite (0:00:00 a 0:00:46). Ataca os fazeres: refatore quando precisar ajustar o código para acolher uma mudança, com decisão econômica; priorize o código que muda com frequência; não refatore só por estética em contexto profissional (0:01:12 a 0:02:57). Como fazer: nunca refatore código instável; achou bug, para, volta, conserta e estabiliza, porque corrigir bug na refatoração viola o princípio de não mudar comportamento; metáfora da cirurgia plástica agendada versus a de emergência (0:03:01 a 0:04:40). Chapéus: implementar funcionalidade, refatorar e otimizar são momentos distintos (0:04:52 a 0:05:44). O montinho de areia ilustra o ciclo de expansão, acomodação e consolidação, ligado à hipótese da resistência do design de Fowler e a uma inversão em gráfico de custo, onde o atraso vira custo exponencial (0:05:56 a 0:10:19). Fecha com as condições mentais de quem programa: mito de saber tudo de cabeça, fluxo versus estresse, ressaca cognitiva e ruído; refatoração elimina ruído (0:10:19 a 0:13:23).

Linha do tempo:

- [0:00:00] O sistema cognitivo busca o prioritário; pensar fora da caixa é reconfigurar a saliência.
- [0:00:47] Os fazeres: quando, quando não, como, o que e o que não fazer; tirar a pressão de ter respostas.
- [0:01:12] Quando: sempre que precisar ajustar o código para acolher uma mudança; decisão econômica.
- [0:01:40] Priorize o código que muda com frequência; código que muda uma vez por ano não merece.
- [0:02:37] Quando não: não refatorar só pela estética, em contexto profissional.
- [0:03:01] Como: nunca refatore código instável; achou bug, para tudo, conserta, estabiliza; [0:03:51] cirurgia plástica agendada versus cirurgia de emergência, cicatrizes diferentes.
- [0:04:52] Chapéus: implementar funcionalidade, refatorar (nada muda, só o arranjo), otimizar (números da execução).
- [0:05:56] Montinho de areia na praia: ciclo de expansão, acomodação e consolidação.
- [0:07:10] Hipótese da resistência do design, de Fowler [legenda: marketing Fallen]: gráfico de funcionalidades acumuladas por tempo, curva verde e vermelha.
- [0:09:02] Inversão: gráfico de custo; o atraso gera custo exponencial, tsunami sem tempo de reagir.
- [0:10:19] Condições intelectuais, mentais e físicas; mito do programador que sabe tudo de cabeça; programar o ambiente e o comportamento; [0:11:21] fluxo versus estresse; sistema límbico; ressaca cognitiva.
- [0:12:39] Código, ambiente, casa e computador bagunçados geram ruído; refatoração elimina ruído; arrumar a casa antes de chutar o brinquedo.

Princípios enunciados:

- Pensar fora da caixa é reconfigurar a saliência, não genialidade (0:00:16).
- Refatore sempre que precisar ajustar o código para acolher uma mudança; a decisão é econômica (0:01:12).
- Não dá para refatorar tudo; priorize o código que muda com frequência (0:01:40).
- Não refatore apenas pela estética, em contexto profissional (0:02:37).
- Nunca refatore código instável; ao achar um bug, pare, volte atrás, conserte e estabilize primeiro (0:03:01).
- Corrigir bug junto com a refatoração viola o princípio de não mudar o comportamento (0:03:24).
- Use chapéus diferentes: implementar, refatorar e otimizar são momentos distintos de programação (0:04:52).
- O crescimento do software é um ciclo de expansão, acomodação e consolidação (0:06:29).
- Prudência desde o início do projeto; quando a curva de custo começa a crescer, o controle já foi perdido (0:10:14).
- O brilhantismo de quem programa é programar o ambiente, o comportamento e a abordagem, não só o código (0:10:54).
- Refatoração elimina ruído; capacidade cognitiva e foco são limitados (0:12:52).

Código: nenhum. Mostra dois gráficos (resistência do design e custo invertido).

Paráfrases da legenda (não verificadas):

- pensar fora da caixa não é uma questão de genialidade, é uma questão de capacidade de reconfigurar sua saliência (0:00:16)
- nunca refatore um código instável, o código precisa estar funcionando (0:03:01)
- quando você tá corrigindo um bug você tem que corrigir ele, é impedir o navio de afundar; quando você está refaturando [refatorando] você tá criando novas relações para tornar as próximas mudanças mais fáceis (0:04:27)
- um código bagunçado, um ambiente bagunçado, uma casa, um quarto bagunçado, um computador bagunçado, tudo isso gera ruído e esse ruído vai te distrair, vai detonar sua produtividade (0:12:41)

### Aula #04: O processo

Vídeo: https://www.youtube.com/watch?v=ZU8d31zzlJ0 · 166 s

Os materiais sobre refatoração partem de um degrau acima e pressupõem sensibilidade para organização de código; ele não quer pressupor nada e espera se surpreender com sutilezas não catalogadas (0:00:00 a 0:00:43). O que busca é a essência do processo de tomada de decisão ao olhar um código, processo que independe de quanto tempo a pessoa programa, embora o repertório varie (0:00:45 a 0:01:25). O curso traz exercícios, cenários e problemas; o aluno deve praticar, refletir e registrar a reflexão para comparar e complementar (0:01:25 a 0:02:08). A imagem é programar em terceira pessoa: escrever código refletindo sobre o próprio processo; por isso ele vai narrar a resolução como faz no dia a dia (0:02:15 a 0:02:44).

Linha do tempo:

- [0:00:00] Materiais sobre refatoração pressupõem conhecimento e sensibilidade prévios.
- [0:00:29] Ele não quer pressupor nada; quer descobrir sutilezas que não estão catalogadas.
- [0:00:45] Busca a essência do processo de tomada de decisão ao avaliar um código.
- [0:00:55] O processo independe de anos de experiência; o repertório varia.
- [0:01:25] Série de exercícios, cenários e problemas para analisar soluções e abordagens.
- [0:01:52] Reflita e registre a sua reflexão para comparar e complementar.
- [0:02:15] Programar em terceira pessoa.
- [0:02:31] Vai narrar bastante a resolução e a reflexão, exatamente como trabalha.

Princípios enunciados:

- Não pressuponha nada ao ensinar ou aprender refatoração (0:00:29).
- Registre a sua reflexão sobre o que vê no código (0:01:52).
- A estratégia para dominar refatoração é prática mais reflexão sobre a prática (0:02:06).
- Programe em terceira pessoa: escreva código refletindo sobre o próprio processo de decisão (0:02:15).

Código: nenhum.

Paráfrases da legenda (não verificadas):

- eu não quero pressupor absolutamente nada (0:00:29)
- essa é a estratégia para você dominar refaturação [refatoração], é através da prática e uma reflexão da prática que vai mudar a forma de você fazer as coisas (0:02:06)
- é como se você tivesse meio que programando em terceira pessoa, onde você tá escrevendo o código e refletindo sobre o seu processo de escrever o código (0:02:15)

### Aula #05: Simples, mas não simplório

Vídeo: https://www.youtube.com/watch?v=IL5hd5Z2-0w · 116 s

Refatoração costuma evocar sistemas cabeludos, macarronada; ele pergunta se há oportunidade em problemas pequenos (0:00:00 a 0:00:12). Apresenta o exercício que mais usa em treinamentos, parte de uma coleção de exercícios do Google, e conta que coleciona as respostas dos alunos (0:00:12 a 0:00:45). Pede um chute: quantas oportunidades de refatoração existem num problema que se resolve em uma linha; a resposta dele é dez (0:00:45 a 0:01:18). O interesse é observar o que cada um pensa e qual abordagem usa, sem tratar como equívocos (0:01:18 a 0:01:52).

Linha do tempo:

- [0:00:00] Refatoração costuma evocar sistemas complexos; há oportunidade em problemas pequenos?
- [0:00:12] O exercício que ele mais usa em treinamentos, da coleção de exercícios do Google.
- [0:00:40] Ele coleciona as respostas dos alunos.
- [0:00:45] Pergunta: quantas oportunidades num problema de uma linha; anote um número.
- [0:01:13] Resposta: dez oportunidades.
- [0:01:18] Observar o que cada um pensa, o processo de decisão e o que tenta alcançar; não são equívocos.

Princípios enunciados:

- Até um problema de uma linha tem dez oportunidades de refatoração (0:01:13).
- O que importa não é o equívoco, é o que a pessoa estava pensando e tentando alcançar (0:01:31).

Código: nenhum nesta aula (o enunciado aparece em #06).

Paráfrases da legenda (não verificadas):

- quantas oportunidades de fatoração [refatoração] você acha que existem num problema que você pode resolver em apenas uma linha (0:00:45)
- eu vou te dizer quantos são: 10 oportunidades (0:01:13)
- o que será que passa na cabeça da pessoa durante o processo de programação (0:01:39)

### Aula #06: Respeite o domínio do problema

Vídeo: https://www.youtube.com/watch?v=BA_56L6cFG4 · 388 s

Título no `playlist.json`: Refactoring in Practice #06: Respect the Problem Domain (tradução automática); retradução a partir de 0:05:54, observe o domínio do seu problema.

Pede que o aluno pause e implemente antes de ver as análises (0:00:00 a 0:00:16). Enunciado do donuts: dado um contador inteiro, retornar Number of donuts: e a quantidade; se o contador for 10 ou mais, usar a palavra many [legenda: meme] (0:00:19 a 0:00:53). Como refatoração exige código estável, recruta a implementação mais comum entre alunos, com uma função de teste abaixo, rodada com pytest pelo PyCharm [legendas: Pie teste, pai Charme]; roda, falha, cola o código, roda, passa (0:00:59 a 0:02:14). A primeira coisa que ele observa é a relação do código com o domínio do problema: o enunciado diz 10 ou mais, mas o código testa `count < 10`; a inversão pode não ser problema, mas é sempre um alerta, porque requisitos displicentes geram telefone sem fio (0:02:35 a 0:04:50). Ajusta para maior ou igual a 10, roda os testes, e fixa o primeiro ponto de atenção: cuidado com o entendimento do problema (0:05:16 a 0:06:24).

Linha do tempo:

- [0:00:00] Pause o vídeo e implemente a sua solução antes.
- [0:00:19] Enunciado: contador inteiro; Number of donuts: e a quantidade; 10 ou mais vira many.
- [0:00:59] Refatoração exige código estável; recruta a implementação mais comum; há uma função de teste.
- [0:01:26] pytest, rodado pelo PyCharm; o teste falha: donuts(4) retorna None [legenda: Nani].
- [0:02:04] Cola o código; roda; tudo passando; é a implementação que mais aparece.
- [0:02:35] Primeira coisa a observar: a relação do código com o domínio do problema.
- [0:03:02] Domínio do problema é de onde se extrai o conhecimento para criar o valor necessário.
- [0:03:19] Inversão: enunciado diz 10 ou mais; código usa count < 10; para ele é sempre um alerta.
- [0:04:17] Requisito displicente, user story mal detalhada; telefone sem fio.
- [0:05:16] Muda para maior ou igual a 10; roda os testes; passando.
- [0:05:48] Primeiro ponto de atenção: cuidado com o entendimento do problema.

Princípios enunciados:

- Refatoração exige código estável; sem testes passando não se começa (0:01:02).
- A primeira coisa a observar é a relação do código com o domínio do problema (0:02:37).
- Quando o código expressa o problema de um jeito distinto de como ele foi entendido, é um alerta (0:03:53).
- Validar que se entendeu perfeitamente o que tem de ser feito é muito importante (0:04:46).
- Defina muito bem, e expresse muito bem, o problema que está tentando resolver (0:05:07).
- Faça uma pequena mudança e rode os testes; isso se repete o tempo inteiro (0:05:44).

Código, reconstruído a partir da narração (ele não publica o arquivo). Implementação mais comum, como recrutada (0:02:04 e 0:03:35):

```python
def donuts(count):
    if count < 10:
        return 'Number of donuts: ' + str(count)
    else:
        return 'Number of donuts: many'


def test_donuts():
    assert donuts(4) == 'Number of donuts: 4'
```

Só o caso donuts(4) é ouvido na transcrição (0:01:46); os demais asserts do exercício original do Google não são narrados. Depois do alinhamento com o enunciado (0:05:23):

```python
def donuts(count):
    if count >= 10:
        return 'Number of donuts: many'
    else:
        return 'Number of donuts: ' + str(count)
```

Paráfrases da legenda (não verificadas):

- a primeira coisa que eu gosto de observar antes de qualquer coisa do código é a relação do código com o domínio do problema (0:02:37)
- pode ser que isso não seja um problema, pode, de qualquer maneira para mim isso é sempre um alerta (0:03:53)
- do mesmo jeito que na vida real a gente tem o problema de telefone sem fio, na programação toda vez que a gente vai fazer alguma coisa a gente faz a partir do nosso entendimento (0:04:39)
- veja que eu fiz só uma pequena mudança e rodei os testes, a gente vai fazer isso o tempo inteiro (0:05:44)

### Aula #07: Evitando labirintos

Vídeo: https://www.youtube.com/watch?v=YdQ74OOTPT4 · 351 s

Título no `playlist.json`: Refactoring in Practice #07: Avoiding Mazes (tradução automática); o título original em português não consta, e Evitando labirintos é retradução deste documento. A aula fecha com a dica mantenha o seu código linear (0:05:46).

Parte de como o computador funciona: tudo está na memória, que é sequencial, e a grande sacada é o desvio de execução, as condicionais (0:00:04 a 0:01:31). O risco é o código virar uma pulga, pulando de lugar em lugar, o que dificulta entender e agir; por isso o código deve ficar o mais linear e sequencial possível (0:01:36 a 0:02:07). O código do donuts viola isso: precisa do branch, mas não precisa de dois pontos de retorno; são quase dois programas fantasiados de um, e em relatórios isso vira três ou quatro níveis de condicionais (0:02:09 a 0:03:35). Solução: um único return, com uma variável de mensagem; entra por uma porta e sai por outra (0:03:42 a 0:04:36). Liga ao esquema entrada, processamento e saída e à imagem de uma lista de tarefas em que um item prepara o próximo (0:04:39 a 0:05:49).

Linha do tempo:

- [0:00:04] Princípio fundamental: o computador executa instruções sequencialmente na memória.
- [0:01:01] A sacada do computador é o desvio: condicionais, branches [legenda: brights].
- [0:01:36] É fácil o código virar uma pulga, quicando de um ponto para outro.
- [0:02:00] Manter o código o mais linear, direto e sequencial possível.
- [0:02:09] Violado aqui: a execução começa na linha 12 e salta para a 14 ou a 16, com dois retornos.
- [0:02:50] Se o código cresce, acumulam-se decisões; relatórios com três ou quatro níveis de condicionais; múltiplos programas fantasiados de um.
- [0:03:42] Como eliminar os dois returns: um único return; entra por uma porta e sai por outra; há um preço quando se faz diferente.
- [0:04:02] Cria a variável de mensagem nos dois ramos e retorna no fim; roda; passa.
- [0:04:39] Entrada, processamento e saída, da primeira aula de faculdade.
- [0:05:04] Dica: pense numa lista de tarefas em que um item prepara o próximo.

Princípios enunciados:

- Mantenha o código o mais linear, direto e sequencial possível (0:02:00).
- Precisar de uma decisão (branch) não obriga a ter dois pontos de retorno (0:02:15).
- Um ponto de entrada e um ponto de saída; múltiplos returns têm um preço e exigem saber por que se está pagando (0:03:42).
- Entrada, processamento e saída, e isso se mantém linear mesmo compondo várias chamadas (0:04:39).
- Enunciado claro sobre a sequência de passos mais código expresso da mesma forma: tudo fica fácil de gerir (0:05:35).

Código, reconstruído a partir da narração. Mudança em 0:04:02 a 0:04:21:

```python
def donuts(count):
    if count >= 10:
        message = 'Number of donuts: many'
    else:
        message = 'Number of donuts: ' + str(count)
    return message
```

O nome da variável é ouvido como mensagem (0:04:10; em #09 0:00:58 a legenda também diz mensagem). A reconstrução mantém `message` por coerência com o restante do código; o nome real não é verificável.

Paráfrases da legenda (não verificadas):

- é muito fácil o seu código virar uma pulga, fica pulando de lugar, fica quicando de um ponto para o outro (0:01:36)
- são múltiplos programas fantasiados de um código só, isso é um problema clássico, isso é muito sério (0:03:25)
- eu quero um único retâneo [return] no meu código, eu quero que ele entre por uma porta e saia para uma outra porta (0:03:45)
- mantenha o seu código linear (0:05:46)

### Aula #08: Siga um estilo

Vídeo: https://www.youtube.com/watch?v=GzgLKcS1YAc · 102 s

Algo passou despercebido sem gerar erro: a formatação está feia, e isso importa porque legibilidade é muito importante (0:00:00 a 0:00:23). Há incongruência na quantidade de espaços; não importa a linguagem, importa entender o estilo que se segue e mantê-lo; linters [legenda: slenders] ajudam, e em Python a maioria segue a PEP 8 (0:00:27 a 0:00:51). Ajusta manualmente para quatro espaços e separa com linhas em branco (0:00:53 a 0:01:09). Seja qual for a regra, mantenha e force o código a respeitá-la; mesmo mudança só de estilo exige rodar os testes (0:01:15 a 0:01:41).

Linha do tempo:

- [0:00:00] Algo passou despercebido: nenhum erro sinalizado, mas faz diferença.
- [0:00:14] A formatação está feia; legibilidade é muito importante.
- [0:00:27] Incongruência na quantidade de espaços; entenda o estilo e mantenha.
- [0:00:39] Linters ajudam; em Python, PEP 8.
- [0:00:53] Ajuste manual: tudo com quatro espaços; mais um enter para separar.
- [0:01:15] Seja qual for a regra de formatação, mantenha e force o código a respeitar.
- [0:01:28] Mesmo mudança só de estilo: executa os testes; tudo funcionando.

Princípios enunciados:

- Legibilidade é muito importante; código feio importa (0:00:20).
- Não importa a linguagem; entenda o estilo que está seguindo e mantenha esse estilo (0:00:33).
- Seja qual for a regra de formatação, mantenha a regra e force o código a respeitá-la (0:01:19).
- Mesmo uma mudança só de estilo exige rodar os testes (0:01:28).

Código, reconstruído: sem mudança de lógica em relação a #07; reindentação para quatro espaços e uma linha em branco entre o `if` e o `return` (0:00:56 a 0:01:09).

Paráfrases da legenda (não verificadas):

- a formatação do código está errada, tá bom, não tá errada mas tá feio, e isso importa (0:00:14)
- seja lá qual é a regra que você vai usar para formatação de código, mantenha essa regra, force o código a respeitar essa regra (0:01:19)
- respeite o estilo de código que você decidiu utilizar (0:01:38)

### Aula #09: Não se repita... nem se espalhe

Vídeo: https://www.youtube.com/watch?v=8XXmUHNHCQQ · 341 s

O mantra de evitar repetição vem com uma ressalva: repetição é o mesmo código com o mesmo propósito, não a mesma sintaxe (0:00:04 a 0:00:34). O repetido aqui é o texto Number of donuts; a solução clássica dos alunos, que resolve um problema criando outro, é extrair `message = 'Number of donuts: '` e fazer `+=` em cada ramo (0:00:37 a 0:01:22). O efeito colateral é espalhar a variável por todo o fluxo, que em código maior vira cirurgia de espingarda [legenda: choque grande surge]: mexer em um monte de lugar para uma mudança de intenção (0:01:22 a 0:02:42). Ele separa entrada, processamento e saída, puxa a mensagem para baixo, cria uma variável `t` de texto nos ramos e concatena no return; depois tira a variável intermediária (0:02:44 a 0:04:03). A linha de saída e o bloco do `if` ficam isolados, sem acoplamento, porque a variável transporta um valor para outro lugar e outro momento; desacoplamento é fractal e não é só entre classes; cuidado com o pensamento de C de declarar tudo antes (0:04:06 a 0:05:40).

Linha do tempo:

- [0:00:04] Mantra de evitar repetições; ressalva: mesmo código com o mesmo propósito, não sintaxe.
- [0:00:37] O repetido é o texto Number of Donuts.
- [0:00:46] Solução clássica que resolve um problema criando outro: `message = ...` e `+=` nos ramos; roda; passa.
- [0:01:22] Efeito colateral: a mensagem espalhada por todo o fluxo do código.
- [0:02:00] Shotgun surgery, cirurgia de espingarda: tirar caquinho por caquinho em vários lugares.
- [0:02:44] Separar entrada (número), processamento (decisão) e saída (mensagem); puxar a mensagem para baixo.
- [0:03:14] Variável `t` de texto nos ramos; soma no return; roda; funcionando.
- [0:03:39] Arruma a casa: a definição na linha 18 só serve à 19; coloca direto; roda; passa.
- [0:04:06] Linha de saída e bloco do `if` isolados, sem acoplamento; a variável transporta um valor.
- [0:04:47] Separar para que qualquer mudança aconteça com o menor impacto.
- [0:04:58] Desacoplamento não é só entre classes: é fractal, em múltiplos graus.
- [0:05:17] Pensamento de C de definir a variável antes; observe o impacto na semântica e na possibilidade de mudança.

Princípios enunciados:

- Evitar repetição é evitar o mesmo código com o mesmo propósito; prenda-se ao propósito, não à sintaxe (0:00:19).
- Eliminar repetição pode criar outro problema: espalhar (0:00:49).
- Separe entrada, processamento e saída (0:02:44).
- A variável serve para transportar um valor para outro lugar e outro momento (0:04:21).
- Separe as coisas para que qualquer mudança aconteça com o menor impacto possível (0:04:47).
- Desacoplamento não é só entre classes; é fractal, em múltiplos graus (0:04:58).
- Observe o impacto da organização na semântica e na possibilidade de mudança do código (0:05:31).

Código, reconstruído a partir da narração. Solução clássica dos alunos (0:00:56 a 0:01:19):

```python
def donuts(count):
    message = 'Number of donuts: '
    if count >= 10:
        message += 'many'
    else:
        message += str(count)
    return message
```

Versão dele, com a variável `t` (0:03:14 a 0:04:03):

```python
def donuts(count):
    if count >= 10:
        t = 'many'
    else:
        t = str(count)
    return 'Number of donuts: ' + t
```

Paráfrases da legenda (não verificadas):

- evitar repetição é você evitar que exista o mesmo código com o mesmo propósito, então não se prenda apenas à sintaxe, se prenda ao propósito (0:00:19)
- essa é uma solução clássica de resolver um problema criando outro (0:00:49)
- a variável serve para isso, ela transporta um valor para o outro lugar, para um outro momento (0:04:23)
- é um fractal, acontece em múltiplos graus e de várias formas (0:05:06)

### Aula #10: Nomes modelam a realidade

Vídeo: https://www.youtube.com/watch?v=H1Qi6vrPK6E · 143 s

De novo, resolver um problema criou outro: `t` é um péssimo nome, assim como `x`, `x1`, `bbb`, `tmp`, `str1`, `str2`; nomes que qualificam o tipo nomeiam em função da implementação e não do domínio (0:00:00 a 0:00:49). Bons nomes são difíceis, mas expressam um conceito de mais alto nível; pelo enunciado, o bom nome é quantidade, abreviado `qty` (0:00:49 a 0:01:27). Em vez de mudar na mão, usa o recurso de renomear da IDE (PyCharm, shift F6 no Mac), que muda todos ao mesmo tempo; roda os testes (0:01:32 a 0:01:57). Não economize nos nomes; ele só aceitou `t` antes porque estava refatorando a relação entre as partes; uma coisa de cada vez (0:01:59 a 0:02:22).

Linha do tempo:

- [0:00:00] Resolver um problema cria outro efeito colateral; agora é nomenclatura.
- [0:00:15] `t` é péssimo nome; `x`, `x1`, `bbb`, `tmp`, `str1`, `str2`, idade misturados.
- [0:00:40] Nomear em função da implementação e não do domínio do problema.
- [0:00:49] Bons nomes são difíceis, mas expressam ideia, conceito, abstração de mais alto nível.
- [0:01:05] Pelo enunciado, o bom nome é quantidade; abreviação `qty`.
- [0:01:35] Recurso de renomear da ferramenta; PyCharm [legenda: pai Charme], shift F6; roda; passando.
- [0:01:59] Não economize nos nomes.
- [0:02:04] Ele tomou a liberdade do `t` porque estava refatorando a relação entre as partes; agora, próximo estágio.
- [0:02:18] Não tente resolver tudo ao mesmo tempo; passo a passo, uma coisa de cada vez.

Princípios enunciados:

- Nomeie em função do domínio do problema, não da implementação (0:00:40).
- Bons nomes são difíceis de dar, mas expressam um conceito de mais alto nível (0:00:49).
- Use o recurso de renomear da sua ferramenta em vez de mudar na mão (0:01:35).
- Não economize nos nomes (0:01:59).
- Não tente resolver tudo ao mesmo tempo; uma coisa de cada vez (0:02:18).

Código, reconstruído: renomeação de `t` para `qty` (0:01:44 a 0:01:53):

```python
def donuts(count):
    if count >= 10:
        qty = 'many'
    else:
        qty = str(count)
    return 'Number of donuts: ' + qty
```

Paráfrases da legenda (não verificadas):

- T é um péssimo nome (0:00:15)
- você está nomeando as coisas em função da implementação e não em função do domínio do problema que está resolvendo (0:00:42)
- bons nomes são difíceis de dar mas são muito importantes porque eles vão expressar algo de mais alto nível (0:00:49)
- não tenta resolver tudo ao mesmo tempo, vai passo a passo fazendo uma coisa de cada vez (0:02:18)

### Aula #11: Simetria de tipos

Vídeo: https://www.youtube.com/watch?v=kQHMSxpbcsc · 188 s

Misturar tipos de dado no mesmo contexto gera bugs chatos; variante comum: `qty = count` sem `str` e interpolação com `%s`; roda e passa (0:00:00 a 0:00:47). O problema: `count` é inteiro e o `if` calcula sobre o inteiro, mas a saída desejada é string; o bloco do `if` transforma inteiro em string, e a questão entrada, processamento e saída também é fractal, valendo para as partes da função (0:00:48 a 0:01:45). O ideal é garantir `qty` sempre string; a variante funciona implicitamente, por acaso, porque a interpolação do Python converte; se alguém trocar por soma, quebra na hora (0:01:45 a 0:02:31). Resolve com `str(count)`, que não é só conversão: instancia uma string a partir do inteiro, ou seja, há uma lógica de transformação no `if`; identifique e respeite o tipo em cada setor do código (0:02:33 a 0:03:06).

Linha do tempo:

- [0:00:00] Misturar tipos de dado no mesmo contexto gera bugs chatos de resolver.
- [0:00:16] Variante comum: `qty = count` (sem `str`) e interpolação `%s`; roda; passa.
- [0:00:48] `count` é inteiro; o `if` calcula em cima do inteiro, mas a saída é string.
- [0:01:11] Olhar os tipos dentro do bloco: o `if` transforma inteiro em string.
- [0:01:33] Entrada, processamento e saída também é fractal; olhe as partes do código.
- [0:01:45] Ideal: `qty` sempre string; funciona implicitamente por acaso da interpolação.
- [0:02:19] Se alguém trocar por soma, quebra na hora: misturou tipos.
- [0:02:40] `str(count)` não é só conversão; instancia uma string: lógica de transformação.
- [0:02:56] Identifique e respeite o tipo de dado em cada setor do código.

Princípios enunciados:

- Não misture tipos de dado no mesmo contexto (0:00:00).
- Entrada, processamento e saída é fractal: olhe também as partes internas da função e como se relacionam (0:01:33).
- Não dependa de conversão implícita; o que funciona por acaso quebra depois (0:02:03).
- Identifique e respeite o tipo de dado com que está trabalhando em cada setor do código (0:02:56).

Código, reconstruído a partir da narração. Variante com mistura de tipos (0:00:16 a 0:00:41):

```python
def donuts(count):
    if count >= 10:
        qty = 'many'
    else:
        qty = count
    return 'Number of donuts: %s' % qty
```

Correção (0:02:40): `qty = str(count)` no `else`, voltando à forma de #10.

Paráfrases da legenda (não verificadas):

- um outro problema muito comum que eu vejo é o processo de misturar tipos de dados no mesmo contexto (0:00:00)
- essa questão do input processamento também é fractal (0:01:33)
- aqui tá funcionando implicitamente porque por acaso a interpolação de string do Python vai fazer a conversão se for necessário (0:02:03)
- o str count ele não tá simplesmente convertendo, está instanciando uma string a partir do inteiro, ou seja, de fato nesse if tem uma lógica de transformação (0:02:46)

### Aula #12: Explícito é melhor que implícito

Vídeo: https://www.youtube.com/watch?v=2V6lofWSeJc · 224 s

Na busca por linearidade surge uma negação do `if`: todo `if` tem um `else`, explícito ou implícito, e para economizar linhas as pessoas deixam o código menor do que deveria (0:00:00 a 0:00:42). O truque é quebrar o `if`: extrair o ramo do `else` como valor default [legenda: valor de fogo] antes do `if`, `qty = str(count)`, e sobrescrever no `if`; funciona, mas rompe a estrutura do `if`; o `else` continua existindo, só que implícito, e em lógica maior alguém puxa o fio errado na manutenção (0:00:47 a 0:01:42). Valor default é útil para exceção; aqui há dois caminhos válidos e o `if` expressa isso; ele volta atrás e roda os testes (0:01:45 a 0:02:24). Pergunte por que quer economizar aquela linha; o fundamental é o balanceamento entre forma e função, e a decisão vai além do código: experiência da equipe, culturas diferentes, domínio local como o RG (0:02:24 a 0:03:42).

Linha do tempo:

- [0:00:00] Na busca de linearidade, negação do `if`; todo `if` tem um `else`, explícito ou implícito.
- [0:00:19] Economizar linhas deixa o código menor do que deveria.
- [0:00:47] Quebrar o `if`: `qty = str(count)` como valor default antes, `if` sem `else`.
- [0:01:03] Eliminou uma linha, continua funcionando, mas rompeu a estrutura do `if`.
- [0:01:31] Em lógica mais complexa, alguém puxa o fio errado na manutenção.
- [0:01:45] Valor default é útil para exceção; aqui são dois caminhos válidos e o `if` expressa isso.
- [0:02:13] Volta atrás; roda para estabilizar e garantir que a refatoração não fez lambança.
- [0:02:24] Por que economizar a linha? Às vezes senso estético; balanceamento entre forma e função.
- [0:02:47] Decisão além do código: equipe com pouca experiência, culturas diferentes, exemplo do RG.
- [0:03:30] Até onde ir na refatoração considera mais do que o código.

Princípios enunciados:

- Todo `if` tem um `else`, explícito ou implícito (0:00:12).
- Pergunte até onde vale a pena economizar linha de código (0:00:40).
- Valor default mascarando um `else` rompe a estrutura do `if` (0:01:13).
- Valor default serve para exceção; dois caminhos válidos pedem `if` e `else` explícitos (0:01:45).
- O fundamental é o balanceamento entre forma e função (0:02:32).
- A decisão de organização considera a equipe, as culturas e o domínio, não só o código (0:02:47).

Código, reconstruído a partir da narração. Variante com valor default (0:00:47 a 0:01:03), depois revertida:

```python
def donuts(count):
    qty = str(count)
    if count >= 10:
        qty = 'many'
    return 'Number of donuts: ' + qty
```

Paráfrases da legenda (não verificadas):

- todo if tem um Élcio [else], não interessa o que aconteça, pode ser explícito, pode ser implícito (0:00:12)
- mas você acabou de romper com a própria estrutura do if (0:01:10)
- existem dois caminhos válidos, o if expressa isso e deveria ser mantido (0:02:05)
- para mim o que é fundamental é um balanceamento entre forma e função, não dá para fazer a coisa só estética e não dá para fazer a coisa só funcional (0:02:32)

### Aula #13: Quando menos não é mais

Vídeo: https://www.youtube.com/watch?v=pDKPX5NfbnA · 202 s

Quem foca só na execução, e não na manutenção, sobrescreve o input: o iniciante acha que variável é só para guardar qualquer coisa, mas isso aparece em projetos grandes também, pela dificuldade de nomear (0:00:00 a 0:00:46). A variante: `count = 'many'` dentro do `if` e interpolação direta; passa, mas ressignifica `count`, que é inteiro com natureza de contagem, em string (0:00:46 a 0:01:28). Pode? Pode; precisa? Só com argumento muito sólido; ele evita completamente mudar a entrada, a menos que seja a proposta do algoritmo, como ordenação in-place, e busca funções sem efeitos colaterais para manter a entrada disponível para decisões futuras (0:01:28 a 0:02:19). Mesmo com `str(count)` na concatenação, não acha boa decisão; prefere a forma com `qty` e `else` explícito; na ânsia de enxugar se paga um preço de legibilidade (0:02:19 a 0:03:19).

Linha do tempo:

- [0:00:00] Foco só na execução, não na manutenção: sobrescrita do input.
- [0:00:17] Iniciante acha que variável é só para guardar algo; aparece em projetos grandes pela dificuldade de nomear.
- [0:00:46] Variante: `count = 'many'` no `if`, interpolação `%s` com `count`; roda; passa.
- [0:01:13] Dois problemas: ressignificou `count` (inteiro, contagem) em string; e misturou tipos de novo.
- [0:01:28] Pode fazer? Pode; precisa? Argumento muito sólido.
- [0:01:36] Ele evita completamente mudar a entrada, a menos que seja a proposta do algoritmo (ordenação).
- [0:01:49] Funções sem efeitos colaterais; entrada nem ressignificada nem alterada; dado de entrada disponível para decisões.
- [0:02:19] Mesmo com `str(count)` na concatenação, não acha boa decisão.
- [0:02:47] Prefere a forma anterior: `count` toma a decisão, guarda em `qty`, `else` explícito.
- [0:03:09] Cuidado na ânsia de enxugar: preço de legibilidade para quem nunca viu o programa.

Princípios enunciados:

- Não sobrescreva o input (0:00:11).
- Ressignificar uma variável em execução exige um argumento muito sólido (0:01:23).
- Evite mudar a entrada, a menos que isso seja a proposta do algoritmo (0:01:36).
- Busque funções sem efeitos colaterais; a entrada permanece disponível para decisões futuras (0:01:49).
- Enxugar código tem preço de legibilidade e compreensão para quem nunca viu o programa (0:03:09).

Código, reconstruído a partir da narração. Variante com sobrescrita do input (0:00:46 a 0:01:11), depois revertida:

```python
def donuts(count):
    if count >= 10:
        count = 'many'
    return 'Number of donuts: %s' % count
```

Paráfrases da legenda (não verificadas):

- o cálcio [else] ressignificou o count em execução; pode fazer isso? pode, mas precisa fazer isso? eu acho que não (0:01:23)
- as coisas não são escritas em pedra, mas precisa de um argumento muito sólido (0:01:34)
- eu gosto de buscar fazer funções que não tem efeitos colaterais (0:01:49)
- cuidado na ânsia de tentar enxugar o código, porque você pode acabar pagando um preço de legibilidade e de compreensão de quem nunca viu aquele programa antes (0:03:09)

### Aula #14: Números mágicos

Vídeo: https://www.youtube.com/watch?v=qfhrOp1vnyU · 175 s

O número 10 não quer dizer muita coisa: serve para tomar decisão, mas que nome expressa a sua função? Ele propõe limite, cria `limite = 10` e compara com ele; quanto mais próximo do domínio, melhor; roda (0:00:07 a 0:01:13). Depois, injeção de dependência: o limite vira parâmetro da função com valor padrão 10; se virou atacadista com limite 100, chama passando 100 (0:01:22 a 0:01:55). Cuidado para não passar todas as opções para a assinatura, porque muitos parâmetros é outro cheiro de código (0:02:07 a 0:02:21). O valor padrão mantém o comportamento externo, então continua sendo refatoração; o número mágico foi extraído, nomeado e virou configuração da execução (0:02:23 a 0:02:53).

Linha do tempo:

- [0:00:07] O número 10 não quer dizer muita coisa; que nome expressa o que ele faz?
- [0:00:37] Nome: limite; variável `limite = 10`; `count >= limite`.
- [0:00:55] Qualquer nome que expresse melhor; quanto mais próximo do domínio, melhor.
- [0:01:08] Roda; funcionando; já ficou mais expressivo.
- [0:01:22] Injeção de dependência: limite fornecido à função com valor padrão.
- [0:01:45] Atacadista com limite 100: chama a função passando 100.
- [0:02:07] Cuidado para não passar toda opção para a assinatura: muitos parâmetros é outro cheiro de código [legenda: colds Mel].
- [0:02:28] O valor padrão mantém tudo funcionando: melhoria sem mudar o comportamento exterior.
- [0:02:37] Magic number [legenda: médico Number] extraído, nomeado, virou configuração da execução.

Princípios enunciados:

- Dê nome ao número que decide algo; quanto mais próximo do domínio do problema, melhor (0:00:34).
- Mova o limite para um parâmetro com valor padrão (injeção de dependência) (0:01:25).
- Não passe todas as opções para a assinatura; muitos parâmetros é um cheiro de código (0:02:07).
- O valor padrão preserva o comportamento externo, o que mantém a mudança como refatoração (0:02:28).
- Extraia o número mágico, nomeie e torne-o configuração da execução (0:02:48).

Código, reconstruído a partir da narração. Passo 1 (0:00:40): `limite = 10` dentro da função. Passo 2 (0:01:32 a 0:01:41):

```python
def donuts(count, limite=10):
    if count >= limite:
        qty = 'many'
    else:
        qty = str(count)
    return 'Number of donuts: ' + qty
```

Chamada do atacadista narrada em 0:01:50: `donuts(count, 100)` ou equivalente; a forma exata não é ouvida.

Paráfrases da legenda (não verificadas):

- esse número 10 é um número que não quer dizer muita coisa, o que que ele representa (0:00:15)
- eu posso também fazer uma injeção de dependência, eu posso fazer com que o 10, limite, seja fornecido para a função e considerar um valor padrão (0:01:22)
- tem que tomar cuidado para também não passar tudo quanto é opção do seu código para dentro da assinatura da função, porque isso vai gerar um outro colds Mel [code smell] (0:02:07)
- o que eu fiz foi pegar um médico Number [magic number], um número que tá lá solto no meu código, e extrair ele, dar um nome bom e tornar ele uma configuração da execução do meu algoritmo (0:02:37)

### Aula #15: Não seja um espertalhão

Vídeo: https://www.youtube.com/watch?v=npXhjOlhjGc · 158 s

Com o código estável e claro, aparece a coceira de fazer diferente, de ser espertalhão: quatro linhas, por que não uma só? Troca o `if` comando pelo `if` por expressão e roda; passa (0:00:00 a 0:01:20). Agora está tudo numa tripa só e é preciso saber de cabeça a ordem dos operadores e se precisa de parênteses; juntou a lógica de processamento com a montagem da saída (0:01:30 a 0:01:59). Num exercício é legal; num projeto ele não recomenda, porque vai mudar e crescer e será preciso refazer o que funcionava; volta para o que estava, resiste à tentação, pensa na evolução do projeto e da equipe e roda de novo (0:01:59 a 0:02:36).

Linha do tempo:

- [0:00:00] Código estável e claro; comichão de fazer diferente; ser espertalhão.
- [0:00:23] Quatro linhas em uma: trocar o `if` comando por `if` por expressão.
- [0:01:05] Roda; passou; funcionou.
- [0:01:30] Tudo numa tripa só; precisa saber a ordem dos operadores; parênteses?
- [0:01:49] Juntou a tomada de decisão sobre o número com a montagem da saída.
- [0:01:59] Num exercício é bacana; num projeto, não recomenda nem um pouco.
- [0:02:22] Volta para o que estava; resista à tentação de ser espertão; pragmatismo.
- [0:02:32] Roda de novo; tudo funcionando.

Princípios enunciados:

- Não junte a tomada de decisão com a montagem da saída numa linha só (0:01:49).
- Tudo numa linha serve para exercício, não para projeto que vai mudar e crescer (0:02:01).
- Resista à tentação de ser espertão; seja pragmático pensando na evolução do projeto e da equipe (0:02:25).

Código, reconstruído a partir da narração. Variante numa linha (0:00:45 a 0:01:05), depois revertida:

```python
def donuts(count, limite=10):
    return 'Number of donuts: ' + ('many' if count >= limite else str(count))
```

A posição exata dos parênteses não é ouvida; ele mesmo pergunta se precisa deles (0:01:41).

Paráfrases da legenda (não verificadas):

- sabe aquele bichinho que vai falar no nosso ouvido: dá para fazer diferente, dá para fazer diferente; e a gente começa a ser espertalhão (0:00:11)
- agora tá tudo numa tripa só, numa única linha, e você tem que saber de cabeça qual é a ordem dos operadores (0:01:30)
- num exercício é legal, é bacana você fazer tudo numa linha só, mas num projeto eu não recomendo, não recomendo nem um pouco (0:01:59)
- resista à tentação de ser um espertão, vamos tentar ser o mais pragmático possível, pensar na evolução do projeto e da equipe (0:02:25)

### Aula #16: Torne evidente o que é óbvio

Vídeo: https://www.youtube.com/watch?v=1iPHoTnfkhM · 761 s

Ele pararia por aqui com iniciantes, mas há uma oportunidade de design orientado a objetos mesmo em código procedural pequeno: um conceito que está manifesto mas não expresso, óbvio mas não evidente (0:00:18 a 0:00:46). O pecado capital de quem estuda OO é olhar classe, atributo, público e privado; a essência é a interação dos objetos, a troca de mensagens (0:00:49 a 0:01:15). A função donuts existe para fornecer um relatório, mas todo o seu código calcula; o conceito de quantidade está disperso; ele vai encapsular o `if` numa classe Quantity [legenda: quantite, quântico] (0:01:25 a 0:02:10). Primeiro roda e escreve testes para não desestabilizar; cria `test_quantity`, instancia `Quantity(9)`, vê falhar, cria a classe, adiciona `__init__(count)`, testa `str(Quantity(9)) == '9'`, o teste pega um typo, faz `__str__` retornar '9' fixo porque está montando as bordas do quebra-cabeça (0:02:12 a 0:04:50). Testa `str(Quantity(10)) == 'many'`, copia a lógica do `if` para `__str__`, guarda `self.count` e `self.limite = 10`; donuts passa a usar `str(Quantity(count))` e a interface se simplifica; o conceito fica reaproveitável e o atacadão de 100 muda num único lugar (0:04:55 a 0:07:45). Cereja: método `many` com a expressão, `__str__` vira um `if` por expressão, `@property`, e donuts vira `format` ou f-string com `Quantity(count)` (0:07:47 a 0:10:42). Exemplo de moeda em classe em vez de primitivo; sempre que houver repetição ou muitos `if`s, pergunte se aquilo não é um conceito; objetos expressam interações (0:10:56 a 0:12:39).

Linha do tempo:

- [0:00:18] Oportunidade de design OO mesmo em código pequeno: conceito manifesto mas não expresso; óbvio mas não evidente.
- [0:00:49] Pecado capital ao estudar OO: olhar classe, atributos, público, privado; a essência é a troca de mensagens.
- [0:01:25] donuts existe para fornecer o relatório, mas todo o código calcula; o conceito de quantidade está disperso; [0:02:02] extrair e encapsular o `if` num conceito ainda não manifestado: Quantity.
- [0:02:12] Antes, rodar e escrever testes para não desestabilizar o projeto.
- [0:02:30] `test_quantity`: `Quantity(9)`; falha; cria a classe; falha por argumento; `__init__(self, count)`; passa.
- [0:03:44] `assert str(Quantity(9)) == '9'`; o teste pega um erro de digitação; [0:04:22] `__str__` retorna '9' fixo: interfaces primeiro, como as bordas de um quebra-cabeça.
- [0:04:55] `assert str(Quantity(10)) == 'many'`; estoura; copia a lógica do `if`; `self.count`, `self.limite = 10`; passa.
- [0:06:34] donuts usa `str(Quantity(count))`; apaga o resto; simplifica a interface; passa.
- [0:07:23] Conceito reaproveitável em qualquer relatório; atacadão de 100: muda num único lugar.
- [0:07:47] Cereja do bolo: método `many` com a expressão; `__str__` vira `'many' if self.many else str(self.count)`; [0:09:14] `@property` no `many`: método usado como atributo.
- [0:09:48] donuts com `format` e depois f-string, interpolando `Quantity(count)`.
- [0:10:56] Exemplo de moeda: classe para o número que representa dinheiro, em vez de primitivo tratado em cada relatório; [0:11:44] repetição ou muitos `if`s: pergunte se não poderia ser um conceito; objetos expressam interações.

Princípios enunciados:

- Torne evidente o que está óbvio mas não expresso no código (0:00:42).
- A essência da orientação a objetos é a interação entre objetos, a troca de mensagens, não classes e atributos (0:01:02).
- Um `if` que decide sobre um conceito pode ser encapsulado numa classe desse conceito (0:01:55).
- Antes de extrair, rode o código e escreva testes; não desestabilize o projeto (0:02:12).
- O teste pega erro de digitação; é muito importante usar teste ao refatorar (0:03:59).
- Trabalhe primeiro as interfaces, como as bordas de um quebra-cabeça; o miolo depois (0:04:29).
- Conceito encapsulado muda em um único lugar e todos os usos continuam funcionando (0:07:33).
- O problema de #11 era misturar; tudo string, tudo inteiro ou tudo Quantity é consistente (0:09:57).
- Sempre que houver repetição ou muitos `if`s, pergunte se aquilo não é um conceito (0:11:44).
- Olhe objetos não só como forma de descrever coisas, mas como forma de expressar interações (0:11:57).

Código, reconstruído a partir da narração; ele não publica o arquivo. Nome da classe ouvido como quantite e quântico, reconstruído como `Quantity`; o nome do atributo de limite é ouvido como limite (0:05:49). Estado final em 0:10:33:

```python
class Quantity:
    def __init__(self, count):
        self.count = count
        self.limite = 10

    @property
    def many(self):
        return self.count >= self.limite

    def __str__(self):
        return 'many' if self.many else str(self.count)


def donuts(count):
    return f'Number of donuts: {Quantity(count)}'


def test_quantity():
    assert str(Quantity(9)) == '9'
    assert str(Quantity(10)) == 'many'
```

Observações: o limite deixa de ser parâmetro de donuts; ele diz eu não tô passando o limite mas ele já tá lá (0:06:13). Se `__init__` recebe `limite` com valor padrão ou fixa 10 internamente não é verificável; a reconstrução fixa 10 porque ele diz boto aqui em cima o limite igual a 10 (0:05:54). A versão intermediária com `format` (0:10:09) antecede a f-string.

Paráfrases da legenda (não verificadas):

- um conceito que ele está manifesto mas não tá expresso, ele tá óbvio mas não tá evidente, a gente precisa evidenciar isso (0:00:38)
- a essência da orientação a objeto é exatamente a interação dos objetos com o exterior, a interação dos objetos entre si, é nessa troca de mensagem que a coisa acontece (0:01:04)
- é como se tivesse montando um quebra-cabeça em que eu começo pelas bordas, o que delimita, e depois o miolo a gente vai trabalhando e refatorando (0:04:38)
- sempre que você tem repetição no seu código ou que você tem muitos ifs tomando várias decisões, pense se aquilo não poderia ser um conceito do funcionamento do seu código (0:11:44)

### Aula #17: O Que Não Te Contaram Sobre Componentes

Vídeo: https://www.youtube.com/watch?v=_XObMldi2B0 · 872 s

Começa pelo porquê: refatoração tem relação econômica com a sustentabilidade do projeto; a pergunta agora é como saber que se está no caminho certo (0:00:00 a 0:00:31). Em 1968 a OTAN reuniu profissionais para discutir a crise do software, e Douglas McIlroy [legenda: Douglas macroy] abordou pela primeira vez componentização; McIlroy foi chefe de Ken Thompson no Unix e responsável pelo pipeline, que conecta saída de um programa à entrada de outro; seu paper reclamava que se discutia como construir e não que componentes usar (0:00:33 a 0:02:15). O maior desafio é padronização, ilustrado pela função seno e suas variações (0:02:15 a 0:03:22). Ele distingue arquitetura (o que é difícil de mudar) de design (como as partes se relacionam intimamente), que é onde está a capacidade de mudança; design é equilíbrio entre forma e função; cita Dijkstra [legenda: Dexter] sobre máquinas mais poderosas tornarem a programação um problema gigantesco (0:03:32 a 0:05:33). O que não é componente: a máquina de Rube Goldberg tem partes, não componentes; dominós são componentes porque são iguais, substituíveis e compõem; quebra-cabeça não é componente; operadores aritméticos cooperam compondo coisas mais complexas; componentes eletrônicos operam todos sobre fluxo de elétrons, e a natureza do que é processado define o que encaixa; transformar número em string muda a natureza e, sem atenção, o código escorrega para Rube Goldberg com forte acoplamento (0:05:37 a 0:11:44). Fecha com as dimensões a observar para identificar componentes implícitos: natureza, forma, interdependência e generalidade das entradas; o mesmo para saídas; processamento (transforma, cria ou filtra; consistência); responsabilidade única ou várias; robustez; componentes emergem do contexto, não de regra (0:11:44 a 0:14:30).

Linha do tempo:

- [0:00:00] Começar pelo porquê; refatoração tem relação econômica com a sustentabilidade do projeto.
- [0:00:33] 1968, OTAN, crise do software; Douglas McIlroy e o conceito de componentização; [0:01:15] McIlroy, Unix, pipeline: saída de um conecta à entrada de outro.
- [0:01:43] Reutilização como em outras indústrias; discutir que componentes usar, não como construir.
- [0:02:15] Desafio da padronização; exemplo da função seno e suas variações no computador.
- [0:03:32] Arquitetura (difícil de mudar) versus design interno (como as partes se relacionam); design é equilíbrio entre forma e função.
- [0:04:38] Dijkstra sobre a crise do software: máquinas gigantes, programação gigantesca.
- [0:05:37] O que não é componente: máquina de Rube Goldberg tem partes, não componentes.
- [0:06:48] Dominós: mesmo componente, substituíveis, compõem; quebra-cabeça não é componente, mas mostra fronteiras.
- [0:07:58] Operadores aritméticos: entradas e saída variam, mas cooperam compondo coisas mais complexas.
- [0:09:06] Componentes eletrônicos: todos operam sobre fluxo de elétrons; a natureza do processado define restrições; [0:10:23] HD e cartão perfurado: mudança de natureza mexe com a categorização dos componentes.
- [0:10:56] Transformar número em string é mexer em naturezas diferentes; escorregar para Rube Goldberg e forte acoplamento.
- [0:12:09] Dimensões: entradas (natureza, forma, interdependência, generalidade), saídas, processamento, responsabilidade, robustez; [0:14:04] não é regra; componentes emergem do contexto; observar para reduzir código enquanto aumenta a capacidade.

Princípios enunciados:

- Ao explorar um conceito novo, comece pelo porquê (0:00:02).
- A capacidade de mudança do software vem do design interno, de como as partes se relacionam, mais do que da arquitetura (0:03:50).
- Design é a busca de equilíbrio entre forma e função (0:04:14).
- Fazer funcionar não está errado, só não é o bastante (0:05:40).
- Partes não são componentes; componentes podem ser substituídos e padronizados (0:06:35).
- A característica fundamental de um componente é trabalhar cooperativamente, compondo coisas mais complexas (0:08:12).
- A variação e a combinação dos componentes têm relação com a natureza do que está sendo processado (0:09:27).
- Um componente que transforma número em string mexe em naturezas diferentes; transformações limitam o que encaixa com o quê (0:10:56).
- Identificar o componente implícito e torná-lo evidente é papel do programador (0:11:52).
- Não é questão de regra: componentes emergem do contexto; observe as dimensões para identificar padrões (0:14:04).

Código: nenhum. Aula expositiva com slides.

Paráfrases da legenda (não verificadas):

- quando vai começar um projeto novo todo mundo discutia como deveríamos construir algo e não que componentes devemos utilizar para resolver o problema (0:02:07, ele resumindo o paper de McIlroy)
- a capacidade de mudança do software para mim tem muito mais relação com o seu design interno, com como as partes se relacionam de forma mais íntima (0:03:50)
- uma máquina desse tipo ela não tem componentes, ela tem partes (0:06:35)
- não é uma questão de regra, os componentes vão em energia [emergir] a partir do seu contexto (0:14:07)

### Aula #18: O Desafio de Entender Componentes

Vídeo: https://www.youtube.com/watch?v=1pAk4C8Y0Ns · 149 s

Abertura do bloco prático sobre componentes. Ele avisa que o objetivo não é decorar técnicas, e sim sensibilizar para um processo de observação e organização que permita decidir o que fazer primeiro ao abordar código desconhecido (0:00:13). Vai usar Python, mas a linguagem não importa (0:00:44). O que ele chama de ajuste de relevância é a dinâmica natural do cérebro de olhar um foco, depois o entorno, descer e subir um nível (0:00:52). A crítica central: refatoração como receita de bolo fica presa ao texto do código, quando o que importa é o fluxo de informação e de execução, que está implícito (0:01:15 a 0:01:38). Pede atenção à semântica, à relação entre linhas e à proximidade entre coisas relacionadas, e anuncia a natureza fractal dos componentes (0:01:38 a 0:02:24).

Linha do tempo:

- [0:00:00] Anuncia a investigação das dimensões dos componentes e das oportunidades escondidas nas entrelinhas.
- [0:00:13] Objetivo: não decorar nada, sensibilizar para o processo de observação e organização.
- [0:00:44] Não importa a linguagem; vai mostrar em Python.
- [0:00:52] Processo de ajuste de relevância: olhar o foco, o entorno, descer um nível, subir um nível, dentro e fora da caixa.
- [0:01:15] Crítica à refatoração como receita de bolo: o que importa é o fluxo de execução, que está implícito no código.
- [0:01:38] Observar não só a sintaxe mas a semântica: o que começa, o que termina, relação entre linhas e proximidade.
- [0:02:09] Natureza fractal dos componentes: pequenos se agrupam em maiores.
- [0:02:24] Chamada para a mão na massa.

Princípios enunciados:

- Não decore técnicas; treine o processo de observar e organizar para decidir o que fazer primeiro (0:00:13).
- Refatorar é ajustar relevância: olhar o foco, depois o entorno, descer e subir um nível (0:00:52).
- O fluxo de execução não está no texto do código, está implícito; é ele que precisa ser percebido (0:01:29).
- Coisas relacionadas devem estar próximas; observe a proximidade (0:01:54).
- Componentes têm natureza fractal: pequenos se agrupam em maiores, e se trabalha isso passo a passo (0:02:09).

Código: nenhum nesta aula.

Paráfrases da legenda (não verificadas):

- o meu grande objetivo aqui novamente não é fazer você decorar absolutamente nada, eu quero te sensibilizar para o processo de observação, de organização (0:00:13)
- mais importante que isso na minha visão é perceber o fluxo da informação, o fluxo de execução do programa; isso não está no código, isso está implícito no código (0:01:29)
- existe uma natureza fractal nos componentes: componentes muito pequenos que se agrupam, criam componentes maiores (0:02:09)

### Aula #19: Testando O Que Não Tem Testes

Vídeo: https://www.youtube.com/watch?v=pFDv4S49AGo · 244 s

Apesar do título na playlist, o conteúdo desta aula é o enunciado do exercício wordcount; os testes aparecem na aula #20. Ele abre com o ciclo fazer funcionar, fazer direito e, se medir, fazer rápido, e insiste que não faz sentido fragmentar isso em três tarefas: os três estágios acontecem no mesmo fluxo com escopo reduzido, porque escopo reduzido intensifica o ciclo de feedback (0:00:09 a 0:00:50). Lê o enunciado: um programa que conta palavras de um arquivo em dois modos, `--count` (ordem alfabética com ocorrências) e `--topcount` (as 20 mais frequentes), com um esqueleto que já traz `main` chamando `print_words` e `print_top` (0:01:39 a 0:03:05). Pede que o aluno pause, implemente a sua solução antes de ver as próximas aulas, e poste o link do GitHub nos comentários (0:01:16 e 0:03:48).

Linha do tempo:

- [0:00:00] Apresenta o exercício que costuma surpreender os alunos.
- [0:00:09] As pessoas se preocupam com fazer funcionar; o ciclo completo é funcionar, direito e rápido.
- [0:00:26] Não faz sentido ter uma tarefa para cada estágio; os três no mesmo fluxo com escopo reduzido.
- [0:00:50] Escopo reduzido intensifica o feedback e garante passos de progresso.
- [0:01:16] Link do exercício; pausar e implementar antes de continuar.
- [0:01:39] Enunciado do wordcount: `--count` lista as palavras em ordem alfabética com ocorrências (exemplo `letras.txt`).
- [0:02:30] `--topcount` lista as 20 palavras mais frequentes.
- [0:03:05] O esqueleto fornece `main`, que analisa os parâmetros e chama `print_words` ou `print_top`.
- [0:03:48] Pede o link do código no GitHub nos comentários.

Princípios enunciados:

- Faça o ciclo completo: fazer funcionar, fazer direito e, se medir, fazer rápido (0:00:14).
- Não fragmente o trabalho em três tarefas separadas (funcionar, direito, performance) (0:00:26).
- Use os três estágios no mesmo fluxo, com escopo reduzido (0:00:47).
- Reduzir o escopo intensifica o ciclo de feedback e garante que os passos são de progresso (0:00:50).
- Implemente a sua solução antes de ver a dele, para contrastar o que e como pensou (0:01:23).

Código, reconstruído a partir do que ele descreve do esqueleto; não publicado por ele:

```python
import sys


def print_words(filename):
    ...  # a implementar


def print_top(filename):
    ...  # a implementar


def main():
    # analisa sys.argv e chama print_words ou print_top
    # conforme o parâmetro --count ou --topcount
    ...
```

A transcrição ouve wordcout, Word Card e pai para wordcount, wordcount.py e py; county para count.

Paráfrases da legenda (não verificadas):

- a gente tem que fazer funcionar, fazer direito e, se precisar, se você medir, você faz ficar rápido (0:00:14)
- quando você reduz o escopo você intensifica o seu ciclo de feedback e você tem garantias de que os passos que você tá dando realmente são passos de progresso (0:00:50)
- é um desafio simples com código que pode ficar uma macarronada linda (0:01:10)

### Aula #20: A Herança Maldita

Vídeo: https://www.youtube.com/watch?v=DThBxTy15A4 · 602 s

Em vez de implementar a própria solução, ele recebe de presente um código legado do wordcount. Não gosta do termo: o que define código legado não é idade nem autoria, é o grau de entropia, a perda de conexão com o porquê das coisas (0:01:19). Componentização é o recurso para não ter que mexer em tudo ao mesmo tempo (0:01:56). Antes de ler o código, executa: `SyntaxError` por `print` do Python 2 nas linhas 73 e 91, corrige, cria o `letras.txt` do enunciado com `echo`, roda `--count` e `--topcount` e confere com o exemplo (0:02:17 a 0:04:12). Como o código não tem testes e o programa é determinístico (mesmo arquivo, mesmo resultado), redireciona as saídas para `count.txt` e `topcount.txt` e usa `diff` para cercar o programa por fora: são os golden files (0:05:01 a 0:06:49). Em seguida faz o mesmo com pytest (`test_wordcount.py`, com `capsys` e `monkeypatch` sobre `sys.argv`), deixando o terreno preparado para quando as refatorações se complicarem; menciona `subprocess` como alternativa. Os dois testes passam (0:07:30 a 0:09:52).

Linha do tempo:

- [0:00:06] Recebe um código legado; discute o termo; [0:01:19] o que define código legado é o grau de entropia.
- [0:01:56] Componentização para não mexer em tudo ao mesmo tempo nem precisar conhecer tudo.
- [0:02:17] Antes de ler o código, executar.
- [0:02:52] `SyntaxError`: `print` do Python 2 na linha 73, depois na 91; corrige e roda de novo.
- [0:03:42] Cria `letras.txt` com o conteúdo do enunciado via `echo`.
- [0:04:12] Roda `--count` (a 2, b 4, c 3) e `--topcount`; igual ao esperado.
- [0:04:39] Programar é insistir no erro; é preciso cercar o trabalho.
- [0:05:01] Sem testes: programa determinístico de entrada e saída; redireciona a saída para `topcount.txt` e `count.txt`.
- [0:05:55] `diff` entre o arquivo esperado e a saída atual; demonstra a diferença com um `echo asdf`; [0:06:49] nomeia: golden file, arquivo de ouro.
- [0:07:30] Mesma coisa com pytest: `test_wordcount.py`, `capsys`, `monkeypatch`, função auxiliar `run`; [0:08:44] `run` faz patch de `sys.argv` e captura o stdout.
- [0:09:30] Alternativa sem pytest: módulo `subprocess`.
- [0:09:52] Dois testes encontrados e passando; pronto para mudar o código.

Princípios enunciados:

- O que define código legado é o grau de entropia, não a idade nem quem escreveu (0:01:19).
- Componentização é o recurso para não mexer em tudo ao mesmo tempo nem precisar conhecer tudo (0:01:56).
- Antes de ler o código, execute-o; crie as condições para vê-lo funcionar (0:02:17).
- Programar é insistir no erro até funcionar; cerque o trabalho para ter segurança (0:04:47).
- Programa determinístico de entrada e saída: amarre a validação com golden files e `diff` (0:05:08).
- Prepare o terreno de testes para quando as refatorações se complicarem (0:09:16).

Código, reconstruído; comandos e teste deduzidos do que ele narra:

```bash
echo "A a C c c B b b B" > letras.txt          # conteúdo exato conforme o enunciado
python wordcount.py --count letras.txt > count.txt
python wordcount.py --topcount letras.txt > topcount.txt
diff count.txt <(python wordcount.py --count letras.txt)   # a forma exata do diff não fica clara na transcrição
```

```python
# test_wordcount.py (reconstrução)
import sys
import wordcount


def run(mode, capsys, monkeypatch):
    monkeypatch.setattr(sys, 'argv', ['wordcount.py', mode, 'letras.txt'])
    wordcount.main()
    out, err = capsys.readouterr()
    return out


def test_count(capsys, monkeypatch):
    assert run('--count', capsys, monkeypatch) == 'a 2\nb 4\nc 3\n'   # formato exato incerto


def test_topcount(capsys, monkeypatch):
    assert run('--topcount', capsys, monkeypatch) == 'b 4\nc 3\na 2\n'
```

A transcrição ouve código legal para código legado, pai teste para pytest, frango de teste para framework de teste, irmão que pede para monkeypatch, Czar de v e ar de v para sys.argv, gif para diff.

Paráfrases da legenda (não verificadas):

- para mim o que define um código legado é o seu grau de entropia (0:01:19) [transcrição: código legal]
- antes de sequer ler o código eu tenho que fazer a coisa mais importante do mundo: não me importa o quão fera você seja, quantos PhDs você tem, receber um código tem que executar ele (0:02:19)
- a gente sempre vai errar; programar é insistir no erro até que de repente as coisas funcionam (0:04:47)
- dessa maneira eu consigo cercar o programa por fora do código e criar o que a gente chama de golden file, que é arquivo de ouro (0:06:49)

### Aula #21: Explorando o Ambiente

Vídeo: https://www.youtube.com/watch?v=-Ej-jM9gV8A · 778 s

Reconhecimento do código: mapear o problema para áreas, sem detalhes (0:00:08). Primeira impressão é confusão; muito comentário é cheiro de código pouco expressivo, e para ele comentário é sintoma de código não bom o bastante (0:00:43 a 0:01:24). Começa pela função utilitária compartilhada pelos dois modos e a limpa sem mudar comportamento: remove comentários, critica a prática de pastas `utils` e `helpers` (0:01:49), renomeia o dicionário local `word_count` para `d` e `input_file` para `f` (convenções, escopo interno a uma função bem nomeada; 0:03:36 a 0:04:26), remove o `'r'` do `open` (convenção, não configuração; 0:05:07), alerta para o loop dentro de loop (0:06:05), troca `word` por `w` por falta de contraste com `words` (0:06:42), marca o caso especial com um TODO (0:07:57), defende sempre fechar recursos (0:08:52), e reformata de dois para quatro espaços (0:10:03). Roda os testes a cada passo. Metáfora: não se limpa o terreno inteiro, só a área de trabalho (0:11:38). Observa que não mexeu na interface da função com o exterior (0:12:41).

Linha do tempo:

- [0:00:08] Reconhecimento: mapear o problema para áreas de código, só primeiras impressões.
- [0:00:43] Muito comentário: cheiro de que o código não está expressivo; [0:01:24] comentário é sintoma de código não bom o bastante.
- [0:01:49] Crítica a funções utilitárias e pastas `utils` e `helpers`.
- [0:02:55] Escrever bem: frases com começo, meio e fim; remove comentários que não ajudam.
- [0:03:36] Shift+F6 no PyCharm: renomeia `word_count` para `d`, local à função; [0:04:18] refatoração é contração e expansão; [0:04:26] `input_file` vira `f`, convenção para file handler.
- [0:05:07] Remove o `'r'` do `open`: convenção sobre configuração.
- [0:06:05] Loop dentro de loop: alerta de custo exponencial, mas não é a preocupação agora.
- [0:06:42] `word` e `words` têm pouco contraste; usa `w`.
- [0:07:57] Comentário caso especial vira TODO para resolver depois; [0:08:52] fechar arquivo é requerido: responsabilidade com recursos.
- [0:10:03] Código em dois espaços; reformata para quatro; [0:10:49] refatora passo a passo; roda os testes.
- [0:11:38] Metáfora do terreno cheio de entulho.
- [0:12:13] Recapitulação: contraste, simplicidade, convenções; [0:12:41] não mexeu no nome nem na interface da função.

Princípios enunciados:

- Comece com um reconhecimento: mapear o problema para áreas de código sem entrar em detalhes (0:00:08).
- Muito comentário é cheiro de código pouco expressivo (0:00:48).
- Comentário é sintoma de que o código não é bom o bastante; use com muita moderação e justificativa (0:01:24).
- Nomear algo como `utils` ou `helpers` é se eximir de dar sentido; todo código é útil, e o que não é deve ser removido (0:02:09).
- Escreva bem: frases com começo, meio e fim; a linearidade facilita a compreensão (0:02:55).
- Dentro de uma função bem nomeada, use nomes locais curtos e convencionais (`d`, `f`) (0:03:51).
- Refatorar é contração e expansão o tempo inteiro: simplifica, depois vê o que ficou simples demais (0:04:18).
- Priorize convenção, não configuração; explicitar o padrão ignora a convenção (0:05:14).
- Loop dentro de loop é ponto de alerta: de linear para exponencial (0:06:05).
- Cuidado com palavras de pouco contraste (`word` e `words`); use a primeira letra da coleção para o item iterado (0:06:50).
- Caso especial é problema; evite ao máximo (0:08:03).
- Sempre feche os recursos que o código aloca (0:09:03).
- Refatore passo a passo; não organize tudo antes de começar a trabalhar (0:10:49).
- Arrume a área de trabalho, não o terreno inteiro (0:11:38).
- Mude só o interior da função; não comprometa a interface com o exterior (0:12:41).

Código, reconstruído: estado da função após a limpeza desta aula.

```python
def word_count_dict(filename):
    d = {}
    f = open(filename)
    for line in f:
        words = line.split()
        for w in words:
            w = w.lower()
            # TODO: caso especial
            if w not in d:
                d[w] = 1
            else:
                d[w] += 1
    f.close()
    return d
```

A transcrição ouve pai Charme para PyCharm, Fire rendler e Fire renda para file handler, he-man para rename, em code reformata para o comando de reformatar.

Paráfrases da legenda (não verificadas):

- eu acho que comentário é um sintoma de que o código não é bom o bastante (0:01:24)
- quando você bota alguma coisa como utilitário, coloca numa pastinha utils, helper, você está literalmente se eximindo de dar sentido a esse código (0:02:09) [transcrição: se exibindo]
- é sempre um processo de contração e expansão, contração, expansão, o tempo inteiro assim na refatoração (0:04:18)
- você não vai limpar o terreno todo antes de começar a resolver o seu problema; você tem que pegar a área de trabalho e dar uma arrumada nela (0:11:43)

### Aula #22: Desfiando O Novelo de Lã

Vídeo: https://www.youtube.com/watch?v=jRo6Q04_6qY · 502 s

A percepção de ordem vem de como a sintaxe comunica a semântica; o código deve ser uma sucessão de elementos com uma única responsabilidade, e a sensação de macarrão é vazamento de responsabilidades (0:00:00 a 0:00:19). Lista o que `word_count_dict` faz: abre o arquivo, lê, transforma, conta e fecha, tudo emaranhado (0:00:45). Troca a gestão do recurso por `with open(...) as f`, lê o conteúdo inteiro com `f.read()` e, para manter o algoritmo por linha, `split('\n')`; testes (0:02:23 a 0:03:00). Aplica `lower()` ao conteúdo todo de uma vez e elimina o `lower` por palavra; `content.split()` sem argumento já separa por espaço e quebra de linha, o que elimina um `for` (0:04:07 a 0:04:40). No caso especial, inverte a lógica: se a palavra não está no dicionário, inicializa com zero, e sempre incrementa; uma bifurcação vira etapa de preparação (0:05:17). Tira o algoritmo de dentro do `with`, para o arquivo ficar aberto só durante a leitura (0:06:30). Os blocos passam a refletir a lista inicial (0:06:58). Fecha removendo comentários e escrevendo uma docstring (0:07:51).

Linha do tempo:

- [0:00:00] Ordem vem de como a sintaxe comunica a semântica; elementos de responsabilidade única.
- [0:00:19] Código macarrônico é vazamento de responsabilidades.
- [0:00:45] Lista as responsabilidades: abre, lê, transforma, conta, fecha.
- [0:02:23] `with open(filename) as f`: context manager garante o fechamento.
- [0:03:00] `content = f.read()` e `content.split('\n')` para manter o algoritmo por linha; testes passam (0:03:19).
- [0:04:07] `content = content.lower()` elimina o `lower` por palavra.
- [0:04:40] `words = content.split()` elimina um `for` e um nível de indentação.
- [0:05:17] Caso especial: inversão de lógica, inicializa com zero e sempre incrementa.
- [0:06:30] Traz o algoritmo para fora do `with`; arquivo aberto só durante a leitura.
- [0:06:58] Os blocos refletem a lista: abre, lê, fecha, transforma, conta.
- [0:07:51] Remove comentários e escreve a docstring.

Princípios enunciados:

- O código deve ser uma sucessão de elementos com uma única responsabilidade (0:00:11).
- Sensação de código embolado é vazamento de responsabilidades entrelaçadas (0:00:19).
- Liste o que a função faz antes de mexer; a lista vira o mapa dos blocos (0:00:42).
- Use o context manager (`with`) para gestão de recurso (0:02:33).
- Se uma transformação vale para todos os itens, aplique à coleção toda de uma vez (0:04:02).
- Inverta a lógica para eliminar bifurcação: uma etapa de preparação em vez de caso especial (0:05:39).
- O `with` gerencia o arquivo, não encapsula o algoritmo; mantenha o recurso aberto só o necessário (0:06:32).
- Separar responsabilidades em blocos, mesmo dentro da mesma função, já é componentizar (0:07:28).

Código, reconstruído: estado da função ao fim da aula.

```python
def word_count_dict(filename):
    """Conta as palavras do arquivo.

    Retorna um dicionário com a palavra e a contagem.
    """
    with open(filename) as f:
        content = f.read()
    content = content.lower()
    words = content.split()
    d = {}
    for w in words:
        if w not in d:
            d[w] = 0
        d[w] += 1
    return d
```

A transcrição ouve item para with, contact Manager para context manager, f.uid para f.read, contente para content.

Paráfrases da legenda (não verificadas):

- toda vez que você olha um código e tem a sensação de que ele tá embolado, bem macarrônico, é porque você tá tendo vazamento de responsabilidades (0:00:19)
- com um pouquinho de inversão de lógica a gente consegue eliminar uma bifurcação no meu algoritmo para trabalhar na verdade com uma etapa de preparação (0:05:39)
- organizar o código, refatorar o código, tornar o código componentizável é muito mais sobre essa lógica de identificar quais são as reais etapas que o meu código tá fazendo (0:07:31)

### Aula #23: Cada Macaco No Seu Galho

Vídeo: https://www.youtube.com/watch?v=Uk34ewi98Hs · 623 s

Código organizado revela fronteiras e encaixes; o risco é cuidar de algoritmo e estrutura de dados e esquecer as interfaces (0:00:00). `print_words` e `print_top` têm a mesma entrada e chamam `word_count_dict`, mas uma usa `keys()` e a outra `items()`: problema de interface, que acopla a ordenação à montagem do relatório (0:01:02 a 0:02:37). Como o propósito é contar palavras, a função passa a retornar `d.items()`; `print_words` ordena as duplas e deixa de acessar o dicionário (0:03:21). Remove `get_count` (parametrizava em separado o que deveria estar junto) em favor de `lambda t: t[-1]`, puxa o slice `[:20]` para antes da impressão, uniformiza nomes (0:04:44 a 0:05:55). Último problema: as funções retornam `None`; ele prefere que retornem (0:06:57). Acumula as linhas em uma lista `l`, junta com `'\n'.join`, separa a composição (`out`) do `print`, retorna `out` e move o `print` para `main`, que já cuida da entrada (`argv`) e portanto deve cuidar da saída (0:07:40 a 0:09:50).

Linha do tempo:

- [0:00:00] Código organizado ajuda a reconhecer fronteiras; interfaces encadeiam as partes.
- [0:00:42] `print_words` e `print_top`: mesma entrada, saída no terminal.
- [0:01:02] As duas usam `word_count_dict`, mas uma via `keys()` e outra via `items()`: interface não uniforme.
- [0:02:37] A forma de ordenar está acoplada a como se monta o relatório.
- [0:03:21] `word_count_dict` retorna `items()`; `sorted` sobre duplas; `print_top` deixa de converter; testes passam.
- [0:04:44] Remove `get_count`; `lambda t: t[-1]`.
- [0:05:55] Slice `[:20]` puxado para a definição do conjunto; nomes uniformes `word_count`, `w`, `c`.
- [0:06:57] Último problema de interface: as funções retornam `None`.
- [0:07:40] Lista `l`, `append` de cada linha, `'\n'.join(l)`.
- [0:08:30] Separa a construção da string (`out`) do `print`.
- [0:09:27] `return out`; o `print` vai para `main`.
- [0:09:50] `main` trata a entrada (`argv`), logo trata a saída.

Princípios enunciados:

- Preocupe-se com as interfaces entre as partes, não só com algoritmo, estrutura de dados e modelo do banco (0:00:06).
- Interfaces uniformes: quem consome a mesma função deve se apoiar na mesma estrutura (0:01:49).
- Escolha o tipo de retorno pensando no propósito da função e em quem a chama (0:02:54).
- Não parametrize em separado o que deveria estar junto (0:04:48).
- A definição de qual conjunto se analisa (o slice) fica antes do processo de impressão (0:06:00).
- Funções devem retornar algo; evite funções que só imprimem (0:07:13).
- Imprimir é uma coisa; compor o que vai ser impresso é outra (0:08:40).
- Quem trata a entrada (`main`, `argv`) deve tratar a saída (stdout) (0:09:52).

Código, reconstruído: estado ao fim da aula; direção do `sorted` em `print_top` deduzida do enunciado.

```python
def word_count_dict(filename):
    ...
    return d.items()


def print_words(filename):
    word_count = word_count_dict(filename)
    word_count = sorted(word_count)
    l = []
    for w, c in word_count:
        l.append(f'{w} {c}')
    out = '\n'.join(l)
    return out


def print_top(filename):
    word_count = word_count_dict(filename)
    word_count = sorted(word_count, key=lambda t: t[-1], reverse=True)[:20]
    l = []
    for w, c in word_count:
        l.append(f'{w} {c}')
    out = '\n'.join(l)
    return out


def main():
    ...
    if option == '--count':
        print(print_words(filename))
    elif option == '--topcount':
        print(print_top(filename))
```

A transcrição ouve Kiss para keys, whitens para items, Noni para None, San Andreas de áudio para standard output, xrv para argv.

Paráfrases da legenda (não verificadas):

- é um risco muito grande a gente ficar preocupado com o algoritmo e com estrutura de dados e com o modelo do banco e não se preocupar com as interfaces do nosso código (0:00:06)
- uma função necessariamente retorna alguma coisa; essas duas funções estão retornando None porque não têm return; eu gosto sempre que as funções tenham retorno (0:07:13)
- imprimir é uma coisa, compor o que vai ser impresso é outra coisa (0:08:40)
- a função main é a função que trabalha com a entrada que vem da linha de comando, então naturalmente ela deveria ser responsável por cuidar da saída do programa (0:09:52)

### Aula #24: Componentes Em Toda Parte

Vídeo: https://www.youtube.com/watch?v=6nAUn2bEKbk · 1.105 s

O ponto alto da refatoração: o código começa a falar (0:00:00). Extrai `lines(word_count)` para o trecho duplicado (0:00:40); extrai as estratégias de ordenação `top` e `asc`, e apaga `asc` porque embrulhar o `sorted` do Python é a síndrome de se preparar para o futuro (0:01:32 a 0:02:30). Extrai `word_counter(filename, order)`, injetando a função de ordenação como parâmetro, inversão de dependência (0:03:27 a 0:04:14). Quebra `word_count_dict` em `read`, `split` e `count`, e a apaga (0:04:43). No `main`, o `if` sobre a opção vira um dicionário `{'--count': sorted, '--topcount': top}` dentro de `try/except KeyError`, com acesso por colchetes para explodir se a opção não existir, e um único `print(word_counter(...))` (0:07:55). `count` usa `defaultdict(int)` e perde o `if`; `lines` vira list comprehension; o número mágico 20 vira `limit=20` (0:10:06 a 0:12:32). Externamente o programa ainda não é componente: `cat letras.txt | python wordcount.py --count -` falha (0:13:03). Faz funcionar com `if file == '-': sys.stdin`, extrai `open_file`, o teste quebra até ajustar o chamador, e troca o `if/else` por early return: não é caminho alternativo, é abortar a missão (0:14:33 a 0:17:03). O programa vira componente do sistema operacional (0:18:07).

Linha do tempo:

- [0:00:00] O código chega a um estado em que começa a falar com você; extrações e substituições.
- [0:00:40] Extrai `lines(word_count)` do código duplicado; aplica nos dois lugares; testes.
- [0:01:32] Extrai `top(word_count)` e `asc(word_count)`; [0:02:30] apaga `asc`: síndrome de se preparar para o futuro; `sorted` já é um componente.
- [0:03:27] Extrai `word_counter(filename, order)`, que retorna `lines(order(word_count(filename)))`; [0:04:14] inverteu a dependência injetando a função de ordenação.
- [0:04:43] Extrai `read(filename)` com `return` dentro do `with`, `split(content)` e `count(words)`; apaga `word_count_dict`.
- [0:07:03] Componentes em diversos estágios de abstração; mesma estrutura que o processador executa.
- [0:07:55] `if` do `main` vira dicionário de opções com `try/except KeyError`; `print` unificado.
- [0:10:06] `defaultdict(int)` de `collections` elimina o `if` do `count`; [0:10:46] `lines` vira list comprehension.
- [0:11:58] `word_counter` é componente de componente; cuidado com grãos pequenos demais; [0:12:32] número mágico 20 vira `limit=20`.
- [0:13:03] Externamente não resolvido: pipe do Unix com `-` para stdin falha; [0:14:33] faz funcionar: `if file == '-': sys.stdin`; testes passam; terminal funciona.
- [0:15:35] Extrai `open_file`; o teste explode até adaptar o chamador em `word_counter` (0:16:03); [0:16:47] troca o `if/else` por early return.
- [0:18:07] O programa se torna componente do sistema operacional, usável em shell script.

Princípios enunciados:

- O ponto alto da refatoração é quando o código começa a falar; aí se extrai e substitui (0:00:00).
- Não entre na síndrome de se preparar para o futuro; não embrulhe o que a linguagem já dá (0:02:41).
- Inverta a dependência injetando por parâmetro a função que muda a estratégia (0:04:14).
- Componentes muito simples em diversos estágios de abstração, com cuidado na ordem de execução (0:07:05).
- Mapeamento com `if` vira dicionário; acesso com colchetes para explodir no `KeyError` e tratar (0:08:36).
- Não componentize em grãos pequenos demais; uma função de nível acima articula as menores, para que uma não dependa do conhecimento da de baixo (0:12:05).
- Elimine o número mágico com um parâmetro de valor padrão (0:12:32).
- Antes de discutir qualquer estratégia, faça funcionar (0:14:30).
- Ao criar um componente num nível mais baixo, adapte a hierarquia; por isso cuidado com a repetição (0:16:13).
- Uma entrada e uma saída; o early return é abortar a missão quando não há condição para o propósito, não um caminho alternativo (0:17:03).

Código, reconstruído: forma final do wordcount conforme ele narra; nomes conforme a fala, detalhes de usage e de `reverse` deduzidos.

```python
import sys
from collections import defaultdict


def open_file(file):
    if file == '-':
        return sys.stdin
    return open(file)


def read(file):
    with open_file(file) as f:
        return f.read()


def split(content):
    return content.lower().split()


def count(words):
    d = defaultdict(int)
    for w in words:
        d[w] += 1
    return d.items()


def top(word_count, limit=20):
    return sorted(word_count, key=lambda t: t[-1], reverse=True)[:limit]


def lines(word_count):
    return '\n'.join(f'{w} {c}' for w, c in word_count)


def word_counter(filename, order):
    return lines(order(count(split(read(filename)))))


def main():
    try:
        order = {'--count': sorted, '--topcount': top}[sys.argv[1]]
    except KeyError:
        print('usage: ...')   # mensagem original do esqueleto
        sys.exit(1)
    print(word_counter(sys.argv[2], order))
```

A transcrição ouve Word Counter e Word Carter para word_counter, software para sorted, The vodict e de fogo digno para defaultdict, Eli para early return, x.sdim para sys.stdin, list completion para list comprehension.

Paráfrases da legenda (não verificadas):

- o ponto alto do processo de refatoração é quando você passa por todas as etapas e de repente o código tá num estado tal que ele começa a falar com você (0:00:00)
- a gente entra numa síndrome de vou me preparar para o futuro, quero fazer a coisa mais prontinha para mudar, e a gente acaba fazendo coisa demais (0:02:41)
- eu inverti a dependência injetando uma função que vai impactar na estratégia do algoritmo pela passagem de parâmetros (0:04:14)
- o nome disso é early return, é um retorno antecipado quando não tem a condição para executar o propósito do meu comando (0:17:18) [transcrição: Eli]

### Aula #25: Refatoração Vista Do Alto

Vídeo: https://www.youtube.com/watch?v=ON7Urk5qV_M · 188 s

Recapitulação do bloco wordcount: refatoração é parte intrínseca do trabalho, para entregar valor sem retrabalho (0:00:00 a 0:00:21). O processo começou com testes de caixa preta, para garantir que nada desestabilizaria o paciente (0:00:29); depois legibilidade, arrumar o terreno (0:00:47), separação de responsabilidades no nível do comando da linguagem (0:00:58), consistência das interfaces para dar linearidade (0:01:11), e encapsulamento para que a fragmentação em pequenos componentes não bagunce os níveis superiores (0:01:23). Componentização em múltiplas dimensões, da instrução ao programa como componente do sistema (0:01:32). As etapas são cíclicas; uma coisa de cada vez (0:01:48). Exercício: gravar no Loom de 5 a 10 minutos a análise de um código próprio e postar o link com o repositório (0:02:02).

Linha do tempo:

- [0:00:00] Refatoração é parte intrínseca do trabalho; valor para o cliente sem retrabalho.
- [0:00:29] Recap 1: testes de caixa preta para não desestabilizar o paciente.
- [0:00:47] Recap 2: legibilidade, arrumar o terreno para enxergar o entorno (0:00:51).
- [0:00:58] Recap 3: responsabilidades de cada trecho, no nível do comando da linguagem.
- [0:01:11] Recap 4: consistência das interfaces, linearidade, encaixe sem aparar arestas à força.
- [0:01:23] Recap 5: encapsulamento para a fragmentação não bagunçar os níveis superiores.
- [0:01:32] Componentização em múltiplas dimensões, do micro ao programa como componente do ecossistema.
- [0:01:48] Etapas cíclicas; uma coisa de cada vez.
- [0:02:02] Exercício: gravar no Loom (5 a 10 min) a análise de um código próprio; postar vídeo e repositório.

Princípios enunciados:

- Refatoração é parte intrínseca do trabalho, não tarefa à parte (0:00:21).
- Comece cercando o comportamento com testes de caixa preta (0:00:29).
- Encapsule para que a fragmentação em pequenos componentes não bagunce os níveis superiores (0:01:23).
- As etapas voltam de forma cíclica a cada iteração; faça uma coisa de cada vez (0:01:50).

Código: nenhum nesta aula.

Paráfrases da legenda (não verificadas):

- a refatoração é chave nesse processo, ela é parte intrínseca do nosso trabalho (0:00:21) [transcrição: restauração]
- fizemos um processo para conseguir garantir que seja lá o que a gente faça a gente não vai desestabilizar o paciente (0:00:40)
- é importante sempre fazer uma coisa de cada vez (0:01:52) [a transcrição segue com é a tua pequena na refaturação, provável mis-hearing]

### Aula #26: Veja o Invisível

Vídeo: https://www.youtube.com/watch?v=eogxJkZDGqI · 222 s

Abertura do bloco de planejamento. Falta mostrar o processo de análise: o reconhecimento do terreno que constrói um mapa na cabeça e a partir dele um plano (0:00:00). Planejar é essencial porque não dá para fazer tudo; até aqui o ambiente era controlado, mas no dia a dia o tempo é curto (0:00:26 a 0:00:35). O desafio é descobrir a coisa certa a fazer agora (0:00:55). O risco é se prender a um ideal e, depois de um dia de trabalho, ter que voltar ao que estava (0:00:58). Refatoração exige priorização e precisão sobre a quantidade de passos; do conflito entre o ideal e o possível nascem estratégias intermediárias boas o bastante (0:01:39 a 0:02:08). Pede um passo para trás, foco nas relações entre as partes (0:02:15). Nas próximas aulas analisa códigos e monta um plano para o aluno implementar; a ambição é parar de enxergar código legado e ver oportunidade de melhoria (0:02:30 a 0:02:54). Assistir com caderninho, como programação em par (0:03:16).

Linha do tempo:

- [0:00:00] Falta mostrar o processo de análise: reconhecimento do terreno e mapa mental.
- [0:00:26] Planejar é essencial; não dá para fazer tudo.
- [0:00:35] Até aqui o ambiente era controlado; no dia a dia o tempo é curto.
- [0:00:55] O desafio é descobrir a coisa certa a fazer agora.
- [0:00:58] Risco de se prender a um ideal e ter que voltar atrás depois de um dia.
- [0:01:39] Refatoração exige priorização; precisão sobre a quantidade de passos.
- [0:01:52] Conflito ideal versus possível: padrões e estratégias intermediárias boas o bastante.
- [0:02:15] Dê um passo para trás; foque nas relações entre as partes.
- [0:02:30] Próximas aulas: analisar códigos e montar um plano de refatoração.
- [0:02:54] Parar de enxergar código legado; ver oportunidade de melhoria.
- [0:03:16] Assistir com caderninho, como programação em par; anotar o que ele deixar passar.

Princípios enunciados:

- Planejar é parte essencial da prática: não dá para fazer tudo (0:00:26).
- O desafio é descobrir qual a coisa certa a fazer agora (0:00:55).
- Não se prenda a um ideal de perfeição; o plano precisa caber no tempo e nas restrições (0:00:58).
- Refatoração exige priorização, com precisão sobre o fluxo e a quantidade de passos (0:01:39).
- Entre o ideal e o possível, estratégias intermediárias boas o bastante (0:02:08).
- Dê um passo para trás e foque nas relações entre as partes (0:02:15).
- O objetivo é tornar a mudança mais fácil e o desenvolvimento mais fluido (0:03:05).

Código: nenhum nesta aula.

Paráfrases da legenda (não verificadas):

- não dá para fazer tudo; até aqui a gente sempre estava num ambiente controlado, mas no dia a dia do seu trabalho as coisas são caóticas, o tempo é curto (0:00:35)
- o desafio do jogo é descobrir qual a coisa certa a fazer agora (0:00:55)
- é exatamente nesse conflito entre o ideal, o perfeito, e o possível que a gente começa a reconhecer padrões e montar estratégias intermediárias que já são melhor do que era (0:01:52)
- a partir desse ponto de vista a gente para de enxergar código legado e começa a pegar códigos que têm oportunidade de melhoria (0:02:54)

### Aula #27: Desafio da Matriz Movente

Vídeo: https://www.youtube.com/watch?v=HtXh311XG4o · 289 s

O código a analisar manipula matrizes e foi escrito por alguém começando a programar; ele gosta de código feito pela busca do aprendizado, com afeto (0:00:00 a 0:00:22). A qualidade do código reflete o conhecimento de quem escreve; não se programa o que não se compreende (0:00:51). Primeiro passo: obter e executar, relacionando comportamento com o que se lerá no fonte (0:00:59). Aponta o vídeo do autor e o link do código, que não constam na transcrição (0:01:12). O projeto tem `matriz.py` e `README.md`; o README descreve uma matriz M×N de pixels e comandos de uma letra (I cria, C limpa, L colore um pixel, e outros) e traz sequências de comandos com resultado esperado, que ele usa para orientar a exploração (0:01:31 a 0:02:13). Executa: `I 5 6`, `L 2 3 A`, `S` e `G` dão comando inválido, `V 2 3 4 W` mostra intervalo inclusivo (diferente do Python), `H 3 4 2 Z` tem ordem de parâmetros invertida em relação ao `V` (falta de uniformidade), `F 3 3 J` é preenchimento, `S` falha de novo, `X` sai (0:02:40 a 0:04:38).

Linha do tempo:

- [0:00:00] Código de manipulação de matrizes feito por autor iniciante; afeto pelo código de aprendizado.
- [0:00:51] A qualidade do código reflete o conhecimento; não se programa o que não se compreende.
- [0:00:59] Começar obtendo e executando o código para relacionar comportamento e fonte.
- [0:01:12] Vídeo do autor e link do código; pausar para assistir.
- [0:01:31] Dois arquivos: `matriz.py` e `README.md`.
- [0:01:45] Comandos do README: I cria M×N, C limpa, L colore um pixel, outros.
- [0:02:13] Não precisa entender tudo de primeira; o README traz sequências com resultado esperado.
- [0:02:40] Executa `I 5 6` e `L 2 3 A`; [0:02:59] `S one.bmp` e `G 2 3 J` dão comando inválido.
- [0:03:11] `V 2 3 4 W`: linha vertical com intervalo inclusivo, diferente do Python.
- [0:03:42] `H 3 4 2 Z`: ordem dos parâmetros invertida em relação ao V; falta uniformidade.
- [0:04:18] `F 3 3 J`: algoritmo de preenchimento (fill).
- [0:04:38] `S` falha de novo; `X` sai.

Princípios enunciados:

- A qualidade do código reflete o conhecimento de quem escreve (0:00:51).
- Não é possível programar aquilo que não se compreende (0:00:54).
- Comece obtendo e executando o código para relacionar comportamento e fonte (0:00:59).
- Ao refatorar não é preciso entender tudo de primeira; é preciso rodar (0:02:13).
- Use as sequências de exemplo do README como testes para orientar a exploração (0:02:28).
- Falta de uniformidade entre comandos é ponto de atenção (0:04:12).

Código, reconstruído: sequência de comandos que ele digita, conforme ouvida; nomes de arquivo incertos.

```
I 5 6
L 2 3 A
S one.bmp      (comando inválido)
G 2 3 J        (comando inválido)
V 2 3 4 W
H 3 4 2 Z
F 3 3 J
S ...          (comando inválido)
X
```

Paráfrases da legenda (não verificadas):

- eu pessoalmente gosto muito desse tipo de código que é criado pela busca do aprendizado, com certo afeto inclusive (0:00:22)
- a qualidade do código vai refletir o conhecimento que as pessoas têm; não é possível programar aquilo que você não compreende (0:00:51)
- quando eu tô refatorando um código eu não preciso entender tudo de primeira, mas eu preciso tentar rodar esse cara (0:02:13) [transcrição: ruim fatorar]

### Aula #28: Puxando o Fio da Meada

Vídeo: https://www.youtube.com/watch?v=CkaZH1olYxk · 727 s

Análise de `matriz.py` começando pelo início da execução, o entry point, não pelo início do arquivo (0:00:02). `main` tem `while True`, `try`, chama `read_seq` (que devolve lista de strings) e uma cadeia de `if/elif` sobre `cmd[0]`, passando slices como `cmd[1:3]` e `cmd[1:4]`: `main` conhece os detalhes de cada comando (0:00:33 a 0:01:17). Anota TODOs em vez de mexer: substituir o `if` por mapeamento com dicionário (0:02:13); encapsular os detalhes do comando (0:03:25); `board` pode ser usado antes de definido (L antes de I), extrair sua definição para o início (0:03:56); as funções recebem e retornam `board` (implementação procedural), verificar se `board` deveria ser instância de uma classe (0:04:35); o `F` converte para inteiro e subtrai um, ou seja, `main` conhece índices base 1 dos comandos e base 0 do board, encapsular a conversão (0:05:29 a 0:06:29); o `S` falha em silêncio por um `except` genérico, especificar as exceções (0:06:59); a validação de comando escapa de `main` e precisa migrar para `read_seq` (0:08:16); o `else: continue` é furo na validação (0:09:01); `print_board` deveria devolver o board como string (0:09:49); entrada e saída o mais fora possível para facilitar teste (0:10:59). `main` tem três coisas: entrada, saída e dispatch (0:11:55).

Linha do tempo:

- [0:00:02] Começar pelo entry point, não pelo início do arquivo.
- [0:00:33] `main`: `while True`, `try`, `read_seq` retorna lista de strings.
- [0:01:17] Cadeia de `if/elif` sobre `cmd[0]`; slices `cmd[1:3]` e `cmd[1:4]` vazam detalhes do comando.
- [0:02:13] TODO: substituir o `if` por mapeamento com dicionário; [0:03:25] TODO: encapsular os detalhes do comando sem vazar para `main`.
- [0:03:56] `board` pode não estar definido se L vier antes de I; TODO extrair a definição para o início.
- [0:04:35] Funções recebem e retornam `board`: procedural; TODO verificar se `board` deveria ser instância de classe.
- [0:05:29] `F` pré-processa (int, menos um): `main` conhece duas naturezas de índice; [0:06:29] TODO: encapsular a conversão de índices do board.
- [0:06:59] `S` falha em silêncio; `except` genérico camufla o erro; TODO especificar exceções.
- [0:08:16] Validação de comando escapa de `main`; TODO isolar em `read_seq`; [0:09:01] `else: continue` é furo na validação; imprime o board sem alteração.
- [0:09:49] `print_board` deveria ser board como string; usar o `print` do Python.
- [0:10:59] Entrada e saída o mais fora possível, até para facilitar o teste; `main` em loop é difícil de testar.
- [0:11:55] `main` tem três coisas: entrada, saída e o dispatch.

Princípios enunciados:

- Comece a análise pelo início da execução (entry point), não pelo início do arquivo (0:00:04).
- O chamador não deve conhecer os detalhes do comando nem da função ativada; encapsule (0:02:07).
- Mapeamento com `if/elif` vira dicionário de chave para objeto executável (0:02:23).
- Funções que todas recebem e retornam a mesma estrutura sugerem uma classe (0:05:06).
- Quem conhece duas naturezas de índice está fazendo meio de campo; encapsule a conversão (0:05:41).
- Evite `except` genérico: camufla o erro e tira a capacidade de depurar (0:07:25).
- Função que imprime deveria devolver a representação string; o `print` fica com o Python (0:09:56).
- Mantenha o tratamento de entrada e saída o mais fora possível do código, até para facilitar o teste (0:11:01).

Código, reconstruído: TODOs anotados no fonte, conforme ditados.

```
TODO substituir o uso do if por um mapeamento com dicionário
TODO encapsular os detalhes do comando sem vazar para o main
TODO extrair a definição do board para o início do processamento
TODO verificar a possibilidade do board ser instância de uma classe
TODO encapsular a conversão de índices do board
TODO especificar as exceptions que serão tratadas
TODO verificar como isolar a validação do comando no read_seq
TODO remover o else quando a validação do comando for encapsulada no read_seq
TODO extrair o print do print_board
```

A transcrição ouve entre Point para entry point, it Seconds, Red Seconds e Secrets para read_seq, Will para while, hitlers para read_seq (provável), dedurar para depurar, the Burger para debugger.

Paráfrases da legenda (não verificadas):

- não é do início do arquivo, é do início da execução do programa; vamos encontrar o entry point (0:00:04)
- significa que a função main tá tendo que conhecer os detalhes do comando e os detalhes da função que é ativada a partir do comando; o ideal é a gente conseguir encapsular (0:02:01)
- é muito importante evitar utilizar except genérico porque isso camufla no processo de mudança do código, camufla a nossa capacidade de depurar o código (0:07:25) [transcrição: dedurar]
- eu gosto sempre de manter o tratamento de entrada e saída o mais fora possível do meu código, até para facilitar o teste (0:11:01)

### Aula #29: Separação de Entrada e Saída

Vídeo: https://www.youtube.com/watch?v=S0tmxA9q9wk · 602 s

Continua pelas beiradas: `read_seq` e `print_board`. `read_seq` está fisicamente longe de `main`; TODO mover (0:00:18). O comentário que explica a função vira docstring (0:00:40). `char_valid` é nome ruim (são os comandos válidos) e tem parênteses desnecessários (0:00:55); `sqc` e `read_seq` nomeiam pela sequência, quando o que se lê é um comando (`read_command`, `cmd`; 0:01:29). O `input()` devolve string, mas depois do `split` a variável é lista: separar a obtenção do comando do tratamento (0:02:33). A validação percorre `char_valid` comparando o primeiro caractere; se inválido imprime mas retorna mesmo assim, e quem segura é o `else: continue` do `main`: funciona por coincidência, frágil (0:03:34 a 0:04:10). `read_seq` tem dois papéis (garantir um comando válido no loop e validar) e deve separá-los (0:04:24); unificar o que estava espalhado liberta o programa da prisão daquele `except` para comando inválido e abre o território (0:05:27 a 0:05:42); o `and not` parece redundante (0:05:50); dois `return` viram um (0:06:26). Validação separada é testável, e pode ser conversão: um parser que devolve um objeto comando em vez de lista de strings (0:06:44 a 0:06:58). `print_board` está cheio de `print`; deveria ser board como string (`__str__` se for classe), e como depende da estrutura interna do board (`for row in board`, `join`), deveria ser método da classe (0:07:54 a 0:09:10).

Linha do tempo:

- [0:00:18] `read_seq` fisicamente distante de `main`; TODO mover para perto; [0:00:40] TODO mover o comentário para uma docstring.
- [0:00:55] `char_valid`: nome ruim; remover parênteses desnecessários.
- [0:01:29] `input()` guardado em `sqc`; `read_seq` e `sqc` são nomes ruins; sugere `read_command` e `cmd`.
- [0:02:33] `upper` e `split`: separar a obtenção do comando do tratamento.
- [0:03:34] Loop de validação sobre o primeiro caractere; comando inválido imprime mas retorna.
- [0:04:10] Funciona por coincidência com o `else/continue` do `main`: frágil.
- [0:04:24] `read_seq` tem dois papéis; TODO separar: garantir comando válido e validar o comando; [0:05:27] consolidar liberta da prisão do `except` e permite depurar com tracebacks válidos.
- [0:05:50] `and not` não quer dizer muita coisa; TODO verificar a necessidade.
- [0:06:26] Dois `return`; TODO um único `return`.
- [0:06:44] Validação separada vira testável; [0:06:58] validação pode ser de conversão; TODO verificar um parser único que devolve objeto comando.
- [0:07:54] `print_board`: cheio de `print`; docstring; extrair o `print` (0:08:21); board como string (0:08:27); `__str__`.
- [0:09:10] `print_board` conhece a estrutura interna do board; deveria ser método da classe.

Princípios enunciados:

- Mantenha fisicamente próximas as funções que trabalham juntas (0:00:28).
- Comentário que explica a função vira docstring (0:00:43).
- Nomeie pelo que a função faz (ler o comando), não por um detalhe (sequência) (0:01:54).
- Separe a obtenção da entrada do tratamento e validação da entrada (0:03:14).
- Comportamento que funciona por coincidência entre duas funções é frágil; consolide (0:04:19).
- Consolidar a validação liberta o programa do `except` genérico e devolve os tracebacks (0:05:30).
- Verifique expressões lógicas redundantes (`and not`) e remova (0:05:50).
- Um único `return` (0:06:29).
- Separar a validação do loop torna a validação testável (0:06:44).
- Validação pode ser conversão: um parser que devolve um objeto comando em vez de lista de strings (0:07:04).
- Quem depende da estrutura interna de um dado deveria ser método dele (0:09:47).

Código, reconstruído: TODOs anotados, conforme ditados.

```
TODO mover read_seq para próximo do main
TODO mover o comentário para uma docstring
TODO melhorar o nome char_valid para algo mais semântico
TODO remover os parênteses desnecessários
TODO melhorar o nome read_seq, pois na verdade ela lê o comando
TODO melhorar o nome sqc; sugestão cmd
TODO separar a obtenção do comando do tratamento do comando
TODO separar as responsabilidades do read_seq: garantir a estrutura de um comando válido; validar o comando em si
TODO verificar a real necessidade desse and not
TODO implementar um único return
TODO verificar se faz sentido ter um parser único para o comando validado, eliminando a lista de strings
TODO (print_board) mover o comentário para docstring
TODO extrair o print do print_board
TODO print_board deveria ser "board como string"; caso o board seja instância de classe, implementar __str__
```

A transcrição ouve 25 e Ride Seconds para read_seq, charvale e Carvalho para char_valid, dandere STR para dunder str, Elvis e Elson para else.

Paráfrases da legenda (não verificadas):

- separar a obtenção do comando do tratamento do comando (0:03:14)
- isso tá meio que funcionando por coincidência, tá muito frágil (0:04:19)
- uma pequena mudança, coisa que estava espalhada em dois lugares, quando você unifica, como é que isso abre para você o território (0:05:42)
- o fato de você depender de conhecer a estrutura interna do board já sugere que isso poderia ser um método da classe board (0:09:47)

### Aula #30: Organização Potencializa a Composição

Vídeo: https://www.youtube.com/watch?v=z_-c2oyGxIQ · 1.295 s

Análise das funções de comando. `create_array`: docstring com os parâmetros esperados (0:00:18); expandir o argumento `cmd` em parâmetros nomeados, já que a função faz `col, line = cmd` por dentro; os valores deveriam chegar convertidos pelo validador (`width`, `height`); renomear `x`; list comprehension; o nome deveria falar de board, provavelmente o `__init__` (0:00:14 a 0:02:38). `clean_array`: docstring, renomear, e o fato de recalcular `len` a toda hora sugere um objeto que guarde as dimensões; remover o zero do `range` (0:03:48). `color_pixel` faz conversão para inteiro e de índice base 1 para base 0, o que aparece em toda parte: pede um objeto Coordenada ou Célula que resolva isso num único ponto, `board[Coordenada(1, 2)] = color` (0:05:37 a 0:07:55). `v_pixel` e `h_pixel` são linhas vertical e horizontal; alinhar nomes com `range` (`start`, `stop`); `c` é nome ruim; computar as coordenadas e passá-las a um método do board que atribui valor a múltiplas coordenadas, porque o que se quer é mudar o estado do board; uniformizar as assinaturas, que são o mesmo método com rotação (0:09:05 a 0:13:24). `block_pixel` é uma região retangular, e as linhas são regiões de uma coluna ou de uma linha: os três comandos viram um só algoritmo, um range de coordenadas (0:15:39 a 0:17:58). A composição Board, Coordenada, Região evita entulhar algoritmos dentro da classe (0:18:46). Tudo isso só analisando, sem mexer (0:21:01).

Linha do tempo:

- [0:00:14] `create_array`: TODO docstring explicando os parâmetros; expandir `cmd` nas partes.
- [0:01:13] `board` é lista de listas; os parâmetros deveriam chegar convertidos (`width`, `height`).
- [0:02:38] Renomear `x`; trocar o `for` por list comprehension; renomear `create_array` para algo do board (`__init__`).
- [0:03:48] `clean_array`: docstring; renomear; recalcular `len` a toda hora sugere objeto; remover o zero do `range`.
- [0:05:37] `color_pixel` acessa detalhe de implementação do board; precisa de uma camada.
- [0:06:30] Conversão int e de base 1 para base 0: objeto Coordenada ou Célula; [0:07:55] exemplo: `board[Coordenada(1, 2)] = color` resolvido num dunder.
- [0:08:51] Renomear `color_pixel` para `color`.
- [0:09:05] `v_pixel` é `vertical_line`; `start` e `stop` como no `range`; `c` é nome ruim.
- [0:11:44] Computar as coordenadas e passá-las a um método do board que atribui a múltiplas.
- [0:13:24] `h_pixel`: mesma natureza com rotação; uniformizar as assinaturas.
- [0:15:39] `block_pixel` é uma região retangular; as linhas também são regiões; [0:17:58] um range de coordenadas; `block_pixel` vira uma linha de código.
- [0:18:46] Composição Board, Coordenada, Região; não entulhar a classe; [0:21:01] a análise, sem mexer, revela um desenho possível.

Princípios enunciados:

- A docstring de um comando explica os parâmetros que ele espera (0:00:22).
- Expanda o argumento genérico (`cmd`) nas partes nomeadas, já na assinatura (0:00:52).
- O validador de comandos entrega os parâmetros já no tipo certo (0:02:05).
- Busque sempre representações de mais alto nível que array e lista (0:04:14).
- Recomputar `len` a toda hora é sinal de estrutura de baixo nível; um objeto guardaria as dimensões (0:04:35).
- Conversão de índice espalhada pede um objeto que a resolva num único ponto, no nível de negócio (0:06:42).
- Alinhe nomes de parâmetros com as convenções da linguagem (`range`: `start`, `stop`) (0:10:17).
- Você quer mudar o estado do board, não acessar coordenada por coordenada (0:13:08).
- Uniformize as assinaturas de comandos da mesma natureza (0:14:11).
- Algoritmos de natureza parecida revelam uma estrutura única (0:17:25).
- Componha abstrações maiores; não entulhe algoritmos na classe; algoritmos usam a interface da estrutura (0:18:46).
- A análise, sem mexer no código, revela o desenho; você escolhe quanto implementar (0:21:12).

Código, reconstruído: o esboço que ele descreve em voz alta, não digitado.

```python
board[Coordenada(1, 2)] = color            # dunder converte índice base 1 em base 0
board.set_many(Regiao(Coordenada(2, 3), Coordenada(2, 4)), color)   # nome a definir; "um set que define múltiplos itens"
```

```
TODO (create_array) mover o comentário para uma docstring
TODO expandir o argumento cmd para contemplar as partes
TODO idealmente col e line já deveriam chegar como inteiros (width, height)
TODO renomear x para algo mais semântico
TODO trocar o for por uma list comprehension
TODO mudar o nome create_array para algo ligado ao board
TODO (clean_array) renomear clean_array; extrair len(board) e len(board[0]) para variáveis; remover o zero do range
TODO (color_pixel) expandir cmd em parâmetros; receber os parâmetros já no tipo correto
TODO verificar se faz sentido um objeto coordenada/célula que encapsule a conversão de índices
TODO renomear color_pixel para color
TODO (v_pixel) renomear para vertical_line; alinhar variáveis com o range (start, stop); c é um nome ruim; renomear v para line
TODO computar as coordenadas e passá-las para um método do board que atribui valor a múltiplas coordenadas
TODO (h_pixel) idem; verificar se é possível uniformizar a assinatura de v_pixel e h_pixel
TODO (block_pixel) melhorar o nome (region); alinhar nomes com o range; simplificar com as abstrações coordenada, região e board
```

A transcrição ouve crateray e Create a Ray para create_array, Cleaner Ray para clean_array, cool para col, Rangel para range, rean e ridian para region, Borja para board.

Paráfrases da legenda (não verificadas):

- a gente precisa estar sempre buscando representações mais alto nível para o nosso código (0:04:14)
- eu preciso de um objeto coordenada, célula, você escolhe o nome, mas alguém que expresse no nível de negócio (0:06:42)
- a gente não quer acessar a coordenada ou definir a coordenada, a gente quer mudar o estado do board (0:13:08)
- eu não preciso pegar os meus algoritmos e entulhar dentro da minha classe; eu posso fazer algoritmos que usam as interfaces dessa estrutura de dados (0:19:38)
- a gente está só fazendo uma análise e essa análise tá naturalmente revelando um desenho possível de código (0:21:12)

### Aula #31: Boas Estruturas Ajudam Bons Algorítimos

Vídeo: https://www.youtube.com/watch?v=h9e5jU1wZ50 · 953 s

Quando se identifica uma estrutura de dados com seu comportamento, dá para compor algoritmos sobre ela; o fill é um caso (0:00:01). `out_range(board, y, x)` recebe `y, x` por causa da estrutura linhas e colunas: ajustar para a lógica de par ordenado; docstring; nome preso ao detalhe de lista; poderia ser o `__contains__` (`Coordenada(x, y) in board`); `line` e `col` são `width` e `height`, propriedades se for objeto; `if/else` que devolve `True` e `False` vira `return` da expressão; comparações ricas `0 <= x < width`; e a lógica está invertida em relação ao nome (0:00:17 a 0:03:34). `fill_pixel`: expandir `cmd`; guarda a cor original e visita vizinhos recursivamente; renomear para `fill`; `color` é a cor original; o algoritmo não deveria conhecer a implementação do board, por analogia com a lista do Python, cuja implementação não se conhece; inverter o teste para condição de parada no início; `chg_color` nome ruim; a repetição dos quatro vizinhos varia só na coordenada: computar os vizinhos e chamar em loop, com o teste de elegibilidade extraído; algoritmo genérico (ortogonal ou diagonal), função ou classe independente, não entulhado no Board (0:04:31 a 0:12:17). `save_array`: reutilizar a representação string do board, renomear `save`, `name` é `filename`, remover o `lower` (escolha do cliente), `my_file` vira `f` (0:13:19).

Linha do tempo:

- [0:00:17] `out_range(board, y, x)`: ordem `y, x` reflete linhas e colunas; [0:00:58] TODO ajustar a ordem para par ordenado; docstring; renomear (preso ao detalhe lista).
- [0:01:33] TODO verificar se vira `__contains__`: `coordenada in board`.
- [0:02:11] Renomear para `width` e `height`; como objeto, propriedades.
- [0:02:37] `if/else` com expressão lógica: retornar a expressão; [0:03:00] comparações ricas: `0 <= x < width`.
- [0:03:34] Lógica invertida em relação ao nome `out_range`; TODO alinhar.
- [0:04:31] `fill_pixel`: expandir `cmd`; guarda a cor original; visita vizinhos recursivamente.
- [0:06:32] Renomear para `fill`; `color` é a cor original ou anterior.
- [0:07:18] O algoritmo não deve conhecer a implementação do board; analogia com `list`.
- [0:08:18] Inverter: se fora, parar; condição de parada no início.
- [0:09:20] Repetição clássica: só a coordenada varia; computar os quatro vizinhos e chamar em loop.
- [0:12:17] Fill como algoritmo genérico (ortogonal, diagonal); não entulhar na classe board.
- [0:13:19] `save_array`: reutilizar board como string; renomear `save`; `filename`; remover `lower`; `my_file` vira `f`.

Princípios enunciados:

- Respeite a lógica de par ordenado (x, y) na ordem dos argumentos (0:00:58).
- Use os protocolos da linguagem (dunder `contains`) quando expressam a ideia (0:01:33).
- Retorne o resultado da expressão lógica em vez de `if/else` com `True` e `False` (0:02:47).
- Use comparações ricas (`0 <= x < width`) (0:03:00).
- Alinhe a lógica do retorno com o nome da função (0:04:14).
- Um algoritmo opera sobre uma estrutura de dados pela interface, sem conhecer os detalhes internos (0:07:34).
- Inverta a condição para virar condição de parada no início (0:08:31).
- Extraia o que varia; o que fica igual se repete em loop (0:10:19).
- Não sucumba à tentação de entulhar o algoritmo na classe; pode ser função ou classe independente (0:12:54).
- Reaproveite a representação string para persistir (0:14:27).
- Não force `lower` no nome do arquivo: é escolha do cliente (0:14:46).
- `f` para o arquivo manipulado num ponto só, padrão em código Python (0:15:13).

Código, reconstruído: o esboço que ele descreve.

```python
# a função de pertencimento, como ele a descreve
def contains(board, x, y):
    return 0 <= x < width and 0 <= y < height   # ou __contains__ em Board


# a essência do fill, como ele a descreve: vizinhos computados antes, chamada em loop
for neighbour in neighbours(coordenada):
    if eligible(neighbour, original_color):
        fill(board, neighbour, new_color)
```

```
TODO (out_range) ajustar a ordem de argumentos para respeitar a lógica de um par ordenado
TODO mover o comentário para docstring
TODO melhorar o nome out_range, preso ao detalhe de implementação com lista
TODO verificar se essa função não poderia ser substituída pelo dunder contains
TODO renomear para width e height
TODO retornar o resultado da expressão lógica
TODO utilizar comparações ricas
TODO alinhar a lógica do retorno com o nome da função
TODO (fill_pixel) melhorar o nome, apenas fill; expandir cmd para os parâmetros com os tipos corretos; docstring
TODO melhorar o nome da variável color para enfatizar que é a cor original/anterior
TODO fill_pixel não deveria conhecer os detalhes de implementação do board
TODO inverter a lógica para parar caso esteja fora
TODO melhorar o nome chg_color
TODO trazer o teste da cor para junto do out_range com um and
TODO extrair a coordenada para variáveis auxiliares
TODO computar as coordenadas dos vizinhos antes e chamá-las em um loop
TODO encapsular o teste do vizinho em uma pequena função auxiliar
TODO (save_array) mover o comentário para docstring; melhorar o nome (save); melhorar o nome do parâmetro name (filename)
TODO utilizar a mesma lógica do board como string para persistir no arquivo texto
TODO remover o lower
TODO melhorar my_file para f
```

A transcrição ouve outlet, Alt Range e altrend para out_range, thunder contém para dunder contains, Witch e right para width e height, fio Pixel e fios para fill_pixel e fill, savery para save_array.

Paráfrases da legenda (não verificadas):

- uma das coisas interessantes na refatoração é quando você consegue identificar uma estrutura de dados com todo o seu comportamento e consegue compor essa estrutura com algoritmos que trabalham nela (0:00:01)
- é um algoritmo que opera sobre uma estrutura de dados; você não sabe como a lista do Python é implementada no detalhe, você tem apenas uma interface que permite acessar os recursos dela (0:07:34)
- o que varia em todas essas linhas de código, apenas uma coisa varia, que é a coordenada (0:10:10)
- a gente não precisa sucumbir à tentação, que sempre costuma acontecer, de pegar o algoritmo de fill e entulhar ele dentro da classe board (0:12:54)

### Aula #32: A Moral da História

Vídeo: https://www.youtube.com/watch?v=VSnuUsCHMos · 282 s

Refatorar não é sair aplicando padrões; é entender o código e o terreno, construindo um mapa fiel, e entender a equipe (0:00:00). O que ele fez foi uma dinâmica de code review (0:00:45). Os comentários `TODO` são reconhecidos pelo PyCharm e viram uma lista de tarefas: 84 melhorias possíveis em um único arquivo (0:00:57). São sugestões, não obrigações: a propriedade do código é da equipe que cuida dele, não de quem escreve; a sugestão provoca diálogo sobre o porquê, e as decisões são tomadas em equipe, mesmo quando ele é o líder (0:01:20 a 0:02:09). Alguns comentários beiram a preferência, e é difícil separar o estrutural do estético, mas legibilidade conta (0:02:29 a 0:02:52). A ferramenta não importa; importa o cuidado na interação (0:03:16). Separar os momentos: primeiro listar (muito mais rápido que fazer), depois escolher o que executar e, principalmente, o que não fazer, para não cair no loop infinito nem em discussões do sexo dos anjos (0:03:33 a 0:04:13).

Linha do tempo:

- [0:00:00] Refatorar não é aplicar padrões; é entender o terreno e a equipe.
- [0:00:45] O processo foi literalmente um code review.
- [0:00:57] `TODO` reconhecido pelo PyCharm vira lista de tarefas: 84 melhorias.
- [0:01:20] 84 sugestões, não obrigações; propriedade coletiva do código (0:01:40).
- [0:02:09] Provocar o diálogo sobre o porquê; decisões em equipe.
- [0:02:29] Alguns comentários beiram a preferência; difícil separar estrutural de estético.
- [0:02:52] Legibilidade conta: passamos parte do tempo lendo código.
- [0:03:16] A ferramenta de review não importa; importa o cuidado com os colegas.
- [0:03:33] Separar os momentos: listar é muito mais rápido que fazer.
- [0:03:49] Fazer gera novas questões: loop infinito, sexo dos anjos (0:04:06).
- [0:04:13] Primeiro listar, depois escolher o que executar e o que não fazer.

Princípios enunciados:

- Refatorar é entender o código e o terreno, construindo um mapa fiel, não aplicar padrões (0:00:07).
- Melhorias listadas são sugestões, não definições nem obrigações (0:01:20).
- A propriedade do código é da equipe que cuida dele, não de quem escreve (0:01:30).
- Sugestões provocam diálogo sobre o porquê; não são imposição, mesmo vindas do líder (0:02:09).
- Legibilidade conta: passamos parte do tempo de programação lendo código (0:02:52).
- Separe o momento de listar do momento de fazer; listar é mais rápido (0:03:39).
- Escolha o que executar e, principalmente, o que não fazer (0:04:28).

Código: nenhum nesta aula; menciona a lista de 84 `TODO`s no arquivo.

Paráfrases da legenda (não verificadas):

- é literalmente uma dinâmica de code review onde eu fiz uma revisão do código para encontrar oportunidade de melhoria (0:00:45) [transcrição: couro review]
- a propriedade do código não é de quem escreve, mas sim daquela equipe que trabalha nele, de quem cuida para que aquele sistema continue funcionando (0:01:30)
- é muito mais rápido listar do que fazer (0:03:39) [transcrição: ele está]
- em nenhum momento eu posso me dar o luxo de escorregar e cair para discussões do sexo dos anjos (0:04:03)

### Aula #33: Tem Mais Uma Coisa...

Vídeo: https://www.youtube.com/watch?v=aDHZwVoyfMs · 35 s

Encerramento curto: o aluno tem 84 tarefas para implementar (0:00:00). Ele deixa na descrição o link do fork que fez do projeto da matriz, com as anotações; o link não aparece na transcrição (0:00:06). A prática é implementar cada tarefa e, para o que não concordar, comentar o que não quer fazer e por quê, o que sedimenta a dinâmica de melhoria e desenvolve a priorização (0:00:13 a 0:00:27).

Linha do tempo:

- [0:00:00] Não acabou: 84 tarefas para implementar.
- [0:00:06] Link para o fork do projeto no repositório dele, com as mudanças.
- [0:00:13] Implementar cada tarefa; comentar o que não concorda e por quê.
- [0:00:27] Isso desenvolve a priorização.

Princípios enunciados:

- Comentar o que você não concorda, e por quê, sedimenta a melhoria de código e a priorização (0:00:18).

Código: nenhum. O repositório do fork é dele, mas a URL não consta na transcrição.

Paráfrases da legenda (não verificadas):

- eu tô colocando aqui embaixo o link para o meu repositório que eu fiz o fork desse projeto (0:00:06) [transcrição: forte]
- você pegar esse código, implementar cada uma dessas tarefas, e aquilo que você não concordar é muito bacana também você comentar o que você não quer fazer e por que (0:00:13)

### Aula #34: (sem título)

Vídeo: https://www.youtube.com/watch?v=4ZOhCPTWrS0 · duração desconhecida (`null` em `playlist.json`)

Sem transcrição: não existe `34-4ZOhCPTWrS0.md` em `sources/transcripts/refatoracao-na-pratica/`, e o `playlist.json` traz título e duração nulos para o índice 34. Nada a resumir, nenhuma citação, nenhum princípio.

## 6. Princípios que atravessam toda a série

Quinze regras que ele formula na fala, consolidadas a partir dos 52 princípios candidatos dos dois passes por aula. Nenhuma é inferência deste documento; cada uma traz as aulas e os timestamps onde é dita. A linha entre colchetes diz se a regra já existe em `kb/principles/` (ids de `kb/INDEX.md`) ou é nova.

#### 1. Refatorar é mudar a estrutura, não o comportamento

Refatorar é melhorar a estrutura interna do código sem mudar o comportamento com o mundo exterior, e nem toda mudança com intenção de melhorar é refatoração (aula #02, 0:00:13 e 0:00:31); reescrever tudo não é refatorar (aula #02, 0:02:02). Corrigir um bug durante a refatoração viola o princípio, porque quando se refatora nada muda, só o arranjo (aula #03, 0:03:24 e 0:05:09). Um parâmetro com valor padrão preserva o comportamento externo e por isso a mudança continua sendo refatoração (aula #14, 0:02:28). A refatoração é parte intrínseca do trabalho, não tarefa à parte (aula #25, 0:00:21).

[novo]

#### 2. Nunca refatore código instável: execute, cerque com testes, rode a cada passo

Não se refatora sistema instável (aula #02, 0:05:42); achou bug, para, volta, conserta e estabiliza (aula #03, 0:03:01); sem testes passando não se começa (aula #06, 0:01:02). Antes de sequer ler um código recebido, execute-o (aula #20, 0:02:17; aula #27, 0:00:59). Programa determinístico de entrada e saída se cerca por fora com golden files e `diff`, depois com pytest (aula #20, 0:05:08 e 0:06:49), e o bloco inteiro começa com testes de caixa preta para não desestabilizar o paciente (aula #25, 0:00:29). Toda pequena mudança é seguida dos testes, inclusive só de estilo (aula #06, 0:05:44; aula #08, 0:01:28; aula #21, 0:10:49 e 0:11:28; aula #22, 0:03:19; aula #24, 0:16:03), e antes de extrair um conceito ele escreve o teste, que pega até erro de digitação (aula #16, 0:02:12 e 0:03:59). Os chapéus de implementar, refatorar e otimizar são momentos distintos (aula #03, 0:04:52), mas fazer funcionar, fazer direito e fazer rápido acontecem no mesmo fluxo com escopo reduzido, que intensifica o feedback (aula #19, 0:00:14, 0:00:26 e 0:00:50); antes de discutir estratégia, faça funcionar (aula #24, 0:14:30).

[novo; vizinho de teste-primeiro-das-folhas, que é sobre escrever código novo, não sobre cercar código existente]

#### 3. A decisão é econômica e contextual, não estética

Qualidade ninguém define; a decisão precisa ser econômica, vinculada ao desempenho da equipe, porque a única certeza é que o software vai mudar (aula #02, 0:02:48, 0:03:27 e 0:03:43). Refatore quando precisar acolher uma mudança, priorize o que muda com frequência e não refatore só por estética em contexto profissional (aula #03, 0:01:12, 0:01:40 e 0:02:37); o atraso vira custo exponencial e o crescimento é um ciclo de expansão, acomodação e consolidação (aula #03, 0:06:29 e 0:10:14). Até onde ir considera a experiência da equipe, culturas diferentes e o domínio local, não só o código (aula #02, 0:07:51; aula #12, 0:02:24, 0:02:47 e 0:03:30; aula #15, 0:02:25), e a relação econômica com a sustentabilidade do projeto reabre a aula de componentes (aula #17, 0:00:11). Alguns comentários de review beiram a preferência, e é difícil separar o estrutural do estético, mas legibilidade conta (aula #32, 0:02:29 e 0:02:52).

[ja no KB: pragmatismo-sobre-pureza]

#### 4. Não decore; o repertório vem da prática e da reflexão sobre ela

Nada para decorar; sensibilidade para o implícito (aula #01, 0:01:14; aula #18, 0:00:13). Não se aprende refatoração só lendo, boas práticas não são regras, e a explosão combinatória impede mapear tudo: o repertório da prática é o que decide (aula #02, 0:06:58, 0:07:12, 0:08:03 e 0:09:07). A estratégia é prática mais reflexão sobre a prática, programando em terceira pessoa e registrando a reflexão (aula #04, 0:01:52, 0:02:06 e 0:02:15). Componentes não vêm de regra, emergem do contexto (aula #17, 0:03:24 e 0:14:04), e refatorar é entender o código e o terreno construindo um mapa fiel, não aplicar padrões (aula #32, 0:00:07). Pensar fora da caixa é reconfigurar a saliência, e a prática com cenários concretos é o que permite isso (aula #03, 0:00:16).

[novo]

#### 5. O código expressa o domínio, e os nomes vêm dele

A primeira coisa a observar é a relação do código com o domínio do problema; quando o código expressa o problema de um jeito distinto do entendido, é um alerta; valide o entendimento e expresse muito bem o problema (aula #06, 0:02:37, 0:03:53, 0:04:46 e 0:05:07). Nomeie em função do domínio, não da implementação; bons nomes expressam um conceito de mais alto nível; não economize nos nomes (aula #10, 0:00:40, 0:00:49 e 0:01:59; aula #14, 0:00:34). Dentro de uma função bem nomeada, nomes locais curtos e convencionais; cuidado com palavras de pouco contraste (aula #21, 0:03:51 e 0:06:50); nomeie pelo que a função faz, alinhe a lógica com o nome e os parâmetros com as convenções da linguagem (aula #29, 0:01:54; aula #30, 0:10:17; aula #31, 0:04:14). Muito comentário é cheiro de código pouco expressivo; o comentário que explica a função vira docstring (aula #21, 0:00:48 e 0:01:24; aula #29, 0:00:43; aula #30, 0:00:18 e 0:00:22).

[parcialmente no KB: o-codigo-e-a-interface cobre os nomes como artefato de design; a verificação do entendimento do domínio antes de qualquer refatoração é nova]

#### 6. Código linear: uma entrada, uma saída, sem caso especial

Mantenha o código o mais linear, direto e sequencial possível; precisar de um branch não obriga a dois pontos de retorno; entra por uma porta e sai por outra (aula #07, 0:02:00, 0:02:15, 0:03:42 e 0:05:46). Entrada, processamento e saída separados, e a divisão é fractal, valendo dentro da função (aula #07, 0:04:39; aula #09, 0:02:44; aula #11, 0:01:33). Caso especial é problema; inverta a lógica para virar etapa de preparação ou condição de parada no início (aula #21, 0:08:03; aula #22, 0:05:39; aula #31, 0:08:31); o early return é abortar a missão, não um caminho alternativo (aula #24, 0:17:03); um único `return` (aula #29, 0:06:29). Comece a análise pelo entry point e siga o fluxo de execução, que está implícito no texto (aula #18, 0:01:29; aula #28, 0:00:04).

[novo]

#### 7. Entrada e saída ficam nas bordas; funções retornam em vez de imprimir

Quem trata a entrada trata a saída (aula #23, 0:09:52); funções devem retornar algo, e imprimir é uma coisa, compor o que vai ser impresso é outra (aula #23, 0:07:13 e 0:08:40). Função que imprime deveria devolver a representação string, e o tratamento de entrada e saída fica o mais fora possível do código, até para facilitar o teste (aula #28, 0:09:56 e 0:11:01; aula #29, 0:08:21). Separe a obtenção da entrada do seu tratamento e validação; validação separada é testável e pode ser um parser que devolve um objeto comando (aula #29, 0:03:14, 0:06:44 e 0:07:04).

[novo; eco de camada-de-servico, que é a mesma regra para views de Django]

#### 8. Uma responsabilidade por elemento; desacoplamento é fractal

O código deve ser uma sucessão de elementos com uma única responsabilidade, e a sensação de macarrão é vazamento de responsabilidades; liste o que a função faz antes de mexer e a lista vira o mapa dos blocos (aula #22, 0:00:11, 0:00:19 e 0:00:42). Separe para que qualquer mudança aconteça com o menor impacto; desacoplamento não é só entre classes, é fractal, em múltiplos graus (aula #09, 0:04:47 e 0:04:58). `main` com entrada, saída e dispatch tem três coisas (aula #28, 0:11:55); `read_seq` com dois papéis deve separá-los, e o que funciona por coincidência entre duas funções é frágil (aula #29, 0:04:19 e 0:04:24). Separar responsabilidades em blocos, mesmo dentro da mesma função, já é componentizar (aula #22, 0:07:28).

[ja no KB: uma-responsabilidade-por-identidade]

#### 9. Repetição é de propósito, não de sintaxe; ao eliminar, não espalhe

Evitar repetição é evitar o mesmo código com o mesmo propósito; prenda-se ao propósito (aula #09, 0:00:19). Eliminar repetição pode criar outro problema, espalhar, a cirurgia de espingarda (aula #09, 0:00:49 e 0:02:00). Extraia o trecho duplicado para uma função e aplique nos dois lugares (aula #24, 0:00:40); ao criar um componente num nível mais baixo, adapte a hierarquia, por isso cuidado com a repetição (aula #24, 0:16:13). Extraia o que varia; o que fica igual se repete em loop (aula #31, 0:10:19).

[novo]

#### 10. Explícito é melhor que implícito; menos linhas não é mais

Todo `if` tem um `else`, explícito ou implícito; valor default serve para exceção, e dois caminhos válidos pedem os dois ramos escritos (aula #12, 0:00:12, 0:01:13 e 0:01:45). Não misture tipos no mesmo contexto nem dependa de conversão implícita; identifique e respeite o tipo em cada setor (aula #11, 0:00:00, 0:02:03 e 0:02:56; aula #16, 0:09:57). Não sobrescreva a entrada; busque funções sem efeitos colaterais (aula #13, 0:00:11, 0:01:36 e 0:01:49). Enxugar tem preço de legibilidade; não junte decisão e montagem da saída numa linha; resista a ser espertalhão (aula #12, 0:00:40; aula #13, 0:03:09; aula #15, 0:01:49 e 0:02:25). Evite `except` genérico: camufla o erro e tira a capacidade de depurar (aula #28, 0:07:25; aula #29, 0:05:30). O fundamental é o balanceamento entre forma e função (aula #12, 0:02:32; aula #17, 0:04:14).

[novo; o trecho sobre `except` genérico é vizinho de prefira-excecoes-a-booleanos e erros-na-fronteira]

#### 11. Número mágico vira nome e parâmetro com valor padrão; estratégia se injeta

Dê nome ao número que decide algo, quanto mais próximo do domínio melhor; mova-o para um parâmetro com valor padrão, injeção de dependência; extraia, nomeie e torne configuração da execução (aula #14, 0:00:34, 0:01:25 e 0:02:48; aula #24, 0:12:32). Cuidado para não passar todas as opções para a assinatura, porque muitos parâmetros é outro cheiro (aula #14, 0:02:07). Inverta a dependência injetando por parâmetro a função que muda a estratégia do algoritmo (aula #24, 0:04:14). Mapeamento com `if/elif` vira dicionário de chave para objeto executável, com acesso por colchetes para explodir no `KeyError` (aula #24, 0:08:36; aula #28, 0:02:23).

[novo; a estratégia injetada ecoa componha-em-vez-de-herdar, e o parâmetro com valor padrão ecoa configuracao-fora-do-codigo, mas nenhum dos dois cobre o número mágico]

#### 12. Torne evidente o conceito implícito

Há conceitos manifestos mas não expressos, óbvios mas não evidentes, e evidenciá-los é papel do programador (aula #16, 0:00:42; aula #17, 0:11:52). Um `if` que decide sobre um conceito pode ser encapsulado numa classe desse conceito, que passa a mudar em um único lugar; sempre que houver repetição ou muitos `if`s, pergunte se aquilo não é um conceito (aula #16, 0:01:55, 0:07:33 e 0:11:44). A essência da orientação a objetos é a interação entre objetos, a troca de mensagens, e objetos expressam interações, não só descrevem coisas (aula #16, 0:01:02 e 0:11:57). Funções que todas recebem e retornam a mesma estrutura sugerem uma classe (aula #28, 0:05:06); conversão de índice espalhada pede um objeto que a resolva num único ponto; busque representações de mais alto nível que array e lista (aula #30, 0:04:14, 0:04:35 e 0:06:42); quem depende da estrutura interna de um dado deveria ser método dele (aula #29, 0:09:47).

[novo]

#### 13. Algoritmos usam a interface da estrutura; não entulhe a classe

Preocupe-se com as interfaces entre as partes, não só com algoritmo e estrutura de dados; interfaces uniformes, retorno escolhido para quem chama (aula #23, 0:00:06, 0:01:49 e 0:02:54; aula #30, 0:14:11). Trabalhe primeiro as interfaces, como as bordas de um quebra-cabeça (aula #16, 0:04:29). Mude só o interior da função sem comprometer a interface com o exterior (aula #21, 0:12:41). O chamador não deve conhecer os detalhes do comando; quem conhece duas naturezas de índice está fazendo meio de campo (aula #28, 0:02:07 e 0:05:41). Um algoritmo opera sobre a estrutura pela interface, sem conhecer os internos, como a lista do Python; componha abstrações maiores e não sucumba à tentação de entulhar o algoritmo na classe (aula #30, 0:18:46; aula #31, 0:07:34 e 0:12:54).

[ja no KB: a-interface-e-o-que-importa]

#### 14. Componentes são fractais e substituíveis; não se prepare para o futuro

Partes não são componentes; componentes podem ser substituídos e padronizados, trabalham cooperativamente, e a natureza do que é processado define o que encaixa (aula #17, 0:06:35, 0:08:12, 0:09:27 e 0:10:56). Componentes têm natureza fractal: pequenos se agrupam em maiores (aula #18, 0:02:09), em diversos estágios de abstração, com uma função de nível acima articulando as menores e sem grãos pequenos demais (aula #24, 0:07:05 e 0:12:05), até o programa inteiro virar componente do sistema operacional (aula #24, 0:18:07; aula #25, 0:01:32). Não entre na síndrome de se preparar para o futuro nem embrulhe o que a linguagem já dá (aula #24, 0:02:41): convenção, não configuração (aula #21, 0:05:14); `with` para gestão de recurso e recursos sempre fechados (aula #21, 0:09:03; aula #22, 0:02:33 e 0:06:32); `defaultdict`, dunder `contains`, comparações ricas (aula #24, 0:10:06; aula #31, 0:01:33 e 0:03:00).

[ja no KB: nao-projete-a-generalizacao, para a segunda metade; a natureza fractal dos componentes e a definição de componente versus parte são novas]

#### 15. Planeje: liste antes de fazer, priorize, escolha o que não fazer

Planejar é essencial porque não dá para fazer tudo; o desafio é a coisa certa a fazer agora; entre o ideal e o possível, estratégias boas o bastante (aula #26, 0:00:26, 0:00:55, 0:00:58 e 0:02:08). Listar é muito mais rápido que fazer; primeiro listar, depois escolher o que executar e, principalmente, o que não fazer (aula #32, 0:03:39 e 0:04:28). Uma coisa de cada vez (aula #10, 0:02:18; aula #25, 0:01:50); arrume a área de trabalho, não o terreno inteiro, e não organize tudo antes de começar (aula #21, 0:10:49 e 0:11:38); refatoração elimina ruído, e foco é limitado (aula #03, 0:12:52). Código legado é grau de entropia, não idade; o olhar muda de legado para oportunidade de melhoria (aula #20, 0:01:19; aula #26, 0:02:54). O código é coletivo: sugestões provocam diálogo, não imposição, e o aluno comenta o que não concorda e por quê (aula #32, 0:01:30 e 0:02:09; aula #33, 0:00:18).

[novo; vizinho de deixe-o-codigo-descansar, que trata de entender antes de mexer, e de postergue-decisoes]

## 7. Citações-chave do curso

Paráfrases de legenda automática, sem aspas e não verificadas contra o vídeo. Mis-hearings evidentes anotados entre colchetes.

| Aula | Timestamp | Paráfrase |
|---|---|---|
| #01 | 0:01:14 | o objetivo desse programa não é fazer você decorar absolutamente nada, o que eu quero é estimular sua sensibilidade para você começar a perceber os detalhes que ficam implícitos no código |
| #02 | 0:00:13 | refaturar [refatorar] é melhorar a estrutura interna do seu código sem mudar o comportamento com o mundo exterior |
| #02 | 0:02:02 | reescrever tudo não é refaturar [refatorar] |
| #02 | 0:03:45 | não me interessa o sistema que você fez, a única certeza que eu tenho é que ele vai mudar |
| #02 | 0:08:01 | na prática a teoria é outra e a gente sempre precisa priorizar o terreno da realidade através do mapa do ideal |
| #03 | 0:03:01 | nunca refatore um código instável, o código precisa estar funcionando |
| #04 | 0:02:15 | é como se você tivesse meio que programando em terceira pessoa, onde você tá escrevendo o código e refletindo sobre o seu processo de escrever o código |
| #06 | 0:02:37 | a primeira coisa que eu gosto de observar antes de qualquer coisa do código é a relação do código com o domínio do problema |
| #07 | 0:03:45 | eu quero um único retâneo [return] no meu código, eu quero que ele entre por uma porta e saia para uma outra porta |
| #09 | 0:00:19 | evitar repetição é você evitar que exista o mesmo código com o mesmo propósito, então não se prenda apenas à sintaxe, se prenda ao propósito |
| #10 | 0:00:42 | você está nomeando as coisas em função da implementação e não em função do domínio do problema que está resolvendo |
| #12 | 0:00:12 | todo if tem um Élcio [else], não interessa o que aconteça, pode ser explícito, pode ser implícito |
| #12 | 0:02:32 | para mim o que é fundamental é um balanceamento entre forma e função, não dá para fazer a coisa só estética e não dá para fazer a coisa só funcional |
| #13 | 0:03:09 | cuidado na ânsia de tentar enxugar o código, porque você pode acabar pagando um preço de legibilidade e de compreensão de quem nunca viu aquele programa antes |
| #15 | 0:02:25 | resista à tentação de ser um espertão, vamos tentar ser o mais pragmático possível, pensar na evolução do projeto e da equipe |
| #16 | 0:00:38 | um conceito que ele está manifesto mas não tá expresso, ele tá óbvio mas não tá evidente, a gente precisa evidenciar isso |
| #16 | 0:01:04 | a essência da orientação a objeto é exatamente a interação dos objetos com o exterior, a interação dos objetos entre si, é nessa troca de mensagem que a coisa acontece |
| #17 | 0:06:35 | uma máquina desse tipo ela não tem componentes, ela tem partes |
| #17 | 0:14:07 | não é uma questão de regra, os componentes vão em energia [emergir] a partir do seu contexto |
| #18 | 0:01:29 | mais importante que isso na minha visão é perceber o fluxo da informação, o fluxo de execução do programa; isso não está no código, isso está implícito no código |
| #20 | 0:02:19 | antes de sequer ler o código eu tenho que fazer a coisa mais importante do mundo: não me importa o quão fera você seja, quantos PhDs você tem, receber um código tem que executar ele |
| #20 | 0:06:49 | dessa maneira eu consigo cercar o programa por fora do código e criar o que a gente chama de golden file, que é arquivo de ouro |
| #21 | 0:01:24 | eu acho que comentário é um sintoma de que o código não é bom o bastante |
| #22 | 0:00:19 | toda vez que você olha um código e tem a sensação de que ele tá embolado, bem macarrônico, é porque você tá tendo vazamento de responsabilidades |
| #23 | 0:08:40 | imprimir é uma coisa, compor o que vai ser impresso é outra coisa |
| #24 | 0:02:41 | a gente entra numa síndrome de vou me preparar para o futuro, quero fazer a coisa mais prontinha para mudar, e a gente acaba fazendo coisa demais |
| #26 | 0:00:55 | o desafio do jogo é descobrir qual a coisa certa a fazer agora |
| #30 | 0:19:38 | eu não preciso pegar os meus algoritmos e entulhar dentro da minha classe; eu posso fazer algoritmos que usam as interfaces dessa estrutura de dados |
| #32 | 0:01:30 | a propriedade do código não é de quem escreve, mas sim daquela equipe que trabalha nele, de quem cuida para que aquele sistema continue funcionando |
| #32 | 0:03:39 | é muito mais rápido listar do que fazer [transcrição: ele está] |

## 8. A evolução técnica, aula a aula

| Etapa | O que é feito | Conceito ou ferramenta | O que isso destrava |
|---|---|---|---|
| **#01 a #05** | Exposição: definição, por quê, quando, processo, dez oportunidades numa linha (#02 0:00:13; #03 0:01:12; #04 0:02:15; #05 0:01:13) | Refatoração como mudança de estrutura; decisão econômica; chapéus; programar em terceira pessoa | O vocabulário e o pressuposto de código estável que os blocos práticos assumem |
| **#06** | Enunciado do donuts, teste com pytest, `count < 10` vira `count >= 10` (0:01:26 a 0:05:23) | pytest no PyCharm; domínio do problema | O ciclo pequena mudança mais testes (0:05:44) |
| **#07** | Dois `return` viram um, com variável de mensagem (0:04:02) | Código linear; entrada, processamento e saída | Um bloco de decisão e uma linha de saída separáveis |
| **#08** | Reindentação para quatro espaços e linha em branco (0:00:53) | PEP 8; linters | Formatação consistente antes de mexer na estrutura |
| **#09** | `+=` que espalha é trocado por variável `t` nos ramos e concatenação no `return` (0:03:14 a 0:04:03) | Repetição de propósito; shotgun surgery; variável como transporte | Saída desacoplada do `if` |
| **#10** | `t` vira `qty` com o rename da IDE (0:01:44) | Shift F6; nomes do domínio | Nome que o `str(count)` de #11 e a classe de #16 vão reutilizar |
| **#11** | Variante `qty = count` com `%s` é rejeitada; `str(count)` fica (0:00:16 a 0:02:40) | Simetria de tipos; conversão implícita | O `if` reconhecido como lógica de transformação |
| **#12** | Variante com valor default antes do `if` é revertida (0:00:47 a 0:02:13) | Explícito sobre implícito; forma e função | Dois caminhos válidos mantidos como `if` e `else` |
| **#13** | Variante `count = 'many'` é revertida (0:00:46 a 0:02:47) | Entrada intacta; funções sem efeito colateral | A entrada disponível para decisões futuras |
| **#14** | `limite = 10`, depois `limite=10` como parâmetro (0:00:40 a 0:01:41) | Número mágico; injeção de dependência | O atacadista com 100 sem mudar o comportamento padrão |
| **#15** | Versão numa linha com `if` por expressão é revertida (0:00:45 a 0:02:22) | Espertalhão; pragmatismo | Decisão e montagem da saída continuam separadas |
| **#16** | Classe `Quantity` guiada por `test_quantity`, `__str__`, `many` como `@property`, f-string (0:02:30 a 0:10:33) | Conceito evidente; troca de mensagens; bordas do quebra-cabeça | donuts vira uma linha que delega ao conceito |
| **#17 e #18** | Exposição: componentes, dimensões, ajuste de relevância (#17 0:05:37 a 0:14:30; #18 0:00:52) | Componente versus parte; natureza fractal | O critério para ler o wordcount |
| **#19 e #20** | Enunciado; executar o legado, corrigir `print`, `letras.txt`, golden files com `diff`, pytest com `capsys` e `monkeypatch` (#20 0:02:52 a 0:09:52) | Código legado como entropia; teste de caixa preta | Segurança para mudar sem ler tudo |
| **#21** | Limpeza de `word_count_dict`: comentários, `d`, `f`, `w`, sem `'r'`, TODO, reformatação (0:02:55 a 0:10:49) | Convenção sobre configuração; contraste; área de trabalho | Função legível sem mudar a interface |
| **#22** | `with`, `read()`, `lower()` na coleção, `split()` sem argumento, inversão do caso especial, docstring (0:02:23 a 0:07:51) | Context manager; etapa de preparação | Blocos que refletem a lista de responsabilidades |
| **#23** | `items()` como retorno, `lambda t: t[-1]`, slice antes da impressão, `'\n'.join`, `return out`, `print` em `main` (0:03:21 a 0:09:50) | Interface uniforme; compor versus imprimir | Funções testáveis pelo retorno |
| **#24** | `lines`, `top`, `word_counter(filename, order)`, `read`, `split`, `count`, dicionário de opções, `defaultdict`, `limit=20`, `open_file` com `-`, early return (0:00:40 a 0:18:07) | Inversão de dependência; componente de componente; stdin | O programa como componente do sistema operacional |
| **#25 e #26** | Recapitulação em cinco etapas; abertura do planejamento (#25 0:00:29 a 0:01:48; #26 0:00:26) | Etapas cíclicas; bom o bastante | O modo análise das aulas seguintes |
| **#27** | Executar a matriz pelos comandos do README (0:02:40 a 0:04:38) | README como teste; uniformidade | O comportamento relacionado ao fonte antes de ler |
| **#28** | TODOs em `main`: dicionário de dispatch, encapsular comando, `board` como classe, conversão de índice, `except` específico (0:02:13 a 0:11:55) | Entry point; encapsulamento | A lista de tarefas começa |
| **#29** | TODOs em `read_seq` e `print_board`: nomes, obtenção versus validação, parser para objeto comando, `__str__` (0:00:18 a 0:09:10) | Entrada e saída nas bordas; funcionar por coincidência | Validação testável |
| **#30** | TODOs nos comandos: parâmetros expandidos, Coordenada, Região, método que atribui a múltiplas coordenadas (0:00:14 a 0:21:12) | Representação de mais alto nível; composição Board, Coordenada, Região | Três comandos viram um algoritmo |
| **#31** | TODOs em `out_range`, `fill_pixel`, `save_array`: `__contains__`, comparações ricas, vizinhos em loop, fill genérico (0:00:17 a 0:15:13) | Algoritmo sobre a interface; condição de parada | Fill independente do Board |
| **#32 e #33** | 84 TODOs como lista de tarefas; fork com as anotações (#32 0:00:57; #33 0:00:06) | Code review; código coletivo; listar antes de fazer | O plano que o aluno executa e contesta |

## 9. Arsenal técnico demonstrado no curso

| Técnica ou recurso | Para que ele usa | Aula e timestamp |
|---|---|---|
| pytest rodado pelo PyCharm | Garantir código estável antes de cada refatoração | #06, 0:01:26; #16, 0:02:30 |
| Rename da IDE (shift F6) | Renomear todas as ocorrências de uma vez | #10, 0:01:35; #21, 0:03:36 |
| Reformat do PyCharm | Passar de dois para quatro espaços | #21, 0:10:03 |
| Variável de mensagem e único `return` | Eliminar dois pontos de saída | #07, 0:04:02 |
| `str(count)` como transformação | Manter o tipo consistente em cada setor | #11, 0:02:40 |
| Parâmetro com valor padrão | Extrair o número mágico sem mudar o comportamento | #14, 0:01:32; #24, 0:12:32 |
| `if` por expressão | Mostrar a versão numa linha e por que não usá-la | #15, 0:00:23 |
| `__str__`, `@property`, f-string | Encapsular o conceito `Quantity` e interpolá-lo | #16, 0:04:22, 0:09:14 e 0:09:48 |
| `echo` e redirecionamento de saída | Criar `letras.txt` e os golden files | #20, 0:03:42 e 0:05:01 |
| `diff` | Comparar a saída atual com o golden file | #20, 0:05:55 |
| `capsys` e `monkeypatch` sobre `sys.argv` | Testar `main` por dentro do pytest | #20, 0:07:30 e 0:08:44 |
| `subprocess` | Alternativa ao pytest para cercar o programa | #20, 0:09:30 |
| `open` sem `'r'` | Convenção sobre configuração | #21, 0:05:07 |
| `with open(...) as f` | Gestão de recurso com context manager | #22, 0:02:23 |
| `content.lower()` e `split()` sem argumento | Transformar a coleção inteira e eliminar um `for` | #22, 0:04:07 e 0:04:40 |
| Inversão de lógica no caso especial | Inicializar com zero e sempre incrementar | #22, 0:05:17 |
| Docstring no lugar de comentário | Explicar a função pela própria função | #22, 0:07:51; #29, 0:00:40 |
| `d.items()` como retorno; `sorted` com `key=lambda t: t[-1]` | Interface uniforme para as duas saídas | #23, 0:03:21 e 0:04:44 |
| `'\n'.join` e `return out` | Compor a saída em vez de imprimir | #23, 0:07:40 a 0:09:27 |
| Função de ordenação injetada por parâmetro | Inverter a dependência da estratégia | #24, 0:03:27 |
| Dicionário de opções com `try/except KeyError` | Substituir o `if/elif` do `main` | #24, 0:07:55 |
| `defaultdict(int)` | Eliminar o `if` do `count` | #24, 0:10:06 |
| List comprehension | Reescrever `lines` e o `for` de `create_array` | #24, 0:10:46; #30, 0:02:38 |
| `sys.stdin` quando o arquivo é `-` | Tornar o programa um componente de pipe | #24, 0:14:33 |
| Early return | Abortar quando não há condição para o propósito | #24, 0:16:47 |
| Comentários `TODO` como lista de tarefas do PyCharm | Transformar a análise em plano | #28, 0:02:13; #32, 0:00:57 |
| Dunder `contains` e comparações ricas | Pertencimento de coordenada ao board | #31, 0:01:33 e 0:03:00 |
| Vizinhos computados e chamados em loop | Extrair o que varia no fill recursivo | #31, 0:09:20 |

## 10. Glossário do curso

| Termo | Significado no contexto da série | Onde |
|---|---|---|
| **Refatoração** | Melhorar a estrutura interna do código sem mudar o comportamento com o mundo exterior | #02, 0:00:13 |
| **Cheiro de código** | Alguma coisa que não cheira bem; há diversos catalogados | #02, 0:05:02; #14, 0:02:14 |
| **Padrão de projeto** | Receita já articulada sobre design de código, principalmente orientado a objetos | #02, 0:05:13 |
| **Antídoto contra o envelhecimento** | Reconhecer o cheiro, recrutar um padrão, aplicar a refatoração | #02, 0:04:47 |
| **Explosão combinatória** | Uns 30 casos de refatoração, 30 padrões e 30 cheiros que raramente aparecem sozinhos | #02, 0:08:18 |
| **Saliência** | O que o sistema cognitivo prioriza; pensar fora da caixa é reconfigurá-la | #03, 0:00:20 |
| **Chapéus** | Momentos distintos de funcionalidade, refatoração e otimização | #03, 0:04:56 |
| **Expansão, acomodação e consolidação** | O ciclo do montinho de areia que desmorona e aumenta a base | #03, 0:06:29 |
| **Hipótese da resistência do design** | Conceito de Fowler: funcionalidades acumuladas por tempo com curva de bom e mau design | #03, 0:07:13 |
| **Ressaca cognitiva** | Um monte de coisa desperta na cabeça e muito menos concentração para o que está na frente | #03, 0:12:11 |
| **Ruído** | Código, ambiente, casa e computador bagunçados; refatoração elimina ruído | #03, 0:12:46 |
| **Programar em terceira pessoa** | Escrever o código refletindo sobre o processo de escrever o código | #04, 0:02:15 |
| **Domínio do problema** | De onde se extrai o conhecimento e a informação para criar o código que cria o valor | #06, 0:03:02 |
| **Telefone sem fio** | Cada um faz a partir do próprio entendimento do requisito | #06, 0:04:39 |
| **Código pulga** | Código que fica pulando de lugar, quicando de um ponto para o outro | #07, 0:01:36 |
| **Código linear** | O mais linear, direto e sequencial possível; um ponto de entrada e um de saída | #07, 0:02:00 |
| **Programas fantasiados de um** | Um único bloco com inúmeros caminhos | #07, 0:03:25 |
| **Entrada, processamento e saída** | O esquema da primeira aula de faculdade; fractal, vale dentro da função | #07, 0:04:47; #11, 0:01:33; #17, 0:12:09 |
| **Cirurgia de espingarda** | Mudança espalhada como um tiro de espingarda, tirada caquinho por caquinho | #09, 0:02:04 |
| **Desacoplamento** | Não só entre classes e objetos; fractal, em múltiplos graus | #09, 0:04:58 |
| **Variável como transporte** | Transporta um valor para outro lugar, para outro momento | #09, 0:04:23 |
| **Simetria de tipos** | Identificar e respeitar o tipo de dado em cada setor do código | #11, 0:02:56 |
| **Valor default** | Útil quando se trabalha uma exceção, não para dois caminhos válidos | #12, 0:00:55 |
| **Sobrescrita do input** | Ressignificar a variável de entrada em execução | #13, 0:00:11 |
| **Efeito colateral** | Entrada alterada ou ressignificada; ele busca funções sem isso | #13, 0:01:49 |
| **Número mágico** | Um número solto no código sem nome nem motivo claro | #14, 0:02:37; #24, 0:12:32 |
| **Injeção de dependência** | Fazer o limite, ou a estratégia, ser fornecido à função por parâmetro | #14, 0:01:25; #24, 0:04:14 |
| **Espertalhão** | O bichinho que fala no ouvido: dá para fazer diferente | #15, 0:00:19 |
| **Óbvio mas não evidente** | Conceito manifesto mas não expresso, a evidenciar | #16, 0:00:42 |
| **Troca de mensagens** | A essência da orientação a objetos: a interação dos objetos entre si | #16, 0:01:10 |
| **Quebra-cabeça pelas bordas** | Trabalhar as interfaces primeiro, o miolo depois | #16, 0:04:38 |
| **Crise do software** | Conferência da OTAN em 1968 | #17, 0:00:49 |
| **Componentização** | Abordada por McIlroy: reutilizar em vez de construir tudo de novo | #17, 0:01:06 |
| **Pipeline** | Programas de propósito específico conectados pela saída de um à entrada de outro | #17, 0:01:31 |
| **Design versus arquitetura** | Arquitetura é o difícil de mudar; design interno é como as partes se relacionam | #17, 0:03:40 |
| **Design** | Vem de designar, dar sentido; equilíbrio entre forma e função | #17, 0:04:06 |
| **Máquina de Rube Goldberg** | Geringonça que faz uma tarefa simples da forma mais complicada; tem partes, não componentes | #17, 0:06:02 |
| **Componente versus parte** | Componentes podem ser substituídos e padronizados; partes não | #17, 0:06:35 |
| **Dimensões do componente** | Entradas, saídas, processamento, responsabilidade, robustez | #17, 0:12:09 |
| **Ajuste de relevância** | Olhar o foco, depois o entorno, descer e subir um nível | #18, 0:00:52 |
| **Natureza fractal dos componentes** | Componentes pequenos se agrupam em maiores | #18, 0:02:09 |
| **Fazer funcionar, fazer direito, fazer rápido** | O ciclo completo, no mesmo fluxo, com escopo reduzido | #19, 0:00:14 |
| **Macarronada** | Código embolado; vazamento de responsabilidades | #19, 0:01:10; #22, 0:00:19 |
| **Código legado** | Definido pelo grau de entropia, não pela idade | #20, 0:01:19 |
| **Golden file** | Arquivo de ouro: a saída esperada que cerca o programa por fora | #20, 0:06:49 |
| **Teste de caixa preta** | Cercar o comportamento sem olhar o interior | #25, 0:00:29 |
| **Contração e expansão** | O ritmo da refatoração: simplificar, depois ver o que ficou simples demais | #21, 0:04:18 |
| **Convenção, não configuração** | Não explicitar o padrão que a linguagem já assume | #21, 0:05:14 |
| **Palavras de pouco contraste** | `word` e `words`; o cérebro não funciona bem com pouco contraste | #21, 0:06:50 |
| **Caso especial** | Problema a evitar ao máximo; inversão de lógica o transforma em preparação | #21, 0:08:03; #22, 0:05:39 |
| **Arrumar o terreno** | Dar uma arrumada na área de trabalho para enxergar onde se está | #21, 0:11:38; #25, 0:00:51 |
| **Vazamento de responsabilidades** | A causa da sensação de código macarrônico | #22, 0:00:19 |
| **Context manager** | O comando `with` do Python, para gestão de recurso | #22, 0:02:33 |
| **Interface uniforme** | Quem consome a mesma função se apoia na mesma estrutura | #23, 0:01:49 |
| **Síndrome de se preparar para o futuro** | Fazer coisa demais para a mudança que não veio | #24, 0:02:41 |
| **Componente de componente** | A função de nível acima que reúne as menores | #24, 0:11:55 |
| **Early return** | Retorno antecipado quando não há condição para o propósito do comando | #24, 0:17:18 |
| **Bom o bastante** | A estratégia intermediária entre o ideal e o possível | #26, 0:02:08 |
| **Entry point** | O início da execução, por onde a análise começa | #28, 0:00:08 |
| **Implementação procedural** | Funções que recebem e retornam a mesma estrutura | #28, 0:04:53 |
| **Except genérico** | Camufla o erro e tira a capacidade de depurar | #28, 0:07:25 |
| **Board como string** | A representação que substitui o `print` dentro da função | #28, 0:09:56; #29, 0:08:27 |
| **Funcionar por coincidência** | Comportamento que depende de duas funções se cobrirem por acaso | #29, 0:04:19 |
| **Parser, objeto comando** | Validação que converte a entrada num objeto em vez de lista de strings | #29, 0:07:26 |
| **Coordenada, célula** | O objeto que expressa posição no nível de negócio e encapsula a conversão de índice | #30, 0:06:42 |
| **Região** | A abstração que unifica linha vertical, horizontal e bloco | #30, 0:16:45 |
| **Entulhar a classe** | Colocar algoritmos dentro da classe em vez de usá-la pela interface | #30, 0:18:46; #31, 0:12:54 |
| **Comparações ricas** | `0 <= x < width`, recurso do próprio Python | #31, 0:03:00 |
| **Condição de parada** | O teste no início da recursão, obtido invertendo a lógica | #31, 0:08:27 |
| **Code review** | A dinâmica que a análise da matriz reproduz | #32, 0:00:45 |
| **Código coletivo** | A propriedade do código é da equipe que cuida dele | #32, 0:01:40 |
| **Sexo dos anjos** | Discussão em que não se pode escorregar ao escolher o que fazer | #32, 0:04:06 |

## 11. Perguntas e respostas que o curso responde

#### O que é refatorar, e o que não é?

Melhorar a estrutura interna sem mudar o comportamento com o mundo exterior; nem toda mudança com intenção de melhorar é refatoração, e reescrever tudo não é refatorar (aula #02, 0:00:13 a 0:02:02).

#### Quando refatorar, e quando não?

Quando precisar ajustar o código para acolher uma mudança, com decisão econômica, priorizando o que muda com frequência; não por estética em contexto profissional (aula #03, 0:01:12 a 0:02:57).

#### Achei um bug no meio da refatoração. E agora?

Para tudo, volta atrás, conserta, estabiliza, e só então continua; corrigir o bug junto viola o princípio de não mudar o comportamento (aula #03, 0:03:01 a 0:03:24).

#### Como refatorar código que não tem testes?

Executa antes de ler; se o programa é determinístico, redireciona a saída para golden files e compara com `diff`; depois replica em pytest com `capsys` e `monkeypatch` (aula #20, 0:02:17 a 0:09:52).

#### Quantas oportunidades há num problema de uma linha?

Dez, segundo ele, no exercício donuts (aula #05, 0:01:13), percorridas das aulas #06 a #16.

#### Dois `return` numa função são um problema?

Precisar de um branch não obriga a dois pontos de retorno; ele quer um único `return`, entrando por uma porta e saindo por outra (aula #07, 0:02:15 a 0:03:45). O early return é a exceção: abortar a missão quando não há condição para o propósito (aula #24, 0:17:03).

#### Posso usar um valor default antes do `if` para economizar o `else`?

Funciona, mas rompe a estrutura do `if`; valor default serve para exceção, e dois caminhos válidos pedem `if` e `else` explícitos (aula #12, 0:01:03 a 0:02:05).

#### Posso reatribuir o parâmetro de entrada?

Pode, mas precisa de argumento muito sólido; ele evita, a menos que seja a proposta do algoritmo, e busca funções sem efeito colateral (aula #13, 0:01:28 a 0:01:49).

#### O que fazer com o número 10 solto no código?

Dar um nome do domínio, depois movê-lo para um parâmetro com valor padrão, sem inchar a assinatura (aula #14, 0:00:37 a 0:02:48).

#### Vale a pena colocar tudo numa linha?

Num exercício é bacana; num projeto, não recomenda nem um pouco, porque junta decisão e saída e exige saber a ordem dos operadores de cabeça (aula #15, 0:01:30 a 0:02:25).

#### Quando um `if` vira uma classe?

Quando decide sobre um conceito manifesto mas não expresso; sempre que há repetição ou muitos `if`s, a pergunta é se aquilo não é um conceito (aula #16, 0:01:55 e 0:11:44).

#### O que é um componente, e o que é só uma parte?

Componentes podem ser substituídos e padronizados e trabalham cooperativamente; a máquina de Rube Goldberg tem partes (aula #17, 0:06:35 a 0:08:12).

#### Devo criar uma função `asc` para embrulhar o `sorted`?

Não; é a síndrome de se preparar para o futuro, e o `sorted` já é um componente (aula #24, 0:02:30 a 0:02:41).

#### Por que o `print` sai da função e vai para o `main`?

Imprimir é uma coisa, compor o que vai ser impresso é outra; quem trata a entrada deve tratar a saída (aula #23, 0:08:40 a 0:09:52).

#### Por que ele não implementa os 84 TODOs da matriz?

Porque listar é muito mais rápido que fazer, e o momento seguinte é escolher o que executar e o que não fazer; a implementação fica com o aluno, que comenta o que não concorda (aula #32, 0:03:39 a 0:04:28; aula #33, 0:00:13).

#### O algoritmo de fill deve ser método do Board?

Não necessariamente; ele opera sobre a estrutura pela interface, pode ser função ou classe independente, e não se deve entulhar a classe (aula #31, 0:07:34 e 0:12:54).

## 12. Repositórios e recursos

| Recurso | Onde encontrar | Observação |
|---|---|---|
| Playlist completa (fonte desta documentação) | [Refatoração na Prática](https://www.youtube.com/playlist?list=PLeKXYyZCJHxfTqEvicb9dqcbj-eCOFhhj) | 34 vídeos; ids em `sources/transcripts/refatoracao-na-pratica/playlist.json`. |
| Canal | [HB Network](https://www.youtube.com/@hbnetworkoficial) | |
| Livro de refatoração de Martin Fowler | citado na aula #02, 0:04:09 [legenda: marketing falller] | Sem edição nem link; a hipótese da resistência do design é atribuída a Fowler na aula #03, 0:07:10. |
| Coleção de exercícios do Google | citada na aula #05, 0:00:12; o link do wordcount é mencionado na aula #19, 0:01:16 | O donuts e o wordcount vêm dela; a URL não aparece na transcrição. |
| PEP 8 | citada na aula #08, 0:00:39 | Como o estilo que a maioria segue em Python. |
| Conferência da OTAN de 1968 e o paper de Douglas McIlroy | citados na aula #17, 0:00:33 a 0:02:15 | Ele resume o paper; não dá título nem link. |
| Dijkstra sobre a crise do software | citado na aula #17, 0:04:38 [legenda: Dexter] | Sem referência. |
| Vídeo do autor e código da matriz | citados na aula #27, 0:01:12 | Links na descrição do vídeo; não constam da transcrição. |
| Fork do projeto da matriz com os 84 TODOs | citado na aula #33, 0:00:06 | Repositório dele; a URL não consta da transcrição. |
| Exercício no Loom | aula #25, 0:02:02 | Vídeo de 5 a 10 minutos analisando um código próprio, postado com o repositório. |
| Série sobre o mesmo tema | `kb/courses/oo-na-pratica.md` e `kb/courses/raio-x-da-oo.md` | A troca de mensagens como essência da orientação a objetos (aula #16, 0:01:02) é o ponto de contato. |

Repositório do instrutor para esta série: **nenhum verificável a partir das transcrições**. O donuts e o wordcount são digitados no PyCharm e não são salvos em lugar que a aula mencione; o fork da matriz existe segundo a aula #33, mas esta documentação não verificou o GitHub do autor além das transcrições e não lista reimplementações de comunidade para este curso.

## 13. Análise linha a linha do código real

Não há código publicado para esta série, portanto não há análise de código real. O que existe são três conjuntos de reconstruções, marcados como tal na seção 5:

- **Donuts (aulas #06 a #16).** A cadeia de versões da função `donuts`, da implementação recrutada com `count < 10` (aula #06, 0:02:04) até a classe `Quantity` com `__str__`, `many` como `@property` e a f-string (aula #16, 0:10:33), passando pelas variantes que ele mostra e reverte (aulas #11, #12, #13 e #15). Limites: só o assert `donuts(4)` é audível (aula #06, 0:01:46); o nome da variável de mensagem é ouvido como mensagem e reconstruído como `message` (aula #07, 0:04:10); o nome da classe é ouvido como quantite e quântico (aula #16); se o limite entra em `Quantity.__init__` como parâmetro ou fixo não é verificável (aula #16, 0:05:54 e 0:06:13); a posição dos parênteses na versão de uma linha não é ouvida (aula #15, 0:01:41).
- **Wordcount (aulas #19 a #24).** O esqueleto descrito (aula #19, 0:03:05), os comandos de shell e o `test_wordcount.py` (aula #20), o estado de `word_count_dict` ao fim das aulas #21 e #22, as funções de impressão ao fim da aula #23 e a forma final com `open_file`, `read`, `split`, `count`, `top`, `lines`, `word_counter` e o `main` com dicionário de opções (aula #24). Limites: o conteúdo exato de `letras.txt` e o formato das linhas de saída são deduzidos do enunciado; a forma do `diff` não fica clara (aula #20, 0:05:55); a mensagem de usage e a direção do `reverse` são deduzidas; o esqueleto original do Google não é transcrito.
- **Matriz (aulas #27 a #31).** Aqui ele não altera o código: dita comentários TODO. A seção 5 transcreve os TODOs como ditados e dois esboços falados (`board[Coordenada(1, 2)] = color` na aula #30, 0:07:55; a função de pertencimento e o loop de vizinhos na aula #31). O fonte `matriz.py` é de um aluno e não é reproduzido; os nomes das funções (`read_seq`, `char_valid`, `create_array`, `clean_array`, `color_pixel`, `v_pixel`, `h_pixel`, `block_pixel`, `out_range`, `fill_pixel`, `save_array`, `print_board`) são os que a fala registra, e as formas ouvidas pelo reconhecedor ficam anotadas em cada aula.

## 14. Execução real dos testes

Não há código publicado, logo não há suíte do curso para executar. As reconstruções do donuts e do wordcount são, em princípio, executáveis, mas este documento não as executou: diferentemente do digest de Raio X da Orientação a Objetos, nenhuma seção aqui registra saída de terminal, e os asserts reproduzidos (`test_donuts` na aula #06, `test_quantity` na aula #16, `test_count` e `test_topcount` na aula #20) são os que a legenda deixa ouvir, com os formatos de saída marcados como incertos onde a fala não os confirma. Os TODOs da matriz não são código e não têm o que rodar.

---

Documentação elaborada a partir das transcrições automáticas de 33 das 34 aulas da playlist Refatoração na Prática, de Henrique Bastos (HB Network), playlist `PLeKXYyZCJHxfTqEvicb9dqcbj-eCOFhhj`, legendas em português (pt-orig) capturadas em 2026-10-08; a aula #34 (`4ZOhCPTWrS0`) não tem legenda, título nem duração. As citações são paráfrases das legendas automáticas, não verificadas contra o vídeo (`verified: false`), renderizadas sem aspas e com os erros de reconhecimento de fala anotados entre colchetes quando precisam aparecer. O curso não publicou repositório, gist, documento ou teste: o donuts e o wordcount são reconstruções a partir da narração, marcadas como tal na seção 5, a matriz é código de um aluno analisado em TODOs, e o fork com as anotações (aula #33) não tem URL na transcrição. Nenhuma reconstrução foi executada nesta sessão. Datas de publicação e visualizações não foram coletadas. Conteúdo de caráter educativo.
