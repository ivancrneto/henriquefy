<!-- written by the henrique-ingest distiller on 2026-11-11 from sources/transcripts/refatoracao-poo-legado/; see kb/courses/README.md for provenance and license -->

HB Network · Documentação de curso

# Refatoração com POO em código legado

As 9 aulas da playlist, lidas aula a aula a partir das legendas automáticas. É uma única sessão ao vivo, com turma no Zoom e chat aberto, recortada em nove vídeos. Ele pega um jogo da cobrinha em pygame escrito por um membro da comunidade como tutorial, faz um fork e começa a transformá-lo no ponto de partida de um jogo multiplayer com power ups. Primeiro lê o código rodando-o e investigando a API do pygame (aulas 1 e 2), depois separa a camada do pygame da lógica do jogo (aulas 3 e 4), então cria sob teste uma classe Snake que o código antigo continua usando (aulas 5 e 6), introduz um valor Point para esconder a aritmética de coordenadas (aulas 7 e 8) e fecha trocando a representação interna por um deque e corrigindo a regra que deixava a cobra voltar sobre si mesma (aula 9).

Instrutor: **Henrique Bastos** · Canal [HB Network](https://www.youtube.com/@hbnetworkoficial) · Playlist: [Refatoração com POO em código legado](https://www.youtube.com/playlist?list=PLeKXYyZCJHxeEeta6ddgqUagLp_Oo_kAx) · Repositório: nenhum publicado para esta série (o fork não tem URL nas transcrições)

Documento elaborado a partir das transcrições das 9 aulas (legenda automática em português, pt-orig, capturada em 2026-11-11). As aulas são recortes de uma transmissão ao vivo com turma no Zoom e chat, e a legenda não marca quem fala. Trechos de fala de participantes identificados pela mudança de interlocutor no texto: aula 3, 0:07:15 a 0:07:36 (um participante explica o Rect do pygame); aula 4, 0:02:53 a 0:03:00 (observação de que a cobra nem sempre está comendo) e 0:03:53 a 0:04:02 (pergunta sobre extrair a configuração do pygame); aula 5, 0:02:55 a 0:03:02 e 0:14:30 a 0:14:58 (diálogo sobre manter a lista e sobre direção relativa); aula 7, 0:03:01 a 0:06:10 (um participante sugere namedtuple e manda um link da documentação); aula 8, 0:02:34 a 0:02:42 (correção de índice); aula 9, 0:02:38 a 0:02:55 (pergunta sobre o atributo da cobra). Esses trechos não são atribuídos a ele em nenhuma seção. O código refatorado é de terceiro, um tutorial publicado num fórum da comunidade; não é reproduzido, nem na forma original nem em trechos, e o autor não é nomeado. Os participantes também não são nomeados.

## 1. Visão geral do curso

Refatoração com POO em código legado é uma série de **9 vídeos** que somam **5.417 segundos, 1 hora, 30 minutos e 17 segundos**. O objetivo declarado da sessão é pegar o jogo da cobrinha e fazer dele uma cobrinha com esteroides: multiplayer online, com power ups e com o objetivo de eliminar os outros jogadores (aula 1, 0:00:58 a 0:02:12). O caminho tem quatro blocos: entender o código lendo-o junto com a documentação do pygame (aulas 1 e 2); separar a camada do pygame da lógica do jogo em funções, ainda sem teste (aulas 3 e 4); criar a classe Snake por testes, de modo que o algoritmo original continue funcionando enquanto a lógica migra para dentro dela (aulas 5 e 6); e simplificar com um valor Point e um deque, já protegido pelos testes (aulas 7 a 9). O saldo, dito no fecho, é isolar a lógica do jogo da estrutura de exibição e atualização para poder construir o multiplayer (aula 9, 0:09:50 a 0:10:10).

| Dimensão | Valor | Observação |
|---|---|---|
| Aulas | 9 | Playlist completa, numerada de #01 a #09. |
| Duração total | 5.417 s (1h 30min 17s) | Soma das durações em `playlist.json`. |
| Aula mais curta / mais longa | 448 s (#6) / 1.050 s (#5) | A #6, Como implantar um código novo em um sistema legado, tem 7:28; a #5 tem 17:30. |
| Datas de publicação | não coletadas | O `playlist.json` desta coleta traz id, título e duração. |
| Visualizações | não coletadas | Idem. |
| Transcrições | 9 de 9 disponíveis | Todas em legenda automática (pt-orig). Não há legenda humana nem transcrição Whisper. |
| Títulos em inglês | aulas #5 e #7 | Constam no `playlist.json` como How to use automated tests to break down working code e Creating new features for a legacy project safely, provavelmente títulos traduzidos automaticamente pelo YouTube. O `playlist.json` não traz o título original em português, então ficam como listados. A fala é em português. |
| Legenda ruidosa | nomes de código | PyCharm sai como pai charms e pai Charme, pygame como pai game, slither como slider e sleezer, head como Red e Redi, tail como Taylor e Tale, deque como Deck, turn como Turner e turnê. Os trechos conceituais são legíveis. |
| Código do curso | nenhum publicado | O jogo é de terceiro e não é reproduzido. O código que ele escreve ao vivo (testes, classe Snake, Point) aparece na seção 5 como reconstrução a partir da fala, não publicada. |

Nota de método: cada afirmação traz aula e timestamp. As citações são paráfrases de legenda, sem aspas, não verificadas contra o vídeo. Mis-hearings ficam entre colchetes. As seções 13 e 14 dizem que não há código publicado a analisar nem suíte a rodar.

## 2. Filosofia e método de ensino

### 2.1 Uma sessão ao vivo, em clima de conversa

Ele abre dizendo que gosta do esquema de interação, de estar junto trocando ideia (aula 1, 0:00:52 a 0:00:58), e a sessão inteira é conduzida assim: lê o chat, aceita sugestões e dá crédito a quem sugeriu (aula 7, 0:06:40 a 0:06:44), pede que corrijam se estiver errado (aula 2, 0:06:59). Admite não conhecer o pygame: está conhecendo agora e sabe tanto quanto quem assiste (aula 1, 0:09:10 a 0:09:17). O método de leitura nasce disso: abrir a documentação de cada chamada do pygame no meio da leitura (aula 1, 0:04:57 a 0:05:33; aula 2, 0:01:22 a 0:02:21).

### 2.2 O alvo dirige a crítica, não o autor

Antes de começar a mudar, ele marca a virada: daqui em diante nada do que vai dizer é sobre o código do autor, é sobre o objetivo deles, e o tutorial faz total sentido para o que se propunha (aula 3, 0:01:01 a 0:01:25). O critério de cada mudança é o multiplayer: as coisas precisam ficar mais separadas, não dá para ser um arquivão só, tudo solto (aula 3, 0:01:11 a 0:01:21). O fecho repete a gentileza com o tutorial e a meta (aula 9, 0:09:18 a 0:10:10).

### 2.3 Não matar o paciente

A imagem que ele usa para o exercício é extrair comportamento para criar o espaço de levar o código para onde se quer, sem matar o paciente (aula 6, 0:06:15 a 0:06:28). Por isso ele não reescreve: se mudasse a lógica toda, jogaria fora o código do autor e o jogo ficaria sem funcionar (aula 5, 0:06:43 a 0:06:51). O preço que aceita pagar é criar uma nova interface, a classe, por testes, e mover para dentro dela a lógica que é da cobra, mantendo a interface com o jogo de fora (aula 5, 0:06:51 a 0:07:13). Quando o jogo volta a rodar com a classe nova, ele comemora ter refatorado sem matar o software (aula 6, 0:06:09 a 0:06:13).

### 2.4 Uma coisa de cada vez

Ele recusa melhorias que estão no caminho mas não são o passo atual. Quando alguém sugere usar as constantes de direção já existentes, responde que poderia, mas que agora só quer esvaziar o código para separar a camada do pygame da lógica do jogo (aula 4, 0:02:10 a 0:02:22). Quando a conversa vai para direção relativa, pede calma, uma coisa de cada vez, já é uma mudança (aula 5, 0:14:43 a 0:14:48). Vê a falta de uma classe de ponto na aula 6, mas primeiro quer o jogo funcionando (aula 6, 0:02:09 a 0:02:21). Vê o custo de mover a cobra inteira na aula 2 (0:10:20 a 0:10:47) e só troca a estrutura na aula 9, depois dos testes.

### 2.5 Relação com os outros cursos de refatoração

Comparação deste documento, não fala dele: em Domine o Método da Refatoração Rápida (`kb/courses/refatoracao-rapida.md`), ele proíbe orientação a objeto e recusa um tipo Coordenada porque é dia de fluxo, não de estrutura (aula 8 daquele curso, 0:08:07). Aqui o título já anuncia POO e ele introduz uma classe Snake e um valor Point. A ordem, porém, é a mesma: separar a lógica em funções primeiro (aulas 3 e 4), reconhecer a classe a partir das funções que manipulam a mesma lista (aula 4, 0:06:51 a 0:07:15), e só então criá-la, por teste.

## 3. Pilares conceituais

### 3.1 Separar o motor da lógica do jogo

O drama principal do código, para ele, é que as coisas do pygame e a lógica do jogo estão misturadas, e a primeira coisa que gosta de tentar é separá-las (aula 3, 0:03:13 a 0:03:34). Ele esvazia o laço principal extraindo funções (aula 4, 0:00:12 a 0:02:00) até poder apontar: isto é a lógica do jogo, todo o resto é do pygame (aula 4, 0:02:39 a 0:02:45). A lógica do jogo pede uma abstração do tabuleiro que não tem nada a ver com o pygame e poderia ser um jogo de console (aula 4, 0:03:28 a 0:03:48), e o setup do pygame é o motor, que poderia ser uma classe com um loop (aula 4, 0:04:06 a 0:04:22). O commit dessa etapa diz novo layout de arquivos e camadas separadas (aula 4, 0:05:55 a 0:06:04).

### 3.2 Separar para poder mexer isolado

O que fizeram até ali não mudou muito o código; o objetivo é que, para mexer no código, é preciso separá-lo, para mexer de forma isolada (aula 4, 0:04:25 a 0:04:37). A separação, nessa fase, é feita sem teste, e ele diz isso (aula 3, 0:09:10 a 0:09:13); a verificação é rodar o jogo depois de cada movimento grande (aula 4, 0:04:37 a 0:04:45), e é rodando que aparece o bug da variável global que virou local (aula 4, 0:04:51 a 0:05:10).

### 3.3 A classe aparece no código que manipula a mesma coisa

Ele não começa pela classe. Depois de extrair as funções, vê que há manipulação de lista para mudar a posição da cobra, que mudar de direção deveria ser só o método turn, que se movimentar deveria ser só o slither e que comer deveria ser o eat; então fica claro que tem que ter uma classe Snake com esses métodos, cuja representação interna ainda não se sabe (aula 4, 0:06:51 a 0:07:15). A pergunta de modelagem que ele faz é concreta: a cobra tem direção, ou se move numa direção recebida por parâmetro? Tem direção, porque a direção teria de ser guardada em algum lugar (aula 5, 0:13:24 a 0:13:37).

### 3.4 Teste como andaime da interface nova

A classe nasce por teste, e o teste diz o que o código antigo precisa dela: um corpo inicial (aula 5, 0:00:47 a 0:01:23), acesso por índice porque o algoritmo original acessa a cobra por índice (aula 5, 0:04:24 a 0:05:20), atribuição por índice como camada temporária que ele não quer expor (aula 5, 0:06:07 a 0:06:40). Escrever o teste do slither revela que o turn original não move a cobra, só muda a direção (aula 5, 0:08:31 a 0:08:43). Com a classe pronta, o jogo passa a usá-la (aula 6, 0:02:27 a 0:03:30), e daí em diante as mudanças internas são feitas com os testes rodando, inclusive as que quebram só o teste e não o jogo (aula 9, 0:01:24 a 0:01:34).

### 3.5 Um valor para a aritmética escondida

O que o irrita profundamente é pegar o índice zero como x e o um como y: falta uma classe de ponto para ocultar essa matemática (aula 6, 0:02:04 a 0:02:18). O Point precisa de x e y, somar dois pontos e comparar dois pontos (aula 7, 0:00:34 a 0:00:40), e multiplicar por um escalar para converter grade em pixel (aula 7, 0:01:16 a 0:01:25). Com ele, as direções viram pontos que se somam à cabeça (aula 7, 0:07:20 a 0:07:24), a conversão vezes 10 vira uma operação só (aula 8, 0:05:38 a 0:06:20), e virar para trás se detecta porque duas direções opostas somam zero (aula 9, 0:06:16 a 0:06:44).

### 3.6 Encapsulado, o deselegante pode esperar

Trocar a lista por um deque mexe só no interno, e os testes devem continuar passando (aula 9, 0:00:08 a 0:00:12). Quando alguém acha deselegante o acesso por índice que trata a cabeça como caso especial, ele responde que o problema está dentro da classe, encapsulado, e que só se estivesse vazando faria sentido torná-lo mais elegante agora (aula 9, 0:02:58 a 0:03:10). Mesmo assim simplifica no fim, deixando o zero como único caso especial (aula 9, 0:08:14 a 0:08:33).

## 4. As aulas em uma tabela

| # | Título | Duração | Foco em uma linha |
|---|---|---|---|
| 1 | #01 - A postura correta para encarar um código legado | 10:04 | A meta multiplayer (0:01:07); roda o jogo e lê o código com a documentação do pygame aberta (0:04:04). |
| 2 | #02 - Como investigar um código legado | 11:11 | Grade de 64 por 48 (0:00:12); o tick que trava o loop (0:02:24); mover a cobra em O(1) em vez de O(n) (0:10:20). |
| 3 | #03 - Como delimitar as fronteiras de um sistema legado | 9:37 | A crítica é sobre o objetivo, não o autor (0:01:03); pacote com `__main__`; pygame misturado com a lógica (0:03:13). |
| 4 | #04 - Desatando os nós do sistema legado | 7:41 | Funções eat, slither, turn; isto é lógica, o resto é pygame (0:02:39); separar para mexer isolado (0:04:25). |
| 5 | #05 - How to use automated tests to break down working code (título como listado) | 17:30 | Classe Snake por testes, com `__getitem__` e `__setitem__` temporários (0:06:32); direção como vetor (0:11:21). |
| 6 | #06 - Como implantar um código novo em um sistema legado | 7:28 | O jogo passa a usar a Snake; refatorar sem matar o paciente (0:06:15). |
| 7 | #07 - Creating new features for a legacy project safely (título como listado) | 8:29 | Point por testes: soma, igualdade, escalar (0:00:34); namedtuple e `__slots__` (0:06:15). |
| 8 | #08 - Como ampliar a capacidade do projeto legado sem quebrar nada | 7:44 | Cabeça separada do corpo; gambiarra temporária no índice (0:02:29); Point simplifica a conversão (0:06:03). |
| 9 | #09 - Como reduzir o débito técnico para garantir a saúde do seu projeto | 10:33 | Deque (0:00:15); a cobra não volta mais (0:06:31); retorno como aborto e código para quem lê (0:07:27). |

## 5. Resumo por aula

### Aula 1: #01 - A postura correta para encarar um código legado
Vídeo: https://www.youtube.com/watch?v=YvbREfT1YeI · Duração: 10:04

Resumo: abertura da live. Ele conta que um membro de um fórum da comunidade [legenda: fórum de Jungle] escreveu um tutorial com pygame ensinando a construir o jogo da cobrinha, e que quer pegar esse código para fazer uma cobrinha com esteroides: multiplayer, para jogar online durante o Zoom, com power ups (pimenta que acelera, porco espinho que dispara um míssil pela boca) e com o objetivo de matar os outros, crescendo com as frutas para cercá-los (0:00:15 a 0:02:17). Discute o incentivo do jogo, comer para não deixar o outro crescer e ganhar quem tiver o maior tamanho (0:02:31 a 0:03:20). Não vai começar do zero: faz um fork e clona o projeto num ambiente Python 3.8 já criado, abre no PyCharm [legenda: pai charms] e roda o jogo antes de ler (0:02:21 a 0:04:44). Na leitura, declara que detesta o import com asterisco, embora entenda por que o autor o usa (0:04:50 a 0:04:55), e vai abrindo a documentação de cada chamada do pygame: init, set_mode e seus flags, set_caption, Surface (0:04:57 a 0:07:41). Investiga no console o cálculo da posição aleatória e descobre que o jogo arredonda para múltiplos de 10, ou seja, a janela de 640 por 480 é uma grade de 64 por 48 (0:08:27 a 0:09:06). Admite que está conhecendo o pygame agora (0:09:10 a 0:09:17) e fecha dizendo que sente um cheirinho esquisito nesse código (0:09:37 a 0:09:41).

Linha do tempo:
- [0:00:00] vamos fazer o jogo do Snake hoje
- [0:00:15] o tutorial de pygame de um membro da comunidade
- [0:00:52] gosta da interação, de estar junto trocando ideia
- [0:01:07] a meta: cobrinha com esteroides, multiplayer online
- [0:01:17] power ups: pimenta, porco espinho com míssil
- [0:02:00] o objetivo do jogo é matar todo mundo
- [0:02:21] não vai começar do zero: fork do projeto
- [0:04:04] roda o jogo antes de ler
- [0:04:50] detesta o import com asterisco
- [0:04:57] lê o código com a documentação do pygame aberta
- [0:08:36] investiga a posição aleatória no console: grade de 64 por 48
- [0:09:37] um cheirinho esquisito no código

Princípios:
- Não começar do zero: partir do código que existe, com fork (0:02:21 a 0:02:27).
- Rodar o programa antes de ler o fonte (0:04:02 a 0:04:44).
- Ler o código legado com a documentação da biblioteca aberta, chamada por chamada, quando não se conhece a biblioteca (0:04:57 a 0:05:33; 0:09:10 a 0:09:17).
- Investigar no console o que uma expressão faz em vez de supor (0:08:34 a 0:09:01).

Código: nenhum escrito por ele. O código lido é o tutorial de terceiro e não é reproduzido.

Citações (paráfrases de legenda, não verificadas):
- [0:01:01] pegar esse código do [autor do tutorial] e fazer um joguinho né cobrinha com esteróides
- [0:02:21] não vão começar do zero né porque eu vou copiar fazer um forte desse projeto [provável: fork]
- [0:09:12] Tô conhecendo o pai game agora então eu sei tanto quanto você [pai game: pygame]
- [0:09:37] tá Sentindo cheirinho tem um cheirinho esquisito desse código aqui

### Aula 2: #02 - Como investigar um código legado
Vídeo: https://www.youtube.com/watch?v=zi-TEhaxWk8 · Duração: 11:11

Resumo: continua a leitura. O jogo está mapeado pixel a pixel, mas na verdade só tem 64 por 48 pontos e o resto é resolução; é algo que dá para melhorar para evitar o cálculo todo (0:00:05 a 0:00:28). Lê a colisão como comparação de par ordenado (0:00:31 a 0:00:51), a criação da maçã e o relógio do pygame, abrindo a documentação do Clock (0:01:19 a 0:02:21). Sobre o tick que espera o tempo do próximo quadro, diz que é bom e é ruim: simplifica muito, mas perde-se o controle durante o período em que nada é feito, tempo em que se poderia calcular a inteligência artificial ou a rede, coisa para ver mais à frente (0:02:21 a 0:02:52). Explica a fila de eventos consumida a cada ciclo do laço (0:03:00 a 0:03:51), corrige um import que faltava (0:04:00 a 0:04:15) e nota que o jogo deixa a cobra voltar sobre si mesma, coisa para olhar depois (0:04:48 a 0:05:18). Lê o movimento do corpo de trás para frente e reconhece que lógica reversa é complicada de seguir (0:06:03 a 0:06:19). Para entender o valor provisório que o código acrescenta ao comer, monta uma planilha e pinta células como tabuleiro (0:07:15 a 0:08:49). Fecha com a observação de custo: mover a cobra atualizando cada parte é O(n) no comprimento; bastaria tirar o último e acrescentar um na frente, duas operações sempre, sem mexer nos outros, coisa para investigar depois (0:09:04 a 0:10:47).

Linha do tempo:
- [0:00:05] o jogo tem só 64 por 48 pontos; o resto é resolução
- [0:00:31] a colisão como par ordenado
- [0:01:19] o Clock do pygame e a documentação
- [0:02:21] o tick é bom e é ruim: simplifica, mas trava o loop
- [0:03:00] a fila de eventos consumida a cada ciclo
- [0:04:48] a cobra consegue voltar sobre si mesma: anotar para depois
- [0:06:16] lógica reversa é complicada para o cérebro
- [0:07:15] monta um tabuleiro numa planilha para entender o movimento
- [0:09:00] uma pergunta do chat sobre lista encadeada
- [0:10:20] mover a cobra com duas operações em vez de n

Princípios:
- Toda simplificação tem preço; o tick simplifica o laço mas tira o controle do tempo ocioso (0:02:24 a 0:02:52).
- Desenhar o estado num meio externo (planilha, tabuleiro) para entender um algoritmo difícil de seguir (0:07:15 a 0:07:25; 0:09:56 a 0:10:01).
- Anotar o problema percebido e seguir a leitura, em vez de consertar na hora (0:02:50 a 0:02:52; 0:05:16 a 0:05:18; 0:10:45 a 0:10:47).

Código: nenhum escrito por ele. A planilha é só um desenho do estado.

Citações (paráfrases de legenda, não verificadas):
- [0:02:24] isso é bom mas é ruim é bom porque simplifica para caceta
- [0:02:37] o ruim é que eu perco o controle né por aquele período de tempo em que ele não tá fazendo nada
- [0:06:16] lógica reversa é complicado o fruto do cérebro
- [0:10:34] em vez de fazer o de n que seria o comprimento [provável: O(n)]

### Aula 3: #03 - Como delimitar as fronteiras de um sistema legado
Vídeo: https://www.youtube.com/watch?v=NW9VlojTl6k · Duração: 9:37

Resumo: termina a leitura do desenho na tela e descobre na documentação que o fill aceita um retângulo (0:00:08 a 0:00:49). Então muda de registro: nada do que vai dizer daqui em diante é sobre o código do autor, é sobre o objetivo, um jogo multiplayer, e para isso as coisas têm que ficar separadas, não dá para ser um arquivão só (0:01:01 a 0:01:25). Afirma que não tem jeito, tem que fazer teste, que teste para ele importa, e começa preparando o projeto: grava o pygame 2.0 num arquivo de requisitos, cria o pacote snake, move o arquivo do tutorial para o `__main__.py` do pacote para rodar com python -m snake e cria um pacote de testes (0:01:28 a 0:03:07). Nomeia o drama principal: há coisas do pygame e lógica do jogo misturadas, e a primeira coisa que gosta de tentar é separá-las (0:03:13 a 0:03:34). Envolve tudo numa função main (0:03:37 a 0:03:50), roda, e começa a reduzir a parte de desenho trocando a cópia de Surface por um fill com retângulo; um participante explica que o Rect já define o tamanho (0:04:35 a 0:07:36). Usa desempacotamento de tupla para montar o retângulo, o que dispensa as Surfaces (0:08:04 a 0:08:58). Registra que tudo isso é sem teste, só agrupando para separar (0:09:04 a 0:09:13).

Linha do tempo:
- [0:00:41] o fill aceita um retângulo
- [0:01:01] a crítica daqui em diante é sobre o objetivo, não sobre o autor
- [0:01:11] multiplayer exige separar: não dá para ser um arquivão
- [0:01:28] tem que fazer teste
- [0:01:45] arquivo de requisitos com o pygame 2.0
- [0:02:19] pacote snake com `__main__`; python -m snake
- [0:03:04] pacote de testes
- [0:03:13] o drama: pygame e lógica do jogo misturados
- [0:03:37] envolve o código numa função main
- [0:04:41] troca a cópia de Surface por fill com retângulo
- [0:08:04] desempacotamento de tupla dispensa as Surfaces
- [0:09:10] isso é sem teste, só agrupando

Princípios:
- Criticar pelo objetivo, não pelo autor: o código servia ao propósito do tutorial; a mudança vem do novo objetivo (0:01:03 a 0:01:25).
- Teste é condição para mudar de verdade (0:01:28 a 0:01:38).
- Primeiro movimento num legado misturado: separar a biblioteca de infraestrutura da lógica do domínio (0:03:13 a 0:03:34).
- Ser explícito quando um passo é dado sem rede de teste (0:09:10 a 0:09:13).

Código: reconstrução a partir da fala; não publicada. Só a estrutura de projeto que ele monta, não o conteúdo do jogo.

```text
# reconstrução a partir da fala, não publicada
requirements-dev.txt     # pygame==2.0 (versão dita como 2.0; nome do arquivo de leitura incerta, 0:01:45)
snake/
    __init__.py
    __main__.py          # o arquivo do tutorial movido para cá; roda com python -m snake
tests/
    __init__.py
```

Citações (paráfrases de legenda, não verificadas):
- [0:01:03] agora nada que eu vou falar é sobre o código do [autor do tutorial] é com foco no nosso objetivo
- [0:01:28] cara não tem jeito tem que fazer teste tem que fazer teste
- [0:03:25] a primeira coisa que eu gosto de tentar fazer é dar tentar na separada nisso aí
- [0:09:10] isso é sem teste né estamos só mexendo na parada aqui

### Aula 4: #04 - Desatando os nós do sistema legado
Vídeo: https://www.youtube.com/watch?v=UvmZBBafELY · Duração: 7:41

Resumo: ele extrai do laço principal as funções da lógica do jogo, aceitando uma global temporária para poder extrair (0:00:00 a 0:00:15). Nomeia cada bloco pelo que faz: comer, quando há colisão com a maçã (0:00:30 a 0:01:03); rastejar, para o movimento do corpo [legenda: slider, sleezer; provável: slither] (0:01:06 a 0:01:51); e o ajuste da direção (0:01:55 a 0:02:10). A uma sugestão de usar as constantes de direção já existentes, responde que poderia, mas que agora só quer esvaziar o código para separar a camada do pygame da lógica do jogo (0:02:10 a 0:02:22). Aponta o resultado: isto é a lógica do jogo, todo o resto é do pygame (0:02:39 a 0:02:45). Vê que a cobra sofre uns efeitos, a maçã outros, e que falta uma abstração do tabuleiro que não tem nada a ver com o pygame e poderia ser um jogo de console (0:03:17 a 0:03:48); o setup do pygame é o motor, que poderia ser uma classe com um loop (0:04:06 a 0:04:22). Resume: para mexer no código é preciso separá-lo, para mexer de forma isolada (0:04:25 a 0:04:37). Roda o jogo e encontra um bug que ele mesmo introduziu, a posição da maçã virou variável local, e corrige com global (0:04:37 a 0:05:10). Faz o commit novo layout de arquivos e camadas separadas (0:05:12 a 0:06:04). Fecha propondo tratar o quadrado como um ponto, com uma escala (0:06:24 a 0:06:35), e concluindo que tem que haver uma classe Snake com os métodos turn, slither e eat, de representação interna ainda desconhecida (0:06:51 a 0:07:15).

Linha do tempo:
- [0:00:06] uma global temporária para poder extrair
- [0:00:30] a função de comer
- [0:01:06] a função de rastejar [legenda: slider]
- [0:02:14] não usar as constantes agora: só esvaziar para separar as camadas
- [0:02:39] isto é a lógica do jogo, o resto é do pygame
- [0:03:28] falta a abstração do tabuleiro, que podia ser de console
- [0:04:06] o setup do pygame é o motor
- [0:04:25] separar para mexer de forma isolada
- [0:04:37] roda o jogo e encontra o bug da variável local
- [0:05:12] commit: novo layout de arquivos e camadas separadas
- [0:06:24] tratar o quadrado como ponto, com escala
- [0:06:51] tem que ter uma classe Snake com turn, slither e eat

Princípios:
- Separar para poder mexer de forma isolada (0:04:25 a 0:04:37).
- Um objetivo por passo: recusar a melhoria vizinha enquanto o passo atual não termina (0:02:14 a 0:02:22).
- A lógica do domínio não depende do motor: o tabuleiro podia ser de console (0:03:28 a 0:03:48).
- Rodar depois de mexer muito, para ver se continua funcionando (0:04:37 a 0:04:45).
- Comportamento que manipula o mesmo dado aponta a classe: turn, slither e eat são métodos da cobra (0:06:51 a 0:07:15).

Código: nenhum reconstruído; as funções extraídas carregam o algoritmo do tutorial, que não é reproduzido. Os nomes dados por ele são, em leitura provável, eat, slither e turn.

Citações (paráfrases de legenda, não verificadas):
- [0:02:17] eu quero só esvaziar o código para separar a camada do pai game da lógica do jogo [pai game: pygame]
- [0:02:39] isso aqui é a lógica do jogo todo esse resto aqui é do Pai game
- [0:04:31] para a gente poder mexer no código ele precisa separar ele separar para poder mexer de forma isolada
- [0:07:08] tá bem claro para mim que tem que ter um objeto uma classe cobra a classe Snake

### Aula 5: #05 - How to use automated tests to break down working code
Vídeo: https://www.youtube.com/watch?v=qgjnVwD7FaU · Duração: 17:30 · Título como listado no `playlist.json` (provável tradução automática; o original em português não consta na coleta)

Resumo: cria o arquivo de teste da cobra e o primeiro teste: uma cobra criada na posição zero zero com tamanho 3 tem um corpo que é a sequência de três pontos a partir da cabeça (0:00:02 a 0:01:23). Prototipa o range no console antes de escrever (0:02:21 a 0:03:28) e decide manter a lista como o autor fez, para manter a lógica original (0:03:02 a 0:03:09). Como o algoritmo original acessa a cobra por índice, escreve um teste de acesso por índice e implementa `__getitem__` (0:04:24 a 0:05:39), e depois `__setitem__` (0:06:07 a 0:06:17). Explica que a atribuição por índice é temporária e que não quer expô-la: quer que o algoritmo do autor funcione com essa classe, porque senão jogaria o código fora, mudaria a lógica toda e o jogo pararia de funcionar (0:06:32 a 0:06:51). O preço que paga é criar uma interface nova, a classe, através de testes, para mover para dentro dela a lógica que é da cobra; mantida a interface com o jogo de fora, não há problema (0:06:51 a 0:07:13). Ao escrever o teste do slither descobre que ele depende da direção e que o turn original não move a cobra, só muda a direção (0:07:15 a 0:08:43). Conclui que a cobra tem direção (0:10:01 a 0:10:27) e lê o mapa de direções do jogo como vetores: cima é zero menos um, baixo zero um, direita um zero, esquerda menos um zero (0:10:48 a 0:12:27). Pergunta se a cobra tem direção ou se move numa direção recebida por parâmetro, e decide que tem, porque teria de guardá-la em algum lugar (0:13:24 a 0:13:37). Escreve o teste de que uma cobra indo para a esquerda ignora o pedido de virar para a direita (0:13:40 a 0:14:24), pede uma coisa de cada vez quando a conversa vai para direção relativa (0:14:43 a 0:14:48), separa o mapeamento de teclas do jogo do turn (0:15:45 a 0:16:14), implementa o turn como atribuição de direção e o slither somando a direção à cabeça, e o teste passa (0:16:16 a 0:17:06).

Linha do tempo:
- [0:00:02] arquivo de teste da cobra
- [0:00:47] primeiro teste: cabeça em zero zero, tamanho 3
- [0:02:21] prototipa o range no console
- [0:03:02] manter a lista como o autor fez
- [0:04:24] o algoritmo acessa por índice: teste e `__getitem__`
- [0:06:07] `__setitem__`
- [0:06:32] temporário, não quer expor: o algoritmo do autor tem que funcionar com a classe
- [0:06:51] o preço: interface nova por testes, interface com o jogo mantida
- [0:08:31] o turn não move a cobra, só muda a direção
- [0:11:21] a direção é um vetor
- [0:13:24] a cobra tem direção ou se move numa direção?
- [0:14:06] teste: indo para a esquerda, ignora a direita
- [0:14:43] uma coisa de cada vez
- [0:16:24] turn guarda a direção; slither soma à cabeça; passou

Princípios:
- Quando se quer mover lógica para uma classe nova, a classe nasce por testes e oferece primeiro a interface que o código antigo já usa, com adaptadores temporários, para o jogo não parar (0:06:32 a 0:07:13).
- Não jogar fora a lógica do autor: preservar o comportamento enquanto ele migra (0:06:43 a 0:06:51).
- Escrever o teste revela o que o código faz de verdade, como o turn que não move (0:08:31 a 0:08:45).
- Modelar pela pergunta concreta: o estado é do objeto ou é parâmetro da operação? (0:13:24 a 0:13:37).
- Uma coisa de cada vez (0:14:43 a 0:14:48).

Código: reconstrução a partir da fala; não publicada. Nomes prováveis: Snake, body, head, length, direction, turn, slither [legenda: slider], `__getitem__`, `__setitem__`. É o estado da classe ao fim da aula; a lógica de movimento do corpo, portada do tutorial, não é reproduzida.

```python
# reconstrução a partir da fala, não publicada
class Snake:
    LEFT, RIGHT, UP, DOWN = (-1, 0), (1, 0), (0, -1), (0, 1)  # ordem dita em 0:15:03

    def __init__(self, head, length=3, direction=LEFT):
        x, y = head
        self.body = [(x + i, y) for i in range(length)]
        self.direction = direction

    def __getitem__(self, item):      # o algoritmo antigo acessa por índice
        return self.body[item]

    def __setitem__(self, item, value):  # temporário, não exposto (0:06:32)
        self.body[item] = value

    def turn(self, direction):
        self.direction = direction

    # slither: o deslocamento do corpo ainda é o do tutorial (não reproduzido);
    # a cabeça passa a ser cabeça + direção, componente a componente (0:16:42)


def test_snake_body():
    s = Snake((0, 0))
    assert s.body == [(0, 0), (1, 0), (2, 0)]

def test_turn_ignores_reverse():      # descrito em 0:14:06; a regra só passa na aula 9
    s = Snake((0, 0))
    s.turn(Snake.RIGHT)
    assert s.direction == Snake.LEFT
```

Citações (paráfrases de legenda, não verificadas):
- [0:06:35] esses sete não é temporário isso eu não quero expor isso não mas eu quero fazer que o algoritmo dele funcione com essa classe [sete: set, `__setitem__`]
- [0:06:43] senão vou jogar fora o código do cara vou mudar a lógica da toda e aí a gente vai o jogo não vai ficar sem funcionar
- [0:06:51] eu tô pagando um preço aqui que eu tô criando uma nova interface que é a nossa classe através de testes
- [0:13:24] a cobra tem direção ou ela se move numa direção

### Aula 6: #06 - Como implantar um código novo em um sistema legado
Vídeo: https://www.youtube.com/watch?v=TUcujjrODwo · Duração: 7:28

Resumo: é hora de conectar a classe ao jogo. Escreve o teste do eat: comer só aumenta a cobra, e para respeitar o que o autor tinha feito e a lógica do slither, o eat acrescenta um valor provisório que o próximo movimento conserta (0:00:00 a 0:02:02). Diz que já há uma coisa que o irrita profundamente: pegar o zero como x e o um como y, faltando uma classe de ponto para ocultar essa matemática; mas antes quer o jogo funcionando (0:02:04 a 0:02:21). Troca no laço principal a lista da cobra por uma Snake, chama eat na colisão e acerta a ordem, primeiro turn depois slither (0:02:27 a 0:03:30). Compensa no desenho a multiplicação por 10 entre grade e pixel (0:03:44 a 0:04:03), roda, corrige erros um a um (direção padrão para a esquerda, a maçã ainda em pixels, a nova maçã não sorteada) e repete que tem que haver um ponto que resolva a multiplicação (0:04:07 a 0:06:07). Com o jogo rodando, comemora ter refatorado sem matar o software, e define o exercício: extrair comportamento para criar o espaço de levar o código aonde se quer, sem matar o paciente (0:06:09 a 0:06:28). Faz o commit com os testes passando (0:06:45 a 0:07:02).

Linha do tempo:
- [0:00:00] hora de conectar a classe ao jogo
- [0:00:13] teste do eat
- [0:01:02] respeitar a lógica do slither: valor provisório ao crescer
- [0:02:09] falta uma classe de ponto para esconder a matemática
- [0:02:19] mas primeiro quero o jogo funcionando
- [0:02:27] o laço passa a usar a Snake
- [0:03:04] primeiro turn, depois slither
- [0:03:44] compensar a multiplicação por 10 no desenho
- [0:05:38] tem que ter um objeto ponto que resolva isso
- [0:06:09] refatorou sem matar o software
- [0:06:15] extrair comportamento sem matar o paciente
- [0:06:45] commit com testes passando

Princípios:
- Ver o problema seguinte e não resolvê-lo antes de fechar o atual: o jogo volta a funcionar primeiro (0:02:09 a 0:02:21).
- Respeitar a lógica existente ao encaixar a peça nova (0:01:02 a 0:01:09).
- Refatorar é extrair comportamento para abrir espaço, sem matar o paciente (0:06:15 a 0:06:28).

Código: reconstrução a partir da fala; não publicada. Só o eat e seu teste; o laço do jogo é do tutorial e não é reproduzido.

```python
# reconstrução a partir da fala, não publicada
    def eat(self):
        self.body.append((0, 0))  # provisório; o slither o leva à posição certa (0:01:09)

def test_eat():
    s = Snake((0, 0))
    s.eat()
    assert len(s.body) == 4       # asserção exata não legível; a fala diz que só aumenta a cobra
```

Citações (paráfrases de legenda, não verificadas):
- [0:02:11] esse negócio de pegar o zero é x e y tá faltando uma classe de ponto aqui para ocultar toda essa mágica
- [0:02:19] mas eu quero botar para funcionar o jogo
- [0:06:09] Olha quem te refaturou a parada sem matar o software
- [0:06:20] como é que você extrai comportamento para criar o espaço de tornar o código né levar o código para onde você quer sem matar o paciente

### Aula 7: #07 - Creating new features for a legacy project safely
Vídeo: https://www.youtube.com/watch?v=vruZt-uX2ZU · Duração: 8:29 · Título como listado no `playlist.json` (provável tradução automática; o original em português não consta na coleta)

Resumo: anuncia que vai fazer uma mágica só criando uma ferramenta auxiliar (0:00:06 a 0:00:13). Cria o arquivo e o teste do Point: tem que ter x e y, poder somar dois pontos e poder comparar dois pontos (0:00:25 a 0:00:40). Os testes: atributos, soma de um zero com zero um igual a um um, e multiplicação de um um por 10 igual a dez dez (0:00:46 a 0:01:25). Implementa a igualdade, a soma e a multiplicação por escalar, e os testes passam (0:02:01 a 0:02:49). Ao refatorar a Snake para receber um ponto, um participante sugere namedtuple e manda o exemplo da documentação (0:03:01 a 0:06:10). Ele adota a ideia e explica o `__slots__` que aparece no exemplo: uma otimização de alocação de memória que diz que não existirão outros atributos além dos definidos pela classe base (0:06:15 a 0:06:29); com namedtuple, a comparação com tupla e com ponto já funciona (0:06:33 a 0:06:40). Dá o crédito da dica (0:06:40 a 0:06:44). Com os testes no lugar, simplifica os algoritmos da Snake: a cabeça já é um ponto, o corpo é range mais Point, e as direções podem virar pontos que se somam (0:07:01 a 0:07:24). Um participante batiza o jogo de Stallone Cobra (0:07:30 a 0:08:02).

Linha do tempo:
- [0:00:10] uma ferramenta auxiliar
- [0:00:34] o Point precisa de x e y, soma e comparação
- [0:00:46] testes de atributos e de soma
- [0:01:16] teste de multiplicação por escalar
- [0:02:01] implementa igualdade, soma e multiplicação
- [0:02:49] refatorar a Snake para receber um ponto
- [0:03:01] sugestão de namedtuple vinda do chat
- [0:06:15] o que é `__slots__`
- [0:06:33] namedtuple já compara com tupla
- [0:07:01] simplifica os algoritmos, os testes já existem
- [0:07:20] as direções viram pontos

Princípios:
- Um valor pequeno, criado por teste, esconde a aritmética espalhada (0:00:34 a 0:01:25).
- Com teste no lugar, simplificar o algoritmo é seguro (0:07:01 a 0:07:05).
- Aceitar a ferramenta melhor quando ela aparece, e dar o crédito (0:06:40 a 0:06:44).

Código: reconstrução a partir da fala; não publicada. A forma final do Point não é legível: ele adota namedtuple com `__slots__` a partir do exemplo da documentação, e a fala sugere que a igualdade própria some (a comparação de tupla basta, 0:06:33) e que a soma talvez não precise ficar (0:04:57), mas a cobra soma pontos nas aulas 8 e 9 e o teste de soma continua; a versão abaixo mantém soma e escalar, que os testes exigem.

```python
# reconstrução a partir da fala, não publicada
from collections import namedtuple

class Point(namedtuple('Point', 'x y')):
    __slots__ = ()   # nenhum atributo além dos da classe base (0:06:15)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Point(self.x * scalar, self.y * scalar)


def test_point():
    p = Point(0, 0)
    assert p.x == 0 and p.y == 0

def test_sum():
    assert Point(1, 0) + Point(0, 1) == Point(1, 1)

def test_multiplication():
    assert Point(1, 1) * 10 == Point(10, 10)
```

Citações (paráfrases de legenda, não verificadas):
- [0:00:34] essas coisas de tem que ter o X e Y tem que poder somar dois pontos e tem que ter poder comparar dois pontos
- [0:06:18] o slot é porque é uma otimização a indicação de otimização de alocação de memória do Python
- [0:07:01] eu quero simplificar aqueles algoritmos boladões né já tem os testes aí

### Aula 8: #08 - Como ampliar a capacidade do projeto legado sem quebrar nada
Vídeo: https://www.youtube.com/watch?v=5Fo7DslEZTg · Duração: 7:44

Resumo: começa a fazer sentido ter o corpo separado da cabeça (0:00:10 a 0:00:20). Ele nota que poderia matar o deslocamento com um deque, mas antes separa a cabeça num atributo próprio, usando o refactor do PyCharm [legenda: pai Charme] (0:01:00 a 0:01:22). Para o resto continuar funcionando, o acesso por índice passa a devolver a cabeça quando o índice é zero, o que ele chama de gambiarra temporária, que vão eliminar (0:02:17 a 0:02:47). O slither e o teste quebram e são ajustados; a cabeça passa a andar com mais igual a direção (0:03:01 a 0:03:57), e ele reclama que índice é chato de ficar mexendo (0:04:22 a 0:04:29). Simplifica um teste que tinha repetição desnecessária (0:05:12 a 0:05:19), passa, e vai ao jogo: com Point, a conversão de grade para pixel vira x vezes 10 e y vezes 10 sobre o ponto, com desempacotamento (0:05:25 a 0:06:43). Com isso elimina um monte de código (0:06:45 a 0:06:53) e faz o commit usa Point para simplificar as contas (0:06:57 a 0:07:18).

Linha do tempo:
- [0:00:10] faz sentido o corpo separado da cabeça
- [0:01:00] poderia ser um deque, mas primeiro separar
- [0:01:13] refactor do PyCharm
- [0:02:29] a gambiarra temporária no índice zero
- [0:03:01] slither e teste quebram e são ajustados
- [0:03:49] a cabeça anda com mais igual a direção
- [0:04:26] índice é chato de mexer
- [0:05:14] simplifica a repetição no teste
- [0:05:38] no jogo, a conversão vezes 10 sobre o Point
- [0:06:48] elimina um monte de código
- [0:07:14] commit: usa Point para simplificar as contas

Princípios:
- Adaptador temporário dito em voz alta, com a intenção de removê-lo, para o resto continuar funcionando (0:02:24 a 0:02:47).
- Uma mudança estrutural por vez: separar a cabeça antes de trocar a estrutura (0:01:00 a 0:01:10).
- O teste também se refatora quando tem repetição (0:05:12 a 0:05:19).

Código: reconstrução a partir da fala; não publicada. Nomes prováveis: head [legenda: Red], tail [legenda: Taylor].

```python
# reconstrução a partir da fala, não publicada
class Snake:
    def __init__(self, head, length=3, direction=LEFT):
        self.head = head
        self.tail = [head + Point(i, 0) for i in range(1, length)]
        self.direction = direction

    def __getitem__(self, item):
        if item == 0:            # gambiarra temporária (0:02:29)
            return self.head
        return self.tail[item - 1]
```

Citações (paráfrases de legenda, não verificadas):
- [0:01:00] matar isso com um Deck a gente muda esse cara aqui para ser um Deck mas aí eu separo [Deck: deque]
- [0:02:29] é a gambiarra temporária
- [0:04:26] essa merda cara índice é [ __ ] ficar mexendo [palavrão censurado na legenda]

### Aula 9: #09 - Como reduzir o débito técnico para garantir a saúde do seu projeto
Vídeo: https://www.youtube.com/watch?v=lNTog38daKQ · Duração: 10:33

Resumo: última coisa: mexer só no interno, e os testes devem continuar passando (0:00:00 a 0:00:12). Explica o deque: a lista do Python é um array dinâmico, não uma lista encadeada, e inserir no início custa mexer na posição de todo mundo; o deque permite mexer nas duas pontas em O(1) (0:00:15 a 0:00:41). Assim o slither põe a nova cabeça na frente e tira o último, em vez de arrastar todo mundo (0:00:43 a 0:01:17). Roda o jogo sem rodar o teste e funciona; o teste quebra porque a comparação do deque com lista é diferente (0:01:17 a 0:01:34). O `__setitem__` sai, porque não é mais usado (0:01:51 a 0:01:58), e o teste passa a comparar a lista da cobra inteira: para ele, aquilo já é a cobra (0:02:09 a 0:02:27). Diante de quem acha deselegante o atributo que existe só para simplificar o teste, responde que está dentro da classe, encapsulado; só se estivesse vazando faria sentido torná-lo mais elegante já (0:02:58 a 0:03:10). Comemora menos código (0:03:18 a 0:03:21), mantém a validação da API (0:03:24 a 0:03:28) e faz o commit (0:03:56 a 0:04:04). Então corrige a regra anotada na aula 2: um teste com a sequência esquerda, cima, direita, baixo, verificando que a virada para trás é ignorada (0:04:23 a 0:05:21); descobre no console que duas direções opostas somam zero, e o turn ganha um retorno antecipado quando a soma da direção nova com a atual é o ponto zero zero (0:06:01 a 0:06:44). O jogo não volta mais para trás (0:06:47 a 0:06:57). Ele pede que se imagine fazer aquilo sem teste (0:06:59 a 0:07:07) e explica a forma do turn: o return faz papel de aborto, a estrutura é entrada, validação da entrada e processamento; com isso, se a lógica mudar, sabe-se onde mexer (0:07:27 a 0:07:56). Programa-se para quem vai ler o código, que pode ser você mesmo (0:07:59 a 0:08:05). Simplifica o acesso por índice deixando o zero como único caso especial (0:08:12 a 0:08:33), faz o commit corrige a lógica (0:08:48 a 0:08:56) e fecha com o saldo: isolar a lógica do jogo da estrutura de exibição e atualização para fazer o multiplayer com power ups; a maçã vira ponto numa próxima vez (0:09:18 a 0:10:10).

Linha do tempo:
- [0:00:08] mexer só no interno; os testes devem continuar passando
- [0:00:15] lista é array dinâmico; deque tem O(1) nas duas pontas
- [0:00:53] slither: nova cabeça na frente, tira o último
- [0:01:24] o jogo funciona, o teste quebra pela comparação do deque
- [0:01:54] o `__setitem__` sai
- [0:02:12] o teste compara a lista da cobra inteira
- [0:02:58] encapsulado, o deselegante não é problema
- [0:04:23] teste da sequência de viradas
- [0:06:16] direções opostas somam zero
- [0:06:31] turn aborta quando a soma é o ponto zero
- [0:07:27] o return como aborto: entrada, validação, processamento
- [0:07:59] programa-se para quem vai ler
- [0:09:50] o saldo: lógica do jogo isolada da exibição

Princípios:
- Troca de estrutura interna atrás de interface estável: os testes não mudam de propósito (0:00:08 a 0:00:12).
- Escolher a estrutura de dados pelo custo da operação que o domínio faz (0:00:15 a 0:01:12).
- Remover o andaime quando ninguém mais o usa (0:01:54 a 0:01:58).
- Feiura encapsulada pode esperar; feiura que vaza, não (0:02:58 a 0:03:10).
- Validação no topo como aborto, depois o processamento: entrada, validação, processamento, saída (0:07:27 a 0:07:56).
- Programar para quem vai ler, que pode ser você mesmo (0:07:59 a 0:08:05).
- Mudança rápida e segura só existe com teste (0:06:59 a 0:07:07).

Código: reconstrução a partir da fala; não publicada. Estado provável da classe ao fim da série. Nomes e chamadas do deque são leituras prováveis (appendleft e pop não são legíveis na legenda, 0:00:58 a 0:01:12).

```python
# reconstrução a partir da fala, não publicada
from collections import deque

class Snake:
    def __init__(self, head, length=3, direction=LEFT):
        self.head = head
        self.tail = deque(head + Point(i, 0) for i in range(1, length))
        self.direction = direction

    def __getitem__(self, item):
        return self.tail[item - 1] if item else self.head  # só o zero é caso especial (0:08:29)

    def turn(self, direction):
        if direction + self.direction == Point(0, 0):  # opostas somam zero (0:06:31)
            return                                     # o return faz papel de aborto (0:07:32)
        self.direction = direction

    def slither(self):
        self.tail.appendleft(self.head)
        self.tail.pop()
        self.head += self.direction


def test_turn_sequence():
    s = Snake(Point(0, 0))   # começa para a esquerda
    s.turn(RIGHT); assert s.direction == LEFT
    s.turn(UP);    assert s.direction == UP
    s.turn(DOWN);  assert s.direction == UP
    s.turn(RIGHT); assert s.direction == RIGHT
    s.turn(LEFT);  assert s.direction == RIGHT
```

Citações (paráfrases de legenda, não verificadas):
- [0:00:24] a lista do Python quando adiciona um elemento no início dela ele precisa ele tem custo de mexer na posição de todo mundo
- [0:03:01] ele tá dentro da classe Tá encapsulado então não vejo no stress para isso não se ele tivesse vazando Aí sim
- [0:07:04] imagina fazer essa sem teste tá louco essas mudanças
- [0:07:59] Você programa para quem vai ler o código entendeu para quem vai ter que mexer nessa depois no caso pode ser você mesmo

## 6. Princípios que atravessam toda a série

Dez regras que ele formula na fala. Nenhuma é inferência deste documento, e nenhuma vem de trecho de participante.

#### 1. Separe a lógica do domínio do motor antes de qualquer outra coisa

O drama do código é o pygame misturado com a lógica do jogo, e a primeira coisa que ele tenta é separar (aula 3, 0:03:13 a 0:03:34). Esvazia o laço até poder dizer: isto é a lógica do jogo, o resto é do pygame (aula 4, 0:02:39 a 0:02:45). O tabuleiro do jogo não tem nada a ver com o pygame e poderia ser de console (aula 4, 0:03:28 a 0:03:48). O saldo da série é exatamente esse isolamento (aula 9, 0:09:50 a 0:10:02).

#### 2. Separe para poder mexer de forma isolada

Para mexer no código é preciso separá-lo, para mexer de forma isolada (aula 4, 0:04:25 a 0:04:37). O commit nomeia a etapa: camadas separadas (aula 4, 0:05:55 a 0:06:04).

#### 3. Não mate o paciente: a classe nova serve primeiro ao código antigo

Ele não joga fora a lógica do autor, porque o jogo pararia de funcionar (aula 5, 0:06:43 a 0:06:51). Cria por testes uma interface nova, a classe, e move para dentro dela a lógica que é da cobra, mantendo a interface com o jogo (aula 5, 0:06:51 a 0:07:13). Refatorar é extrair comportamento para criar o espaço de levar o código para onde se quer, sem matar o paciente (aula 6, 0:06:15 a 0:06:28).

#### 4. Adaptador temporário se declara e se remove

O `__setitem__` é temporário e não deve ser exposto; existe só para o algoritmo antigo funcionar com a classe (aula 5, 0:06:32 a 0:06:40). O índice zero que devolve a cabeça é uma gambiarra temporária que vão eliminar (aula 8, 0:02:29 a 0:02:47). Quando ninguém mais usa o `__setitem__`, ele sai (aula 9, 0:01:54 a 0:01:58).

#### 5. Tem que fazer teste, e teste é o que permite mudar rápido

Não tem jeito, tem que fazer teste (aula 3, 0:01:28 a 0:01:38). As mudanças internas são feitas com os testes passando (aula 9, 0:00:08 a 0:00:12), e a correção da regra de direção foi rápida porque havia teste: imagine fazer sem (aula 9, 0:06:59 a 0:07:07). Quando um passo é dado sem teste, ele diz (aula 3, 0:09:10 a 0:09:13) e roda o jogo para conferir (aula 4, 0:04:37 a 0:04:45).

#### 6. Uma coisa de cada vez

Agora é só esvaziar o código para separar as camadas, não usar as constantes (aula 4, 0:02:14 a 0:02:22). Uma coisa de cada vez, já é uma mudança (aula 5, 0:14:43 a 0:14:48). A classe de ponto que falta espera o jogo voltar a funcionar (aula 6, 0:02:09 a 0:02:21). O deque espera a cabeça ser separada (aula 8, 0:01:00 a 0:01:10).

#### 7. O comportamento que mexe no mesmo dado é método do mesmo objeto

Mudar a direção deveria ser só o turn da cobra, movimentar só o slither, e comer só o eat: tem que haver uma classe Snake (aula 4, 0:06:51 a 0:07:15). A cobra tem direção porque o estado precisa ser guardado em algum lugar (aula 5, 0:13:24 a 0:13:37).

#### 8. Um valor para a matemática que se repete

Falta uma classe de ponto para ocultar a matemática de pegar o zero como x e o um como y (aula 6, 0:02:09 a 0:02:18). O Point tem x e y, soma e comparação (aula 7, 0:00:34 a 0:00:40), e com ele direção, movimento, conversão para pixel e a regra de não voltar viram operações de ponto (aula 7, 0:07:20; aula 8, 0:06:03; aula 9, 0:06:31).

#### 9. Encapsulado, a deselegância espera; vazando, não

O que está dentro da classe, encapsulado, não é motivo de stress; se estivesse vazando, aí sim (aula 9, 0:02:58 a 0:03:10). Trocar a lista pelo deque mexe só no interno (aula 9, 0:00:08 a 0:00:12).

#### 10. Validação no topo como aborto, e código para quem vai ler

O return do turn faz papel de aborto: entrada, validação da entrada, processamento; assim se sabe onde mexer quando a lógica muda (aula 9, 0:07:27 a 0:07:56). Programa-se para quem vai ler o código, que pode ser você mesmo (aula 9, 0:07:59 a 0:08:05).

## 7. Citações-chave do curso

Paráfrases de legenda automática, sem aspas e não verificadas contra o vídeo. Nenhuma linha vem de trecho de participante.

| Aula | Timestamp | Paráfrase |
|---|---|---|
| #1 | 0:02:21 | não vão começar do zero né porque eu vou copiar fazer um forte desse projeto [provável: fork] |
| #1 | 0:09:12 | Tô conhecendo o pai game agora então eu sei tanto quanto você [pai game: pygame] |
| #2 | 0:02:24 | isso é bom mas é ruim é bom porque simplifica para caceta |
| #2 | 0:06:16 | lógica reversa é complicado o fruto do cérebro |
| #3 | 0:01:03 | agora nada que eu vou falar é sobre o código do [autor] é com foco no nosso objetivo |
| #3 | 0:01:28 | cara não tem jeito tem que fazer teste tem que fazer teste |
| #3 | 0:09:10 | isso é sem teste né estamos só mexendo na parada aqui |
| #4 | 0:02:17 | eu quero só esvaziar o código para separar a camada do pai game da lógica do jogo |
| #4 | 0:04:31 | ele precisa separar ele separar para poder mexer de forma isolada |
| #4 | 0:07:08 | tá bem claro para mim que tem que ter um objeto uma classe cobra a classe Snake |
| #5 | 0:06:35 | isso eu não quero expor isso não mas eu quero fazer que o algoritmo dele funcione com essa classe |
| #5 | 0:06:51 | eu tô pagando um preço aqui que eu tô criando uma nova interface que é a nossa classe através de testes |
| #5 | 0:13:24 | a cobra tem direção ou ela se move numa direção |
| #6 | 0:02:11 | tá faltando uma classe de ponto aqui para ocultar toda essa mágica essa matemática |
| #6 | 0:06:20 | como é que você extrai comportamento para criar o espaço de levar o código para onde você quer sem matar o paciente |
| #7 | 0:07:01 | eu quero simplificar aqueles algoritmos boladões né já tem os testes aí |
| #8 | 0:02:29 | é a gambiarra temporária |
| #9 | 0:03:01 | ele tá dentro da classe Tá encapsulado então não vejo no stress para isso não se ele tivesse vazando Aí sim |
| #9 | 0:07:04 | imagina fazer essa sem teste tá louco essas mudanças |
| #9 | 0:07:59 | Você programa para quem vai ler o código entendeu para quem vai ter que mexer nessa depois no caso pode ser você mesmo |

## 8. A evolução técnica, aula a aula

O programa é um jogo da cobrinha em pygame, num único arquivo, escrito como tutorial por um membro da comunidade (aula 1, 0:00:15 a 0:00:33). A tabela mostra a ordem das mudanças; o código original não é reproduzido.

| Etapa | O que é feito | Conceito ou ferramenta | O que isso destrava |
|---|---|---|---|
| **#1** | Fork, ambiente, rodar o jogo, ler com a documentação aberta (0:02:21 a 0:07:41) | PyCharm, documentação do pygame, console | Saber o que o jogo faz antes de mexer |
| **#2** | Grade de 64 por 48, Clock, fila de eventos, movimento desenhado numa planilha (0:00:05 a 0:10:47) | leitura com desenho externo | Anotar três dívidas: cálculo em pixel, cobra que volta, movimento O(n) |
| **#3** | Requisitos, pacote com `__main__`, pacote de testes, função main, fill com retângulo (0:01:45 a 0:09:04) | python -m, desempacotamento | Um projeto que se testa e se roda como pacote |
| **#4** | Funções eat, slither, turn; camadas separadas; commit (0:00:06 a 0:06:04) | extração com global temporária | A lógica do jogo isolada do pygame (0:02:39) |
| **#5** | Classe Snake por testes, com acesso por índice temporário; direção como vetor (0:00:02 a 0:17:06) | pytest, `__getitem__`, `__setitem__` | A lógica da cobra muda de lugar sem o jogo parar |
| **#6** | O jogo usa a Snake; eat; ordem turn e slither (0:00:00 a 0:07:02) | adaptação no laço | Primeiro commit com a classe nova em produção |
| **#7** | Point por testes; namedtuple com `__slots__` (0:00:25 a 0:07:24) | valor imutável, sobrecarga de operadores | Direções e posições somáveis |
| **#8** | Cabeça separada do corpo; conversão de pixel com Point (0:00:10 a 0:07:18) | refactor do PyCharm, gambiarra temporária | Menos código no laço; preparação para o deque |
| **#9** | Deque; teste pela lista inteira; turn que não volta; commit (0:00:15 a 0:08:56) | `collections.deque`, soma de vetores opostos | A dívida da aula 2 paga e a lógica pronta para o multiplayer |

## 9. Arsenal técnico demonstrado no curso

| Técnica ou recurso | Para que ele usa | Aula e timestamp |
|---|---|---|
| Fork em vez de começar do zero | Partir do código que funciona | #1, 0:02:21 a 0:02:27 |
| Documentação aberta durante a leitura | Entender uma biblioteca desconhecida chamada por chamada | #1, 0:04:57 a 0:07:41; #2, 0:01:22 a 0:02:21 |
| Console Python para investigar expressões | Descobrir o arredondamento da posição; prototipar range; somar direções | #1, 0:08:34; #5, 0:02:21; #9, 0:06:01 |
| Planilha como tabuleiro | Desenhar o estado para entender o movimento | #2, 0:07:15 a 0:08:49 |
| Pacote com `__main__.py` e python -m | Rodar o jogo como pacote e abrir espaço para testes | #3, 0:02:19 a 0:02:53 |
| Global temporária | Conseguir extrair funções de um laço que compartilha variáveis | #4, 0:00:06 a 0:00:12 |
| Rodar o jogo depois de cada mudança grande | Verificar o que ainda não tem teste | #4, 0:04:37 a 0:05:10 |
| Commits por etapa | Fechar cada passo com um nome | #4, 0:05:55; #6, 0:06:45; #8, 0:07:14; #9, 0:03:56 e 0:08:50 |
| `__getitem__` e `__setitem__` como adaptadores | Deixar o algoritmo antigo usar a classe nova | #5, 0:04:24 a 0:06:40 |
| Direção como vetor | Trocar códigos 0 a 3 por deslocamentos somáveis | #5, 0:11:21 a 0:12:27 |
| Point sobre namedtuple, com `__slots__` | Valor com x, y, soma e escalar, comparável com tupla | #7, 0:00:34 a 0:06:40 |
| Refactor do PyCharm | Renomear e separar atributos com segurança | #8, 0:01:13 a 0:01:22 |
| `collections.deque` | Mexer nas duas pontas da cobra em O(1) | #9, 0:00:15 a 0:01:12 |
| Soma de direções opostas igual a zero | Detectar a virada para trás numa linha | #9, 0:06:16 a 0:06:44 |
| Retorno antecipado como aborto | Validação no topo antes do processamento | #9, 0:07:27 a 0:07:56 |

## 10. Glossário do curso

| Termo | Significado no contexto da série | Onde |
|---|---|---|
| **Cobrinha com esteroides** | A meta do fork: Snake multiplayer online com power ups | #1, 0:01:07 a 0:02:12 |
| **Motor** | O setup e o laço do pygame, separados da lógica do jogo | #4, 0:04:06 a 0:04:22 |
| **Camada do pygame** | Tudo o que desenha, lê eventos e controla o tempo | #4, 0:02:17 a 0:02:45 |
| **Lógica do jogo** | O que a cobra e a maçã sofrem, independente da exibição | #4, 0:02:39; 0:03:17 a 0:03:48 |
| **Grade** | A malha de 64 por 48 por trás dos 640 por 480 pixels | #1, 0:09:01 a 0:09:06; #2, 0:00:12 a 0:00:20 |
| **Slither** [legenda: slider, sleezer] | Rastejar: o movimento do corpo da cobra a cada quadro | #4, 0:01:06 a 0:01:41; #9, 0:00:53 |
| **Turn** | Mudar a direção, sem mover a cobra | #5, 0:08:31 a 0:08:43 |
| **Eat** | Comer: aumentar a cobra | #4, 0:00:30; #6, 0:00:56 a 0:01:02 |
| **Direção como vetor** | Cima, baixo, esquerda e direita como deslocamentos de uma unidade | #5, 0:11:21 a 0:12:27 |
| **Point** | Valor com x e y, soma e multiplicação por escalar | #7, 0:00:34 a 0:02:49 |
| **Gambiarra temporária** | Adaptador declarado como provisório, a ser removido | #8, 0:02:29 a 0:02:47 |
| **Não matar o paciente** | Refatorar sem que o programa pare de funcionar | #6, 0:06:15 a 0:06:28 |
| **Deque** [legenda: Deck] | Estrutura com inserção e remoção em O(1) nas duas pontas | #9, 0:00:15 a 0:00:41 |
| **Stallone Cobra** | O nome que um participante deu ao jogo | #7, 0:07:30 a 0:07:45 |

## 11. Perguntas e respostas que o curso responde

#### Por onde começar num código legado de outra pessoa?

Fazendo um fork em vez de começar do zero (aula 1, 0:02:21), rodando o programa antes de ler (aula 1, 0:04:04) e lendo com a documentação da biblioteca aberta (aula 1, 0:04:57 a 0:07:41).

#### Qual é o primeiro movimento de refatoração num programa com framework e regra misturados?

Separar a camada do framework da lógica do domínio (aula 3, 0:03:13 a 0:03:34; aula 4, 0:02:17 a 0:02:45), para poder mexer de forma isolada (aula 4, 0:04:25 a 0:04:37).

#### Dá para mexer sem teste?

Ele mexe sem teste no começo, só agrupando, e diz isso (aula 3, 0:09:10 a 0:09:13), conferindo rodando o jogo (aula 4, 0:04:37). Mas não tem jeito, tem que fazer teste (aula 3, 0:01:28), e as mudanças de lógica vêm com teste (aula 9, 0:06:59 a 0:07:07).

#### Como introduzir uma classe nova sem quebrar o código que ainda não foi migrado?

Criar a classe por testes oferecendo primeiro a interface que o código antigo usa, como acesso e atribuição por índice, de forma temporária e não exposta (aula 5, 0:06:32 a 0:07:13), e remover o adaptador quando ninguém mais o usa (aula 9, 0:01:54 a 0:01:58).

#### Como ele sabe que uma classe deve existir?

Quando vê que as operações sobre a mesma lista deveriam ser métodos de um objeto: turn, slither e eat da cobra (aula 4, 0:06:51 a 0:07:15).

#### A direção é estado da cobra ou parâmetro do movimento?

Estado, porque teria de ser guardada em algum lugar (aula 5, 0:13:24 a 0:13:37).

#### Por que criar um Point?

Para ocultar a matemática de pegar o índice zero como x e o um como y (aula 6, 0:02:09 a 0:02:18); com soma e escalar, direção, movimento e conversão para pixel viram operações de ponto (aula 7, 0:07:20; aula 8, 0:06:03).

#### Por que trocar a lista por um deque?

Porque a lista é um array dinâmico e inserir no início move todo mundo, enquanto o deque mexe nas duas pontas em O(1); a cobra só precisa pôr uma cabeça e tirar o último (aula 9, 0:00:15 a 0:01:12; aula 2, 0:10:20 a 0:10:47).

#### Um detalhe deselegante dentro da classe deve ser corrigido já?

Não, se está encapsulado; só se estivesse vazando (aula 9, 0:02:58 a 0:03:10).

#### Como impedir a cobra de virar para trás?

Duas direções opostas somam zero, então o turn aborta quando a soma da nova com a atual é o ponto zero zero (aula 9, 0:06:16 a 0:06:44).

#### Por que o return no topo do turn?

Ele faz papel de aborto: entrada, validação, processamento; quando a lógica mudar, sabe-se onde mexer (aula 9, 0:07:27 a 0:07:56), porque se programa para quem vai ler (aula 9, 0:07:59 a 0:08:05).

## 12. Repositórios e recursos

| Recurso | Onde encontrar | Observação |
|---|---|---|
| Playlist completa (fonte desta documentação) | [Refatoração com POO em código legado](https://www.youtube.com/playlist?list=PLeKXYyZCJHxeEeta6ddgqUagLp_Oo_kAx) | 9 vídeos. Os ids estão em `playlist.json` e nos links da seção 5. |
| Canal | [HB Network](https://www.youtube.com/@hbnetworkoficial) | |
| Tutorial de pygame que serve de legado | sem URL nas transcrições | De um membro da comunidade, publicado num fórum (aula 1, 0:00:15 a 0:00:33). Não é reproduzido nem avaliado aqui; o autor não é nomeado. |
| Documentação do pygame | citada, sem URL | Consultada ao vivo para init, display, Surface, Clock e eventos (aula 1, 0:04:57; aula 2, 0:01:22; aula 3, 0:00:41). |
| Documentação de `collections.namedtuple` | citada, sem URL | O exemplo com `__slots__` vem de um link mandado no chat (aula 7, 0:03:03 a 0:06:29). |
| Domine o Método da Refatoração Rápida | `kb/courses/refatoracao-rapida.md` | Curso dele sobre refatoração só com funções; contraste na seção 2.5. |

Repositórios do curso: **nenhum**. O fork é mencionado (aula 1, 0:02:21; commits nas aulas 4, 6, 8 e 9), mas não tem URL, caminho nem hash nas transcrições.

## 13. Análise linha a linha do código real

O curso não publica código com caminho, commit ou URL, portanto não há análise de código real. O programa refatorado é um tutorial de terceiro e não é reproduzido aqui, nem na forma original nem em trechos. O que a seção 5 traz são reconstruções a partir da fala do código que ele escreve ao vivo (testes, classe Snake, Point), marcadas como não publicadas. Limites que ficam registrados:

- Identificadores vêm deformados na legenda; os nomes usados nas reconstruções (Snake, head, tail, body, direction, turn, slither, eat, Point) são leituras prováveis.
- A forma final do Point não é legível: não se sabe se a soma e a multiplicação ficaram como métodos ao lado do namedtuple (aula 7, 0:04:57 a 0:06:53).
- As chamadas exatas do deque no slither não são legíveis (aula 9, 0:00:58 a 0:01:12), nem as asserções exatas dos testes de eat e de slither (aula 5, 0:08:54 a 0:09:38; aula 6, 0:00:13 a 0:02:02).
- O valor provisório que o eat acrescenta é uma escolha para respeitar o algoritmo do tutorial (aula 6, 0:01:02 a 0:01:15); sua sobrevivência depois do deque não é dita.

## 14. Execução real dos testes

O curso não publicou código nem suíte. Não há o que rodar. As reconstruções da seção 5 dependem de constantes e de um laço de jogo que a fala não dita por inteiro e não foram executadas nesta documentação.

---

Documentação elaborada a partir das transcrições das 9 aulas da playlist Refatoração com POO em código legado, de Henrique Bastos (HB Network), playlist `PLeKXYyZCJHxeEeta6ddgqUagLp_Oo_kAx`, legendas automáticas em português (pt-orig) capturadas em 2026-11-11. As citações são paráfrases das transcrições, não verificadas contra o vídeo (`verified: false`), renderizadas sem aspas e com os erros de reconhecimento anotados entre colchetes quando precisam aparecer. Falas de participantes identificadas (listadas no início) não são atribuídas a ele, e nenhum participante é nomeado. O código refatorado é um tutorial de pygame de um membro da comunidade: não é reproduzido e o autor não é nomeado. O fork e o código que ele escreve ao vivo não têm repositório, caminho nem commit publicados. Os títulos das aulas #5 e #7 aparecem em inglês no `playlist.json` e ficam como listados. Datas de publicação e visualizações não foram coletadas. Conteúdo de caráter educativo.
