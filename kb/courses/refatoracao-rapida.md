<!-- written by the henrique-ingest distiller on 2026-10-12 from sources/transcripts/refatoracao-rapida/; see kb/courses/README.md for provenance and license -->

HB Network · Documentação de curso

# Domine o Método da Refatoração Rápida

As 16 aulas da playlist, lidas aula a aula a partir das legendas automáticas. Quatro aulas conceituais (contexto de carreira, refatoração, fluxo) abrem caminho para doze aulas de refatoração ao vivo de um editor de matriz de pixels escrito por um aluno, o mesmo programa que ele tinha analisado sem mexer, ditando TODOs, nas aulas #27 a #33 de Refatoração na Prática. Aqui ele executa a refatoração, só com funções, e fecha reaproveitando a API resultante num Game of Life escrito na hora.

Instrutor: **Henrique Bastos** · Canal [HB Network](https://www.youtube.com/@hbnetworkoficial) · Playlist: [Domine o Método da Refatoração Rápida](https://www.youtube.com/playlist?list=PLeKXYyZCJHxfHUETjNouzr1hyaiuljrUY) · Repositório: nenhum publicado para esta série (a única biblioteca dele que aparece é a inputao, aula 15, 0:10:44)

Documento elaborado a partir das transcrições das 16 aulas (legenda automática em português, pt-orig, capturada em 2026-10-12). As aulas 4 a 16 são recortes de uma transmissão ao vivo com turma, com chat e microfone aberto: há falas de participantes misturadas às dele, e a legenda não marca quem fala. Os trechos de fala alheia identificados (aula 4, 0:16:05 a 0:16:44; aula 14, 0:13:55 a 0:18:19; aula 16, 0:36:57 em diante) não são atribuídos a ele em nenhuma seção. O código refatorado é de um aluno e não é reproduzido; o aluno não é nomeado.

## 1. Visão geral do curso

Domine o Método da Refatoração Rápida é uma série de **16 vídeos** que somam **16.720 segundos, 4 horas, 38 minutos e 40 segundos**. A série tem dois blocos. As aulas 1 a 4 são conceituais: o vale das sombras do mercado e a carreira antifrágil (aulas 1 e 2), a refatoração como forma de enxergar o invisível no código (aula 3, 0:00:29) e a tese do curso, entender a estrutura, depois o fluxo, e então mudar a estrutura mantendo o fluxo (aula 4, 0:03:33 a 0:03:41). As aulas 5 a 16 são uma única sessão prática: rodar o programa legado (aula 5), cercá-lo com testes pela interface (aulas 6 e 7), esconder detalhes de implementação (aulas 8 e 9), generalizar a partir de três repetições (aulas 10 a 12), isolar o disco com mock (aula 13), separar o algoritmo de preenchimento da estrutura (aula 14), reorganizar a entrada e o despacho (aula 15) e reaproveitar a API num programa novo (aula 16).

| Dimensão | Valor | Observação |
|---|---|---|
| Aulas | 16 | Playlist completa, numerada de #01 a #16. |
| Duração total | 16.720 s (4h 38min 40s) | Soma das durações em `playlist.json`. |
| Aula mais curta / mais longa | 189 s (#1) / 2.915 s (#14) | A #1, Por Que Estamos Aqui?, tem 3:09; a #14, O Poder de Abstração dos Algoritmos, tem 48:35. |
| Datas de publicação | não coletadas | O `playlist.json` desta coleta traz id, título e duração. |
| Visualizações | não coletadas | Idem. |
| Transcrições | 16 de 16 disponíveis | Todas em legenda automática (pt-orig). Não há legenda humana nem transcrição Whisper. |
| Título em inglês | aula #2 | Publicada como Mastering the Rapid Refactoring Method #02: The Context; a fala é em português. |
| Legenda ruidosa | nomes de código | Quase todo identificador sai deformado (Witch para width, Death Regiane para def region, Beauty open para builtins.open). Os trechos conceituais são legíveis em todas as aulas. A aula 14 tem um trecho de falas cruzadas (0:13:55 a 0:18:19) que não é citado. |
| Código do curso | nenhum publicado | O programa é de um aluno e não é reproduzido. O código que ele escreve ao vivo aparece na seção 5 como reconstrução a partir da fala, não publicada. |

Nota de método: cada afirmação traz aula e timestamp. As citações são paráfrases de legenda, sem aspas, não verificadas contra o vídeo. Mis-hearings ficam entre colchetes. As seções 13 e 14 dizem que não há código publicado a analisar nem suíte a rodar.

## 2. Filosofia e método de ensino

### 2.1 Rápido de progredir, não rápido de fazer

O nome engana de propósito: a refatoração rápida não é rápida de fazer, porque programar é lento, mas é rápida de progredir, uma refatoração em que não se fica travado (aula 2, 0:00:44 a 0:00:58). Os dois fracassos que ele vê são escorregar para a estética pela estética ou travar sem saber a coisa certa a fazer (aula 2, 0:00:58 a 0:01:13). No fecho ele volta ao nome: a turma levou um tempão, e o rápido é a capacidade de agir a partir do momento em que se enxerga o fluxo (aula 16, 0:37:57 a 0:38:08).

### 2.2 Processo em vez de genialidade

Desde o primeiro treinamento, em 2010, ele usa passos de bebê com ciclo de feedback intensivo, o que quebra a visão de programação como coisa genial em que é preciso ter tudo na cabeça (aula 1, 0:02:04 a 0:02:32). Na parte prática ele avisa que vai mostrar passo a passo como pensa (aula 5, 0:01:59 a 0:02:09), e lembra que o foco não é só mexer no código, é olhar o processo mental (aula 9, 0:11:50 a 0:12:00). A ressalva aparece na aula 16: quem achou que o treinamento era sobre recursos do Python, ele não cumpriu a tarefa (aula 16, 0:00:45 a 0:01:02).

### 2.3 O passo prático que faltava ao Refatoração na Prática

Ele diz que a experiência com a turma de Refatoração na Prática foi boa porque quebrava a refatoração na sua essência, mas que a essência não basta: é preciso entender como canalizá-la em ação no dia a dia, e este curso complementa aquilo (aula 2, 0:00:18 a 0:00:42). O código da prática foi compartilhado por um aluno durante Refatoração na Prática e foi o que lhe deu a ideia do treinamento (aula 5, 0:00:59 a 0:01:03; 0:03:28 a 0:03:40). Naquele curso, segundo o digest `kb/courses/refatoracao-na-pratica.md`, ele analisou o mesmo programa sem mexer em nada e ditou 84 TODOs como plano para o aluno (aula #30, 0:21:01; aula #32, 0:00:57). Aqui ele faz a refatoração ao vivo, e vários desses TODOs viram código (seção 8).

### 2.4 Proibir orientação a objeto e padrões

Ele exigiu que o treinamento todo não usasse orientação a objeto (aula 16, 0:01:51 a 0:01:58). O motivo, dito no fecho: sem ficar preso à estrutura de classe tentando encaixar as coisas, ficaram abstrações e conceitos específicos, os tijolinhos, e a classe passa a ser um detalhe, uma escolha posterior (aula 16, 0:02:08 a 0:02:55). A mesma recusa vale para padrões de projeto: quem começa tenta decorá-los e encaixá-los (aula 3, 0:02:50 a 0:03:04), e no meio da prática ele manda esquecer padrões e começar com a função, que todo mundo aprende (aula 12, 0:10:56 a 0:11:06). Quando um aluno pede um tipo Coordenada, ele recusa: hoje é dia de fluxo, não de estrutura (aula 8, 0:07:56 a 0:08:09).

### 2.5 Aula ao vivo, com a turma no microfone

A parte prática é uma sessão com turma, e as aulas começam e terminam no meio da fala (aula 14, 0:00:06; aula 15, 0:00:01). Ele pede que puxem o microfone se errar algo enquanto codifica (aula 9, 0:01:49) e responde perguntas no meio da refatoração: sobre lógica no teste (aula 7, 0:06:03 a 0:06:54), sobre dependência do teste em relação ao código (aula 10, 0:02:36 a 0:03:06), sobre tirar uma repetição cedo demais (aula 11, 0:03:06 a 0:03:54), sobre Enum (aula 15, 0:23:52 a 0:24:22) e sobre geradores (aula 12, 0:19:38 a 0:25:03).

### 2.6 O contexto de carreira

A aula 2 é quase toda contexto: vaga boa é a que rende como juros compostos (0:01:41 a 0:02:13); quem fica preso em trabalho que não progride está no vale das sombras (0:04:03 a 0:04:21); o validador só quer saber o que se prova que entrega de resultado (0:08:56 a 0:09:35), por isso currículo que lista linguagem tem que ser rasgado (0:09:40). A carreira antifrágil, conceito tomado do livro de Nassim Taleb, sabe como vai dominar uma tecnologia desconhecida e nunca começa do zero (0:14:34 a 0:18:36). Para fortalecer um pilar fraco, ele recorta o problema e aprofunda as definições dentro desse escopo reduzido (0:19:37 a 0:21:38). A refatoração é o elemento-chave para construir a ponte sobre o vale (aula 1, 0:01:43 a 0:01:59).

## 3. Pilares conceituais

### 3.1 Fluxo antes de estrutura

Fluxo é o processo de transformação dos dados, o código em movimento; o código no editor é uma foto, o código rodando é um filme (aula 4, 0:00:46 a 0:01:22). Quem começa olha só a estrutura e não olha o fluxo (aula 3, 0:02:39 a 0:02:46), e quem fica na estrutura acaba com o código pinball (aula 4, 0:02:06 a 0:02:47). A ordem de trabalho é entender a estrutura, a partir daí entender o fluxo, e mudar a estrutura para manter o fluxo (aula 4, 0:03:33 a 0:03:41). Na prática a tese reaparece como bordão: hoje é dia de fluxo, não de estrutura (aula 8, 0:08:07); saindo da lógica e das etapas para esculpir um fluxo único semântico (aula 12, 0:09:10 a 0:09:23); só get item e set item tocam o board, todo o resto foca no fluxo (aula 15, 0:00:52 a 0:01:10); trocou-se o algoritmo e a estratégia e tudo funcionou porque a estrutura está isolada do fluxo (aula 14, 0:47:30 a 0:47:40).

### 3.2 Isolamento, interação e impacto

Para alcançar o degrau do fluxo, ele olha três elementos que representam relações: impacto, interação e isolamento (aula 4, 0:08:00 a 0:08:24). A análise é fractal, parte por parte, porque não dá para olhar o código como um todo (aula 4, 0:10:23 a 0:10:36). Os três voltam como justificativa a cada decisão: o teste pela representação trabalha isolamento, equilibra a interação e reduz o impacto (aula 7, 0:10:57 a 0:11:04); o mock reduz o impacto do teste e cria isolamento (aula 13, 0:01:05 a 0:01:13). No fim da aula 15 ele os nomeia como os três critérios que guiaram tudo, sem precisar saber design nem orientação a objeto (0:37:38 a 0:38:09), e a aula 16 abre e fecha com eles: o curso é sobre a sensibilidade de construir abstrações identificando isolamento, interação e impacto nos quatro degraus da escadaria (0:01:04 a 0:01:23), e essa sensibilidade governa qualquer padrão, estratégia ou paradigma (0:34:48 a 0:35:05).

### 3.3 Rodar, cercar com teste, só então mudar

A primeira coisa é rodar: tem que funcionar, tem que rodar o código (aula 3, 0:03:06). Ele executa o programa antes de ler (aula 5, 0:05:24 a 0:05:47), lê pelo ponto de entrada simulando a execução em vez de olhar banco, classes ou modelo (aula 6, 0:01:00 a 0:01:33) e pergunta como mudar aquilo em segurança (aula 6, 0:04:18). O teste fica na fronteira certa: o primeiro, que mede linhas e colunas, depende da estrutura interna e é descartado (aula 7, 0:03:17 a 0:03:56); o segundo compara uma representação em string, que não tem relação com a estrutura (aula 7, 0:04:00 a 0:04:13; 0:10:45 a 0:10:57). Cada comando ganha um teste que passa com o código como está, e só então ele mexe (aula 8, 0:01:31 a 0:01:35). Rodar na mão é aceitável; depender de rodar na mão é o problema (aula 7, 0:08:04 a 0:08:08).

### 3.4 Esconder a implementação e deixar o padrão aparecer

A mudança de estado do board passa por uma função de propósito específico, e o código passa a se ler como uma frase (aula 8, 0:04:48 a 0:05:15). A conversão entre o índice da interface, que começa em um, e o do board, que começa em zero, fica com quem guarda o detalhe de implementação (aula 9, 0:04:04 a 0:05:00). Dependência sempre existe; o problema é quantas coisas prendem e se elas se acumulam (aula 8, 0:09:10 a 0:09:28; aula 10, 0:02:49 a 0:03:06). As repetições têm ritmo: a primeira chama a atenção e ele segue (aula 10, 0:06:12 a 0:06:20); a segunda deixa duas funções muito parecidas, e mexer na interface antes de mudar todas quebraria tudo (aula 11, 0:02:59; 0:03:14 a 0:03:51); a terceira revela o padrão, e uma abstração resolve todas as anteriores (aula 12, 0:02:08 a 0:02:15; 0:04:00 a 0:04:06). O `for` usado indiscriminadamente amarra as estruturas, e a navegação num retângulo vira um gerador (aula 12, 0:04:58 a 0:05:18). É o que já criticava na aula 4: o não se repita aplicado por mantra, sem olhar o propósito (0:10:12 a 0:10:21).

### 3.5 A decisão como parâmetro e a classe por último

O algoritmo de preenchimento calcula coordenadas e depende da estrutura do board: são duas responsabilidades (aula 14, 0:27:50 a 0:28:05). Ele o separa em uma chamadora que conhece o board e um algoritmo genérico que recebe as funções inside e match, por inversão de dependência, como o sort do Python recebe a chave (aula 14, 0:31:47 a 0:32:11). Com isso troca a estratégia de vizinhança e depois a implementação inteira, de recursiva para iterativa, sem quebrar os testes (aula 14, 0:39:59 a 0:40:08; 0:47:30 a 0:47:40). Quando o acoplamento é inevitável, como o `open` que amarra o código ao disco, o mock entra (aula 13, 0:05:25 a 0:05:52). A interface externa manda: o comando não conhece coordenada, então a coordenada não aparece nessa fronteira (aula 15, 0:30:18 a 0:30:39). E a classe vem depois das abstrações: com os tijolinhos prontos, Coordinate e Board ficam fáceis de escrever (aula 16, 0:02:08 a 0:02:55), mas o importante foi explicitar as fronteiras (aula 16, 0:03:40 a 0:03:48).

## 4. As aulas em uma tabela

| # | Título | Duração | Foco em uma linha |
|---|---|---|---|
| 1 | Domine o Método da Refatoração Rápida #01: Por Que Estamos Aqui? | 3:09 | Abertura: vale das sombras, carreira antifrágil, refatoração; baby steps desde 2010 (0:02:04). |
| 2 | Mastering the Rapid Refactoring Method #02: The Context | 22:51 | Rápido de progredir, não de fazer (0:00:47); validador, carreira antifrágil, aprender recortando o problema. |
| 3 | Domine o Método da Refatoração Rápida #03: A refatoração | 4:31 | Refatorar é enxergar o invisível (0:00:29); quem começa olha estrutura, não fluxo (0:02:42). |
| 4 | Domine o Método da Refatoração Rápida #04: Entendendo o Fluxo | 19:34 | Estrutura, fluxo, mudar a estrutura mantendo o fluxo (0:03:33); impacto, interação e isolamento (0:08:11). |
| 5 | Domine o Método da Refatoração Rápida #05: As Oportunidades do Legado | 7:21 | Apresenta o editor de matriz de pixels de um aluno e o roda antes de ler (0:05:42). |
| 6 | Domine o Método da Refatoração Rápida #06: Reconhecendo o Código Legado | 5:48 | Ler pelo ponto de entrada simulando a execução (0:01:08); como mudar em segurança (0:04:18). |
| 7 | Domine o Método da Refatoração Rápida #07: A Fronteira de Um Bom Teste | 20:31 | Testar por uma representação, não pela estrutura interna (0:10:45); primeira refatoração da criação. |
| 8 | Domine o Método da Refatoração Rápida #08: Encapsule a Mudança de Estado | 11:57 | Mudança de estado atrás de uma função de propósito único (0:04:48); hoje é dia de fluxo (0:08:07). |
| 9 | Domine o Método da Refatoração Rápida #09: Oculte os Detalhes de Implementação | 12:49 | Índice base 1 fora, base 0 dentro (0:04:04); um teste que passou por coincidência (0:10:28). |
| 10 | Domine o Método da Refatoração Rápida #10: Uma Repetição Desperta a Atenção | 6:24 | Fixture do pytest; dependência sempre existe (0:02:49); primeira repetição (0:06:12). |
| 11 | Domine o Método da Refatoração Rápida #11: Duas Repetições Apontam um Sintoma | 3:56 | Vertical e horizontal ficam quase iguais (0:02:59); um andar de análise de cada vez (0:03:14). |
| 12 | Domine o Método da Refatoração Rápida #12: Três Repetições Permitem a Generalização | 25:11 | Tudo é retângulo; a navegação sai do `for` para o gerador `region` (0:05:43); geradores no terminal. |
| 13 | Domine o Método da Refatoração Rápida #13: Quando O Acoplamento É Inevitável: Mock | 6:19 | Mock do `open` para o teste do Save (0:01:05); o `open` cria acoplamento com o disco (0:05:25). |
| 14 | Domine o Método da Refatoração Rápida #14: O Poder de Abstração dos Algoritmos | 48:35 | Fill separado da estrutura; flood genérico recebe inside e match como o sort (0:31:56). |
| 15 | Domine o Método da Refatoração Rápida #15: Divida Responsabilidades para Conquistar Qualidade | 41:29 | API com o board primeiro, parse, despacho por dicionário, invoke; os três critérios (0:37:38). |
| 16 | Domine o Método da Refatoração Rápida #16: A Mágica da API de Alto Nível | 38:15 | Abstrações antes de classes (0:02:13); a API reaproveitada num Game of Life escrito na hora. |

## 5. Resumo por aula

### Aula 1: Domine o Método da Refatoração Rápida #01: Por Que Estamos Aqui?
Vídeo: https://www.youtube.com/watch?v=8DG_a8lPbbo · Duração: 3:09

Resumo: abertura do programa. Ele conta que, em mais ou menos um ano e meio, chegou muita gente nova a Python pela onda de data science e que essa turma tem dificuldade de fazer a ponte entre os conceitos e se sente insegura mesmo conseguindo trabalhar o material (0:00:24 a 0:00:53). Depois de pesquisar e revisitar livros, decidiu mergulhar nos fundamentos e anuncia três tópicos a amarrar: o vale das sombras do mercado, a carreira antifrágil e a refatoração como elemento-chave para construir uma ponte sobre esse vale (0:01:01 a 0:01:56). Diz que usa desde o primeiro treinamento, em 2010, um processo de passos de bebê [provável: baby steps] com ciclo de feedback intensivo, que quebra a visão de programação como coisa genial em que é preciso ter tudo na cabeça (0:02:04 a 0:02:38). Fecha dizendo que este é o primeiro de uma série sobre os processos que o deixam aprender coisas novas rápido (0:02:41 a 0:03:00).

Linha do tempo:
- [0:00:02] boas-vindas ao método da refaturação [provável: refatoração] rápida
- [0:00:15] lembra o e-mail sobre o vale das sombras do mercado de tecnologia
- [0:00:28] a turma nova vinda de data science com Python e a dificuldade de fazer a ponte entre conceitos
- [0:01:01] decide mergulhar no que chama de fundamentos
- [0:01:13] anuncia os três tópicos: vale das sombras, carreira antifrágil, refatoração
- [0:01:43] a refatoração como elemento-chave para construir a ponte sobre o vale
- [0:02:04] o primeiro treinamento, em 2010, já usava passos de bebê [provável: baby steps] e ciclo de feedback intensivo
- [0:02:22] quebra a visão antiga de programação genial, de saber tudo de cabeça
- [0:02:41] atenção aos processos que permitem aprender coisas novas muito rápido
- [0:02:58] o programa é a primeira iniciativa de uma série

Princípios:
- Processo em vez de genialidade: focar num processo de passos pequenos com feedback intensivo dispensa a grande estrutura cognitiva de saber tudo de cabeça (0:02:08 a 0:02:41).
- A refatoração é o elemento-chave para atravessar o vale das sombras e mudar a relação com a programação (0:01:43 a 0:01:59).

Código: nenhum.

Citações (paráfrases de legenda, não verificadas):
- [0:02:04] o concedidiano que eu fiz né o primeiro treinamento que eu dei em 2010 [provável: Welcome to the Django; leitura incerta]
- [0:02:08] eu uso esse processo de passos de beber ciclo feedback intensivo [provável: passos de bebê, baby steps]
- [0:02:22] quebra aquela visão antiga de programação como uma coisa genial você tem que ter tudo na cabeça
- [0:02:32] a Gente para com essa essa necessidade de uma grande estrutura cognitiva

### Aula 2: Mastering the Rapid Refactoring Method #02: The Context
Vídeo: https://www.youtube.com/watch?v=5aSxy_AO0fk · Duração: 22:51

Resumo: apesar do título em inglês, a aula é falada em português. Ele conceitua o método: refatoração rápida não é rápida de fazer, porque programar é lento, mas é rápida de progredir, sem travar; os dois fracassos comuns ao refatorar são trabalhar a estética pela estética ou travar por não saber qual a coisa certa a fazer (0:00:44 a 0:01:13). O resto da aula é o contexto de carreira: só um subconjunto das vagas é bom, e vaga boa é a que rende como juros compostos (0:01:41 a 0:02:13); quem fica preso em trabalho que não progride está no vale das sombras (0:04:03 a 0:04:21); para sair dele é preciso passar pelo validador, que só quer saber o que você prova que entrega de resultado (0:08:56 a 0:09:35), por isso currículo que lista linguagem e quadradinho colorido do GitHub não provam nada, e sim a história ancorada em fatos (0:09:40 a 0:11:30). A ponte é sustentada por esforço pessoal e por reputação numa rede, combinação que constrói a carreira antifrágil, conceito que ele toma do livro de Nassim Taleb (0:13:07 a 0:16:22). O antifrágil sabe como vai dominar uma tecnologia desconhecida, conhece a própria forma de aprender e nunca começa do zero (0:16:55 a 0:18:36). Para fortalecer um pilar fraco ele recorta o problema e aprofunda as definições dentro desse escopo reduzido, em ciclo de interação, em vez de estudar a base de forma abstrata (0:19:37 a 0:21:38); exemplo: o React funciona como o Excel, sistemas reativos que já existiam nos anos 70, e programar por dogma é abrir mão da responsabilidade pela decisão (0:21:41 a 0:22:43).

Linha do tempo:
- [0:00:01] conceitua o método da Refrigeração [provável: Refatoração] rápida
- [0:00:44] rápido de progredir, não de fazer, porque programar é lento
- [0:01:01] os dois fracassos: estética pela estética ou travar sem saber a coisa certa
- [0:01:41] vagas boas como subconjunto de todas as vagas; rendimento de juros compostos
- [0:04:08] define o vale das sombras
- [0:08:56] o validador: porteiro, guardião, alfândega
- [0:09:40] currículo que lista linguagem tem que ser rasgado; vale a história de resultado
- [0:13:07] a ponte no Vietnã sustentada por duas mãos: esforço e pessoas
- [0:14:34] recomenda o livro Antifrágil, de Nassim Taleb
- [0:16:01] o que é a carreira antifrágil: não desmorona se mudar tecnologia ou projeto
- [0:20:37] estudar a base recortando o problema em vez de voltar ao livro do colégio
- [0:21:41] React funciona igual Excel; sistemas reativos dos anos 70; programação por dogma

Princípios:
- Refatorar para progredir, não para enfeitar: o método evita a refatoração estética pela estética e a paralisia de não saber o próximo passo (0:00:56 a 0:01:13).
- Resultado entregue é a única prova que o mercado aceita: histórias ancoradas em fatos valem mais que lista de linguagens ou atividade no GitHub (0:09:29 a 0:09:51; 0:11:22 a 0:11:30).
- Aprender recortando o problema: reduzir o escopo, aprofundar nas definições dentro dele e iterar, em vez de estudar a base em abstrato (0:20:40 a 0:20:58).
- Procurar a essência por trás da novidade, como no caso React e Excel (0:21:51 a 0:22:14).
- Toda decisão é responsabilidade de quem decide; seguir regra por dogma não isenta (0:22:20 a 0:22:43).

Código: nenhum. Ele mostra slides com fotos (a ponte das mãos, um pilar antigo) e a capa do livro, só descritos em fala.

Citações (paráfrases de legenda, não verificadas):
- [0:00:47] Apesar do nome rápido né ele não é rápido de fazer porque programar é lento mas é rápido de progredir
- [0:01:03] o bicho escorrega para aquela questão de ficar trabalhando a parte estética pela parte estética ou trava
- [0:09:40] currículo de programador que lista a linguagem tem que ser rasgado
- [0:22:37] p800 que dá problema sou eu eu digo o que que é melhor que não é toda decisão eu tenho que me responsabilizar pelo processo [provável: PEP 8; trecho confuso]

### Aula 3: Domine o Método da Refatoração Rápida #03: A refatoração
Vídeo: https://www.youtube.com/watch?v=ybTuYdnEXAs · Duração: 4:31

Resumo: para construir uma carreira antifrágil e chegar à senioridade é preciso fundações sólidas, e para ele a refatoração é ferramenta crucial para trabalhar e aprender, porque é o processo pelo qual você se acostuma a enxergar o invisível no código, as relações invisíveis (0:00:00 a 0:00:39; 0:01:38 a 0:01:46). Refatoração não é novidade: desde a década de 60 se discute como organizar código, e houve a conferência da OTAN sobre a crise do software; inovação é alguém subir no ombro de gigantes, como dizia Newton (0:00:45 a 0:01:38). Aponta dois problemas no universo da refatoração: o Java, com sua pretensa orientação a objetos, e os padrões de projeto, porque todo mundo tenta decorá-los, olha só a estrutura e não o fluxo, e tenta encaixar padrão (0:01:46 a 0:03:04). O que importa é rodar o código e desenvolver a capacidade de observar a necessidade e a emergência dessas técnicas, já que OO e padrões emergiram de problemas reais e concretos (0:03:06 a 0:03:56). Ressalva que o Java é legal; o problema é a junção Java e universidade formando gente para fábrica de software (0:04:00 a 0:04:19).

Linha do tempo:
- [0:00:02] carreira antifrágil e a ponte para a senioridade pedem fundações sólidas
- [0:00:19] refatoração como ferramenta crucial para trabalhar e aprender
- [0:00:29] refatorar é acostumar-se a enxergar o invisível no código
- [0:00:50] o tema existe desde os anos 60; a crise do software e a reunião da OTAN
- [0:01:28] ombro de gigante, citando Nilton [provável: Newton]
- [0:01:46] os dois problemas malditos: Java com pretensa OO e padrões de projeto
- [0:02:39] quem começa olha só a estrutura, não o fluxo
- [0:02:50] padrões foram catalogados porque emergem naturalmente; as pessoas ficam loucas tentando encaixar
- [0:03:06] tem que funcionar, tem que rodar o código
- [0:03:24] a síndrome do arquiteto astronauta e seus diagramas
- [0:03:39] observar a necessidade e a emergência dos padrões, que vieram de problemas concretos
- [0:04:03] o problema é a junção Java com universidade, não o Java

Princípios:
- Refatorar é aprender a ver as relações invisíveis do código (0:00:29 a 0:00:35; 0:01:38 a 0:01:46).
- Fluxo antes de estrutura: quem só olha a estrutura (classes, atributos, público ou privado) não vê o fluxo (0:02:42 a 0:02:50; 0:03:22 a 0:03:37).
- Não encaixar padrão de projeto; deixar emergir: padrões e OO nasceram de problemas reais, então a habilidade é perceber quando o código os pede (0:02:50 a 0:03:56).
- Primeiro rodar: o código tem que funcionar antes de qualquer preocupação estrutural (0:03:06 a 0:03:10).

Código: nenhum.

Citações (paráfrases de legenda, não verificadas):
- [0:00:29] é o processo pelo qual você se acostuma a enxergar o que é de invisível no código
- [0:01:53] o Java com a sua pretensa orientação objetos e os padrões de projeto são dois desgraça que tem nesse mundo porque todo mundo fica tentando decorar
- [0:03:06] tem que funcionar tem que rodar o código
- [0:03:39] a gente precisa na verdade é criar a capacidade de observar a necessidade e a emergência desses padrões

### Aula 4: Domine o Método da Refatoração Rápida #04: Entendendo o Fluxo
Vídeo: https://www.youtube.com/watch?v=KUPOImm5rbs · Duração: 19:34

Resumo: aula conceitual sobre estrutura versus fluxo. Fluxo é o processo de transformação dos dados, o código em movimento; o código no editor é uma foto, o código rodando é um filme, e TDD é um artifício para ver os sintomas do que escrevemos rodando (0:00:46 a 0:01:22). Quem fica na estrutura acaba com o código pinball, cheio de efeitos colaterais em vários lugares (0:01:59 a 0:02:47); a ordem de trabalho é entender a estrutura, daí o fluxo, e então mudar a estrutura para manter o fluxo (0:03:34 a 0:03:41). Propõe uma escada de quatro degraus de maturidade: código (sintaxe), lógica, etapas da solução e fluxo, que é ver a relação entre os três e desconstruir o roteiro do filme (0:03:47 a 0:06:51). Para chegar ao fluxo, olha três elementos: interação, impacto e isolamento, analisados de forma fractal, parte por parte (0:08:11 a 0:10:36). Critica o mantra do não se repita aplicado sem olhar quais casos acontecem sempre e quais são especiais (0:09:56 a 0:10:21). Amplia a complexidade ciclomática para além do grafo de chamadas: é preciso considerar a mutação do runtime, quem transforma cada objeto em memória, e isso dá sensibilidade ao risco de cada estratégia (0:11:02 a 0:14:12). Refatorar dá repertório de arranjos que reduzem arestas, melhoram isolamento, reduzem impacto e organizam interação; o software é um organismo vivo e o programador age como médico que não pode matar o paciente (0:14:21 a 0:15:34). Depois do comentário de um aluno sobre a metáfora do médico (0:16:05 a 0:16:44, fala do aluno, não dele), ele responde que a metáfora ajuda a acabar com o papo de programação genial e que a restrição cria a criatividade, com o exemplo do filme Apollo 13, nome corrigido pela turma (0:16:47 a 0:19:12).

Linha do tempo:
- [0:00:01] estrutura versus fluxo; o um forzinho resolve que os alunos dizem
- [0:00:46] fluxo é a transformação dos dados; por isso TDD
- [0:01:13] a foto e o filme
- [0:02:06] o código pinball
- [0:03:22] botar luva e máscara: entender estrutura, depois fluxo, depois mudar estrutura
- [0:03:47] os quatro degraus: código, lógica, etapas, fluxo
- [0:08:11] os três elementos: impacto, interação e isolamento
- [0:10:15] crítica ao mantra não se repita aplicado a casos especiais
- [0:11:02] complexidade ciclomática e grafo de chamadas
- [0:12:37] considerar a evolução e a mutação do runtime
- [0:14:54] calibrar o triângulo o tempo todo; software como organismo vivo; o médico
- [0:17:28] restrição cria criatividade; Apollo 13 (corrigido pela turma, de Apollo 11)

Princípios:
- Fluxo antes de estrutura: classe e atributos são palpáveis mas não importantes; o fluxo invisível determina o resto (0:01:38 a 0:01:57; 0:01:59 a 0:02:09).
- Entender estrutura, entender fluxo, mudar a estrutura para manter o fluxo (0:03:34 a 0:03:41).
- Interação, impacto e isolamento como lentes para qualquer trecho de código, aplicadas de forma fractal (0:08:20 a 0:08:24; 0:10:23 a 0:10:36).
- Repetição só se generaliza olhando o propósito: se só um caso acontece sempre e os outros são especiais, a deduplicação mal direcionada gasta energia errada (0:10:00 a 0:10:21).
- Complexidade inclui o estado em memória: quem muta o objeto, em um ou em vários lugares (0:13:06 a 0:13:21).
- Software é organismo vivo; tome decisões que reduzam o risco de crise, como médico que não pode matar o paciente (0:15:16 a 0:15:34).
- A arquitetura nunca está pronta: é calibração contínua, como andar de bicicleta (0:14:56 a 0:15:15).

Código: nenhum. Ele mostra um slide com um grafo de chamadas como exemplo de complexidade ciclomática (0:11:30), só descrito pela fala.

Citações (paráfrases de legenda, não verificadas):
- [0:00:48] o fluxo é o processo de transformação dos dados é o código em movimento
- [0:01:16] porque o código rodando é um filme O Código no editor de texto é uma foto
- [0:03:37] para partir daí você entender o fluxo e aí você mudar a estrutura para manter o fluxo
- [0:15:16] Finja que você quer ser um bom programador Finjo que você é um médico que não pode matar o paciente e trate o software como organismo vivo

### Aula 5: Domine o Método da Refatoração Rápida #05: As Oportunidades do Legado
Vídeo: https://www.youtube.com/watch?v=u988rWb2gYw · Duração: 7:21

Resumo: começo da parte prática (hands-on) com código legado. Ele conta que o código foi compartilhado com ele por um aluno durante o Refaturação na Prática [provável: Refatoração na Prática], que o achou incrível por mostrar um processo claro de aprendizagem e que foi esse código que lhe deu a ideia do treinamento (0:00:19 a 0:01:03; 0:03:28 a 0:03:59). Avisa que vai mostrar passo a passo como pensa, em baby steps (0:01:59 a 0:02:09). Abre o código no PyCharm [legenda: pai Charme] e lê o README: um programa que, dada uma matriz M por N em que cada elemento é um pixel, lê comandos e manipula a matriz: C limpa, L pinta um pixel, V e H desenham segmentos vertical e horizontal, K desenha um retângulo, F preenche uma região de mesma cor, S salva e X sai (0:04:22 a 0:05:24). Roda o programa ao vivo: cria uma matriz 4 por 5, pinta pixels com W e usa o preenchimento, que pinta os zeros sem invadir a área W (0:05:38 a 0:06:58). Fecha dizendo que parece bobinho mas não é (0:07:11 a 0:07:19).

Linha do tempo:
- [0:00:19] hands-on [legenda: Hands]: vai trabalhar com código legado
- [0:00:36] o código foi generosamente compartilhado; mostra um processo claro de aprendizagem
- [0:00:59] esse código deu a ideia do treinamento
- [0:01:59] vai mostrar passo a passo como pensa, em steps [provável: baby steps]
- [0:03:01] compartilha a tela com o pai Charme [provável: PyCharm]
- [0:03:28] o código veio de um aluno durante o Refaturação na Prática [provável: Refatoração na Prática]
- [0:04:22] lê o README: matriz de pixels e comandos
- [0:04:50] os comandos C, L, V, H, K, F, S, X
- [0:05:42] roda: cria a matriz 4 por 5 e pinta pixels
- [0:06:35] o comando F faz o preenchimento por inundação
- [0:07:11] parece bobinho, mas não é

Princípios:
- Executar o programa antes de mexer: primeiro ver o comportamento rodando (0:05:24 a 0:05:31; 0:05:42 a 0:07:08).
- Legado como oportunidade de aprendizagem: o código de um aluno mostra um processo claro de aprendizagem e serve de matéria-prima do treinamento (0:00:48 a 0:01:03).

Código: o programa legado de um aluno, um editor de matriz de pixels por comandos, é mostrado na tela e executado, mas não publicado; é código de aluno e esta documentação não o reproduz. A legenda dá o nome do programa como Change (0:04:31) [leitura incerta]. Nenhum trecho reconstruível; só os comandos lidos do README.

Citações (paráfrases de legenda, não verificadas):
- [0:00:52] Eles prestam um processo muito claro de aprendizagem para aprendizagem [legenda confusa]
- [0:00:59] e foi esse código que me deu a ideia de fazer esse treinamento aqui com vocês
- [0:02:01] passo a passo que eu penso e como eu penso na coisa então a gente vai vamos aqui bem steps [provável: baby steps]
- [0:07:11] parece bobinho não parece bobinho mas não é

### Aula 6: Domine o Método da Refatoração Rápida #06: Reconhecendo o Código Legado
Vídeo: https://www.youtube.com/watch?v=47E3ruksHBQ · Duração: 5:48

Resumo: no PyCharm, ele cria logo um arquivo de teste e mostra que o projeto tem um arquivo de testes rodado com pytest, mas vazio (0:00:11 a 0:00:59). Para entender a estrutura, começa pelo ponto de entrada e simula a execução, em vez de olhar banco, classes ou modelo; assim descobre o código emulando o comportamento (0:01:00 a 0:01:33). Percorre o main: um loop que lê o comando e, numa cadeia de ifs, mapeia cada letra para uma função; o X sai do loop, o I chama a função que cria a matriz (0:01:35 a 0:02:16). A criação monta uma lista de listas, a de fora para linhas e a de dentro para colunas, preenchida com zero representando o vazio (0:02:30 a 0:03:21). Elogia o uso do editor para navegar (0:03:42 a 0:03:47). Pergunta como mudar o código com segurança; a turma responde testes, e ele aponta que um teste de saída em loop (golden file [provável]) funciona, mas o código está acoplado ao loop de interface: ou se ignora essa camada e testa cada função, ou se mexe no loop para testar emulando o usuário, o que seria um teste de aceitação e de integração ao mesmo tempo (0:04:10 a 0:05:43).

Linha do tempo:
- [0:00:00] abre o pai Charme [provável: PyCharm]
- [0:00:11] cria já na largada um arquivo de teste
- [0:00:48] o pai teste [provável: pytest] roda e os testes estão vazios
- [0:01:00] entender a estrutura indo para onde a coisa começa
- [0:01:08] analisar fluxo é simular a execução, não olhar banco, classes ou modelo
- [0:01:35] o main com loop lendo comandos; o if mapeia letras para funções
- [0:02:27] a função que cria a matriz: lista de listas preenchida com zero
- [0:03:42] navega usando o editor
- [0:04:10] qual a pegadinha: como mudar com segurança
- [0:04:49] golden file [provável] funciona, mas é preciso romper o loop
- [0:05:02] o código está absolutamente acoplado à interface do usuário
- [0:05:27] teste de aceitação e de integração ao mesmo tempo

Princípios:
- Ler pelo ponto de entrada, emulando a execução: começar onde o programa começa e simular o comportamento, não passar o olho pela estrutura (0:01:04 a 0:01:33).
- Antes de mudar, ter como mudar com segurança: testes (0:04:18 a 0:04:28).
- Acoplamento à interface do usuário impede o teste; é preciso romper o loop ou testar abaixo dele (0:04:57 a 0:05:25).

Código: o código legado é mostrado na tela, não publicado. É código de aluno e não é reproduzido aqui; a fala só descreve a ideia da criação da matriz, uma lista de listas preenchida com zero (0:02:30 a 0:03:21).

Citações (paráfrases de legenda, não verificadas):
- [0:01:08] fluxo eu preciso simular Como se eu tivesse executando o programa
- [0:01:28] ao invés de se perder na passada de olho você vai descobrindo o código emulando o comportamento execução do código
- [0:04:18] como é que eu faço para mudar esse cara em segurança
- [0:04:57] romper com esse look aqui porque esse código está absolutamente acoplado [provável: loop]

### Aula 7: Domine o Método da Refatoração Rápida #07: A Fronteira de Um Bom Teste
Vídeo: https://www.youtube.com/watch?v=atl0Q0iG84Y · Duração: 20:31

Resumo: escolhe a interface antes e começa do começo, com um teste da criação do board: deduz pelo fluxo que a função recebe dois parâmetros, 4 e 5 (0:00:00 a 0:01:35). O primeiro teste afirma que o board tem 5 linhas e 4 colunas e passa, mas ele pergunta se é bom: o teste não está isolado, porque depende da estrutura interna; se a criação inverter linhas e colunas, quebra (0:01:54 a 0:03:56). Sobe o nível criando uma representação em string do board, extraída do print que o programa já faz no fim, e compara com uma string literal usando dedent (0:04:06 a 0:09:32). A uma pergunta sobre pôr lógica no teste, responde que o risco existe, mas o sistema legado já funciona e ele o está desconstruindo; o ciclo é em baby steps, sem sair testando tudo (0:06:03 a 0:06:54). Rodar na mão não é problema; depender de rodar na mão é (0:07:37 a 0:08:11). A representação não tem relação com a estrutura interna, então o teste testa a interface e o detalhe de implementação não o afeta, o que trabalha isolamento, interação e impacto (0:10:18 a 0:11:09; 0:13:12 a 0:13:37). Depois refatora a criação: troca a ordem para coluna e linha, converte para inteiro no preparo da entrada para errar antes de entrar no algoritmo, extrai o número mágico para a constante BLANK e o torna parâmetro com valor padrão, que chama de inversão de dependência, e troca o for com append por compreensão de lista, explicando por que repetir um valor imutável é seguro (0:14:27 a 0:18:41). Deixa um TODO em vez de mexer nas camadas de cima, para manter interfaces bem delimitadas e contratos explícitos, indo passo a passo (0:19:18 a 0:20:29).

Linha do tempo:
- [0:00:00] escolher a interface antes e começar do começo
- [0:00:30] deduz pelo fluxo que a criação recebe 4 e 5
- [0:01:57] primeiro teste: tamanho 5 e tamanho da linha 4
- [0:03:17] o teste não está isolado: depende de como a criação funciona por dentro
- [0:04:06] criar uma representação, aproveitando o print do board
- [0:06:03] pergunta da turma sobre lógica no teste; resposta sobre legado e baby steps
- [0:07:55] rodar na mão não é problema; depender de rodar na mão é
- [0:08:54] usa dedent [legenda: dente] para escrever a string esperada
- [0:10:18] a representação não tem relação com a estrutura interna
- [0:14:37] refatora a criação: índices, conversão para inteiro, erro antes do algoritmo, constante BLANK
- [0:17:04] for com append vira compreensão de lista; repetição de valor imutável
- [0:19:21] deixa um TODO: interfaces delimitadas, contratos explícitos, passo a passo

Princípios:
- Teste a interface, nunca a estrutura interna: detalhe de implementação não pode afetar o teste (0:10:45 a 0:10:57; 0:13:12 a 0:13:30).
- Suba a distância entre teste e implementação com uma representação do objeto (0:03:56 a 0:04:13; 0:10:22 a 0:10:31).
- Teste preso à implementação está preso à estrutura e não respeita o fluxo (0:13:30 a 0:13:39).
- Rodar na mão é aceitável como exploração, mas não se pode depender disso (0:07:55 a 0:08:11).
- Valide e converta a entrada antes do algoritmo, para errar antes e sem efeito colateral (0:15:17 a 0:15:47).
- Números mágicos viram constantes; a constante pode virar parâmetro com valor padrão (0:15:58 a 0:16:46).
- Não crie distração: variável não usada sai (0:16:54 a 0:17:00).
- Passo a passo, com contratos explícitos: não propague a mudança por todas as camadas de uma vez; anote o TODO e siga (0:19:55 a 0:20:29).

Código: reconstrução a partir da fala; o código não foi publicado nesta aula. Os nomes são leituras prováveis da legenda: a função de criação aparece como Crate, Creator, cream e crateray [provável: create ou create_array], a função de string como stream board e swing [provável: string_board], join como Johnny, append como atende, TODO como Dudu.

```python
# reconstrução a partir da fala, não publicada
from textwrap import dedent

BLANK = '0'  # valor do número mágico não legível na legenda

def create_array(cols, rows, value=BLANK):  # nome provável
    return [[value] * cols for _ in range(rows)]

def string_board(board):  # nome provável
    return '\n'.join(''.join(row) for row in board)

def test_create():
    board = create_array(4, 5)
    assert string_board(board) == dedent('''\
        0000
        0000
        0000
        0000
        0000''')
```

O primeiro teste, descartado por não ser isolado, era da forma `assert len(board) == 5` e `assert len(board[0]) == 4` (0:01:57 a 0:02:22).

Citações (paráfrases de legenda, não verificadas):
- [0:03:32] não tá isolado porque eu dependo de como o cliente aí funciona internamente para analisar essa estrutura aqui
- [0:08:07] rodar na mão não é um problema o problema é depender de rodar na mão
- [0:10:54] o detalhe de implementação não pode afetar os seus testes
- [0:13:30] o teste que amarra na implementação ele não respeita o fluxo ele tá preso a estrutura

### Aula 8: Domine o Método da Refatoração Rápida #08: Encapsule a Mudança de Estado
Vídeo: https://www.youtube.com/watch?v=Z1SY_-nn5mw · Duração: 11:57

Resumo: continuação ao vivo da refatoração do editor de matriz de pixels (o código legado apresentado na aula 5). Ele escreve o teste do comando de limpar: cria o board, suja todos os elementos com X e verifica que o Clear devolve tudo ao valor Blank; o teste passa de primeira porque o código já funcionava, e só então ele mexe com segurança (0:00:00 a 0:01:35). Aponta o problema da implementação: a lógica depende de como o board é estruturado, igual ao teste da aula anterior, então extrai a altura e a largura do board e uma função que atualiza uma coordenada, escondendo a ordem e a forma da estrutura atrás de um nome com propósito (0:02:17 a 0:05:32). Troca linha e coluna separadas por uma coordenada única em dupla, com funções x e y que amarram a definição em um lugar só, e recusa criar um tipo Coordenada porque hoje é dia de fluxo, não de estrutura (0:05:51 a 0:08:42). Responde que estar preso a algo não é o problema, o problema é a quantidade de coisas que prendem (0:09:03 a 0:09:36). Fecha registrando desconforto com o `for` sobre o `range` do board, que limita o entendimento, e a diferença entre o Clear, que muda a lista existente, e o Create, que cria listas novas (0:09:50 a 0:11:55).

Linha do tempo:
- [0:00:00] próximo passo: o comando Clear; monta o teste pegando o board criado
- [0:00:32] o Clear transforma tudo em zero de novo; reaproveita o Blank já extraído
- [0:00:51] suja o board com X para o teste não ficar só no cognitivo
- [0:01:31] teste passa porque o código já funcionava; agora pode mexer em segurança
- [0:02:17] qual o problema da implementação: impacto, isolamento e interação; a lógica depende da estrutura do board
- [0:03:03] extrai altura (High [provável: height]) e largura (Witch [provável: width]) do board
- [0:03:51] voz ativa de comando: quero o comprimento e a largura do board
- [0:04:04] cria a função que recebe coluna, linha e valor e atualiza a coordenada
- [0:04:48] a implementação fica escondida atrás de uma função de propósito específico; ler como uma frase
- [0:05:51] o board ter duas dimensões é detalhe de implementação; passa a coordenada como uma dupla
- [0:07:05] cria x e y da coordenada; a definição fica amarrada em um lugar só
- [0:07:52] recusa um tipo Coordenada: hoje é dia de fluxo, não de estrutura
- [0:09:03] não é problema estar preso; o problema é quantas coisas te prendem
- [0:09:50] não gosta do `for`: o range até o tamanho do board é limitante; deixa um TODO

Princípios:
- Antes de mexer, um teste que passa com o código como está; só então mexer em segurança (0:01:31 a 0:01:35).
- O teste concreto evita trabalhar só na cabeça: ele suja o board com X para ver o Clear funcionar (0:00:51 a 0:01:05).
- A lógica não deve depender da forma da estrutura; isolar a dependência atrás de funções (0:02:30 a 0:02:51).
- Esconder a implementação atrás de uma função com propósito específico, de modo que o código se leia como uma frase (0:04:48 a 0:05:15).
- Saber quantas dimensões o board tem é detalhe de implementação (0:05:53 a 0:06:06).
- Definição amarrada em um lugar: se tiver de mudar, muda num lugar só (0:07:39 a 0:07:45).
- Não introduzir estrutura (um tipo) quando o trabalho é de fluxo (0:07:52 a 0:08:09).
- Dependência sempre existe; o que importa é o número de pontos de contato (0:09:10 a 0:09:33).
- O `for` com range explícito limita o entendimento e amarra a estrutura (0:10:03 a 0:10:19).

Código (reconstrução a partir da fala, não publicada; nomes e índices inferidos das legendas, que dizem Clean Away, High, Witch e reflecto). O estado do board passa a ser mudado por uma única função:

```python
def height(board):
    return len(board)

def width(board):
    return len(board[0])

def x(coord):
    return coord[0]

def y(coord):
    return coord[1]

def set_item(board, coord, value):  # nome incerto
    board[y(coord)][x(coord)] = value

def clear_array(board, value=BLANK):
    for row in range(height(board)):
        for col in range(width(board)):
            set_item(board, (col, row), value)  # TODO: conhece muito sobre a estrutura do board
```

A ordem coluna, linha vem da fala em 0:04:29 (a coluna a linha e o valor). Os índices de x e y não são ditos.

Citações (paráfrases de legenda, não verificadas):
- [0:01:33] o código já estava funcionando mesmo agora eu posso mexer em segurança
- [0:05:05] não importa mais o que que é a implementação está escondida atrás daquela função que tem um propósito muito específico de atualizar uma coordenada do meu blog [provável: board]
- [0:08:07] hoje é dia de fluxo não é dia de estrutura
- [0:09:10] o problema não é ficar preso você sempre vai estar preso alguma coisa O problema é quantas coisas te prendem

### Aula 9: Domine o Método da Refatoração Rápida #09: Oculte os Detalhes de Implementação
Vídeo: https://www.youtube.com/watch?v=HgBuQSLtPCc · Duração: 12:49

Resumo: ele testa o comando de colorir um pixel (L), passando a entrada como uma lista de strings obtida com split, e faz o teste passar (0:00:00 a 0:02:01). Reescreve o color pixel no mesmo molde da aula anterior: converte os inteiros na entrada e delega à função que atualiza a coordenada (0:02:12 a 0:03:34). Percebe que o color pixel desconta um dos índices e o create não, o que revela que a interface do programa considera índices a partir de um e a implementação do board a partir de zero; decide que quem converte é a função que atualiza o board, que guarda o detalhe de implementação (0:03:39 a 0:06:31). Os testes continuam passando e ele estranha: investiga e descobre que o Clear passou por coincidência, porque o índice menos um pega o último elemento da lista; corrige os ranges para começar em um e ir até o tamanho mais um (0:06:47 a 0:11:15). Fecha dizendo que o foco é o processo mental, e que ao jogar o impacto para cima ele escolheu onde absorvê-lo, deixando a coisa esquisita mais evidente para tratar depois (0:11:48 a 0:12:46).

Linha do tempo:
- [0:00:25] teste do color pixel com entrada como lista de strings via split (linha, coluna e cor)
- [0:01:49] pede que a turma puxe o microfone se ele errar algo enquanto codifica
- [0:02:12] mesmo tratamento: converte para inteiro os campos zero e um, o dois fica a cor
- [0:03:17] o teste explode: três argumentos onde esperava quatro; faltavam os parênteses da dupla
- [0:03:39] o color pixel tem menos um, o create não: a interface começa em um, o board em zero
- [0:04:30] passo para trás: quem converte de um para o outro é a função de atribuir [legenda: o 7]
- [0:05:29] move o menos um para essa função; o color pixel passa só a coordenada
- [0:06:47] roda os testes, nada quebra; por que não quebrou?
- [0:09:12] usa o teste para investigar o fluxo no ponto certo
- [0:10:28] o menos um pega o último elemento: funcionou por coincidência
- [0:10:53] ajusta o range para ir de um até o tamanho mais um; elimina a coincidência
- [0:12:10] o impacto tem de ser absorvido em algum lugar; ele escolhe onde

Princípios:
- Ocultar o detalhe de implementação do board (índice a partir de zero) atrás da sua interface externa (índice a partir de um), e a conversão fica com quem guarda o detalhe (0:04:04 a 0:05:01).
- Uma coisa de cada vez (0:05:02 a 0:05:05).
- Teste que passa quando devia quebrar pede investigação: entender por que não quebrou é olhar o fluxo (0:06:47; 0:11:19 a 0:11:35).
- O teste ajuda a chegar ao ponto certo quando se quer entender algo (0:09:57 a 0:10:01).
- Eliminar coincidências: código que funciona por acaso não está certo (0:10:44; 0:11:15 a 0:11:19).
- O foco não é só mexer no código, é o processo mental de avaliação da estrutura (0:11:50 a 0:12:00).
- Quando há impacto, alguém tem de absorvê-lo; escolha onde (0:12:10 a 0:12:17).

Código (reconstrução a partir da fala, não publicada; nomes inferidos, legendas dizem Cola, Grow e o 7):

```python
def color_pixel(cmd, board):
    col, row, color = int(cmd[0]), int(cmd[1]), cmd[2]
    set_item(board, (col, row), color)

def set_item(board, coord, value):
    board[y(coord) - 1][x(coord) - 1] = value  # interface em 1, board em 0

def clear_array(board, value=BLANK):
    for row in range(1, height(board) + 1):
        for col in range(1, width(board) + 1):
            set_item(board, (col, row), value)
```

Antes da correção do range (0:10:53), o Clear ainda iterava a partir de zero e o menos um caía no último elemento da lista, por isso nada quebrou (0:10:28 a 0:10:44).

Citações (paráfrases de legenda, não verificadas):
- [0:04:04] a interface do programa considera índice começando em um e a implementação do board considera índice começando em zero Então isso é um problema para gente
- [0:10:34] o -1 tá pegando o último ele funciona por acaso porque a lista ela é circular [ele quer dizer: o índice negativo conta a partir do fim]
- [0:11:50] o foco não é só mexer no código foco é olhar esse entorno todo é olhar o processo mental
- [0:12:13] quando tem Impacto você tem que absorver esse Impacto você escolhe onde você quer saber o impacto [provável: absorver o impacto]

### Aula 10: Domine o Método da Refatoração Rápida #10: Uma Repetição Desperta a Atenção
Vídeo: https://www.youtube.com/watch?v=ClcO1OkcdJU · Duração: 6:24

Resumo: antes de seguir para o comando vertical, ele elimina uma repetição irritante nos testes: a criação do board vira uma fixture do pytest, injetada pelo nome do parâmetro (0:00:03 a 0:01:07). Escreve o teste do segmento vertical com a entrada 2 2 4 W e descobre que o fim é inclusivo, diferente da natureza do range do Python (0:01:09 a 0:02:31). A um aluno que nota que o teste agora depende da estrutura do código, responde que sempre haverá dependência, porque é preciso existir um board para operar; o que importa é quantas dependências há e se elas se acumulam (0:02:36 a 0:03:06). Reescreve o vertical no molde dos anteriores (desempacota os campos do comando, converte, usa a coordenada e a função que atribui) e ajusta o range para começar no início e terminar no fim mais um (0:03:14 a 0:06:08). Nota a primeira repetição, entre esse `for` e o de cima, e segue para o horizontal (0:06:12 a 0:06:22).

Linha do tempo:
- [0:00:03] repetição irritante: a criação do board em todo teste
- [0:00:09] usa pytest e cria uma fixture `board` (legenda: Death board bytest fixter)
- [0:00:34] basta pôr `board` como parâmetro que o pytest detecta e chama
- [0:01:09] teste do vertical com 2 2 4 W
- [0:02:15] o segmento vai até o índice 4, inclusive; diferente do range
- [0:02:36] pergunta de aluno: o teste agora depende da estrutura do código
- [0:02:49] sempre vai ter dependência; o problema é quantas e se se acumulam
- [0:03:44] desempacota cmd0 a cmd3 no topo da função
- [0:05:15] aqui não desconta menos um por causa do range: start até end mais um
- [0:06:12] primeira repetição: este `for` e o `for` de cima

Princípios:
- Repetição nos testes também se elimina; uma fixture tira a criação do board de cada teste (0:00:03 a 0:01:07).
- Depender não é o problema; o problema é quantas dependências e se elas se acumulam ao longo do tempo (0:02:49 a 0:03:06).
- Preparar o input no topo da função, deixando o algoritmo simples (0:03:44 a 0:05:46).
- Uma repetição chama a atenção, mas ainda não pede ação: ele nota e segue (0:06:12 a 0:06:20).

Código (reconstrução a partir da fala, não publicada; nome do comando incerto, legenda: ver Pixel):

```python
@pytest.fixture
def board():
    return create_array(...)  # argumentos não ditos

def vertical_pixel(cmd, board):
    col, start, end, color = int(cmd[0]), int(cmd[1]), int(cmd[2]), cmd[3]
    for row in range(start, end + 1):
        set_item(board, (col, row), color)

def test_vertical(board):
    vertical_pixel('2 2 4 W'.split(), board)
    ...  # o board esperado é escrito à mão; conteúdo não ditado
```

Citações (paráfrases de legenda, não verificadas):
- [0:00:03] antes disso tem uma repetição irritante acontecendo aqui
- [0:02:49] o problema depender sempre vai ter alguma dependência porque eu preciso do board existir
- [0:02:59] o problema é quantas dependências você tem e qual a relação entre ela se ela se acumula ao longo do tempo
- [0:06:12] Já começamos a ver uma repetição né esse fora [provável: for] aqui com aquele forte [provável: for] cima

### Aula 11: Domine o Método da Refatoração Rápida #11: Duas Repetições Apontam um Sintoma
Vídeo: https://www.youtube.com/watch?v=Yr4vZE-UzkI · Duração: 3:56

Resumo: teste do segmento horizontal com a entrada 2 3 3 W, e ele observa que a interface muda de um comando para o outro, a ordem dos campos não é a mesma do vertical (0:00:02 a 0:01:29). Reescreve o horizontal igual ao vertical, com o mesmo ajuste de range, e renomeia variáveis até as duas funções ficarem muito parecidas (0:01:33 a 0:03:03). A um aluno que insiste em tirar a repetição do desempacotamento, explica que neste andar da análise, o das funções e não o da interface do usuário que interpreta o comando, tirar aquilo quebra tudo; é preciso mudar todos para chegar a um padrão, e ao subir de volta a complexidade vai revelar algum padrão (0:03:06 a 0:03:54).

Linha do tempo:
- [0:00:02] teste do horizontal, muito parecido com o vertical
- [0:00:30] entrada 2 3 3 W
- [0:01:23] a interface muda de um comando para o outro
- [0:01:27] teste passa; pode mexer
- [0:01:54] desempacota cmd1, cmd2 e cmd3; limpa o índice
- [0:02:34] o mesmo problema do range: start até end mais um
- [0:02:48] renomeia para col; estão ficando muito parecidos
- [0:03:09] aluno insiste na repetição do desempacotamento
- [0:03:17] o andar da análise: deixou a interface do usuário para olhar as funções
- [0:03:43] trazer a complexidade para cima vai revelar um padrão

Princípios:
- Duas funções que ficam muito parecidas depois da limpeza são o sintoma; tornar a semelhança óbvia é parte do trabalho (0:02:45 a 0:03:03; 0:03:39 a 0:03:43).
- Trabalhar um andar de cada vez: no andar das funções não se mexe na interface do usuário, senão quebra tudo (0:03:14 a 0:03:39).
- Mudar todos para chegar a um padrão antes de mudar a interface de cima (0:03:33 a 0:03:39).
- O padrão aparece quando a complexidade é trazida para a vista (0:03:43 a 0:03:54).

Código (reconstrução a partir da fala, não publicada). A ordem dos campos segue o enunciado clássico (H X1 X2 Y C); a legenda em 0:01:10 é confusa sobre qual número é linha e qual é coluna:

```python
def horizontal_pixel(cmd, board):  # nome incerto
    start, end, row, color = int(cmd[0]), int(cmd[1]), int(cmd[2]), cmd[3]
    for col in range(start, end + 1):
        set_item(board, (col, row), color)
```

Citações (paráfrases de legenda, não verificadas):
- [0:01:23] é isso que ele tá fazendo a interface muda tá vendo de um para o outro
- [0:02:59] estão ficando muito parecidos Estamos quase lá
- [0:03:28] quando eu tiver nesse andar não adianta tentar tirar esse cara porque vai dar merda eu tenho que mudar todos para conseguir ter um padrão
- [0:03:49] vai aparecer algum padrão na nossa frente tem certeza absoluta disso

### Aula 12: Domine o Método da Refatoração Rápida #12: Três Repetições Permitem a Generalização
Vídeo: https://www.youtube.com/watch?v=p5pDefzS8E0 · Duração: 25:11

Resumo: teste do comando de bloco (retângulo) com 2 2 3 4 W, reescrito no mesmo molde; ao expandir o desempacotamento ele diz que expandir revela o padrão (0:00:00 a 0:02:23). Com os três comandos lado a lado, enxerga que linha vertical, linha horizontal e bloco são todos retângulos, achatados ou não, e que o `for` amarra as estruturas; extrai a navegação de um retângulo para um gerador `region` que produz coordenadas com yield, e o bloco, o vertical, o horizontal e o Clear passam a iterar coordenadas sem saber se é x ou y (0:03:28 a 0:10:10). Diz que o propósito do treinamento é transmitir o fluxo, e que basta começar com a função, esquecendo padrões (0:10:39 a 0:11:06). Vê então que todos fazem a mesma coisa, percorrer uma região e atribuir um valor, e cria uma função que atribui um valor a várias coordenadas; o código das funções some (0:11:13 a 0:12:45). A expressão do Clear fica difícil de ler, então cria `coords` do board, que faz yield from da região inteira, ligando gerador a gerador como um fluxo de transformação (0:12:53 a 0:14:33). Explica geradores no terminal (yield, next, StopIteration, for, yield from) e responde a perguntas sobre retornar o gerador ou fazer yield from, memória e asyncio (0:15:00 a 0:25:03).

Linha do tempo:
- [0:00:00] teste do bloco (Block pixel) com 2 2 3 4 W
- [0:02:08] expandir o desempacotamento revela o padrão
- [0:03:28] olha o range: paciência, cuidado e teste fazem o progresso ser exponencial
- [0:04:00] o block pixel resolve todas as anteriores: linha é retângulo achatado
- [0:04:58] o `for` é perigoso: embola as coisas, amarra as estruturas
- [0:05:43] extrai `region` (legenda: Death Regiane) como gerador de coordenadas com yield
- [0:07:40] o bloco itera coordenadas; não sabe mais se é x ou y
- [0:08:02] poderia receber duas coordenadas, mas espera para ver se é necessário
- [0:09:10] o código se revela: saindo da lógica e das etapas, esculpindo um fluxo único semântico
- [0:09:32] o Clear também passa a iterar a região do board inteiro
- [0:10:39] o propósito do treinamento é passar o fluxo; esqueça padrões, comece com a função
- [0:11:21] percorrer uma região e atribuir item: cria a função de várias coordenadas e um valor
- [0:13:02] ficou difícil de ler; cria `coords` do board com yield from
- [0:15:00] demonstra geradores no terminal: yield, next, StopIteration
- [0:19:38] pergunta: qual a diferença de retornar o gerador
- [0:24:22] vantagem: nada vai para a memória; asyncio é tudo gerador

Princípios:
- Três repetições permitem generalizar: com as três funções expandidas lado a lado, o padrão aparece e uma abstração resolve todas as anteriores (0:02:08 a 0:02:15; 0:04:00 a 0:04:06).
- Progresso exponencial vem de passos pacientes, com cuidado e com teste, porque cada passo cria novas abstrações e conceitos (0:03:42 a 0:04:00).
- O `for` usado indiscriminadamente embola as coisas e amarra as estruturas; extraia a navegação para algo de mais alto nível (0:04:58 a 0:05:18).
- Não antecipar a generalização: duas coordenadas como parâmetro poderiam ser úteis, mas só se forem necessárias (0:08:07 a 0:08:16).
- Sair da lógica e das etapas para chegar ao fluxo: um fluxo único semântico (0:09:10 a 0:09:23).
- Use o que você tem: função; esqueça padrões de projeto ao refatorar (0:10:58 a 0:11:06).
- Se a expressão ficou difícil de ler é porque tem detalhe de implementação demais; nomeie o que você quer (as coordenadas do board) (0:12:56 a 0:13:21).
- Geradores conectados formam um fluxo de transformação, sem ocupar memória (0:13:52 a 0:14:03; 0:19:21 a 0:19:28).
- Quem quer os valores faz yield from; quem quer o maquinário do gerador o retorna (0:20:50 a 0:20:59; 0:22:10 a 0:22:26).

Código (reconstrução a partir da fala, não publicada; a ordem dos parâmetros de `region` é a melhor leitura das legendas Colt, start, cover, roll and e searound, e não é certa):

```python
def region(col_start, col_end, row_start, row_end):
    for row in range(row_start, row_end + 1):
        for col in range(col_start, col_end + 1):
            yield col, row

def set_many(board, coords, value):  # legenda: set Man
    for c in coords:
        set_item(board, c, value)

def coords(board):  # legendas: Cordis, cortes
    yield from region(1, width(board), 1, height(board))

def clear_array(board, value=BLANK):
    set_many(board, coords(board), value)

def vertical_pixel(cmd, board):
    col, start, end, color = int(cmd[0]), int(cmd[1]), int(cmd[2]), cmd[3]
    set_many(board, region(col, col, start, end), color)

def horizontal_pixel(cmd, board):
    start, end, row, color = int(cmd[0]), int(cmd[1]), int(cmd[2]), cmd[3]
    set_many(board, region(start, end, row, row), color)

def block_pixel(cmd, board):
    c0, r0, c1, r1, color = int(cmd[0]), int(cmd[1]), int(cmd[2]), int(cmd[3]), cmd[4]
    set_many(board, region(c0, c1, r0, r1), color)
```

Demonstração no terminal (reconstrução, 0:15:17 a 0:18:05; o encerramento da função e o limite exato do range não são legíveis):

```python
def g():
    yield 1
    yield 2
    yield 3
    for n in range(1, 10, 2):
        yield n * n
    yield 'quase lá'

gen = g()
next(gen)  # 1, depois 2, 3, 1, 9, 25 ... e por fim StopIteration
for elemento in g():
    print(elemento)  # o for trata o StopIteration
```

Citações (paráfrases de legenda, não verificadas):
- [0:02:08] olha como é que isso revela o padrão né quando você expande o troço revela o padrão na tua cara
- [0:04:58] o for é uma coisa muito perigosa porque a gente está acostumada a usar o foco [provável: for] ou um comando indiscriminado e ele geralmente ele tenta ele embola as coisas Ele amarra as estruturas
- [0:10:58] esquece Pater [provável: patterns] esquece esquece essa merda esquece usa o que você tem cara todo mundo aprende função Então usa a função começa com a função
- [0:13:55] então um gerador conectado com gerador como um fluxo de transformação

### Aula 13: Domine o Método da Refatoração Rápida #13: Quando O Acoplamento É Inevitável: Mock
Vídeo: https://www.youtube.com/watch?v=CyQo3MsOVrE · Duração: 6:19

Resumo: ele pula o comando de preenchimento, que é grande, e vai ao Save (0:00:12 a 0:00:27). Como salvar mexe com arquivo, usa mock para o teste não ter efeito colateral: reduz o impacto do teste e cria isolamento metendo-se dentro do código, com `unittest.mock.patch` sobre o `open` embutido e um objeto especificado a partir de `io.IOBase` (0:00:45 a 0:01:46). Explica o MagicMock como um objeto plástico que finge ser o `open`, não faz nada e anota o que aconteceu; acessa o arquivo pelo valor de retorno e pelo `__enter__` do gerenciador de contexto, e afirma que `write` foi chamado uma vez com o board como string (0:02:07 a 0:03:55). O teste falha porque o código chamava `write` cinco vezes, uma por linha; ele corrige para um único `f.write` com a função que já representa o board como string, e renomeia o arquivo para `f` (0:04:24 a 0:05:19). Conclui que o `open` cria um acoplamento inevitável com o disco, e o mock, aproveitando que Python é dinâmico, sequestra esse ponto (0:05:25 a 0:06:05).

Linha do tempo:
- [0:00:12] pula o comando grande (preenchimento) e vai ao Save
- [0:00:47] salvar mexe com arquivo; usa mock para não ter efeito colateral
- [0:01:08] reduzir o impacto do teste e criar isolamento usando mock
- [0:01:25] patch do open embutido (legenda: Beauty open) com spec io.IOBase (legenda: ponto io base)
- [0:01:43] o patch vem do Python, unittest.mock (legenda: test.moc ponto Pet)
- [0:01:53] chama o save (legenda: Save A Ray) com um nome de arquivo (legenda: out dmp)
- [0:02:14] o mock é um objeto plástico que finge ser o open e anota as chamadas
- [0:02:40] o arquivo é o return value do mock (legenda: Victor Velho) via enter do contexto (legenda: Bandeirante)
- [0:03:38] afirma write chamado uma vez com o board como string
- [0:04:36] falha: write foi chamado cinco vezes; queria uma
- [0:05:09] um único f.write usando a função que já representa o board
- [0:05:25] o open cria acoplamento com o disco; o mock sequestra o processo

Princípios:
- Quando o acoplamento é inevitável (o `open` amarra o código ao disco), isole com mock para o teste não ter efeito colateral (0:00:56 a 0:01:16; 0:05:25 a 0:05:53).
- Teste que funciona independente: sem ficar lendo arquivo, que existe e depois não existe (0:05:36 a 0:05:43).
- Afirmar a interação que importa: a escrita aconteceu uma vez, com o conteúdo exato (0:03:34 a 0:03:55).
- Reaproveitar a função que já representa o board em vez de escrever linha a linha (0:05:09 a 0:05:17).
- Pequeno padrão pessoal: o arquivo aberto se chama `f` (0:05:00 a 0:05:06).

Código (reconstrução a partir da fala, não publicada; nomes `save_array`, `str_board` e o nome do arquivo inferidos das legendas, e o alvo exato do patch não é legível):

```python
import io
from unittest.mock import patch

@patch('builtins.open', spec=io.IOBase)
def test_save(mock_open, board):
    save_array(board, 'out.tmp')
    file = mock_open.return_value.__enter__.return_value
    file.write.assert_called_once_with(str_board(board))

def save_array(board, filename):
    with open(filename, 'w') as f:
        f.write(str_board(board))
```

Citações (paráfrases de legenda, não verificadas):
- [0:01:05] eu vou reduzir o impacto do meu teste e vou criar um isolamento no meu código de uma forma metendo dentro do código mesmo usando Moc [provável: mock]
- [0:02:14] esse Moque [provável: mock] vai ser um objeto que ele é plástico
- [0:05:25] aqui não teve jeito porque o open ele cria um acoplamento né Ele amarra o seu código com impacto no disco
- [0:05:47] aproveita que pai [provável: Python] tem uma linguagem dinâmica e se mete ali no meio para que ele não chegue no disco

### Aula 14: Domine o Método da Refatoração Rápida #14: O Poder de Abstração dos Algoritmos
Vídeo: https://www.youtube.com/watch?v=n2Itx0p1DaM · Duração: 48:35

Resumo: a aula é um recorte de uma sessão ao vivo contínua e começa no meio de uma frase, com o programa da matriz (o editor de pixels com comandos I, C, L, V, H, K, F, S, X que ele recebeu de um aluno, apresentado na aula 5) já parcialmente refatorado. Ele apaga o print do board que ficou desnecessário e ataca o algoritmo mais complexo, o preenchimento por região de cor (fill pixel [legenda: fio Pixel]), que é recursivo nos quatro vizinhos ortogonais (0:00:06 a 0:02:42). Escreve um teste com uma linha de corte de X no board para validar o algoritmo, leva a correção de índice (o board começa em 1) para dentro de funções de acesso get e set, renomeia cor para new color e old color, isola o que varia entre as quatro chamadas repetidas, renomeia outland (que na verdade testa se a coordenada está dentro) para contains, corrige a lógica com comparação encadeada e inverte o if para tirar a execução de dentro dele (0:02:50 a 0:20:56).

A segunda metade é a virada conceitual. Ele extrai os deslocamentos dos vizinhos para uma tabela e uma função offset, e nota que o algoritmo, que só navega coordenadas, depende explicitamente da estrutura do board: são duas responsabilidades (0:21:06 a 0:28:05). Quebra a função em duas, uma chamadora que conhece o board e um algoritmo genérico flood que recebe funções inside e match, por inversão de dependência, como o sort do Python recebe a chave (0:28:21 a 0:33:18; 0:31:56). Com a estrutura isolada do fluxo, troca a estratégia de vizinhança (ortogonal por diagonal) e depois troca a implementação recursiva por uma iterativa com conjunto de visitados e deque, sem mudar a assinatura, e os testes continuam passando (0:40:15 a 0:47:41).

Linha do tempo:
- [0:00:06] apaga o print do board [legenda: printboard], basta imprimir a string do board [legenda: bode]
- [0:00:41] volta ao algoritmo mais complexo; a função outland é usada em vários lugares
- [0:01:30] discrepância entre nome e comportamento: outland na verdade verifica se a coordenada está dentro do board
- [0:02:04] explica o algoritmo: pinta a coordenada e chama a si mesmo para os quatro vizinhos ortogonais da mesma cor
- [0:02:50] escreve o teste do fill [legenda: Death teste, teste fio] com um board de X em diagonal como linha de corte
- [0:05:56] leva a correção de índice para dentro; concentrar a bagunça; trabalhar no isolamento da zona
- [0:07:55] não quer depender de entender a indexação: quer o get item do board [legenda: get ithan]; cria get e set com menos um
- [0:10:06] extrai vizinho para isolar a única coisa que varia nas chamadas repetidas
- [0:14:09] no trecho de falas cruzadas com a turma (0:13:55 a 0:18:19), outland passa a se chamar contains; o trecho não é citado
- [0:18:21] acha o erro de lógica no contains (o índice, como um aluno tinha apontado) e usa comparação rica do Python
- [0:20:20] move contains para a API de manipulação do board e inverte o if
- [0:21:06] extrai a tabela de deslocamentos (os ossos secos) e a função offset, com generator expression
- [0:26:04] incômodo: um algoritmo de coordenadas depende da estrutura do board; duas responsabilidades
- [0:28:21] separa em função chamadora que conhece o board e algoritmo genérico flood, que recebe inside e match como o sort do Python
- [0:40:15] estratégia como parâmetro; troca ortogonal por diagonal e o preenchimento pula o muro
- [0:44:48] reescreve flood sem recursão (visitados num set, pendentes num deque), mesma assinatura; testes passam

Princípios:
- Nome que discorda do que a função faz é um problema a corrigir (0:01:30 a 0:01:52).
- Não dá para limpar tudo de uma vez; concentra-se a bagunça por tipo, isolando a zona (0:06:09 a 0:06:23).
- Acesso à estrutura por funções de acesso (get item, set item), para não depender de entender o detalhe de implementação, como o índice começando em 1 (0:07:55 a 0:09:14).
- Extrair a única coisa que varia para que o código repetido fique igual (0:11:33 a 0:12:18).
- Inverter o if quando toda a execução está dentro dele (0:20:35 a 0:20:56).
- Algoritmo que calcula coordenadas e depende da estrutura do board tem duas responsabilidades; separar a chamadora que conhece a estrutura do algoritmo genérico (0:27:50 a 0:28:29).
- Inversão de dependência: o algoritmo recebe a decisão como função, como o sort do Python (0:31:56 a 0:32:11; 0:39:05 a 0:39:22).
- Com a estrutura isolada do fluxo, troca-se algoritmo e estratégia sem quebrar nada (0:39:59 a 0:40:08; 0:47:34 a 0:47:41).
- A recursão em Python empilha chamadas e gasta mais memória; as duas versões estão corretas (0:47:48 a 0:48:09).

Código: reconstrução a partir da fala, não publicada. O código original é de um aluno e não é reproduzido; abaixo, só o ponto a que ele chega ao vivo. Nomes incertos estão anotados.

```python
# reconstrução a partir da fala, não publicada
from collections import deque

ORTHOGONAL = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 0:21:21; ordem incerta

def get_item(board, coord):        # 0:08:01 [legenda: get ithan, gerarite]
    x, y = coord
    return board[y - 1][x - 1]     # correção de índice, o board começa em 1 (0:09:01)

def contains(board, coord):        # antes outland (0:14:09); 0:19:12
    x, y = coord
    return 1 <= x <= width(board) and 1 <= y <= height(board)

def offset(coord, rel):            # 0:23:22 [legenda: off 77, A7, F7]
    return coord[0] + rel[0], coord[1] + rel[1]

def flood(coord, inside, match, strategy=ORTHOGONAL):   # versão iterativa, 0:44:48
    visited = set()
    pending = deque([coord])
    while pending:
        coord = pending.pop()
        visited.add(coord)
        yield coord
        neighbors = (offset(coord, rel) for rel in strategy)
        for n in neighbors:
            if n not in visited and inside(n) and match(n):
                pending.append(n)

def fill_pixel(board, coord, new_color):              # 0:33:36
    old_color = get_item(board, coord)
    def inside(c):                 # [legenda: Band, balde; provável: bound]
        return contains(board, c)
    def same_color(c):             # [legenda: semicolor]
        return get_item(board, c) == old_color
    set_many(board, flood(coord, inside, same_color), new_color)
```

A versão recursiva anterior (0:31:47 a 0:33:18) testa inside, faz yield da coordenada e chama flood para cada vizinho válido; ele a mantém comentada ao lado da iterativa (0:48:04). A estratégia diagonal (0:41:27) é narrada só em parte (menos um menos um, um, 1 menos 1), sem lista completa audível.

Citações (paráfrases de legenda, não verificadas):
- [0:06:13] tem duas bagunças dois quartos bagunçado eles não vão deixar de estar bagunçado só tem que concentrar a bagunça
- [0:11:33] eu isolei o que varia em todos os códigos
- [0:28:00] quando eu tenho isso É como se eu tivesse duas responsabilidades eu tenho duas coisas acontecendo
- [0:31:56] exatamente como sorte do pai tão funciona o sorte do Python delega ele recebe né Por inversão de dependência [provável: sort do Python]
- [0:47:34] trocamos o algoritmo trocamos a estratégia e por que a estrutura está isolada do fluxo tudo funcionou

### Aula 15: Domine o Método da Refatoração Rápida #15: Divida Responsabilidades para Conquistar Qualidade
Vídeo: https://www.youtube.com/watch?v=W4jFN2p8Gas · Duração: 41:29

Resumo: continuação direta da sessão. Ele observa que mexeu na estrutura toda sem tocar a parte de fora, porque refatorar exige escolher o que atacar, e que agora só get item e set item tocam de fato o board: o resto foca no fluxo e não na estrutura (0:00:01 a 0:01:13). Padroniza a API pondo o board como primeiro parâmetro de todas as operações e ajusta os testes; quando passar a coordenada como tupla quebra a chamada, dá um passo para trás (0:01:28 a 0:09:01). Vê o padrão de muitos inteiros e strings e decide tirar a validação da leitura de entrada, que fazia coisas demais e dependia do while e de continue (0:09:13 a 0:10:30). Traz uma biblioteca de prompt que ele mesmo escreveu, a inputao [legenda: imputão], repositório público dele `henriquebastos/inputao` (seção 12), copia o arquivo para o projeto como prompt e escreve primeiro o teste de um parse que tokeniza, valida o comando e converte dígitos em inteiros (0:10:30 a 0:17:10).

Com o parse, separa comando e argumentos, troca o acesso por índice por board e asterisco args com substituição por expressão regular no editor, e monta um dicionário de comandos; a um aluno que sugere Enum responde que acha o Enum do Python complicado e prefere uma classe simples (0:18:44 a 0:24:27). Uniformiza a API para que todas as funções recebam o board e o modifiquem, sem retornar board, e deleta o código que sobrou, técnica de deletar código (0:25:27 a 0:28:07). Despacha com f(board, *args), percebe que a interface do comando não conhece coordenada e desfaz essa mudança, extrai uma função invoke que conhece o board e passa os testes de unidade para ela, um teste de interface maior (0:28:38 a 0:37:21). Fecha com os três critérios que guiaram tudo, isolamento, interação e impacto, sem precisar de design nem de orientação a objeto, e trata TypeError como argumentos inválidos no loop (0:37:38 a 0:41:11).

Linha do tempo:
- [0:00:01] mexeu na estrutura sem se preocupar com a parte de fora; refatoração exige escolher o que atacar
- [0:00:52] só o get item e o set item [legenda: set trite] tocam o board; o resto foca no fluxo
- [0:01:28] traz as funções para o novo esquema: board primeiro (create, clean, color pixel, vertical, horizontal, block, fill)
- [0:05:04] os testes quebram; ajusta um a um, sem split e sem prints
- [0:07:39] passar a coordenada como argumento quebra a contagem; não faz sentido, dá um passo para trás e passa a tupla junta
- [0:09:45] a leitura de entrada faz coisas demais (pega, transforma, split, valida) e depende do while para validar
- [0:10:44] mostra a biblioteca que ele fez para pedir input em loop até converter, a inputao [legenda: imputão]; compatível com Python 2
- [0:13:06] teste primeiro do parse [legenda: parça, passe, paz]: X, I 4 5, F 3 2 +, K 2 2 3 4 W, S out.bmp em maiúsculas, e pytest.raises para comando inexistente [legenda: pai Teste Ponto raízes]
- [0:15:26] implementa o parse: tokeniza, levanta erro de comando inválido, converte tokens que são dígitos
- [0:18:44] separa Command e args; substitui por expressão regular no editor para board, *args
- [0:21:51] dicionário de comandos; pergunta sobre Enum e prefere classe simples
- [0:25:27] puxa o board para cima: todas as funções recebem o board; create modifica a lista por slice
- [0:30:09] L 2 2 W explode: a interface do comando não conhece coordenada; desfaz o uso de coordenada nos comandos
- [0:31:42] extrai invoke (o invocador) e passa os testes para ele; sai do teste unitário para um teste de interface maior
- [0:37:38] três critérios: isolamento, interação e impacto; não precisa saber design nem orientação a objeto
- [0:38:38] TypeError vira argumentos inválidos; limpa a tela com system clear; ctrl+c sai do loop

Princípios:
- Refatorar exige escolher o que atacar; o que está funcionando e atendendo pode ficar (0:00:14 a 0:00:25).
- Separar o fluxo de controle da interface do usuário do fluxo das APIs de processamento, isolando as dependências (0:00:25 a 0:00:34).
- Poucos pontos tocam a estrutura de fato; o resto foca no fluxo, e isso dá flexibilidade para coisas mais ousadas (0:00:47 a 0:01:31).
- Dar um passo para trás quando a mudança não faz sentido (0:07:45 a 0:07:48; 0:30:18 a 0:30:39).
- Uma função que pega o input, transforma, valida e depende do loop para comandar faz coisas demais; extrair a transformação específica (0:09:45 a 0:10:18).
- Teste primeiro para a peça nova (0:13:06 a 0:15:13).
- A interface externa manda: o comando não conhece coordenada, então a coordenada não aparece nessa fronteira (0:30:18 a 0:30:39).
- Uniformizar a API: todas as operações recebem o board e o transformam, sem retornar board (0:26:06 a 0:27:47).
- Apagar código é técnica (0:28:07).
- Preferir uma classe simples ao Enum do Python, que exige saber bem como funciona para não tropeçar (0:24:03 a 0:24:22).
- Os critérios de decisão são isolamento, interação e impacto de cada parte do código; não exige design nem OO, só funções (0:37:38 a 0:38:09).
- Andar de bicicleta: mudar daqui e dali, sempre buscando equilíbrio no design da API (0:36:48 a 0:37:01).

Código: reconstrução a partir da fala, não publicada. A biblioteca de prompt é a inputao, repositório público dele (`henriquebastos/inputao`, seção 12); ele a nomeia como imputão na legenda (0:10:44; 0:11:03), descreve o que faz (0:11:09 a 0:11:39) e não dita URL. Ele copia o arquivo para o projeto e o renomeia para prompt (0:12:05 a 0:12:17).

```python
# reconstrução a partir da fala, não publicada
import os
import sys

def parse(text, options=COMMANDS):            # 0:15:26
    tokens = text.upper().split()             # 0:16:01, leitura incerta
    if tokens[0] not in options:
        raise ValueError('Comando inválido')  # tipo da exceção não audível
    for i, token in enumerate(tokens):
        if token.isdigit():
            tokens[i] = int(token)
    return tokens

COMMANDS = {                                  # 0:21:51 a 0:23:23
    'X': sys.exit, 'I': create, 'C': clean, 'L': color_pixel,
    'V': vertical, 'H': horizontal, 'K': block, 'F': fill, 'S': save,
}

def invoke(board, tokens, commands=COMMANDS): # 0:31:58
    cmd, *args = tokens
    f = commands[cmd]
    f(board, *args)

def test_color_pixel():                       # 0:35:34
    board = []
    invoke(board, ['I', 4, 5])
    invoke(board, ['L', 2, 2, 'W'])
    ...

def main():
    board = []
    while True:
        cmd = prompt('...', parse)            # biblioteca de prompt dele; assinatura incerta
        try:
            invoke(board, cmd)
        except TypeError:
            print('Argumentos inválidos')     # 0:39:16
        os.system('clear')                    # 0:39:55
```

O create passa a substituir o conteúdo da lista recebida por slice em vez de retornar um board novo (0:26:40 a 0:27:11).

Citações (paráfrases de legenda, não verificadas):
- [0:00:16] fatoração é isso exige Você escolheu o que você vai atacar [provável: refatoração é isso, exige que você escolha]
- [0:01:06] todo o resto tudo que tá acontecendo tá focando no fluxo e não na estrutura
- [0:24:03] eu acho o enun do Python muito complicado eu prefiro criar um objeto normal uma classe simples [provável: Enum]
- [0:28:07] é técnica de deletar código
- [0:37:51] não tem que saber design não tem que saber orientação objeto ... o critério de entender o que pertence aqui o que tá mais próximo de que qual é a interação o impacto e o isolamento de cada parte do código entre si

### Aula 16: Domine o Método da Refatoração Rápida #16: A Mágica da API de Alto Nível
Vídeo: https://www.youtube.com/watch?v=3ymDmFjt9QY · Duração: 38:15

Resumo: aula de fechamento. Ele avisa que, se alguém achou que o treinamento era sobre recursos do Python, ele não cumpriu a tarefa: é sobre a sensibilidade de construir abstrações identificando isolamento, interação e impacto de cada parte do código nos quatro degraus da escadaria (código, lógica, procedimentos, fluxo), e tudo busca fluxo (0:00:33 a 0:01:38). Explica por que proibiu orientação a objeto no curso: sem ficar preso a estrutura de classe, ficaram os tijolinhos (x, y, offset, coords, items, contains, a string do board) que agora tornam fácil escrever classes Coordinate e Board com os métodos especiais do Python; o importante foi explicitar as fronteiras (0:01:51 a 0:04:16).

Para provar o ganho, escreve ao vivo um programa novo, game_of_life.py, reaproveitando a API da matriz: explica as regras, cria o board com caracteres Unicode para morto e vivo, posiciona um glider com set many, usa deepcopy para ter dois boards, calcula os oito vizinhos com a mesma lógica de offset, conta os vivos, aplica a regra e, ao estourar na borda, faz o board circular com módulo (0:04:52 a 0:24:52). Depois do funcionar, vem a elegância: extrai should die, a regra sem board, items do board, get many, count live, e separa coordenadas e status dos vizinhos em nomes distintos (0:24:57 a 0:33:53). Fecha dizendo que essa sensibilidade governa qualquer padrão, estratégia ou paradigma, que o código do aluno tinha a mesma essência mas uma forma que não deixava compor, e que o rápido da refatoração rápida é a capacidade de agir quando se enxerga o fluxo (0:34:48 a 0:38:10).

Linha do tempo:
- [0:01:04] é sobre sensibilidade na construção de abstrações: isolamento, interação e impacto nos quatro níveis da escadaria
- [0:01:51] exigiu não usar orientação a objeto; agora passar para OO fica muito mais fácil
- [0:02:43] classes Coordinate e Board ficam na mão: dunder getitem, iter, contains, str [legenda: dander]
- [0:03:40] explicitar as fronteiras é muito importante; sem mágica, isolando, encapsulando, eliminando repetição
- [0:04:52] vamos fazer um programa novo muito rápido: game_of_life.py; mostra o glider na internet
- [0:06:51] regras: vivo com menos de dois ou mais de três vizinhos morre; morto com exatamente três nasce
- [0:09:51] cria o board 50 por 25 e posiciona o glider com set many
- [0:11:03] new board com deepcopy, porque é lista de listas; explica a pergunta do Fabrício sobre deepcopy
- [0:13:20] oito vizinhos: tupla gerada com range(-1, 2) duas vezes, excluindo o (0, 0)
- [0:16:19] testa os vizinhos no console; pensa em fluxo, não numa estrutura que consulta o board
- [0:17:41] conta vizinhos vivos e aplica a regra no new board
- [0:21:43] estoura no canto: ou capa ou faz circular; wrap com módulo da largura e da altura
- [0:25:12] elegância: extrai should die, a regra (sem board, só coordenada), items, get many e count live
- [0:32:38] separa coordenadas dos vizinhos e status dos vizinhos em variáveis distintas
- [0:34:48] a sensibilidade de isolamento, interação e impacto governa qualquer padrão, estratégia ou paradigma
- [0:38:00] o rápido da refatoração rápida é a capacidade de agir quando se enxerga o fluxo

Princípios:
- O curso não é sobre Python; é sobre sensibilidade na construção de abstrações (0:00:45 a 0:01:11).
- Isolamento, interação e impacto de cada parte, nos quatro degraus da escadaria (0:01:11 a 0:01:31; 0:34:48 a 0:35:00).
- Abstrações e conceitos específicos antes da estrutura de classe; com os tijolinhos prontos, a classe é um detalhe, uma escolha posterior (0:02:08 a 0:02:55).
- Explicitar as fronteiras (0:03:40 a 0:03:48).
- Primeiro fazer funcionar, depois ir para a elegância extraindo (0:24:57 a 0:25:04).
- Pensar em fluxo: calcular coordenadas sem consultar a estrutura, e prender o board num ponto só do fluxo (0:16:23 a 0:16:33; 0:18:32 a 0:18:42; 0:26:57).
- Separar em nomes distintos coisas de natureza diferente que interoperam (0:32:38 a 0:33:44).
- O objetivo de qualquer organização é evitar o Frankenstein e gerar reaproveitamento (0:35:07 a 0:35:17).
- Eficiência de memória importa menos que manter a cápsula que viabiliza o fluxo (0:35:53 a 0:36:15).
- O rápido é agir a partir do momento em que se enxerga o fluxo (0:38:00 a 0:38:08).

Código: reconstrução a partir da fala, não publicada. Usa funções da API da matriz construída nas aulas anteriores (create, set many, get item, set item, offset, items, get many), importadas do módulo da matriz [legenda: Uma Triste; nome do módulo incerto] (0:15:50).

```python
# reconstrução a partir da fala, não publicada
import os
from copy import deepcopy
from time import sleep

DEAD, LIVE = chr(0x00B7), chr(0x2588)               # 0:08:37 a 0:09:13
SIZE = 50, 25                                        # 0:23:04
NEIGHBORS = tuple((a, b) for a in range(-1, 2)
                         for b in range(-1, 2) if not a == b == 0)   # 0:13:43

def neighbors(coord):                                # 0:14:53
    return (offset(coord, r) for r in NEIGHBORS)

def wrap(coords, w, h):                              # 0:22:12; detalhe do índice 1 não narrado
    return ((a % w, b % h) for a, b in coords)

def should_die(total):                               # 0:25:22 [legenda: Should I]
    return total < 2 or total > 3

def rule(coord, status, total):                      # 0:26:16
    s = status
    if status == LIVE:
        if should_die(total):
            s = DEAD
    elif total == 3:
        s = LIVE
    return s

def count_live(ns):                                  # 0:31:28
    return sum(1 for status in ns if status == LIVE)

def main():
    board = []
    create(board, *SIZE, DEAD)                       # 0:08:05
    set_many(board, GLIDER, LIVE)                    # 0:09:51
    while True:
        os.system('clear')
        print(board_to_str(board))
        new_board = deepcopy(board)                  # 0:11:03
        for coord, status in items(board):           # 0:27:40
            ncoords = wrap(neighbors(coord), *SIZE)  # 0:33:01
            nstatus = get_many(board, ncoords)
            set_item(new_board, coord, rule(coord, status, count_live(nstatus)))
        board = new_board
        sleep(0.05)                                  # 0:24:24
```

As coordenadas do glider ele já tinha calculadas e não as dita (0:09:27 a 0:09:42). Os nomes de create e da função de string são inferidos do contexto das aulas 14 e 15.

Citações (paráfrases de legenda, não verificadas):
- [0:01:04] isso é sobre a sensibilidade da construção de Abstrações quando você identifica o isolamento a interação e o impacto de cada parte do seu código nas quatro níveis da escadaria
- [0:02:13] a gente não ficou preso na estrutura da classe tentando encaixar os troços
- [0:03:42] explicitar as fronteiras e é explicitar as fronteiras que é muito muito importante
- [0:16:23] Então veja que eu tô pensando em fluxo eu não quero ter uma estrutura que consulta o board
- [0:38:03] o rápido do fatoração rápida o rápido é a tua capacidade de agir a partir do momento que você enxerga o fluxo [provável: refatoração rápida]

## 6. Princípios que atravessam toda a série

Quinze regras que ele formula na fala. Nenhuma é inferência deste documento, e nenhuma vem de trecho de participante.

#### 1. Entenda a estrutura, depois o fluxo, e mude a estrutura mantendo o fluxo

Primeiro entender que estrutura é aquela, a partir daí entender o fluxo, e então mudar a estrutura para manter o fluxo (aula 4, 0:03:33 a 0:03:41). Quem começa olha só a estrutura e não olha o fluxo (aula 3, 0:02:39 a 0:02:46). Na prática: hoje é dia de fluxo, não é dia de estrutura (aula 8, 0:08:07).

#### 2. Isolamento, interação e impacto são os critérios de cada decisão

Os três elementos que ele olha para alcançar o fluxo são impacto, interação e isolamento (aula 4, 0:08:11 a 0:08:24), analisados de forma fractal, parte por parte (aula 4, 0:10:23 a 0:10:36). São os três critérios para avaliar o que mexer e como desacoplar, sem precisar saber design nem orientação a objeto (aula 15, 0:37:38 a 0:38:09). O curso inteiro é sobre a sensibilidade de identificá-los em cada parte do código (aula 16, 0:01:04 a 0:01:23).

#### 3. Rode antes de ler, e leia pelo ponto de entrada simulando a execução

Tem que funcionar, tem que rodar o código (aula 3, 0:03:06). Ele roda o programa legado antes de abrir as funções (aula 5, 0:05:24 a 0:05:47). Para analisar o fluxo, vai aonde o programa começa e simula a execução, em vez de olhar banco, classes ou modelo (aula 6, 0:01:00 a 0:01:33).

#### 4. Antes de mudar, um teste que passa com o código como está

A pergunta antes de mexer é como mudar em segurança, e a resposta é teste (aula 6, 0:04:18 a 0:04:28). O teste de cada comando passa porque o código já funcionava, e só então ele mexe em segurança (aula 8, 0:01:31 a 0:01:35). Rodar na mão não é problema; o problema é depender de rodar na mão (aula 7, 0:08:04 a 0:08:08).

#### 5. Teste a interface por uma representação, nunca a estrutura interna

O teste que mede linhas e colunas depende de como a criação funciona por dentro e não está isolado (aula 7, 0:03:17 a 0:03:56). Ele aumenta a distância entre o teste e a implementação criando uma representação do board (aula 7, 0:03:56 a 0:04:13). O detalhe de implementação não pode afetar os testes (aula 7, 0:10:45 a 0:10:57), e o teste que amarra na implementação não respeita o fluxo, está preso à estrutura (aula 7, 0:13:30 a 0:13:37).

#### 6. Esconda o detalhe de implementação atrás de funções de propósito único

A ordem e a forma do board ficam escondidas atrás de uma função com o propósito específico de atualizar uma coordenada, e o código se lê como uma frase (aula 8, 0:04:48 a 0:05:15). Quem converte o índice da interface, que começa em um, para o do board, que começa em zero, é a função que guarda o detalhe de implementação (aula 9, 0:04:30 a 0:05:00). No fim, só get item e set item tocam o board de fato (aula 15, 0:00:52 a 0:01:10).

#### 7. Dependência sempre existe; o problema é quantas e se elas se acumulam

O problema não é ficar preso, você sempre vai estar preso a alguma coisa; o problema é quantas coisas te prendem (aula 8, 0:09:10 a 0:09:14). Com um ponto de contato só, a definição muda em um único lugar (aula 8, 0:09:17 a 0:09:28). Sempre vai haver dependência; importa quantas há e se elas se acumulam ao longo do tempo (aula 10, 0:02:49 a 0:03:06).

#### 8. Uma repetição chama a atenção, duas são sintoma, três permitem generalizar

Na primeira repetição ele nota e segue (aula 10, 0:06:12 a 0:06:20). Na segunda, as funções ficam muito parecidas (aula 11, 0:02:59), e tirar a repetição antes de mudar todas quebraria tudo (aula 11, 0:03:28 a 0:03:51). Na terceira, expandir revela o padrão e uma função resolve todas as anteriores (aula 12, 0:02:08 a 0:02:15; 0:04:00 a 0:04:06). Mesmo então, só generaliza o necessário: duas coordenadas como parâmetro, só se fizer sentido (aula 12, 0:08:04 a 0:08:16).

#### 9. Tire a navegação de dentro do `for` e transforme-a em gerador

O `for` usado indiscriminadamente embola as coisas e amarra as estruturas; a lógica de navegar num retângulo sai para algo de mais alto nível (aula 12, 0:04:58 a 0:05:18). O gerador `region` passa a produzir coordenadas, e gerador conectado com gerador forma um fluxo de transformação (aula 12, 0:05:43; 0:13:52 a 0:14:03).

#### 10. Teste que passa quando devia quebrar pede investigação

Ele roda os testes depois de mudar o índice, nada quebra, e pergunta por quê (aula 9, 0:06:47 a 0:07:10). O índice menos um pegava o último elemento da lista: funcionou por coincidência, e o teste ajudou a ver (aula 9, 0:10:28 a 0:10:46).

#### 11. Mock só quando o acoplamento é inevitável

Para salvar arquivo ele usa mock e assim reduz o impacto do teste e cria isolamento (aula 13, 0:01:03 a 0:01:16). Aqui não teve jeito, porque o `open` cria um acoplamento que amarra o código com impacto no disco; o mock se mete no meio para o teste não gravar nada (aula 13, 0:05:25 a 0:05:52).

#### 12. Separe o algoritmo da estrutura e passe a decisão como função

Um algoritmo que calcula coordenadas e depende da estrutura do board tem duas responsabilidades (aula 14, 0:27:50 a 0:28:05). O algoritmo genérico recebe as funções inside e match, exatamente como o sort do Python recebe a chave, por inversão de dependência (aula 14, 0:31:47 a 0:32:11). Quem chama configura o algoritmo (aula 14, 0:39:05 a 0:39:22), e por isso dá para trocar o algoritmo e a estratégia sem quebrar nada (aula 14, 0:39:59 a 0:40:08; 0:47:30 a 0:47:40).

#### 13. A interface externa manda

A interface do comando não conhece coordenada, então a coordenada sai dos comandos e volta para onde estava (aula 15, 0:30:18 a 0:30:39). É o mesmo cuidado da aula 9: a interface do programa conta a partir de um, a implementação a partir de zero, e essa diferença não pode vazar (aula 9, 0:04:04 a 0:04:11).

#### 14. Refatorar é escolher o que atacar

Refatoração exige escolher o que atacar: se a interface de fora está funcionando e atendendo, ela pode ficar (aula 15, 0:00:14 a 0:00:25). Na aula 7 ele deixa um TODO em vez de propagar a mudança pelas camadas de cima (aula 7, 0:19:18 a 0:20:29).

#### 15. Abstrações antes de classes; comece com a função

Esqueça padrões, use o que você tem, comece com a função (aula 12, 0:10:56 a 0:11:06). Sem ficar preso à estrutura de classe, ficaram abstrações e conceitos específicos, e a classe vira um detalhe, uma escolha posterior (aula 16, 0:02:08 a 0:02:55). O importante foi explicitar as fronteiras (aula 16, 0:03:40 a 0:03:48).

## 7. Citações-chave do curso

Paráfrases de legenda automática, sem aspas e não verificadas contra o vídeo. Nenhuma linha vem de trecho de participante.

| Aula | Timestamp | Paráfrase |
|---|---|---|
| #1 | 0:02:19 | quebra aquela visão antiga de programação como uma coisa genial você tem que ter tudo na cabeça |
| #2 | 0:00:47 | apesar do nome rápido ele não é rápido de fazer porque programar é lento mas é rápido de progredir |
| #2 | 0:09:40 | currículo de programador que lista a linguagem tem que ser rasgado |
| #3 | 0:00:29 | é o processo pelo qual você se acostuma a enxergar o que é de invisível no código |
| #3 | 0:03:06 | tem que funcionar tem que rodar o código |
| #4 | 0:01:16 | o código rodando é um filme o código no editor de texto é uma foto |
| #4 | 0:03:37 | para partir daí você entender o fluxo e aí você mudar a estrutura para manter o fluxo |
| #4 | 0:10:23 | o isolamento a interação e o impacto precisa ser analisado do código e é fractal |
| #4 | 0:15:16 | finja que você é um médico que não pode matar o paciente e trate o software como organismo vivo |
| #6 | 0:01:06 | quando eu vou analisar fluxo eu preciso simular como se eu tivesse executando o programa |
| #7 | 0:08:04 | rodar na mão não é um problema o problema é depender de rodar na mão |
| #7 | 0:10:54 | o detalhe de implementação não pode afetar os seus testes |
| #7 | 0:13:30 | o teste que amarra na implementação ele não respeita o fluxo ele tá preso a estrutura |
| #8 | 0:08:07 | hoje é dia de fluxo não é dia de estrutura |
| #8 | 0:09:10 | o problema não é ficar preso você sempre vai estar preso a alguma coisa o problema é quantas coisas te prendem |
| #9 | 0:12:13 | quando tem impacto você tem que absorver esse impacto você escolhe onde |
| #10 | 0:02:59 | o problema é quantas dependências você tem e qual a relação entre elas, se ela se acumula ao longo do tempo |
| #11 | 0:03:28 | quando eu tiver nesse andar não adianta tentar tirar esse cara eu tenho que mudar todos para conseguir ter um padrão |
| #12 | 0:02:08 | quando você expande o troço revela o padrão na tua cara |
| #12 | 0:04:58 | o for é uma coisa muito perigosa ele embola as coisas ele amarra as estruturas |
| #12 | 0:10:56 | esquece Pater [provável: patterns] usa o que você tem todo mundo aprende função então usa a função começa com a função |
| #13 | 0:05:25 | aqui não teve jeito porque o open ele cria um acoplamento ele amarra o seu código com impacto no disco |
| #14 | 0:28:00 | quando eu tenho isso é como se eu tivesse duas responsabilidades |
| #14 | 0:31:56 | exatamente como sorte do pai tão [provável: sort do Python] ele recebe por inversão de dependência |
| #14 | 0:47:30 | trocamos o algoritmo trocamos a estratégia e porque a estrutura está isolada do fluxo tudo funcionou |
| #15 | 0:00:16 | fatoração [provável: refatoração] é isso exige você escolher o que você vai atacar |
| #15 | 0:01:06 | todo o resto tudo que tá acontecendo tá focando no fluxo e não na estrutura |
| #15 | 0:37:51 | não tem que saber design não tem que saber orientação objeto |
| #16 | 0:01:04 | isso é sobre a sensibilidade da construção de abstrações quando você identifica o isolamento a interação e o impacto de cada parte do seu código |
| #16 | 0:02:13 | a gente não ficou preso na estrutura da classe tentando encaixar os troços |
| #16 | 0:03:42 | explicitar as fronteiras que é muito muito importante |
| #16 | 0:38:00 | o rápido do fatoração rápida [provável: refatoração rápida] é a tua capacidade de agir a partir do momento que você enxerga o fluxo |

## 8. A evolução técnica, aula a aula

O programa é o editor de matriz de pixels de um aluno, com comandos de uma letra para criar, limpar, pintar pixel, linha vertical, linha horizontal, bloco, preenchimento, salvar e sair (aula 5, 0:04:22 a 0:05:24). Em Refatoração na Prática ele analisou o mesmo programa sem mexer em nada e ditou TODOs (digest `kb/courses/refatoracao-na-pratica.md`, aulas #27 a #33). Aqui a refatoração é feita, e a tabela mostra a ordem.

| Etapa | O que é feito | Conceito ou ferramenta | O que isso destrava |
|---|---|---|---|
| **#1 a #4** | Contexto, refatoração, fluxo (aula 2, 0:00:47; aula 4, 0:03:33) | foto e filme, escada de quatro degraus, impacto, interação e isolamento | O critério que guia o resto (aula 4, 0:08:11) |
| **#5 e #6** | Roda o programa, lê pelo ponto de entrada, acha o acoplamento ao loop de interface (aula 5, 0:05:42; aula 6, 0:01:08; 0:05:02) | PyCharm, pytest com arquivo de testes vazio | Saber o que precisa de teste antes de mexer (aula 6, 0:04:18) |
| **#7** | Teste da criação por representação em string; criação reescrita com constante BLANK e compreensão de lista (0:04:06; 0:14:27 a 0:18:41) | textwrap.dedent, constante com valor padrão | Teste que sobrevive à mudança de estrutura (0:10:45) |
| **#8 e #9** | Clear testado; height, width, função que atribui uma coordenada, coordenada em dupla com x e y; conversão de índice para dentro dessa função (aula 8, 0:03:03 a 0:07:45; aula 9, 0:04:30 a 0:06:31) | encapsular a mudança de estado | Um único ponto conhece a forma do board (aula 8, 0:09:17 a 0:09:28) |
| **#10 a #12** | Fixture; vertical, horizontal e bloco no mesmo molde; tudo é retângulo; gerador `region`, função que atribui várias coordenadas, `coords` com yield from (aula 10, 0:00:09; aula 12, 0:04:00 a 0:14:12) | pytest.fixture, gerador, yield from | O corpo das funções de desenho some (aula 12, 0:11:21 a 0:12:45) |
| **#13** | Save testado com mock; cinco writes viram um, com a representação já existente (0:01:25 a 0:05:17) | unittest.mock.patch, MagicMock, io.IOBase | Teste de I/O sem efeito colateral (0:05:36) |
| **#14** | Fill: get e set item, contains, offset, tabela de vizinhos, flood genérico com inside e match, estratégia diagonal, versão iterativa (0:07:55 a 0:47:41) | inversão de dependência, generator expression, deque, set de visitados | Algoritmo trocável sem tocar a estrutura (0:47:30) |
| **#15** | Board como primeiro parâmetro de toda a API, parse com teste primeiro, dicionário de comandos, invoke, TypeError no loop (0:01:28 a 0:39:16) | inputao, pytest.raises, `cmd, *args` | Testes de interface maior via invoke (0:34:59 a 0:35:24) |
| **#16** | Game of Life novo sobre a mesma API; extração de should die, rule, items, get many, count live (0:04:52 a 0:33:53) | deepcopy, módulo para borda circular | A API vira biblioteca reaproveitável (0:35:15 a 0:35:34) |

O que vinha dos TODOs de Refatoração na Prática e o que ele faz aqui, citando os dois digests:

- Mapear comandos por dicionário em vez da cadeia de `if` (refatoracao-na-pratica, aula #28, 0:02:13) vira o dicionário de comandos e o invoke (aula 15, 0:21:51; 0:31:58).
- Encapsular a conversão entre índice base 1 dos comandos e base 0 do board (refatoracao-na-pratica, aula #28, 0:05:29 a 0:06:29) vira a conversão dentro da função que atribui e, depois, get e set item (aula 9, 0:04:30 a 0:05:00; aula 14, 0:07:55 a 0:09:14).
- Separar os dois papéis da leitura de entrada (refatoracao-na-pratica, aula #29, 0:04:24) vira o parse extraído com teste primeiro (aula 15, 0:09:45 a 0:10:18; 0:13:06).
- Fazer o board se representar como string (refatoracao-na-pratica, aula #28, 0:09:49) vira a representação usada no teste da aula 7 (0:04:06) e no Save (aula 13, 0:05:09 a 0:05:17).
- Um método que atribui valor a múltiplas coordenadas e as linhas como regiões de um retângulo (refatoracao-na-pratica, aula #30, 0:09:05 a 0:13:24; 0:15:39 a 0:17:58) viram a função de várias coordenadas e o gerador `region` (aula 12, 0:05:43; 0:11:21 a 0:12:45).
- O pertencimento com comparação rica e a lógica invertida em relação ao nome (refatoracao-na-pratica, aula #31, 0:00:17 a 0:03:34) viram contains (aula 14, 0:01:30 a 0:01:52; 0:18:21 a 0:19:34).
- O fill genérico, ortogonal ou diagonal, que não conhece o board (refatoracao-na-pratica, aula #31, 0:04:31 a 0:12:17) vira o flood com inside, match e estratégia (aula 14, 0:28:21 a 0:33:18; 0:40:15).
- A diferença está nos objetos: lá ele sugeria um objeto Coordenada e uma classe Board (refatoracao-na-pratica, aula #30, 0:05:37 a 0:07:55; aula #28, 0:04:35); aqui ele recusa o tipo Coordenada porque é dia de fluxo (aula 8, 0:07:56 a 0:08:09) e deixa as classes como passo opcional depois das abstrações (aula 16, 0:02:43 a 0:02:55).

## 9. Arsenal técnico demonstrado no curso

| Técnica ou recurso | Para que ele usa | Aula e timestamp |
|---|---|---|
| Rodar o programa pelos comandos do README | Ver o comportamento antes de ler o fonte | #5, 0:05:24 a 0:06:58 |
| Leitura pelo ponto de entrada | Simular a execução para achar o fluxo | #6, 0:01:00 a 0:01:33 |
| Representação em string do board | Testar a interface sem depender da estrutura | #7, 0:04:06 a 0:10:31 |
| textwrap.dedent [legenda: dente] | Escrever a string esperada no teste | #7, 0:08:54 |
| Conversão da entrada antes do algoritmo | Errar antes, sem efeito colateral | #7, 0:15:17 a 0:15:40 |
| Constante BLANK como parâmetro com valor padrão | Tirar o número mágico | #7, 0:15:58 a 0:16:46 |
| Compreensão de lista no lugar de for com append | Criar o board | #7, 0:17:04 |
| TODO no lugar da mudança em cascata | Manter contratos explícitos, passo a passo | #7, 0:19:18 a 0:20:29 |
| Função que atribui uma coordenada; height e width | Encapsular a mudança de estado | #8, 0:03:03 a 0:05:15 |
| Coordenada em dupla com funções x e y | Amarrar a definição em um lugar | #8, 0:05:51 a 0:07:45 |
| Fixture do pytest | Tirar a criação do board de cada teste | #10, 0:00:09 a 0:00:42 |
| Range inclusivo (start até end mais um) | Casar a semântica dos comandos com o range | #9, 0:10:53; #10, 0:05:15; #11, 0:02:34 |
| Gerador `region` e `coords` com yield from | Navegar regiões sem `for` aninhado nos comandos | #12, 0:05:43 a 0:14:12 |
| Geradores no terminal (yield, next, StopIteration) | Explicar o mecanismo à turma | #12, 0:15:00 a 0:19:28 |
| unittest.mock.patch sobre o `open`, spec io.IOBase | Testar o Save sem tocar o disco | #13, 0:01:25 a 0:03:55 |
| Inverter o if | Tirar a execução de dentro do if | #14, 0:20:35 a 0:20:56 |
| Comparação encadeada do Python | Escrever contains como uma expressão | #14, 0:19:12 a 0:19:34 |
| Tabela de deslocamentos e generator expression | Substituir quatro chamadas repetidas | #14, 0:21:06 a 0:24:31 |
| Funções como parâmetro (inside, match) | Inversão de dependência no flood | #14, 0:31:47 a 0:32:11 |
| deque e set de visitados | Trocar recursão por iteração com a mesma assinatura | #14, 0:44:48 a 0:47:41 |
| Busca e substituição com expressão regular no editor | Trocar acesso por índice por `board, *args` | #15, 0:19:23; 0:20:47 |
| inputao [legenda: imputão] | Pedir input em loop até converter | #15, 0:10:44 a 0:12:17 |
| pytest.raises | Testar comando inválido no parse | #15, 0:14:52 |
| Dicionário de comandos e invoke | Despachar sem cadeia de if | #15, 0:21:51; 0:31:58 |
| Deletar código | Técnica, quando a API fica uniforme | #15, 0:28:07 |
| copy.deepcopy | Ter dois boards no Game of Life | #16, 0:11:03 a 0:12:23 |
| Módulo da largura e da altura | Fazer o board circular nas bordas | #16, 0:21:43 a 0:22:12 |

## 10. Glossário do curso

| Termo | Significado no contexto da série | Onde |
|---|---|---|
| **Refatoração rápida** | Rápida de progredir, não de fazer; a refatoração em que não se trava | #2, 0:00:44 a 0:00:58; #16, 0:38:00 |
| **Vale das sombras** | O lugar do mercado onde o trabalho não progride | #2, 0:04:03 a 0:04:21 |
| **Validador** | O filtro do mercado que pergunta o que você prova que entrega | #2, 0:08:56 a 0:09:35 |
| **Carreira antifrágil** | Não desmorona se mudar a tecnologia ou o projeto; sabe como vai aprender | #2, 0:16:01 a 0:18:36 |
| **Fluxo** | O processo de transformação dos dados, o código em movimento | #4, 0:00:46 |
| **Foto e filme** | O código no editor versus o código rodando | #4, 0:01:13 a 0:01:22 |
| **Código pinball** | Código com efeitos colaterais em tantos lugares que não cabe na cabeça | #4, 0:02:06 a 0:02:47 |
| **Escada de quatro degraus** | Código, lógica, etapas ou procedimentos, fluxo | #4, 0:03:47; #16, 0:01:15 a 0:01:23 |
| **Impacto, interação, isolamento** | As três relações que ele analisa em cada parte do código | #4, 0:08:11 a 0:08:24; #15, 0:37:38 |
| **Complexidade ciclomática ampliada** | O grafo de chamadas mais quem muta cada objeto em memória | #4, 0:11:02 a 0:13:21 |
| **Arquiteto astronauta** | A síndrome dos diagramas antes do código rodando | #3, 0:03:24 |
| **Andar da análise** | O nível em que se trabalha, interface do usuário ou funções | #11, 0:03:14 a 0:03:28 |
| **Coincidência** | Código que funciona por acaso, como o índice negativo que pega o último elemento | #9, 0:10:28 a 0:10:46 |
| **Fluxo de transformação** | Gerador conectado a gerador | #12, 0:13:52 a 0:14:03 |
| **Mock** | Objeto plástico que finge ser o `open`, não faz nada e anota o que aconteceu | #13, 0:02:14 a 0:02:35 |
| **Inversão de dependência** | O algoritmo recebe a decisão como função | #14, 0:31:56 a 0:32:11 |
| **Estratégia** | A tabela de vizinhança, ortogonal ou diagonal, passada ao flood | #14, 0:40:15 a 0:41:29 |
| **Invocador** | A função invoke, que conhece o board e ativa os comandos | #15, 0:31:52 a 0:32:01 |
| **Tijolinhos** | As abstrações pequenas (x, y, offset, contains) que tornam a classe um detalhe | #16, 0:02:21 a 0:02:32 |

## 11. Perguntas e respostas que o curso responde

#### O que é rápido na refatoração rápida?

O progresso, não a execução: programar é lento, mas não se trava (aula 2, 0:00:47 a 0:00:58); o rápido é agir quando se enxerga o fluxo (aula 16, 0:38:00 a 0:38:08).

#### Por onde começar num código legado?

Rodando o programa (aula 5, 0:05:24 a 0:05:47) e lendo pelo ponto de entrada, simulando a execução (aula 6, 0:01:00 a 0:01:33).

#### Como mudar em segurança um código acoplado ao loop de interface?

Testando abaixo do loop, função por função, ou rompendo o loop para testar emulando o usuário (aula 6, 0:04:49 a 0:05:43). Ele vai pelas funções, começando pela criação (aula 7, 0:00:00 a 0:00:22).

#### O que torna um teste bom?

Testar a interface por uma representação, de modo que o detalhe de implementação não o afete (aula 7, 0:04:06; 0:10:45 a 0:10:57).

#### Pôr lógica no teste não é arriscado?

O risco existe, mas o sistema legado já funciona e ele o está desconstruindo em baby steps (aula 7, 0:06:03 a 0:06:54).

#### Depender da estrutura do board no teste não é problema?

Sempre haverá dependência; o problema é quantas e se se acumulam (aula 10, 0:02:49 a 0:03:06).

#### Quando eliminar uma repetição?

Na terceira: a primeira chama a atenção, a segunda é sintoma, a terceira revela o padrão (aula 10, 0:06:12; aula 11, 0:03:28; aula 12, 0:02:08 a 0:04:06).

#### Por que não criar um tipo Coordenada?

Porque hoje é dia de fluxo, não de estrutura (aula 8, 0:07:56 a 0:08:09); as classes ficam para depois das abstrações (aula 16, 0:02:43 a 0:02:55).

#### O que fazer com um teste que passa quando devia quebrar?

Investigar: no caso, o índice menos um pegava o último elemento e funcionava por coincidência (aula 9, 0:06:47 a 0:07:10; 0:10:28 a 0:10:46).

#### Quando usar mock?

Quando o acoplamento é inevitável, como o `open` com o disco (aula 13, 0:05:25 a 0:05:52).

#### Como separar um algoritmo da estrutura de dados?

Uma chamadora que conhece a estrutura e um algoritmo que recebe as decisões como funções, como o sort do Python (aula 14, 0:27:50 a 0:28:05; 0:31:47 a 0:32:11).

#### Recursão ou iteração no flood?

As duas estão corretas; a iterativa é mais eficiente em Python porque a recursão empilha chamadas (aula 14, 0:47:44 a 0:48:09).

#### Enum para o dicionário de comandos?

Ele acha o Enum do Python complicado e prefere uma classe simples (aula 15, 0:24:03 a 0:24:22).

#### Por que o curso proibiu orientação a objeto?

Para não ficar preso à estrutura de classe; com as abstrações prontas, a classe vira detalhe (aula 16, 0:01:51 a 0:02:55).

#### Preciso saber design para refatorar assim?

Não: os critérios são isolamento, interação e impacto, com funções (aula 15, 0:37:38 a 0:38:09).

## 12. Repositórios e recursos

| Recurso | Onde encontrar | Observação |
|---|---|---|
| Playlist completa (fonte desta documentação) | [Domine o Método da Refatoração Rápida](https://www.youtube.com/playlist?list=PLeKXYyZCJHxfHUETjNouzr1hyaiuljrUY) | 16 vídeos. Os ids estão em `playlist.json` e nos links da seção 5. |
| Canal | [HB Network](https://www.youtube.com/@hbnetworkoficial) | |
| inputao [legenda: imputão] | [henriquebastos/inputao](https://github.com/henriquebastos/inputao) | Aula 15, 0:10:44 a 0:12:17: biblioteca dele que pede input em loop até a função de conversão aceitar (0:11:09 a 0:11:39); ele copia o arquivo para o projeto como prompt. README: Um input melhor para ajudar os iniciantes em Python. Último commit `ff10484c37e3fbf8f60e70dbb0816dce6a62f1d2`, de 2020-05-15. |
| Refatoração na Prática | `kb/courses/refatoracao-na-pratica.md` | Curso anterior dele. As aulas #27 a #33 analisam o mesmo programa sem mexer; o código foi compartilhado durante esse curso (aula 2, 0:00:18; aula 5, 0:03:28). |
| Antifrágil, de Nassim Taleb | citado, sem URL | Aula 2, 0:14:34 a 0:15:15. Ele recomenda como leitura; a legenda deforma o nome do autor. |
| Primeiro treinamento, de 2010 [legenda: concedidiano] | citado, sem URL | Aula 1, 0:02:04. Provável Welcome to the Django, leitura incerta. |
| Conferência da OTAN sobre a crise do software | citada, sem URL | Aula 3, 0:01:02 a 0:01:12. |
| Filmes Apollo 13 e First Man | citados, sem URL | Aula 4, 0:17:41 a 0:19:08, como exemplo de restrição que cria criatividade. |

Repositórios do curso: **nenhum**. O programa refatorado é de um aluno e não tem URL nas transcrições; o código que ele escreve ao vivo não é publicado com caminho nem commit. A inputao é o único repositório dele que o curso usa.

## 13. Análise linha a linha do código real

O curso não publica código com caminho, commit ou URL, portanto não há análise de código real. O programa refatorado é de um aluno e não é reproduzido aqui, nem na forma original nem em trechos. O que a seção 5 traz são reconstruções a partir da fala do código que ele escreve ao vivo, marcadas como não publicadas. Limites que ficam registrados:

- Quase todo identificador vem deformado na legenda; os nomes usados nas reconstruções (create_array, set_item, region, set_many, coords, flood, invoke) são leituras prováveis, anotadas em cada aula.
- A ordem dos parâmetros de `region` não é legível (aula 12, 0:05:51 a 0:06:30), e a ordem dos campos do comando horizontal se contradiz na fala (aula 11, 0:01:10).
- O alvo exato do patch e o nome do arquivo de saída na aula 13 não são legíveis (0:01:25; 0:01:53).
- A estratégia diagonal da aula 14 é narrada só em parte (0:41:27), e as coordenadas do glider da aula 16 não são ditadas (0:09:27 a 0:09:42).
- O trecho de falas cruzadas da aula 14 (0:13:55 a 0:18:19) não é usado para reconstrução.
- A inputao é repositório público dele, mas esta documentação não a analisa linha a linha; a fala só descreve o que ela faz (aula 15, 0:11:09 a 0:11:39).

## 14. Execução real dos testes

O curso não publicou código nem suíte. Não há o que rodar. As reconstruções da seção 5 dependem de funções que a fala não dita por inteiro e não foram executadas nesta documentação.

---

Documentação elaborada a partir das transcrições das 16 aulas da playlist Domine o Método da Refatoração Rápida, de Henrique Bastos (HB Network), playlist `PLeKXYyZCJHxfHUETjNouzr1hyaiuljrUY`, legendas automáticas em português (pt-orig) capturadas em 2026-10-12. As citações são paráfrases das transcrições, não verificadas contra o vídeo (`verified: false`), renderizadas sem aspas e com os erros de reconhecimento anotados entre colchetes quando precisam aparecer. Falas de participantes identificadas (aula 4, 0:16:05 a 0:16:44; aula 14, 0:13:55 a 0:18:19; aula 16, a partir de 0:36:57) não são atribuídas a ele. O curso não publica o código refatorado: o programa é de um aluno, não é reproduzido e o aluno não é nomeado; o código que ele escreve ao vivo não tem repositório, caminho nem commit. O único repositório dele citado é `henriquebastos/inputao`. Datas de publicação e visualizações não foram coletadas. Conteúdo de caráter educativo.
