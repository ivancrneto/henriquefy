<!-- written by the henrique-ingest distiller on 2026-10-08 from sources/transcripts/raio-x-da-oo/; see kb/courses/README.md for provenance and license -->

HB Network · Documentação de curso

# Raio X da Orientação a Objetos

As 5 aulas, dos paradigmas de programação à herança em Python, lidas aula a aula a partir das legendas automáticas, com o código do terminal reconstruído e verificado.

Instrutor: **Henrique Bastos** · Canal [HB Network](https://www.youtube.com/@hbnetworkoficial) · Playlist: [Raio X da Orientação a Objetos](https://www.youtube.com/playlist?list=PLeKXYyZCJHxdT8vUW3x9bd7B8PnwnHINW) · Repositório: nenhum publicado para esta série

Documento elaborado a partir das transcrições automáticas das 5 aulas (legendas em português, capturadas em 2026-10-08). O curso não publicou código: tudo que ele digita é feito ao vivo no terminal Python, e os trechos desta documentação são reconstruções a partir do que ele diz, marcadas como tal e verificadas por execução na seção 14.

## 1. Visão geral do curso

Raio X da Orientação a Objetos é uma série curta de **5 aulas** que somam **2.359 segundos, 39 minutos e 19 segundos**. É a versão compacta do argumento que a série Orientação a Objetos na Prática desenvolve em 23 aulas: antes de aprender a sintaxe de classes, o aluno precisa entender a distância entre o nível da máquina e o nível humano (aula #01, 0:00:43), o que um objeto tem que um dado não tem (aula #01, 0:07:17) e por que a sacada de Alan Kay foi a troca de mensagens, e não as classes (aula #03, 0:00:37).

O desenho é em dois blocos. As três primeiras aulas são conceituais e curtas: paradigmas (#01), uma demonstração de valor, identidade e tipo no terminal (#02) e a origem biológica da orientação a objetos em Alan Kay (#03). As duas últimas são mecânica de Python no terminal: a aula #04, que sozinha tem mais da metade da duração total, abre a classe e mostra `__dict__`, o fallback de atributos, o inicializador e o objeto método; a aula #05 fecha com herança e `super()`.

| Dimensão | Valor | Observação |
|---|---|---|
| Aulas | 5 | Playlist completa, numerada de #01 a #05. |
| Duração total | 2.359 s (39min 19s) | Soma das durações informadas pelos metadados de cada vídeo (`playlist.json`). |
| Aula mais curta / mais longa | 152 s (#03) / 1.252 s (#04) | A #04, classes, atributos e métodos, é 53% do curso. |
| Datas de publicação | não coletadas | O `playlist.json` desta coleta traz apenas id, título e duração. |
| Visualizações | não coletadas | Idem. |
| Transcrições | 5 de 5 disponíveis | Legenda automática em português (pt-orig); não há legenda humana. |
| Código do curso | nenhum publicado | As aulas citam nenhum repositório, gist ou documento; o código é digitado no terminal (aulas #02, #04 e #05). |
| Bloco prático | aulas #02, #04 e #05 | Sessões no interpretador interativo do Python. |

Nota de método: este documento tem uma única fonte, a transcrição automática. Cada afirmação traz aula e timestamp. As citações são paráfrases de legenda, sem aspas, não verificadas contra o vídeo, e os erros de reconhecimento de fala ficam anotados entre colchetes quando precisam aparecer. Os trechos de código da seção 5 são reconstruções do que ele narra, nunca cópias de um arquivo publicado; a seção 14 registra a execução dessas reconstruções.

## 2. Filosofia e método de ensino

### 2.1 Dar um passo atrás antes de avançar

A série abre reconhecendo que o termo orientação a objetos deixa uma grande interrogação no ar e que não é certo que todo mundo queira dizer a mesma coisa; por isso, antes de avançar, ele dá um passo para trás para garantir que todos falam da mesma coisa (aula #01, 0:00:05 a 0:00:19). O resto do curso é esse passo para trás.

### 2.2 Partir da distância entre dado e símbolo

Em vez de começar por classes, ele começa pelos níveis de programação: o baixo nível dos bits e do controle de para onde o elétron passa, e o alto nível do ser humano, das palavras, dos conceitos e das ideias (aula #01, 0:00:23 a 0:01:08). A diferença que sustenta toda a série é que dado tem apenas valor e símbolo tem significado (aula #01, 0:01:11). As abstrações existem para aproximar o código do nível simbólico (aula #01, 0:01:57 a 0:02:20).

### 2.3 A história como ordem de ensino

Os paradigmas são apresentados na ordem em que surgiram, cada um como resposta a uma dor do anterior: imperativo (aula #01, 0:02:57), procedural com sub-rotinas e saltos (0:03:49), estruturado com estruturas de controle de fluxo e variáveis locais (0:04:30), e só então a orientação a objetos, quando os dados se proliferaram e precisaram de uma forma melhor de ser organizados (0:05:16 a 0:05:42). É o mesmo método da série longa: o aluno precisa sentir o que doía antes de ver a solução.

### 2.4 O terminal como prova

Nenhum conceito fica só na fala. Valor, identidade e tipo são mostrados com `print`, `id` e `type` sobre duas listas (aula #02, 0:01:26 a 0:01:53). A afirmação de que `class` é um comando executável é provada colocando `print`, `for` e `if` dentro do corpo de uma classe e vendo o interpretador executar tudo (aula #04, 0:02:25 a 0:03:47). Ele chama a própria demonstração de loucura e de doideira (aula #04, 0:03:05 e 0:03:45), e é exatamente o efeito que quer.

### 2.5 Mostrar o que acontece por debaixo dos panos

A regra do acessor é explicada abrindo `__dict__` de classe e de instância (aula #04, 0:09:17 a 0:10:21), e a chamada de método é decomposta em `__func__`, `__self__` e `__call__` (aula #04, 0:17:42 a 0:19:21). Ele avisa que ninguém vai ficar fazendo coisas muito sutis e sagazes ao programar, mas faz questão de mostrar esses detalhes (aula #04, 0:20:32).

### 2.6 Desaprender Java, PHP e C++

O objetivo declarado da aula #04 é que o aluno tire tudo que conhece de Java, de PHP e de C++ sobre classes e objetos e olhe para o Python com um olhar completamente novo (aula #04, 0:20:40). A aula #05 termina na mesma nota: orientação a objetos em Python é muito mais flexível e maleável do que o que se vê popularmente (aula #05, 0:03:02).

## 3. Pilares conceituais

### 3.1 Dado versus símbolo, e as camadas de abstração

Tudo que existe na computação são abstrações das naturezas mais elementares da máquina (aula #01, 0:02:00). O exemplo escolhido é o `for`: em vez de contar passos, ele pede `for food in foods` e o Python conta por ele, e assim ele trabalha no nível simbólico de uma sequência (aula #01, 0:02:22). Paradigma de programação é, historicamente, o nome dessas abstrações: uma forma de pensar sobre um problema e de organizar a abordagem para a solução (aula #01, 0:02:39 a 0:02:57).

### 3.2 Valor, identidade e tipo

Um conjunto de bits pode significar qualquer coisa; é o contexto que o interpreta que diz o que ele significa, e não existe nele informação sobre o que ele é (aula #01, 0:06:57 a 0:07:12). Objetos têm valor, identidade e tipo, e isso muda tudo (aula #01, 0:07:17). Mesmo em C, a informação de tipo mora no compilador, na análise sintática, e não no dado em si (aula #01, 0:07:27). No terminal, os mesmos bits `0b1000001` são o inteiro 65 ou a letra A conforme o contexto (aula #02, 0:00:02 a 0:00:41); `==` compara valor e `is` compara identidade (aula #02, 0:02:42 a 0:03:20). A síntese: o tipo é o DNA, a espécie do objeto; a identidade é quem ele é no meio de todos os objetos em memória; o valor é o que tem nele quando é avaliado (aula #02, 0:03:59 a 0:04:14).

### 3.3 Troca de mensagens

A orientação a objetos foi criada por Alan Kay, matemático e biólogo, pensando em objetos como células que não acessam o interior umas das outras e se comunicam por troca de mensagens; a segunda metáfora é a de computadores em rede, que se comunicam por protocolos combinados (aula #03, 0:00:01 a 0:00:34). A tese do curso está em uma frase: esse processo de troca de mensagens é a base da orientação a objetos, não são as classes em si nem os objetos em si, mas como os objetos se relacionam, o que está entre os objetos (aula #03, 0:00:37 a 0:00:48).

### 3.4 Classe como DNA, objeto como organismo

Do artigo History of Smalltalk de Kay, ele extrai quatro afirmações: tudo é objeto; objetos se comunicam enviando e recebendo mensagens; cada objeto tem a sua própria memória, no sentido de estado, que não fica referenciado globalmente fora do objeto; e cada objeto é instância de uma classe (aula #03, 0:01:03 a 0:01:39). A classe armazena o comportamento comum, o objeto é o organismo vivo, a classe é o DNA, e o código não se replica em cada objeto: o objeto, sabendo quem é a sua classe, pede para o código da classe executar no contexto da sua própria memória (aula #03, 0:01:44 a 0:02:26).

### 3.5 Tudo é objeto, inclusive a classe e o método

Classes em Python são objetos, e a palavra `Car` é uma variável que referencia o objeto classe na memória em tempo de execução (aula #04, 0:00:22 a 0:00:33). Classe é objeto, instância é objeto, função é objeto, método é objeto (aula #04, 0:17:09). A consequência, na aula #05: como tudo em Python é objeto, a todo momento há a oportunidade de definir melhores relações entre os objetos que compõem o programa, e esse é o segredo da maleabilidade do Python (aula #05, 0:03:12 a 0:03:33).

## 4. As aulas em uma tabela

| # | Título | Duração | Foco em uma linha |
|---|---|---|---|
| 01 | Raio X da Orientação a Objetos #01: Os paradigmas de programação | 467 s | Baixo nível e alto nível, dado versus símbolo, a sequência imperativo, procedural, estruturado, funcional, orientado a objetos; o que um objeto tem a mais que um dado. |
| 02 | Raio X da Orientação a Objetos #02: Demonstração no Terminal | 273 s | Os mesmos bits como 65 e como A; valor, identidade e tipo de duas listas; `==` versus `is`; `type` devolve a própria classe. |
| 03 | Raio X da Orientação a Objetos #03: Alan Kay | 152 s | Células e redes como metáforas; troca de mensagens como base; as quatro afirmações do History of Smalltalk; classe como DNA. |
| 04 | Raio X da Orientação a Objetos #04: Classes, atributos e métodos no Python | 1.252 s | `class` como comando executável; atributos de classe e de instância; `__dict__` e o fallback do acessor; `__init__`; método como objeto com `__func__` e `__self__`. |
| 05 | Raio X da Orientação a Objetos #05: Herança no Python | 215 s | `class Ferrari(Car)`; `super().__init__` explícito; onde cada atributo mora; não confundir orientação a objetos com criar classes. |

## 5. Resumo por aula

### Aula #01: Os paradigmas de programação

Vídeo: https://www.youtube.com/watch?v=a9LXgufi1e4 · 467 s

A aula é inteiramente expositiva e constrói a motivação do paradigma em três movimentos: a distância entre o nível da máquina e o nível humano, a sucessão histórica dos paradigmas como camadas de abstração sobre essa distância, e a definição do que um objeto tem a mais do que um dado. O ponto de chegada é a tríade valor, identidade e tipo, que a aula #02 vai demonstrar no terminal.

Linha do tempo:

- [0:00:05] Abertura: quando ele fala orientação a objetos fica uma grande interrogação no ar; dar um passo para trás para garantir que todos falam da mesma coisa.
- [0:00:23] Níveis de programação: baixo nível é o nível dos bits, do controle de para onde o elétron passa; alto nível é o nível do ser humano.
- [0:01:11] Dado tem apenas valor; símbolo tem significado; a distância entre os dois é gigante.
- [0:01:19] Programar em baixo nível não é natural para o ser humano e exige esforço cognitivo enorme; o computador, por sua vez, não trabalha no nível simbólico.
- [0:01:57] As camadas de abstração ligam os dois mundos; tudo na computação são abstrações de dados; o exemplo é `for food in foods`.
- [0:02:39] Essas abstrações, historicamente, são os paradigmas; um paradigma é uma forma de pensar sobre um problema.
- [0:02:57] Paradigma imperativo: o paradigma da ordem, do comando; natural quando as máquinas eram rústicas e se fazia a gestão do estado da máquina.
- [0:03:49] Paradigma procedural: sub-rotinas, condições testadas e saltos de um trecho de código para outro.
- [0:04:30] Paradigma estruturado: estruturas de controle de fluxo como o `for`, linguagens como C, variáveis locais reduzindo as globais.
- [0:05:01] Paradigmas declarativos, como o funcional, que evita controle de fluxo e trata tudo como expressões e funções.
- [0:05:16] Um programa é feito simultaneamente de comandos e de dados; gerenciar dados sempre foi um grande desafio.
- [0:05:39] Surge a orientação a objetos: a sacada é organizar dados e código na mesma unidade de trabalho.
- [0:06:19] Paradigma não é linguagem; linguagens multi-paradigma; Python é multi-paradigma.
- [0:06:44] A diferença essencial é o conceito de objeto: dado tem só valor; um conjunto de bits pode significar qualquer coisa.
- [0:07:17] Objetos têm valor, identidade e tipo; mesmo em C a informação de tipo mora no compilador, não no dado.

Princípios enunciados:

- Dado tem apenas valor; símbolo tem significado (0:01:11).
- Tudo que existe na computação são abstrações das naturezas mais elementares da máquina (0:02:00).
- Um paradigma é uma forma de pensar sobre um problema, de organizar as ideias e a abordagem para a solução (0:02:46).
- A sacada da orientação a objetos é dar uma estratégia para organizar dados e código numa mesma unidade de trabalho (0:05:42).
- Paradigma de programação não significa linguagem de programação (0:06:19).
- Objetos têm valor, identidade e tipo (0:07:17).

Código: nenhum. A aula é exposição sem terminal; a única expressão citada é `for food in foods` (0:02:28).

Paráfrases da legenda (não verificadas):

- a distância entre dados e símbolos é gigante porque dado tem apenas valor e símbolos tem significado (0:01:08)
- um paradigma de programação é uma forma que você consegue pensar sobre um problema é como você organiza suas ideias (0:02:44)
- a grande sacada da orientação objetos é exatamente te dar uma estratégia para você organizar dados e código numa mesma unidade de trabalho (0:05:42)
- quando eu falo de objetos os objetos têm valor identidade e tipo e isso muda tudo (0:07:17)

### Aula #02: Demonstração no Terminal

Vídeo: https://www.youtube.com/watch?v=AxFV18iaalg · 273 s

A aula é uma sessão de terminal que materializa o fim da aula #01. Primeiro, um literal binário é lido como inteiro e como caractere para mostrar que dado só tem valor e que o contexto decide o significado. Depois, duas listas com o mesmo conteúdo servem para separar valor, identidade e tipo e para distinguir `==` de `is`. Por fim, `type` devolve a própria classe, que pode ser usada para instanciar.

Linha do tempo:

- [0:00:00] Literal binário com `0b`; o mesmo conjunto de bits é o número 65 em decimal e, criando uma string a partir dele, a letra A.
- [0:00:44] Em assembler [legenda: uma sem glicer] as rotinas que consomem os bits dizem o que eles são; o compilador de C verifica os tipos na sintaxe, mas nada impede violar isso dentro do código.
- [0:01:12] Lista `foods` com três strings; `print(foods)` mostra o valor, `id(foods)` a identidade única, `type(foods)` o tipo.
- [0:01:58] Lista `bag` com o mesmo conteúdo: valor igual, identidade nova, mesmo tipo.
- [0:02:34] Duas listas com o mesmo conteúdo mas distintas; `foods == bag` é verdadeiro porque compara valor.
- [0:03:00] `foods is bag` é falso porque compara identidade; objetos diferentes embora equivalentes.
- [0:03:20] `type` retorna a própria classe `list`, não uma string; `cls = type(foods)` e `cls((1, 2, 3))` instancia uma lista nova.
- [0:03:59] Síntese: tipo é o DNA, a espécie; identidade é quem é o objeto entre todos em memória; valor é o que tem nele quando avaliado.
- [0:04:18] Objetos complexos não têm valor simples: um objeto pessoa tem nome, sobrenome e idade, valores associados ao objeto, os atributos.

Princípios enunciados:

- O mesmo conjunto de bits produz resultados diferentes dependendo do contexto em que é trabalhado (0:00:35).
- Para comparar valor usa-se `==`; para saber se são o mesmo objeto usa-se `is` (0:02:42 e 0:03:03).
- `type` devolve a classe, que é um objeto utilizável, e não um nome (0:03:27).
- Valores associados a um objeto complexo são seus atributos (0:04:29).

Código, reconstruído a partir da narração (ele digita no terminal; a legenda em 0:00:09 registra um um dois três quatro cinco zero e depois número 1, que é a leitura dos dígitos de `0b1000001`):

```python
>>> 0b1000001
65
>>> chr(0b1000001)      # a construção exata da string a partir dos bits não é audível na legenda
'A'
>>> foods = ["apple", "orange", "cat"]   # o terceiro item soa como Cat na legenda (0:02:10)
>>> print(foods); id(foods); type(foods)
>>> bag = ["apple", "orange", "cat"]
>>> foods == bag
True
>>> foods is bag
False
>>> cls = type(foods)
>>> cls((1, 2, 3))
[1, 2, 3]
```

Paráfrases da legenda (não verificadas):

- é o mesmo conjunto de bits só que dependendo do contexto que eu trabalho ele eu vou conseguir um ou outro resultado (0:00:35)
- são objetos diferentes embora são equivalentes (0:03:17)
- o tipo ele é meio que o DNA é qual é a espécie daquele objeto a identidade é quem é o objeto no meio de todos os objetos em memória e o valor é o que tem nesse objeto é quando eu avalio ele (0:03:59)

### Aula #03: Alan Kay

Vídeo: https://www.youtube.com/watch?v=VI7-CFXzlMo · 152 s

A aula mais curta é a que carrega a tese. Alan Kay, pesquisador na Xerox e criador do Smalltalk, pensou objetos como células e como computadores em rede, e em ambas as metáforas o que importa é a comunicação por mensagens, não a unidade em si. Das afirmações do History of Smalltalk sai a imagem que organiza as duas aulas seguintes: a classe é o DNA, o objeto é o organismo vivo, e o código da classe executa no contexto da memória de cada instância.

Linha do tempo:

- [0:00:01] Orientação a objetos foi criada por Alan Kay [legenda: allanquei], pesquisador na Xerox que desenvolveu o Smalltalk; matemático e biólogo.
- [0:00:12] Ideia original: objetos como células, que não acessam o interior umas das outras e se comunicam por troca de mensagens.
- [0:00:22] Segunda metáfora: computadores individuais em rede, que não acessam um ao outro e trocam informações por protocolos combinados.
- [0:00:37] A troca de mensagens é a base da orientação a objetos; não são as classes nem os objetos em si, mas o que está entre os objetos.
- [0:00:53] Unidades independentes que se comunicam através de uma interface bem estabelecida.
- [0:01:03] No History of Smalltalk [legenda: History of Smoke]: tudo é objeto; objetos se comunicam enviando e recebendo mensagens.
- [0:01:21] Cada objeto tem a sua própria memória, no sentido de estado; isso não fica referenciado globalmente, espalhado fora do objeto.
- [0:01:35] Cada objeto é instância de uma classe; sempre há um código DNA anterior ao objeto.
- [0:01:44] A classe armazena o comportamento comum; o objeto é o organismo vivo, a classe é o DNA; o código não se replica em cada objeto.
- [0:02:07] Ao acessar um método, o objeto, sabendo quem é a sua classe, pede para o código da classe executar no contexto da sua própria memória.

Princípios enunciados:

- A base da orientação a objetos é a troca de mensagens, não as classes nem os objetos (0:00:37).
- Objetos são unidades independentes que se comunicam através de uma interface bem estabelecida (0:00:53).
- O estado de um objeto fica no objeto, não referenciado globalmente fora dele (0:01:21).
- O código mora na classe e executa no contexto da instância; não se replica por objeto (0:02:02).

Código: nenhum. Aula expositiva.

Paráfrases da legenda (não verificadas):

- esse processo de troca de mensagens é a base da orientação objetos não são as classes em si não são os objetos em si mas sim como os objetos se relaciona o que está entre os objetos (0:00:37)
- cada objeto tem a sua própria memória memória aqui é no conceito de estado cada objeto sabe como ele está sabe o seu estado interno isso não fica referenciado globalmente espalhado fora do objeto (0:01:21)
- o objeto em si é o organismo vivo a classe é o DNA (0:01:52)

### Aula #04: Classes, atributos e métodos no Python

Vídeo: https://www.youtube.com/watch?v=4jfg5RtiCq0 · 1.252 s

A aula central do curso é uma única sessão de terminal que desmonta a classe Python peça por peça. Começa provando que classes são objetos e que `class` é um comando executável, não uma declaração. Daí deriva a distinção entre atributos de classe e de instância, explicada pela regra do acessor e exposta com `__dict__`. Em seguida mostra por que o inicializador existe (evitar atributos injetados depois e estado inconsistente) e termina decompondo a chamada de método em `__func__`, `__self__` e `__call__`, para mostrar que o método é um objeto que pode ser passado por parâmetro.

Linha do tempo:

- [0:00:00] `class Car: pass` é a classe mais simples; classes em Python são objetos; `Car` é uma variável que referencia o objeto classe.
- [0:00:33] Instanciar com parênteses; a saída distingue a classe no módulo `__main__` da instância com identidade própria.
- [0:00:56] `type(Car())` é `Car`; `type(Car)` é `type`; toda classe no Python 3 é subclasse de `object`; `class Car(object)` é igual a `class Car: pass`.
- [0:02:16] Em Java e C++ [legenda: já você mais mais] `class` declara uma estrutura; em Python é um comando executável.
- [0:02:32] Demonstração: `print`, atribuição, `for` e `if` dentro do corpo da classe, tudo executado na construção do objeto classe.
- [0:05:06] As variáveis locais definidas no corpo da classe são os atributos de classe: `Car.name`, `Car.portas`.
- [0:05:49] Distinção importante: ao acessar `c.name`, verifica-se se a instância possui o atributo; se não, faz-se fallback para a classe.
- [0:06:15] Atribuir `c.name = "BMW"` cria dinamicamente um atributo de instância; a classe não muda; `d = Car()` ainda vê `Ferrari`.
- [0:08:22] `del c.name` faz `c.name` voltar a `Ferrari`; `Car.name = "Fiat"` muda o que as instâncias sem atributo próprio enxergam.
- [0:09:17] Todo objeto tem `__dict__`; o da classe tem `portas` e `name`, o de `c` só `portas`, o de `d` só `name`.
- [0:10:30] Atributo inexistente: busca na instância e em toda a hierarquia até `object`, e dá `AttributeError`.
- [0:10:47] `__class__` liga instância e classe; o acessor, o ponto, já tem a lógica de pesquisar toda a hierarquia.
- [0:11:31] Para não injetar atributos depois de instanciar, o inicializador `__init__(self, model)`; `Car()` sem modelo dá `TypeError`.
- [0:12:46] O inicializador é o melhor lugar para inicializar a instância com seus atributos e valores iniciais.
- [0:12:57] `hasattr(Car, "model")` é falso; injetando `Car.model` e deletando `c.model`, a instância volta a cair na classe.
- [0:13:52] Como a classe também é um objeto, atributo de classe é atributo de instância da classe.
- [0:14:22] Python trata os objetos de forma livre; não existe público e privado, e isso não é necessário no Python.
- [0:14:32] Por que inicializar no `__init__`: `ignition` que cria `motor_running` deixa uma segunda instância sem o atributo, `AttributeError`.
- [0:15:20] Versão correta: `self.motor_running = False` no `__init__`, `ignition` muda para `True`.
- [0:16:14] Método é uma função definida no corpo da classe; o primeiro argumento é `self`, o `this` de outras linguagens, explícito em Python.
- [0:16:52] `d.ignition()` é açúcar sintático para `Car.ignition(d)`: a instância é passada como primeiro argumento.
- [0:17:09] `Car.ignition` é uma função; `d.ignition` é um bound method, outro tipo de objeto.
- [0:17:42] `m = d.ignition` tem `__call__`, `__class__`, `__func__` e `__self__`; o método sabe a função que envelopa e a instância.
- [0:19:26] Como o método é objeto, pode ser passado por parâmetro: `f(d.ignition)` executa e o efeito colateral aparece em `d.motor_running`.
- [0:20:32] Fecho: não se programa fazendo coisas tão sutis, mas o objetivo é tirar o que se sabe de Java, PHP e C++ e olhar o Python com olhar novo.

Princípios enunciados:

- Classes em Python são objetos, e o nome da classe é uma variável que referencia esse objeto (0:00:22).
- `class` é um comando executável, não uma instrução declarativa (0:02:25).
- Atributos de instância ficam na frente dos atributos de classe; o acessor pergunta na hierarquia toda (0:09:05).
- O inicializador é o melhor lugar para inicializar a instância com seus atributos e valores iniciais (0:12:51).
- Inicializar o estado no `__init__` evita inconsistência no estado do objeto (0:15:20).
- Não existe público e privado, e isso não é necessário no Python (0:14:25).
- Em Python o `self` é explícito porque a chamada de método é açúcar sintático sobre uma função da classe (0:16:30).
- Tudo é objeto: classe, instância, função e método (0:17:11).
- Tire o que você conhece de Java, PHP e C++ sobre classes e objetos e olhe o Python com olhar completamente novo (0:20:40).

Código, reconstruído a partir da narração. Nomes de variáveis são os que a legenda registra (`Car`, `c`, `d`, `name`, `portas`, `model`, `ignition`, `motor_running`, `m`, `f`, `g`); mensagens de `print` são aproximadas.

```python
# 0:00:00 a 0:02:10
class Car:
    pass

Car()                       # instância com identidade própria
type(Car())                 # Car
type(Car)                   # type
issubclass(Car, object)     # True
class Car(object): pass     # idêntico a class Car: pass

# 0:02:32 a 0:05:05, a classe como comando executável
class Car:
    print("loading class")
    name = "Ferrari"
    print("defining " + name + "!" * 5)
    for char in name:
        print(char.upper())
    if len(name) % 2 == 0:
        portas = 2
    else:
        portas = 3
    print(portas)           # 3, porque Ferrari tem sete letras

# 0:05:27 a 0:11:14, atributos de classe e de instância
Car.name, Car.portas        # Ferrari, 3
c = Car(); c.name, c.portas # Ferrari, 3 por fallback
c.name = "BMW"; c.portas = 2
d = Car(); d.name, d.portas # Ferrari, 3
d.name = "Audi"
del c.name; c.name          # Ferrari
Car.name = "Fiat"; c.name, d.name   # Fiat, Audi
Car.__dict__; c.__dict__; d.__dict__
c.xpto                      # AttributeError
c.__class__.name

# 0:11:31 a 0:14:20, o inicializador
class Car:
    name = "Ferrari"
    def __init__(self, model):
        self.model = model

Car()                       # TypeError, falta model
c, d = Car("F50"), Car("F40")
hasattr(Car, "model")       # False
Car.model = "Top Gear"; del c.model; c.model   # Top Gear por fallback

# 0:14:32 a 0:16:14, por que inicializar no __init__
class Car:
    name = "Ferrari"
    def ignition(self):
        print("...")
        self.motor_running = True

c = Car(); c.ignition(); c.motor_running   # True
d = Car(); d.motor_running                 # AttributeError

class Car:
    def __init__(self):
        self.motor_running = False
    def ignition(self):
        self.motor_running = True
        print("...")

# 0:16:14 a 0:20:30, o método como objeto
d = Car()
d.ignition()                # açúcar sintático para
Car.ignition(d)
m = d.ignition              # bound method
m.__func__ is Car.ignition  # True
m.__self__ is d             # True
m()                         # equivale a m.__func__(m.__self__)

def f(g):
    g()
f(d.ignition)               # d.motor_running vira True
```

Paráfrases da legenda (não verificadas):

- a palavra Car é uma variável que referencia o objeto classe no runtime memória [legenda: han time] (0:00:28)
- no Python não é só uma instrução declarativa classe é um comando executável (0:02:25)
- atributos de instância não sobrescrevem atributos da classe (0:07:32)
- o ideal é inicializar o cara lá no __init__ [legenda: dandarenite] porque aí eu evito esse tipo de inconsistência no estado do meu objeto (0:15:20)
- tudo é objeto classe objeto instância objeto função objeto e método é objeto (0:17:11)

### Aula #05: Herança no Python

Vídeo: https://www.youtube.com/watch?v=PZTr4c86y7g · 215 s

A aula fecha o curso com o mínimo de herança: uma `Ferrari` que herda de `Car`, chama `super().__init__` e ganha um atributo próprio. A lição técnica é que o Python não chama o método da classe base por conta própria; a lição conceitual, dita nos últimos quarenta segundos, é que orientação a objetos não se confunde com criar classes, e que a maleabilidade do Python está em definir relações entre objetos.

Linha do tempo:

- [0:00:00] `class Car` com `portas = 2` como atributo de classe e `__init__(self, name)` guardando `self.name`.
- [0:00:21] `class Ferrari(Car)` com `__init__(self, model)` que chama `super().__init__("Ferrari")` e guarda `self.model`.
- [0:00:48] O `__init__` do `super()` resolve para `Car`; `name` vira atributo de instância; `portas` é atributo de classe de `Car`; `Ferrari` não tem atributos de classe.
- [0:01:20] `f = Ferrari("F50")`: `f.name` e `f.model` são de instância, `f.portas` é de classe; `f.__dict__` tem só os dois de instância; `Ferrari.__dict__` não tem nenhum deles; `Car.__dict__` tem `portas`.
- [0:01:58] Herança em Python é super simples: na declaração da classe, parênteses com a classe base.
- [0:02:09] O Python não chama automaticamente o método da classe base; sem a chamada explícita, o `__init__` de `Ferrari` substitui completamente o de `Car`; você controla se chama antes ou depois; vale para qualquer método.
- [0:02:38] `super` é especial e geralmente incompreendido, mas extremamente necessário: nele está a lógica de resolver qual método das classes anteriores executa, porque Python suporta herança múltipla.
- [0:02:57] Fecho: orientação a objetos em Python é muito mais flexível e maleável do que o popular; não confundir objetos com criar classes; como tudo é objeto, há sempre a oportunidade de definir melhores relações entre os objetos; esse é o segredo da maleabilidade e de usar vários paradigmas em conjunto.

Princípios enunciados:

- O Python não chama o método da classe base automaticamente; a chamada a `super()` é explícita e você decide quando (0:02:09).
- `super()` carrega a resolução de qual método das classes anteriores executa, por causa da herança múltipla (0:02:42).
- Não confundir orientação a objetos com criar classes (0:03:09).
- A maleabilidade do Python está em definir melhores relações entre os objetos que compõem o programa (0:03:14).

Código, reconstruído a partir da narração:

```python
class Car:
    portas = 2
    def __init__(self, name):
        self.name = name

class Ferrari(Car):
    def __init__(self, model):
        super().__init__("Ferrari")
        self.model = model

f = Ferrari("F50")
f.name, f.model, f.portas   # Ferrari, F50, 2
f.__dict__                  # {'name': 'Ferrari', 'model': 'F50'}
Ferrari.__dict__            # sem name, model ou portas
Car.__dict__                # com portas
```

Paráfrases da legenda (não verificadas):

- o Python não chama automaticamente o seu método da classe base você tem que explicitamente chamar ele (0:02:12)
- o super é um cara especial e geralmente incompreendido mas ele é extremamente necessário (0:02:38)
- a gente não pode confundir objetos com criar classes como tudo em Python é objeto a todo momento você tem a oportunidade de definir melhores relações entre os objetos que compõem o seu programa (0:03:09)

## 6. Princípios que atravessam toda a série

Dez regras que ele formula na fala. Nenhuma é inferência deste documento; cada uma traz a aula e o timestamp onde é dita.

#### 1. Dado tem valor; símbolo tem significado

A abstração existe para que o programador trabalhe no nível simbólico, e a linguagem é a camada que aproxima o código desse nível (aula #01, 0:01:11 e 0:01:57).

#### 2. Paradigma é uma forma de pensar, não uma linguagem

Um paradigma é como você organiza suas ideias e a abordagem para a solução (aula #01, 0:02:46); paradigma de programação não significa linguagem de programação, e Python é multi-paradigma (aula #01, 0:06:19 a 0:06:35).

#### 3. Objeto é código e dado na mesma unidade

A sacada da orientação a objetos é organizar dados e código numa mesma unidade de trabalho, em vez de tratar dados como coleções acessórias manipuladas durante a execução (aula #01, 0:05:42 a 0:06:07).

#### 4. Objeto tem valor, identidade e tipo

Dado tem apenas valor; objetos têm valor, identidade e tipo (aula #01, 0:07:17). `==` compara valor, `is` compara identidade; dois objetos podem ser equivalentes sem ser o mesmo (aula #02, 0:02:42 a 0:03:20).

#### 5. A base da orientação a objetos é a troca de mensagens

Não são as classes em si nem os objetos em si, mas como os objetos se relacionam, o que está entre os objetos (aula #03, 0:00:37). Unidades independentes que se comunicam por uma interface bem estabelecida (aula #03, 0:00:53).

#### 6. O estado mora no objeto

Cada objeto tem a sua própria memória, no sentido de estado, e isso não fica referenciado globalmente, espalhado fora do objeto (aula #03, 0:01:21).

#### 7. A classe é o DNA; o código não se replica por objeto

A classe armazena o comportamento comum, o objeto é o organismo vivo, e o código da classe executa no contexto da memória de cada instância (aula #03, 0:01:44 a 0:02:26). Em Python isso aparece como `Car.ignition(d)` por baixo de `d.ignition()` (aula #04, 0:16:52).

#### 8. Inicialize o estado no `__init__`

O inicializador é o melhor lugar para dar à instância seus atributos e valores iniciais (aula #04, 0:12:51). Criar atributos em outros métodos deixa instâncias em estado inconsistente, e a demonstração é um `AttributeError` em `d.motor_running` (aula #04, 0:14:32 a 0:15:20).

#### 9. Chame a classe base explicitamente

O Python não chama automaticamente o método da classe base; sem `super().__init__`, o método da subclasse substitui completamente o da base, e é o programador que decide se chama antes ou depois (aula #05, 0:02:09 a 0:02:35).

#### 10. Orientação a objetos não é criar classes

Não se pode confundir objetos com criar classes; como tudo é objeto, a todo momento há a oportunidade de definir melhores relações entre os objetos que compõem o programa (aula #05, 0:03:09 a 0:03:21). O mesmo espírito do fecho da aula #04: desaprender Java, PHP e C++ e olhar o Python com olhar novo (aula #04, 0:20:40).

## 7. Citações-chave do curso

Paráfrases de legenda automática, sem aspas e não verificadas contra o vídeo. Mis-hearings evidentes anotados entre colchetes.

| Aula | Timestamp | Paráfrase |
|---|---|---|
| #01 | 0:00:05 | quando eu falo programação orientada a objetos fica uma grande interrogação no ar que raios é isso e será que todo mundo quer dizer a mesma coisa |
| #01 | 0:01:11 | a distância entre dados e símbolos é gigante porque dado tem apenas valor e símbolos tem significado |
| #01 | 0:02:00 | tudo que existe na computação são abstrações de dados abstrações das naturezas mais elementares da máquina |
| #01 | 0:05:42 | a grande sacada da orientação objetos é exatamente te dar uma estratégia para você organizar dados e código numa mesma unidade de trabalho |
| #01 | 0:06:19 | paradigma de programação não significa linguagem de programação |
| #01 | 0:07:17 | os objetos têm valor identidade e tipo e isso muda tudo |
| #02 | 0:03:17 | são objetos diferentes embora são equivalentes |
| #02 | 0:03:59 | o tipo ele é meio que o DNA é qual é a espécie daquele objeto |
| #03 | 0:00:37 | esse processo de troca de mensagens é a base da orientação objetos não são as classes em si não são os objetos em si mas sim como os objetos se relaciona o que está entre os objetos |
| #03 | 0:01:21 | cada objeto tem a sua própria memória memória aqui é no conceito de estado isso não fica referenciado globalmente espalhado fora do objeto |
| #03 | 0:01:52 | o objeto em si é o organismo vivo a classe é o DNA |
| #04 | 0:02:25 | no Python não é só uma instrução declarativa classe é um comando executável |
| #04 | 0:07:32 | atributos de instância não sobrescrevem atributos da classe |
| #04 | 0:14:25 | não existe esse negócio de público privado na verdade isso não é necessário no Python |
| #04 | 0:15:20 | o ideal é inicializar o cara lá no __init__ [legenda: dandarenite] porque aí eu evito esse tipo de inconsistência no estado do meu objeto |
| #04 | 0:17:11 | tudo é objeto classe objeto instância objeto função objeto e método é objeto |
| #04 | 0:20:40 | tirar tudo que você conhece de Java de PHP de C++ [legenda: ser mais mais] enquanto classes e objeto e olhar para o Python com olhar completamente novo |
| #05 | 0:02:12 | o Python não chama automaticamente o seu método da classe base você tem que explicitamente chamar ele |
| #05 | 0:03:09 | a gente não pode confundir objetos com criar classes |

## 8. A evolução técnica, aula a aula

| Etapa | O que é feito | Conceito ou ferramenta | O que isso destrava |
|---|---|---|---|
| **#01** | Exposição dos níveis de programação e da sucessão dos paradigmas (0:00:23 a 0:06:44) | Abstração; imperativo, procedural, estruturado, funcional, orientado a objetos | A motivação: por que organizar código e dado juntos (0:05:42) e o que é um objeto (0:07:17) |
| **#02** | Sessão de terminal com literal binário e duas listas (0:00:00 a 0:04:32) | `0b`, `print`, `id`, `type`, `==`, `is`, instanciar a partir de `type(x)` | Valor, identidade e tipo deixam de ser definição e viram saída de terminal |
| **#03** | Exposição sobre Alan Kay e o History of Smalltalk (0:00:01 a 0:02:29) | Células, rede, troca de mensagens, classe como DNA | O vocabulário para ler as aulas #04 e #05: instância, classe, método executando no contexto da instância |
| **#04** | `class Car` aberto no terminal, do `pass` ao bound method (0:00:00 a 0:20:49) | `class` executável, `__dict__`, `__class__`, fallback do acessor, `__init__`, `hasattr`, `del`, `__func__`, `__self__`, `__call__` | Atributo de classe versus de instância; estado inicializado no `__init__`; método como objeto passável |
| **#05** | `class Ferrari(Car)` com `super().__init__` (0:00:00 a 0:02:55) | Herança por parênteses; `super()`; onde cada atributo mora no `__dict__` | A chamada explícita da base e a tese final: orientação a objetos não é criar classes (0:03:09) |

## 9. Arsenal técnico demonstrado no curso

| Técnica ou recurso | Para que ele usa | Aula e timestamp |
|---|---|---|
| Literal binário `0b` | Mostrar que os mesmos bits são 65 ou A conforme o contexto | #02, 0:00:04 |
| `print`, `id`, `type` | Exibir valor, identidade e tipo de um objeto | #02, 0:01:26 a 0:01:53 |
| `==` e `is` | Comparar valor versus comparar identidade | #02, 0:02:42 e 0:03:03 |
| `cls = type(x); cls(...)` | Provar que `type` devolve a classe e que a classe instancia | #02, 0:03:34 |
| `class X: pass` | A classe mais simples; classe como objeto | #04, 0:00:00 |
| `type(Car)` e `issubclass(Car, object)` | Toda classe é instância de `type` e subclasse de `object` | #04, 0:01:14 a 0:01:32 |
| `print`, `for`, `if` no corpo da classe | Provar que `class` é um comando executável | #04, 0:02:32 a 0:03:47 |
| Atribuição e `del` em atributos de instância | Mostrar que a instância fica na frente da classe e cai nela por fallback | #04, 0:06:15 a 0:09:05 |
| `__dict__` | Ver onde cada atributo mora | #04, 0:09:17; #05, 0:01:38 |
| `__class__` | Ver como a instância encontra a classe | #04, 0:10:47 |
| `AttributeError` e `TypeError` | O acessor chega em `object` e falha; o `__init__` exige argumento | #04, 0:10:30 e 0:12:09 |
| `__init__(self, ...)` | Inicializar a instância com seus atributos | #04, 0:11:35 e 0:15:30 |
| `hasattr` | Confirmar que `model` não existe na classe | #04, 0:12:57 |
| `Car.ignition(d)` como forma de `d.ignition()` | Explicar o `self` explícito | #04, 0:16:52 |
| `__func__`, `__self__`, `__call__` do bound method | Decompor a chamada de método | #04, 0:17:42 a 0:19:21 |
| Método passado como argumento | Mostrar o método como objeto de primeira classe | #04, 0:19:35 |
| `class Ferrari(Car)` e `super().__init__(...)` | Herança e chamada explícita da base | #05, 0:00:21 a 0:00:48 |

## 10. Glossário do curso

| Termo | Significado no contexto da série | Onde |
|---|---|---|
| **Baixo nível** | O nível mais próximo do computador: bits, controle de para onde o elétron passa | #01, 0:00:27 |
| **Alto nível** | O nível do ser humano: palavras, conceitos, ideias | #01, 0:00:37 |
| **Dado** | Aquilo que tem apenas valor; um conjunto de bits sem informação sobre o que é | #01, 0:01:11 e 0:06:57 |
| **Símbolo** | Aquilo que tem significado | #01, 0:01:11 |
| **Abstração** | Camada que liga o mundo dos dados ao mundo dos símbolos; tudo na computação é abstração | #01, 0:01:57 |
| **Paradigma** | Forma de pensar sobre um problema e organizar a abordagem para a solução | #01, 0:02:46 |
| **Imperativo** | Paradigma da ordem, do comando, próximo do metal | #01, 0:03:01 |
| **Procedural** | Sub-rotinas, condições e saltos entre trechos de código | #01, 0:03:49 |
| **Estruturado** | Estruturas de controle de fluxo e variáveis locais; C | #01, 0:04:30 |
| **Declarativo, funcional** | Evita controle de fluxo; trata tudo como expressões e funções | #01, 0:05:06 |
| **Multi-paradigma** | Linguagem que traz elementos de vários paradigmas; Python | #01, 0:06:32 |
| **Valor** | O que tem no objeto quando ele é avaliado | #02, 0:04:12 |
| **Identidade** | Quem é o objeto no meio de todos os objetos em memória | #02, 0:04:05 |
| **Tipo** | O DNA, a espécie do objeto | #02, 0:03:59 |
| **Atributo** | Valor associado a um objeto complexo (nome, sobrenome, idade) | #02, 0:04:29 |
| **Troca de mensagens** | A base da orientação a objetos; o que está entre os objetos | #03, 0:00:37 |
| **Memória do objeto** | O estado interno, que não fica referenciado globalmente | #03, 0:01:21 |
| **Classe** | O DNA: onde fica o comportamento comum a cada instância; em Python, um objeto criado por um comando executável | #03, 0:01:44; #04, 0:02:25 |
| **Instância** | O organismo vivo criado a partir da classe | #03, 0:01:52 |
| **Atributo de classe** | Variável local definida no corpo da classe | #04, 0:05:18 |
| **Atributo de instância** | Atributo criado dinamicamente na instância; fica na frente do atributo de classe | #04, 0:06:55 e 0:09:05 |
| **Fallback** | Quando a instância não tem o atributo, o acessor pergunta à classe e à hierarquia | #04, 0:06:06 |
| **Acessor** | O ponto; tem a lógica de pesquisar o atributo em toda a hierarquia | #04, 0:11:17 |
| **`__dict__`** | Atributo especial que guarda os atributos de qualquer objeto | #04, 0:09:21 |
| **Inicializador (`__init__`)** | Método onde a instância recebe seus atributos e valores iniciais | #04, 0:11:37 e 0:12:51 |
| **Método** | Função definida no corpo da classe cujo primeiro argumento é `self` | #04, 0:16:14 |
| **`self`** | O `this` de outras linguagens, explícito em Python | #04, 0:16:24 |
| **Bound method** | Objeto que envelopa a função da classe (`__func__`) e a instância (`__self__`) | #04, 0:17:25 e 0:18:08 |
| **Herança** | Passar a classe base entre parênteses na declaração | #05, 0:02:01 |
| **`super()`** | Onde está a lógica de resolver qual método das classes anteriores executa | #05, 0:02:46 |

## 11. Perguntas e respostas que o curso responde

#### O que um objeto tem que um dado não tem?

Valor, identidade e tipo. Dado é só valor; o contexto diz o que ele significa (aula #01, 0:06:57 a 0:07:22). No terminal: `print`, `id` e `type` (aula #02, 0:01:26 a 0:01:53).

#### Qual a diferença entre `==` e `is`?

`==` compara valor: duas listas com o mesmo conteúdo são equivalentes. `is` compara identidade: são objetos diferentes (aula #02, 0:02:42 a 0:03:20).

#### Por que ele diz que a sacada da orientação a objetos não são os objetos?

Porque, para Alan Kay, a base é a troca de mensagens: unidades independentes que não acessam o interior umas das outras e se comunicam por uma interface bem estabelecida (aula #03, 0:00:12 a 0:01:01).

#### Em Python, `class` declara ou executa?

Executa. O corpo da classe roda comando por comando na construção do objeto classe, e as variáveis locais que sobram viram atributos de classe (aula #04, 0:02:25 a 0:05:23).

#### O que acontece quando eu atribuo `c.name` em uma instância?

Cria-se um atributo de instância que fica na frente do atributo de classe; a classe não muda e as outras instâncias continuam vendo o valor da classe (aula #04, 0:06:49 a 0:07:45). `del` na instância faz o acessor voltar a cair na classe (0:08:35).

#### Como o Python encontra um atributo?

Pelo `__dict__` da instância; se não está lá, pelo `__dict__` da classe e da hierarquia até `object`; se não encontra, `AttributeError` (aula #04, 0:09:17 a 0:10:44).

#### Por que inicializar tudo no `__init__`?

Porque um atributo criado em outro método só existe nas instâncias em que aquele método rodou; a segunda instância dá `AttributeError`, um estado inconsistente (aula #04, 0:14:32 a 0:15:28).

#### Por que o `self` é explícito?

Porque `d.ignition()` é açúcar sintático para `Car.ignition(d)`: a instância é passada como primeiro argumento à função definida na classe (aula #04, 0:16:30 a 0:17:06).

#### O que é um bound method?

Um objeto que sabe a função que envelopa (`__func__`) e a instância (`__self__`); chamá-lo é `__func__(__self__)`. Por ser objeto, pode ser passado por parâmetro (aula #04, 0:17:25 a 0:20:25).

#### A classe filha chama o `__init__` da mãe sozinha?

Não. Sem `super().__init__`, o método da filha substitui completamente o da mãe; você decide se chama e quando (aula #05, 0:02:09 a 0:02:35).

#### Existe público e privado em Python?

Não, e segundo ele não é necessário (aula #04, 0:14:22).

#### Orientação a objetos é criar classes?

Não. Como tudo em Python é objeto, o trabalho é definir melhores relações entre os objetos que compõem o programa (aula #05, 0:03:09 a 0:03:21).

## 12. Repositórios e recursos

| Recurso | Onde encontrar | Observação |
|---|---|---|
| Playlist completa (fonte desta documentação) | [Raio X da Orientação a Objetos](https://www.youtube.com/playlist?list=PLeKXYyZCJHxdT8vUW3x9bd7B8PnwnHINW) | 5 vídeos; ids `a9LXgufi1e4`, `AxFV18iaalg`, `VI7-CFXzlMo`, `4jfg5RtiCq0`, `PZTr4c86y7g`. |
| Canal | [HB Network](https://www.youtube.com/@hbnetworkoficial) | |
| The Early History of Smalltalk, Alan Kay | citado como History of Smalltalk na aula #03, 0:01:03 | Única referência externa que o curso cita. Ele não dá link nem edição. |
| Série longa sobre o mesmo tema | `kb/courses/oo-na-pratica.md` | Orientação a Objetos na Prática desenvolve em 23 aulas o que esta série resume; a troca de mensagens (seção 3.2 lá) e o arco histórico (seção 4 lá) são os pontos de contato. |

Repositório do instrutor para esta série: **nenhum**. As cinco transcrições não citam repositório, gist, documento ou arquivo; o código das aulas #02, #04 e #05 é digitado no interpretador interativo e não é salvo em lugar algum que a aula mencione. Esta documentação não verificou o GitHub do autor além das transcrições, e não lista reimplementações de comunidade para este curso.

## 13. Análise linha a linha do código real

Não há código publicado para esta série, portanto não há análise de código real. O que existe é o que ele digita ao vivo no terminal nas aulas #02, #04 e #05, e esse código está reconstruído na seção 5, aula por aula, marcado como reconstrução a partir da narração. Três limites dessa reconstrução ficam registrados:

- As mensagens dos `print` dentro de `ignition` (aula #04, 0:14:51 e 0:15:56) não são audíveis na legenda e aparecem como `"..."`.
- A forma exata como ele constrói a string a partir dos bits na aula #02 (0:00:29) não é audível; `chr(0b1000001)` é uma escolha deste documento para produzir o resultado que ele descreve, a letra A.
- O terceiro item das listas da aula #02 soa como Cat na legenda (0:02:10) e é mantido assim.

## 14. Execução real dos testes

O curso não publicou código nem testes, portanto não há suíte a executar. Em vez disso, as reconstruções da seção 5 foram executadas em Python 3.9.6 nesta sessão para confirmar que se comportam como ele narra. Cada linha abaixo é saída real de terminal:

| Comportamento narrado | Aula e timestamp | Resultado da execução |
|---|---|---|
| `0b1000001` é 65 e, como caractere, A | #02, 0:00:17 a 0:00:33 | `65`, `'A'` |
| Duas listas iguais: `==` verdadeiro, `is` falso, ids diferentes | #02, 0:02:56 e 0:03:07 | `True`, `False`, ids diferentes |
| `type(foods)` é a classe `list` e instancia `[1, 2, 3]` | #02, 0:03:34 a 0:03:59 | `True`, `[1, 2, 3]` |
| O corpo da classe executa `print`, `for` e `if`; `portas` vira 3 | #04, 0:03:47 a 0:05:05 | o corpo rodou na ordem narrada e `portas == 3` |
| `type(Car) is type` e `issubclass(Car, object)` | #04, 0:01:14 a 0:01:32 | `True`, `True` |
| Atributo de instância na frente; classe intacta; outra instância cai na classe | #04, 0:06:15 a 0:07:45 | `('BMW', 2)`, `('Ferrari', 3)`, `('Ferrari', 3)` |
| `del c.name` volta a `Ferrari`; `Car.name = "Fiat"` muda `c.name`, não `d.name` | #04, 0:08:22 a 0:09:05 | `Ferrari`; `Fiat`, `Audi` |
| `c.__dict__` só com `portas`, `d.__dict__` só com `name` | #04, 0:09:41 a 0:09:52 | `{'portas': 2}`, `{'name': 'Audi'}` |
| `c.xpto` dá `AttributeError` | #04, 0:10:42 | `'Car' object has no attribute 'xpto'` |
| `Car()` sem `model` dá `TypeError` | #04, 0:12:06 | `__init__() missing 1 required positional argument: 'model'` |
| `hasattr(Car, "model")` falso; após `del c.model`, fallback para `Car.model` | #04, 0:12:57 a 0:13:38 | `False`; `Top Gear` |
| `d.motor_running` sem `__init__` dá `AttributeError` | #04, 0:15:12 | `'Car3' object has no attribute 'motor_running'` |
| `Car.ignition` é função; `d.ignition` é método | #04, 0:17:19 a 0:17:28 | `function`, `method` |
| `m.__func__ is Car.ignition` e `m.__self__ is d`; `m.__func__(m.__self__)` liga o motor | #04, 0:18:08 a 0:19:21 | `True`, `True`; `True` |
| `f(d.ignition)` liga o motor por efeito colateral | #04, 0:19:57 a 0:20:25 | `True` |
| `Ferrari("F50")`: `name`, `model` na instância, `portas` na classe `Car` | #05, 0:01:20 a 0:01:58 | `Ferrari F50 2`; `f.__dict__ == {'name': 'Ferrari', 'model': 'F50'}`; `portas` só em `Car.__dict__` |
| Sem `super().__init__`, a instância não tem `name` | #05, 0:02:09 a 0:02:29 (ele descreve, não executa) | `'Ferrari2' object has no attribute 'name'` |

Uma observação que a aula não faz: a variável `char` do `for` dentro do corpo da classe (aula #04, 0:03:05) também sobra como atributo de classe, e aparece em `Car.__dict__` ao lado de `name` e `portas`. Ele lê o `__dict__` em 0:09:29 e menciona apenas `__module__`, `__weakref__`, `portas` e `name`.

O script de verificação ficou fora do repositório; nada do que ele produz é código do curso.

---

Documentação elaborada a partir das transcrições automáticas das 5 aulas da playlist Raio X da Orientação a Objetos, de Henrique Bastos (HB Network), playlist `PLeKXYyZCJHxdT8vUW3x9bd7B8PnwnHINW`, legendas em português (pt-orig) capturadas em 2026-10-08. As citações são paráfrases das legendas automáticas, não verificadas contra o vídeo (`verified: false`), renderizadas sem aspas e com os erros de reconhecimento de fala anotados entre colchetes quando precisam aparecer. O curso não publicou repositório, gist, documento ou teste; todo o código desta documentação é reconstrução a partir da narração, marcada como tal na seção 5, e a seção 14 registra a execução dessas reconstruções em Python 3.9.6 nesta sessão. Datas de publicação e visualizações não foram coletadas. Conteúdo de caráter educativo.
