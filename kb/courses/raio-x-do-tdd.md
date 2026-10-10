<!-- written by the henrique-ingest distiller on 2026-10-09 from sources/transcripts/raio-x-do-tdd/; see kb/courses/README.md for provenance and license -->

HB Network · Documentação de curso

# Raio-X do Test-Driven Development

As 5 aulas, do mantra de testar o tempo todo ao framework de testes, lidas aula a aula a partir das legendas automáticas. O código é digitado ao vivo no PyCharm e no terminal. Nenhum repositório é falado.

Instrutor: **Henrique Bastos** · Canal [HB Network](https://www.youtube.com/@hbnetworkoficial) · Playlist: [Raio-X do Test-Driven Development](https://www.youtube.com/playlist?list=PLeKXYyZCJHxe1X_B-o5bMDyNLxIBQB1q7) · Repositório: nenhum URL nesta série

Documento elaborado a partir das transcrições automáticas das 5 aulas (legendas em português, pt-orig, capturadas em 2026-10-09). O título da aula #04 chegou em inglês no `playlist.json`. O código desta documentação é reconstrução a partir da narração.

## 1. Visão geral do curso

Raio-X do Test-Driven Development é uma série de **5 aulas** que somam **8.192 segundos, 2 horas, 16 minutos e 32 segundos**. A aula #01 monta o motivo: entregar software é delicado, código sem teste é risco, e o mantra que a legenda ouve como Dafiti é testar o tempo inteiro, de forma automática (0:13:27, 0:13:38, 0:14:10). A aula #02 reduz um teste ao comando que a legenda chama de acerte: verdadeiro não faz nada, falso levanta exceção, e todo test runner se baseia nisso (0:01:42, 0:02:51). A aula #03 é o kata do fiz bus, passo a passo, com a distinção entre erro e falha (0:08:03). A aula #04 repete o mesmo ciclo nos números felizes, do teste do 1 até uma versão recursiva. A aula #05 abre o acerte que para no primeiro erro, escreve um helper que roda todos, e só então entra no módulo que a legenda chama de unit test e no framework que ela chama de Jungle.

| Dimensão | Valor | Observação |
|---|---|---|
| Aulas | 5 | Playlist completa, numerada de #01 a #05. |
| Duração total | 8.192 s (2h 16min 32s) | Soma das durações em `playlist.json`. |
| Aula mais curta / mais longa | 221 s (#02) / 2.736 s (#03) | A #03, o kata, é 33% do curso. |
| Datas de publicação | não coletadas | O `playlist.json` desta coleta traz id, título e duração. |
| Visualizações | não coletadas | Idem. |
| Transcrições | 5 de 5 disponíveis | Legenda automática em português (pt-orig); não há legenda humana. |
| Código do curso | nenhum publicado | As cinco transcrições não citam GitHub, URL nem repositório. O eventex aparece só como exemplo de onde o Jungle acha um teste (aula #05, 0:27:09). |
| Bloco prático | aulas #02 a #05 | Acerto no terminal, kata do fiz bus, números felizes, helper e unit test. |

Nota de método: cada afirmação traz aula e timestamp. As citações são paráfrases de legenda, sem aspas, não verificadas contra o vídeo. Mis-hearings ficam entre colchetes. A palavra que a legenda escreve acerte, A7 e chamada 7 é a leitura deste documento para o `assert` do Python; ele não soletra assert. Pai Charme é o PyCharm, pelo contexto de IDE, refactor rename e column selection. Unit test e Jungle são os nomes ouvidos para a biblioteca padrão e para o framework web; pytest não é nomeado. A seção 14 executa só o fragmento da aula #02 e os restos da aula #03, que a narração sustenta.

## 2. Filosofia e método de ensino

### 2.1 A coragem que ele pede é a prudência

Entregar software é delicado, e a tarefa não pode ser subestimada (aula #01, 0:02:05). O maior risco que ele nomeia é o esquema de proteger o próprio traseiro, ouvido como cover your S (0:01:33). A grande coragem, frase que ele atribui a Eurípedes, é a prudência (0:15:01). O programador corajoso faz big design up front e carrega pedra (0:15:43, 0:16:23). O prudente rascunha, camada por camada, e sobe a complexidade vendo o todo funcionar (0:16:48, 0:17:05).

### 2.2 Testar o tempo todo, e de forma automática

A solução que ele anuncia é atacar o desperdício (aula #01, 0:12:56). A legenda ouve o nome do mantra como Dafiti e, em seguida, teste all the fucking all the fucking o tempo inteiro (0:13:27, 0:13:30). Código sem teste é um risco para a sociedade (0:13:38). Teste manual não escala; tem que ser automático (0:14:10). Teste funcional, unitário, de carga e de aceitação são repertório; o importante é a essência do porquê testar (0:14:38, 0:14:46). O termo, na legenda, foi cunhado pelo Brian Lions (0:13:47). As quatro letras do título da aula não são soletradas.

### 2.3 O kata é treino de movimento, não a peça pronta

Kata, ouvido como catar, significa forma: os movimentos de artes marciais, passo a passo, vagarosamente, o mais simples possível (aula #03, 0:02:37). No kata a gente rouba, porque o teste garante, e o teste esculpe o código pela demanda (0:09:48). O fecho compara com guitarra devagar e metrônomo [legenda: metrô], para internalizar o movimento e, na batalha, entregar software que gera valor (0:44:55).

### 2.4 Crescer por incisão, sem apagar o que ainda não foi substituído

Com o teste passando, ou se faz um teste novo ou se melhora o código (aula #03, 0:08:42). A generalização entra por incisão: o retorno novo vai antes do bloco velho, o bloco de baixo deixa de executar, e só então se apaga (0:13:33). Não se comenta um bloco grande e não se apaga antes de ver o substituto funcionando, para não se perder em control Z (0:28:56). Na aula #04, antes de se perder atrás do porquê, dá-se um passo para trás e se estabiliza (0:17:05).

### 2.5 O dojo é o lugar em que o código emerge

A aula #04 existe para mostrar a dinâmica de um coding dojo [legenda: caldinho Dojo]: a dúvida dos e-mails é o código emergir durante o dojo (0:00:10). No fim ele pede comentário, e diz que essa conversa é a parte mais importante (0:30:48).

## 3. Pilares conceituais

### 3.1 De trás para frente: o valor está no output

Todo software é input, processamento e o que a legenda chama de altitude (aula #01, 0:18:32). Para o cliente só o output tem valor; input e processamento são custo (0:19:26). O prudente parte do problema resolvido e constrói de trás para frente (0:21:18). Escrever o teste expressa o que se está entendendo, e os testes que importam evidenciam a silhueta do problema (0:24:21, 0:25:05). O círculo de olhar o output, estabelecer o teste e criar o código que passa é o que a legenda chama de tdd, teste drive and (0:26:47). A frase corta em and.

### 3.2 A essência de um teste é o acerte

Para fazer um teste, dizer o que se espera quando executar (aula #02, 0:00:28). O comando acerte avalia a expressão: se é verdadeira, não faz nada; se é falsa, levanta exceção (0:01:42, 0:01:50). Vale para qualquer expressão de valor lógico falso, não só para o literal falso: lista vazia e string vazia também (0:02:03, 0:02:12). Todo mecanismo de teste, todo executor e o test runner, em várias linguagens e no Python, se baseia nesse comando (0:02:51). Dá para desenvolver com teste usando só o acerto, sem biblioteca (0:03:32).

### 3.3 Erro e falha não são a mesma coisa

Quando a expectativa não é atendida, a legenda chama de seixa nela e de falha (aula #03, 0:07:25). Quando alguma coisa explode no código, é erro (0:07:52). Resolver um erro é sempre mais prioritário do que resolver uma falha (0:08:03). A aula #04 repete os dois estados: exceção é erro; o acerte que retorna falso é falha (0:04:35). A aula #05 mostra o relatório: trocar end por or produz falhas; um nome indefinido produz erros (0:20:17, 0:20:42).

### 3.4 Confiança nos limites, não cobertura combinatória

TDD não é análise combinatória de tudo que é possível imaginar. É criar código que dê confiança nos limites do problema e nos limites do comportamento (aula #03, 0:14:53). Três cenários da mesma natureza bastam (0:14:43). Dois casos geram dicotomia; o terceiro faz o voto de Minerva (0:16:29). Na aula #04 a mesma conta: um caso é pouco, dois são contraponto, três delineiam uma tendência (0:07:28).

### 3.5 Rodar todos, e deixar a mensagem dizer a divergência

Parar no primeiro assertion error não serve num projeto grande: aquele erro pode ter sido causado por outro (aula #05, 0:01:06). A soma das falhas informa mais: falhar no fiz e no bus ao mesmo tempo aponta um lugar em que os dois se relacionam (0:16:24). A mensagem tem de mostrar o que veio e o que se esperava (0:10:02). Relatório de quantidade e de tempo ele não faz na mão, porque o Python já tem baterias e o módulo unit test (0:16:56).

## 4. As aulas em uma tabela

| # | Título | Duração | Foco em uma linha |
|---|---|---|---|
| 01 | Repita comigo seu novo mantra: TAFT | 1.616 s | Casos de software que falha; testar o tempo todo, automaticamente; prudência contra big design up front. |
| 02 | A essência de um teste | 221 s | O acerte: verdadeiro não faz nada, falso levanta exceção; todo runner se baseia nisso. |
| 03 | Kata: A arte marcial na programação | 2.736 s | Fiz bus em baby steps: erro antes de falha, três casos, um ponto de saída, partial. |
| 04 | Dojo Gameplay Happy Numbers | 1.853 s | Números felizes no dojo: traceback de baixo para cima, três casos, loop e depois recursão. O título da playlist está em inglês. |
| 05 | Por dentro do framework de testes | 1.766 s | Não parar no primeiro erro; helper; unit test; o que a legenda chama de Jungle. |

## 5. Resumo por aula

### Aula #01: Repita comigo seu novo mantra: TAFT

Vídeo: https://www.youtube.com/watch?v=_YJAjxWAHsM · 1616 s

A aula é exposição, sem código. Ele empilha casos de software que falhou, do sistema de mísseis de 83 ao relatório que a legenda chama de caos Report, e chega ao mantra: testar o tempo inteiro, de forma automática. O contraste seguinte é o programador corajoso, que desenha tudo antes, e o prudente, que rascunha a partir do output. O nome do círculo, no fim da legenda, é tdd.

Linha do tempo:

- [0:00:05] Cena de um projeto que começa com o prazo distante e, projeto após projeto, o prazo passa por cima.
- [0:01:33] O maior risco é proteger o próprio traseiro [legenda: cover your S].
- [0:02:05] Entregar software é delicado; a tarefa não pode ser subestimada.
- [0:02:19] Em 83, o sistema mostra cinco mísseis; o coronel segura a cadeia de comando.
- [0:10:21] 68% de falha no relatório de 2010 que a legenda chama de tênis grupo, caos Report: dois projetos em cada três falham.
- [0:12:56] A solução é atacar o desperdício.
- [0:13:27] A legenda diz Dafiti. Em 0:13:30, teste all the fucking all the. Em 0:13:35, fucking o tempo inteiro tem que testar.
- [0:13:38] Código sem teste é um risco para a sociedade.
- [0:13:47] O termo foi cunhado pelo Brian Lions. Sem URL de palestra.
- [0:14:10] Teste manual não escala; tem que ser automático.
- [0:14:46] O tipo de teste é repertório. A essência é o porquê testar.
- [0:15:01] A grande coragem é a prudência, frase de Eurípedes.
- [0:15:43] O corajoso faz big design up front.
- [0:18:32] Input, processamento e altitude. Para o cliente só o output tem valor (0:19:26).
- [0:21:18] O prudente constrói de trás para frente.
- [0:25:05] Os testes que importam evidenciam a silhueta do problema.
- [0:26:47] Esse círculo incremental a gente chama de tdd, teste drive and. A legenda acaba aqui.

Princípios enunciados:

- Código sem teste é um risco para a sociedade; tem que testar o tempo todo (0:13:38).
- Teste manual não escala (0:14:10).
- A grande coragem é a prudência (0:15:01).
- Para o cliente só o output tem valor (0:19:26).
- O teste expressa o entendimento e desenha a silhueta do problema (0:24:21, 0:25:05).

Código: nenhum. A calculadora de dois números fica na fala, sem sintaxe. Cenários narrados, não ditados: 1 e 0 esperam 1; 1 e 1 esperam 2; 1 com 254 tem de ser 255; 1 com 255 fica em aberto (0:24:33 a 0:25:27).

Paráfrases da legenda (não verificadas):

- entregar o software é muito delicado, a gente não pode subestimar essa tarefa (0:02:05)
- código sem teste é um risco para a sociedade, tem que testar o software o tempo todo (0:13:38)
- a grande coragem para mim é a prudência (0:15:01)
- esse círculo incremental a gente chama de tdd teste drive and (0:26:47)

### Aula #02: A essência de um teste

Vídeo: https://www.youtube.com/watch?v=xm_n6qj9PNg · 221 s

A aula mostra uma função que soma dois números e transforma a frase "eu espero três" no comando acerte. Verdadeiro não faz nada. Falso, lista vazia e string vazia levantam exceção. O fecho é que todo test runner se baseia nesse comando, e o exercício seguinte vai usar só o acerto, sem biblioteca. A legenda acaba antes do exercício.

Linha do tempo:

- [0:00:14] Def calk, retorne a + b. Um e dois retornam 3 (0:00:24).
- [0:00:28] Para fazer um teste: eu espero três quando executar Calc 1 e 2.
- [0:00:43] A frase fica como comentário, com a tralha, porque o Python não processa.
- [0:01:00] O comando acerte é palavra reservada e avalia a expressão.
- [0:01:42] Quando é verdadeiro, o acerte não faz nada.
- [0:01:50] Quando é falso, levanta exceção.
- [0:02:09] Lista vazia e string vazia também, porque o valor lógico é falso.
- [0:02:26] Acerto de zero igual a Calc 1 e 2 falha, e a exceção aponta a linha (0:02:43).
- [0:02:51] Todo mecanismo de teste e todo test runner se baseia nesse comando.
- [0:03:16] Desenvolvimento guiado pelo teste: expressar o teste e então implementar o código para ele passar, só com o acerto (0:03:32).

Princípios enunciados:

- Um teste diz o que se espera ao executar (0:00:28).
- Verdadeiro não faz nada; falso levanta exceção (0:01:42, 0:01:50).
- Todo test runner se baseia nesse comando (0:02:51).
- Dá para fazer TDD sem biblioteca de teste (0:03:32).

Código, reconstruído. O nome da função não é soletrado. Parênteses e vírgula não são audíveis. A classe da exceção não é dita.

```python
def calk(a, b):          # "Def calk" "retorne a + b" (0:00:14). Parâmetros não soletrados.
    return a + b

# "eu espero três quando executar Calc 1 e 2" (0:00:31)
assert 3 == calk(1, 2)   # [legenda: acerte três igual a igual calc12] (0:01:06)
assert False             # [legenda: acerte falso] (0:01:47)
assert []                # lista vazia (0:02:09)
assert ""                # string vazia; aspas não audíveis (0:02:17)
assert 0 == calk(1, 2)   # falha e aponta a linha (0:02:26)
```

Paráfrases da legenda (não verificadas):

- para fazer um teste eu tenho que dizer eu espero três quando executar Calc 1 e 2 (0:00:28)
- o comando acerte é uma palavra reservada do Python que avalia essa expressão (0:01:00)
- todo mecanismo de teste, todo executor de teste, o teste runner, se baseia nessa essência, nesse comando (0:02:51)

### Aula #03: Kata, a arte marcial na programação

Vídeo: https://www.youtube.com/watch?v=FeXjPipKbQs · 2736 s

O exercício é o fiz bus: crianças passam a bola e falam fiz no múltiplo de 3, bus no múltiplo de 5, fiz bus no múltiplo dos dois, e o próprio número no resto (0:01:56). O robô tem de jogar com qualquer criança. A estratégia é o kata. No PyCharm ele cria um projeto Python, escreve o teste mais simples, roda para ver quebrar, e só então escreve o menor código. Erro e falha se separam. Três casos da mesma natureza bastam. O caso de 3 e de 5 juntos tem de ser testado antes do múltiplo de 5, senão o retorno de cima engole o de baixo (0:30:02). O polimento pede um ponto de saída, funções com nome, e o partial para colar o 3 e o 5.

Linha do tempo:

- [0:00:05] Fish bus. Arnaldinho, Boris e Clóvis. Posição 3 fala fiz; 5 fala bus; 15 é múltiplo dos dois.
- [0:02:37] Kata é forma. Passo a passo, vagarosamente, o mais simples possível.
- [0:03:02] PyCharm [legenda: pai Charme]. Projeto puro Python, interpretador 3.5, arquivo fiz buzz.
- [0:04:54] Primeiro o teste, depois o código.
- [0:05:16] O teste mais simples: acerte Robot 1 igual à string 1. Roda para quebrar (0:05:59).
- [0:07:25] Seixa nela é falha. Explosão no código é erro.
- [0:08:03] Resolver um erro é sempre mais prioritário do que resolver uma falha.
- [0:08:13] O menor trecho: retorne a string 1.
- [0:09:48] No kata a gente rouba. O teste esculpe pela demanda.
- [0:11:40] Fatorar é organizar como se o próximo programador fosse um psicopata que sabe onde você mora.
- [0:13:33] Incisão: o retorno novo entra antes; não se apaga o bloco velho antes de ver que não executa.
- [0:14:53] TDD não é análise combinatória. É confiança nos limites do problema e do comportamento.
- [0:16:29] Dois casos são dicotomia. O terceiro é o voto de Minerva.
- [0:27:12] O que a expressão quer é o resto. Operador por cento.
- [0:30:02] O 15 entra no múltiplo de 5 e o código novo nunca executa. O caso conjunto sobe para o começo.
- [0:33:04] O ideal é um ponto de entrada e um ponto de saída.
- [0:39:19] Lambda não suporta comando, só expressão. Def e lambda, nesse caso, geram o mesmo código (0:40:23).
- [0:43:42] O partial adequa a API: cola o 5, ou o 3, no primeiro parâmetro.
- [0:44:55] Baby step, como guitarra devagar com metrônomo, para a hora da batalha.

Princípios enunciados:

- Primeiro o teste, o mais simples, só input e output (0:04:54, 0:05:16, 0:05:49).
- Erro antes de falha (0:08:03).
- Três cenários bastam; não é preciso testar todos os casos (0:14:43, 0:14:49).
- TDD é confiança nos limites, não análise combinatória (0:14:53).
- Um ponto de saída (0:33:04).
- Não apagar antes de o substituto funcionar (0:28:56).

Código, reconstrução parcial. Identificadores ficam como foram ouvidos. O arquivo inteiro não é ditado de uma vez.

```python
# projeto "Fish", arquivo ouvido como fiz buzz, Python 3.5 (0:03:08)
# acertes na ordem: 1, 2, 4, depois 3, 6, 9 (fiz), 5, 10, 20 (bus), 15, 30, 45 (fiz bus)
# o 15 não serve para fechar o bus, porque cai no caso conjunto (0:19:56)

from functools import partial  # [legenda: funk Tools Import parcial] (0:42:42)

multiple_off = lambda base, num: num % base == 0  # (0:40:10, 0:41:08)
# partial cola o 5 e o 3 (0:42:50, 0:43:17). Nomes ouvidos: multiplayer, passion.

def robot(post):
    sei = str(post)  # um ponto de saída (0:33:22)
    # o caso de 3 e de 5 fica primeiro, senão o de 5 devolve e o de baixo não roda (0:30:02)
    # o segundo e o terceiro são elif [legenda: Life, elite] (0:35:19)
    if ...:  # múltiplo de 3 e de 5
        sei = "fiz Buzz"
    elif ...:
        sei = "Buzz"
    elif ...:
        sei = "fiz"
    return sei
```

No terminal, fora do arquivo: 6 % 3 é zero, 4 % 3 é um, 5 % 3 é dois (0:27:30). A divisão de inteiros no Python 3 devolve ponto flutuante; a barra barra trunca (0:26:10, 0:26:30).

Paráfrases da legenda (não verificadas):

- a gente faz as coisas passo a passo, vagarosamente, o mais simples possível (0:02:53)
- resolver um erro é sempre mais prioritário do que resolver uma falha (0:08:03)
- no kata a gente rouba, o código mais simples, porque está garantido com teste (0:09:48)
- tdd não se trata de análise combinatória de tudo que é possível imaginável, é para criar código que dê confiança nos limites do problema e do comportamento (0:14:53)

### Aula #04: Dojo Gameplay, números felizes

Vídeo: https://www.youtube.com/watch?v=j0HjzkXFn08 · 1853 s

O título da playlist está em inglês. Na fala, a gravação se chama Dojo Gameplay (0:00:18) e o problema são os números felizes [legenda: rap numbers] (0:00:26). Um inteiro positivo troca pela soma dos quadrados dos dígitos; se der 1, é feliz; senão repete (0:00:44). O 7 chega em 1. O 4 volta para 4, então não é feliz (0:02:16). O ciclo é o mesmo da aula #03: teste mais simples, traceback de baixo para cima, baby step, erro e depois falha, três casos, isolar o que não bate, renomear quando o comportamento já é outro. Um while sem memória entra em loop no 4. Uma lista anota o que já foi visto. No fim ele conta que, da primeira vez, entendeu o enunciado errado, parando abaixo de 10, e que esse equívoco abriu a versão recursiva (0:26:00).

Linha do tempo:

- [0:00:10] A gravação mostra o código emergir durante o dojo.
- [0:01:01] O 7: 49, 97, 130, 10, 1.
- [0:01:37] O 4 percorre 16, 37, 58, 89, 145, 42, 20 e volta ao 4. Não é feliz (0:02:16).
- [0:02:25] Teste mais simples: o acerte do 1.
- [0:03:18] O traceback se lê de baixo para cima. NameError na linha 1 [legenda: Happy Sniper, nem me erra].
- [0:03:37] Baby steps: só o necessário para o teste passar.
- [0:04:35] Sai do estado de erro e entra no estado de falha: o acerte retorna falso.
- [0:05:22] Contraponto: o 4 retorna falso, com o if mais curto que estabiliza.
- [0:07:28] Um caso é pouco, dois são contraponto, três delineiam uma tendência.
- [0:13:48] Para usar a função que soma, separa percorrer, converter e somar.
- [0:17:05] Antes de reescrever tudo, um passo para trás e estabilizar.
- [0:19:12] A soma do 130 imprime 4; falta o quadrado, asterisco asterisco.
- [0:20:01] Um if cair no outro não é legal.
- [0:20:37] Renomear na IDE [legenda: chip de f6]: a soma dos dígitos passa a ser a soma dos quadrados.
- [0:23:06] Sem o if do 4, o while não termina. A lista anota o que já foi calculado (0:23:40).
- [0:26:00] O equívoco de parar abaixo de 10 abre a versão recursiva.
- [0:26:44] Menores que 10, só 1 e 7 são felizes.
- [0:27:16] Recursão precisa de condição de parada.
- [0:29:24] Não redefinir a builtin next. O nome ganha underscore.
- [0:30:48] O comentário embaixo do vídeo é a parte mais importante.

Princípios enunciados:

- Baby steps, só o necessário para passar (0:03:37).
- Erro é exceção; falha é o acerte que retorna falso (0:04:35).
- Três casos delineiam uma tendência (0:07:28).
- Passo para trás antes de se perder (0:17:05).
- Um if que depende de cair no outro não é legal (0:20:01).
- Não redefinir função que o Python já define (0:29:24).

Código, reconstrução do que a narração sustenta no começo e no fim. O meio é substituído várias vezes; os corpos intermediários não são um arquivo estável.

```python
# teste mais simples (0:02:32). Nome da função ouvido como rap e como Happy.
assert rap(1) == True

def rap(Number):
    if Number == 4:    # contraponto (0:05:29)
        return False
    return             # o valor deste retorno não é soletrado (0:04:57)

# fim da aula, depois de apagar o while (0:27:34 a 0:30:08)
# menores que 10: retorna se o número está em 1 ou 7
# senão: chama a si com a soma dos quadrados dos dígitos
# next_ com underscore, porque next já existe (0:29:31)
```

Paráfrases da legenda (não verificadas):

- o objetivo é fazer baby steps e só o necessário para o teste passar (0:03:37)
- eu gosto sempre de fazer três, um é pouco, dois é contraponto, três delineia uma tendência (0:07:28)
- um if cair no outro não é legal (0:20:01)
- é boa prática não redefinir função que o Python já define por padrão (0:29:24)

### Aula #05: Por dentro do framework de testes

Vídeo: https://www.youtube.com/watch?v=cwQZW7m2qdU · 1766 s

Ele volta ao fiz bus já pronto e troca um end por or. O acerte para no primeiro assertion error (0:00:23). Ele quer rodar todos e contar, porque aquele erro pode ter sido causado por outro (0:01:06). Extrai uma função, faz a mensagem dizer o que veio e o que se esperava, tira o try, e busca a linha no frame de quem chamou. Underscore na frente é dica de interno, acordo no fio do bigode, porque o Python não tem burocracia de privado (0:12:04). Aí ele para de fazer na mão: o Python já tem o módulo unit test (0:16:56). A classe herda de test case, o método começa com test, e doze passam. Separar o arquivo de teste do projeto é o normal (0:22:10). O que a legenda chama de Jungle executa parecido, com manage test, e o trabalho de quem testa é criar asserções de mais alto nível, de olho na expressividade (0:28:56).

Linha do tempo:

- [0:00:23] Troca end por or. Assertion error na posição três: entra em fiz bus e não devolve fiz. A execução para.
- [0:01:06] Num projeto grande, rodar todos e contar. O primeiro erro pode ter sido causado por outro.
- [0:01:29] Assertion error é exceção. Try numa linha ainda deixa a seguinte estourar. Extrai a função acert.
- [0:06:48] Dizer a linha não basta. A mensagem tem de mostrar a divergência.
- [0:10:02] Na linha 41 ele lê: recebi fiz bus, esperando fiz.
- [0:10:16] O try e o assert saem. If not, e o print do template.
- [0:11:04] first vira result, second vira expected, porque a frase é got e expecting.
- [0:11:55] A linha deixa de ser argumento. A busca ouve Sis ponto und get frame.
- [0:12:07] Underscore na frente: interno. Usar fica por conta de quem usa. A API pode mudar.
- [0:16:24] Falhar no fiz e no bus ao mesmo tempo dá mais informação do que um erro só.
- [0:16:56] Não fazer o relatório na mão. O Python já tem baterias e o módulo unit test.
- [0:18:08] O prefixo test no método é o que faz o unit test detectar o test method.
- [0:19:20] Doze passando. A interface do PyCharm passa a usar o test runner.
- [0:20:17] O or produz falhas, não erros. Um nome indefinido produz erros (0:20:42).
- [0:21:01] python -m, ouvido como Men M, aponta o entry point para o unit test e varre o diretório.
- [0:22:10] Separa o código de teste do código do projeto. Sem o if de __name__, porque o runner acha os testes.
- [0:25:46] Em cada test case: setup, o teste, e o que a legenda chama de terd, para limpar efeito colateral.
- [0:26:39] O Jungle é parecido: manage test, do pacote até um método, no eventex.
- [0:28:56] Criar asserções de mais alto nível, estendendo o unit test e o Jungle, de olho na expressividade.

Princípios enunciados:

- Rodar todos, porque um erro pode ter sido causado por outro (0:01:06).
- A mensagem mostra o que veio e o que se esperava (0:10:02).
- Underscore na frente é acordo, não trava da linguagem (0:12:07).
- A soma das falhas informa mais do que um erro só (0:16:24).
- Falha e erro são relatórios diferentes (0:20:17, 0:20:42).
- Separar teste e projeto (0:22:10).
- Expressividade: não repetir o teste o tempo todo; subir o nível da asserção (0:28:56).

Código, reconstrução do helper na forma final narrada, e do esqueleto do test case. Os doze métodos não são ditados. pytest não é nomeado.

```python
def acert_equal(result, expected):
    from sys import _getframe          # [legenda: from se Import get frame] (0:13:34)
    caller = _getframe().f_back        # [legenda: current p f Back] (0:14:20)
    line_no = caller.f_lineno          # [legenda: color f l no] (0:14:46)
    if not result == expected:         # (0:10:19)
        msg = "fail: Line {} got {} expecting {}"  # (0:08:55)
        print(msg.format(line_no, result, expected))

import unittest  # [legenda: Import unit test], o módulo inteiro (0:17:28)

class fbus_test(unittest.TestCase):  # (0:17:39)
    def test_say_one_when_one(self):  # "test und say One when One" (0:18:08)
        self.assertEqual(Robot(1), "1")  # [legenda: self acert equal] (0:18:27)
```

Comandos ouvidos, não conferidos na tela: python no arquivo do jogo, python -m unittest, --help, -v (0:19:48, 0:21:01, 0:21:48, 0:21:58). O arquivo do projeto sozinho, sem o if de __name__, não faz nada (0:24:09).

Paráfrases da legenda (não verificadas):

- eu quero rodar todos os testes e contar quantos deram erro, porque vai que esse erro é causado por um outro (0:01:10)
- underscore na frente é uma dica: isso aqui é interno, se usar fica ciente que essa API pode mudar (0:12:07)
- o Python já tem baterias e já tem o módulo unit test (0:16:56)
- o trabalho é entender as repetições e os padrões do domínio e criar asserções de mais alto nível, de olho na expressividade (0:28:56)

## 6. Princípios que atravessam toda a série

Dez regras que ele formula na fala. Nenhuma é inferência deste documento.

#### 1. Testar o tempo todo, automaticamente

Código sem teste é um risco para a sociedade (aula #01, 0:13:38). Tem que testar o tempo todo (0:13:35). Teste manual não escala (0:14:10). O nome que a legenda dá ao mantra é Dafiti (0:13:27), com a expansão ouvida em 0:13:30.

#### 2. A essência do teste é o acerte

Verdadeiro não faz nada; falso levanta exceção (aula #02, 0:01:42, 0:01:50). Todo test runner se baseia nesse comando (0:02:51).

#### 3. Erro antes de falha

Expectativa não atendida é falha. Explosão no código é erro. Resolver o erro é sempre mais prioritário (aula #03, 0:07:25, 0:08:03). A aula #04 separa os mesmos dois estados (0:04:35). A aula #05 mostra os dois no relatório (0:20:17, 0:20:42).

#### 4. Confiança nos limites, não combinação

Não precisa de teste para todos os casos (aula #03, 0:14:49). TDD é confiança nos limites do problema e do comportamento (0:14:53). Três cenários da mesma natureza bastam (0:14:43). Um é pouco, dois são contraponto, três delineiam uma tendência (aula #04, 0:07:28).

#### 5. O teste mais simples, e o menor código que passa

Primeiro o teste, o mais simples, só input e output (aula #03, 0:05:16, 0:05:49). Baby steps: só o necessário para passar (aula #04, 0:03:37). No kata se rouba, porque o teste garante (aula #03, 0:09:48).

#### 6. Incisão, e um passo para trás se perder o chão

Não apagar antes de o substituto funcionar (aula #03, 0:13:33, 0:28:56). Se a mudança se perde, estabilizar de novo (aula #04, 0:17:05).

#### 7. Um ponto de saída

O ideal é um ponto de entrada e um ponto de saída (aula #03, 0:33:04). Ifs soltos que escrevem a mesma variável um por cima do outro pedem elif (0:35:08).

#### 8. Rodar todos

Parar no primeiro assertion error esconde a causa (aula #05, 0:01:06). Várias falhas juntas apontam a relação (0:16:24).

#### 9. A mensagem diz a divergência

O que veio e o que se esperava (aula #05, 0:10:02). O nome acompanha a frase: result e expected (0:10:50).

#### 10. Subir o nível da asserção

O unit test já traz os acertes. O Jungle estende com foco na web. O trabalho é criar asserções do domínio, de olho na expressividade, em vez de repetir o teste (aula #05, 0:28:56).

## 7. Citações-chave do curso

Paráfrases de legenda automática, sem aspas e não verificadas contra o vídeo.

| Aula | Timestamp | Paráfrase |
|---|---|---|
| #01 | 0:02:05 | entregar o software é delicado, a gente não pode subestimar essa tarefa |
| #01 | 0:13:30 | teste all the fucking all the fucking o tempo inteiro tem que testar |
| #01 | 0:13:38 | código sem teste é um risco para a sociedade |
| #01 | 0:14:10 | teste manual não escala |
| #01 | 0:15:01 | a grande coragem para mim é a prudência |
| #01 | 0:26:47 | esse círculo incremental a gente chama de tdd teste drive and |
| #02 | 0:01:00 | o comando acerte é uma palavra reservada do Python que avalia essa expressão |
| #02 | 0:02:51 | todo mecanismo de teste, o teste runner, se baseia nessa essência |
| #03 | 0:02:53 | passo a passo, vagarosamente, o mais simples possível |
| #03 | 0:08:03 | resolver um erro é sempre mais prioritário do que resolver uma falha |
| #03 | 0:09:48 | no kata a gente rouba, porque está garantido com teste |
| #03 | 0:11:40 | fatorar como se o próximo programador fosse um psicopata que sabe onde você mora |
| #03 | 0:14:53 | tdd não se trata de análise combinatória, é confiança nos limites do problema e do comportamento |
| #03 | 0:33:04 | o ideal é um ponto de entrada e um ponto de saída |
| #04 | 0:03:37 | baby steps, só o necessário para o teste passar |
| #04 | 0:07:28 | um é pouco, dois é contraponto, três delineia uma tendência |
| #04 | 0:29:24 | não redefinir função que o Python já define por padrão |
| #05 | 0:01:10 | rodar todos os testes, porque esse erro pode ter sido causado por outro |
| #05 | 0:12:07 | underscore na frente é dica de interno, a API pode mudar |
| #05 | 0:16:56 | o Python já tem baterias e o módulo unit test |
| #05 | 0:28:56 | criar asserções de mais alto nível, de olho na expressividade |

## 8. A evolução técnica, aula a aula

| Etapa | O que é feito | Conceito ou ferramenta | O que isso destrava |
|---|---|---|---|
| **#01** | Exposição, sem código (0:00:05 a 0:26:50) | Mantra, prudência, output | O motivo de testar e a ordem de trás para frente (0:21:18) |
| **#02** | Calc e o acerte (0:00:14 a 0:03:38) | assert, sem biblioteca | A essência de qualquer runner (0:02:51) |
| **#03** | Kata do fiz bus (0:00:05 a 0:45:30) | Baby step, %, elif, lambda, partial | Erro antes de falha, três casos, um retorno (0:08:03, 0:33:04) |
| **#04** | Números felizes (0:00:24 a 0:30:50) | Traceback, sum, while, recursão | Três casos como tendência; não redefinir builtin (0:07:28, 0:29:24) |
| **#05** | Helper e unit test (0:00:05 a 0:29:23) | try, frame, unittest, o Jungle | Rodar todos, mensagem com divergência, asserção do domínio (0:01:06, 0:28:56) |

## 9. Arsenal técnico demonstrado no curso

| Técnica ou recurso | Para que ele usa | Aula e timestamp |
|---|---|---|
| Comentário com tralha | Guardar a frase do teste antes de virar comando | #02, 0:00:43 |
| acerte | A essência do teste, sem biblioteca | #02, 0:01:00 |
| PyCharm [legenda: pai Charme] | O editor do kata, do dojo e do helper | #03, 0:03:02; #04, 0:00:35 |
| Rodar para ver quebrar | O primeiro teste existe para falhar | #03, 0:05:59 |
| str de inteiro | Generalizar o retorno do número | #03, 0:12:06 |
| Operador % | Resto, no lugar da conta de múltiplo à mão | #03, 0:27:12 |
| // | Divisão inteira no Python 3 | #03, 0:26:30 |
| elif [legenda: Life] | Impedir que um if reescreva o resultado do anterior | #03, 0:35:19 |
| lambda | A mesma função, como expressão | #03, 0:39:19 |
| functools.partial [legenda: funk tu, parcial] | Colar o 3 ou o 5 e adequar a API | #03, 0:42:42 |
| Dois espaços entre funções [legenda: Pepe 8] | O espaçamento que ele diz que a convenção manda | #03, 0:37:21 |
| Traceback de baixo para cima | Achar a linha e o tipo do problema | #04, 0:03:18 |
| pass | Função vazia, no caminho do baby step | #04, 0:04:14 |
| sum, list comprehension, generator | Separar percorrer, converter e somar | #04, 0:14:01, 0:15:08, 0:25:32 |
| ** | Quadrado do dígito | #04, 0:19:12 |
| Refactor rename [legenda: chip de f6] | O nome acompanha o comportamento | #04, 0:20:37 |
| all | Vários acertes felizes numa expressão | #04, 0:25:14 |
| Underscore no nome | Não redefinir next | #04, 0:29:31 |
| try / AssertionError | Deixar o próximo teste rodar | #05, 0:01:29 |
| str.format | A mensagem fail, line, got, expecting, no lugar do % | #05, 0:09:19 |
| sys._getframe | A linha de quem chamou, sem argumento | #05, 0:11:55 |
| unittest [legenda: unit test] | O módulo da biblioteca padrão, baterias inclusas | #05, 0:16:56 |
| python -m [legenda: Men M] | Entry point do unit test, varre o diretório | #05, 0:21:01 |
| -v | Cada teste com status | #05, 0:21:58 |
| setup e tearDown [legenda: terd] | Montar o contexto e limpar efeito colateral | #05, 0:25:46 |
| manage test, eventex [legenda: Jungle] | O mesmo runner, restringindo pacote, classe ou método | #05, 0:26:39 |

## 10. Glossário do curso

| Termo | Significado no contexto da série | Onde |
|---|---|---|
| **Dafiti** | O mantra, como a legenda ouve o título TAFT. A expansão ouvida é testar o tempo inteiro | #01, 0:13:27 |
| **Brian Lions** | Quem, na legenda, cunhou o termo. Nome não soletrado | #01, 0:13:47 |
| **Prudência** | A coragem que ele pede, contra o heroísmo | #01, 0:15:01 |
| **Big design up front** | Desenhar a solução inteira antes de desenrolar | #01, 0:15:43 |
| **Altitude** | A terceira parte de input, processamento e altitude. No contexto, o output | #01, 0:18:35 |
| **Silhueta** | O que os testes que importam evidenciam do problema | #01, 0:25:05 |
| **Acerto** | O comando que avalia a expressão. Leitura: assert | #02, 0:01:00 |
| **Test runner** | O executor que se baseia nesse comando | #02, 0:02:55 |
| **Kata** | Forma, treino de movimento, devagar. A legenda ouve catar | #03, 0:02:37 |
| **Falha** | Expectativa não atendida. A legenda ouve seixa nela | #03, 0:07:25 |
| **Erro** | Explosão no código, exceção que não era a expectativa | #03, 0:07:52 |
| **Baby step** | O menor passo que faz o teste passar | #03, 0:15:57; #04, 0:03:37 |
| **Voto de Minerva** | O terceiro caso, que desfaz a dicotomia de dois | #03, 0:16:31 |
| **Incisão** | Código novo em cima do velho, sem apagar antes | #03, 0:13:33 |
| **Fiz, bus, fiz bus** | O que se fala no múltiplo de 3, de 5 e dos dois. A legenda também ouve Fish, Bush e Buzz | #03, 0:01:56 |
| **Número feliz** | Inteiro que, pela soma dos quadrados dos dígitos, chega em 1. A legenda ouve rap numbers | #04, 0:00:26 |
| **Dojo** | A dinâmica em que o código emerge. A legenda ouve caldinho Dojo | #04, 0:00:03 |
| **Underscore na frente** | Dica de interno. Acordo, não proibição da linguagem | #05, 0:12:07 |
| **Unit test** | O módulo da biblioteca padrão | #05, 0:16:56 |
| **Jungle** | O framework que estende o test case com foco na web. O eventex é o exemplo | #05, 0:26:39 |
| **Serão sua** | A asserção de mais alto nível, a partir da repetição do domínio. Leitura: assertion | #05, 0:28:56 |

## 11. Perguntas e respostas que o curso responde

#### Por que testar o tempo todo?

Porque código sem teste é um risco para a sociedade, e teste manual não escala (aula #01, 0:13:38, 0:14:10).

#### Qual teste é o bom?

A pergunta tira o olho do porquê. Funcional, unitário, de carga e de aceitação são repertório (aula #01, 0:14:18, 0:14:38).

#### O que é um teste, sem framework?

Dizer o que se espera ao executar, e deixar o acerte avaliar. Verdadeiro não faz nada. Falso levanta exceção (aula #02, 0:00:28, 0:01:42). Todo runner se baseia nisso (0:02:51).

#### Erro ou falha, o que se resolve primeiro?

O erro. Falha é expectativa não atendida. Erro é o código explodindo (aula #03, 0:08:03). No relatório do unit test os dois aparecem separados (aula #05, 0:20:17).

#### Quantos casos bastam?

Três da mesma natureza. Não é análise combinatória. É confiança nos limites (aula #03, 0:14:43, 0:14:53). Um é pouco, dois são contraponto, três delineiam uma tendência (aula #04, 0:07:28).

#### Por que o teste do 15 não fecha o caso do bus?

Porque 15 é múltiplo de 3 e de 5. O terceiro caso do bus é o 20. E o caso conjunto tem de ser testado antes do múltiplo de 5, senão o retorno de cima engole o de baixo (aula #03, 0:19:56, 0:30:02).

#### Por que não parar no primeiro teste que quebra?

Porque aquele erro pode ter sido causado por outro, e a soma das falhas aponta a relação (aula #05, 0:01:06, 0:16:24).

#### Underscore na frente proíbe o uso?

Não. É dica de interno. Usar fica por conta de quem usa, ciente de que a API pode mudar. O Python não faz a burocracia de privado (aula #05, 0:12:07). A aula #04 usa o mesmo recurso para não redefinir next (0:29:24).

#### Quando escrever o próprio assert?

Quando a repetição do domínio pede uma asserção mais expressiva. Até lá, o unit test e o Jungle já sobem o nível (aula #05, 0:28:56).

## 12. Repositórios e recursos

| Recurso | Onde encontrar | Observação |
|---|---|---|
| Playlist completa (fonte desta documentação) | [Raio-X do Test-Driven Development](https://www.youtube.com/playlist?list=PLeKXYyZCJHxe1X_B-o5bMDyNLxIBQB1q7) | 5 vídeos; ids `_YJAjxWAHsM`, `xm_n6qj9PNg`, `FeXjPipKbQs`, `j0HjzkXFn08`, `cwQZW7m2qdU`. |
| Canal | [HB Network](https://www.youtube.com/@hbnetworkoficial) | |
| Brian Lions | sem URL | Aula #01, 0:13:47. A legenda manda pesquisar e ver as palestras. Sem título. |
| eventex | citado como exemplo do Jungle | Aula #05, 0:27:09: manage test até um método em testes, em core, em eventex. Sem usuário nem caminho nesta fala. O digest do repositório está em `kb/repos/eventex.md`. |
| Documento sobre o caso do Toyota | "um documento na internet" | Aula #01, 0:06:57. Sem endereço. |

Repositório do kata, do dojo e do helper: **nenhum URL nesta transcrição**. Esta documentação não foi ao GitHub procurá-los.

## 13. Análise linha a linha do código real

Não há código publicado com caminho, commit ou URL para esta série, portanto não há análise de código real. O que existe é o que ele digita ao vivo, reconstruído na seção 5. Limites que ficam registrados:

- A aula #01 narra cenários da calculadora e não dita sintaxe. A legenda acaba em "teste drive and" (0:26:50).
- Na aula #02 o nome da função, os parênteses e a classe da exceção não são soletrados.
- Na aula #03 o arquivo do robô é construído e reescrito o tempo todo. A reconstrução da seção 5 guarda a forma final narrada, não cada versão intermediária. Os nomes fiz, bus, Robot, multiple_off e partial são leitura da fala.
- Na aula #04 o mesmo: o while, o for, a lista e a recursão se substituem. O retorno verdadeiro do primeiro baby step não é soletrado.
- Na aula #05 só um método de teste é ditado. Os outros onze ele acelera (0:18:43). Os nomes de `sys._getframe`, `f_back` e `f_lineno` são leitura de "Sis ponto und get frame", "f Back" e "f l no".
- pytest não é nomeado. Unit test e Jungle ficam como a legenda ouve.

## 14. Execução real dos testes

O curso não publicou código nem suíte. Não há o kata nem o dojo para rodar.

As reconstruções da seção 5 não foram executadas como programa do curso. O fragmento da aula #02 e os restos da aula #03 são audíveis o bastante para uma checagem. A reconstrução abaixo é deste documento. Rodou em Python 3 nesta sessão:

| Comportamento narrado | Aula e timestamp | Resultado da reconstrução |
|---|---|---|
| Calc 1 e 2 retorna 3, e o acerte de 3 não faz nada | #02, 0:00:24 e 0:01:42 | nenhuma exceção |
| acerte falso levanta exceção | #02, 0:01:50 | `AssertionError` |
| lista vazia e string vazia também | #02, 0:02:09 e 0:02:17 | `AssertionError` nos dois |
| acerte de zero igual a Calc 1 e 2 falha | #02, 0:02:26 | `AssertionError` |
| 6 % 3 é zero, 4 % 3 é um, 5 % 3 é dois | #03, 0:27:30 | `0`, `1`, `2` |
| 4 // 3 trunca | #03, 0:26:30 | `1` |

A cadeia do 7 que ele narra (49, 97, 130, 10, 1) e a do 4 (16, 37, 58, 89, 145, 42, 20, 4) conferem com a soma dos quadrados dos dígitos, que é o enunciado (aula #04, 0:01:01, 0:01:40). Isso é conta do enunciado, não execução de uma função dele. O script ficou fora do repositório.

---

Documentação elaborada a partir das transcrições automáticas das 5 aulas da playlist Raio-X do Test-Driven Development, de Henrique Bastos (HB Network), playlist `PLeKXYyZCJHxe1X_B-o5bMDyNLxIBQB1q7`, legendas em português (pt-orig) capturadas em 2026-10-09. As citações são paráfrases das legendas automáticas, não verificadas contra o vídeo (`verified: false`), renderizadas sem aspas e com os erros de reconhecimento de fala anotados entre colchetes quando precisam aparecer. O curso não publica URL de repositório nesta transcrição. O título da aula #04 chegou em inglês no `playlist.json`. Todo o código desta documentação é reconstrução a partir da narração, marcada como tal na seção 5. A seção 14 registra a reconstrução do acerte da aula #02 e dos restos da aula #03. Datas de publicação e visualizações não foram coletadas. Conteúdo de caráter educativo.
