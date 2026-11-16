<!-- written by the henrique-ingest distiller on 2026-11-15 from sources/transcripts/desafios-pythonicos/; see kb/courses/README.md for provenance and license -->

HB Network · Documentação de curso

# Pacote de Desafios Pythônicos

As 15 aulas da playlist, lidas aula a aula a partir das legendas automáticas. É um curso curto e gravado, não ao vivo: uma aula de boas-vindas e uma aula por exercício, cada uma com a mesma estrutura, que ele anuncia na aula de abertura (aula 0, 0:04:30 a 0:05:03): lê o enunciado, roda os testes do arquivo, pede uma pausa para o aluno tentar e volta com dicas e provocações. Ele não escreve a solução de nenhum exercício. Os exercícios vêm de um repositório dele no GitHub, `pacote-desafios-pythonicos`, já descrito em `kb/repos/pacote-desafios-pythonicos.md`. Os primeiros sete trabalham strings (aulas 1 a 7), os cinco seguintes trabalham listas, ordenação e complexidade (aulas 8 a 12), e os dois últimos são programas de linha de comando sobre arquivos de texto, com esqueleto pronto (aulas 13 e 14). O fio que atravessa as dicas é a forma do código: nomes do domínio do problema, menos repetição, código linear, e a advertência de que o mais sofisticado nem sempre é o melhor.

Instrutor: **Henrique Bastos** · Canal [HB Network](https://www.youtube.com/@hbnetworkoficial) · Playlist: [Pacote de Desafios Pythônicos](https://www.youtube.com/playlist?list=PLeKXYyZCJHxetT2NwFzKcslYfiE3yPUWL) · Repositório: `henriquebastos/pacote-desafios-pythonicos`, commit `ae90952cdaa7690a31e62f4715f0bd60600213b3`

Documento elaborado a partir das transcrições das 15 aulas (legenda automática em português, pt-orig, capturada em 2026-11-15). A legenda não marca quem fala, mas só ele fala: não há turma, chat nem convidado. Nenhum aluno é citado; a única referência a terceiros é genérica (sempre que ele passa o desafio para alguém, aula 14, 0:03:48 a 0:03:55). Numeração: este documento numera as aulas pelo título do vídeo, de #00 a #14, então "aula 5" é o vídeo #05. A posição na playlist e o prefixo do arquivo de transcrição são uma unidade maior (a aula 5 é `06-6pWg3dljBOo.md`).

## 1. Visão geral do curso

Pacote de Desafios Pythônicos é uma série de **15 vídeos** que somam **3.125 segundos, 52 minutos e 5 segundos**. Ele abre dizendo que programar exige prática e que, para dominar os recursos das ferramentas, é importante explorar exercícios e desafios (aula 0, 0:00:05 a 0:00:18), e fecha a abertura dizendo que os desafios existem para tirar o aluno da zona de conforto, levando-o ao limite do que sabe e do que não sabe, e que foi para isso que bolou o pacote (aula 0, 0:05:17 a 0:05:31).

| Dimensão | Valor | Observação |
|---|---|---|
| Aulas | 15 | Playlist completa, numerada de #00 a #14 no título. |
| Duração total | 3.125 s (52min 5s) | Soma das durações em `playlist.json`. O `playlist.json` arredonda o total para 0,9 hora. |
| Aula mais curta / mais longa | 83 s (#02) / 457 s (#13) | A #13, wordcount, tem 7:37; a #02, both_ends, tem 1:23. |
| Datas de publicação | não coletadas | O `playlist.json` desta coleta traz id, título e duração. Os commits do repositório são de 2020-03-21 e 2020-04-01. |
| Visualizações | não coletadas | Idem. |
| Transcrições | 15 de 15 disponíveis | Todas em legenda automática (pt-orig). |
| Formato | aula gravada, tela do editor | Ele abre o arquivo no PyCharm, roda e comenta; nas aulas 13 e 14 roda no terminal. Cada aula tem uma marcação de pausa antes das dicas (aula 0, 0:04:56 a 0:05:03). |
| Legenda ruidosa | nomes de funções e módulos | Pythônicos sai Pai tônicos (aula 0, 0:00:00), PyCharm sai phy charme e pai charme (aula 0, 0:02:00 a 0:02:04), join sai John e joia (aula 4, 0:01:41; aula 7, 0:03:13), list comprehension sai Lis compro rations e lixo compro ranchos (aula 8, 0:02:04; aula 9, 0:02:32), heapq.merge sai rip e nerd (aula 12, 0:03:24 a 0:03:28), defaultdict sai the foldick (aula 14, 0:04:19). Lista no glossário e na seção 13. |
| Código do curso | o kit publicado; nenhuma solução | Ele mostra os arquivos do repositório e roda os testes deles; não escreve solução. A seção 5 traz três ilustrações deste documento, marcadas como tal. |

Nota de método: cada afirmação traz aula e timestamp. As citações são paráfrases de legenda, sem aspas, não verificadas contra o vídeo. Mis-hearings ficam entre colchetes. Caminhos do repositório citam o commit `ae90952`; o repositório não tem licença, então os trechos são curtos.

## 2. Filosofia e método de ensino

### 2.1 Prática, não leitura

O curso inteiro parte de uma frase: programar exige prática (aula 0, 0:00:05 a 0:00:18). Ele gosta desses exercícios porque são simples e diretos e, ainda assim, têm muitas formas de resolver (aula 0, 0:00:18 a 0:00:37), e o intuito é pôr a cabeça para pensar e o repertório em prática, para validar o que se aprendeu e continuar esticando as possibilidades (aula 0, 0:00:52 a 0:01:05).

### 2.2 Resolver de novo, de outro jeito

A pergunta que ele quer deixar com o aluno é como é que eu poderia fazer diferente (aula 0, 0:00:43 a 0:00:52). Ela volta em quase toda aula: fazer o máximo de versões possíveis (aula 6, 0:01:41 a 0:01:43), refazer o exercício várias vezes e guardar todas as versões, sem apagar, para comparar (aula 7, 0:03:13 a 0:03:33), implementar de diversas maneiras por se tratar de um desafio (aula 8, 0:03:00 a 0:03:05), e publicar o link da solução nos comentários, de preferência de todas as versões (aula 10, 0:02:48 a 0:02:53). Comparar estratégias é parte do método: é sempre interessante ver como cada um pensa (aula 0, 0:00:35 a 0:00:41; aula 4, 0:03:00 a 0:03:07).

### 2.3 Se ficou fácil, sofistique

Ele pede que a ordem dos arquivos seja respeitada, porque aumenta a complexidade aos poucos (aula 0, 0:02:24 a 0:02:33), e que um exercício fácil não seja pulado, mas resolvido de forma mais sofisticada (aula 0, 0:02:33 a 0:02:46). Nas aulas isso vira provocação concreta: contar com `while` sem as facilidades do Python (aula 2, 0:01:05 a 0:01:20), escrever o próprio algoritmo em vez do `replace` (aula 3, 0:01:39 a 0:01:49), escrever o próprio algoritmo de ordenação (aula 10, 0:01:32 a 0:01:47), acrescentar um caso de teste que rompe a premissa do enunciado (aula 4, 0:02:10 a 0:02:55) ou um requisito novo no meio do projeto (aula 6, 0:01:43 a 0:02:07).

### 2.4 O teste como corretor

Os exercícios trazem uma rotina de teste que mostra o que corrigir, então são autocorrigíveis: não importa a estratégia, se o resultado estiver correto, está tudo certo (aula 0, 0:03:13 a 0:03:30). A cada exercício ele roda os testes antes de dar a dica e lê os casos como limites do problema (aula 1, 0:00:51 a 0:01:06; aula 5, 0:00:34 a 0:00:39; aula 10, 0:00:41 a 0:00:51).

### 2.5 Relação com os outros cursos

Comparação deste documento, não fala dele: os exercícios donuts (aula 1) e wordcount (aula 13) desta série são os dois que ele refatora em Refatoração na Prática (`kb/courses/refatoracao-na-pratica.md`, aulas 6 a 16 e 18 a 25 daquele curso), e a regra de deixar o código o mais linear possível (aula 1, 0:01:53 a 0:02:02) é a de `kb/principles/codigo-linear.md`. A sugestão de passar uma função para mudar a lógica da ordenação (aula 9, 0:02:34 a 0:02:52; aula 10, 0:01:57 a 0:02:04) é o movimento que `kb/principles/separe-a-navegacao-da-decisao.md` descreve em Refatoração Rápida.

## 3. Pilares conceituais

### 3.1 Nomes que vêm do problema

A dica que mais se repete é sobre nomes. Prestar atenção nos nomes das variáveis (aula 1, 0:01:40 a 0:01:45); variáveis auxiliares com nomes significativos que, ao mesmo tempo, não ocupam muito espaço (aula 3, 0:02:09 a 0:02:22); evitar variáveis como `s`, texto ou mensagem, que não se relacionam com o domínio, e buscar a inspiração no problema, que é manipulação de verbos (aula 5, 0:01:32 a 0:01:50); ao dividir o problema, manter a semântica dele e nomear a lista das palavras que começam com x e a das que não começam, em vez de um atalho que complica a leitura de outra pessoa (aula 9, 0:01:36 a 0:02:14); e evitar nomes fora do domínio de contagem de palavras (aula 13, 0:06:47 a 0:07:00).

### 3.2 O óbvio costuma ser melhor que o sofisticado

Ele oferece a versão em uma linha como exercício em seis aulas (aula 2, 0:00:58; aula 3, 0:01:49; aula 4, 0:02:06; aula 5, 0:01:50; aula 11, 0:02:30; aula 12, 0:03:32), mas desconfia dela: será que fica bom assim (aula 2, 0:01:00 a 0:01:02), não acho que fica tão elegante (aula 5, 0:01:52 a 0:01:56), acho que fica bem esquisito (aula 11, 0:02:32 a 0:02:36). A aula 8 diz a regra: nem sempre o código mais sofisticado é o melhor, e a solução mais óbvia e mais simples costuma ser a mais eficiente em memória, legibilidade e manutenibilidade (aula 8, 0:02:37 a 0:02:53).

### 3.3 Menos repetição, código linear

Depois de implementar, observe se dá para reduzir as repetições, simplificando o código e tornando-o o mais linear possível (aula 1, 0:01:53 a 0:02:02). No verbing, isolar o processamento da tomada de decisão dá um código quase linear, com uma simples bifurcação no meio (aula 5, 0:01:56 a 0:02:11). No front_back, o cálculo do índice repetido para as duas strings pede algo que as duas usem (aula 7, 0:02:22 a 0:02:36).

### 3.4 Conhecer o custo do que se usa

Três aulas falam do custo das operações, não da lógica. A concatenação cria uma string nova a cada operação e o `join` faz uma vez só, como um string builder (aula 4, 0:01:43 a 0:02:04). Remover da lista reordena os elementos seguintes, criar uma lista nova só adiciona referências (aula 11, 0:01:27 a 0:01:49). E `pop(0)` quebra a exigência de tempo linear sem que a lógica esteja errada, porque a lista do Python reindexa tudo ao tirar do começo (aula 12, 0:02:12 a 0:02:53).

### 3.5 Separar as tarefas em funções

Nos programas de linha de comando, o comum é misturar abrir, processar, contar e imprimir num algoritmo só; o desafio é listar as tarefas e encapsular cada uma numa função, numa composição de funções (aula 13, 0:05:30 a 0:06:08). Os dois modos do wordcount só diferem na ordenação e no limite, e o código deve ser organizado para que só essa diferença seja distinta (aula 13, 0:06:10 a 0:06:47).

## 4. As aulas em uma tabela

| # | Título | Duração | Foco em uma linha |
|---|---|---|---|
| 0 | #00: Bem vindo | 5:36 | Prática (0:00:05); como obter o repositório (0:01:05); testes autocorrigíveis (0:03:13); passos de bebê (0:03:49). |
| 1 | #01: Quantos bolinhos você come? | 2:10 | donuts: condicional, conversão de tipo, nomes, um só return, linearidade (0:01:18 a 0:02:02). |
| 2 | #02: Construindo a sua String | 1:23 | both_ends: slice (0:00:50); uma linha (0:00:58); contar com while (0:01:05). |
| 3 | #03: Mexendo na sua String | 2:37 | fix_start: replace (0:01:18); algoritmo próprio (0:01:39); legibilidade e nomes (0:02:05). |
| 4 | #04: Tudo junto e misturado | 3:09 | mix_up: replace ou slice (0:01:08); concatenação contra join (0:01:31); um teste que rompe a premissa (0:02:10). |
| 5 | #05: Verbificando | 2:22 | verbing: três caminhos lógicos (0:00:57); nomes do domínio (0:01:32); uma bifurcação só (0:01:56). |
| 6 | #06: Seja otimista! | 2:48 | not_bad: find, replace, algoritmo, regex (0:01:26); requisito novo e mais testes (0:01:43). |
| 7 | #07: Recortar e Colar | 3:44 | front_back: cálculo do índice (0:02:00); repetição e encapsulamento (0:02:22); guardar as versões (0:03:23). |
| 8 | #08: Casando o começo e o fim | 3:14 | match_ends: contador, list comprehension, generator (0:01:45 a 0:02:37); o óbvio é melhor (0:02:37). |
| 9 | #09: Mulheres, crianças.. e a letra 'X' na frente | 3:02 | front_x: dividir e conquistar mantendo a semântica (0:01:25); uma ordenação só (0:02:16); função de ordenação (0:02:34). |
| 10 | #10: Ordenação, Só que não... | 2:57 | sort_last: o parâmetro key (0:00:51); escrever o próprio sort (0:01:32); lambda e itemgetter (0:02:15). |
| 11 | #11: Reunindo os Vizinhos | 2:48 | remove_adjacent: nova lista contra remoção (0:01:12); sem índice, com zip (0:02:06). |
| 12 | #12: Um desafio de Complexidade | 3:44 | linear_merge: complexidade (0:01:03); pop(0) contra pop(-1) (0:02:12); pesquise o ecossistema (0:03:05). |
| 13 | #13: O dicionário de Palavras | 7:37 | wordcount: por partes (0:03:08); with open (0:05:11); composição de funções (0:05:47); o print fora das funções (0:07:00). |
| 14 | #14: Gerador de Lero-Lero | 4:54 | mimic: o dicionário de imitação (0:00:27); recursão (0:03:19); defaultdict e Counter, sem if (0:04:06). |

## 5. Resumo por aula

### Aula 0: #00 - Bem vindo
Vídeo: https://www.youtube.com/watch?v=LzvdFV2-zns · Duração: 5:36

Resumo: ele se apresenta como guia e diz que programar exige prática, e que dominar as ferramentas pede exercícios e desafios (0:00:00 a 0:00:18). Gosta destes porque são simples e diretos, têm muitas formas de resolver e podem ser refeitos com a pergunta de como fazer diferente (0:00:18 a 0:00:52). Mostra o repositório no GitHub dele e as três formas de obtê-lo: fork, clone, ou download do zip para quem ainda não domina Git (0:01:05 a 0:01:52). Recomenda o PyCharm [legenda: phy charme, pai charme] na versão Community [legenda: com minion], gratuita (0:01:54 a 0:02:13). Os arquivos estão em ordem e a ordem deve ser respeitada porque a complexidade cresce aos poucos; se um parecer fácil, sofistique em vez de pular (0:02:13 a 0:02:46). Cada exercício tem sua aula, e ele mesmo responde dúvidas nos comentários (0:02:46 a 0:02:59). Roda o primeiro arquivo no PyCharm: a rotina de teste mostra o que corrigir, o exercício é autocorrigível, e qualquer estratégia vale se o resultado estiver certo (0:03:01 a 0:03:30). Lê a saída: o xizinho vermelho diz que `donuts` com 4 retornou None [legenda: Nani] e qual era o correto (0:03:30 a 0:03:49). Pede que se avance devagar, um movimento de cada vez, em passos de bebê, para usar o erro como ferramenta de aprendizado (0:03:49 a 0:04:16); quando todos os testes estiverem verdes, passe ao próximo (0:04:18 a 0:04:28). Anuncia a estrutura das aulas seguintes e as marcações de pausa contra spoiler (0:04:28 a 0:05:09), e fecha com a zona de conforto (0:05:17 a 0:05:35).

Linha do tempo:
- [0:00:05] programar exige prática
- [0:00:20] simples e diretos, muitas formas de resolver
- [0:00:45] como é que eu poderia fazer diferente
- [0:01:05] o repositório: fork, clone ou zip
- [0:02:00] PyCharm Community
- [0:02:26] respeite a ordem; se for fácil, sofistique
- [0:03:13] testes autocorrigíveis
- [0:03:53] passos de bebê, um movimento de cada vez
- [0:04:30] a estrutura das aulas e a pausa
- [0:05:17] sair da zona de conforto

Princípios:
- Pratique: resolver, comparar e refazer (0:00:05 a 0:00:52).
- O resultado correto é o que conta, qualquer que seja a estratégia (0:03:24 a 0:03:30).
- Passos de bebê, um movimento de cada vez, e o erro como ferramenta (0:03:53 a 0:04:16).

Código: nenhum escrito. Ele roda `01_donuts.py` publicado, cujo corpo é `return` (`01_donuts.py:12-14` em `ae90952`), e lê a saída do verificador `test` (`01_donuts.py:19-33`).

Citações (paráfrases de legenda, não verificadas):
- [0:00:05] programar exige prática e para você dominar todos os recursos das Ferramentas é muito importante você explorar exercícios e desafios
- [0:03:24] o exercício é alto corrigível [autocorrigível] então não importa qual a estratégia de programação você use se o resultado estiver correto tá tudo certo
- [0:03:53] é muito importante fazer as coisas bem devagar passo a passo preocupado em apenas um movimento de cada vez
- [0:05:17] os desafios existem para tirar você da zona de conforto

### Aula 1: #01 - Quantos bolinhos você come?
Vídeo: https://www.youtube.com/watch?v=qsuilI_CyFk · Duração: 2:10

Resumo: lê o enunciado do donuts: o contador vira a string Number of donuts com o número, ou many [legenda: mani, Manny] de 10 em diante (0:00:00 a 0:00:44). Roda os testes e aponta que os quatro casos (4, 9, 10 e 99) qualificam os limites do código, com 9 e 10 na fronteira do enunciado (0:00:44 a 0:01:06). Depois da pausa, as observações: o exercício estabelece a bifurcação da execução por condicional (0:01:18 a 0:01:25), trabalha a transformação de número em string (0:01:26 a 0:01:39), pede atenção aos nomes das variáveis (0:01:40 a 0:01:45), propõe resolver com um só return [legenda: retâneo] (0:01:48 a 0:01:53) e pede que, depois de implementar, se reduzam as repetições, tornando o código o mais linear possível (0:01:53 a 0:02:02).

Linha do tempo:
- [0:00:00] o enunciado
- [0:00:44] rodar os testes
- [0:00:51] quatro testes que qualificam os limites
- [0:01:02] 9 e 10 no limite do enunciado
- [0:01:18] bifurcação por condicional
- [0:01:40] os nomes das variáveis
- [0:01:48] um só return
- [0:01:53] menos repetição, mais linear

Princípios:
- Os testes marcam os limites do enunciado (0:00:51 a 0:01:06).
- Um só return; reduza a repetição; código o mais linear possível (0:01:48 a 0:02:02).

Código: nenhum escrito; os quatro casos estão em `01_donuts.py:38-41`.

Citações (paráfrases de legenda, não verificadas):
- [0:01:02] Observe que 9 e 10 estão no limite do enunciado
- [0:01:40] uma coisa interessante é você prestar bastante atenção nas variáveis os nomes de variáveis
- [0:01:55] depois que você implementar Observe se é possível reduzir as repetições simplificando o seu código tornando ele o mais linear possível

### Aula 2: #02 - Construindo a sua String
Vídeo: https://www.youtube.com/watch?v=BYWIU1fRxYo · Duração: 1:23

Resumo: o both_ends [legenda: buffeends] devolve os dois primeiros e os dois últimos caracteres, ou string vazia se o tamanho for menor que 2 (0:00:00 a 0:00:31). Dos quatro casos, os dois primeiros parecem o enunciado e os dois últimos são especiais (0:00:31 a 0:00:43). A dica: é simples se lembrar do slice (0:00:50 a 0:00:55); dá para fazer em uma linha, e ele pergunta se fica bom assim (0:00:58 a 0:01:02); se ficou fácil, conte com `while` [legenda: Will] na mão e veja se o código fica organizado e expressivo sem as facilidades do Python (0:01:05 a 0:01:20).

Linha do tempo:
- [0:00:00] o enunciado
- [0:00:31] rodar os testes
- [0:00:36] dois casos comuns, dois especiais
- [0:00:50] o slice
- [0:00:58] uma linha: será que fica bom assim
- [0:01:07] contar com while, sem as facilidades

Princípios:
- Uma linha é um experimento, não um objetivo (0:00:58 a 0:01:02).
- Organizado e expressivo mesmo sem os atalhos da linguagem (0:01:09 a 0:01:20).

Código: nenhum escrito; os casos estão em `02_both_ends.py:36-39`, e o caso `'a'` dá `''` (`:38`).

Citações (paráfrases de legenda, não verificadas):
- [0:00:58] dá para fazer esse código em uma única linha será que fica bom assim vai experimentar
- [0:01:12] para ver se você consegue deixar o código organizado expressivo mesmo sem usar as mil facilidades do pai [Python]

### Aula 3: #03 - Mexendo na sua String
Vídeo: https://www.youtube.com/watch?v=WNc--Gb3jtE · Duração: 2:37

Resumo: o fix_start [legenda: fixx start] troca por asterisco as ocorrências do primeiro caractere, menos a primeira; babble [legenda: deble, bable] vira ba**le (0:00:00 a 0:00:29). Os quatro casos: babble, aardvark [legenda: arde varcing], google, e donut [legenda: Dantes], sem outra ocorrência, que volta igual; os casos já dão dicas (0:00:29 a 0:01:03). As observações: o enunciado sugere o `replace`, que troca todas as ocorrências, não é exatamente o que se quer, mas já é alguma coisa (0:01:08 a 0:01:39); se achar fácil, escreva o próprio algoritmo com os comandos básicos, e para explorar tente em uma linha (0:01:39 a 0:01:54). Em exercício que parece simples se perde o cuidado com a organização; este serve para exercitar eliminar repetição e focar em legibilidade, com nomes de variáveis auxiliares significativos e curtos, para um código simples, legível e eficiente (0:01:55 a 0:02:26). Pede que o aluno publique a solução e ponha o link nos comentários (0:02:26 a 0:02:34).

Linha do tempo:
- [0:00:00] o enunciado
- [0:00:29] rodar os testes
- [0:00:56] a palavra sem ocorrência volta igual
- [0:01:18] a dica do replace
- [0:01:39] o próprio algoritmo; uma linha
- [0:01:55] exercício simples, cuidado perdido
- [0:02:07] repetição, legibilidade e nomes curtos e significativos

Princípios:
- Exercício simples não dispensa organização (0:01:55 a 0:02:05).
- Nomes auxiliares significativos sem ser grandes (0:02:09 a 0:02:22).

Código: nenhum escrito. A dica está no enunciado publicado (`03_fix_start.py:12-13`).

Citações (paráfrases de legenda, não verificadas):
- [0:01:55] quando a gente vê exercícios que parecem simples assim a gente muitas vezes deixa perde um certo cuidado com a organização do código
- [0:02:09] o foco em legibilidade como é que você consegue se elegível [ser legível] utilizar nomes de variáveis auxiliares que são significativos e ao mesmo tempo não ocupam muito espaço

### Aula 4: #04 - Tudo junto e misturado
Vídeo: https://www.youtube.com/watch?v=DgSKYuTfMCc · Duração: 3:09

Resumo: o mix_up junta duas strings com espaço trocando os dois primeiros caracteres de cada uma; mix e pod viram pox mid, e as strings têm tamanho 2 ou mais (0:00:00 a 0:00:36). Os quatro casos usam os exemplos e outros maiores da mesma natureza (0:00:36 a 0:00:47). Depois da pausa, diz que o exercício revela abordagens diferentes: resolver uma coisa de cada vez com `replace`, ou usar o slice, mais enxuto (0:01:01 a 0:01:29). Há duas formas de juntar: concatenação e `join` [legenda: John]; a concatenação produz uma nova string em memória a cada operação e, repetida, é ineficiente, enquanto o `join` faz uma vez só, como um string builder de outras linguagens (0:01:31 a 0:02:04). Também cabe em uma linha (0:02:06 a 0:02:10). A provocação: o enunciado assume pelo menos dois caracteres para dispensar validação; crie um caso de teste que rompa a premissa, pela linha 45, com o resultado esperado, e faça o código validar sem misturar com o que já funcionava (0:02:10 a 0:02:55).

Linha do tempo:
- [0:00:00] o enunciado
- [0:00:36] rodar os testes
- [0:01:03] abordagens diferentes
- [0:01:24] o slice deixa o código enxuto
- [0:01:31] concatenação ou join
- [0:01:47] a concatenação cria uma string a cada operação
- [0:02:10] a premissa de dois caracteres
- [0:02:25] um caso de teste novo que rompe a premissa
- [0:02:51] sem misturar com o que já funcionava

Princípios:
- Conheça o custo da operação: concatenação repetida contra `join` (0:01:43 a 0:02:04).
- Mude a premissa escrevendo primeiro o caso de teste (0:02:25 a 0:02:51).

Código: nenhum escrito. Os casos ficam em `04_mix_up.py:41-44`, e a linha 45 que ele indica é a seguinte à última chamada de `test`; o verificador recebe os dois argumentos como tupla e os espalha com `f(*in_)` (`04_mix_up.py:27`).

Citações (paráfrases de legenda, não verificadas):
- [0:01:47] a concatenação a cada operação ela produz uma nova string em memória então se você faz isso muitas vezes repetidas é ineficiente
- [0:01:58] o método Joe [join] ele faz uma vez só ele é extremamente eficiente funciona como um string builder em outras linguagens
- [0:02:25] eu te provoco agora para criar um novo caso de teste para abrir mão desse pressuposto
- [0:02:52] vamos ver se você consegue fazer isso sem misturar com o que já tava funcionando

### Aula 5: #05 - Verbificando
Vídeo: https://www.youtube.com/watch?v=6pWg3dljBOo · Duração: 2:22

Resumo: o verbing [legenda: Furby] acrescenta ing a strings de três ou mais caracteres, ly se já terminarem em ing, e não mexe nas menores que 3 (0:00:00 a 0:00:23). Os três casos cobrem um caminho cada, e assim os testes delineiam os limites do problema (0:00:23 a 0:00:39). A lógica é simples, mas o exercício abre espaço para a estética do código: não tem dois caminhos lógicos, tem três, e com cuidado quatro, e a forma de organizar a execução define a estética final (0:00:46 a 0:01:18). Sugere quebrar em partes menores com nomes muito específicos, e evitar variáveis como `s`, texto ou mensagem, sem relação com o domínio; o problema é manipulação de verbos, e é nele que se busca o nome (0:01:21 a 0:01:50). Cabe em uma linha, mas ele não acha tão elegante (0:01:50 a 0:01:56); prefere isolar o processamento da tomada de decisão, para um código quase linear com uma bifurcação só (0:01:56 a 0:02:11).

Linha do tempo:
- [0:00:00] o enunciado
- [0:00:23] três casos de teste
- [0:00:34] os testes delineiam os limites
- [0:00:57] três caminhos lógicos, talvez quatro
- [0:01:21] partes menores, nomes específicos
- [0:01:32] evite s, texto, mensagem
- [0:01:50] uma linha, pouco elegante
- [0:01:58] isolar a decisão; quase linear

Princípios:
- Nomes do domínio do problema, nunca genéricos (0:01:32 a 0:01:50).
- Isole a decisão; uma bifurcação no meio de um caminho linear (0:01:56 a 0:02:11).

Código: nenhum escrito. Observação deste documento, não dele: o esqueleto publicado nomeia o parâmetro `s` (`05_verbing.py:13`, também `02_both_ends.py:10`, `03_fix_start.py:16`, `06_not_bad.py:12`), exatamente o nome que ele pede para evitar nas variáveis.

Citações (paráfrases de legenda, não verificadas):
- [0:00:57] a coisa mais interessante é que ele não tem dois caminhos lógicos ele tem três na verdade
- [0:01:32] então evite variáveis como s ou texto ou mensagem coisas que não estão relacionadas com o domínio do problema
- [0:01:52] dá para fazer esse cara em apenas uma única linha mas eu não acho que fica tão elegante
- [0:02:04] você consegue ter um código quase linear como uma simples bifurcação no meio do caminho

### Aula 6: #06 - Seja otimista! O copo está meio cheio, não meio vazio.
Vídeo: https://www.youtube.com/watch?v=XANYQVu3sdI · Duração: 2:48

Resumo: o not_bad troca o trecho entre not e bad por good quando bad vem depois de not (0:00:00 a 0:00:31). Os quatro casos: not so bad vira good; o segundo e o terceiro saem truncados na legenda; o terceiro não tem substituição e o quarto, com bad antes de not, fica igual (0:00:31 a 0:01:09). Há várias formas: `find`, `replace`, um algoritmo próprio, expressões regulares, e vale fazer o máximo de versões (0:01:17 a 0:01:43). Propõe incrementar o enunciado como se entrasse um requisito novo no meio do projeto: not not bad, dois not bad seguidos, bad antes de um not bad; qual é a resiliência do algoritmo, e para saber, incremente os testes com todas as opções (0:01:43 a 0:02:22). Com regex a solução fica elegantíssima, embora exija conhecimento mais avançado (0:02:25 a 0:02:40).

Linha do tempo:
- [0:00:00] o enunciado
- [0:00:31] rodar os testes
- [0:01:02] bad antes de not fica igual
- [0:01:26] find, replace, algoritmo, regex
- [0:01:41] o máximo de versões
- [0:01:45] um requisito novo no meio do projeto
- [0:02:06] a resiliência do algoritmo
- [0:02:15] incrementar os testes com todas as opções
- [0:02:33] regex: elegantíssima

Princípios:
- Requisito novo entra primeiro como teste (0:02:15 a 0:02:22).
- Faça várias versões do mesmo código (0:01:41 a 0:01:43).

Código: nenhum escrito; os casos estão em `06_not_bad.py:38-41`.

Citações (paráfrases de legenda, não verificadas):
- [0:01:43] você pode incrementar enunciado como se entrasse um novo requisito no meio do projeto
- [0:02:06] Qual é a resiliência do algoritmo que você implementou
- [0:02:15] vale a pena você incrementar os testes colocando todas as opções para ver como é que o seu código se comporta

### Aula 7: #07 - Recortar e Colar
Vídeo: https://www.youtube.com/watch?v=yBBTuQ_Zjjo · Duração: 3:44

Resumo: o front_back divide cada string ao meio, com o caractere extra na frente quando o tamanho é ímpar, e monta frente de a, frente de b, trás de a, trás de b (0:00:00 a 0:00:37). Percorre os três casos, par, ímpar, Kitten e Donut (0:00:37 a 0:01:36). É um dos desafios de que ele mais gosta (0:01:43 a 0:01:48). Espera o slice, mas o índice pode ser calculado com os operadores aritméticos, com o módulo, ou com uma rotina da biblioteca padrão [legenda: Seal; provável: `math.ceil`] (0:01:51 a 0:02:19). Pergunta se o cálculo do índice se repete para a e para b e se não cabe algo que os dois usem, e se há variáveis auxiliares demais; o exercício permite extrair a lógica e reaplicá-la, um encapsulamento (0:02:22 a 0:02:52). Para juntar, concatenação ou `join` [legenda: joia], que ele já disse ser mais eficiente (0:03:00 a 0:03:16). Pede que o exercício seja refeito várias vezes e que as versões sejam guardadas, não apagadas, para comparar (0:03:16 a 0:03:33).

Linha do tempo:
- [0:00:00] o enunciado
- [0:00:37] rodar os testes
- [0:01:46] um dos desafios que ele mais gosta
- [0:01:55] o slice e o cálculo do índice
- [0:02:24] a repetição do cálculo para a e b
- [0:02:39] variáveis auxiliares demais
- [0:02:46] extrair a lógica e reaplicar
- [0:03:00] concatenação ou join
- [0:03:23] guarde todas as versões

Princípios:
- Repetição vira uma função que os dois casos usam (0:02:22 a 0:02:52).
- Guarde as versões e compare (0:03:23 a 0:03:33).

Código: nenhum escrito; os casos estão em `07_front_back.py:39-41`.

Citações (paráfrases de legenda, não verificadas):
- [0:02:24] é muito importante você ver se houve repetição você tá fazendo o cálculo do índice tanto para o ar [a] quanto para o b separadamente
- [0:02:46] esse é o exercício interessante que permite você fazer um encapsulamento onde você extrai a lógica como comandos e reaplica ela
- [0:03:23] lembre-se de guardar todas as suas versões não apenas delete o código e escreva um novo

### Aula 8: #08 - Casando o começo e o fim
Vídeo: https://www.youtube.com/watch?v=vRQO4mQ4TDk · Duração: 3:14

Resumo: o match_ends [legenda: match ands] conta as strings com dois ou mais caracteres e o primeiro igual ao último (0:00:00 a 0:00:16). A dica do enunciado: o Python não tem `++`, mas `+=` funciona (0:00:16 a 0:00:32). Lê os três casos e por que cada resposta é 3, 2 e 1 (0:00:36 a 0:01:34). A solução simples é percorrer a sequência e incrementar um contador (0:01:45 a 0:01:56). Dá para fazer diferente: com list comprehension [legenda: Lis compro rations], gerando a lista dos que respeitam a restrição, ou com generator expression, pensando no que acumular a cada iteração (o número 1) e usando uma função do Python para o resultado final (0:01:59 a 0:02:37). E então a reflexão: nem sempre o código mais sofisticado é o melhor; a solução mais óbvia e mais simples costuma ser a mais eficiente em memória, em legibilidade e em manutenibilidade, e usar recursos avançados não garante o melhor código; como é desafio, vale fazer de várias maneiras (0:02:37 a 0:03:05).

Linha do tempo:
- [0:00:00] o enunciado
- [0:00:16] sem ++, com +=
- [0:00:36] rodar os testes
- [0:01:45] a solução simples: percorrer e contar
- [0:02:04] list comprehension
- [0:02:16] generator expression: o que acumular
- [0:02:37] nem sempre o mais sofisticado é o melhor
- [0:03:00] no desafio, várias maneiras

Princípios:
- O óbvio e simples costuma ganhar em memória, legibilidade e manutenção (0:02:37 a 0:03:00).

Código: nenhum escrito. A função do Python que ele não nomeia em 0:02:35 é, por leitura deste documento, `sum`.

Citações (paráfrases de legenda, não verificadas):
- [0:02:39] esse desafio promove uma reflexão interessante porque nem sempre o código mais sofisticado é o melhor
- [0:02:44] a solução mais óbvia e mais simples ela costuma ser a mais eficiente em termos de memória em termos de legibilidade e em termos de manutibilidade [manutenibilidade] do seu código
- [0:02:55] nem sempre usar recursos avançados significa que você vai conseguir fazer o melhor código

### Aula 9: #09 - Mulheres, crianças.. e a letra 'X' na frente
Vídeo: https://www.youtube.com/watch?v=CnTrJXG75h0 · Duração: 3:02

Resumo: o front_x ordena a lista pondo primeiro as strings que começam com x; a dica do enunciado é criar duas listas e ordenar cada uma (0:00:00 a 0:00:31). Os testes pedem tratar o x como prioridade, contra a ordem natural das letras (0:00:34 a 0:01:10). A sugestão de separar em dois é dividir e conquistar, uma das estratégias mais usadas na computação (0:01:25 a 0:01:36); ao dividir, mantenha a semântica do problema, sem variáveis de nome esquisito: a lista das que contêm x na primeira posição e a das que não contêm, apegando-se ao domínio em vez de um atalho que complica o entendimento de quem lê (0:01:36 a 0:02:14). Pergunta quantas ordenações o código faz e se dá com uma só (0:02:16 a 0:02:28). Há list comprehension [legenda: lixo compro ranchos] e generator [legenda: Generation] (0:02:28 a 0:02:34), e a forma mais legal, que parece um hack, é subverter a função de ordenação do Python passando uma função que muda a lógica da ordenação, um grande bônus (0:02:34 a 0:02:52).

Linha do tempo:
- [0:00:00] o enunciado e a dica das duas listas
- [0:00:34] rodar os testes
- [0:01:05] o x como prioridade
- [0:01:28] dividir e conquistar
- [0:01:39] manter a semântica do problema
- [0:02:03] apegar-se ao domínio, sem atalho
- [0:02:16] quantas ordenações
- [0:02:37] passar uma função para a ordenação

Princípios:
- Ao dividir o problema, os nomes continuam sendo do problema (0:01:36 a 0:02:14).
- Mude a ordenação passando uma função, não reescrevendo o algoritmo (0:02:34 a 0:02:52).

Código: nenhum escrito; a dica está em `09_front_x.py:10-11`.

Citações (paráfrases de legenda, não verificadas):
- [0:01:39] quando você divide o problema em problemas menores mantenha a semântica do seu problema
- [0:02:01] isso é um exemplo de como você consegue se apegar ao domínio do problema ao invés de simplesmente escolher um atalho uma variável rápida
- [0:02:37] a forma mais legal que parece meio que um Hack é você subverter a função de ordenação que o próprio Python já traz

### Aula 10: #10 - Ordenação, Só que não...
Vídeo: https://www.youtube.com/watch?v=MzIokXlMfPQ · Duração: 2:57

Resumo: o sort_last [legenda: soft last] ordena tuplas pelo último elemento (0:00:00 a 0:00:39). Os três casos limitam o comportamento e evitam coincidências no código (0:00:39 a 0:00:51). A dica do enunciado é a key function: o `sort` do Python aceita o parâmetro `key` [legenda: que], uma função chave que influencia a lógica do algoritmo, recurso que todo mundo usa e muitas vezes não para para entender (0:00:51 a 0:01:17). Para dominar o que está por baixo, escreva o próprio algoritmo de ordenação com o mesmo comportamento: comece simples, com o loop, faça funcionar, e só depois procure onde pôr uma função que muda o comportamento; isso dá o insight de como é elegante a solução do Python (0:01:25 a 0:02:13). Com o sort do Python, a chave pode ser uma `lambda`, uma função definida, ou a `itemgetter` [legenda: getsiten] da biblioteca padrão, do repertório funcional (0:02:13 a 0:02:36).

Linha do tempo:
- [0:00:00] o enunciado
- [0:00:41] três casos que evitam coincidências
- [0:00:54] a key function
- [0:01:11] o recurso que todo mundo usa sem entender
- [0:01:39] escrever o próprio sort
- [0:01:50] simples primeiro, a função chave depois
- [0:02:19] lambda, função, itemgetter
- [0:02:40] expandir o repertório

Princípios:
- Faça funcionar simples primeiro; depois procure o ponto de variação (0:01:47 a 0:02:04).
- Entenda o recurso que usa, reimplementando-o (0:01:32 a 0:02:13).

Código: nenhum escrito. Ilustração deste documento, não dele, com a ferramenta que ele cita (0:02:30 a 0:02:36); passa os três casos de `10_sort_last.py:38-43` (seção 14):

```python
from operator import itemgetter

def sort_last(tuples):
    return sorted(tuples, key=itemgetter(-1))
```

Citações (paráfrases de legenda, não verificadas):
- [0:00:43] ele tem três casos de teste e servem para você limitar o comportamento e evitar a Coincidências no código
- [0:01:50] comece fazendo o algoritmo de ordenação simples com o código lá dentro usa lá o seu loop tudo mais e faz a coisa funcionar Somente depois
- [0:02:09] vai te dar um Insight de com sofisticado de como elegante a solução que o pai Então [Python] traz para esse problema

### Aula 11: #11 - Reunindo os Vizinhos
Vídeo: https://www.youtube.com/watch?v=yaKSFhh9ELE · Duração: 2:48

Resumo: o remove_adjacent [legenda: remover] reduz elementos adjacentes iguais a um só; 1, 2, 2, 3 vira 1, 2, 3 (0:00:00 a 0:00:25). Dos quatro casos, o terceiro é o caso limite da lista vazia e o quarto mostra que só os adjacentes saem, sem tornar a lista única (0:00:25 a 0:01:03). Na experiência dele há duas abordagens: alterar a lista removendo adjacentes, ou criar uma lista nova; o resultado é o mesmo, a performance é completamente distinta, porque remover reordena os elementos seguintes e criar uma lista nova só adiciona referências a objetos que já existem (0:01:12 a 0:01:49). É comum usar índice para comparar o anterior com o atual, e funciona; o grande lance é fazer sem índice nenhum, porque no Python dificilmente se precisa de índice, e a função `zip` ajuda, pedindo pensar fora da caixa (0:01:49 a 0:02:30). Cabe numa linha, mas fica bem esquisito (0:02:30 a 0:02:36).

Linha do tempo:
- [0:00:00] o enunciado
- [0:00:25] rodar os testes
- [0:00:38] o caso limite da lista vazia
- [0:00:48] adjacentes, não únicos
- [0:01:16] remover ou criar lista nova
- [0:01:33] a performance é distinta
- [0:02:06] sem índice nenhum
- [0:02:19] o zip
- [0:02:32] uma linha fica esquisito

Princípios:
- Prefira construir uma lista nova a remover da lista existente (0:01:27 a 0:01:49).
- No Python dificilmente se precisa de índice (0:02:13 a 0:02:19).

Código: nenhum escrito. Ilustração deste documento, não dele, com o `zip` que ele sugere; passa os quatro casos de `11_remove_adjacent.py:37-40` (seção 14):

```python
def remove_adjacent(nums):
    return [current for previous, current in zip([None] + nums, nums) if current != previous]
```

Citações (paráfrases de legenda, não verificadas):
- [0:01:30] O resultado é o mesmo mas a solução a performance do algoritmo é completamente distinta
- [0:01:38] quando você remove o elemento de uma lista ele precisa reordernar [reordenar] os elementos que vem depois já quando você cria uma nova lista tudo que você está fazendo é adicionar referências para objetos que já existem
- [0:02:13] sim no Python dificilmente você precisa usar índice

### Aula 12: #12 - Um desafio de Complexidade
Vídeo: https://www.youtube.com/watch?v=-Fi39s1-HjU · Duração: 3:44

Resumo: o linear_merge [legenda: linear] combina duas listas ordenadas numa só, em tempo linear, uma passagem em cada lista; pode modificar as listas recebidas (0:00:00 a 0:00:30). Três casos (0:00:30 a 0:00:48). O exercício toca a complexidade de algoritmos [legenda: complexidade algoritmo] e a eficiência de cada comando do Python (0:00:59 a 0:01:19): juntar e ordenar não é linear (0:01:19 a 0:01:26). A imagem é a fila de escola: duas filas em ordem de nome, compara-se o primeiro de cada uma e se chama o menor (0:01:26 a 0:01:56). Há duas estratégias, um sentinela que percorre sem alterar as listas, ou consumir as listas como o enunciado sugere (0:01:56 a 0:02:12). Quem consome com `pop(0)` não respeita o tempo linear, e isso não tem a ver com a lógica, mas com a lista do Python: pôr no fim não custa nada, tirar do começo reindexa todo mundo; com `pop(-1)`, numa lógica inversa a partir do fim, a solução é linear (0:02:12 a 0:03:05). A lição: pesquisar o ecossistema antes de sair fazendo, porque já existe na biblioteca o `heapq` [legenda: rip] com a função `merge` [legenda: nerd], que resolve em uma linha (0:03:05 a 0:03:34).

Linha do tempo:
- [0:00:00] o enunciado: tempo linear
- [0:00:30] rodar os testes
- [0:01:07] complexidade de algoritmos
- [0:01:19] juntar e ordenar não é linear
- [0:01:31] a fila de escola
- [0:01:58] sentinela ou consumir a lista
- [0:02:12] o pop(0) não é linear
- [0:02:34] a lista do Python reindexa ao tirar do começo
- [0:02:53] o pop(-1) a partir do fim
- [0:03:07] pesquise o ecossistema
- [0:03:24] heapq.merge em uma linha

Princípios:
- O custo vem da estrutura, não só da lógica (0:02:26 a 0:02:53).
- Pesquise o ecossistema antes de fazer (0:03:07 a 0:03:15).

Código: nenhum escrito. Ilustração deste documento, não dele, com a função que ele cita (0:03:21 a 0:03:34); passa os três casos de `12_linear_merge.py:38-43` (seção 14):

```python
import heapq

def linear_merge(list1, list2):
    return list(heapq.merge(list1, list2))
```

Citações (paráfrases de legenda, não verificadas):
- [0:02:26] Infelizmente o seu código não está respeitando a restrição de tempo linear isso não tem nada a ver com a sua Lógica tem a ver com como o pop funciona
- [0:02:37] as listas no Python elas custam nada para você colocar um elemento no final mas se você tira um elemento do começo ele precisa rendexar [reindexar] todo mundo
- [0:03:07] esse desafio traz uma lição valiosa para a gente que é pesquisar o ecossistema antes de sair fazendo alguma coisa

### Aula 13: #13 - O dicionário de Palavras
Vídeo: https://www.youtube.com/watch?v=hDFc3cJyJMY · Duração: 7:37

Resumo: o wordcount [legenda: World count] conta as palavras de um arquivo de dois jeitos: `--count` lista todas em ordem alfabética com as ocorrências, usando o `letras.txt` do pacote (0:00:00 a 0:01:09), e `--topcount` lista as 20 mais frequentes, que ele lê como em ordem crescente de ocorrências e exemplifica com B 4, C 3, A 2, parando nas 20 primeiras (0:01:09 a 0:02:20). Há um esqueleto: a `main` chama `print_words` e `print_top` conforme o parâmetro, e o trabalho é escrever as duas (0:02:23 a 0:02:44). As dicas: palavras em caixa baixa, `split` sem parâmetros, e não sair programando muito tempo sem ver o que acontece; faça por etapas, imprima cada parte e só avance se resolveu a anterior (0:02:44 a 0:03:23). Mostra a estrutura e roda no terminal: sem argumentos, a mensagem de uso; com `--count`, o erro porque `print_words` não existe; com `--topcount`, o erro de `print_top`, e é assim que se acompanha a evolução do código (0:03:23 a 0:04:41). Depois da pausa: arquivo se abre com `open` e se fecha com `close`, ou com o context manager `with open`, que fecha sozinho (0:05:00 a 0:05:30). É comum começar pelo `print_words` misturando abrir, processar, contar e imprimir num algoritmo só; o exercício permite separar responsabilidades, listando as tarefas e encapsulando cada uma numa função, numa composição de funções, técnica muito importante de organização (0:05:30 a 0:06:10). O `print_top` reaproveita quase tudo: muda a ordenação e o limite, e o desafio é organizar o código para que só essa diferença seja distinta (0:06:10 a 0:06:47). Pede de novo atenção às palavras e aos termos, sem nomes fora do domínio de contagem de palavras (0:06:47 a 0:07:00), e deixa uma última provocação sobre a própria `main` do esqueleto: o nome das funções, `print_words` e `print_top`, é a dica; por que o print não está fora delas (0:07:00 a 0:07:18).

Linha do tempo:
- [0:00:00] o enunciado do --count
- [0:01:12] o --topcount e o limite de 20
- [0:02:23] o esqueleto: main, print_words, print_top
- [0:03:08] por partes, imprimindo cada etapa
- [0:03:55] rodar sem argumentos
- [0:04:22] o erro de print_words; a evolução pelo terminal
- [0:05:08] open e close, ou with
- [0:05:47] separar responsabilidades
- [0:06:03] composição de funções
- [0:06:37] só a diferença fica distinta
- [0:06:51] nomes do domínio de contagem de palavras
- [0:07:13] por que o print não está fora delas

Princípios:
- Faça por partes e veja cada etapa antes de avançar (0:03:08 a 0:03:23).
- Cada tarefa numa função; o programa é a composição delas (0:05:47 a 0:06:08).
- Só a diferença entre os dois modos deve ser distinta (0:06:37 a 0:06:47).

Código: nenhum escrito. Ele mostra o esqueleto publicado: a `main` valida `sys.argv` e chama `print_words(filename)` ou `print_top(filename)` (`13_wordcount.py:63-76`). A provocação de 0:07:13 aponta para essas chamadas: o nome das funções diz que elas imprimem. A resposta não é dada na aula.

Citações (paráfrases de legenda, não verificadas):
- [0:03:08] não saia programando durante muito tempo sem ver o que está acontecendo faça por partes por etapa e Imprima cada parte do seu Progresso
- [0:05:47] esse desafio oferece a oportunidade de você separar responsabilidades
- [0:05:56] você consegue encapsular cada tarefa numa função separada criando uma grande composição de funções Isso é uma técnica muito importante de organização de código
- [0:07:10] a dica vem do nome das funções que o desafio de propõe um é print Words o outro é print Stop [print_top] porque o print não tá fora deles

### Aula 14: #14 - Gerador de Lero-Lero
Vídeo: https://www.youtube.com/watch?v=pkYuKNKOAdw · Duração: 4:54

Resumo: o mimic [legenda: mimec] é um gerador de lero-lero: lê um arquivo, guarda a relação entre as palavras e gera um texto novo que imita o escritor (0:00:00 a 0:00:18). Os passos: abrir o arquivo da linha de comando, separar as palavras, criar o dicionário de imitação, em que cada palavra aponta para a lista das que vêm depois dela (0:00:18 a 0:00:40), com o exemplo do enunciado [legenda: a b c d a; o arquivo diz A B C B A] (0:00:40 a 0:01:16); a string vazia aponta para a primeira palavra, e a última aponta para a string vazia (0:01:16 a 0:01:33). Para emitir, imprime-se uma palavra e se sorteia a próxima entre as possíveis, com `random.choice` [legenda: renda um ponto Choice] (0:01:33 a 0:02:06). Roda no terminal: sem argumento pede o arquivo; com `small.txt` [legenda: mal potxt] não faz nada e não dá erro; `alice.txt` [legenda: ls.xt] é bem maior (0:02:09 a 0:02:41). Mostra a estrutura: `mimic_dict`, `print_mimic` e a `main` que coordena, guarda o resultado numa variável `dict` e chama `print_mimic` com a string vazia, o que sugere que dá para usar `print_mimic` recursivamente (0:02:44 a 0:03:26). Depois da pausa: a primeira solução de quem faz este desafio costuma ser pouco sofisticada, o foco é resolver o problema, e isso é bom (0:03:48 a 0:04:00); daí se enxuga o código até ficar muito pequeno, com `defaultdict` [legenda: the foldick] e depois `Counter` [legenda: Country] do módulo `collections`, e dá para fazer sem nenhum `if` (0:04:00 a 0:04:30). Por último, olhar a estrutura que o programa já dá e ver o que melhorar, já que existe uma composição entre várias funções que fazem cada uma uma parte (0:04:30 a 0:04:43).

Linha do tempo:
- [0:00:04] o gerador de lero-lero
- [0:00:27] o dicionário de imitação
- [0:01:20] a string vazia no começo e no fim
- [0:01:58] random.choice
- [0:02:19] rodar no terminal: small.txt e alice.txt
- [0:02:59] a main coordena
- [0:03:21] a dica da recursão
- [0:03:51] a primeira solução é pouco sofisticada, e tudo bem
- [0:04:06] enxugar: defaultdict e Counter
- [0:04:28] sem nenhum if
- [0:04:32] melhorar a estrutura dada

Princípios:
- Primeiro resolver o problema; enxugar depois (0:03:48 a 0:04:06).
- Programa como composição de funções que fazem cada uma uma parte (0:04:30 a 0:04:43).

Código: nenhum escrito. Ele mostra `14_mimic.py:46-66` publicado. Observação deste documento, não dele: a `main` guarda o dicionário numa variável chamada `dict`, que esconde o builtin (`14_mimic.py:65`); ele lê a linha (0:03:12 a 0:03:16) sem comentar o nome.

Citações (paráfrases de legenda, não verificadas):
- [0:03:51] sempre que eu faço esse Desafio ou passo para alguém fazer a primeira solução acaba sendo pouco sofisticada Na verdade o foco é resolver o problema isso é muito legal
- [0:04:03] enxugar o código até ele ficar muito pequeno
- [0:04:28] também é possível fazer esse código sem nenhum if

## 6. Princípios que atravessam toda a série

Doze regras que ele formula na fala. Nenhuma é inferência deste documento. A linha entre colchetes diz se a regra já existe em `kb/principles/`, se virou princípio novo, ou por que não foi promovida.

#### 1. Nomes vêm do domínio do problema

Atenção aos nomes das variáveis (aula 1, 0:01:40 a 0:01:45); nomes auxiliares significativos e curtos (aula 3, 0:02:09 a 0:02:22); evite `s`, texto, mensagem, e busque no problema a inspiração (aula 5, 0:01:32 a 0:01:50); ao dividir, mantenha a semântica e não pegue o atalho da variável rápida (aula 9, 0:01:36 a 0:02:14); nada fora do domínio de contagem de palavras (aula 13, 0:06:47 a 0:07:00).

[novo: `kb/principles/nomes-do-dominio-do-problema.md`; vizinho de `o-codigo-e-a-interface`, que trata nomes de classes e métodos como desenho]

#### 2. Nem sempre o código mais sofisticado é o melhor

O mais óbvio e simples costuma ser o mais eficiente em memória, legibilidade e manutenibilidade, e recurso avançado não garante o melhor código (aula 8, 0:02:37 a 0:03:00). A versão em uma linha é exercício, e ele mesmo a acha pouco elegante ou esquisita (aula 2, 0:00:58 a 0:01:02; aula 5, 0:01:50 a 0:01:56; aula 11, 0:02:30 a 0:02:36). A primeira solução pouco sofisticada, focada em resolver o problema, é bem-vinda (aula 14, 0:03:48 a 0:04:00).

[novo: `kb/principles/o-obvio-antes-do-sofisticado.md`; vizinho de `escolha-a-regra-mais-simples`, que trata regras de domínio]

#### 3. Reduza a repetição e mantenha o código linear

Depois de implementar, reduza as repetições e torne o código o mais linear possível (aula 1, 0:01:53 a 0:02:02); um só return (aula 1, 0:01:48 a 0:01:53); isole a decisão numa bifurcação só (aula 5, 0:01:56 a 0:02:11); o cálculo repetido para a e b vira algo que os dois usam (aula 7, 0:02:22 a 0:02:52).

[já no KB: `kb/principles/codigo-linear.md`]

#### 4. Passos de bebê: faça por partes e veja cada etapa

Um movimento de cada vez, usando o erro como ferramenta (aula 0, 0:03:49 a 0:04:16); não programe muito tempo sem ver o que acontece, imprima cada etapa e só avance se resolveu a anterior (aula 13, 0:03:08 a 0:03:23); rode o esqueleto e acompanhe a evolução pelo erro (aula 13, 0:04:22 a 0:04:41).

[já no KB: `kb/principles/teste-primeiro-das-folhas.md`, pelo ciclo curto de ver falhar e passar]

#### 5. Faça funcionar simples, depois sofistique

Comece com o loop, faça funcionar, e só depois procure onde pôr a função que muda o comportamento (aula 10, 0:01:47 a 0:02:04); primeiro resolver o problema, depois enxugar (aula 14, 0:03:48 a 0:04:06).

[já no KB: `kb/principles/funcione-direito-e-depois-rapido.md`]

#### 6. O teste diz os limites; o resultado é o que conta

O exercício é autocorrigível e qualquer estratégia vale se o resultado estiver correto (aula 0, 0:03:13 a 0:03:30). Os casos qualificam os limites do código (aula 1, 0:00:51 a 0:01:06), delineiam os limites do problema (aula 5, 0:00:34 a 0:00:39) e evitam coincidências no código (aula 10, 0:00:41 a 0:00:51).

[já no KB: `kb/principles/teste-o-efeito-nao-o-codigo.md`]

#### 7. Requisito novo entra primeiro como caso de teste

Rompa a premissa com um caso de teste novo e faça o código validar sem misturar com o que funcionava (aula 4, 0:02:10 a 0:02:55); trate a variação como requisito novo no meio do projeto e incremente os testes com todas as opções (aula 6, 0:01:43 a 0:02:22).

[já no KB: `kb/principles/teste-primeiro-das-folhas.md`]

#### 8. Uma função por tarefa; o programa é a composição

Liste as tarefas e encapsule cada uma numa função (aula 13, 0:05:47 a 0:06:08); só a diferença entre os modos fica distinta (aula 13, 0:06:10 a 0:06:47); melhore a estrutura dada pela composição (aula 14, 0:04:30 a 0:04:43); extraia a lógica e reaplique (aula 7, 0:02:46 a 0:02:52).

[já no KB, na escala de objeto: `kb/principles/uma-responsabilidade-por-identidade.md`]

#### 9. Passe o comportamento como função

Subverta a ordenação do Python passando uma função (aula 9, 0:02:34 a 0:02:52); a key function muda a lógica do algoritmo (aula 10, 0:00:51 a 0:01:17), e escrever o próprio sort mostra onde ela entra (aula 10, 0:01:57 a 0:02:13).

[já no KB: `kb/principles/separe-a-navegacao-da-decisao.md`]

#### 10. Conheça o custo da estrutura que usa

Concatenação repetida cria uma string a cada passo, o `join` faz uma vez (aula 4, 0:01:43 a 0:02:04; aula 7, 0:03:00 a 0:03:16); remover da lista reordena, criar lista nova só adiciona referências (aula 11, 0:01:27 a 0:01:49); `pop(0)` reindexa a lista e quebra o tempo linear, `pop(-1)` não (aula 12, 0:02:12 a 0:03:05). No Python dificilmente se precisa de índice (aula 11, 0:02:13 a 0:02:19).

[não promovido: é conhecimento da linguagem mais que regra de desenho; vizinho de `funcione-direito-e-depois-rapido`]

#### 11. Pesquise o ecossistema antes de fazer

Já existe `heapq.merge` (aula 12, 0:03:05 a 0:03:34); `itemgetter` na biblioteca padrão (aula 10, 0:02:26 a 0:02:36); `defaultdict` e `Counter` em `collections` (aula 14, 0:04:06 a 0:04:26).

[não promovido: dito como regra uma vez, na aula 12; vizinho de `use-o-framework-sem-abstrai-lo`]

#### 12. Refaça, guarde as versões e compare

Resolva várias vezes perguntando como fazer diferente (aula 0, 0:00:43 a 0:00:52); faça o máximo de versões (aula 6, 0:01:41 a 0:01:43); guarde todas, não apague, e compare (aula 7, 0:03:16 a 0:03:33).

[não promovido: método de estudo, não regra sobre o código]

## 7. Citações-chave do curso

Paráfrases de legenda automática, sem aspas e não verificadas contra o vídeo.

| Aula | Timestamp | Paráfrase |
|---|---|---|
| #0 | 0:00:05 | programar exige prática |
| #0 | 0:00:48 | aquela pergunta como é que eu poderia fazer diferente |
| #0 | 0:03:24 | não importa qual a estratégia de programação você use se o resultado estiver correto tá tudo certo |
| #0 | 0:04:05 | fazer as coisas em Passos de bebê é muito importante |
| #1 | 0:01:55 | Observe se é possível reduzir as repetições simplificando o seu código tornando ele o mais linear possível |
| #2 | 0:00:58 | dá para fazer esse código em uma única linha será que fica bom assim |
| #3 | 0:01:55 | quando a gente vê exercícios que parecem simples assim a gente muitas vezes deixa perde um certo cuidado com a organização do código |
| #4 | 0:01:47 | a concatenação a cada operação ela produz uma nova string em memória |
| #4 | 0:02:25 | criar um novo caso de teste para abrir mão desse pressuposto |
| #5 | 0:01:32 | evite variáveis como s ou texto ou mensagem coisas que não estão relacionadas com o domínio do problema |
| #6 | 0:01:43 | incrementar enunciado como se entrasse um novo requisito no meio do projeto |
| #7 | 0:03:23 | guardar todas as suas versões não apenas delete o código e escreva um novo |
| #8 | 0:02:39 | nem sempre o código mais sofisticado é o melhor |
| #8 | 0:02:44 | a solução mais óbvia e mais simples ela costuma ser a mais eficiente |
| #9 | 0:01:39 | quando você divide o problema em problemas menores mantenha a semântica do seu problema |
| #10 | 0:00:43 | servem para você limitar o comportamento e evitar a Coincidências no código |
| #11 | 0:02:13 | no Python dificilmente você precisa usar índice |
| #12 | 0:02:26 | isso não tem nada a ver com a sua Lógica tem a ver com como o pop funciona |
| #12 | 0:03:07 | pesquisar o ecossistema antes de sair fazendo alguma coisa |
| #13 | 0:03:08 | não saia programando durante muito tempo sem ver o que está acontecendo |
| #13 | 0:05:58 | encapsular cada tarefa numa função separada criando uma grande composição de funções |
| #14 | 0:03:51 | a primeira solução acaba sendo pouco sofisticada Na verdade o foco é resolver o problema |

## 8. A evolução técnica, aula a aula

Não há um programa que evolua: cada aula é um exercício novo. A tabela mostra a progressão dos recursos.

| Etapa | O que é feito | Conceito ou ferramenta | O que isso destrava |
|---|---|---|---|
| **#0** | Obter o kit, rodar o primeiro arquivo (0:01:05 a 0:04:28) | fork, clone, zip; o verificador `test` | Trabalhar com feedback imediato |
| **#1** | donuts (0:00:00 a 0:02:02) | condicional, conversão de tipo, um return | A bifurcação e o código linear |
| **#2** | both_ends (0:00:00 a 0:01:20) | slice, while | Fatiar strings |
| **#3** | fix_start (0:00:00 a 0:02:26) | `replace` | Métodos de string e nomes curtos significativos |
| **#4** | mix_up (0:00:00 a 0:02:55) | slice, `join`, caso de teste novo | Custo da concatenação; mudar premissa por teste |
| **#5** | verbing (0:00:00 a 0:02:11) | caminhos lógicos | Nomes do domínio; uma bifurcação só |
| **#6** | not_bad (0:00:00 a 0:02:40) | `find`, `replace`, regex | Várias versões; requisito novo como teste |
| **#7** | front_back (0:00:00 a 0:03:33) | índice por aritmética, módulo, `ceil` | Eliminar repetição por encapsulamento |
| **#8** | match_ends (0:00:00 a 0:03:05) | `+=`, list comprehension, generator expression | O óbvio contra o sofisticado |
| **#9** | front_x (0:00:00 a 0:02:52) | dividir e conquistar, uma ordenação | Passar função para a ordenação |
| **#10** | sort_last (0:00:00 a 0:02:36) | `key`, `lambda`, `itemgetter` | Entender o sort reimplementando-o |
| **#11** | remove_adjacent (0:00:00 a 0:02:36) | lista nova, `zip` | Iterar sem índice |
| **#12** | linear_merge (0:00:00 a 0:03:34) | complexidade, `pop(0)` contra `pop(-1)`, `heapq.merge` | Custo da estrutura; pesquisar o ecossistema |
| **#13** | wordcount (0:00:00 a 0:07:18) | arquivos, `with open`, `split`, linha de comando | Separar responsabilidades em funções |
| **#14** | mimic (0:00:00 a 0:04:43) | dicionário de listas, `random.choice`, recursão, `defaultdict`, `Counter` | Enxugar o código; melhorar a estrutura dada |

## 9. Arsenal técnico demonstrado no curso

Ele não escreve solução; a coluna diz onde ele indica cada recurso.

| Técnica ou recurso | Para que ele usa | Aula e timestamp |
|---|---|---|
| Fork, clone, download do zip | Obter o kit | #0, 0:01:22 a 0:01:52 |
| PyCharm Community | Editor recomendado, rodar pelo botão direito | #0, 0:02:00 a 0:03:09 |
| Verificador embutido (`test`) | Corrigir o exercício automaticamente | #0, 0:03:13 a 0:03:49 |
| Condicional | Bifurcar a execução | #1, 0:01:18 a 0:01:25 |
| Slice | Cortar strings | #2, 0:00:50; #4, 0:01:24; #7, 0:01:55 |
| `while` | Contar na mão, sem atalho | #2, 0:01:07 a 0:01:12 |
| `str.replace`, `str.find` | Trocar e achar trechos | #3, 0:01:18 a 0:01:36; #6, 0:01:26 a 0:01:33 |
| `str.join` | Juntar strings numa operação só | #4, 0:01:38 a 0:02:04; #7, 0:03:08 a 0:03:16 |
| Caso de teste acrescentado pelo aluno | Romper a premissa do enunciado | #4, 0:02:25 a 0:02:51; #6, 0:02:15 |
| Expressões regulares | Solução sucinta do not_bad | #6, 0:01:37; 0:02:33 a 0:02:40 |
| Módulo, `ceil` | Calcular o meio da string | #7, 0:02:00 a 0:02:19 |
| `+=` | Incrementar, já que não há `++` | #8, 0:00:16 a 0:00:32 |
| List comprehension, generator expression | Filtrar e acumular | #8, 0:01:59 a 0:02:37; #9, 0:02:28 |
| Dividir e conquistar | Separar o front_x em duas listas | #9, 0:01:25 a 0:01:36 |
| `key` do sort, `lambda`, `itemgetter` | Mudar a lógica da ordenação | #9, 0:02:34; #10, 0:00:51 a 0:01:17; 0:02:13 a 0:02:36 |
| `zip` | Comparar vizinhos sem índice | #11, 0:02:19 a 0:02:30 |
| `list.pop(-1)` no lugar de `pop(0)` | Manter o tempo linear | #12, 0:02:12 a 0:03:05 |
| `heapq.merge` | Merge linear em uma linha | #12, 0:03:16 a 0:03:34 |
| `with open` (context manager) | Fechar o arquivo sozinho | #13, 0:05:08 a 0:05:30 |
| `str.split()` sem argumentos, `lower` | Separar e normalizar palavras | #13, 0:02:44 a 0:03:08 |
| Composição de funções | Separar as tarefas do programa | #13, 0:05:47 a 0:06:47; #14, 0:04:30 |
| `random.choice` | Sortear a próxima palavra | #14, 0:01:54 a 0:02:06 |
| Recursão | Emitir o texto a partir da string vazia | #14, 0:03:19 a 0:03:26 |
| `collections.defaultdict`, `collections.Counter` | Enxugar o código, sem `if` | #14, 0:04:06 a 0:04:30 |

## 10. Glossário do curso

| Termo | Significado no contexto da série | Onde |
|---|---|---|
| **Desafio** | Um exercício do pacote, num arquivo numerado | #0, 0:00:52; 0:02:18 a 0:02:24 |
| **Autocorrigível** [legenda: alto corrigível] | O exercício que traz os próprios testes | #0, 0:03:22 a 0:03:26 |
| **Passos de bebê** | Um movimento de cada vez | #0, 0:04:05 a 0:04:16 |
| **Pausa** | A marcação antes das dicas, para evitar spoiler | #0, 0:04:56 a 0:05:01 |
| **Limite** | O caso que fica na fronteira do enunciado, como 9 e 10 no donuts | #1, 0:01:02 a 0:01:06 |
| **Caminho lógico** | Cada ramo da execução; o verbing tem três ou quatro | #5, 0:00:57 a 0:01:10 |
| **Estética do código** | Como a organização da execução aparece na forma final | #5, 0:00:52 a 0:01:18 |
| **Domínio do problema** | O vocabulário de onde os nomes devem vir | #5, 0:01:40; #9, 0:02:03; #13, 0:06:58 |
| **Resiliência do algoritmo** | Como a solução reage a entradas fora do enunciado | #6, 0:02:04 a 0:02:07 |
| **String builder** | O que o `join` faz, por comparação com outras linguagens | #4, 0:02:01 a 0:02:06 |
| **Encapsulamento** | Extrair a lógica repetida para reaplicá-la | #7, 0:02:46 a 0:02:52 |
| **Dividir e conquistar** | Quebrar o problema em problemas menores | #9, 0:01:30 a 0:01:36 |
| **Função chave** [legenda: Custom que] | A `key` passada ao sort | #10, 0:00:54 a 0:01:09 |
| **Complexidade de algoritmos** [legenda: complexidade algoritmo] | Eficiência das partes e de cada comando | #12, 0:01:05 a 0:01:19 |
| **Tempo linear** | Uma passagem em cada lista | #12, 0:00:20 a 0:00:27 |
| **Sentinela** | Marcador que percorre a lista sem alterá-la | #12, 0:01:58 a 0:02:04 |
| **Context manager** [legenda: contact Manager] | O `with`, que fecha o arquivo ao sair do bloco | #13, 0:05:16 a 0:05:28 |
| **Composição de funções** | O programa feito de funções que fazem uma tarefa cada | #13, 0:06:01 a 0:06:08; #14, 0:04:39 |
| **Lero-lero** | O texto gerado que imita o original | #14, 0:00:04 a 0:00:15 |
| **Dicionário de imitação** | Palavra para a lista das que vêm depois dela | #14, 0:00:27 a 0:00:40 |

## 11. Perguntas e respostas que o curso responde

#### Como o pacote se usa?

Baixe o repositório, abra a pasta no editor, faça os arquivos na ordem, rode cada um e avance quando todos os testes estiverem verdes (aula 0, 0:01:05 a 0:04:28). Em cada aula, pause antes das dicas (aula 0, 0:04:56 a 0:05:03).

#### O que faço se o exercício for fácil demais?

Não pule: sofistique a solução (aula 0, 0:02:33 a 0:02:46), escreva o próprio algoritmo (aula 3, 0:01:39 a 0:01:49; aula 10, 0:01:32 a 0:01:47) ou acrescente um caso de teste que rompa a premissa (aula 4, 0:02:10 a 0:02:51).

#### Fazer em uma linha é melhor?

Não necessariamente. É um bom exercício, mas ele acha pouco elegante ou esquisito (aula 5, 0:01:50 a 0:01:56; aula 11, 0:02:30 a 0:02:36), e o mais óbvio costuma ganhar em memória, legibilidade e manutenção (aula 8, 0:02:37 a 0:03:00).

#### Como escolher o nome das variáveis?

Pelo domínio do problema, nunca `s`, texto ou mensagem (aula 5, 0:01:32 a 0:01:50), significativo e curto (aula 3, 0:02:09 a 0:02:22), mantendo a semântica ao dividir o problema (aula 9, 0:01:36 a 0:02:14).

#### Concatenar strings com + ou usar join?

`join`: a concatenação cria uma string nova a cada operação, o `join` faz uma vez só (aula 4, 0:01:43 a 0:02:04; aula 7, 0:03:08 a 0:03:16).

#### Por que meu merge com pop(0) não é linear?

Porque a lista do Python reindexa tudo ao tirar do começo; tire do fim com `pop(-1)` numa lógica inversa, ou use `heapq.merge` (aula 12, 0:02:12 a 0:03:34).

#### Como comparar um elemento com o anterior sem índice?

Com `zip` (aula 11, 0:02:13 a 0:02:30); e construa uma lista nova em vez de remover da existente (aula 11, 0:01:27 a 0:01:49).

#### Como organizar um programa como o wordcount?

Liste as tarefas, uma função para cada, e componha; os dois modos só diferem na ordenação e no limite (aula 13, 0:05:30 a 0:06:47). Faça por partes, vendo cada etapa (aula 13, 0:03:08 a 0:03:23).

## 12. Repositórios e recursos

| Recurso | Onde encontrar | Observação |
|---|---|---|
| Playlist completa (fonte desta documentação) | [Pacote de Desafios Pythônicos](https://www.youtube.com/playlist?list=PLeKXYyZCJHxetT2NwFzKcslYfiE3yPUWL) | 15 vídeos. Os ids estão em `playlist.json` e nos links da seção 5. |
| Canal | [HB Network](https://www.youtube.com/@hbnetworkoficial) | |
| `henriquebastos/pacote-desafios-pythonicos` | GitHub, commit `ae90952cdaa7690a31e62f4715f0bd60600213b3` | O kit dos exercícios, mostrado na aula 0 (0:01:05 a 0:01:22). Descrito em `kb/repos/pacote-desafios-pythonicos.md`, que registra que os exercícios correspondem aos básicos do Google's Python Class traduzidos, sem atribuição nem licença no commit. Ele não fala da origem dos exercícios nas legendas. |
| PyCharm Community | citado, link na descrição do vídeo | Editor recomendado (aula 0, 0:02:00 a 0:02:11). |
| Refatoração na Prática | `kb/courses/refatoracao-na-pratica.md` | Comparação deste documento: refatora o donuts (aulas 6 a 16) e um wordcount legado (aulas 18 a 25 daquele curso). |

Repositórios do curso: **um**, o kit. Não há repositório de soluções.

## 13. Análise linha a linha do código real

O código publicado é o kit, não soluções. Trechos curtos, porque o repositório não tem licença; caminhos no commit `ae90952`.

- **O esqueleto.** Cada arquivo de 01 a 12 tem o enunciado no docstring, a função com `# +++ SUA SOLUÇÃO +++` e `return` (`01_donuts.py:12-14`), e abaixo do marcador de código auxiliar (`:17`) o verificador e os casos. É o que ele roda na aula 0 (0:03:01 a 0:03:49).
- **O verificador.** `out = f(in_)`, compara com `expected` e imprime `✅` ou `❌` com `f'e o correto é {expected!r}'` (`01_donuts.py:24-33`). A frase que ele lê na aula 0, donuts com 4 retornou None e o correto é Number of donuts 4 (0:03:35 a 0:03:46), é essa linha. O verificador informa e não falha: o processo sai com 0 mesmo com todos os casos errados (seção 14).
- **Dois argumentos.** Em `04_mix_up.py`, `07_front_back.py` e `12_linear_merge.py` o caso é uma tupla e o verificador faz `out = f(*in_)` (`04_mix_up.py:27`). A linha 45 que ele indica para o caso novo (aula 4, 0:02:32 a 0:02:36) vem logo depois da última chamada, `04_mix_up.py:44`.
- **Os casos de limite.** Os quatro do donuts, 4, 9, 10 e 99 (`01_donuts.py:38-41`), são os que ele lê como limites (aula 1, 0:00:53 a 0:01:06); a lista vazia do remove_adjacent (`11_remove_adjacent.py:39`) é o caso limite da aula 11 (0:00:38 a 0:00:45); o quarto caso, `[2, 2, 3, 3, 3, 2, 2]` dando `[2, 3, 2]` (`:40`), é o que mostra adjacentes contra únicos (0:00:48 a 0:01:03).
- **A main do wordcount.** Valida `len(sys.argv) != 3`, imprime o uso e sai com `sys.exit(1)`, e despacha `--count` para `print_words(filename)` e `--topcount` para `print_top(filename)` (`13_wordcount.py:63-76`). A provocação da aula 13 (0:07:00 a 0:07:18) é sobre esses dois nomes.
- **Divergência no enunciado do wordcount**, observação deste documento: o texto pede ordem crescente de ocorrências (`13_wordcount.py:30`), mas o exemplo é decrescente, `b 4`, `c 3`, `a 2` (`:35-37`). Ele lê as duas coisas sem notar a diferença (aula 13, 0:01:41 a 0:01:59).
- **O mimic.** `mimic_dict(filename)` e `print_mimic(mimic_dict, word)` com `return` vazio, e a `main` que faz `dict = mimic_dict(sys.argv[1])` e `print_mimic(dict, '')` (`14_mimic.py:46-66`). O arquivo é indentado com dois espaços, e o nome `dict` esconde o builtin (observações de `kb/repos/pacote-desafios-pythonicos.md`, não dele).
- **O parâmetro `s`.** Quatro esqueletos nomeiam o parâmetro `s` (`02_both_ends.py:10`, `03_fix_start.py:16`, `05_verbing.py:13`, `06_not_bad.py:12`), que é o nome que ele pede para evitar nas variáveis (aula 5, 0:01:32). Observação deste documento.
- **Leituras da legenda corrigidas por este documento:** Pythônicos [Pai tônicos] (aula 0, 0:00:00), PyCharm [phy charme, pai charme] e Community [com minion] (aula 0, 0:02:00 a 0:02:07), return [retâneo] (aula 1, 0:01:50), while [Will] (aula 2, 0:01:09), aardvark [arde varcing] e donut [Dantes] (aula 3, 0:00:43 a 0:01:00), join [John, Joe, joia] (aula 4, 0:01:41 e 0:01:58; aula 7, 0:03:13), verbing [Furby] (aula 5, 0:00:00), list comprehension [Lis compro rations, lixo compro ranchos] (aula 8, 0:02:04; aula 9, 0:02:32), key [que] e itemgetter [getsiten] (aula 10, 0:01:00 e 0:02:30), heapq [rip] e merge [nerd] (aula 12, 0:03:24 a 0:03:28), context manager [contact Manager] (aula 13, 0:05:16), print_top [print Stop] (aula 13, 0:02:35; 0:07:13), defaultdict [the foldick] e Counter [Country] (aula 14, 0:04:19 a 0:04:24), small.txt [mal potxt] e alice.txt [ls.xt] (aula 14, 0:02:29 a 0:02:36).
- **Leituras incertas:** a rotina chamada [Seal] para o meio da string (aula 7, 0:02:19), lida como `math.ceil`, embora ele diga só a biblioteca padrão; a função do Python que fecha o generator da aula 8 (0:02:35), lida como `sum`; o segundo e o terceiro casos do not_bad saem truncados na legenda (aula 6, 0:00:46 a 0:00:59) e foram conferidos contra `06_not_bad.py:38-41`.

## 14. Execução real dos testes

O kit roda. Execução desta documentação em 2026-11-15, Python 3.9.6, com os arquivos do commit `ae90952` sem alteração:

- `01_donuts.py` a `12_linear_merge.py`: cada arquivo imprime uma linha `❌` por caso, todas com `retornou None`, e sai com código 0. São 42 casos ao todo: quatro em 01, 02, 03, 04, 06 e 11; três em 05, 07, 08, 09, 10 e 12. A primeira linha de `01_donuts.py` é `❌ donuts(4) retornou None e o correto é 'Number of donuts: 4'`, a mesma que ele lê na aula 0 (0:03:35 a 0:03:46).
- `13_wordcount.py` sem argumentos: imprime `Utilização: ./13_wordcount.py {--count | --topcount} file` e sai com 1, como ele mostra (aula 13, 0:03:55 a 0:04:20). Com `--count letras.txt`: `NameError: name 'print_words' is not defined`, saída 1; com `--topcount letras.txt`: `NameError` de `print_top` (aula 13, 0:04:22 a 0:04:39). Com uma opção desconhecida: `unknown option: --foo`, saída 1.
- `14_mimic.py` sem argumentos: imprime `Utilização: ./14_mimic.py file-to-read` e sai com 1. Com `small.txt`: não imprime nada e sai com 0, o que ele descreve como não faz nada mas também não dá erro (aula 14, 0:02:29 a 0:02:36).
- As três ilustrações da seção 5 (`sort_last`, `remove_adjacent`, `linear_merge`) foram rodadas contra os casos dos arquivos, como asserções, fora do repositório: 10 de 10 passam. São deste documento, não dele.

---

Documentação elaborada a partir das transcrições das 15 aulas da playlist Pacote de Desafios Pythônicos, de Henrique Bastos (HB Network), playlist `PLeKXYyZCJHxetT2NwFzKcslYfiE3yPUWL`, legendas automáticas em português (pt-orig) capturadas em 2026-11-15. As citações são paráfrases das transcrições, não verificadas contra o vídeo (`verified: false`), renderizadas sem aspas e com os erros de reconhecimento anotados entre colchetes quando precisam aparecer. Não há fala de participante; nenhuma pessoa além dele é nomeada. O código publicado é o kit de exercícios (`henriquebastos/pacote-desafios-pythonicos`, commit `ae90952`), sem licença, citado em trechos curtos; o curso não publica soluções, e as três soluções da seção 5 são ilustrações deste documento. Datas de publicação e visualizações não foram coletadas. Conteúdo de caráter educativo.
