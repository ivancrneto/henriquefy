<!-- written by the henrique-ingest distiller on 2026-10-09 from sources/transcripts/procedural-para-oo/; see kb/courses/README.md for provenance and license -->

HB Network · Documentação de curso

# Transforme seu código Procedural em Orientado a Objetos

As 10 aulas, da dicotomia entre paradigmas ao game of life com CLI e GUI, lidas aula a aula a partir das legendas automáticas. O código é digitado ao vivo e não foi publicado com URL nesta série; os trechos desta documentação são reconstruções, marcadas como tal.

Instrutor: **Henrique Bastos** · Canal [HB Network](https://www.youtube.com/@hbnetworkoficial) · Playlist: [Transforme seu código Procedural em Orientado a Objetos](https://www.youtube.com/playlist?list=PLeKXYyZCJHxeKQ13fuBUuLyfeOK9Jr8t7) · Repositório: nenhum URL falado (aula #10, 0:35:16, ele diz que vai botar no GitHub e colocar o link embaixo do vídeo)

Documento elaborado a partir das transcrições automáticas das 10 aulas (legendas em português, pt-orig, capturadas em 2026-10-09). O curso não dita um arquivo linha a linha: as aulas #02 e #04 a #10 acontecem no editor, e os trechos de código desta documentação são reconstruções a partir do que ele narra.

## 1. Visão geral do curso

Transforme seu código Procedural em Orientado a Objetos é uma série de **10 aulas** que somam **11.832 segundos, 3 horas, 17 minutos e 12 segundos**. O arco é um só. As três primeiras aulas tiram a dicotomia entre procedural e objetos: o objeto não é dados com código, é um processo, e encapsular é articular comportamento, não esconder atributo (aula #01, 0:24:31; aula #02, 0:12:11). A aula #03 recusa regras que não escalam e instala o ciclo de fazer funcionar, fazer direito e, se precisar, fazer ficar rápido (0:24:11). Da aula #04 em diante o caso é um game of life já escrito em funções: ele lê o arquivo, parte o novelo em módulos, sobe o board e a coordenada para objetos que falam o data model do Python, separa o jogo do loop de entrada e saída, e termina com a mesma lógica consumida por uma linha de comando e por uma janela Tk (aula #10, 0:14:02).

| Dimensão | Valor | Observação |
|---|---|---|
| Aulas | 10 | Playlist completa, numerada de #01 a #10. |
| Duração total | 11.832 s (3h 17min 12s) | Soma das durações em `playlist.json`. |
| Aula mais curta / mais longa | 413 s (#05) / 2.206 s (#10) | A #10, CLI e GUI, é a sessão de fechamento. |
| Datas de publicação | não coletadas | O `playlist.json` desta coleta traz id, título e duração. |
| Visualizações | não coletadas | Idem. |
| Transcrições | 10 de 10 disponíveis | Legenda automática em português (pt-orig); não há legenda humana. |
| Código do curso | nenhum URL publicado | Aula #10, 0:35:16: ele vai botar no GitHub e o link fica embaixo do vídeo. Nome de repositório, usuário e caminho não são falados. |
| Bloco prático | aulas #02 e #04 a #10 | Cesta de maçãs no editor; depois o game of life, do arquivo em funções até CLI e GUI. |

Nota de método: este documento tem uma única fonte, a transcrição automática. Cada afirmação traz aula e timestamp. As citações são paráfrases de legenda, sem aspas, não verificadas contra o vídeo, e os erros de reconhecimento de fala ficam anotados entre colchetes quando precisam aparecer. Identificadores que a legenda não soletra (nomes de classe, de método, `wrap`, `python -m`, `namedtuple`, `Tk`) ficam marcados como leitura e não entram como código publicado. A seção 14 registra só o fragmento do interpretador da aula #08, que é audível o bastante para uma reconstrução mínima.

## 2. Filosofia e método de ensino

### 2.1 Eliminar a dicotomia antes de escolher o paradigma certo

A série abre atacando a dicotomia entre programação procedural e orientada a objetos (aula #01, 0:00:12). A disputa de paradigmas, para ele, simboliza a dificuldade de fazer a coisa certa (0:02:10). Não saber padrão de projeto não é um problema de detalhe; é um problema de dimensão (0:02:46). Dicotomia é o ou exclusivo, isso ou aquilo, certo ou errado (0:04:38). O pedido é eliminar essa exclusão e ver as questões como frequências distintas da mesma luz (0:03:37).

### 2.2 O código é uma foto; a execução é um filme

Ele repete que o código é uma foto e o código rodando é um filme: a partir da foto se modela a execução (aula #01, 0:08:32). O que se quer desenrolar é a melhor forma de organizar código e memória (0:16:53). Na aula #05 o mesmo critério volta: o foco é a interação dos objetos na memória, com o filme rodando, e não a classe em específico (0:06:38).

### 2.3 Voltar à base, porque tecnologia avançada parece mágica

Qualquer tecnologia suficientemente avançada será indistinguível de mágica, e programar parece magia em forma de bits (aula #01, 0:05:43). Por isso a aula #01 volta aos fundamentos: o que é procedural, o que a estruturada acrescentou com o Algol, e o que o Simula precisou inventar para a simulação não perder o contexto no retorno da função (0:07:02, 0:13:04, 0:18:10).

### 2.4 Regras não escalam; o processo pesa mais que o conhecimento

Regras não escalam: a legislação brasileira tem regra para tudo e ninguém consegue fazer nada (aula #03, 0:07:30). A alternativa são princípios, que se contradizem, dependem de contexto e são mais sutis do que regras (0:07:47). Não existe a resposta que resolve tudo (0:08:49). O obstáculo ao bom design somos nós, que nos impomos no processo (0:15:57). Só se programa o que se entende, e o normal é programar o que ainda se desconhece (0:21:10). O processo é mais importante do que o conhecimento; ser é mais importante do que saber (0:25:00).

### 2.5 Fazer funcionar, fazer direito, e só então ficar rápido

O ciclo que ele instala é fazer funcionar, fazer direito e, se precisar, fazer ficar rápido, repetindo e enxugando escopo (aula #03, 0:24:11). É preciso orbitar a solução: ir direto nela dá paralisia ou trata como pronto o que não está adequado (0:24:25). Enquanto não houver um código funcionando com uma forma, não adianta tentar a melhor forma (0:18:10). A dinâmica que a legenda ouve como always Dane é ter alguma coisa pronta cada vez que se trabalha, gambiarra ou sistema ideal (0:25:36). Na aula #10 a performance espera: a organização já está no ponto de tunar depois (0:30:42).

### 2.6 Partir o que mexe com o quê, e manter funcionando

Antes de separar arquivos, a aula #05 gera um gráfico de chamada para ver a interdependência (0:01:34, 0:02:24). A aula #06 chama o gesto de passar o facão: criar restrições e separar as partes, e cada extração tem de continuar funcionando (0:00:06, 0:01:27). Diante de código duro, a aula #09 manda comer pelas beiradas (0:01:33). A aula #10 nomeia o trabalho contínuo: estão sempre lapidando a fronteira para ver o que faz sentido (0:19:38).

## 3. Pilares conceituais

### 3.1 Do procedural ao objeto: código, memória e processo

No procedural, o programa é código e memória, e qualquer código mexe em qualquer memória (aula #01, 0:08:57). Procedimentos não são funções: são checklists, sequências de passos (0:10:04). A programação estruturada, com o Algol, traz bloco de código, pilha e encadeamento de funções: o código da função é o mesmo, a memória é contextualizada pela execução, e no retorno a memória do bloco sai da pilha (0:13:07, 0:16:24). O Simula precisava que a informação não sumisse nesse retorno, para simulações em que a mesma função era chamada com contexto diferente (0:18:30). Os três critérios que ele junta são alocação dinâmica, foco em processos e despacho dinâmico (0:22:04). Polimorfismo, nesse desenho, não é funções com múltiplas assinaturas: é resolver na execução qual função daquele nome corre no contexto daquele objeto (0:23:18).

### 3.2 O objeto é um processo, não uma estrutura de dados com métodos

A visão de que objetos são dados e código juntos não vale no conceito: o objeto está acima disso, porque o objeto é um processo (aula #01, 0:24:22 e 0:24:31). Objetos envolvem a estrutura com processos e provêm serviços; como o serviço é implementado é detalhe (0:28:12). Uma estrutura de dados com métodos não é necessariamente um objeto (0:30:28). A aula #02 mostra o mesmo no editor: o primeiro desenho da cesta de maçãs roda, e mesmo assim ele diz que está programando procedural com classes (0:04:38).

### 3.3 Encapsulamento é articulação do comportamento

Encapsulamento não é sobre atributos. É sobre o comportamento e sobre o processo que envolve aquele código e aquele dado (aula #03, 0:01:51). Na cesta, violar encapsulamento não é mexer no `data` oculto: é a capacidade de resolver o problema estar em quem consome, e não no objeto (aula #02, 0:12:11). O consumidor acoplado controla o processo em vez de delegar a quem é de direito (0:08:40). A dificuldade que ele nomeia no fecho é definir a fronteira (0:13:24).

### 3.4 Superfície de contato, e a relação na dinâmica

A superfície de contato entre dois códigos tem de ser reduzida (aula #02, 0:09:30). No game of life, cada import mostra o tamanho dessa superfície entre o jogo e o bitmap (aula #06, 0:03:54). Trocar dois imports por um é pouco na superfície e muito no conceito (0:07:22). Na aula #10 a mesma ideia sobe de módulo para sistema: sistemas complexos se relacionam na dinâmica, na vida dos caras; relação estruturada direto, fisicamente no código, amarra (0:22:06). A estratégia é podar o excesso de contato (0:22:26).

### 3.5 O dado espalhado importa mais do que o rótulo global

No arquivo do game of life o board nasce na pilha do `main` e é passado a todas as funções (aula #04, 0:15:12). Entender que é uma variável espalhada no código é mais importante do que se prender se é global ou se não é (0:16:45). O que importa é que tem gente mexendo nele (0:18:04). A aula #10 formula o alvo da série inteira: harmonizar dado e código, memória e código, evitando que um dado fique usado em muitos lugares, manipulado por muita gente, e criando interfaces que encapsulam esses comportamentos (0:00:14).

## 4. As aulas em uma tabela

| # | Título | Duração | Foco em uma linha |
|---|---|---|---|
| 01 | Removendo a Dicotomia | 1.855 s | Dicotomia de paradigmas; procedural, estruturada e Simula; objeto como processo. |
| 02 | A Cesta de Maças | 809 s | A mesma cesta procedural com classes e como processo; encapsulamento como comportamento. |
| 03 | O Ciclo de Melhoria Continua | 1.566 s | Regras não escalam; quatro naturezas de sistema; fazer funcionar, fazer direito, ficar rápido. |
| 04 | Mão na Massa! Entendendo o Problema | 1.095 s | Game of life em funções; board passado para todo lado; variável espalhada. |
| 05 | Modelando o Problema | 413 s | Gráfico de chamada; quebrar em módulos já é encapsulamento; OO não é só classe. |
| 06 | Desenrolando o Novelo | 1.119 s | Pacote, imports como superfície de contato, inversão pequena, board no módulo. |
| 07 | Montando o Bitmap/Trabalhando no Board | 901 s | Classe do board com o data model; o offset de -1 fica no protocolo, não espalhado. |
| 08 | Montando as Coordenadas | 701 s | Coordenada como dupla com nome e soma; um lugar só muda e o offset sai. |
| 09 | Separando as Responsabilidades do main | 1.167 s | Update, show e loop; o wrap toroidal vai para o board. |
| 10 | CLI e GUI | 2.206 s | A mesma lógica na linha de comando e no Tk; fronteira, adapter, herança com cuidado. |

## 5. Resumo por aula

### Aula #01: Removendo a dicotomia

Vídeo: https://www.youtube.com/watch?v=413wIxuhy2w · 1855 s

A aula é uma apresentação, sem código audível. Ele abre a dicotomia entre procedural e objetos, pede para eliminar o ou exclusivo, e reconstrói os fundamentos: no procedural qualquer código mexe em qualquer memória; na estruturada o mesmo código opera em memória de cada chamada; nos objetos, a partir do Simula, a memória não some no retorno e o despacho acha a função daquele objeto. O fecho é que objeto não é dados e código juntos: é um processo. O exemplo da cesta de maçãs é anunciado e não é ditado nesta legenda.

Linha do tempo:

- [0:00:12] Abertura: atacar a dicotomia, procedural versus orientado a objetos.
- [0:02:10] A disputa de paradigmas simboliza a dificuldade de fazer a coisa certa.
- [0:02:46] O problema é de dimensão, não de detalhe de padrão de projeto.
- [0:03:37] Eliminar a dicotomia: frequências de luz distintas da mesma luz.
- [0:04:38] Dicotomia é o ou exclusivo, certo ou errado, melhor ou pior.
- [0:05:43] Qualquer tecnologia suficientemente avançada será indistinguível de mágica.
- [0:08:32] O código é uma foto; o código rodando é um filme.
- [0:08:57] No procedural o programa é código e memória, e qualquer código mexe em qualquer memória.
- [0:10:04] Procedimentos não são funções; são checklists, sequências de passos.
- [0:13:07] A estruturada, com o Algol, traz bloco, pilha e encadeamento de funções.
- [0:16:24] O código da função é o mesmo; a memória é contextualizada pela execução.
- [0:18:10] O Simula, para simulações em que o contexto não podia sumir no retorno da função.
- [0:22:04] Três critérios juntos: alocação dinâmica, foco em processos, despacho dinâmico.
- [0:23:18] Polimorfismo não é múltiplas assinaturas; resolve na execução a função daquele objeto.
- [0:24:31] No conceito o objeto é um processo, acima de dados e código.
- [0:30:28] Uma estrutura de dados com métodos não é necessariamente um objeto.

Princípios enunciados:

- A disputa de paradigmas simboliza a dificuldade de fazer a coisa certa (0:02:10).
- Eliminar a dicotomia: as questões são frequências distintas da mesma luz (0:03:37).
- O código é uma foto; o código rodando é um filme (0:08:32).
- Polimorfismo resolve na execução qual função daquele nome corre no contexto do objeto (0:23:18).
- O objeto é um processo (0:24:31).
- Uma estrutura de dados com métodos não é necessariamente um objeto (0:30:28).

Código: nenhum. Em 0:30:50 ele diz que vai dar um exemplo de código; a legenda termina em 0:30:52 sem o exemplo.

Paráfrases da legenda (não verificadas):

- o problema da disputa entre paradigmas simboliza a dificuldade de fazer a coisa certa (0:02:10)
- sempre repito o código é uma foto o código rodando é um filme (0:08:32)
- no conceito o objeto é mais, o objeto é algo que está acima de dados e códigos, porque o objeto ele é um processo em si (0:24:22)
- uma estrutura de dados com métodos não é necessariamente um objeto (0:30:28)

### Aula #02: A cesta de maçãs

Vídeo: https://www.youtube.com/watch?v=v134Xr57xbg · 809 s

A aula escreve a cesta como uma sequência de pesos. O primeiro desenho guarda a lista, ordena e deixa o consumidor pedir um índice: ao rodar, o 20 vai para o final, e o diagnóstico é que isso ainda é programação procedural com classes. O segundo desenho pede a mais pesada. Uma forma ordena e devolve; outra usa max sem ordenar. O consumidor deixa de controlar os passos. O fecho redefine encapsulamento: não é o atributo oculto, é a articulação do comportamento.

Linha do tempo:

- [0:00:18] Maçãs pelo peso: 20, 4, 5, 10, 15. Classe com init, sort em self.data, get que devolve um índice.
- [0:02:43] O consumidor chama get no começo e depois no fim; o sort crescente manda o mais pesado para o final.
- [0:04:31] Ao rodar: ordenou e jogou o 20 para o final.
- [0:04:38] Não está fazendo objetos: está programando procedural com classes.
- [0:05:45] O que se quer é a mais pesada, pedida ao objeto. O nome do método não fica audível.
- [0:07:03] O nível de abstração mudou: o consumidor não sabe como a maçã é selecionada, só diz o quê.
- [0:08:18] Dá para não ordenar: a legenda ouve Max selfie ponto data. Funciona (0:08:27).
- [0:08:40] O desenho acoplado controla o processo em vez de delegar a quem é de direito.
- [0:09:30] A superfície de contato entre os dois códigos está muito grande; é preciso reduzi-la.
- [0:10:02] Mais importante do que como faz é o que vai ser feito e por quê.
- [0:11:06] Sai de uma lógica de código e dado para uma lógica de processo.
- [0:12:11] Violação de encapsulamento mesmo sem mexer no data oculto: a capacidade de resolver não está no objeto.

Princípios enunciados:

- Dá para programar procedural com classes; o drama é parar de programar com classes (0:04:38).
- O consumidor acoplado controla o processo; o outro desenho delega (0:08:40).
- Reduzir a superfície de contato (0:09:30).
- Encapsulamento é a articulação do comportamento, não o atributo oculto (0:12:11).
- A dificuldade é definir a fronteira (0:13:24).

Código, reconstruído a partir da narração. O nome da classe, o nome do método que pede a mais pesada e o índice exato do get não são audíveis:

```python
apples = [20, 4, 5, 10, 15]  # 0:00:18

class ...:  # a legenda ouve "coordenador" (0:00:41); o identificador não foi soletrado
    def __init__(self, data):  # [legenda: nit] (0:00:53)
        self.data = data

    def sort(self):
        self.data.sort()  # ordem crescente; o 20 vai para o final (0:03:01, 0:04:31)

    def get(self, index):
        return self.data[index]

# segundo desenho, sem ordenar (0:08:18). A forma ouvida:
#     return max(self.data)
```

Paráfrases da legenda (não verificadas):

- o problema é que eu não estou de objetos aqui eu estou programando procedural com classes (0:04:38)
- o nível de abstração mudou, o consumidor não sabe como esse cara vai selecionar a maçã, ele só vai dizer o que (0:07:03)
- você está violando a articulação do comportamento do cara, a capacidade de resolver o problema não está no objeto, está em quem está consumindo o objeto (0:12:11)

### Aula #03: O ciclo de melhoria contínua

Vídeo: https://www.youtube.com/watch?v=um7FeXbPTQE · 1566 s

Ele retoma que objeto não é a junção de dados com código (0:00:11) e comenta um vídeo em que a premissa é deixar dados serem dados e ações serem ações. Recusa: existe a relação entre a memória e o código, e essa relação facilita ou dificulta o crescimento do projeto (0:02:52, 0:03:04). Narra um slide de palestra de 2012 que manda parar de criar classes, com uma saudação em classe e a mesma coisa numa função parcial. Daí segue para regras que não escalam, quatro naturezas de sistema, e o ciclo de fazer funcionar, fazer direito e, se precisar, fazer ficar rápido.

Linha do tempo:

- [0:00:11] Objeto não é simplesmente a junção de dados com código.
- [0:01:51] Encapsulamento não é sobre atributos. É sobre o comportamento e o processo.
- [0:02:52] Deixar dados serem dados e ações serem ações não basta: existe a relação entre memória e código.
- [0:03:29] Palestra de 2012 [legenda: Jack diglett, na picon]: parar de criar classes. O nome do autor e o evento não são soletrados.
- [0:06:40] O que determina a escolha é como isso vai ser usado.
- [0:07:30] Regras não escalam. O exemplo é a legislação brasileira.
- [0:07:47] Princípios se contradizem, dependem de contexto e são mais sutis do que regras.
- [0:10:46] Qualquer sistema com interação humana é, por definição, complexo.
- [0:15:57] O obstáculo ao bom design somos nós.
- [0:21:10] Só se programa o que se entende e se conhece.
- [0:23:05] Design é bate e volta, incrementos.
- [0:24:11] Ciclos: fazer funcionar, fazer direito e, se precisar, fazer ficar rápido.
- [0:25:00] O processo é mais importante do que o conhecimento. Ser é mais importante do que saber.

Princípios enunciados:

- Encapsulamento é sobre o comportamento e o processo, não sobre atributos (0:01:51).
- Não se trata de como programar. Se trata de que relações o código vai motivar (0:03:11).
- Regras não escalam; princípios dependem de contexto (0:07:30, 0:07:47).
- Enquanto não houver código funcionando com uma forma, não adianta tentar a melhor forma (0:18:10).
- Fazer funcionar, fazer direito e, se precisar, fazer ficar rápido (0:24:11).
- O processo é mais importante do que o conhecimento (0:25:00).

Código, reconstruído a partir da narração dos slides (0:03:50 a 0:06:08). Ele não digita este arquivo. Classe, método e a chamada de partial não foram lidos pela legenda:

```python
class Saudacao:  # "classe de saudação" (0:03:50); o identificador não foi lido
    def __init__(self, saudacao):  # [legenda: esterilizador] (0:03:53)
        self.saudacao = saudacao  # "armazena esse cara no estado do objeto" (0:04:01)

# a outra forma guarda o cumprimento numa função parcial
# [legenda: paixão, função em paz] (0:05:10, 0:05:54)
# a classe fica no heap [legenda: rip] (0:05:43); a parcial guarda o dado por closure [legenda: cloujo] (0:05:58)
```

Paráfrases da legenda (não verificadas):

- encapsulamento não é sobre atributos, é sobre o comportamento, é sobre o processo que envolve aquele código e aquele dado (0:01:51)
- regras não escalam, veja por exemplo a legislação brasileira (0:07:30)
- você precisa de ciclos, você precisa fazer funcionar, fazer direito e se precisar fazer ficar rápido (0:24:11)

### Aula #04: Entendendo o problema

Vídeo: https://www.youtube.com/watch?v=5gLDIvUakIc · 1095 s

Ele roda um game of life no terminal e abre o arquivo, todo em funções, para a turma avaliar locação, relação da memória com o código e vazamento de comportamento (0:02:12). O `main` cria um board, desenha o glider, limpa a tela, imprime e clona, porque não pode mudar o bitmap que está sendo lido (0:04:40). O bitmap é toroide: passou do fim, volta ao começo (0:05:12). O fecho da aula não é se o board é global de módulo. É que tem gente mexendo nele (0:18:04).

Linha do tempo:

- [0:00:32] Roda o game of life: matriz, célula, glider no terminal.
- [0:02:12] Avaliar procedural, estruturado e objetos: locação, memória e código, vazamento de responsabilidade.
- [0:03:08] O main declara um board, tamanho ouvido como 50 por 25, clear com dead (pontinho) e live (barrinha), set do glider.
- [0:04:16] O loop limpa a tela, imprime o board e duplica para um board novo.
- [0:04:40] Não pode usar o mesmo bitmap: clona para mudar o estado do novo a partir do velho.
- [0:04:58] A cópia é a função de deepcopy do próprio Python [legenda: zip cop].
- [0:05:12] Bitmap virado em toroide [legenda: touros].
- [0:07:04] A regra que ele lê: menor que dois morre, maior que três morre; total igual a 3 e célula morta renasce (0:07:31).
- [0:09:06] As funções do board recebem o board: clear, set de várias coordenadas, clone, offset, contains, get e set.
- [0:13:28] As de cima são constantes, em maiúsculo, e não mudam.
- [0:15:12] O board está na pilha do main, não é global do módulo, mas é passado por todos os processos.
- [0:16:45] Variável espalhada importa mais do que o rótulo global.
- [0:18:04] O que importa é que tem gente mexendo nele.

Princípios enunciados:

- Avaliar o código pela locação, pela relação da memória com o código e pelo vazamento para quem chama (0:02:12).
- Não usar o mesmo bitmap: clonar para mudar o novo a partir do velho (0:04:40).
- Uma variável pode não ser global de módulo e ainda assim estar espalhada (0:15:12).
- O que importa é que tem gente mexendo no board (0:18:04).

Código: ele mostra um arquivo já escrito e aponta funções. A legenda não dita corpos. O que fica audível é a forma do loop e a regra lida em voz:

```python
# reconstrução. identificadores ouvidos, não soletrados.
# DEAD pontinho, LIVE barrinha (0:03:48)
# board de 50 por 25 (0:03:17); set do glider (0:04:02)
# loop: system clear, imprime o board, deepcopy para o board novo (0:04:16 a 0:04:58)
# morre se o total é menor que dois ou maior que três (0:07:04)
# total igual a 3 e célula morta: renasce (0:07:31)
```

A regra não fecha de uma leitura para a outra. Em 0:01:12 a legenda também diz que com dois vizinhos ela nasce. Em 0:07:10 a leitura é menor que dois ou mais que três morre, e em 0:07:31 total igual a 3 e célula morta renasce. Sobrevivência com dois vizinhos não é dita na segunda leitura.

Paráfrases da legenda (não verificadas):

- eu não posso usar o mesmo bitmap, eu tenho que clonar o cara para poder mudar o estado do novo a partir do velho (0:04:40)
- entender que é uma variável espalhada no código é mais importante do que se prender se é global ou se não é (0:16:45)
- o que me importa não é se o board é ou não é uma global, o que importa é que tem gente mexendo nele (0:18:04)

### Aula #05: Modelando o problema

Vídeo: https://www.youtube.com/watch?v=wBZllbxUzKE · 413 s

Ele olha o arquivo e diz que está uma zona: todo mundo enxerga todo mundo, com coisa do board, coisa da coordenada e coisa do jogo no mesmo troço (0:00:13). Para ver o que mexe com o quê, gera um gráfico de chamada. As áreas do gráfico indicam onde quebrar em módulos menores, e no Python isso já é encapsulamento. O design com tendência a objetos não é só classe, porque tudo é objeto e o foco é o filme rodando (0:06:21).

Linha do tempo:

- [0:00:13] O código está uma zona: todo mundo enxerga todo mundo.
- [0:00:37] O wrap do jogo, com efeito toroidal, depende do board e está no meio da lógica do game of life. A legenda ouve rap.
- [0:01:10] Gera 0.png com tracing e profile; interrompe com control c e abre o gráfico.
- [0:02:05] Um nó concentra 130 mil chamadas e 14 segundos. Números lidos por ele no gráfico, não medidos de novo aqui.
- [0:03:08] A ferramenta é uma biblioteca Python que trabalha com o que a legenda ouve como graves e gera o gráfico. Ele diz que tem o código e mostra depois (0:03:23).
- [0:05:49] Dá para contornar áreas e quebrar em módulos menores.
- [0:06:10] Módulos menores já encapsulam: isolamento e menos contato.
- [0:06:38] O foco é a interação dos objetos na memória, o filme rodando, e não a classe em específico.

Princípios enunciados:

- Organizar em módulos menores já é encapsulamento (0:06:06).
- Design orientado a objeto não é só classe; o foco é a interação na memória (0:06:21).

Código: nenhum escrito nesta aula. Ele mostra o gráfico e nomeia funções sem ditar corpo.

Paráfrases da legenda (não verificadas):

- aqui tá uma zona, todo mundo enxerga todo mundo (0:00:13)
- organizar o código em módulos menores já é um processo de encapsulamento, você já tá criando um certo isolamento (0:06:06)
- não é só classe, até porque em Python tudo é objeto; o foco é a interação dos objetos na memória, na hora que tiver o filme rodando (0:06:21)

### Aula #06: Desenrolando o novelo

Vídeo: https://www.youtube.com/watch?v=_wKocImKAc4 · 1119 s

É o momento de passar o facão: separar as partes e transformar o game of life num pacote (0:00:06). Ele extrai o bitmap, recoloca os imports para continuar funcionando, e trata a lista de imports como a medida da superfície de contato (0:03:54). X e y só servem aos vizinhos, então uma camada no meio impede que a relação do board com as coordenadas vaze para o jogo (0:06:24). Dois imports viram um. Não há teste: o código vinha de outra coisa, e meter teste agora tiraria o foco da relação (0:07:52). No fim, uma pequena inversão cria o board já em branco e dispensa o clear, e a posse do board começa a ir para o módulo.

Linha do tempo:

- [0:00:06] Passar o facão: separar as partes, criar restrições, virar pacote.
- [0:01:22] A linha de comando passa a executar o módulo. A legenda ouve pai ou menos M game of life.
- [0:01:41] Três grupos: coordenadas, board e game of life. O board é o bitmap.
- [0:03:54] Cada import mostra o tamanho da superfície de contato do game of life com o bitmap.
- [0:06:24] Uma camada no meio encapsula a relação do board com as coordenadas; não interessa o que o cara é, interessa o que ele devolve.
- [0:07:22] Dois imports viram um: mudança pequena, progresso conceitual.
- [0:07:59] Sem teste, porque o código vinha de outra coisa. Teste agora tiraria o foco (0:08:08).
- [0:12:23] Blank no lugar do clear: pequena inversão de dependência, interface menor.
- [0:13:53] Um global no módulo bitmap, e uma função que retorna o board.
- [0:16:51] Função parcial no primeiro parâmetro, como um self desse board. O estágio de ainda passar o board, sem as ferramentas de alto nível, ele chama de intermediário e feio (0:18:01).

Princípios enunciados:

- O import mostra a superfície de contato (0:03:54).
- Não deixar vazar para o cliente uma relação que outro cara já resolve (0:06:24).
- Reduzir dois imports a um é pouco na superfície e muito no conceito (0:07:22).
- Criar já do jeito certo e dispensar o clear reduz a interface (0:12:28).
- Quem detém o board pode ser o módulo, e o primeiro parâmetro fornecido funciona como um self (0:17:10).

Código: nenhum corpo é ditado por completo. O que a legenda sustenta é o gesto, não o arquivo. A troca de x e y por offset é ouvida truncada (0:05:14) e não vira um snippet fiel. A linha de comando ouvida como python -m não foi conferida na tela.

Paráfrases da legenda (não verificadas):

- o importe já tá mostrando qual é o tamanho da superfície de contato do meu game of life para o meu bitmap (0:03:54)
- a gente colocou alguma coisa no meio do caminho que já encapsula esse comportamento, e agora não me interessa o que que é o cara, me interessa que ele vai me retornar o que eu preciso (0:06:24)
- trocou dois imports por um, mas veja o progresso conceitual que a gente teve (0:07:22)

### Aula #07: Montando o bitmap e o board

Vídeo: https://www.youtube.com/watch?v=lCF2rNGAM7I · 901 s

Ele sobe os procedimentos do bitmap para uma classe com self, init e str, e guarda o tabuleiro em self.board. O miolo é o data model do Python: colchetes, atribuição, o in, e um get many que eles criaram (0:08:28). A coordenada começa em 1 e a lista do Python em 0, então o offset de -1 fica no método do protocolo. Acessar o board direto espalha essa compensação (0:03:47, 0:04:00). A classe deixa mudar a implementação do bitmap sem estresse e sem atrito (0:14:08). No fim anuncia uma classe de coordenada que se soma no lugar de chamar uma função de offset (0:14:32).

Linha do tempo:

- [0:00:10] Os procedimentos sobem para uma classe.
- [0:00:41] Init, e o board guardado em self.board (0:00:59).
- [0:01:43] Tamanho como propriedade, sem parêntese.
- [0:03:47] Acessar o board direto espalha a compensação dos acessos de -1.
- [0:04:00] Coordenada começa em 1, a lista do Python começa em 0.
- [0:04:26] A responsabilidade do setitem é fazer a compensação da coordenada.
- [0:05:20] Encapsular métodos e só delegar para baixo, ele diz, equivale a um Adapter. É resposta a uma fala da sala, não uma implementação desta aula.
- [0:08:28] No board entram os protocolos do data model do Python.
- [0:08:53] get many é coisa que eles criaram; o contém existe para o in.
- [0:11:38] Ao rodar: self.board não tem atributo board. O conserto entre esse erro e 0:13:42 não sai limpo na legenda.
- [0:14:08] A classe deixa mudar a implementação do bitmap sem estresse e sem atrito.
- [0:14:32] Em vez de offset, somar duas coordenadas.
- [0:14:51] O desafio é fazer da maneira mais simples.

Princípios enunciados:

- A lógica de acesso fica num lugar; ler o dado por fora espalha o offset (0:03:47).
- O objeto fala os protocolos do data model (0:08:28).
- Conter a implementação numa classe pequena deixa trocá-la sem atrito (0:14:08).
- Fazer da maneira mais simples (0:14:51).

Código, reconstrução. O corpo dos métodos não é ditado. "Classic" lê-se como class (0:00:10). Os nomes setitem, property e contains são leitura da fala (sétimo, cropped, self contra), não identificadores soletrados.

```python
class ...:
    def __init__(...):
        self.board = ...  # 0:00:59

    # tamanho como propriedade, sem parêntese (0:01:43)
    # o -1 mora no método do protocolo: coordenada em 1, lista em 0 (0:04:00)

# criação ouvida com três números, 50, 25 e 10 (0:09:21); o papel de cada um não é dito
# deepcopy passa a receber o board (0:09:41)
# ao rodar: self.board não tem atributo board (0:11:38)
```

Paráfrases da legenda (não verificadas):

- se eu boto o ponto no board eu vou espalhando a lógica, eu vou ter que fazer toda essa compensação dos acessos do -1 (0:03:47)
- a gente aplicou no board os protocolos do Python, as interfaces do data model (0:08:28)
- em vez de fazer um offset eu posso somar duas coordenadas (0:14:32)

### Aula #08: Montando as coordenadas

Vídeo: https://www.youtube.com/watch?v=yUlC6PRSz5E · 701 s

O board já é um objeto, e o offset que sobrou é a falta de um cara que calcule direto (0:00:20). A coordenada nasce como dupla com x e y pelo nome e com soma. No interpretador, coord 1 2 mais coord 3 4 devolve o que ele lê como 4 e 6; uma dupla crua explode (0:08:15). A generalização é envelopar o outro operando. O items deixa de devolver dupla, a região vira coord, o offset sai, e mudar esse lugar só já faz o resto funcionar: o game of life passa a mexer só no board (0:11:12).

Linha do tempo:

- [0:00:20] Offset é falta de um objeto que deixe calcular direto.
- [0:00:55] Dois procedimentos conflitantes é que demandam a fatoração para extrair a orientação a objetos. A etapa extra ele mostra mais na frente; não está nesta aula.
- [0:01:46] No gráfico, a hierarquia é game of life, bitmap, board.
- [0:04:39] A coordenada é uma dupla com parâmetros nomeados.
- [0:05:52] Acessar as posições pelo nome, x e y, primeiro e último.
- [0:06:23] A soma, ouvida como EDGE, retorna um coord novo.
- [0:06:56] Mantém o comportamento de dupla, porque o resto do código usa dupla.
- [0:08:05] No interpretador, collections. A palavra namedtuple não sai limpa.
- [0:08:15] Coord 1 2 mais coord 3 4 deu 4 e 6. A dupla 2 3 explode (0:08:24).
- [0:09:07] Para funcionar com qualquer um, envelopar o outro no coord.
- [0:10:10] O items não pode devolver dupla; o bitmap força a relação com as coordenadas.
- [0:11:12] Mudaram um lugar e funcionou. A interface encolhe: o game of life só mexe no board (0:11:22).

Princípios enunciados:

- A fatoração que extrai objetos é demandada por procedimentos que conflitam (0:00:55).
- Manter o comportamento que o resto já usa, aqui a dupla (0:06:56).
- Um lugar só que mexe é capaz de já funcionar com tudo (0:10:46).
- Com o offset fora, o jogo só mexe no board (0:11:22).

Código, reconstrução do que ele descreve no interpretador. A base da classe não se recupera. A soma é ouvida como EDGE.

```python
# "uma classe que é uma dupla" com x e y pelo nome (0:05:52)
# collections no interpretador (0:08:05); namedtuple não é dito por extenso

# Coord(1, 2) + Coord(3, 4)  -> ele lê 4 e 6 (0:08:15)
# Coord(1, 2) + (2, 3)       -> explode (0:08:24)
# generalização descrita, linha não ditada: envelopar o outro no coord (0:09:07)
```

Paráfrases da legenda (não verificadas):

- offset é falta de ter um cara que permite calcular as coisas diretamente (0:00:20)
- dois procedimentos conflitantes que vão demandar a fatoração para extrair de fato a orientação a objetos (0:00:55)
- mudamos um lugar e a coisa funcionou, reduzimos ainda mais a interface, agora o game of life só mexe no board (0:11:12)

### Aula #09: Separando as responsabilidades do main

Vídeo: https://www.youtube.com/watch?v=LIVog4qc-EI · 1167 s

No que ainda sobra no fluxo, falta um nível: uma classe game of life separada do controle de entrada e saída (0:00:30). Ele come pelas beiradas. Extrai um update que recebe o board e devolve um newboard, manda o print para um show, e deixa o sleep no loop, porque o sleep controla a velocidade e o show plota na tela (0:03:56). Sem a distração do loop, o que incomoda no update é o wrap: se o board é toroidal, esse comportamento é dele (0:05:10). Leva o wrap para o board. O update fica com vizinhos, get many e a conta de quantos estão vivos (0:17:45).

Linha do tempo:

- [0:00:30] Falta uma classe game of life separando o controle de entrada e saída.
- [0:01:33] Diante de código duro, comer pelas beiradas.
- [0:02:15] O trecho que replica e atualiza é um update: recebe o board e retorna o newboard.
- [0:03:11] O print vai para baixo da atualização. Isso é um show.
- [0:03:56] O sleep fica no loop. O show plota na tela.
- [0:05:10] Ser toroidal é propriedade do board, não um detalhe solto no update.
- [0:07:28] O offset vira um método, que ele chama de index, com self e a coordenada.
- [0:09:13] A conta do wrap usa módulo, para não repetir a lógica em dois lugares (0:08:53).
- [0:12:31] O teste do cliente estoura: a dupla não suporta a operação ouvida como menos (0:13:02).
- [0:14:31] Normaliza para acessar como tupla ou como coordenada, porque outros lugares usam dupla.
- [0:15:27] Testa o setup como board toroidal e funciona: o bicho aparece em cima.
- [0:17:00] Levou a capacidade para o board porque ela depende do board.
- [0:18:58] O ideal encapsulado seria perguntar quantos vizinhos vivos existem. Se a live precisa aparecer fica em aberto até a aula #10.

Princípios enunciados:

- Separar o jogo do controle de entrada e saída (0:00:30).
- Comer pelas beiradas (0:01:33).
- O controle da velocidade é do loop; o show plota na tela (0:03:56).
- O comportamento mora onde está a dependência (0:17:00).
- Não repetir a mesma lógica em dois lugares (0:08:53).
- Manter a interface de tupla enquanto também se acessa como coordenada (0:14:31).

Código, reconstrução. Os corpos não foram ditados.

```python
def update(board):
    return newboard  # "vai receber o board e vai retornar o newboard" (0:02:15)

def show(board):
    print(board)  # "o show plota na tela" (0:04:07)

# o sleep fica no loop (0:03:56)
# index(self, cord): a conta do wrap com módulo (0:07:28, 0:09:13)
# self.witch e selfie na legenda não são nomes confiáveis; o sentido é módulo pelo tamanho do board
```

Paráfrases da legenda (não verificadas):

- tá faltando alguma classe game of life separando o controle da entrada e saída (0:00:30)
- o sleep não vai para dentro do show porque tá controlando a velocidade, o controle é do loop, o que o show faz é plotar na tela (0:03:56)
- eu levei essa capacidade para o board porque ele depende muito do board, então tá faltando um comportamento lá (0:17:00)

### Aula #10: CLI e GUI

Vídeo: https://www.youtube.com/watch?v=IwBouxcYO08 · 2206 s

Alguém pergunta se a refatoração foi só para melhorar a visualização. Ele responde que o motivo é harmonizar dado e código: um dado não fica manipulado por muita gente, e as interfaces encapsulam os comportamentos com o que a linguagem permite (0:00:14). Extrai o que vai para a linha de comando. Para a GUI usa o Tk: janela, canvas, pack, e o loop de eventos, no qual ele não manda. Encaixa o update com after, porque o Tk prende no loop (0:07:27). A primeira execução estoura; em seguida o mesmo código, a mesma lógica, com as interfaces mantidas, é consumido pela interface gráfica e pela de comando (0:14:02). O show deixa de precisar conhecer o board e passa a mostrar os que estão vivos (0:16:55). Uma classe game of life, no desenho que ele atribui a uma sugestão da sala, oculta o estado: o next atualiza e devolve a lista dos vivos, o str devolve o str do board (0:24:33, 0:27:06). Sem argumento, roda a linha de comando; passando o que a legenda ouve como sdf, abre a interface (0:29:44). No fechamento diz que vai botar no GitHub e que o link fica embaixo do vídeo (0:35:16). Não fala URL.

Linha do tempo:

- [0:00:14] Harmonizar dado e código, memória e código. A pergunta ouvida não cita um título de livro legível.
- [0:01:39] A interface com os outros módulos encolhe: ficam setup e update.
- [0:02:26] GUI com Tk. Janela, canvas, pack, loop.
- [0:07:27] O Tk prende no loop de eventos. Ele usa after. A legenda diz 10 milissegundos (0:07:30) e também zero (0:07:51).
- [0:08:20] O board não pode ficar preso na stack de dentro do run; usa o board de fora. A palavra ouvida é louco; não tratar como identificador.
- [0:12:07] Implementa a multiplicação da coordenada por um escalar, para o retângulo no canvas. O nome do método na legenda é Dermo.
- [0:14:02] Mesmo código, mesma lógica, interfaces mantidas, duas formas de consumir.
- [0:14:33] O bicho faz o toro e reaparece em cima.
- [0:16:55] O show não precisa conhecer o board. Mostra os que estão vivos.
- [0:19:38] Estão sempre lapidando a fronteira.
- [0:22:06] Sistemas complexos se relacionam na dinâmica; relação física no código amarra.
- [0:24:08] Adapter: a classe oculta o estado do jogo. O next, que ele chama de mais pitônico, devolve a live (0:25:36).
- [0:29:44] Sem argumento, linha de comando. Com o argumento ouvido como sdf, abre a interface.
- [0:31:19] No init do pacote, o que faz sentido é reexportar a classe, não o corpo do código.
- [0:33:14] A única herança no monte de classes ele usa com foco em especialização, em classe sua ou feita para estender (0:33:23).
- [0:34:04] Os métodos underscore são interfaces da própria linguagem.
- [0:35:16] Vai botar no GitHub; o linkzinho fica embaixo do vídeo. Sem URL.

Princípios enunciados:

- Harmonizar dado e código: o dado não fica manipulado em muitos lugares (0:00:14).
- Interfaces mantidas, o mesmo código tem duas formas de consumo (0:14:05).
- Lapidar a fronteira (0:19:38).
- A relação entre sistemas vive na dinâmica, não amarrada fisicamente no código (0:22:12).
- A classe define interfaces e oculta o estado do jogo (0:27:16).
- Herança com foco em especialização, de classe sua ou desenhada para ser estendida (0:33:14). Frameworks ele não é muito fã, e romper o contrato é fácil (0:33:48).
- Performance pode esperar; a organização já permite tunar depois (0:30:42).

Código, reconstrução. Nomes de Tk, Canvas e `__next__` são leitura da fala (Man Windows, meio loop, next mais pitônico), não uma cópia de arquivo.

```python
# o cli continua função: setup, update, show, sleep no loop (0:02:01, 0:03:56 da aula #09)
# a GUI: janela Tk, Canvas, pack, after que se reagenda, mainloop (0:02:26, 0:07:27)
# show deixa de receber o board e passa a pintar as coordenadas vivas (0:16:55, 0:18:49)

class GameOfLife:  # "adapter"; estrutura que ele atribui a uma sugestão da sala (0:27:06)
    def __next__(self):  # "mais pitônico" (0:24:33)
        # update, devolve a lista dos vivos (0:25:36)
        ...
    def __str__(self):
        # devolve o str do board, para a linha de comando (0:28:30)
        ...

# sem argumento: linha de comando; com o argumento ouvido como sdf: a GUI (0:29:44)
# pacote: from game of life import game of life, a classe vinda do core (0:31:42)
# "from Life" também é dito (0:31:51); os dois registros ficam, sem escolher um
```

Paráfrases da legenda (não verificadas):

- a gente está tentando harmonizar a relação entre dado e código, memória e código, evitando que um dado fique sendo usado em muito lugar (0:00:14)
- mesmo código, mesma lógica, interfaces mantidas, e tem duas formas de consumir (0:14:02)
- na hora que eu estruturo relações entre eles direto, fisicamente no código, eu tô me amarrando (0:22:12)
- eu vou botar no github, você vai poder pegar o linkzinho aqui do vídeo aqui embaixo que eu vou botar (0:35:14)

## 6. Princípios que atravessam toda a série

Doze regras que ele formula na fala. Nenhuma é inferência deste documento; cada uma traz a aula e o timestamp onde é dita.

#### 1. Elimine a dicotomia

A disputa de paradigmas simboliza a dificuldade de fazer a coisa certa (aula #01, 0:02:10). Dicotomia é o ou exclusivo (0:04:38). As questões são frequências distintas da mesma luz (0:03:37).

#### 2. O objeto é um processo

No conceito o objeto está acima de dados e código, porque o objeto é um processo (aula #01, 0:24:31). Uma estrutura de dados com métodos não é necessariamente um objeto (0:30:28). Dá para programar procedural com classes (aula #02, 0:04:38).

#### 3. Encapsulamento é articulação do comportamento

Não é o atributo oculto. A capacidade de resolver fica no objeto, não em quem consome (aula #02, 0:12:11). Encapsulamento é sobre o comportamento e o processo que envolve aquele código e aquele dado (aula #03, 0:01:51).

#### 4. Reduza a superfície de contato

A superfície entre dois códigos tem de ser reduzida (aula #02, 0:09:30). O import mede essa superfície (aula #06, 0:03:54). Trocar dois imports por um é o progresso conceitual (0:07:22).

#### 5. A relação vive na dinâmica

Sistemas complexos se relacionam na vida dos caras. Relação estruturada direto, fisicamente no código, amarra (aula #10, 0:22:06). O alvo é harmonizar memória e código para o dado não ser manipulado por muita gente (0:00:14).

#### 6. Variável espalhada importa mais que o rótulo

O board na pilha do main, passado a todas as funções, tem jeito de global (aula #04, 0:15:12). O que importa é que tem gente mexendo nele (0:18:04).

#### 7. Regras não escalam

Regras não escalam (aula #03, 0:07:30). Princípios se contradizem e dependem de contexto (0:07:47). Não existe a resposta que resolve tudo (0:08:49).

#### 8. Fazer funcionar, fazer direito, ficar rápido

O ciclo é fazer funcionar, fazer direito e, se precisar, fazer ficar rápido, enxugando escopo (aula #03, 0:24:11). Enquanto não houver uma forma funcionando, não adianta a melhor forma (0:18:10). Performance espera a organização (aula #10, 0:30:42).

#### 9. Módulo menor já encapsula

Organizar em módulos menores já isola e reduz contato (aula #05, 0:06:06). O foco não é a classe: é a interação dos objetos na memória (0:06:38).

#### 10. O comportamento mora onde está a dependência

Se depende do board, falta comportamento no board (aula #09, 0:17:00). Acessar o dado direto espalha a compensação; o protocolo é que compensa (aula #07, 0:03:47). Uma lógica não se repete em dois lugares (aula #09, 0:08:53).

#### 11. Comer pelas beiradas e manter funcionando

Diante de código duro, comer pelas beiradas (aula #09, 0:01:33). Cada extração continua funcionando (aula #06, 0:01:27). Estão sempre lapidando a fronteira (aula #10, 0:19:38).

#### 12. Herança para especializar classe sua

A única herança no monte de classes ele usa com foco em especialização (aula #10, 0:33:14), em classe sua ou desenhada para ser estendida (0:33:23). Romper o contrato da herança é fácil (0:33:48). Os métodos underscore são as interfaces da própria linguagem (0:34:04).

## 7. Citações-chave do curso

Paráfrases de legenda automática, sem aspas e não verificadas contra o vídeo. Mis-hearings evidentes anotados entre colchetes.

| Aula | Timestamp | Paráfrase |
|---|---|---|
| #01 | 0:02:10 | a disputa entre paradigmas simboliza a dificuldade de fazer a coisa certa |
| #01 | 0:08:32 | o código é uma foto, o código rodando é um filme |
| #01 | 0:23:18 | o polimorfismo não é funções com múltiplas assinaturas |
| #01 | 0:24:31 | o objeto ele é um processo em si |
| #01 | 0:30:28 | uma estrutura de dados com métodos não é necessariamente um objeto |
| #02 | 0:04:38 | eu estou programando procedural com classes |
| #02 | 0:09:30 | superfície de contato |
| #02 | 0:12:11 | violação de encapsulamento, a capacidade de resolver o problema não está no objeto |
| #03 | 0:01:51 | encapsulamento não é sobre atributos, é sobre o comportamento e o processo |
| #03 | 0:07:30 | regras não escalam |
| #03 | 0:24:11 | fazer funcionar, fazer direito e se precisar fazer ficar rápido |
| #04 | 0:04:40 | clonar para mudar o estado do novo a partir do velho |
| #04 | 0:18:04 | o que importa é que tem gente mexendo nele |
| #05 | 0:00:13 | aqui tá uma zona, todo mundo enxerga todo mundo |
| #05 | 0:06:06 | módulos menores já é um processo de encapsulamento |
| #06 | 0:03:54 | o importe já tá mostrando o tamanho da superfície de contato |
| #06 | 0:07:22 | trocou dois imports por um, mas veja o progresso conceitual |
| #07 | 0:03:47 | acessar o board direto espalha a compensação do -1 |
| #07 | 0:08:28 | protocolos do Python, interfaces do data model |
| #08 | 0:11:12 | mudamos um lugar e a coisa funcionou, o game of life só mexe no board |
| #09 | 0:03:56 | o sleep controla a velocidade, o show plota na tela |
| #09 | 0:17:00 | depende do board, então tá faltando um comportamento lá no board |
| #10 | 0:00:14 | harmonizar a relação entre dado e código, memória e código |
| #10 | 0:14:02 | mesmo código, mesma lógica, interfaces mantidas, duas formas de consumir |
| #10 | 0:22:12 | relação direta, fisicamente no código, eu tô me amarrando |
| #10 | 0:35:14 | eu vou botar no github, o linkzinho aqui do vídeo aqui embaixo |

## 8. A evolução técnica, aula a aula

| Etapa | O que é feito | Conceito ou ferramenta | O que isso destrava |
|---|---|---|---|
| **#01** | Exposição, sem código (0:00:12 a 0:30:52) | Procedural, Algol, Simula, despacho | O objeto como processo, não como dados com métodos (0:24:31, 0:30:28) |
| **#02** | Cesta de pesos no editor (0:00:18 a 0:13:24) | sort e get versus pedir a mais pesada; max | Procedural com classes versus delegar o processo (0:04:38, 0:12:11) |
| **#03** | Slides e o ciclo (0:00:11 a 0:25:53) | Regras, princípios, quatro naturezas de sistema | Fazer funcionar antes da melhor forma (0:18:10, 0:24:11) |
| **#04** | Game of life já escrito, em funções (0:00:32 a 0:18:06) | deepcopy, toroide, board passado adiante | O critério: tem gente mexendo no dado (0:18:04) |
| **#05** | Gráfico de chamada (0:01:10 a 0:06:38) | Tracing, áreas no grafo | Onde quebrar em módulos (0:05:49) |
| **#06** | Pacote e extração do bitmap (0:00:06 a 0:18:28) | Imports, offset, blank no lugar do clear | A superfície de contato fica visível e encolhe (0:03:54, 0:07:22) |
| **#07** | Classe do board (0:00:10 a 0:14:51) | Data model, offset de -1 no setitem | Trocar a implementação sem espalhar a compensação (0:03:47, 0:14:08) |
| **#08** | Classe da coordenada (0:04:23 a 0:11:22) | Dupla nomeada, soma | Um lugar muda, o offset sai, o jogo só mexe no board (0:11:12) |
| **#09** | Update, show e loop (0:00:30 a 0:19:15) | Wrap vai para o board | O update fica só com o que é update (0:17:45) |
| **#10** | CLI e GUI (0:00:14 a 0:36:24) | Tk, after, live, next | A mesma lógica, duas formas de consumo, estado oculto (0:14:02, 0:27:16) |

## 9. Arsenal técnico demonstrado no curso

| Técnica ou recurso | Para que ele usa | Aula e timestamp |
|---|---|---|
| Foto e filme | Separar o texto do código da execução | #01, 0:08:32 |
| Pilha e retorno | Mostrar por que a memória da estruturada some | #01, 0:13:07 |
| Heap [legenda: rip] | O dado que continua depois do retorno, no Simula e no objeto da saudação | #01, 0:19:47; #03, 0:05:43 |
| Despacho dinâmico | Achar a função daquele objeto na execução | #01, 0:22:24 |
| `list.sort` e `max` | Dois jeitos de achar a maçã mais pesada; o segundo não expõe o como | #02, 0:03:01 e 0:08:18 |
| `functools.partial` [legenda: função parcial, paixão] | Guardar o cumprimento sem classe | #03, 0:05:10 |
| Análise ciclomática | Medir quantas coisas se relacionam com quantas coisas | #03, 0:14:06 |
| `deepcopy` [legenda: zip cop] | Clonar o board para não alterar o que está sendo lido | #04, 0:04:58 |
| Toroide [legenda: touros, rap] | Vizinho que passou do fim volta ao começo | #04, 0:05:12 |
| Gráfico de chamada, saída 0.png | Ver o que mexe com o quê antes de partir o arquivo | #05, 0:01:10 |
| Pacote e execução como módulo | A legenda ouve python -m; não conferido na tela | #06, 0:01:22 |
| Imports | Medir a superfície de contato | #06, 0:03:54 |
| Data model: colchetes, `in`, propriedade | O board fala os protocolos do Python | #07, 0:08:28 |
| Offset -1 | Coordenada que começa em 1, lista que começa em 0 | #07, 0:04:00 |
| `collections` e dupla nomeada | Coordenada com x e y; namedtuple não é dito por extenso | #08, 0:05:52 e 0:08:05 |
| Soma de coordenadas | Substitui a função de offset | #08, 0:06:23 |
| `update` / `show` / `sleep` | Jogo, plotagem e velocidade em lugares diferentes | #09, 0:02:15 e 0:03:56 |
| Tk, Canvas, `after` | A GUI não controla o loop; encaixa o update no loop de eventos | #10, 0:02:26 e 0:07:27 |
| `__next__` e `__str__` | O next devolve os vivos; o str serve à linha de comando. Nomes ouvidos, não soletrados | #10, 0:24:33 e 0:28:30 |
| Reexport no init do pacote | A classe disponível de fora, não o corpo | #10, 0:31:19 |

## 10. Glossário do curso

| Termo | Significado no contexto da série | Onde |
|---|---|---|
| **Dicotomia** | O ou exclusivo entre paradigmas, certo ou errado | #01, 0:04:38 |
| **Foto e filme** | O código escrito e o código rodando | #01, 0:08:32 |
| **Procedimento** | Checklist, sequência de passos; não é função | #01, 0:10:04 |
| **Despacho dinâmico** | Achar, na execução, a função daquele nome no contexto daquele objeto | #01, 0:22:24 |
| **Polimorfismo** | Esse despacho; não é múltiplas assinaturas | #01, 0:23:18 |
| **Processo** | O que o objeto é, acima de dados e código | #01, 0:24:31 |
| **Serviço** | O que o objeto provê; a implementação é detalhe | #01, 0:28:12 |
| **Superfície de contato** | O quanto dois códigos se tocam; depois, o que a lista de imports mede | #02, 0:09:30; #06, 0:03:54 |
| **Articulação do comportamento** | O nome que ele dá ao encapsulamento quando a capacidade de resolver está no objeto | #02, 0:12:25 |
| **Fronteira** | O corte entre consumidor e objeto, lapidado ao longo da série | #02, 0:13:24; #10, 0:19:38 |
| **Regras e princípios** | Regras não escalam; princípios dependem de contexto | #03, 0:07:30 |
| **Fazer funcionar, fazer direito, fazer ficar rápido** | O ciclo, com escopo enxuto | #03, 0:24:13 |
| **Variável espalhada** | Dado passado a todo mundo, mesmo sem ser global de módulo | #04, 0:16:45 |
| **Board** | O bitmap do jogo. A legenda também ouve bode e borde | #04, 0:03:11 |
| **Toroide** | O bitmap em que a borda continua do outro lado | #04, 0:05:12 |
| **Módulo** | Unidade menor que já isola; no Python, com natureza de objeto | #05, 0:06:06 |
| **Inversão de dependência** | O nome que ele dá a criar o board já em branco e dispensar o clear | #06, 0:12:30 |
| **Data model** | Os protocolos do Python no objeto: colchetes, atribuição, in | #07, 0:08:28 |
| **Coordenada** | Dupla com x e y pelo nome, que se soma | #08, 0:05:52 |
| **Update** | Recebe o board e devolve o board novo | #09, 0:02:15 |
| **Show** | Plota na tela; não controla a velocidade | #09, 0:04:07 |
| **Live** | A lista do que está vivo, para o show não precisar do board | #10, 0:18:49 |
| **Adapter** | A classe game of life por cima do que já existia, ocultando o estado | #10, 0:24:08 |

## 11. Perguntas e respostas que o curso responde

#### Procedural ou objetos: qual é o certo?

Nenhum dos dois como ou exclusivo. A disputa simboliza a dificuldade de fazer a coisa certa, e as duas questões são frequências da mesma luz (aula #01, 0:02:10 e 0:03:37).

#### Objeto é dados mais código?

No conceito, não. O objeto é um processo (aula #01, 0:24:31). Uma estrutura de dados com métodos não é necessariamente um objeto (0:30:28). A cesta que ordena e deixa o consumidor pedir o índice ainda é procedural com classes (aula #02, 0:04:38).

#### Encapsular é deixar o atributo privado?

Não. É a articulação do comportamento: quem resolve é o objeto, não quem consome (aula #02, 0:12:11; aula #03, 0:01:51).

#### Por que a superfície de contato importa?

Porque quanto maior o contato, mais o consumidor controla o processo do outro (aula #02, 0:09:30). No código, essa superfície aparece na lista de imports (aula #06, 0:03:54). Entre sistemas, o contato que fica amarrado no código impede a relação de acontecer na dinâmica (aula #10, 0:22:06).

#### O board do game of life é uma variável global?

Está na pilha do main e é passado a todas as funções (aula #04, 0:15:12). O rótulo importa menos do que o fato de ter gente mexendo nele (0:18:04).

#### Quando partir o arquivo?

Depois de ver o que mexe com o quê, num gráfico de chamada (aula #05, 0:02:24), e mantendo o programa funcionando a cada corte (aula #06, 0:01:27).

#### Onde mora o wrap toroidal?

No board, porque depende do board (aula #09, 0:05:10 e 0:17:00). A compensação entre coordenada que começa em 1 e lista que começa em 0 mora no protocolo, não em quem acessa o dado direto (aula #07, 0:04:00).

#### Dá para a mesma lógica ter CLI e GUI?

Sim, se as interfaces se mantêm: o mesmo código, duas formas de consumir (aula #10, 0:14:02). O show deixa de conhecer o board e recebe quem está vivo (0:16:55).

#### Herança aqui?

Uma, com foco em especialização, de classe sua ou feita para estender (aula #10, 0:33:14). Ele prefere os métodos underscore, interfaces da própria linguagem (0:34:04).

## 12. Repositórios e recursos

| Recurso | Onde encontrar | Observação |
|---|---|---|
| Playlist completa (fonte desta documentação) | [Transforme seu código Procedural em Orientado a Objetos](https://www.youtube.com/playlist?list=PLeKXYyZCJHxeKQ13fuBUuLyfeOK9Jr8t7) | 10 vídeos; ids `413wIxuhy2w`, `v134Xr57xbg`, `um7FeXbPTQE`, `5gLDIvUakIc`, `wBZllbxUzKE`, `_wKocImKAc4`, `lCF2rNGAM7I`, `yUlC6PRSz5E`, `LIVog4qc-EI`, `IwBouxcYO08`. |
| Canal | [HB Network](https://www.youtube.com/@hbnetworkoficial) | |
| GitHub anunciado | não falado | Aula #10, 0:35:14: ele vai botar no GitHub e o link fica embaixo do vídeo. Sem usuário, repositório ou caminho. |
| Código do trace do gráfico | anunciado, não mostrado | Aula #05, 0:03:23: ele diz que tem o código e mostra depois. Não mostra nesta aula. |
| Código do jogo | "de outra coisa" | Aula #06, 0:08:02: por isso não tem teste. Não diz de qual projeto. |
| Vídeo comentado na aula #03 | Brian Will, ouvido na legenda | 0:00:22 e 0:02:27. Sem URL. |
| Palestra de 2012 sobre parar de criar classes | [legenda: Jack diglett, na picon] | Aula #03, 0:03:29. Nome e evento não soletrados. Sem URL. |
| Série curta sobre o mesmo vocabulário | `kb/courses/raio-x-da-oo.md` | Classe, data model e "orientação a objetos não é criar classes" são o contato. Esta série parte de código procedural já escrito. |

Repositório do instrutor para esta série: **nenhum URL nesta transcrição**. Esta documentação não foi ao GitHub procurá-lo, e não lista reimplementação de comunidade.

## 13. Análise linha a linha do código real

Não há código publicado com caminho, commit ou URL para esta série, portanto não há análise de código real. O que existe é o que ele digita ao vivo, e esse código está reconstruído na seção 5, aula por aula, marcado como reconstrução. Limites que ficam registrados:

- A aula #01 anuncia um exemplo e a legenda acaba antes dele (0:30:50).
- Na aula #02 o nome da classe, o método da maçã mais pesada e o índice do get não são audíveis.
- Na aula #03 os slides de saudação e de partial não foram lidos identificador por identificador.
- Da aula #04 à #10 ele aponta um arquivo já existente e o vai cortando. A legenda não dita corpos. Nomes como wrap, setitem, namedtuple, Tk, Canvas, `__next__` e `python -m` são leitura do que a fala parece dizer, anotados como tal na seção 5.
- A regra do game of life não fecha entre 0:01:12 e 0:07:31 da aula #04. As duas leituras ficam na seção 5, sem escolher uma.
- A aula #10, 0:35:16, promete um link de GitHub embaixo do vídeo e não fala o endereço.

## 14. Execução real dos testes

O curso não publicou código nem testes. Na aula #06 ele diz que não há teste porque o código vinha de outra coisa, e que não vai meter teste naquela hora para não tirar o foco (0:07:59). Não há suíte para executar.

As reconstruções da seção 5 não foram executadas como programa do curso: faltam corpos, nomes e a regra fechada do jogo. O único fragmento audível o bastante para uma checagem é o do interpretador na aula #08. Ele diz que coord 1 2 mais coord 3 4 deu 4 e 6 (0:08:15) e que a dupla 2 3 explode (0:08:24), e em seguida descreve envelopar o outro operando (0:09:07). A base da classe não é dita; `namedtuple` não aparece por extenso, só `collections` (0:08:05). A reconstrução abaixo é deste documento, não código dele. Rodou em Python 3 nesta sessão:

| Comportamento narrado | Aula e timestamp | Resultado da reconstrução |
|---|---|---|
| Coord 1 2 mais coord 3 4 dá 4 e 6 | #08, 0:08:15 | `Coord(x=4, y=6)`, igual à dupla `(4, 6)` |
| Dupla crua 2 3 explode, antes de envelopar | #08, 0:08:24 | `AttributeError: 'tuple' object has no attribute 'x'` |
| Envelopar o outro no coord | #08, 0:09:07 | `Coord(1, 2) + (2, 3)` devolve `Coord(x=3, y=5)` |

O script ficou fora do repositório. Nada do que ele produz é código do curso. O game of life, o Tk e a cesta de maçãs não foram executados.

---

Documentação elaborada a partir das transcrições automáticas das 10 aulas da playlist Transforme seu código Procedural em Orientado a Objetos, de Henrique Bastos (HB Network), playlist `PLeKXYyZCJHxeKQ13fuBUuLyfeOK9Jr8t7`, legendas em português (pt-orig) capturadas em 2026-10-09. As citações são paráfrases das legendas automáticas, não verificadas contra o vídeo (`verified: false`), renderizadas sem aspas e com os erros de reconhecimento de fala anotados entre colchetes quando precisam aparecer. O curso não publica URL de repositório nesta transcrição: a aula #10 (`IwBouxcYO08`, 0:35:16) diz que o código vai para o GitHub e que o link fica embaixo do vídeo. Todo o código desta documentação é reconstrução a partir da narração, marcada como tal na seção 5. A seção 14 registra apenas a reconstrução mínima do interpretador da aula #08. Datas de publicação e visualizações não foram coletadas. Conteúdo de caráter educativo.
