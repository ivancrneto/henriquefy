<!-- written by the henrique-ingest distiller on 2026-11-12 from sources/transcripts/labirinto-dos-testes/; see kb/courses/README.md for provenance and license -->

HB Network · Documentação de curso

# Superando o Labirinto dos Testes de Software

As 8 aulas da playlist, lidas aula a aula a partir das legendas automáticas. É uma única aula ao vivo, com turma de microfone aberto e chat, conduzida por um mapa mental que ele vai percorrendo na tela e recortada em oito vídeos. Não há código ao vivo: é um curso conceitual sobre o que é teste, por que é difícil, como escolher o que testar e como começar. Primeiro monta o universo dos testes, da origem histórica à crítica da indústria de QA (aula 1), depois desmistifica o teste como caça a defeitos que aumenta a confiança (aula 2), mostra por que testar é difícil e como pôr teste em código legado sem reengenharia (aula 3), diz como começar, com passos de bebê e testando o efeito (aula 4), organiza os tipos de teste (aula 5), descreve a anatomia de um framework de testes e dos dublês (aula 6), dá as recomendações práticas e o método de quatro etapas para legado (aula 7) e fecha dando de presente o Raio-X do TDD para a prática (aula 8).

Instrutor: **Henrique Bastos** · Canal [HB Network](https://www.youtube.com/@hbnetworkoficial) · Playlist: [Superando o Labirinto dos Testes de Software](https://www.youtube.com/playlist?list=PLeKXYyZCJHxfGaSISKQtt4we_3wmuZEzg) · Repositório: nenhum (o curso não escreve código)

Documento elaborado a partir das transcrições das 8 aulas (legenda automática em português, pt-orig, capturada em 2026-11-12). A legenda não marca quem fala. Trechos de fala de participantes identificados pela mudança de interlocutor ou pela leitura do chat: aula 1, 0:12:32 a 0:12:44 (comentário de um participante que trabalha com seguros, lido por ele) e 0:23:24 a 0:23:36 (comentário do chat sobre implantar Scrum); aula 3, 0:00:12 a 0:02:30 (vários participantes respondem por que testar é difícil), 0:12:13 a 0:12:23 (pergunta do chat sobre estratégia bottom up, lida por ele) e 0:15:20 a 0:15:44 (respostas do chat ao que o teste não é, lidas e aprovadas por ele); aula 5, 0:11:29 a 0:11:41 (um participante descreve mudar um valor para ver se o teste quebra), 0:14:52 a 0:15:16 (um participante define teste unitário), 0:15:48 (o exemplo do cadastro de pessoa com validação de CPF veio de um participante), 0:20:32 a 0:20:42 (provável participante: o chuveiro como smoke test), 0:21:41 a 0:22:09 (pergunta sobre a biblioteca Hypothesis) e 0:24:20 a 0:24:31 (provável participante: estresse comparado a DDoS); aula 6, 0:07:05 a 0:07:15 (pergunta sobre Postgres e SQLite, parafraseada por ele). Esses trechos não são atribuídos a ele em nenhuma seção, e os participantes não são nomeados, embora ele os chame pelo nome na fala.

## 1. Visão geral do curso

Superando o Labirinto dos Testes de Software é uma série de **8 vídeos** que somam **7.930 segundos, 2 horas, 12 minutos e 10 segundos**. Ele abre dizendo que preparou um mapa mental que vai guiar a turma passo a passo na exploração do labirinto que é o universo de teste (aula 1, 0:00:00 a 0:00:13), e fecha dizendo que o teste é sempre o mínimo necessário e é muito mais um processo de como se aborda o desenvolvimento de software do que qualquer outra coisa (aula 8, 0:00:00 a 0:00:25). Entre um e outro há quatro blocos: o contexto (aulas 1 e 2), a mentalidade (aulas 3 e 4), o vocabulário (aulas 5 e 6) e a prática recomendada (aulas 7 e 8).

| Dimensão | Valor | Observação |
|---|---|---|
| Aulas | 8 | Playlist completa, numerada de #01 a #08. |
| Duração total | 7.930 s (2h 12min 10s) | Soma das durações em `playlist.json`. |
| Aula mais curta / mais longa | 201 s (#8) / 2.113 s (#1) | A #1, O Universo dos Testes, é 27% do curso. |
| Datas de publicação | não coletadas | O `playlist.json` desta coleta traz id, título e duração. Ele situa a fala em 2020 (aula 2, 0:04:10; aula 4, 0:02:21). |
| Visualizações | não coletadas | Idem. |
| Transcrições | 8 de 8 disponíveis | Todas em legenda automática (pt-orig). Não há legenda humana nem transcrição Whisper. |
| Formato | aula ao vivo com mapa mental | Microfones abertos e chat; ele lê e responde comentários ao longo da aula. |
| Legenda ruidosa | nomes e siglas | Kent Beck sai como quente back e kateback, Myers como Mayer, Ward Cunningham como Word cunning, TDD como DDD, mock como Moque, Moc e Nokia, stub como estúdio, estabele e Stanley, dummy como Dani, teardown como terdão, fixture como fique e Fiction, fuzz como fase e fãs, debugger como the bug e the Burger. Lista completa no glossário e na seção 13. |
| Código do curso | nenhum | Ele não escreve código. Os exemplos são falados (faixa de idade, cliente do GitHub, envio de e-mail); a seção 5 traz reconstruções a partir da fala, marcadas como tal. |
| Fim da aula #7 | legenda cortada | A última linha da legenda (0:20:54) termina no meio da frase, a cerca de 10 s do fim do vídeo. |

Nota de método: cada afirmação traz aula e timestamp. As citações são paráfrases de legenda, sem aspas, não verificadas contra o vídeo. Mis-hearings ficam entre colchetes. As seções 13 e 14 dizem que não há código publicado a analisar nem suíte a rodar.

## 2. Filosofia e método de ensino

### 2.1 Um mapa mental, uma conversa

A aula inteira segue um mapa mental que ele percorre na tela (aula 1, 0:00:00 a 0:00:13) e pergunta no fim se a turma conseguiu ver bem e se o programa do mapa funcionou melhor que o outro (aula 8, 0:03:05 a 0:03:15). O tom é de conversa: para a cada bloco e pergunta se pode seguir (aula 1, 0:06:45; aula 3, 0:15:08; aula 5, 0:12:38), abre o microfone (aula 3, 0:00:00 a 0:00:12) e avisa antes da parte opinativa que a turma pode discordar dele à vontade (aula 1, 0:18:45 a 0:19:09).

### 2.2 A essência antes do nome

Ele recusa começar pela lista de tipos e ferramentas. Na aula 2, diante da confusão entre teste de integração, unitário e qual ferramenta usar, pede calma e propõe pegar a essência do teste primeiro (aula 2, 0:00:00 a 0:00:20). Na aula 5 a ideia volta como crítica: inventar nome para tudo ajuda a comunicar, mas sem clareza da diferença vira um emaranhado, e quando ele olha os tipos de teste vê sempre a mesma coisa, só muda um detalhe, uma estratégia, uma ferramenta (aula 5, 0:00:00 a 0:01:10). É tudo sorvete, só muda o sabor (aula 5, 0:05:55 a 0:06:21).

### 2.3 Aprender pelo exercício, não pelo conceito

O fecho diz o que o curso não pode fazer sozinho: as pessoas tentam entender teste pela compreensão dos conceitos em vez de pela expressão do exercício, então é preciso praticar (aula 8, 0:00:25 a 0:00:36). Por isso o curso termina em um presente, o Raio-X do TDD, para pôr a mão na massa (aula 8, 0:00:36 a 0:01:21), e já na aula 4 ele dizia que não é possível aprender teste com demonstrações rapidinhas nem num projeto novo do trabalho, mas com kata, coding dojo e programação em par com quem sabe (aula 4, 0:04:12 a 0:06:30).

### 2.4 Teste como postura profissional

Quase metade da aula 1 não fala de teste em sentido estrito: fala da postura de quem programa. A melhor ferramenta de qualidade é o não, e a segunda melhor também (aula 1, 0:13:17 a 0:14:13), dito sem opinião, mostrando que o não protege o bolso do cliente e é só um talvez deslocado no tempo (aula 1, 0:14:29 a 0:15:16). A troca de papel que ele propõe é sair de executor de demanda e de solucionador de problemas para negociador de soluções (aula 1, 0:16:53 a 0:17:29). A aula 3 volta ao ponto como mentalidade: o código é meio, não fim (aula 3, 0:03:11 a 0:03:50).

### 2.5 Relação com os outros cursos

Comparação deste documento, não fala dele: o método de legado da aula 7 (amarração, ordenação, separação, redução) é o mesmo movimento que ele executa ao vivo em Refatoração com POO em código legado (`kb/courses/refatoracao-poo-legado.md`), onde também diz que refatorar é não matar o paciente (aula 6 daquele curso, 0:06:15). E o Raio-X do TDD (`kb/courses/raio-x-do-tdd.md`), dado de presente na aula 8, é a parte prática que este curso deixa de fora.

## 3. Pilares conceituais

### 3.1 A foto e o filme

O software quebra porque se programa uma foto e o que se quer executar é um filme: a diferença é uma dimensão a mais, o tempo, e no tempo se passa pelo mesmo caminho em contextos diferentes (aula 1, 0:06:55 a 0:07:46). Daí vem tudo: programar exige sensibilidade para a estética do filme, da execução (aula 1, 0:08:38 a 0:08:52); o ciclo de desenvolvimento é fazer a foto e ver o filme, em ciclo iterativo e incremental (aula 2, 0:02:45 a 0:03:06); e quem programa tem que poder visualizar o filme para escrever, o que o depurador e o tracer ajudam a fazer (aula 7, 0:14:08 a 0:14:19).

### 3.2 Complexidade exponencial contra esforço linear

Um código pequeno pode ter complexidade exponencial, porque saltos e condicionais criam caminhos que não crescem linearmente com as linhas (aula 1, 0:10:28 a 0:11:02). Usar uma estratégia linear contra uma força exponencial é perder, como pagar o mínimo do cartão de crédito; por isso teste manual não se sustenta e só quem programa consegue criar a foto linear de um teste capaz de mapear uma execução exponencial: fogo com fogo, código com código (aula 1, 0:25:49 a 0:27:12). O mesmo raciocínio aparece no legado: uma validação repetida 50 vezes, extraída numa função, vira 50 usos de uma coisa só, e só essa coisa precisa de teste (aula 3, 0:14:03 a 0:14:33).

### 3.3 Teste não prova, dá confiança

Pela frase de Myers de 1979 [legenda: Mayer], testar é analisar um programa com a intenção de descobrir erros e defeitos, não validar que ele funciona; quanto mais defeitos se encontram, maior a confiança, e nunca se prova que o software funciona (aula 2, 0:00:20 a 0:01:17). A imagem é o campo minado: vai-se cercando as bombas com bandeirinhas até desarmar todas (aula 2, 0:02:04 a 0:02:23). Na aula 3 o ponto vira definição: teste não é garantia, não é prova, não é bala de prata; é uma ferramenta para dar confiança, com muitos tons de cinza (aula 3, 0:15:32 a 0:15:57).

### 3.4 Entropia contida, não eliminada

Adicionar código é desestabilizar o software, porque mais código é mais caminhos possíveis; os testes não eliminam essa instabilidade, contêm o efeito da entropia (aula 2, 0:05:41 a 0:06:18). Programar é tirar água do navio com um balde (aula 2, 0:06:55 a 0:07:04). Sem teste, o software funciona por acaso, e quem vai testar é o usuário final (aula 2, 0:07:13 a 0:07:41).

### 3.5 Pensar de trás para frente

O teste depende de passar do imperativo para o declarativo: não diga o que fazer, explique o que deseja; importa o estado inicial, o estado final e a transição, não a implementação (aula 3, 0:04:45 a 0:05:32). Ele contrasta planejar para frente, a sequência de passos para ir ao shopping, com planejar de trás para frente, a partir de estar no shopping a tal hora, e conclui que a incapacidade de pensar de trás para frente inviabiliza o teste (aula 3, 0:06:06 a 0:07:54). Na aula 4 o desafio de quem já programa não é saber a resposta, é esculpir o caminho de trás para frente (aula 4, 0:01:45 a 0:01:58); na aula 7 é a definição do TDD: declaro o final para então fazer o começo (aula 7, 0:08:56 a 0:09:08).

### 3.6 O mínimo, escolhido por risco e por contexto

Quanto testar: sempre o mínimo possível, nunca menos que o mínimo, e o mínimo se encontra por análise de risco (aula 2, 0:04:38 a 0:05:10). Os riscos são vários: de vida, financeiro, de reputação, de oportunidade, de orçamento, de prazo (aula 3, 0:16:45 a 0:17:05), e a tolerância vai em função do contexto, então não há melhor prática de teste fora do contexto (aula 3, 0:18:13 a 0:18:35). A mesma régua decide a cobertura: ele não usa meta de cobertura, usa a cobertura do que importa pela análise de risco (aula 7, 0:16:01 a 0:16:34).

### 3.7 Teste o efeito, não o código

Um teste que muda quando o código muda testa o código; o que se quer é testar o efeito, para que mudar a implementação não mexa nele (aula 4, 0:07:20 a 0:07:31). Por isso ele prefere caixa preta a caixa branca (aula 5, 0:07:17 a 0:07:30), e por isso o teste ruim, para ele, é o que tem relação de um para um entre alteração no código e alteração no teste (aula 7, 0:00:11 a 0:00:22).

## 4. As aulas em uma tabela

| # | Título | Duração | Foco em uma linha |
|---|---|---|---|
| 1 | #01: O Universo dos Testes | 35:13 | Origem do teste; a foto e o filme (0:06:55); o não como ferramenta de qualidade (0:13:17); linear contra exponencial (0:26:08). |
| 2 | #02: Desmistificando os Testes | 7:59 | Testar é achar defeitos (0:00:20); quanto mais cedo melhor (0:02:23); o mínimo possível por análise de risco (0:04:38). |
| 3 | #03: A Arte dos Testes | 18:47 | O código é meio (0:03:38); pensar de trás para frente (0:06:06); transplante em legado (0:13:19); o que testar, não como (0:16:34). |
| 4 | #04: Começando a testar | 9:01 | Passos de bebê (0:00:00); kata, dojo, par (0:04:23); teste o efeito do código (0:07:20). |
| 5 | #05: Tipos de Testes | 25:11 | Efeito checklist (0:01:10); estático e dinâmico (0:02:50); partição de equivalência e valor limite (0:07:30); unitário a regressão (0:14:52 a 0:25:04). |
| 6 | #06: Anatomia dos Testes | 11:33 | Erro, defeito e falha (0:00:10); discovery, seleção, runner, reporter (0:02:07); dublês (0:07:27). |
| 7 | #07: Testando | 21:05 | Camada de indireção (0:01:00); caminho de sucesso primeiro (0:05:23); expandir e colapsar (0:06:05); amarração, ordenação, separação, redução (0:17:59). |
| 8 | #08: Conclusão | 3:21 | O mínimo necessário (0:00:13); praticar; o Raio-X do TDD de presente (0:00:36). |

## 5. Resumo por aula

### Aula 1: #01 - O Universo dos Testes
Vídeo: https://www.youtube.com/watch?v=h2BkqOQjMBU · Duração: 35:13

Resumo: abre com o mapa mental (0:00:00 a 0:00:13). Contra a ideia de que teste é moderno, coisa do livro do Kent Beck [legenda: quente back] e dos anos 2000, diz que teste existe desde sempre e ganhou status de fundamental no fim dos anos 60, na conferência em que se cunhou o termo engenharia de software (0:00:24 a 0:01:26; ele diz 1969 e conferência da OTAN, 0:05:48). Contrapõe a prova formal, matemática, à estratégia empírica de verificar na prática (0:01:26 a 0:02:24), com a história do concreto: o engenheiro francês passa dez anos no quadro negro, o americano faz três mil corpos de prova e vê quais não racham; nenhum é melhor, depende da natureza do problema e das restrições, e quanto mais escasso o recurso, como numa missão à Lua, maior o esforço de validação (0:02:24 a 0:05:37). Cita um artigo sobre a complexidade crescente [legenda: the Rambo programa; provável: The Humble Programmer, de Dijkstra, leitura incerta] (0:06:03). Então a metáfora central: programa-se uma foto e se executa um filme (0:06:55 a 0:07:46), daí a regra de manter o código o mais linear possível, sem o código esperto que junta funções parecidas com um parâmetro de configuração (0:07:55 a 0:08:29). Indica uma palestra de Bret Victor [legenda: Brad Victor; título não legível] sobre ver o efeito do código enquanto se programa (0:09:14 a 0:09:52). Todo software é único, e a postura prudente é não achar que já fez aquele sistema (0:09:52 a 0:10:28). A complexidade não é linear no número de linhas, com os exemplos do formulário com validações cruzadas e do fluxograma de notificações do Slack (0:10:28 a 0:12:32). A qualidade: a melhor ferramenta é o não, a segunda também; resolve 80% dos problemas, mas não se usa cru, exige argumentação sem opinião e mostrar que o não protege o bolso do cliente e é um talvez (0:13:17 a 0:15:16). Quem faz tudo o que o cliente pede não faz o que ele precisa, e nenhum teste resolve isso (0:15:16 a 0:15:37). Propõe a troca de postura: de executor de demanda e solucionador de problemas para negociador de soluções (0:16:02 a 0:18:22). Na parte que avisa ser opinativa (0:18:45), critica a indústria de QA: certificações e siglas importadas da qualidade total da manufatura, modelos descritivos que não representam o software, porque só o código roda, e um modelo de negócio de alocação de mão de obra (0:19:09 a 0:22:11); trabalhar num lugar assim não é problema, desde que se saiba o jogo que se está jogando (0:22:11 a 0:23:16). Teste manual não se sustenta contra a complexidade exponencial: fogo com fogo, código com código, e por isso teste é parte do desenvolvimento (0:25:49 a 0:27:12). Conviver sem teste é possível, como dívida com o timer ligado (0:27:12 a 0:27:49), e ele conta o caso de sites de campanha que duravam uma semana, sem teste automático, em que o foco foi reaproveitar código a cada edição até surgir um framework da experiência concreta (0:27:49 a 0:30:51). Fecha com o desafio de mercado, teste visto como custo, e uma receita de gestão: medir o custo da equipe, quanto cada projeto consome e quanto do tempo vai para correção, para mostrar que sem teste a equipe passa a pagar dívida de sprint passado (0:30:51 a 0:33:37); se não funcionar, muda a empresa ou muda você de empresa (0:33:37 a 0:34:42).

Linha do tempo:
- [0:00:00] o mapa mental que guia o labirinto
- [0:00:24] teste não é coisa moderna
- [0:02:24] o engenheiro francês e o americano: prova formal contra corpo de prova
- [0:06:55] a foto e o filme
- [0:07:55] mantenha o código o mais linear possível
- [0:09:14] a palestra de Bret Victor
- [0:10:28] código pequeno, complexidade exponencial
- [0:13:17] a melhor ferramenta de qualidade é o não
- [0:16:53] de resolver problema para negociar solução
- [0:19:09] a crítica da indústria de QA
- [0:25:49] linear contra exponencial: código com código
- [0:27:49] os sites de campanha
- [0:31:23] medir quanto do tempo vai para correção

Princípios:
- Teste existe em tudo: a natureza da validação, formal ou empírica, depende do problema e das restrições (0:04:00 a 0:05:37).
- Mantenha o código o mais linear possível, sem esperteza (0:07:55 a 0:08:29).
- A melhor ferramenta de qualidade é não fazer, dito sem opinião (0:13:17 a 0:15:16).
- Negocie a solução em vez de executar a demanda (0:16:53 a 0:17:29).
- Teste manual não escala contra complexidade exponencial; teste é parte do desenvolvimento (0:26:08 a 0:27:12).
- Saiba o jogo que está jogando (0:22:11 a 0:22:56; 0:27:37 a 0:27:49).

Código: nenhum.

Citações (paráfrases de legenda, não verificadas):
- [0:07:07] o software quebra porque a gente programa uma foto nosso código é uma foto enquanto o código rodando que aquilo que a gente quer executar é um filme
- [0:08:17] Não faça isso Mantenha o seu código mais linear possível
- [0:13:44] a melhor ferramenta é não vou fazer isso não vai entrar é não é tirar é reduzir os corpos [provável: escopo]
- [0:26:20] toda vez que você usar uma estratégia linear para lutar contra uma força exponencial você vai perder
- [0:21:03] só o código é código só o código roda

### Aula 2: #02 - Desmistificando os Testes
Vídeo: https://www.youtube.com/watch?v=nybYVtI7Qa8 · Duração: 7:59

Resumo: antes de tipos e ferramentas, a essência (0:00:00 a 0:00:20). Pela frase de Myers [legenda: Mayer] de 1979, testar é analisar um programa com a intenção de descobrir erros e defeitos; erro é o equívoco no código, como um menor que no lugar de um menor ou igual, e defeito é o efeito do erro, a tela azul (0:00:20 a 0:00:57). O objetivo não é validar que funciona: quanto mais erros e defeitos se encontram, maior a confiança, porque não há como provar que funciona (0:00:57 a 0:02:04), e a imagem é o campo minado do Windows 3.1 (0:02:04 a 0:02:23). Quando testar: quanto mais cedo melhor, e daí o gosto dele pelo teste primeiro, porque o ciclo é fazer a foto e ver o filme, iterativo e incremental (0:02:23 a 0:03:06). Mudar um software testado o desestabiliza, e sem automação seria preciso testá-lo todo de novo à mão; testar passo a passo ajuda a descobrir o design que permite o teste, porque há código virtualmente impossível de testar depois (0:03:06 a 0:04:00). Quanto testar: o mínimo possível, nunca menos que o mínimo, achado por análise de risco; testar todas as combinações tende ao infinito (0:04:38 a 0:05:21). O teste é uma troca: programar mais devagar, mas com passo firme que não volta, e a cadência cresce com a experiência (0:05:21 a 0:05:41). Adicionar código desestabiliza; os testes contêm a entropia como quem contém um câncer (0:05:41 a 0:06:43), e programar é tirar água do navio com um balde (0:06:55 a 0:07:04). Conclusão: software sem teste funciona por acaso, e no fim quem testa é o usuário final, no pior momento (0:07:13 a 0:07:49).

Linha do tempo:
- [0:00:09] calma: a essência do teste primeiro
- [0:00:20] Myers, 1979: testar é descobrir erros e defeitos
- [0:00:42] defeito é o efeito do erro
- [0:01:08] não dá para provar que funciona; dá para aumentar a confiança
- [0:02:04] o campo minado
- [0:02:23] quanto mais cedo melhor; teste primeiro
- [0:03:36] testar ajuda a achar o design que permite o teste
- [0:04:38] o mínimo possível, nunca menos que o mínimo
- [0:05:21] mais devagar, mas sem voltar
- [0:06:04] os testes contêm a entropia
- [0:07:13] sem teste, funciona por acaso

Princípios:
- Testar é procurar defeitos para aumentar a confiança, não provar que funciona (0:00:57 a 0:01:29).
- Teste o quanto antes, em ciclo com o código (0:02:23 a 0:03:36).
- O mínimo possível, nunca menos que o mínimo, por análise de risco (0:04:38 a 0:05:10).
- O teste troca velocidade por passo firme (0:05:21 a 0:05:41).

Código: nenhum.

Citações (paráfrases de legenda, não verificadas):
- [0:00:57] o objetivo de testar é para você não é para validar que o software funciona não eu quero pegar os erros e defeito
- [0:02:30] quanto mais cedo melhor quanto mais cedo melhor
- [0:04:47] o quanto testar aí é sempre o mínimo possível nunca menos que o mínimo possível
- [0:07:13] um software sem teste funciona por acaso

### Aula 3: #03 - A Arte dos Testes
Vídeo: https://www.youtube.com/watch?v=85gCGokI2Ok · Duração: 18:47

Resumo: pergunta à turma por que é tão difícil testar, e participantes respondem: não conhecer a saída do código, não ter escrito o código, legado que não se entende (0:00:00 a 0:02:30, fala de participantes). A resposta dele: acreditaram numa mentira, a de que programar é sobre código; o programador usa programação para criar soluções, e o código é meio, não fim (0:02:31 a 0:03:50). A mudança é de foco em tarefa para foco em resultado, como reescrever os tickets: em vez de fazer emissão de nota, permitir que o usuário emita uma nota fiscal após uma compra (0:03:50 a 0:04:45). Do imperativo ao declarativo: o que importa é estado inicial, estado final e transição; a implementação tem de poder mudar sem impactar entrada e saída, e bugs vêm de código que muda a saída de outro lugar por efeito colateral (0:04:45 a 0:05:41). Planejamento para frente e de trás para frente, com o exemplo de ir ao shopping: a incapacidade de pensar de trás para frente inviabiliza o teste (0:06:06 a 0:08:02). A linguagem é a interface com a realidade, e controlar a linguagem é a pior coisa (0:08:02 a 0:09:11). Cita Bruce Lee, be water my friend [legenda: Bill water my friend]: em vez de forçar o ambiente, moldar-se a ele (0:09:11 a 0:09:53). É a estratégia dele para pôr teste em legado: não faz reengenharia; sem mexer no código, agrupa as coisas, olha um loop, pergunta o que precisaria para extrair o miolo para uma função ao lado, no mesmo arquivo, mesmo com assinatura enorme, e testa só aquele trecho crítico (0:09:53 a 0:11:20). É cirurgia plástica, desfiar o pedacinho do novelo que é o filé mignon, porque muito do código grande é boilerplate (0:11:20 a 0:12:13). A uma pergunta do chat sobre bottom up, responde que não é bottom up, é um transplante: copiar e colar, sem mudar definição, para separar a lógica do código e ter uma unidade testável (0:12:13 a 0:13:51). Com o tempo nasce uma nova árvore de execução, e a validação repetida 50 vezes vira uma função testada uma vez: fogo contra fogo (0:13:51 a 0:14:58). O que o teste não é, a partir de respostas do chat: não é garantia, não é prova, não é bala de prata; é ferramenta de confiança, com tons de cinza, e política de 100% de qualquer coisa vai dar ruim (0:15:08 a 0:16:22). Mudar a pergunta de como faço teste para o que preciso testar, com análise de riscos: de vida, financeiro, de reputação, de oportunidade, de orçamento, de prazo (0:16:22 a 0:17:16), com o caso de um controlador automotivo de 150 mil linhas cujo freio falhava em condições especiais, citado de um artigo que ele não identifica (0:17:16 a 0:18:03). O teste depende do contexto, e não há resposta para a forma certa de testar fora dele (0:18:13 a 0:18:44).

Linha do tempo:
- [0:00:00] por que é tão difícil testar? (respostas de participantes até 0:02:30)
- [0:02:41] a mentira: programar é sobre código
- [0:03:38] o código é meio, não fim
- [0:04:01] de tarefa para resultado: reescrever o ticket
- [0:05:12] estado inicial, estado final, transição
- [0:06:06] para frente e de trás para frente
- [0:07:42] não pensar de trás para frente inviabiliza o teste
- [0:09:11] be water my friend
- [0:09:53] legado: agrupar, extrair o miolo do loop, testar o trecho crítico
- [0:13:19] não é bottom up, é transplante
- [0:14:28] fogo contra fogo
- [0:15:44] confiança é o que importa
- [0:16:34] o que eu preciso testar, não como
- [0:18:27] o teste depende do contexto

Princípios:
- O código é meio, não fim; foco no resultado (0:03:38 a 0:04:45).
- Teste a transição de estado, não a implementação (0:05:12 a 0:05:32).
- Pense de trás para frente, do resultado ao começo (0:06:06 a 0:08:02).
- Em legado, extraia sem reengenharia o trecho crítico e teste só ele (0:09:53 a 0:11:20; 0:13:19 a 0:13:51).
- Teste dá confiança, não garantia; nada de 100% de qualquer coisa (0:15:44 a 0:16:22).
- Escolha o que testar por análise de risco, no contexto (0:16:34 a 0:18:35).

Código: nenhum. Ele descreve a extração sem escrever: uma rotina de 200 linhas com um loop, o miolo do loop extraído para uma função declarada logo acima, no mesmo arquivo (0:10:06 a 0:11:10).

Citações (paráfrases de legenda, não verificadas):
- [0:02:41] nos fizeram acreditar numa mentira
- [0:03:40] O código é um meio não fins
- [0:07:42] a incapacidade de pensar de trás para frente inviabiliza execução de Teste
- [0:11:10] eu não quero mudar o código todo para tornar ele mais fácil de testar
- [0:15:46] confiança é o que importa
- [0:16:34] mudar a pergunta para de perguntar como faço teste e começa a perguntar o que eu preciso testar

### Aula 4: #04 - Começando a testar
Vídeo: https://www.youtube.com/watch?v=4XVTrIbIFm4 · Duração: 9:01

Resumo: a coisa mais importante para começar é passos de bebê (0:00:00 a 0:00:21). Programar com teste exige mudança cognitiva e de hábito, que não muda da noite para o dia, como um instrumento musical com o metrônomo (0:00:21 a 0:00:46); a experiência é cinestésica, muda a forma de falar, de pensar e de olhar o trabalho (0:00:46 a 0:01:13). Exige humildade, suspender a certeza: quanto mais experiência, maior a dificuldade, porque se quer correr, e o desafio não é a resposta, é esculpir o caminho de trás para frente na posição de novato, sem pular etapa (0:01:13 a 0:01:58). Conta que, quando aprendia teste em exercícios na Universidade Federal Fluminense, colegas que tinham certeza de como as coisas funcionavam não conseguiam e ficavam com raiva do processo (0:01:58 a 0:02:31). Usa o Karatê Kid e o kata das artes marciais: a forma importa mais que a velocidade e a força, até o corpo fazer sozinho (0:02:31 a 0:03:49). Teste não é extensão da programação, é outra forma de programar (0:03:49 a 0:04:12). As formas de aprender: kata [legenda: catar], coding dojo [legenda: cor do Idoso, code endojo] e programação em par [legenda: Programe limpar] com quem sabe (0:04:12 a 0:04:34). Aprendeu no Dojo Rio, por volta de 2006 e 2007, de forma dolorosa, com um colega insistindo em passos de bebê (0:04:34 a 0:05:26). Aprender teste no sistema da empresa não vai acontecer (0:05:26 a 0:05:37). Indica uma aula de kata que gravou e pôs no YouTube [legenda: rap numbers; nome do kata incerto] e anuncia o presente do fim do curso (0:05:47 a 0:06:13). Perguntas como testar scraping ou banco de dados são a pergunta errada: é preciso desenvolver a capacidade de pensar no teste (0:06:13 a 0:06:47). Fecha com o foco: não teste o código, teste o efeito do código, para que mudar a implementação não mexa no teste; no Django, em vez de depender dos objetos que o ORM devolve, uma representação deles; num algoritmo de ordenação, o efeito é estar em ordem, não a estrutura de dados (0:07:20 a 0:08:54).

Linha do tempo:
- [0:00:06] passos de bebê
- [0:00:33] mudar hábito leva tempo
- [0:01:01] aprender teste é cinestésico
- [0:01:25] suspender a certeza
- [0:02:44] Karatê Kid e o kata
- [0:04:01] teste é outra forma de programar
- [0:04:23] kata, coding dojo, programação em par
- [0:04:42] o Dojo Rio
- [0:05:49] a aula de kata no YouTube
- [0:06:37] a pergunta errada: como testo isso
- [0:07:24] teste o efeito do código
- [0:08:22] o efeito de um algoritmo de ordenação

Princípios:
- Passos de bebê, sem pular etapa (0:00:06 a 0:01:58).
- Teste é outra forma de programar, não extensão dela (0:04:01 a 0:04:12).
- Aprende-se teste com kata, dojo e par, não no sistema do trabalho (0:04:23 a 0:05:37).
- Teste o efeito, não o código (0:07:20 a 0:08:54).

Código: nenhum. Os exemplos do ORM do Django e da ordenação são falados.

Citações (paráfrases de legenda, não verificadas):
- [0:01:25] a gente tem que suspender a nossa Certeza
- [0:01:45] o desafio não é da resposta o desafio é esculpir o caminho de trás para frente
- [0:04:08] teste não é simplesmente uma extensão da programação ela é uma outra forma de programar
- [0:07:24] não teste código teste o efeito do código

### Aula 5: #05 - Tipos de Testes
Vídeo: https://www.youtube.com/watch?v=EqvExX5rfY0 · Duração: 25:11

Resumo: primeiro a confusão: inventar nome para tudo, como fazem Kent Beck [legenda: kateback] e Ward Cunningham [legenda: Word cunning], ajuda a comunicar, mas sem clareza da diferença vira emaranhado; nos tipos de teste a essência é a mesma (0:00:00 a 0:01:10). O efeito checklist: 100% de cobertura, unitário, TDD, BDD, integração, tudo ao mesmo tempo, e perguntas fora de contexto, como qual o melhor teste de integração, que dependem de o software ser uma biblioteca de MP3 ou um sistema distribuído de mensageria (0:01:10 a 0:02:09). Não há jeito certo: o certo é o que atende o cliente e renova o contrato (0:02:09 a 0:02:29). Estáticos e dinâmicos: os estáticos não executam o código e incluem code review, linter, sistema de tipos e analisadores de código, como o alerta de loop dentro de loop, a complexidade ciclomática, a dependência cíclica e a proibição de concatenar strings com SQL (0:02:39 a 0:05:41). Os dinâmicos são todos a mesma coisa: tudo sorvete, só muda o sabor (0:05:55 a 0:06:21). Caixa preta testa pelo contrato, entradas e saídas, e ele prefere a caixa preta porque testa o efeito (0:06:21 a 0:07:30). Partição de equivalência e análise de valor limite, com o exemplo da idade de trabalho entre 18 e 60: dois estados, verdadeiro e falso, e os limites 17, 18, 60 e 61; ele gosta de pôr um valor no meio, 30, e faria cinco entradas em dois testes (0:07:30 a 0:10:34). O ponto é testar o limite do comportamento, não repetir o que se repete, e agrupar os testes pelas categorias naturais do sistema (0:10:34 a 0:11:20); pela especificação, testados os limites, assume-se que o miolo funciona (0:11:41 a 0:12:38). Caixa branca força os caminhos de execução e serve a estruturas de dados, como a ordem de inserção do dicionário do Python, que depende de detalhe de implementação (0:12:38 a 0:13:50). Testes empíricos vêm da experiência, e a categoria que ele adora é transformar cada chamado de suporte em teste de regressão (0:13:50 a 0:14:42). Teste unitário: teste de algo sem dependência, a parte mínima divisível; com dependências, isolam-se os colaboradores com stub [legenda: estúdio] ou mock [legenda: Moque] (0:14:42 a 0:15:36); uma classe de cadastro de pessoa com validação de CPF dentro não é unidade, a validação deveria ser colaboradora separada (0:15:36 a 0:16:20, exemplo vindo de participante). Integração atravessa componentes; o envio de e-mail pode virar unitário partindo do axioma de que o Postfix [legenda: post fixo, post ficção] funciona e substituindo o serviço por um mock que anota que foi chamado (0:16:20 a 0:17:55). Unitário ou integração é adjetivo; a essência é o teste, e a fronteira às vezes é difícil (0:18:22 a 0:19:08). Teste de sistema, de aceitação e smoke test, que vem da eletrônica: ligar e ver se sai fumaça, rodando uma vez por dia o caminho feliz do que é crucial (0:19:08 a 0:20:42). Fuzz [legenda: fase, fãs]: entradas aleatórias, em geral não reprodutíveis; ele mistura no mesmo trecho o caso da Netflix de derrubar sistemas ao acaso (0:20:42 a 0:21:41). A uma pergunta sobre a biblioteca Hypothesis [legenda: hipóteses], diz que nunca usou, olha na hora e acha que tem cheiro de fuzz guiado por restrições do domínio (0:21:41 a 0:22:35). Performance, carga e estresse, com o exemplo de um site de venda de ingressos [legenda: evento Bright; provável: Eventbrite] (0:22:35 a 0:24:54). Fecha com regressão: estudar a falha, reproduzi-la e transformá-la em teste (0:24:54 a 0:25:04).

Linha do tempo:
- [0:00:00] a confusão dos nomes
- [0:01:10] o efeito checklist
- [0:02:09] não há jeito certo fora do contexto
- [0:02:50] estático e dinâmico
- [0:03:56] analisadores de código: loop dentro de loop, SQL concatenado
- [0:06:09] tudo sorvete, só muda o sabor
- [0:07:17] prefere caixa preta
- [0:07:30] partição de equivalência e valor limite: 17, 18, 30, 60, 61
- [0:12:38] caixa branca e o dicionário do Python
- [0:14:00] suporte vira teste de regressão
- [0:15:16] unitário: a parte mínima, sem dependência
- [0:17:08] o axioma do Postfix e o mock do e-mail
- [0:19:41] smoke test
- [0:20:42] fuzz e Hypothesis
- [0:22:35] performance, carga, estresse

Princípios:
- Entenda a essência antes do nome; fuja do efeito checklist (0:00:58 a 0:02:29).
- Use análise estática para impedir erros fáceis de detectar (0:05:30 a 0:05:55).
- Prefira caixa preta, pelo contrato (0:07:06 a 0:07:30).
- Teste os limites e um valor do meio, agrupados pelas categorias do sistema (0:09:06 a 0:11:20).
- Todo chamado de suporte reproduzido vira teste de regressão (0:14:00 a 0:14:42).
- Parta de axiomas: o que é estabelecido, como o Postfix, não se testa (0:17:08 a 0:17:31).

Código: reconstrução a partir da fala; não publicada. A condição é ditada de forma confusa na legenda (0:07:50 a 0:08:04); a leitura é a idade de trabalho entre 18 e 60 inclusive, como ele confirma em 0:11:41. O nome da função é deste documento.

```python
# reconstrução a partir da fala, não publicada
def idade_de_trabalho(idade):
    return 18 <= idade <= 60


def test_dentro_da_faixa():           # partição verdadeira: limites e um do meio (0:10:13)
    for idade in (18, 30, 60):
        assert idade_de_trabalho(idade)

def test_fora_da_faixa():             # partição falsa: logo antes e logo depois (0:09:17)
    for idade in (17, 61):
        assert not idade_de_trabalho(idade)
```

Citações (paráfrases de legenda, não verificadas):
- [0:02:18] quero fazer do jeito certo não tem um jeito certo é que funciona que atende o cliente que cai dinheiro no bolso
- [0:06:09] é tudo sorvete só muda o sabor
- [0:07:23] Eu prefiro o teste caixa preta do que o teste caixa branca exatamente por essa questão de de você conseguir testar o efeito
- [0:10:43] as coisas que se repetem muito você ignora você quer o limite do comportamento

### Aula 6: #06 - Anatomia dos Testes
Vídeo: https://www.youtube.com/watch?v=EyobC22NbD8 · Duração: 11:33

Resumo: definições. Erro é resultado da ação humana, a condição errada no código; defeito é o efeito do erro, a tela azul; falha é a manifestação do defeito na execução, no contexto e no instante em que aparece (0:00:00 a 0:00:44). Há uma relação temporal de causa e efeito, e o mesmo defeito pode ter falhas diferentes (0:00:44 a 0:01:21). Erros podem ser internos ou externos, como uma API ruim de outro sistema que sai do ar, e por isso teste de integração é caro: não basta o caso de sucesso, é preciso testar os efeitos colaterais (0:01:21 a 0:01:57). A anatomia de um framework de testes: discovery, que no Python acha arquivos e funções que começam com test (0:01:57 a 0:02:42); seleção, por filtro ou por nome (0:02:42 a 0:02:58); runner, local ou distribuído (0:02:58 a 0:03:12); reporter, que consolida (0:03:12 a 0:03:33). No reporter os conceitos mudam: erro é quando o código explode com exceção não tratada, falha é quando a expectativa do teste não foi atendida, sucesso é quando foi; teste é sobre expectativa (0:03:33 a 0:03:56). Para organizar: comece com tudo junto e vá separando conforme as categorias aparecem, dividir e conquistar (0:03:56 a 0:04:29). Suíte é a coleção dos testes; caso de teste é um cenário, não uma função nem uma classe, e um cenário pode ter vários testes, como cadastro bem-sucedido e cadastro com erro (0:04:29 a 0:05:31). Setup e teardown [legenda: terdão] por teste, e em ferramentas mais sofisticadas por sessão, módulo ou classe, como otimização (0:05:31 a 0:06:30). Fixture [legenda: fique, Fiction] cria o estado inicial; com banco de dados vira teste de integração (0:06:30 a 0:07:05). A uma pergunta sobre usar recurso específico do Postgres e testar com SQLite: se usa coisa específica do banco, o banco vira axioma da arquitetura, e se desenvolve e testa com aquele banco, sem misturar (0:07:05 a 0:07:27). Os dublês: dummy [legenda: Dani], passado e nunca usado; fake, real mas feito por atalho, como banco em memória; stub [legenda: step, stand], esculpido para dar respostas específicas; spy [legenda: Spice], stub que anota como foi usado; mock, programado com expectativas sobre como deve ser chamado, que verifica o comportamento do chamador (0:07:27 a 0:09:44). A metáfora do mock é a moldura em negativo do casco de fibra: o mock é o negativo do chamador (0:09:44 a 0:10:17). Em Python e Ruby a biblioteca de mock faz tudo isso ao mesmo tempo, inclusive `assert_called_with` [legenda: acerte caldo with], e o importante é entender o limite conceitual de cada um mesmo usando a mesma ferramenta (0:10:17 a 0:11:28).

Linha do tempo:
- [0:00:10] erro, defeito, falha
- [0:00:44] causa, consequência e o instante da falha
- [0:01:21] erros externos e o custo do teste de integração
- [0:02:07] discovery
- [0:02:42] seleção e runner
- [0:03:12] reporter: erro, falha e sucesso
- [0:03:48] teste é sobre expectativa
- [0:04:06] comece junto e vá separando
- [0:04:29] suíte, caso de teste, cenário
- [0:05:31] setup e teardown
- [0:07:05] o banco específico vira axioma
- [0:07:27] dublês: dummy, fake, stub, spy, mock
- [0:09:56] o mock como moldura em negativo

Princípios:
- No relatório, erro é exceção não tratada e falha é expectativa não atendida (0:03:33 a 0:03:48).
- Teste é sobre expectativa (0:03:48 a 0:03:56).
- Comece com tudo junto e separe quando as categorias aparecerem (0:04:06 a 0:04:29).
- Caso de teste é cenário, não classe nem função (0:04:29 a 0:05:31).
- Se depende de um banco específico, ele é axioma: desenvolva e teste com ele (0:07:05 a 0:07:27).
- Conheça o limite conceitual de cada dublê, mesmo usando uma ferramenta só (0:11:17 a 0:11:28).

Código: reconstrução a partir da fala; não publicada. Só a forma do mock que ele cita pelo nome, `assert_called_with`, da biblioteca de mock do Python (0:11:08 a 0:11:17); o objeto e os argumentos são deste documento.

```python
# reconstrução a partir da fala, não publicada
from unittest.mock import Mock

email = Mock()
email.send("a@b.c", "boas-vindas")             # o código sob teste chamaria isto
email.send.assert_called_with("a@b.c", "boas-vindas")  # mock: verifica o chamador
```

Citações (paráfrases de legenda, não verificadas):
- [0:00:20] um defeito é o resultado de um erro é o efeito do erro é a tela azul e a falha é a manifestação de um defeito na execução do software
- [0:03:48] teste é sobre expectativa
- [0:04:11] comece fazendo as coisas juntas e vá reorganizando separando conforme a necessidade
- [0:10:07] ele é plástico ele é uma moldura e negativo do chamador

### Aula 7: #07 - Testando
Vídeo: https://www.youtube.com/watch?v=DqTOk3XyiKo · Duração: 21:05

Resumo: o que faz um teste bom ou ruim: especificidade, foco na interface, e mudança na implementação não gerar mudança no teste; é ruim quando há relação de um para um entre alteração no código e no teste (0:00:00 a 0:00:22). O exemplo canônico: um sistema que usa três recursos do GitHub replicando a chamada HTTP em 15 lugares; mudar a biblioteca muda tudo, e se o GitHub sai do ar o teste não roda (0:00:22 a 0:01:00). A solução são camadas de indireção [legenda: em direção]: uma função fecha pull request [legenda: fecha o record, curricrash] que recebe só o número, outra que abre e outra que lista, mesmo com conteúdo repetido por dentro; no teste se fornece um stub dessa função e se testa toda a lógica de quem chama, sem rede (0:01:00 a 0:02:34). É uma mudança pequena que dá uma ordem de grandeza em facilidade de teste, como um ponteiro que dá para grampear (0:02:50 a 0:03:20). Recomendações: teste o comportamento; teste como o código reage às falhas críticas, para o usuário não ficar com spinner infinito ou erro 500 (0:03:20 a 0:03:52); defina axiomas, como não testar o framework que se estende (0:03:52 a 0:04:09); não se limite ao framework de testes, crie asserções de mais alto nível quando a repetição mostrar que o nível está baixo (0:04:09 a 0:04:54). A refatoração acontece também no teste, que é código; a facilidade do teste depende do desacoplamento, design ruim é teste difícil, e por isso se gosta de testar primeiro (0:04:54 a 0:05:23). Comece pelo caminho de sucesso, sem bancar o corvo pessimista, e só depois os corner cases, o corrimão da escada (0:05:23 a 0:05:53). Organize por expandir e colapsar: começa tudo num arquivo só, passou o teste, para e olha; o código vai gritar para sair; software se faz por demãos, não em série de indústria (0:05:53 a 0:06:55). Põe os testes numa pasta irmã da do projeto e não se estressa por enviá-los a produção num sistema web; com muitas partes móveis, Docker para manter o ambiente de teste perto do de produção (0:06:55 a 0:08:30). Práticas: TDD [legenda: DDD] como técnica de design, declarativa, que define o fim para fazer o começo (0:08:30 a 0:09:13); BDD com linguagem como Gherkin [legenda: just] e dado, quando, então [legenda: guia vendendo], útil com gente de negócio mas cara de implementar; ele prefere testes de caixa preta com asserções normais e uma docstring (0:09:13 a 0:10:32; a frase faço DDD com DDD, 0:10:08, é provavelmente BDD com TDD, leitura incerta); teste de aceitação para definir requisito com quem opera, com a pegadinha de pedir fluxos caros e desnecessários (0:10:32 a 0:11:33). Integração contínua é a última coisa que ele monta: a prioridade é o programador sempre poder rodar todos os testes sozinho na máquina dele; CI é mais uma camada, não a salvação (0:11:33 a 0:12:45); gosta de usar o que todo mundo usa e detesta configurar (0:12:45 a 0:13:16). Ferramentas complementares: depurador e tracer para ver o filme do sistema legado (0:13:16 a 0:14:19), profiler por amostragem para achar o que mais roda (0:14:19 a 0:14:58), linter, e coverage, que só diz quais linhas rodaram; o único uso é revelar cenário faltando, e ele não usa meta, usa a cobertura do que importa pelo risco (0:15:05 a 0:16:55). Comer pelas beiradas: um sistema lento é bom lugar para começar, porque performance pede menos conhecimento do negócio (0:16:55 a 0:17:25). O método para legado: amarração [legenda: integração, 0:17:59; suturazinha, 0:18:12; amarraçãozinha, 0:20:12], um teste do caso de sucesso que prende o comportamento; ordenação, linearizar e agrupar o que é parecido, sem mudar nada; separação, extrair blocos para funções; redução, até ter testes unitários de cada parte e um de integração da chamada, terminando num serviço ou num desmembramento (0:17:37 a 0:19:52). Cita uma palestra dele no YouTube em que reduziu um código de cliente de 859 para 13 linhas assim, rodando o teste a cada mudança para não matar o paciente (0:19:52 a 0:20:32). Fecha com dependências externas: nunca acessar uma API diretamente, criar um cliente ou serviço substituível (0:20:32 a 0:20:54; a legenda termina no meio da frase).

Linha do tempo:
- [0:00:00] o que faz um teste bom ou ruim
- [0:00:22] o GitHub chamado em 15 lugares
- [0:01:00] camadas de indireção
- [0:03:20] teste como o código reage às falhas críticas
- [0:03:52] defina axiomas
- [0:04:09] não se limite ao framework de testes
- [0:05:12] design ruim, teste difícil
- [0:05:23] comece pelo caminho de sucesso
- [0:06:05] expandir e colapsar; por demãos
- [0:07:06] testes numa pasta irmã; Docker
- [0:08:43] TDD, BDD, aceitação
- [0:11:51] integração contínua é a última coisa
- [0:13:16] depurador, tracer, profiler, linter, coverage
- [0:16:14] cobertura sem meta, pelo risco
- [0:17:59] amarração, ordenação, separação, redução
- [0:20:03] de 859 para 13 linhas
- [0:20:45] nunca acesse uma API diretamente

Princípios:
- O teste não muda quando a implementação muda (0:00:00 a 0:00:22).
- Ponha uma camada de indireção sua entre o sistema e cada dependência externa, e use um stub dela no teste (0:01:00 a 0:03:20; 0:20:32 a 0:20:54).
- Teste a reação às falhas críticas, não só o sucesso (0:03:20 a 0:03:52).
- Defina axiomas; não teste o que não é seu (0:03:52 a 0:04:09).
- O teste é código e se refatora; design ruim, teste difícil (0:04:54 a 0:05:23).
- Caminho de sucesso primeiro, corner cases depois (0:05:23 a 0:05:53).
- Comece junto, pare, olhe e separe: por demãos (0:05:53 a 0:06:55).
- Todo programador roda todos os testes na própria máquina antes de qualquer CI (0:11:51 a 0:12:19).
- Cobertura revela cenário faltando; não é meta (0:16:01 a 0:16:55).
- Legado: amarração, ordenação, separação, redução, rodando o teste a cada mudança (0:17:59 a 0:20:32).

Código: reconstrução a partir da fala; não publicada. Os nomes são deste documento; ele diz fecha pull request, abre e lista, recebendo só o número (0:01:07 a 0:01:49), e o teste com um stub que retorna verdadeiro num cenário ou 30 mensagens noutro (0:01:49 a 0:02:11).

```python
# reconstrução a partir da fala, não publicada
# github.py: a única porta do sistema para o GitHub
def close_pull_request(number):
    ...  # a chamada HTTP mora só aqui, mesmo repetida entre as três funções

def open_pull_request(number):
    ...

def list_pull_requests():
    ...


# no teste: a lógica de quem chama, sem rede
def test_fecha_pr_quando_aprovado():
    calls = []
    stub = lambda number: calls.append(number) or True   # stub para este cenário
    review(42, close=stub)                               # review: o código sob teste, hipotético
    assert calls == [42]
```

Citações (paráfrases de legenda, não verificadas):
- [0:00:20] um teste para mim é ruim quando eu tenho uma relação de um para um entre alteração no código e alteração no teste
- [0:01:07] eu crio camadas de em direção termo importantíssimo [em direção: indireção]
- [0:05:14] design ruim teste difícil
- [0:06:47] software acontece por demão
- [0:12:01] minha prioridade é que o programador sempre possa rodar os testes todos sozinho na marca dele sempre [marca: máquina]
- [0:20:20] roda o teste passou é para verificar se eu não tô matando o paciente

### Aula 8: #08 - Conclusão
Vídeo: https://www.youtube.com/watch?v=CSFlxRecqNY · Duração: 3:21

Resumo: a conclusão é que é preciso se tornar capaz de testar; o teste é sempre o mínimo necessário e é mais um processo de abordar o desenvolvimento do que uma ferramenta ou um tipo (0:00:00 a 0:00:25). A dificuldade é tentar entender teste pelos conceitos em vez de pela expressão do exercício, então é preciso praticar (0:00:25 a 0:00:36). Por isso dá de presente o Raio-X do TDD [legenda: raio-x do teste de vela, raio-x do teste de medavelmente], onde demonstra um kata, para ir direto à mão na massa, com referências de sites de exercícios (0:00:36 a 0:01:43). Quer depois um curso só de kata, mais avançado (0:01:43 a 0:02:04), pede compromisso com a prática e com as missões do curso [legenda: missão solo, missão clã, missão resgate] (0:02:04 a 0:02:40) e encerra com o testemunho de convertido: internalizar o teste muda tudo o que se pensa sobre programação (0:02:40 a 0:03:05). Abre para perguntas (0:03:05 a 0:03:15).

Linha do tempo:
- [0:00:00] a conclusão: tornar-se capaz de testar
- [0:00:13] sempre o mínimo necessário; um processo
- [0:00:25] conceito contra exercício
- [0:00:47] o Raio-X do TDD de presente
- [0:01:43] um curso só de kata
- [0:02:16] as missões
- [0:02:52] testemunho de convertido

Princípios:
- O teste é sempre o mínimo necessário (0:00:13 a 0:00:25).
- Aprende-se teste pelo exercício, não pelo conceito (0:00:25 a 0:00:36).

Código: nenhum.

Citações (paráfrases de legenda, não verificadas):
- [0:00:13] o teste é sempre o mínimo necessário e ele é muito mais um processo de como você aborda os homens de software [homens: provável desenvolvimento ou problemas]
- [0:00:25] as pessoas tentam entender teste pela compreensão dos conceitos ao invés de entender teste Pela expressão do exercício
- [0:02:52] é testemunho de convertido vai mudar tudo que você pensa sobre a programação

## 6. Princípios que atravessam toda a série

Doze regras que ele formula na fala. Nenhuma é inferência deste documento, e nenhuma vem de trecho de participante. A linha entre colchetes diz se a regra já existe em `kb/principles/` ou é nova.

#### 1. Teste procura defeitos para dar confiança; não prova nada

Testar é descobrir erros e defeitos, não validar que funciona, e mais defeitos encontrados dão mais confiança (aula 2, 0:00:20 a 0:01:29). Teste não é garantia, não é prova, não é bala de prata; confiança é o que importa (aula 3, 0:15:32 a 0:15:57). Nenhum número de testes resolve o problema de escopo, porque a natureza do teste não garante nada (aula 1, 0:15:27 a 0:15:37); no fim, ele não dá garantia, faz análise de risco (aula 7, 0:16:22 a 0:16:43).

[novo]

#### 2. O mínimo possível, nunca menos que o mínimo, escolhido por risco e contexto

Sempre o mínimo possível, nunca menos, achado por análise de risco (aula 2, 0:04:38 a 0:05:10). A pergunta é o que preciso testar, e os riscos são de vida, financeiro, de reputação, de oportunidade, de orçamento e de prazo (aula 3, 0:16:34 a 0:17:05); o teste depende do contexto (aula 3, 0:18:13 a 0:18:35; aula 5, 0:01:32 a 0:02:29). A cobertura segue a mesma régua (aula 7, 0:16:01 a 0:16:34), e o curso fecha nela (aula 8, 0:00:13).

[novo; vizinho de pragmatismo-sobre-pureza]

#### 3. Teste o efeito, não o código

Não teste o código, teste o efeito do código, para que mudar a implementação não mexa no teste (aula 4, 0:07:20 a 0:08:54). O estado inicial, o final e a transição importam; a implementação tem de poder mudar (aula 3, 0:05:12 a 0:05:32). Prefere caixa preta porque testa o efeito (aula 5, 0:07:17 a 0:07:30). Teste ruim é o que muda um para um com o código (aula 7, 0:00:11 a 0:00:22).

[novo; vizinho de a-interface-e-o-que-importa, que é sobre desenho de API]

#### 4. Contra a complexidade exponencial, código com código, o tempo todo

Teste manual é linear contra uma força exponencial e perde; só quem programa faz a foto linear que mapeia a execução exponencial, e por isso teste é parte do desenvolvimento (aula 1, 0:25:49 a 0:27:12). Mudar um software testado o desestabiliza, e à mão seria preciso testá-lo todo de novo (aula 2, 0:03:06 a 0:03:27). Sem teste, funciona por acaso (aula 2, 0:07:13).

[já no KB: `kb/principles/taft.md`]

#### 5. Teste cedo, e deixe o teste moldar o design

Quanto mais cedo melhor, e daí o gosto pelo teste primeiro: foto e filme em ciclo (aula 2, 0:02:23 a 0:03:06). Testar passo a passo mostra o design que permite o teste, porque há código virtualmente impossível de testar depois (aula 2, 0:03:27 a 0:04:00). Design ruim, teste difícil, e por isso se testa primeiro (aula 7, 0:05:12 a 0:05:23); o TDD define o fim para fazer o começo (aula 7, 0:08:43 a 0:09:08).

[já no KB: `kb/principles/teste-primeiro-das-folhas.md`]

#### 6. Pense de trás para frente

A incapacidade de pensar de trás para frente inviabiliza o teste (aula 3, 0:06:06 a 0:08:02). Do imperativo ao declarativo: não diga o que fazer, explique o que deseja (aula 3, 0:04:45 a 0:05:12). O desafio é esculpir o caminho de trás para frente, sem pular etapa (aula 4, 0:01:45 a 0:01:58).

[novo]

#### 7. Ponha uma camada de indireção sua diante de cada dependência externa

O GitHub chamado em 15 lugares vira três funções suas; no teste, um stub delas, e a lógica de quem chama se testa sem rede (aula 7, 0:00:22 a 0:02:34). É uma mudança pequena para uma ordem de grandeza em facilidade de teste (aula 7, 0:02:50 a 0:03:20). Nunca acesse uma API diretamente; crie um cliente ou serviço substituível (aula 7, 0:20:32 a 0:20:54). O mesmo isolamento aparece no unitário, que isola os colaboradores (aula 5, 0:15:16 a 0:15:36).

[novo; vizinho de superficie-de-contato e de isolamento-interacao-impacto]

#### 8. Defina axiomas: não teste o que não é seu

O Postfix, estabelecido no mercado, é axioma, e o envio de e-mail se testa com um mock (aula 5, 0:17:08 a 0:17:55). Ao estender um framework, teste só o comportamento que se acrescenta e parta do pressuposto de que o framework foi testado (aula 7, 0:03:52 a 0:04:09). Um banco específico também é axioma: desenvolva e teste com ele, sem misturar (aula 6, 0:07:05 a 0:07:27).

[novo; vizinho de use-o-framework-sem-abstrai-lo]

#### 9. Legado: amarre, ordene, separe, reduza, sem reengenharia

Ele não faz reengenharia: extrai o trecho crítico para uma função ao lado e testa só ele, um transplante (aula 3, 0:09:53 a 0:11:20; 0:13:19 a 0:13:51). O método tem quatro etapas: amarração pelo caso de sucesso, ordenação sem mudar nada, separação em funções e redução até testes unitários de cada parte (aula 7, 0:17:59 a 0:19:52), rodando o teste a cada mudança para não matar o paciente (aula 7, 0:20:12 a 0:20:32).

[já no KB: `kb/principles/execute-antes-de-ler.md` e `kb/principles/refatore-sem-matar-o-paciente.md`]

#### 10. Caminho de sucesso primeiro, depois as falhas críticas

Comece pelo caminho de sucesso, sem bancar o corvo pessimista; depois os corner cases (aula 7, 0:05:23 a 0:05:53). Mas teste também a reação às falhas críticas, para o usuário não ver spinner infinito nem erro 500 (aula 7, 0:03:20 a 0:03:52). No legado, a amarração começa pelo caso de sucesso (aula 7, 0:18:02 a 0:18:21).

[vizinho de funcione-direito-e-depois-rapido]

#### 11. Comece junto, pare, olhe e separe

Comece com tudo junto e separe conforme as categorias aparecem (aula 6, 0:04:06 a 0:04:29). Expandir e colapsar: tudo num arquivo, passou o teste, para, olha; software se faz por demãos (aula 7, 0:05:53 a 0:06:55). O teste é código e se refatora (aula 7, 0:04:54 a 0:05:03).

[já no KB: `kb/principles/deixe-o-codigo-descansar.md` e `kb/principles/nao-projete-a-generalizacao.md`]

#### 12. Passos de bebê, e se aprende praticando

Passos de bebê, suspendendo a certeza (aula 4, 0:00:06 a 0:01:58); teste é outra forma de programar (aula 4, 0:04:01 a 0:04:12) e se aprende com kata, dojo e par, não no sistema da empresa (aula 4, 0:04:23 a 0:05:37). Entende-se teste pela expressão do exercício, não pelos conceitos (aula 8, 0:00:25 a 0:00:36).

[novo]

Evidência para outros princípios do KB, fora da lista acima: a regra de código linear (aula 1, 0:07:55 a 0:08:29) para `kb/principles/codigo-linear.md`; a distinção do reporter entre erro e falha (aula 6, 0:03:33 a 0:03:48) para `kb/principles/erro-antes-da-falha.md`; o não como ferramenta e a negociação de soluções (aula 1, 0:13:17 a 0:17:29) para `kb/principles/reserva-para-dizer-nao.md`, como vizinho.

## 7. Citações-chave do curso

Paráfrases de legenda automática, sem aspas e não verificadas contra o vídeo. Nenhuma linha vem de trecho de participante.

| Aula | Timestamp | Paráfrase |
|---|---|---|
| #1 | 0:07:07 | o software quebra porque a gente programa uma foto nosso código é uma foto enquanto o código rodando que aquilo que a gente quer executar é um filme |
| #1 | 0:08:17 | Mantenha o seu código mais linear possível |
| #1 | 0:13:44 | a melhor ferramenta é não vou fazer isso não vai entrar |
| #1 | 0:21:03 | só o código é código só o código roda |
| #1 | 0:26:20 | toda vez que você usar uma estratégia linear para lutar contra uma força exponencial você vai perder |
| #1 | 0:27:00 | fogo código com código é por isso que o teste é parte do processo de desenvolvimento |
| #2 | 0:00:57 | o objetivo de testar é para você não é para validar que o software funciona não eu quero pegar os erros e defeito |
| #2 | 0:04:47 | é sempre o mínimo possível nunca menos que o mínimo possível |
| #2 | 0:06:06 | os testes eles não eliminam essa instabilidade eles contém o efeito da entropia |
| #2 | 0:07:13 | um software sem teste funciona por acaso |
| #3 | 0:03:40 | O código é um meio não fins |
| #3 | 0:07:42 | a incapacidade de pensar de trás para frente inviabiliza execução de Teste |
| #3 | 0:15:46 | confiança é o que importa |
| #3 | 0:16:34 | começa a perguntar o que eu preciso testar |
| #4 | 0:04:08 | teste não é simplesmente uma extensão da programação ela é uma outra forma de programar |
| #4 | 0:07:24 | não teste código teste o efeito do código |
| #5 | 0:06:09 | é tudo sorvete só muda o sabor |
| #5 | 0:07:23 | Eu prefiro o teste caixa preta do que o teste caixa branca |
| #6 | 0:03:48 | teste é sobre expectativa |
| #6 | 0:10:07 | ele é uma moldura e negativo do chamador |
| #7 | 0:00:20 | é ruim quando eu tenho uma relação de um para um entre alteração no código e alteração no teste |
| #7 | 0:05:14 | design ruim teste difícil |
| #7 | 0:12:01 | o programador sempre possa rodar os testes todos sozinho na marca dele [marca: máquina] |
| #8 | 0:00:25 | entender teste Pela expressão do exercício |

## 8. A evolução técnica, aula a aula

Não há programa que evolua: o curso não escreve código. A tabela mostra a evolução dos conceitos, do contexto à prática.

| Etapa | O que é feito | Conceito ou ferramenta | O que isso destrava |
|---|---|---|---|
| **#1** | Origem do teste, foto e filme, o não, crítica da indústria de QA (0:00:24 a 0:34:42) | validação formal contra empírica | Teste como parte do desenvolvimento, não como departamento |
| **#2** | Testar é achar defeitos; quando e quanto testar (0:00:20 a 0:07:49) | Myers 1979, campo minado, análise de risco | O critério do mínimo necessário |
| **#3** | O código é meio; de trás para frente; transplante em legado; o que o teste não é (0:02:31 a 0:18:44) | foco em resultado, declarativo | A pergunta certa: o que testar |
| **#4** | Passos de bebê; kata, dojo, par; testar o efeito (0:00:00 a 0:08:54) | prática deliberada | Como começar |
| **#5** | Estático e dinâmico, caixa preta e branca, partição e limite, unitário a regressão (0:02:39 a 0:25:04) | análise de valor limite, mock, smoke, fuzz | Vocabulário sem efeito checklist |
| **#6** | Erro, defeito, falha; discovery, runner, reporter; dublês (0:00:10 a 0:11:28) | dummy, fake, stub, spy, mock | Ler um relatório e escolher o dublê |
| **#7** | Indireção, recomendações, organização, TDD, BDD, CI, ferramentas, método de legado (0:00:00 a 0:20:54) | camada de indireção, coverage, amarração | Aplicar no código do dia a dia |
| **#8** | Conclusão e o Raio-X do TDD (0:00:00 a 0:03:15) | kata | A prática que o curso deixa para depois |

## 9. Arsenal técnico demonstrado no curso

Nada é demonstrado em tela; tudo é descrito. A coluna diz onde ele descreve.

| Técnica ou recurso | Para que ele usa | Aula e timestamp |
|---|---|---|
| Mapa mental | Conduzir a aula passo a passo | #1, 0:00:00; #8, 0:03:05 |
| Reescrever tarefa como resultado | Sair do o que fazer para o por que | #3, 0:04:01 a 0:04:45 |
| Extrair o miolo de um loop para função ao lado | Pôr teste num trecho crítico de legado sem reengenharia | #3, 0:09:53 a 0:11:20 |
| Kata, coding dojo, programação em par | Aprender teste | #4, 0:04:23 a 0:06:21 |
| Representação no lugar do objeto do ORM | Não acoplar o teste à estrutura de dados | #4, 0:07:44 a 0:08:09 |
| Code review, linter, sistema de tipos, analisadores | Teste estático | #5, 0:02:50 a 0:05:41 |
| Partição de equivalência e valor limite | Escolher poucas entradas para um comportamento infinito | #5, 0:07:30 a 0:12:38 |
| Teste de regressão a partir do suporte | Impedir que o mesmo erro volte | #5, 0:14:00 a 0:14:42; 0:24:54 |
| Mock do serviço de e-mail | Tirar o Postfix do teste | #5, 0:17:08 a 0:17:55 |
| Smoke test diário | Rodar o caminho feliz do que é crucial | #5, 0:19:41 a 0:20:32 |
| Fuzz e Hypothesis | Entradas aleatórias; ele não usou a biblioteca | #5, 0:20:42 a 0:22:35 |
| Teste de carga e de estresse | Validar a carga prevista e o pico fora do padrão | #5, 0:23:08 a 0:24:54 |
| Discovery, seleção, runner, reporter | Anatomia de um framework de testes | #6, 0:01:57 a 0:03:33 |
| Setup, teardown, fixture | Preparar e limpar o estado | #6, 0:05:31 a 0:07:05 |
| Dummy, fake, stub, spy, mock; `assert_called_with` | Dublês de teste | #6, 0:07:27 a 0:11:28 |
| Camada de indireção | Isolar dependência externa e trocá-la por stub | #7, 0:01:00 a 0:03:20; 0:20:32 |
| Asserções de mais alto nível | Tirar repetição do teste | #7, 0:04:13 a 0:04:34 |
| Expandir e colapsar | Organizar código e testes | #7, 0:05:53 a 0:06:55 |
| Testes em pasta irmã; Docker | Navegar fácil e manter o ambiente perto de produção | #7, 0:07:06 a 0:08:30 |
| Gherkin, dado, quando, então | BDD com gente de negócio | #7, 0:09:13 a 0:10:08 |
| Integração contínua | Camada extra depois de todos rodarem tudo localmente | #7, 0:11:40 a 0:12:45 |
| Depurador e tracer | Ver o filme do legado | #7, 0:13:16 a 0:14:19 |
| Profiler por amostragem | Achar o que mais roda | #7, 0:14:19 a 0:14:58 |
| Coverage | Revelar cenário faltando, sem meta | #7, 0:15:05 a 0:16:55 |
| Amarração, ordenação, separação, redução | Refatorar legado com teste | #7, 0:17:59 a 0:20:32 |

## 10. Glossário do curso

| Termo | Significado no contexto da série | Onde |
|---|---|---|
| **Labirinto** | O universo de teste, com seus tipos e nomes, em que a turma se perde | #1, 0:00:13; #6, 0:00:00 |
| **Foto e filme** | O código escrito e o código em execução, separados pela dimensão do tempo | #1, 0:06:55 a 0:07:46 |
| **Executor de demanda** | Quem faz o que pedem, sem voz | #1, 0:16:02 a 0:16:15; #3, 0:03:38 |
| **Negociador de soluções** | A postura que ele propõe acima de resolver problemas | #1, 0:16:53 a 0:17:29 |
| **Indústria de QA** [legenda: indústria de que há] | Processos, certificações e departamentos de qualidade separados do código | #1, 0:18:32 a 0:22:11 |
| **Erro** | Equívoco humano no código | #2, 0:00:31; #6, 0:00:10 |
| **Defeito** | O efeito do erro, a tela azul | #2, 0:00:42; #6, 0:00:20 |
| **Falha** | A manifestação do defeito na execução, num contexto e instante | #6, 0:00:20 a 0:00:44 |
| **Erro e falha no reporter** | Exceção não tratada contra expectativa não atendida | #6, 0:03:33 a 0:03:48 |
| **Transplante** | Extrair um trecho crítico de legado sem mudar sua definição, para testá-lo | #3, 0:13:19 a 0:13:42 |
| **Efeito checklist** | Querer todos os tipos e métricas de teste ao mesmo tempo, fora de contexto | #5, 0:01:10 a 0:02:29 |
| **Caixa preta / caixa branca** | Teste pelo contrato contra teste pela estrutura e pelos caminhos | #5, 0:06:32 a 0:07:30; 0:12:38 |
| **Teste empírico** | Teste que vem da experiência no domínio, como a regressão do suporte | #5, 0:13:50 a 0:14:42 |
| **Axioma** | Premissa assumida que não se testa: o Postfix, o framework, o banco específico | #5, 0:17:08; #6, 0:07:17; #7, 0:03:52 |
| **Smoke test** | Ligar e ver se sai fumaça: o caminho feliz do crucial, todo dia | #5, 0:19:41 a 0:20:32 |
| **Fuzz** [legenda: fase, fãs] | Entradas aleatórias para sondar limites desconhecidos | #5, 0:20:42 a 0:21:18 |
| **Dummy** [legenda: Dani] | Objeto passado e nunca usado | #6, 0:07:57 a 0:08:13 |
| **Fake** | Colaborador real feito por atalho, como banco em memória | #6, 0:08:13 a 0:08:37 |
| **Stub** [legenda: step, stand, estande, estabele] | Objeto esculpido para dar respostas específicas | #6, 0:08:37 a 0:08:59; #7, 0:01:49 |
| **Spy** [legenda: Spice] | Stub que anota como foi usado | #6, 0:09:06 a 0:09:20 |
| **Mock** [legenda: Moque, Moc, Nokia] | Objeto com expectativas sobre o chamador; a moldura em negativo | #6, 0:09:20 a 0:10:17 |
| **Camada de indireção** [legenda: em direção] | Função ou serviço seu entre o sistema e a dependência externa | #7, 0:01:00 a 0:03:20 |
| **Expandir e colapsar** | Começar junto e separar depois de olhar | #7, 0:05:53 a 0:06:14 |
| **Demão** | Cada passada sobre o código até ficar bom bastante | #7, 0:06:36 a 0:06:55 |
| **Amarração, ordenação, separação, redução** | O método dele para legado com teste | #7, 0:17:59 a 0:20:32 |
| **Passos de bebê** | Avançar sem pular etapa | #4, 0:00:00 a 0:01:58 |
| **Kata** [legenda: catar] | Exercício repetido para treinar a forma | #4, 0:02:56; 0:04:23 |

## 11. Perguntas e respostas que o curso responde

#### O que é testar?

Analisar um programa com a intenção de descobrir erros e defeitos, para aumentar a confiança; não é provar que funciona (aula 2, 0:00:20 a 0:01:29; aula 3, 0:15:32 a 0:15:57).

#### Quando testar?

Quanto mais cedo melhor, em ciclo com o código (aula 2, 0:02:23 a 0:03:36).

#### Quanto testar?

O mínimo possível, nunca menos que o mínimo, por análise de risco no contexto (aula 2, 0:04:38 a 0:05:10; aula 3, 0:16:34 a 0:18:35).

#### Qual a forma certa de testar?

Não há fora do contexto; o certo é o que atende o cliente (aula 3, 0:18:13 a 0:18:35; aula 5, 0:02:09 a 0:02:29).

#### Por que é tão difícil testar?

Porque se acredita que programar é sobre código, e falta pensar de trás para frente, do resultado ao começo (aula 3, 0:02:31 a 0:03:50; 0:07:42 a 0:07:54).

#### Como começar?

Com passos de bebê, kata, dojo e par com quem sabe, não no sistema da empresa (aula 4, 0:00:06 a 0:05:37).

#### O que o teste deve verificar?

O efeito, não o código; se a implementação muda, o teste não deveria mudar (aula 4, 0:07:20 a 0:07:31; aula 7, 0:00:11 a 0:00:22).

#### Quantos testes para uma regra de faixa, como idade entre 18 e 60?

Dois testes, um para cada estado, com os limites 17, 18, 60 e 61, e ele acrescenta um valor do meio, 30 (aula 5, 0:09:06 a 0:10:24).

#### O que é unitário e o que é integração?

Unitário testa algo sem dependência, isolando colaboradores; integração atravessa componentes; os dois são adjetivos de uma mesma essência (aula 5, 0:15:16 a 0:16:42; 0:18:22 a 0:18:44).

#### Qual a diferença entre stub e mock?

Stub dá respostas específicas; mock tem expectativas sobre como é chamado e verifica o chamador (aula 6, 0:08:37 a 0:09:44).

#### Como testar código que chama uma API externa?

Pôr uma camada de indireção sua e usar um stub dela no teste; nunca acessar a API diretamente (aula 7, 0:01:00 a 0:02:34; 0:20:32 a 0:20:54).

#### Devo ter meta de cobertura?

Não; a cobertura revela caminhos sem cenário, e se olha a cobertura do que importa pelo risco (aula 7, 0:15:51 a 0:16:34).

#### Quando montar integração contínua?

Por último, depois que todo programador roda todos os testes sozinho na máquina dele (aula 7, 0:11:51 a 0:12:19).

#### Como pôr teste em código legado?

Sem reengenharia: amarrar o caso de sucesso num teste, ordenar sem mudar nada, separar em funções e reduzir, rodando o teste a cada mudança (aula 3, 0:09:53 a 0:11:20; aula 7, 0:17:59 a 0:20:32).

#### Como convencer um chefe que acha teste um custo?

Medindo o custo da equipe, o que cada projeto consome e quanto do tempo vai para correção (aula 1, 0:31:23 a 0:33:26).

## 12. Repositórios e recursos

| Recurso | Onde encontrar | Observação |
|---|---|---|
| Playlist completa (fonte desta documentação) | [Superando o Labirinto dos Testes de Software](https://www.youtube.com/playlist?list=PLeKXYyZCJHxfGaSISKQtt4we_3wmuZEzg) | 8 vídeos. Os ids estão em `playlist.json` e nos links da seção 5. |
| Canal | [HB Network](https://www.youtube.com/@hbnetworkoficial) | |
| Raio-X do Test-Driven Development | `kb/courses/raio-x-do-tdd.md` | Curso dele dado de presente na aula 8 (0:00:47 a 0:01:21) como a parte prática. |
| Aula de kata gravada por ele | no YouTube, sem URL | Citada na aula 4 (0:05:47 a 0:05:59); nome do kata não legível [legenda: rap numbers]. |
| Palestra dele sobre refatorar 859 linhas em 13 | no YouTube, sem URL | Citada na aula 7 (0:19:52 a 0:20:03); ele não lembra quando foi. |
| Dojo Rio | citado, sem URL | Onde ele aprendeu programação com teste, por volta de 2006 e 2007 (aula 4, 0:04:34 a 0:04:47). |
| Myers, 1979 | citado, sem título | A definição de testar (aula 2, 0:00:20); provavelmente The Art of Software Testing, de Glenford Myers, leitura deste documento. |
| Palestra de Bret Victor | citada, sem URL nem título legível | Sobre ver o efeito do código enquanto se programa (aula 1, 0:09:14 a 0:09:52). |
| Artigo sobre a complexidade do software | citado, título não legível | [legenda: the Rambo programa] (aula 1, 0:06:03); leitura provável The Humble Programmer, incerta. |
| Refatoração com POO em código legado | `kb/courses/refatoracao-poo-legado.md` | O método de legado da aula 7 aplicado ao vivo; contraste na seção 2.5. |

Repositórios do curso: **nenhum**. O curso não escreve código e não cita repositório, caminho ou commit.

## 13. Análise linha a linha do código real

O curso não publica código, portanto não há análise de código real. As três reconstruções da seção 5 (a faixa de idade, o mock com `assert_called_with`, a camada de indireção para o GitHub) são ilustrações a partir da fala, com nomes deste documento. Limites que ficam registrados:

- A condição da faixa de idade sai truncada na legenda (aula 5, 0:07:50 a 0:08:04); a leitura 18 a 60 inclusive vem da fala posterior (0:11:41 a 0:11:54).
- Nomes e siglas mal ouvidos que esta documentação corrige por leitura provável: TDD [DDD] (aula 7, 0:08:43), Gherkin [just] e given, when, then [guia vendendo] (aula 7, 0:09:17 a 0:09:33), pull request [pou Quest, curricrash, correque] (aula 7, 0:00:34 a 0:01:36), indireção [em direção] (aula 7, 0:01:07), amarração [integração] (aula 7, 0:17:59), Eventbrite [evento Bright] (aula 5, 0:23:42), SRE [srr site sem dinheiro] (aula 5, 0:24:42), Heroku [herocco] (aula 7, 0:07:28), Redis [Heads] e Postgres [posto] (aula 7, 0:12:55), debugger [the bug, the Burger, deban] (aula 7, 0:13:16 a 0:14:08), Deming [Demi], lean [link] e just in time [Sin timer] (aula 1, 0:20:01).
- Leituras que ficam incertas: a frase faço DDD com DDD (aula 7, 0:10:08), provavelmente BDD com TDD; o termo Exception como teste de aceitação (aula 7, 0:10:32); a lista de siglas da aula 1 [psdr cmmi ai tio cobaltivo] (0:20:12), em que só CMMI é legível; o nome do kata [rap numbers] (aula 4, 0:05:49); o título da palestra de Bret Victor (aula 1, 0:09:14).
- Ele data em 1969 a conferência da OTAN em que se cunhou engenharia de software (aula 1, 0:01:00 e 0:05:48); a data fica como ele diz.

## 14. Execução real dos testes

O curso não publicou código nem suíte. Não há o que rodar. As reconstruções da seção 5 não foram executadas nesta documentação; a da camada de indireção depende de uma função `review` hipotética.

---

Documentação elaborada a partir das transcrições das 8 aulas da playlist Superando o Labirinto dos Testes de Software, de Henrique Bastos (HB Network), playlist `PLeKXYyZCJHxfGaSISKQtt4we_3wmuZEzg`, legendas automáticas em português (pt-orig) capturadas em 2026-11-12. As citações são paráfrases das transcrições, não verificadas contra o vídeo (`verified: false`), renderizadas sem aspas e com os erros de reconhecimento anotados entre colchetes quando precisam aparecer. Falas de participantes identificadas (listadas no início) não são atribuídas a ele, e nenhum participante é nomeado. O curso não escreve código e não publica repositório; a aula de kata e a palestra citadas por ele não têm URL nas transcrições, e o mapa mental que conduz a aula não foi publicado. A legenda da aula #7 termina no meio da última frase. Datas de publicação e visualizações não foram coletadas. Conteúdo de caráter educativo.
