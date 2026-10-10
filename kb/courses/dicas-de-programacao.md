<!-- written by the henrique-ingest distiller on 2026-10-10 from sources/transcripts/dicas-de-programacao/; see kb/courses/README.md for provenance and license -->

HB Network · Documentação de curso

# Dicas de Programação

As 53 aulas curtas da playlist, lidas aula a aula a partir das legendas automáticas e das transcrições Whisper. Cada vídeo responde a uma pergunta, ou comenta um trecho de mentoria ou encontro ao vivo. Nenhuma aula mostra código legível e nenhum repositório é publicado pela série.

Instrutor: **Henrique Bastos** · Canal [HB Network](https://www.youtube.com/@hbnetworkoficial) · Playlist: [Dicas de Programação](https://www.youtube.com/playlist?list=PLeKXYyZCJHxdnGoV8TBYzKqsm8p3PIEeQ) · Repositório: nenhum URL nesta série

Documento elaborado a partir das transcrições das 53 aulas (legenda automática em português, pt-orig, capturada em 2026-10-10; as aulas 22 a 26, 30, 32, 33, 38, 46 e 49 vêm de transcrição Whisper pontuada). Várias aulas são recortes de conversas, com falas de participantes misturadas às dele; a legenda não marca quem fala, e a atribuição a ele só aparece quando o conteúdo permite.

## 1. Visão geral do curso

Dicas de Programação é uma coleção de **53 vídeos** que somam **9.408 segundos, 2 horas, 36 minutos e 48 segundos**. Os temas se espalham por três eixos. O primeiro é o método: rodar cedo, tratar tudo como hipótese até o código funcionar, fazer o mínimo de ponta a ponta e testar para poder mudar (aulas 1, 3, 13, 15, 16, 10 e 18). O segundo é o ofício em Python e Django: exceções específicas, migrações, escala, mocks, views pequenas, rotas e framework (aulas 20 a 25, 28, 33, 37, 41, 50, 51 e 52). O terceiro é a carreira e o aprendizado: responsabilidade, risco, reescrita, estudar fazendo, começar de onde se está (aulas 29, 31, 32, 34, 38, 47 e 49).

| Dimensão | Valor | Observação |
|---|---|---|
| Aulas | 53 | Playlist completa, numerada de 1 a 53. |
| Duração total | 9.408 s (2h 36min 48s) | Soma das durações em `playlist.json`. |
| Aula mais curta / mais longa | 34 s (#46) / 474 s (#47) | A #46, Python é amor, tem 0:34; a #47, melhores dicas para aprender, tem 7:54. |
| Datas de publicação | não coletadas | O `playlist.json` desta coleta traz id, título e duração. |
| Visualizações | não coletadas | Idem. |
| Transcrições | 53 de 53 disponíveis | 42 aulas em legenda automática (pt-orig) e 11 em Whisper pontuado (aulas 22 a 26, 30, 32, 33, 38, 46, 49). Não há legenda humana. |
| Legenda ruidosa | aulas 47, 48, 50, 51 e 52 | A estrutura em dicas é identificável, mas as citações dessas aulas são aproximações. As aulas 8, 31 e 45 também têm trechos pouco legíveis. |
| Código do curso | nenhum publicado | Nenhuma aula mostra código audível. Os únicos nomes de software que ele fala são o Decouple (aula 24, 0:00:00) e uma ferramenta de testes sem migrações (aula 22, 0:02:57). |

Nota de método: cada afirmação traz aula e timestamp. As citações são paráfrases de legenda, sem aspas, não verificadas contra o vídeo. Mis-hearings ficam entre colchetes. As seções 13 e 14 dizem que não há código a analisar nem suíte a rodar.

## 2. Filosofia e método de ensino

### 2.1 A resposta curta, em vez do curso longo

Cada vídeo parte de uma pergunta de aluno ou de um recorte de conversa e responde em um a sete minutos. A resposta costuma recusar a premissa da pergunta: a #21 separa controle de acesso de encapsulamento (0:00:11 a 0:00:34), a #28 diz que a analogia com controller funciona só como alegoria (0:00:08 a 0:00:20), a #29 diz que não gosta da estrutura da pergunta (0:00:04 a 0:00:50) e a #32 chama de estupidez o argumento do carro automático (0:00:00 a 0:00:26).

### 2.2 Metáforas de outras profissões

Ele troca a metáfora industrial pela do médico, que mantém um sistema sem reboot e sem reset (aula 27, 0:00:29 a 0:01:01). A mudança rapidinha do chefe vira sala de emergência de hospital, com uma cirurgia reparadora depois (aula 40, 0:00:37 a 0:01:16). A mudança de marcha serve para explicar automação (aula 32, 0:01:24 a 0:02:32), a guitarra para explicar aprendizado (aula 49, 0:01:47 a 0:02:08) e a obra de casa para explicar o cliente que muda no meio (aula 3, 0:01:58).

### 2.3 Processo antes de resultado

O aprender não tem compromisso com o resultado, só com o processo (aula 12, 0:00:00 a 0:00:06). Estudar é fazer: não se aprende lendo o livro, e sim programando (aula 38, 0:01:06). O repertório vem de experimentar e errar, e não há outro caminho (aula 43, 0:01:48 a 0:02:31). A lógica vem com a prática, e o ensino que fatia a experiência em conteúdos ignora o interesse da pessoa (aula 49, 0:00:37 a 0:01:09).

### 2.4 Responsabilidade como postura

A palavra volta em contextos distintos. Quanto mais responsabilidade se assume, melhor (aula 29, 0:01:35 a 0:01:43). Quem usa um projeto livre se responsabiliza por ele (aula 53, 0:03:50 a 0:03:57). Quem decide não fazer a etapa reparadora de uma emergência sabe que a conta técnica chega (aula 40, 0:02:09 a 0:02:18). O trabalho do programador é gerenciar risco e gerar resultado para o negócio (aula 31, 0:02:49 a 0:03:00).

### 2.5 Presença e decisão

Num trecho de encontro, o que gera liderança é presença, e isso é decisão, não personalidade nem temperamento (aula 5, 0:02:09 a 0:03:37). Disciplina é hábito, como tocar violão (aula 11, 0:00:21). O limite é dito na #12: não dá para trabalhar como um doido, tem de haver tempo para si, para a família e para o estudo (0:00:58 a 0:01:07).

## 3. Pilares conceituais

### 3.1 Feedback, hipótese e o mínimo de ponta a ponta

A pior coisa que se faz com um código é não botar para rodar, porque a primeira versão nunca é boa (aula 1, 0:00:06). Antes de o código funcionar, tudo é hipótese, e toda técnica existe para permitir o ciclo de feedback (aula 3, 0:00:33 a 0:00:56; aula 15, 0:03:38 a 0:03:51). O objetivo é fazer alguma coisa, não terminar algo completo (aula 13, 0:00:09), de ponta a ponta, e isso vale mais do que o genérico e bonito (aula 13, 0:02:27). Enquanto não há caso de sucesso rodando, adicionar coisas aumenta o risco de entrega, e o segredo é um escopo mínimo que dê os 20 por cento (aula 16, 0:00:17 a 0:00:56). O experimento é pequeno, barato e controlado (aula 15, 0:04:25 a 0:04:33), e não se gasta energia preparando um futuro que ainda não chegou (aula 15, 0:02:29).

### 3.2 O teste como modelagem e como custo de mudança

Começar pelo teste e por objetos simples em memória adia o banco e foca na camada de serviço (aula 4, 0:02:29 a 0:03:37). Começar pelo banco é olhar para o estado, e o que importa são as transições (aula 4, 0:03:41 a 0:04:15). O teste dói porque revela o que não se sabe e pode custar de quatro a cinco vezes mais tempo, mas mostra os limites das camadas (aula 10, 0:00:34 a 0:01:07). Com testes bem armados o código evolui para reduzir acoplamento e permitir mudança (aula 11, 0:03:07 a 0:03:43). Não há regra para saber o que testar, há bom senso treinado, e a unidade de teste cresce com o código (aula 18, 0:00:08 a 0:02:35). Mock em excesso denuncia acoplamento (aula 25, 0:01:16 a 0:01:27).

### 3.3 Mudança, legado e risco

O código precisa abraçar a mudança e localizar o esforço dela (aula 2, 0:00:28 a 0:00:53). Cada mudança negocia com o passado em prol de um futuro (aula 30, 0:01:38 a 0:01:54), e a ordem é fazer funcionar, fazer direito, fazer ficar rápido se precisar (aula 30, 0:01:59 a 0:02:08). Software com gente usando não tem reboot, e a pergunta é qual a menor mudança que aumenta a capacidade sem aumentar o código (aula 27, 0:00:54 a 0:01:58). Reescrever com outra tecnologia, arquitetura e escopo é fazer outro projeto, com orçamento e risco próprios (aula 31, 0:00:52 a 0:02:21). Para o legado há testes de regressão, refatoração e intervenções pontuais, e legado é software que dá dinheiro há muito tempo (aula 31, 0:03:51 a 0:04:22). A urgência se trata em duas etapas, estancar e depois reparar (aula 40, 0:01:45 a 0:01:58). A mudança rapidinha esconde uma necessidade real (aula 40, 0:00:24).

### 3.4 Python, Django e o uso de ferramentas prontas

A exceção específica deixa o código linear (aula 20, 0:00:50 a 0:01:47). Encapsulamento é conceito à parte do controle de acesso (aula 21, 0:00:20 a 0:00:34). A escala vem do perfil de uso e do uso eficiente de recursos, não de jogar tudo no framework (aula 23, 0:00:06 a 0:01:51). A view fica pequenininha (aula 28, 0:01:18 a 0:01:23). O desacoplamento do Django serve para intervir, e ele não abstrai o framework nem o ORM (aula 33, 0:00:17 a 0:02:18). Tudo é biblioteca, e o projeto é um pacote (aula 41, 0:00:15). Framework reúne padrões recorrentes e experiência coletiva (aula 51, 0:00:26 a 0:01:55), e não se deve construir o framework antes do sistema (aula 50, 0:00:14 a 0:00:29). Em Python, estética e função andam juntas (aula 26, 0:01:31 a 0:01:52; aula 46, 0:00:16 a 0:00:31).

### 3.5 Aprender, trabalhar e decidir com o outro

Foco e desfoco, convergência e divergência, e polinizar ideias com pessoas (aula 9, 0:00:39 a 0:00:54). Registrar o trabalho na hora, porque a memória é relacional (aula 6, 0:00:31 a 0:00:56). Requisitos em frases curtas, porque português é a linguagem mais importante (aula 17, 0:00:47 a 0:01:55). Padrões emergem depois do problema resolvido (aula 39, 0:01:01). A ferramenta no-code traz opinião embutida e custo de coordenação (aula 44, 0:01:02 a 0:02:43). Para quem começa: programar e copiar linha por linha, 80 por cento em prática (aula 38, 0:02:22 a 0:03:21), planejar o estudo (aula 47, 0:02:41), começar pelo pequeno (aula 48, 0:01:24), partir da menor versão do que se quer fazer (aula 49, 0:02:12 a 0:02:38) e não começar do zero, mas de onde se está (aula 34, 0:00:44 a 0:00:53).

## 4. As aulas em uma tabela

| # | Título | Duração | Foco em uma linha |
|---|---|---|---|
| 1 | Qual a pior coisa que você pode fazer com um código? | 2:30 | Não botar para rodar; a primeira versão é sempre ruim e melhora por interação (0:00:06). |
| 2 | Qual a importância em ter um código que permite ser mudado de forma fácil? | 1:41 | Código que abraça a mudança e localiza o esforço (0:00:28). |
| 3 | Até o código funcionar, tudo que você tem são hipóteses | 2:12 | Sem código rodando só há hipótese; técnicas servem ao feedback (0:00:33). |
| 4 | Importância da modelagem através dos testes | 6:59 | Começar por teste e objetos simples em memória, banco depois (0:03:15). |
| 5 | O poder da iniciativa | 3:48 | Presença gera liderança; marcar horário é decisão (0:02:09). |
| 6 | Registrar trabalho é materializar conhecimento | 1:42 | Registrar na hora, memória não é HD, visibilidade no remoto (0:00:31). |
| 7 | Desenrolo usando testes | 2:44 | Asserts simples em desafios técnicos e desenvolver junto ao teste (0:00:51). |
| 8 | A documentação do seu código é o teste | 1:20 | Plano inicial de projeto muda à revelia (0:00:41); trecho do título pouco legível. |
| 9 | Programador gosta muito de abaixar a cabeça e fazer | 0:59 | Alternar foco e desfoco e polinizar com outras pessoas (0:00:39). |
| 10 | Se você não tem tempo para fazer bem feito, quando você vai arranjar tempo para refazer? | 1:52 | Teste dói porque revela o que não se sabe e força design mutável (0:00:34). |
| 11 | Em software é muito mais caro fazer a coisa errada | 3:46 | Errado é o problema errado, não o código feio; testes e ritmo (0:01:54). |
| 12 | Toda nova habilidade que se desenvolve, não pode ter compromisso com resultado | 1:11 | Aprender novo sem compromisso com resultado e com tempo de descanso (0:00:00). |
| 13 | Faz funcionar, depois melhora | 3:51 | Ponta a ponta antes de genérico, com tempo como restrição (0:02:27). |
| 14 | Quanto mais bagagem a gente tem, mais a gente vê o Big steps e não o baby steps | 3:27 | Núcleo e heurística primeiro; bagagem esconde os baby steps (0:02:53). |
| 15 | Tudo que achamos sobre a solução do problema é uma mera hipótese | 6:13 | Crescer de um caso simples, evitar over-engineering, hipótese até rodar (0:03:38). |
| 16 | Os 20% que entregam 80% | 1:43 | Caso de sucesso rodando primeiro, escopo mínimo de 20 por cento (0:00:48). |
| 17 | Português é a linguagem mais importante do programador saber | 3:21 | Requisitos em frases curtas e consciência do modo de pesquisa (0:00:47). |
| 18 | Existe alguma regra para identificar o código que precisa ser testado? | 4:38 | Sem regra, bom senso; árvore de execução, previsibilidade e TDD (0:00:13). |
| 19 | O que fazer quando aparece um projeto que eu não domino a linguagem? | 5:13 | Avaliar a variabilidade do projeto contra a sua bagagem para estimar risco, e negociar o aprendizado. |
| 20 | Como usar o tratamento de exceção de forma certa? | 2:58 | Tratar exceções específicas, nunca a base, com blocos pequenos, para um código linear. |
| 21 | Qual sua opinião sobre Python não ter controle de acesso a métodos e atributos de um objeto? | 3:56 | Controle de acesso não é encapsulamento; a origem histórica vem de componentes sem código-fonte. |
| 22 | Como trabalhar com migrações em desenvolvimento e produção no Django? | 3:27 | Esquema e estado do banco são parte do código; gerar a migração junto com a mudança, no mesmo commit. |
| 23 | O que fazer para que um sistema em Django não saia do ar com muitos acessos? | 2:42 | Conhecer o perfil de uso e usar cache, CDN, índices e Redis em vez de sobrecarregar o framework. |
| 24 | Como foi o processo de criação do Decouple? | 2:29 | Biblioteca nascida de um problema próprio, API simples e extensível, resistência a inflar o escopo. |
| 25 | O que fazer para verificar um efeito colateral que não está explicito? | 1:47 | Usar Mock para registrar chamadas, com moderação, pois excesso indica acoplamento. |
| 26 | O que é pensamento Pythonico? | 3:03 | Níveis sintático, semântico e simbólico, Zen do Python e equilíbrio entre forma e função. |
| 27 | Como entender o software como um organismo vivo? | 2:56 | Metáfora do médico: menor mudança possível, entender o problema do cliente, sem reboot. |
| 28 | Por que não devemos considerar as views do Django como controllers? | 1:25 | View controla o conteúdo, template a apresentação; manter a view pequena. |
| 29 | É necessário um Web Developer aprender a tratar imagens? | 2:26 | Assumir responsabilidade e aprender o que o problema exige, em vez de dividir o trabalho em compartimentos. |
| 30 | Como lidar com mudanças no código? | 4:01 | Mudar código é negociar com o passado; faz funcionar, faz direito, faz ficar rápido; subir ao nível simbólico. |
| 31 | Quando o sistema é velho, ele precisa ser refeito? | 4:31 | Reescrever é outro projeto com risco e custo; o programador gerencia risco; técnicas para legado. |
| 32 | É ruim aprender a programar com Python? | 5:17 | Resolver problemas das pessoas e subir a abstração, em vez de fetiche por baixo nível. |
| 33 | Faz sentido trocar partes no Django? | 2:25 | Desacoplamento serve para intervir; não abstrair o framework nem o ORM. |
| 34 | Quem tem 30 anos, está começando tarde na programação? | 2:14 | Começar de onde se está, usando a bagagem de vida e o entendimento do negócio. |
| 35 | O que fazer quando se deparar com questões de operação? | 1:46 | Equipe pequena deve delegar operação a uma plataforma como serviço, como Heroku. |
| 36 | Conselho para quem mora no interior e quer aprender programação | 1:09 | Procurar quem faz o que você quer fazer e não se limitar à região. |
| 37 | Como criar rotas no Django do jeito certo | 1:49 | Evitar rota um-para-um com view; classe que compõe URLs a partir do modelo (aula 37, 0:01:03). |
| 38 | Como estudar programação do jeito errado | 4:46 | Programar e copiar código no lugar de ler tudo; 80% em prática (aula 38, 0:03:15). |
| 39 | Sintomas da Patternite | 1:31 | Resolver o problema antes de aplicar padrões; padrões emergem (aula 39, 0:01:01). |
| 40 | O que fazer quando seu chefe pede uma mudança "rapidinha"? | 2:37 | Emergência em duas etapas e comunicação do efeito colateral (aula 40, 0:01:45). |
| 41 | O conceito de app do Django, atrapalha ou ajuda? | 1:13 | Tratar tudo como biblioteca Python normal, não como apps (aula 41, 0:00:15). |
| 42 | Por que uso Wordpress no meu site, e, não Python e Django | 2:23 | Foco em gerar valor; Python e Django nos bastidores (aula 42, 0:00:05). |
| 43 | Dá para programar com uma lógica razoável? | 2:33 | Lógica vem da prática e do repertório; mostrar antes de explicar (aula 43, 0:01:16). |
| 44 | No Code: por que não funciona | 3:40 | Limites da opinião embutida e custo de coordenação entre ferramentas (aula 44, 0:02:17). |
| 45 | E quando o programador diz: FUNCIONA NA MINHA MÁQUINA? | 0:51 | Prints e vídeos; funciona na minha máquina é desculpa fraca (aula 45, 0:00:14). |
| 46 | Python é amor | 0:34 | Por que Python: estética e função juntas, código bonito e eficiente (aula 46, 0:00:28). |
| 47 | Melhores dicas para aprender a programar | 7:54 | Diário de estudo, plano, fundamentos, dividir problemas, arquivo de referências (aula 47, 0:01:59 a 0:05:43). |
| 48 | Não se distraia com "software de verdade" | 2:46 | Não perder o foco no problema; começar pequeno; curva não linear (aula 48, 0:01:24). |
| 49 | "Não adianta tentar programar.., tem que aprender lógica primeiro!" SERÁ MESMO? | 4:39 | Lógica vem com prática; menor versão do que se quer fazer (aula 49, 0:02:12). |
| 50 | Devo programar na mão ou usar um framework? | 2:48 | Não construir o framework antes do sistema; ler código livre (aula 50, 0:00:14). |
| 51 | Mas afinal, o que é um framework? | 2:23 | Padrões recorrentes e funções de alto nível sobre HTTP (aula 51, 0:00:26). |
| 52 | Qual a diferença entre Pyenv e Virtualenv? | 2:07 | pyenv gerencia interpretadores, virtualenv isola dependências (aula 52, 0:00:19). |
| 53 | Não economize pull request | 4:32 | Responsabilidade de quem usa open source; discutir ideia publicamente (aula 53, 0:03:50). |

## 5. Resumo por aula

### Aula 1: Qual a pior coisa que você pode fazer com um código?
Vídeo: https://www.youtube.com/watch?v=R6fhNjTb84w · Duração: 2:30

Resumo: ele conta que um código já passou por seis interações e diz que a pior coisa que se pode fazer com um código é não botar para rodar, porque a primeira versão nunca é boa. Relata um caso em que quase seguiu por um caminho com dicionários, achou o caminho ruim, pesquisou uma alternativa imutável e chegou a uma solução que achou expressiva e elegante, sempre por interação e lapidação (0:00:00 a 0:01:28).

Linha do tempo:
- [0:00:00] conta as interações do código, seis até hoje
- [0:00:06] a pior coisa é não botar para rodar
- [0:00:29] o caminho com dicionário (data e consents [leitura incerta]) parecia ruim
- [0:01:06] pesquisa Frozen dict e vê uma ideia de alguém no Instagram
- [0:01:16] decide fazer um Frozen sete [provável: frozenset]
- [0:01:19] o resultado fica expressivo e elegante, e veio por interação

Princípios:
- Rodar cedo e iterar: a primeira versão é sempre ruim, a qualidade vem de interações (0:00:06 a 0:00:12; 0:01:24).
- Mudar de caminho quando ele fica difícil: se está difícil, está errado, volta e simplifica (0:00:44 a 0:00:46; 0:01:40 a 0:01:44).

Código: nenhum mostrado. A legenda só deixa ler a menção a Frozen dict e a um Frozen sete [provável: frozenset] (0:01:06; 0:01:16), sem trecho reconstruível.

Citações (paráfrases de legenda, não verificadas):
- [0:00:06] Qual é a pior coisa que você pode fazer com o código é não botar para rodar porque a primeira nunca é boa
- [0:00:19] ficou super expressivo super elegante Eu gostei muito do resultado final
- [0:01:24] não foi foi interação lapidando

### Aula 2: Qual a importância em ter um código que permite ser mudado de forma fácil?
Vídeo: https://www.youtube.com/watch?v=-JoBQJ6vi74 · Duração: 1:41

Resumo: o melhor que se faz hoje é o critério de qualidade possível, mas as coisas vão mudar. Por isso ele quer um código que abrace a mudança, com uma estratégia defensiva que localize o esforço para a mudança poder acontecer. Em integração de sistemas e interação com usuário há muitos stakeholders e ele não controla a interface, então o código precisa acompanhar a mudança sem casos especiais que violem o design (0:00:15 a 0:01:36).

Linha do tempo:
- [0:00:15] o nosso melhor é o critério de qualidade
- [0:00:28] um código que abrace a mudança
- [0:00:40] estratégia defensiva e encorajar a mudança
- [0:00:49] localizar o esforço para a mudança acontecer
- [0:01:09] contexto de integração de sistemas, usuário e muitos stakeholders
- [0:01:28] não comprar mudança criando casos especiais que violem o design

Princípios:
- Código que abraça a mudança, com esforço de mudança localizado (0:00:28 a 0:00:53).
- Mudança não vira caso especial: ela deve ser absorvida pelo design (0:01:28 a 0:01:33).

Código: nenhum.

Citações (paráfrases de legenda, não verificadas):
- [0:00:28] eu preciso fazer um código que Abraça a mudança
- [0:00:49] localiza o esforço para que a mudança possa acontecer
- [0:01:28] eu não quero comprar mudança criando caso especiais que violem o design

### Aula 3: Até o código funcionar, tudo que você tem são hipóteses
Vídeo: https://www.youtube.com/watch?v=zONQiYhvD0M · Duração: 2:12

Resumo: comentando uma discussão sobre banco de dados e premissas erradas, ele diz que ninguém pode achar que sabe algo até o código funcionar, porque tudo antes disso é hipótese. Toda técnica boa existe para permitir o ciclo de feedback. Atender premissas de uma planilha pode inflar escopo não previsto, e escopo não previsto se paga; desenvolver software é um processo vivo de aprendizado (0:00:03 a 0:02:09).

Linha do tempo:
- [0:00:03] discussão sobre banco de dados e premissas erradas; alguém confiante demais
- [0:00:33] não dá para achar que sabe até o código funcionar
- [0:00:51] técnicas existem para permitir o ciclo de feedback
- [0:01:09] ver o código funcionando derruba premissas
- [0:01:29] se preocupar com a planilha trouxe escopo não previsto
- [0:01:58] como a obra de casa, o cliente muda no meio; o desenvolvimento é aprendizado

Princípios:
- Antes de funcionar, tudo é hipótese (0:00:33 a 0:00:45).
- Técnicas servem ao ciclo de feedback (0:00:48 a 0:00:56).
- Escopo imprevisto é pago por alguém (0:01:33 a 0:01:37).

Código: nenhum.

Citações (paráfrases de legenda, não verificadas):
- [0:00:33] não dá para você achar que sabe nada sobre hipótese até o código funcionar e você vê a coisa acontecendo
- [0:00:48] toda técnica todos os as estratégias das em sua relação com você permitir o ciclo de feedback [legenda confusa]
- [0:01:35] quando você imprimir escova que não está previsto você paga [provável: quando você imprime escopo que não está previsto]

### Aula 4: Importância da modelagem através dos testes
Vídeo: https://www.youtube.com/watch?v=AFCVyIrQe50 · Duração: 6:59

Resumo: parte inicial (até cerca de 0:02:50) soa como relato de um participante de um exercício de equipe com camisetas (preço, marca, tamanho); a atribuição é inferência. O relato fala de limite de tempo (uns sete dias, umas duas horas por semana) e de começar pelo teste e por uma lista em memória, não pelo modelo. Em seguida ele reforça: modelar a lógica de negócio com objetos simples, sem se preocupar com o banco, e só depois trocar por modelos; começar pelo banco é olhar o estado, e o que importa são as transições. A aula fecha com um alerta contra trabalhar de graça para impressionar cliente (0:00:16 a 0:06:35).

Linha do tempo:
- [0:00:16] exercício com camisetas (preço, marca, tamanho) e imaginação que cresce
- [0:00:46] o teste tem tempo limitado, sobra umas duas horinhas na semana
- [0:01:58] lição: não começar pelos modelos
- [0:02:29] teste antes do código; lista em memória guarda os recursos
- [0:03:15] ele: modelar lógica de negócio com objetos simples, banco depois
- [0:03:41] estados e transições; começar pelo banco é olhar para o estado
- [0:06:06] não trabalhar de graça para impressionar

Princípios:
- Modelar o negócio com objetos simples, adiar a persistência (0:03:15 a 0:03:30).
- Teste primeiro, combinado ao foco na camada de serviço (0:03:32 a 0:03:37).
- Pensar em transições entre estados, não só em estado (0:03:41 a 0:04:15).
- Camadas com contrato estável: mexer no armazenamento sem tocar a regra de negócio (0:04:45 a 0:05:31).
- Cobrar pelo trabalho: trabalhar de graça financia o cliente com tempo da sua família e de estudo (0:06:20 a 0:06:35).

Código: nenhum legível (menção a uma lista em memória no lugar do banco, 0:02:41 a 0:02:47).

Citações (paráfrases de legenda, não verificadas):
- [0:02:29] então eu teste antes do código e já para dar uma direcionar nossos pensamentos
- [0:03:15] na hora que você modela lógica de negócio com objetos partes simples [provável: objetos simples]
- [0:03:54] começar um projeto de hangu [leitura incerta] pelo banco de dados é olhar para o estado

### Aula 5: O poder da iniciativa
Vídeo: https://www.youtube.com/watch?v=nNEhaU8vqL0 · Duração: 3:48

Resumo: um participante relata que perdeu o medo de incomodar colegas, gostou do ambiente de troca e de marcarem horários fixos para o exercício, mesmo sem acreditar que alguém apareceria (0:00:00 a 0:01:38; atribuição inferida). Depois vem a fala dele: o que gera liderança é presença, aparecer no horário combinado mesmo sozinho; os outros passam a temer perder algo; e isso é decisão, não personalidade nem temperamento (0:02:09 a 0:03:35).

Linha do tempo:
- [0:00:00] relato: perder o medo de incomodar colegas
- [0:00:34] Open Space considerado fantástico
- [0:01:20] definir horários fixos para o exercício
- [0:01:42] ele cita o filme Dança com Lobo [provável: Dança com Lobos]
- [0:02:09] o que gera liderança é presença
- [0:03:31] não é personalidade nem temperamento, é decisão

Princípios:
- Presença gera liderança, mesmo sozinho no horário (0:02:09 a 0:02:21).
- Marcar e comparecer é decisão, não temperamento (0:03:31 a 0:03:37).

Código: nenhum.

Citações (paráfrases de legenda, não verificadas):
- [0:02:09] o que que gera liderança é presença presença motivo liderança
- [0:02:35] os outros vão ficar com receio de estar perdendo algo muito importante por não estarem presentes
- [0:03:31] isso não tem a ver com personalidades no telefone temperamento isso é decisão [legenda confusa]

### Aula 6: Registrar trabalho é materializar conhecimento
Vídeo: https://www.youtube.com/watch?v=rE6O-Bd7klU · Duração: 1:42

Resumo: ele propõe fazer uma síntese do que foi desenvolvido nas horas de encontro e registrar as decisões. Memória não é um HD, é relacional, então reservar cinco ou dez minutos antes do fim para registrar em conjunto, consultar depois e dar visibilidade ao trabalho, algo crucial para quem trabalha remoto (0:00:00 a 0:01:37).

Linha do tempo:
- [0:00:00] registrar o trabalho como último passo
- [0:00:29] sem registro você não vai lembrar
- [0:00:36] memória relacional, não HD
- [0:00:42] reservar 5 a 10 minutos antes do fim
- [0:01:04] materializar o trabalho feito, dar visibilidade
- [0:01:28] em remoto, quem fica quieto no canto deixa de existir

Princípios:
- Registrar na hora, com tempo reservado, para consultar depois (0:00:42 a 0:00:56).
- Visibilidade do trabalho, sobretudo no remoto (0:01:22 a 0:01:37).

Código: nenhum.

Citações (paráfrases de legenda, não verificadas):
- [0:00:31] a memória não é um HD agora ele é relacional relaciona afeto
- [0:00:53] registrar na hora é muito importante porque você pode consulta depois
- [0:01:33] remoto meu irmão e fica quietinho no canto ali negócio você não existe mais

### Aula 7: Desenrolo usando testes
Vídeo: https://www.youtube.com/watch?v=5HR5TVa9-9A · Duração: 2:44

Resumo: relato (provavelmente de um participante, pois cita Henrique em terceira pessoa em 0:00:33) de que colocar testes em desafios técnicos rendeu feedback positivo de entrevistadores. Começa com um assert no arquivo, um teste de pobre, e vai completando a função até passar; prefere desenvolver junto ao teste para não ficar trocando de arquivo. Quando o enunciado já trazia teste, foi desenrolando a solução com o entrevistador e acrescentando testes; no fim os testes salvaram (0:00:09 a 0:02:37).

Linha do tempo:
- [0:00:09] feedback positivo por ter colocado testes nos desafios
- [0:00:33] a dica do Henrique: começar com asserts
- [0:00:51] bota o assert e vai completando a função
- [0:01:23] desenvolve em cima do mesmo teste, sem trocar de arquivo
- [0:02:09] o enunciado já trazia um teste para executar
- [0:02:37] os testes passaram e salvaram

Princípios:
- Escrever o teste mais simples primeiro e completar a função até passar (0:00:51 a 0:01:07).
- Manter teste e solução juntos para reduzir custo de navegação (0:01:23 a 0:01:52).

Código: nenhum legível; ele descreve asserts no começo do arquivo (0:00:51; 0:00:59 a 0:01:04).

Citações (paráfrases de legenda, não verificadas):
- [0:00:56] cheio de cobre teste de pobre assim não tem freio [leitura incerta]
- [0:01:23] eu começo a desenvolver uma em cima no mesmo teste
- [0:02:37] Caraca me salvou

### Aula 8: A documentação do seu código é o teste
Vídeo: https://www.youtube.com/watch?v=054kEleJWQc · Duração: 1:20

Resumo: a legenda traz a ideia de que, se a pessoa vai mexer no código e não sabe o que deve fazer, o teste e a documentação devem dizer a próxima funcionalidade (0:00:00 a 0:00:24, legível só em parte). A parte clara é outra: o que se quis fazer no começo do projeto vai ser completamente alterado à revelia, e supor que o projeto tem uma diretriz fixa não funciona na vida real (0:00:41 a 0:00:57). A frase do título não aparece na legenda legível.

Linha do tempo:
- [0:00:00] melhorar a documentação, não só o código
- [0:00:14] como a pessoa saberá a próxima funcionalidade se o teste não diz
- [0:00:41] o planejado no início vai ser alterado à revelia
- [0:00:50] projeto com diretriz fixa não funciona na vida real

Princípios:
- Planos de projeto mudam à revelia; diretriz fixa é ilusão (0:00:41 a 0:00:57).

Código: nenhum.

Citações (paráfrases de legenda, não verificadas):
- [0:00:45] o que você quis fazer quando você começou o projeto vai ser completamente alterado a sua revelia
- [0:00:50] esse pressuposto de que o projeto tem uma diretriz isso é coisa de militar
- [0:00:55] Malandro na vida real não funciona não

### Aula 9: Programador gosta muito de abaixar a cabeça e fazer
Vídeo: https://www.youtube.com/watch?v=_J6wOaspVHs · Duração: 0:59

Resumo: o programador gosta de baixar a cabeça e fazer sem desenvolver sensibilidade. Ele conta que depois de dez horas travado, parou para almoçar e tomar banho e resolveu o problema em poucos minutos. Defende alternar foco e desfoco (convergência e divergência) e polinizar conversando com outras pessoas, habilidade imprescindível numa empresa (0:00:09 a 0:00:54).

Linha do tempo:
- [0:00:09] programador baixa a cabeça e faz
- [0:00:20] dez horas num problema, parou, almoçou, banho, resolveu em minutos
- [0:00:39] saber focar e desfocar, convergência e divergência
- [0:00:46] polinizar, conversar com outras pessoas

Princípios:
- Alternar foco e desfoco (0:00:39 a 0:00:46).
- Polinizar ideias com outras pessoas (0:00:46 a 0:00:54).

Código: nenhum.

Citações (paráfrases de legenda, não verificadas):
- [0:00:09] programador gosta muito de baixar a cabeça fazer fazer fazer fazer
- [0:00:39] você saber que focar e somente desfocar a convergência divergência você polinizar [legenda confusa]
- [0:00:48] isso é uma habilidade imprescindível numa empresa

### Aula 10: Se você não tem tempo para fazer bem feito, quando você vai arranjar tempo para refazer?
Vídeo: https://www.youtube.com/watch?v=bM9yJUYIUBA · Duração: 1:52

Resumo: a dificuldade de escrever teste vem de saber o que se quer sem saber expressar; é normal e exige ganhar repertório. Teste dói porque revela o que você não sabe, e fazer teste primeiro obriga um design diferente: pode demorar quatro ou cinco vezes mais, mas é ele que mostra os limites das camadas. Todo código muda, e o teste exige código passível de mudança; ele fecha com a frase do título (0:00:03 a 0:01:50).

Linha do tempo:
- [0:00:03] dificuldade de escrever teste: saber o que quer e não saber expressar
- [0:00:26] ganhar repertório; forçar a barra
- [0:00:34] teste dói porque revela o que você não sabe
- [0:00:44] teste primeiro obriga outro design de código
- [0:00:53] pode demorar quatro ou cinco vezes mais, mas mostra limites das camadas
- [0:01:32] o teste exige código passível de mudança
- [0:01:42] frase do título

Princípios:
- Dificuldade de teste revela lacuna de conhecimento (0:00:34 a 0:00:38).
- Teste primeiro muda o design e esclarece camadas, mesmo custando mais tempo (0:00:44 a 0:01:07).
- Teste força código mutável (0:01:32 a 0:01:37).

Código: nenhum.

Citações (paráfrases de legenda, não verificadas):
- [0:00:34] teste dói para fazer porque ele revela tudo que você não sabe
- [0:00:53] a gente demorar o quatro cinco vezes mais para fazer alguma coisa [legenda confusa no resto]
- [0:01:44] se você não tem tempo para fazer bem feito quando você vai arrumar tempo para fazer de novo

### Aula 11: Em software é muito mais caro fazer a coisa errada
Vídeo: https://www.youtube.com/watch?v=0tyBbgqUfvo · Duração: 3:46

Resumo: um participante diz que concorda em fazer o mínimo de ponta a ponta em vez do ótimo de pequenas partes, mas sente dificuldade na prática (0:00:00 a 0:00:20; atribuição inferida). Ele responde com disciplina e hábito, como tocar violão, e sugere pomodoro em conjunto com ritual. Desacelerar programando com testes é contraintuitivo, mas fazer a coisa errada é muito mais caro do que não fazer nada, e a coisa errada não é código feio, é gastar energia no problema errado. Com testes bem armados, o código importa menos e o encaixe que reduz acoplamento aparece (0:00:21 a 0:03:43).

Linha do tempo:
- [0:00:00] mínimo ponta a ponta em vez do ótimo em pequenas partes
- [0:00:21] disciplina, como tocar violão
- [0:01:16] pomodoro em conjunto com ritual
- [0:01:42] desacelerar com testes é contraintuitivo
- [0:01:54] fazer a coisa errada é mais caro que não fazer nada
- [0:02:07] a coisa errada é o problema errado, não o código feio
- [0:03:07] testes bem armados; encaixe que reduz acoplamento

Princípios:
- Mais caro fazer a coisa errada do que nada (0:01:54 a 0:02:05).
- Errado é problema errado, falha de percepção de valor, não código feio (0:02:07 a 0:02:22).
- Teste bem armado deixa o código evoluir para reduzir acoplamento e permitir mudança (0:03:07 a 0:03:43).

Código: nenhum.

Citações (paráfrases de legenda, não verificadas):
- [0:01:44] é contraintuitivo programa com o teste porque fazer rápido [frase incompleta na legenda]
- [0:01:54] é muito mais caro fazer a coisa errada do que não fazer nada
- [0:03:38] tu vai encontrando Qual é o encaixe do seu código que reduza o acoplamento e permita a mudança

### Aula 12: Toda nova habilidade que se desenvolve, não pode ter compromisso com resultado
Vídeo: https://www.youtube.com/watch?v=f3_KKOwrL38 · Duração: 1:11

Resumo: ao aprender algo novo não se pode ter compromisso com o resultado, só com o processo. Aprender tecnologia nova no trabalho é conflito de interesse, porque o trabalho garante resultado e a tecnologia nova não; os riscos devem ser assumidos junto com a outra parte. Ele fecha lembrando que não se trabalha como louco e que é preciso tempo para si, família e estudo (0:00:00 a 0:01:07).

Linha do tempo:
- [0:00:00] nova habilidade sem compromisso com resultado
- [0:00:16] conflito de interesse ao aprender tecnologia nova no trabalho
- [0:00:37] risco assumido pelas duas partes
- [0:00:56] aventura de aprendizagem com a outra parte ciente
- [0:00:58] tempo para família, descanso e estudo

Princípios:
- Aprender novo exige separar processo de resultado (0:00:00 a 0:00:06).
- Combinar o risco de aprendizagem com a outra parte (0:00:37 a 0:00:58).
- Limitar a jornada para ter tempo de descanso e estudo (0:00:58 a 0:01:07).

Código: nenhum.

Citações (paráfrases de legenda, não verificadas):
- [0:00:00] em toda nova habilidade que se você não pode ter compromisso com o resultado
- [0:00:16] programadores aprender uma tecnologia nova nosso trabalho é um conflito de interesse
- [0:01:00] não dá para trabalhar que nem um doido Tem que ter tempo para você e para tua família

### Aula 13: Faz funcionar, depois melhora
Vídeo: https://www.youtube.com/watch?v=h5f5PvzWZW0 · Duração: 3:51

Resumo: o objetivo é fazer alguma coisa, não terminar algo completo. Com duas horas por semana em quatro semanas, são oito horas, e um escopo completo não cabe. A estratégia é fazer de ponta a ponta o essencial, pegar o mais fácil e tratar o tempo como restrição; a sensibilidade para isso vem com cultura e prática, não é regra. A versão que funciona vale mais do que a genérica e bonita (0:00:09 a 0:02:54).

Linha do tempo:
- [0:00:03] vão apresentar uma meia implementação
- [0:00:09] o objetivo é alguma coisa ser feita, não terminar completa
- [0:00:20] duas horas por semana em quatro semanas, oito horas
- [0:01:35] fazer ponta a ponta com o banco, por exemplo
- [0:02:04] o tempo é uma restrição; pegar o mais fácil
- [0:02:27] funcionando de ponta a ponta, genérico e bonito não importa
- [0:02:51] um teste atesta que funciona

Princípios:
- Ponta a ponta antes de genérico e bonito (0:02:27 a 0:02:35).
- Tempo como restrição de escopo (0:02:04 a 0:02:11).
- Estratégia de risco é cultura e comportamento, vem com o tempo (0:02:11 a 0:02:21).

Código: nenhum legível.

Citações (paráfrases de legenda, não verificadas):
- [0:00:09] o objetivo maior é alguma coisa ser feita e não terminar alguma coisa completa
- [0:02:27] faz de ponta a ponta não importa essa genérico que tá bonito
- [0:02:51] tem um teste que dá atestado funciona

### Aula 14: Quanto mais bagagem a gente tem, mais a gente vê o Big steps e não o baby steps
Vídeo: https://www.youtube.com/watch?v=LGqP3C7463U · Duração: 3:27

Resumo: discussão de planejamento de um exercício em que o cliente fornece uma planilha. Ele sugere entregar o núcleo e a heurística primeiro, sem dependências pesadas como pandas, e valida o que o cliente reconhece como valor. A parte pedagógica é o ponto: quem tem mais bagagem enxerga big steps em vez de baby steps, e iniciantes podem ficar para trás ou virar o malandrão que resolve sozinho (0:00:33 a 0:03:25).

Linha do tempo:
- [0:00:30] cada um querendo fazer uma coisa; combinar horário
- [0:00:57] chegar ao cliente e pedir a planilha dele
- [0:02:03] qualquer coisa do meio do caminho não mostra valor
- [0:02:18] quer só o núcleo, só heurística
- [0:02:53] mais bagagem, mais big steps e menos baby steps
- [0:03:01] parte pedagógica: quem está começando precisa caminhar junto

Princípios:
- Começar pelo núcleo e pela heurística, não por dependências (0:02:18 a 0:02:27).
- Bagagem faz esquecer os baby steps; o processo precisa considerar quem está começando (0:02:53 a 0:03:13).

Código: nenhum.

Citações (paráfrases de legenda, não verificadas):
- [0:02:18] eu quero só o núcleo só heurística validar [legenda cortada]
- [0:02:53] quanto mais bagagem a gente tem mais a gente vê o Big step não besta [provável: baby steps]
- [0:03:01] tem uma parte pedagógica aqui do nosso do nosso processo tem que caminhar junto

### Aula 15: Tudo que achamos sobre a solução do problema é uma mera hipótese
Vídeo: https://www.youtube.com/watch?v=USIPY7IrYpo · Duração: 6:13

Resumo: parte de um caso de royalties de músicas, com três entradas (contrato, direitos dos proprietários e dados da música com percentual) e uma estrutura de dados como saída (0:00:05 a 0:00:20). Ele recomenda começar com uma música, depois duas e três, aumentando a complexidade da heurística, e avisa que usar pandas cedo dá tiro no pé. Não se gasta energia preparando um futuro que ainda não chegou, e tudo que se acha sobre a solução é hipótese até o código rodar. Fecha com histórias de over-engineering em equipes pequenas (0:01:08 a 0:05:41).

Linha do tempo:
- [0:00:05] três entradas e uma estrutura de dados como saída
- [0:01:08] uma música, depois duas, três: aumentar a heurística
- [0:01:22] pandas cedo dá tiro no pé
- [0:02:29] não gastar energia preparando um futuro que ainda não chegou
- [0:03:38] tudo é hipótese até o código rodar vivo
- [0:04:25] experimento pequeno, barato e controlado
- [0:05:23] história de inventar um lança-foguete para resolver algo simples

Princípios:
- Crescer a complexidade a partir de casos simples (0:01:08 a 0:01:16).
- Hipótese só se confirma com código rodando (0:03:38 a 0:03:51).
- Experimento pequeno, barato e controlado (0:04:25 a 0:04:33).
- Evitar preparar o futuro que ainda não chegou (0:02:29 a 0:02:35).

Código: nenhum.

Citações (paráfrases de legenda, não verificadas):
- [0:03:40] tudo que eu acho que eu sei sobre a solução do problema é uma mera hipótese e só Ser aprovada quando o código estiver rodando vivo na minha frente
- [0:02:29] por que que eu vou gastar energia preparando um futuro que ainda não chegou
- [0:04:27] observa edos primos ferimento pequeno barato e controlado [provável: experimento] que te deu um passo na direção

### Aula 16: Os 20% que entregam 80%
Vídeo: https://www.youtube.com/watch?v=HpzLoui9N-o · Duração: 1:43

Resumo: ele pergunta em que momento se está: explorar ou afunilar. Enquanto não há caso de sucesso rodando, adicionar coisas aumenta os riscos de entrega ao cliente. O segredo é um escopo mínimo [leitura incerta: a legenda diz mingau] que dê os vinte por cento de entrega do resultado. Ilustra com o primeiro commit de um projeto grande (Doc [leitura incerta], provável Docker), que já funcionava com uma gambiarra (0:00:02 a 0:01:41).

Linha do tempo:
- [0:00:04] exploração ou afunilamento
- [0:00:17] sem caso de sucesso, não há o que melhorar
- [0:00:33] fazer mais antes do sucesso aumenta o risco de entrega
- [0:00:48] segredo é um escopo mínimo que dê 20 por cento de entrega
- [0:01:12] histórico de desenvolvimento do Doc [leitura incerta]
- [0:01:35] o exemplo precisa motivar investimento

Princípios:
- Primeiro o caso de sucesso rodando, depois melhorar (0:00:17 a 0:00:33).
- Escopo mínimo que entrega o essencial (0:00:48 a 0:00:56).

Código: nenhum.

Citações (paráfrases de legenda, não verificadas):
- [0:00:17] enquanto eu não tenho caso de sucesso que acontece a maior parte dos casos [legenda confusa]
- [0:00:50] o nosso segredo é que é um mingau [leitura incerta] escopo para conseguir pegar aqui assim Vinte por cento de entrega
- [0:01:35] o exame [provável: exemplo] tem que ter o que motiva investimento e a gente constrói a partir dele

### Aula 17: Português é a linguagem mais importante do programador saber
Vídeo: https://www.youtube.com/watch?v=YeiJV33QFAw · Duração: 3:21

Resumo: ele pergunta qual é a principal dor do cliente (dividir o dinheiro de uma música entre autores, em grande volume) e recomenda, para ganhar clareza nos requisitos, escrever frases curtas, uma única oração, em vez de parágrafos cheios de vírgulas. O desafio é transformar o problema em proposições lógicas. Depois descreve mudar o modo da pesquisa, de vizinhança para profundidade, com a imagem do guarda-chuva e a raiz da árvore, e a ideia de achar a mina de ouro do cliente (0:00:10 a 0:03:16).

Linha do tempo:
- [0:00:10] principal dor do cliente: dividir o que recebe de uma música entre autores
- [0:00:47] dica: frases curtas, uma única oração
- [0:01:10] parágrafo cheio de vírgulas é sinal de problema mal entendido
- [0:01:26] transformar o problema em proposições lógicas
- [0:01:51] português é a linguagem de programação mais importante
- [0:02:10] mudar o modo da pesquisa, de vizinhança para profundidade
- [0:03:01] achar a mina de ouro do cliente

Princípios:
- Escrever requisito em frases curtas de uma oração (0:00:47 a 0:00:55).
- Português é a linguagem mais importante do programador (0:01:51 a 0:01:55).
- Ter consciência do modo de pesquisa do problema, abrangente ou profundo (0:02:10 a 0:02:55).

Código: nenhum.

Citações (paráfrases de legenda, não verificadas):
- [0:00:47] dica dica para ter clareza e requisito de projeto e você entender e os Storm frases curtas [legenda confusa]
- [0:01:32] cada autor pode ter uma porcentagem diferente do direito da música
- [0:01:51] o português é linguagem programação mais importante do programa [provável: programador]

### Aula 18: Existe alguma regra para identificar o código que precisa ser testado?
Vídeo: https://www.youtube.com/watch?v=l6LUoEIRP0U · Duração: 4:38

Resumo: a resposta curta é que não há regra, há bom senso que vem com a experiência. Ele vê o código como uma árvore de execução com vários caminhos, prefere código plano e linear, e observa quem depende de quê. Uma função chamada em muitos lugares precisa ter comportamento previsível, e o teste ajuda nisso. A unidade de teste é dinâmica e cresce conforme o código cresce. Com TDD se define o resultado esperado e se refatora conforme surge necessidade, processo orgânico. Fecha defendendo TDD como treino de ética e estética, promovido por ele desde 2010 (0:00:08 a 0:04:35).

Linha do tempo:
- [0:00:08] não há regra, há bom senso da experiência
- [0:00:25] código como árvore de execução com vários caminhos
- [0:00:54] gosta de código plano e linear
- [0:01:24] função chamada em vários lugares precisa de comportamento previsível
- [0:02:23] a unidade de teste é dinâmica
- [0:02:45] com TDD define o resultado esperado e vai refatorando
- [0:04:08] TDD como treino de ética e estética

Princípios:
- Sem regra fixa, bom senso treinado (0:00:13 a 0:00:19).
- Mais dependentes significam mais necessidade de previsibilidade e de teste (0:01:24 a 0:01:48).
- Unidade de teste cresce com o código (0:02:23 a 0:02:35).
- TDD faz o código evoluir organicamente com o que é necessário (0:03:03 a 0:03:09).

Código: nenhum.

Citações (paráfrases de legenda, não verificadas):
- [0:00:13] não tem uma regra mas existe um bom senso que você vai adquirindo com a experiência
- [0:00:57] para mim o código linha reta perfeito seria o código mais bonito [legenda: mais bonitos]
- [0:04:29] 11 anos promovendo essa técnica maravilhosa que aumenta a capacidade do programador fazer a coisa certa

### Aula 19: O que fazer quando aparece um projeto que eu não domino a linguagem?

Vídeo: https://www.youtube.com/watch?v=_3mbgocpWUM · Duração: 5:13

Resumo: ele responde que a linguagem é só um dos fatores do projeto e que o que importa é observar a variabilidade, isto é, a distância entre a necessidade do projeto e a bagagem de quem vai fazê-lo (0:00:26 a 0:00:42). Essa análise mostra o risco de fracasso (0:00:43 a 0:00:51). A pergunta passa a ser se o projeto comporta o aprendizado, o que se negocia com prazo e cliente (0:02:11 a 0:02:31). Ele alerta para programar com sotaque de outra linguagem (0:04:13 a 0:04:44) e fecha dizendo que o risco nunca some, mas deve ser ponderado (0:05:07).

Linha do tempo:
- [0:00:00] a pergunta: pinta um projeto numa linguagem que eu não domino.
- [0:00:26] a importância de observar a variabilidade do projeto.
- [0:00:44] exemplo: empresa de Python com Django compra outra com sistema em Rails.
- [0:02:09] o projeto contempla o seu aprendizado? A urgência inviabiliza?
- [0:02:43] ponderar se pegar qualquer projeto é bom economicamente (reaproveitamento de bagagem).
- [0:04:13] programação com sotaque de outra linguagem.
- [0:04:47] abordagem: analisar risco e contexto, mapear o que sei e o que não sei.

Princípios:
- A variabilidade do projeto em relação à sua bagagem estima o risco de fracasso (0:00:32 a 0:00:47).
- Aprender dentro do projeto tem de ser negociado (0:02:09 a 0:02:31).
- Reaproveitamento de bagagem é referencial econômico e permite ser mais eficiente e cobrar mais (0:03:21 a 0:03:33).
- Cuidado com a generalização de que programador programa qualquer coisa; o resultado é código com sotaque, que reduz a qualidade (0:03:52 a 0:04:44).

Código: não há código mostrado.

Citações (paráfrases de legenda, não verificadas):
- o que eu quero transmitir é a importância de observar a variabilidade do projeto (aula 19, 0:00:26).
- esse tipo de análise da variabilidade vai mostrar o risco do projeto, o risco de fracasso (aula 19, 0:00:40 a 0:00:51).
- isso é programação com sotaque, tem sotaque de Java no código [legenda: Java e pai para Python] (aula 19, 0:04:13 a 0:04:23).

### Aula 20: Como usar o tratamento de exceção de forma certa?

Vídeo: https://www.youtube.com/watch?v=VwUDRZxDWV8 · Duração: 2:58

Resumo: ele parte da origem do recurso: antes, as operações devolviam código de sucesso ou de erro e o código ficava cheio de ifs para os casos de falha (0:00:22 a 0:00:48). Com exceções, o código fica mais linear, executa o caso de sucesso e permite recuperar a execução quando algo excepcional acontece (0:00:50 a 0:01:11). A regra central é ser absolutamente específico na exceção tratada, porque existe uma hierarquia e pegar a exceção base captura tudo (0:01:13 a 0:01:47). Ele também pede para diminuir o corpo do bloco de tratamento (0:01:57 a 0:02:11).

Linha do tempo:
- [0:00:00] a pergunta e o cuidado de não coletar todas as exceções do universo.
- [0:00:22] origem: códigos de erro que o chamador precisava conhecer de antemão.
- [0:00:50] exceções reduzem os ifs e deixam o código linear.
- [0:01:13] ser absolutamente específico na exceção tratada.
- [0:01:57] diminuir o corpo do bloco protegido.
- [0:02:44] indica a aula do curso de Python (Pythonando, segundo a legenda) sobre modelagem mental de objetos e tratamento de exceção.

Princípios:
- Tratar a exceção mais específica possível, nunca a base, porque a hierarquia faz o filho se identificar com o pai (0:01:13 a 0:01:47).
- Quem trata é o chamador, que precisa saber as ações possíveis daquele código (0:01:47 a 0:01:57).
- Bloco de tratamento pequeno, senão passam a existir vários blocos e o trabalho fica complexo (0:01:57 a 0:02:13).
- O resultado é reduzir caminhos no código e evitar um estouro de pilha (0:02:24 a 0:02:43).

Código: não há código mostrado; ele cita o padrão de pegar a exceção base (0:01:20), sem soletrar nome de classe na legenda [legenda: base deck 7].

Citações (paráfrases de legenda, não verificadas):
- com exceções você reduz a quantidade de ifs no seu código criando um código mais linear (aula 20, 0:00:53 a 0:01:02).
- é muito importante você ser muito específico, porque existe uma hierarquia de exceções (aula 20, 0:01:29 a 0:01:37).
- se você bota muita lógica dentro, muitas coisas podem acontecer (aula 20, 0:02:03 a 0:02:09).

### Aula 21: Qual sua opinião sobre Python não ter controle de acesso a métodos e atributos de um objeto?

Vídeo: https://www.youtube.com/watch?v=c-tk20yz0-A · Duração: 3:56

Resumo: ele separa duas coisas que as pessoas confundem: controle de acesso (público, privado, protegido) e encapsulamento (0:00:11 a 0:00:34). Encapsulamento é um conceito à parte, praticável sem esses modificadores. Sobre o controle de acesso, ele não vê problema em Python não ter e explica a origem histórica: nos anos 90 vendiam-se componentes binários sem código-fonte e era preciso restringir o que o cliente podia fazer (0:00:56 a 0:01:56). A web mudou esse cenário porque virou a interface comum e favoreceu linguagens dinâmicas (0:02:03 a 0:03:10). Ele não usa público, privado e protegido por achar burocracia demais.

Linha do tempo:
- [0:00:00] a pergunta e a separação em duas coisas.
- [0:00:20] encapsulamento é conceito à parte.
- [0:00:56] origem histórica: anos 90, Java, componentes binários, DLLs.
- [0:02:03] a internet muda o cenário: a interface comum passa a ser a web.
- [0:03:29] ele não usa o controle de acesso; burocracia demais.
- [0:03:44] cuidado com gente contornando uma decisão de design que fechou parte do código.

Princípios:
- Não confundir falta de modificadores de acesso com falta de encapsulamento (0:00:20 a 0:00:34, 0:03:47).
- O controle de acesso tem origem histórica na venda de componentes sem código-fonte (0:01:01 a 0:01:56).
- Fechar um pedaço do código por design leva outros a gastar esforço para contornar (0:03:35 a 0:03:47).

Código: não há código mostrado.

Citações (paráfrases de legenda, não verificadas):
- não tem encapsulamento porque não tem público, privado, protegido, e não é verdade, encapsulamento é um conceito à parte (aula 21, 0:00:22 a 0:00:30).
- eu não vejo nenhum problema com isso, é uma burocracia muitas vezes necessária mas que tem a sua origem histórica (aula 21, 0:00:46 a 0:00:54).
- eu já vi gente dando muito jeito para contornar uma decisão prévia de design de fechar um pedaço do código [legenda confusa neste trecho] (aula 21, 0:03:35 a 0:03:42).

### Aula 22: Como trabalhar com migrações em desenvolvimento e produção no Django?

Vídeo: https://www.youtube.com/watch?v=ncm6JHGzSQA · Duração: 3:27

Resumo: ele pede para pensar o código e o controle de versão como um processo evolutivo e para tratar esquema e estado do banco como parte do código (0:00:28 a 0:00:53). Migração é a ferramenta que transforma o estado do banco para alinhar a versão do código com o formato do banco que ele espera (0:01:04 a 0:01:24). Quando se desalinha, as pessoas criam scripts de inicialização e atualização, o que aumenta o gap entre versões (0:01:24 a 0:01:53). O que ele faz: gera a migração antes do commit, junto com o código, e usa uma ferramenta própria para rodar testes sem migrações (0:02:57 a 0:03:23).

Linha do tempo:
- [0:00:00] a pergunta.
- [0:00:28] código e versionamento como processo evolutivo.
- [0:00:42] esquema e estado do banco fazem parte do código.
- [0:01:04] migração como mutação: alinha a versão do código com a do banco.
- [0:01:24] scripts de inicialização e atualização aumentam o gap.
- [0:02:32] desenvolver só com syncdb gera um gap grande depois.
- [0:02:57] prática: gerar a migração antes do commit, casada com o código.

Princípios:
- Tratar o esquema e o estado do banco como parte integrante do código (0:00:42 a 0:00:53).
- Migração alinha a versão do código com a versão do banco (0:01:08 a 0:01:24).
- Antes da release dá para simplificar mutações desnecessárias, mas isso é preocupação secundária (0:01:58 a 0:02:21).
- Gerar a migração junto com o código, no mesmo commit, não depois (0:03:10 a 0:03:23).

Código: não há código mostrado. Ele menciona uma ferramenta chamada [legenda: Jungle Test Without Migrations] para rodar testes sem migrações (0:02:57 a 0:03:06); o nome exato da ferramenta é leitura, não confirmado.

Citações (paráfrases de legenda, não verificadas):
- o ideal é pensar no código e principalmente no controle de versão como um processo evolutivo (aula 22, 0:00:28 a 0:00:37).
- a migração é uma ferramenta para gerar uma transformação no estado do banco de dados (aula 22, 0:01:08 a 0:01:13).
- eu não faço isso depois, eu faço isso combinado, casadinho (aula 22, 0:03:19 a 0:03:23).

### Aula 23: O que fazer para que um sistema em Django não saia do ar com muitos acessos?

Vídeo: https://www.youtube.com/watch?v=wLnAT6Nh1_o · Duração: 2:42

Resumo: ele descreve o erro comum de jogar tudo nas costas do framework, inclusive arquivos estáticos e queries sem critério (0:00:06 a 0:00:32). Desde o começo é preciso ter noção do perfil de uso do sistema: natureza, comportamento no tempo e relação com os usuários, com sazonalidade e picos (0:00:32 a 0:01:07). Escalar é usar os recursos computacionais de forma eficiente: cache, CDN, índices, Redis para sessão (0:01:07 a 0:01:51). Servir arquivo estático por Python é caro (0:01:55 a 0:02:10). A arquitetura não é só a ferramenta (0:02:25 a 0:02:35).

Linha do tempo:
- [0:00:06] o padrão de jogar tudo no framework.
- [0:00:32] conhecer o perfil de uso do sistema.
- [0:00:42] exemplo: sistema de evento tem picos na inscrição.
- [0:01:12] escalar é usar bem os recursos computacionais.
- [0:01:19] cache do que é público, CDN, índice do banco, Redis para sessão.
- [0:02:14] outra fronteira: infraestrutura e máquinas na nuvem.

Princípios:
- Entender o perfil de uso do sistema antes de planejar a escala (0:00:32 a 0:01:07).
- Cachear o que é público e servir estáticos por CDN (0:01:19 a 0:01:27).
- Não usar uma linguagem dinâmica para servir arquivo que poderia ser lido do disco (0:01:55 a 0:02:10).
- Arquitetura vai além da ferramenta (0:02:25 a 0:02:35).

Código: não há código mostrado.

Citações (paráfrases de legenda, não verificadas):
- é muito comum a gente no começo jogar tudo nas costas do framework que você escolheu (aula 23, 0:00:00 a 0:00:12).
- desde o começo é muito importante você ter noção do perfil de uso do seu sistema (aula 23, 0:00:32 a 0:00:37).
- é muito caro usar uma coisa dinâmica, Python, Django, PHP, Java, para servir um arquivo estático (aula 23, 0:01:55 a 0:02:10).

### Aula 24: Como foi o processo de criação do Decouple?

Vídeo: https://www.youtube.com/watch?v=jV50H8STV3c · Duração: 2:29

Resumo: ele conta que o Decouple começou sem pretensão, para resolver um problema dos próprios projetos, como a maioria das suas bibliotecas (0:00:00 a 0:00:10). Importava muito a API de uso: simples e extensível (0:00:18 a 0:00:27). Comenta que o ambiente estimula o comportamento da equipe (0:00:32 a 0:00:49). A primeira versão era específica para Django; depois, um conselho de Felipe Cruz o levou a generalizar para Flask (0:01:08 a 0:01:26). Exigia também suporte a arquivo ini, por causa do servidor estilo Heroku que ele montava para os alunos (0:01:26 a 0:01:53). O desafio posterior é resistir a pedidos de inflar a biblioteca, e ele cita a lei de Zawinski (0:02:04 a 0:02:22).

Linha do tempo:
- [0:00:00] origem: um problema nos próprios projetos.
- [0:00:18] a API de uso tinha de ser simples e extensível.
- [0:00:32] o ambiente estimula o comportamento (copy and paste, classes).
- [0:01:08] publicação como Django Decoupled; sugestão de generalizar para Flask.
- [0:01:26] exigência de funcionar também com ini, por causa do servidor para os alunos.
- [0:02:04] pedidos para inflar a biblioteca e a lei de Zawinski.

Princípios:
- Bibliotecas nascem de resolver um problema próprio e bem (0:00:06 a 0:00:10).
- A API de uso deve ser simples e extensível, sem grandes complicações (0:00:18 a 0:00:27).
- O ambiente em que você está estimula certos comportamentos; ter consciência do que se tenta resolver (0:00:32 a 0:00:56).
- Resistir ao crescimento de escopo (0:02:04 a 0:02:22).

Código: não há código mostrado. Os nomes Decouple, Django Decoupled e Heriki (servidor próprio dele para os alunos, 0:01:38) vêm da legenda; a grafia de Heriki é leitura.

Citações (paráfrases de legenda, não verificadas):
- a maioria das bibliotecas que eu faço geralmente é para resolver um problema meu (aula 24, 0:00:06 a 0:00:10).
- eu estava muito preocupado com a API, a API de uso era muito importante, tinha que ser muito simples, tinha que ser extensível (aula 24, 0:00:18 a 0:00:27).
- o ambiente em que você está estimula você a se comportar daquela maneira (aula 24, 0:00:32 a 0:00:37).

### Aula 25: O que fazer para verificar um efeito colateral que não está explícito?

Vídeo: https://www.youtube.com/watch?v=Zuk3xGkdMFw · Duração: 1:47

Resumo: testar costuma ser pensar em entrada e saída (0:00:00 a 0:00:11). Quando o efeito está em um objeto passado para a função e não aparece na saída, usa-se um Mock, que finge ser o objeto e registra chamadas, valores passados e alterações (0:00:23 a 0:01:03). É útil sobretudo em integrações (0:01:09). O alerta final: usar Mock demais é sinal de código muito acoplado, com pouco espaço para teste unitário e caixa branca (0:01:16 a 0:01:27); deve ser usado com moderação (0:01:42).

Linha do tempo:
- [0:00:00] testes pensam em entrada e saída.
- [0:00:13] o problema: efeito colateral que não aparece na saída.
- [0:00:23] a função recebe um objeto e o modifica.
- [0:00:49] o Mock finge o objeto e registra o que acontece.
- [0:01:09] útil para integrações, sem abusar.
- [0:01:16] muito Mock indica código acoplado.

Princípios:
- Verificar efeito colateral com Mock que registra chamadas e valores (0:00:49 a 0:01:03).
- Não abusar de Mock: excesso é sinal de acoplamento e deixa pouco espaço para teste unitário (0:01:09 a 0:01:27).
- Se o acoplamento não é resolvido, a tendência é ficar cada vez mais complicado (0:01:27 a 0:01:42). O trecho em torno de 0:01:27 a 0:01:40 está truncado na transcrição.

Código: não há código mostrado.

Citações (paráfrases de legenda, não verificadas):
- então você usa um Mock para fingir que é esse objeto e rodar uma parte do sistema (aula 25, 0:00:49).
- usar Mock demais é sinal que você está com um código muito acoplado (aula 25, 0:01:16 a 0:01:22).
- é interessante, é bacana, mas tem que usar com moderação (aula 25, 0:01:42).

### Aula 26: O que é pensamento Pythonico?

Vídeo: https://www.youtube.com/watch?v=A4lISm_Y1DE · Duração: 3:03

Resumo: ele diz que não há resposta fácil e retoma os níveis de compreensão da programação: sintático, semântico e simbólico (0:00:13 a 0:00:44). O pensamento Pythônico vem com o tempo e com a compreensão da beleza estética e da filosofia da linguagem, o Zen do Python, que ele descreve como poesia e não manual (0:00:44 a 0:01:12). Python parece simples e é sofisticado: muito fluxo com pouco código, legível e esteticamente bonito, equilibrando forma e função (0:01:14 a 0:01:52). Existe uma cultura de não só fazer funcionar, mas fazer do jeito certo (0:02:12 a 0:02:30), e o código vira expressão de quem escreve (0:02:36 a 0:02:54).

Linha do tempo:
- [0:00:13] os níveis sintático, semântico e simbólico.
- [0:00:44] o pensamento Pythônico vem com o tempo e com a filosofia da linguagem.
- [0:00:53] o Zen do Python como poesia, não manual.
- [0:01:19] expressividade: muito com pouco código, legível e bonito.
- [0:01:52] a relação artística dele com a programação.
- [0:02:12] cultura de fazer a coisa do jeito certo.

Princípios:
- Os níveis sintático, semântico e simbólico descrevem a evolução de quem programa (0:00:18 a 0:00:40).
- Forma pythônica é equilibrar forma e função, estilo e capacidade (0:01:31 a 0:01:52).
- Na cultura Python importa não apenas funcionar, mas usar os recursos adequados, manutenção fácil e legibilidade (0:02:12 a 0:02:30).

Código: não há código mostrado.

Citações (paráfrases de legenda, não verificadas):
- o Zen do Python é uma coisa que não é um manual, é só uma poesia, mas muito expressiva (aula 26, 0:00:53 a 0:01:04).
- você consegue esculpir fluxos elaborados com muito pouco código (aula 26, 0:01:19 a 0:01:25).
- existe uma cultura nos programadores Python de não apenas fazer funcionar, mas fazer a coisa do jeito certo (aula 26, 0:02:19 a 0:02:24).

### Aula 27: Como entender o software como um organismo vivo?

Vídeo: https://www.youtube.com/watch?v=85e3U-0IpNo · Duração: 2:56

Resumo: ele conta a origem do pensamento: o desenvolvimento de software quebra, muda, atrasa e gera retrabalho (0:00:14 a 0:00:21). Em vez da metáfora industrial ou de arquitetura, usa a do médico, que mantém em funcionamento um sistema que não tem reboot nem reset (0:00:29 a 0:01:01). O software também tem gente usando e precisa melhorar sem parar (0:01:01 a 0:01:06). O programador deve entender o problema do cliente, não ser peão que executa pedidos (0:01:15 a 0:01:36), e buscar a menor mudança possível para aumentar a capacidade sem aumentar a quantidade de código (0:01:41 a 0:01:58). Não se joga o legado fora e recomeça do zero, por ser caro (0:02:19 a 0:02:23).

Linha do tempo:
- [0:00:14] por que a metáfora: o desenvolvimento quebra, muda, atrasa.
- [0:00:29] metáfora do médico em vez da industrial.
- [0:00:54] o sistema não tem reboot nem reset.
- [0:01:15] entender o problema do cliente, não só executar a tarefa.
- [0:01:41] a menor mudança possível, sem aumentar o código.
- [0:02:19] não jogar o legado fora; é caro.
- [0:02:30] em oposição a pensar software como conjunto de funcionalidades e pontos de função.

Princípios:
- Software com gente usando não tem reboot; precisa evoluir mantendo o sistema funcionando (0:00:54 a 0:01:06).
- Entender o problema do cliente antes de executar o pedido (0:01:21 a 0:01:36).
- Buscar a menor invasão que dá o resultado, aumentando a capacidade sem aumentar linearmente o código (0:01:41 a 0:01:58).
- Reescrever do zero o legado é muito caro (0:02:19 a 0:02:23).

Código: não há código mostrado.

Citações (paráfrases de legenda, não verificadas):
- o médico tem um sistema que tem de manter funcionando e não tem reboot, não tem reset (aula 27, 0:00:54 a 0:01:01).
- qual é a menor mudança que você pode fazer para aumentar a capacidade do software sem necessariamente aumentar a quantidade de código (aula 27, 0:01:49 a 0:01:58).
- não pode pegar o legado e jogar fora e começar do zero, é muito caro (aula 27, 0:02:19 a 0:02:23).

### Aula 28: Por que não devemos considerar as views do Django como controllers?

Vídeo: https://www.youtube.com/watch?v=CYExonX7yKs · Duração: 1:25

Resumo: ele diz que não proibiria a analogia, que funciona como alegoria, mas lembra que há necessidade de ser específico (0:00:08 a 0:00:20). O MVC não nasceu na web, vem de sistemas de interface desktop (0:00:24 a 0:00:35). No Django a view controla o conteúdo e o template controla a apresentação (0:00:42 a 0:00:54). Para ele o importante é separar a análise do conteúdo da forma de apresentar (0:01:08 a 0:01:16) e manter a view sempre pequenininha (0:01:18 a 0:01:23). A legenda é bastante ruidosa neste vídeo.

Linha do tempo:
- [0:00:00] a pergunta.
- [0:00:08] a analogia funciona como alegoria, mas pede especificidade.
- [0:00:24] MVC vem dos sistemas desktop, não da web.
- [0:00:42] view controla o conteúdo, template controla a apresentação.
- [0:01:18] a view deve ser sempre pequenininha.

Princípios:
- Separar o tratamento do conteúdo da apresentação (0:01:08 a 0:01:16).
- Estruturar a view para ser sempre muito pequena (0:01:18 a 0:01:23).
- Confusão com o MVC de outras ferramentas não é um problema por si (0:01:02 a 0:01:08).

Código: não há código mostrado.

Citações (paráfrases de legenda, não verificadas):
- o pessoal do Django tenta tratar a view como aquilo que controla o conteúdo e o template como aquilo que controla a apresentação (aula 28, 0:00:42 a 0:00:51).
- o importante é você separar a parte de analisar o conteúdo e apresentar de forma diferente (aula 28, 0:01:10 a 0:01:16).
- é importante estruturar a sua view para ser sempre muito pequenininha (aula 28, 0:01:18 a 0:01:23).

### Aula 29: É necessário um Web Developer aprender a tratar imagens?

Vídeo: https://www.youtube.com/watch?v=juXwimpmNOI · Duração: 2:26

Resumo: ele diz não gostar da estrutura da pergunta, porque esconde uma visão de divisão de trabalho em que cada um faz só a sua obrigação (0:00:04 a 0:00:50). Tratamento de imagem é parte clássica da computação gráfica, e quem lida com computador deveria saber como funciona (0:00:21 a 0:00:36). Ele conta que aprende o que for preciso, mesmo sem ser bom: Photoshop, edição de vídeo e redes sociais (0:00:51 a 0:01:11). Conclui que a pergunta tenta eximir responsabilidade e que quanto mais responsabilidade se assume, melhor (0:01:35 a 0:01:43), inclusive para a remuneração e para servir melhor às pessoas (0:02:13 a 0:02:23). Se o trabalho prometido foi outro, é questão de renegociar (0:01:43 a 0:02:07).

Linha do tempo:
- [0:00:04] não gosta da estrutura da pergunta.
- [0:00:21] tratamento de imagem é clássico em computação gráfica.
- [0:00:42] a pergunta esconde uma visão de divisão de trabalho.
- [0:00:51] ele aprende o que precisa, mesmo sem aptidão.
- [0:01:37] a pergunta tenta eximir responsabilidade.
- [0:01:43] se o trabalho prometido foi outro, renegociar.
- [0:02:09] ampliar a responsabilidade abre portas.

Princípios:
- Assumir mais responsabilidade é melhor do que se limitar à própria obrigação (0:01:37 a 0:01:43).
- Resolver o problema, com ética, pedindo ajuda se preciso (0:01:20 a 0:01:29).
- Se a função prometida não é a real, negocie ou procure outra (0:01:43 a 0:02:07).
- Ampliar a capacidade abre portas para melhor remuneração e para servir melhor às pessoas (0:02:09 a 0:02:23).

Código: não há código mostrado.

Citações (paráfrases de legenda, não verificadas):
- eu não gosto da estrutura da pergunta, ela esconde uma visão de divisão de trabalho em que eu só faço a minha obrigação (aula 29, 0:00:41 a 0:00:50).
- essa pergunta tenta eximir a responsabilidade, quanto mais responsabilidade você assumir, melhor (aula 29, 0:01:35 a 0:01:40).
- seja lá qual for o caminho, busque sempre ampliar a sua responsabilidade (aula 29, 0:02:07 a 0:02:13).

### Aula 30: Como lidar com mudanças no código?

Vídeo: https://www.youtube.com/watch?v=qRlDpvyRO4s · Duração: 4:01

Resumo: ele diz que código é maleável e que quem tem alguém usando o sistema sabe que ele vai mudar (0:00:03 a 0:00:30). O desafio é que se trabalha cada tarefa como um fim em si, sem negociar com o histórico do código existente (0:00:31 a 0:00:45). As técnicas dele (software vivo, automação, testes, trabalhar como chefe de cozinha, Python, ecossistema) existem para aumentar a capacidade de resolver problemas sem criar novos (0:00:45 a 0:01:21). Cada mudança é negociar com o passado em prol de um futuro (0:01:38 a 0:01:54). Ele retoma as três etapas: faz funcionar, faz direito, faz ficar rápido se precisar (0:01:59 a 0:02:08), e o risco de parar no primeiro passo é acumular débito técnico (0:02:14). Defende subir ao nível simbólico (0:02:44 a 0:03:09) e construir o software organicamente, não com plano prévio de 100 por cento (0:03:32 a 0:03:48).

Linha do tempo:
- [0:00:03] código é maleável, sempre muda.
- [0:00:31] tarefas tratadas como fim em si.
- [0:00:45] o conjunto de técnicas: software vivo, automação, testes, chef de cozinha.
- [0:01:38] mudar o código é negociar com o passado em prol de um futuro.
- [0:01:59] fazer funcionar, fazer direito, fazer ficar rápido se precisar.
- [0:02:44] subir ao nível simbólico, além das ferramentas.
- [0:03:32] processo de lapidar, sem planejar tudo antes.

Princípios:
- Cada mudança de código negocia com o passado em prol de um futuro (0:01:38 a 0:01:54).
- Fazer funcionar, depois fazer direito, que é trazer a capacidade sem aumentar o código de um para um (0:01:59 a 0:02:38).
- Parar em fazer funcionar acumula débito técnico (0:02:08 a 0:02:18).
- Subir ao nível simbólico, compreender a execução e o impacto, em vez de só colecionar ferramentas (0:02:44 a 0:03:09).
- Alavancagem do software é grande capacidade com baixo custo de manutenção e alto grau de saúde (0:03:09 a 0:03:30).

Código: não há código mostrado.

Citações (paráfrases de legenda, não verificadas):
- cada vez que você muda um código, você está negociando com o passado em prol de um futuro (aula 30, 0:01:38 a 0:01:45).
- faz funcionar, faz direito, faz ficar rápido se precisar (aula 30, 0:02:04 a 0:02:08).
- sem subir ao nível simbólico você vai estar executando demanda, correndo atrás do rabo (aula 30, 0:02:50 a 0:03:09).

### Aula 31: Quando o sistema é velho, ele precisa ser refeito?

Vídeo: https://www.youtube.com/watch?v=oQOxiqVturE · Duração: 4:31

Resumo: ele diz que a ideia de reescrever o sistema numa tecnologia nova o apavora (0:00:07 a 0:00:30). Já viu empresas quase quebrarem e processos judiciais por isso (0:00:33 a 0:00:40). Quem muda a tecnologia, a arquitetura e o escopo já está fazendo outro projeto, sem vínculo com o original, e deve tratá-lo assim (0:00:52 a 0:01:23, 0:02:04 a 0:02:21). Ele pede entender o risco real e o custo e, se for fazer outro, fazê-lo com planilha e orçamento (0:01:25 a 0:02:21). A equipe que faz o legado e a que aprende tecnologia nova no novo cria conflito de interesse (0:02:21 a 0:02:44). O trabalho do programador é gerenciar risco e gerar resultado (0:02:49 a 0:03:00). Há técnicas para lidar com código legado: testes de regressão, refatoração, intervenções pontuais (0:03:51 a 0:04:09). Legado é software que dá dinheiro há muito tempo (0:04:17 a 0:04:22).

Linha do tempo:
- [0:00:07] a ideia de reescrever o sistema o apavora.
- [0:00:33] empresas quase quebraram e processos judiciais.
- [0:00:52] mudar tecnologia, arquitetura e escopo é fazer outro projeto.
- [0:01:25] entender o risco real e quanto vai custar.
- [0:02:21] conflito de interesse entre a equipe do legado e a do novo.
- [0:02:49] o trabalho do programador é gerenciar risco.
- [0:03:51] técnicas: testes de regressão, refatoração, intervenções pontuais.
- [0:04:17] software legado é o que já dá dinheiro há muito tempo.

Princípios:
- Reescrever com outra tecnologia é fazer outro projeto, com outro orçamento e risco (0:00:52 a 0:01:23, 0:02:04 a 0:02:21).
- O trabalho do programador não é programar, é gerenciar risco e gerar resultado para o negócio (0:02:49 a 0:03:00).
- Para código legado existem técnicas: testes de regressão, refatoração, intervenções pontuais (0:03:54 a 0:04:09).
- Sistema legado já dá dinheiro; a reescrita gasta muito antes de dar retorno (0:04:17 a 0:04:28).

Código: não há código mostrado. A legenda desta aula é muito ruidosa; as citações abaixo são aproximações.

Citações (paráfrases de legenda, não verificadas):
- me dá pavor completo toda vez que alguém tem uma ideia brilhante de reescrever (aula 31, 0:00:07 a 0:00:12).
- o trabalho do programador não é programar, é gerenciar o risco [legenda: armador para programador] (aula 31, 0:02:49 a 0:02:55).
- o software não é legado, ele só está dando dinheiro há muito tempo (aula 31, 0:04:17 a 0:04:22).

### Aula 32: É ruim aprender a programar com Python?

Vídeo: https://www.youtube.com/watch?v=Xu06iC_hKNs · Duração: 5:17

Resumo: ele rebate o argumento de que começar por Python equivale a aprender a dirigir num carro automático: para ele é estupidez (0:00:00 a 0:00:26). O importante é resolver os problemas das pessoas, não fazer coisa difícil por fetiche (0:00:26 a 0:00:43), e o mito do programador fodão limita possibilidades (0:00:49 a 0:01:24). Usa a metáfora da marcha automática: o humano fazia o papel da máquina por restrição técnica; se você faz o que a máquina faz melhor, será automatizado (0:01:24 a 0:02:32). Saber o que acontece por baixo é importante, mas não é preciso fazer o que a máquina faz melhor (0:02:35 a 0:03:03). O garbage collector é o exemplo, e libera a capacidade cognitiva para o alto nível (0:03:07 a 0:03:45). O valor está em subir a abstração (0:03:51 a 0:04:15) e o trabalho do programador é resolver o problema das pessoas, não escrever código (0:04:55 a 0:05:10).

Linha do tempo:
- [0:00:00] o argumento do carro automático e a resposta: estupidez.
- [0:00:26] importante é resolver problemas das pessoas.
- [0:00:55] o mito do programador fodão.
- [0:01:24] metáfora da marcha automática: restrição técnica de uma época.
- [0:02:35] saber o que acontece por baixo, sem fazer o que a máquina faz melhor.
- [0:03:03] gerenciamento de memória e garbage collector.
- [0:03:51] subir o nível de abstração é onde está o valor.
- [0:04:20] por que sempre se estuda algo novo: papers antigos agora executáveis.
- [0:04:55] o trabalho do programador é resolver o problema das pessoas.

Princípios:
- O importante é resolver os problemas das pessoas, não fazer coisa difícil (0:00:26 a 0:00:43).
- Entender como a máquina funciona, sem competir com ela no que ela faz melhor (0:02:41 a 0:02:58).
- Subir o nível de abstração é onde está o valor que se entrega ao cliente (0:03:51 a 0:04:07).
- O trabalho do programador é resolver o problema das pessoas, não escrever código (0:04:55 a 0:05:05).

Código: não há código mostrado.

Citações (paráfrases de legenda, não verificadas):
- o importante é você resolver os problemas das pessoas (aula 32, 0:00:35 a 0:00:39).
- se você faz algo que a máquina faz melhor do que você, você vai ser automatizado (aula 32, 0:02:16 a 0:02:27).
- o trabalho do programador não é escrever código, é resolver o problema das pessoas usando a sua capacidade tecnológica (aula 32, 0:04:55 a 0:05:05).

### Aula 33: Faz sentido trocar partes no Django?

Vídeo: https://www.youtube.com/watch?v=u5jUlN2v9kc · Duração: 2:25

Resumo: para ele a vantagem de o Django ser desacoplável e ter camadas bem definidas não é trocar partes, e sim poder intervir e adicionar o que importa no meio do caminho (0:00:12 a 0:00:29). Ele prefere scripts Python que inicializam o Django em vez dos comandos de gerenciamento quando há muito processamento em segundo plano (0:00:38 a 0:01:01), usa pytest em vez do framework de testes padrão (0:01:06 a 0:01:13), e gosta de estender middlewares, login e banco (0:01:17 a 0:01:27). O que ele não faz de jeito nenhum é abstrair o framework, porque o framework usa o seu código; ele trata o ORM como algo que usa sempre (0:01:28 a 0:01:53), pois o ORM é extensível e aceita SQL direto quando necessário (0:01:59 a 0:02:15).

Linha do tempo:
- [0:00:12] a vantagem do desacoplamento é intervir, não trocar.
- [0:00:38] comandos de gerenciamento versus scripts próprios para processamento em segundo plano.
- [0:01:06] pytest no lugar do framework de testes padrão.
- [0:01:17] middlewares, login e banco como pontos de extensão.
- [0:01:28] não abstrair o framework nem criar camadas para ficar independente do ORM.
- [0:02:03] o ORM é extensível e aceita SQL direto.

Princípios:
- Valor do desacoplamento é poder intervir no caminho, não trocar peças (0:00:17 a 0:00:29).
- Não abstrair o framework: usar o que foi escolhido para ser mais produtivo (0:01:28 a 0:01:41).
- Tratar o ORM como algo que sempre se usa, estendendo-o ou recorrendo a SQL direto quando preciso (0:01:47 a 0:02:15).

Código: não há código mostrado.

Citações (paráfrases de legenda, não verificadas):
- a vantagem dele ser desacoplável não é necessariamente trocar as coisas, mas poder intervir (aula 33, 0:00:17 a 0:00:23).
- uma coisa que eu não faço de jeito nenhum é essa tentativa de abstrair o framework (aula 33, 0:01:23 a 0:01:28).
- não tem muito motivo para você fazer um sistema independente do framework que você escolheu (aula 33, 0:02:15 a 0:02:18).

### Aula 34: Quem tem 30 anos, está começando tarde na programação?

Vídeo: https://www.youtube.com/watch?v=xMmCSleXo0g · Duração: 2:14

Resumo: ele critica a correria de achar o destino final muito cedo e afirma que ninguém começa do zero, mas de onde está, com uma bagagem de vida (0:00:09 a 0:00:53). As pressões são diferentes aos 30 ou 40 anos (0:00:58 a 0:01:09), mas a experiência conta muito (0:01:12). Programar não é só código, é criar riqueza e gerar valor, e o conhecimento do negócio entra nisso (0:01:17 a 0:01:25). Dá o exemplo de um contador que virou programador e atua na área fiscal (0:01:27 a 0:01:39). Conclui que nunca é tarde e que é preciso combinar habilidades práticas e subjetivas num caminho próprio (0:01:55 a 0:02:12).

Linha do tempo:
- [0:00:09] correria de achar o destino cedo demais.
- [0:00:37] com 30 ou 40 anos há bagagem e história a incluir.
- [0:00:49] você começa de onde está.
- [0:00:58] as pressões são outras, a experiência conta.
- [0:01:17] programar é criar riqueza e gerar valor.
- [0:01:27] exemplo do contador que foi para programação na área fiscal.
- [0:01:57] nunca é tarde.

Princípios:
- Ninguém começa do zero, começa de onde está, incluindo a própria história (0:00:44 a 0:00:53).
- Programar não é só fazer código, é gerar valor com o entendimento do negócio (0:01:17 a 0:01:25).
- Combinar talentos anteriores com programação indica o tipo de empresa a buscar (0:01:47 a 0:01:57).

Código: não há código mostrado.

Citações (paráfrases de legenda, não verificadas):
- você não começa do zero, você começa de onde você tá sempre (aula 34, 0:00:49 a 0:00:53).
- lembre-se, programar não é só fazer código, você precisa criar riqueza, gerar valor (aula 34, 0:01:17 a 0:01:21).
- nunca é tarde (aula 34, 0:01:57).

### Aula 35: O que fazer quando se deparar com questões de operação?

Vídeo: https://www.youtube.com/watch?v=bNq0NvfJBbU · Duração: 1:46

Resumo: ele diz que lidar com operação e infraestrutura impacta o deploy, a agilidade e a segurança (0:00:00 a 0:00:21). Equipes pequenas costumam querer fazer tudo na mão para economizar com serviços mais sofisticados (0:00:21 a 0:00:30). Para ele, quem tem pouca grana e investe numa equipe de desenvolvimento corre risco ao não usar o serviço adequado (0:00:32 a 0:00:51). Recomenda para equipe pequena Heroku ou outra plataforma como serviço, que custa mais mas sai mais barato que uma equipe de infraestrutura ou dividir a atenção dos programadores (0:01:00 a 0:01:29, 0:01:30 a 0:01:43).

Linha do tempo:
- [0:00:00] questões de operação e infraestrutura aparecem.
- [0:00:21] equipes pequenas querem fazer tudo na mão para economizar.
- [0:00:51] equipe pequena de um a três programadores.
- [0:01:00] contratar algo de mais alto nível.
- [0:01:30] recomendação: Heroku ou plataforma como serviço.

Princípios:
- Não economizar com bobagem: o serviço adequado custa menos que desviar a atenção da equipe do produto para manutenção (0:01:05 a 0:01:29).
- Para equipe pequena, delegar a sustentação a uma plataforma como serviço (0:01:30 a 0:01:43).

Código: não há código mostrado. A legenda pode ter distorções: contrato um Hello com 4 camisas em 0:01:00 é leitura não confiável.

Citações (paráfrases de legenda, não verificadas):
- é muito comum equipes muito pequenas quererem fazer tudo na mão, tentando economizar dinheiro com serviços mais sofisticados (aula 35, 0:00:21 a 0:00:30).
- não economiza com besteira, as coisas têm o preço que têm (aula 35, 0:01:25 a 0:01:27).
- eu recomendo muito para equipe pequena que use Heroku ou algum platform as a service (aula 35, 0:01:30 a 0:01:36).

### Aula 36: Conselho para quem mora no interior e quer aprender programação

Vídeo: https://www.youtube.com/watch?v=5rKiERO5It8 · Duração: 1:09

Resumo: ele diz que se aprende programação em qualquer lugar do Brasil e aconselha pesquisar a região (0:00:08 a 0:00:17). Indica a comunidade de Belém e oferece contato (0:00:19 a 0:00:28). Pede que procure quem faz o que você quer fazer e que não se limite à região, porque a internet permite expandir a localização e encontrar afinidades em qualquer lugar do país (0:00:28 a 0:01:06). A legenda fala em 2020; trata-se de leitura de legenda ruidosa.

Linha do tempo:
- [0:00:08] aprende-se programação em qualquer lugar do Brasil.
- [0:00:15] pesquisar a própria região.
- [0:00:19] indicação de comunidade e contato de Belém (nomes na legenda são incertos).
- [0:00:28] procure quem faz o que você quer fazer.
- [0:00:35] não se limite à sua região, você está na internet.
- [0:00:54] a internet expande a localização.

Princípios:
- Procure quem faz o que você quer fazer (0:00:28 a 0:00:34).
- Não se limite à região; use a internet para encontrar afinidade em qualquer lugar (0:00:35 a 0:01:06).
- Se houver gente boa na região, colar com ela ajuda (0:00:44 a 0:00:52).

Código: não há código mostrado.

Citações (paráfrases de legenda, não verificadas):
- procure quem faz o que você quer fazer (aula 36, 0:00:28 a 0:00:34).
- não se limite à tua região, você está na internet (aula 36, 0:00:35 a 0:00:44).
- a internet é uma ferramenta para a gente expandir a nossa localização (aula 36, 0:00:54 a 0:00:57).

### Aula 37: Como criar rotas no Django do jeito certo
Vídeo: https://www.youtube.com/watch?v=zG5pS5IxUv8 · Duração: 1:49

Resumo: Ele critica o padrão dos tutoriais e do manual do Django de ter uma relação um-para-um entre rotas e views (aula 37, 0:00:20 a 0:00:34). Propõe definir o workflow do sistema, observar o que se repete e implementar uma classe que compõe as URLs dinamicamente a partir do modelo (aula 37, 0:00:49 a 0:01:10). O resultado é um urlconf pequeno, em que um único objeto representa um conjunto grande de rotas (aula 37, 0:01:29 a 0:01:38).

Linha do tempo:
- [0:00:00] Pergunta o que são urlconf (legenda: urlconf os componentes).
- [0:00:20] Diz que não gosta do padrão de relação um-para-um entre rotas e views.
- [0:00:37] Diz que o Django não exige um módulo `urls.py`; procura o atributo `urlpatterns` do objeto em questão (legenda: url-pattern), que pode ser até o módulo.
- [0:00:49] Define o workflow do sistema e observa o que se repete (num CRUD: criação, edição, deleção com confirmação).
- [0:01:03] Implementa uma classe que computa as URLs dinamicamente em função do modelo, usando o nome do modelo, com padrões que podem ser sobrescritos.
- [0:01:32] Um único objeto representa um conjunto grande de rotas; o sistema fica muito menor.

Princípios:
- Não amarre uma rota a cada view; observe a repetição do workflow e abstraia em um componente de URL reutilizável (aula 37, 0:00:49 a 0:01:21).
- O Django procura `urlpatterns` no objeto, não exige o módulo `urls.py` (aula 37, 0:00:37 a 0:00:47).

Código: nenhum mostrado; a legenda só descreve a ideia.

Citações (paráfrases de legenda, não verificadas):
- Padrão que eu não gosto nem um pouco, que é uma relação um-para-um entre as rotas e as views (aula 37, 0:00:20).
- Posso definir até os padrões de como se comporta caso a pessoa não sobrescreva (aula 37, 0:01:13).
- Um único objeto representa um conjunto grande de rotas e isso faz o sistema ficar muito mais pequenininho (aula 37, 0:01:32).

### Aula 38: Como estudar programação do jeito errado
Vídeo: https://www.youtube.com/watch?v=BM-vS6IaYUY · Duração: 4:46 (transcrição Whisper)

Resumo: A partir de um mentorado em transição de carreira com quatro livros e muitos cursos, que fica ansioso e não percebe progresso (aula 38, 0:00:44 a 0:00:57), ele diz que em programação não se aprende lendo o livro, mas programando (aula 38, 0:01:06). Recomenda copiar código linha por linha, rodar e usar as perguntas geradas para pesquisar (aula 38, 0:02:22 a 0:02:53), com 80% do tempo em prática (aula 38, 0:03:15 a 0:03:21) e começando pelo pequeno (aula 38, 0:04:16 a 0:04:23).

Linha do tempo:
- [0:00:08] Contexto: mentoria modo carreira e um mentorado que estuda todo dia sem resultado.
- [0:00:44] Diagnóstico: quatro livros, lista enorme, ansiedade e dificuldade de perceber progresso.
- [0:01:06] Em programação você aprende programando; o livro dá insight, tira dúvida e serve de referência.
- [0:02:22] Copiar linha por linha, sem copiar e colar, e rodar o código.
- [0:03:15] Focar 80% do tempo em prática e tirar dúvidas a partir dela.
- [0:03:29] Não tentar entender antes de saber fazer; o ciclo faz, não entende, estuda, modela de novo.
- [0:04:16] Começar por coisas muito simples e pequenas; analogia com a criança que engatinha antes de andar.

Princípios:
- Conhecimento é prático: é preciso saber fazer, e o mais real na programação é escrever um programa (aula 38, 0:01:56 a 0:02:17).
- Leia a documentação inteira só se já tem experiência e quer inferir a arquitetura (aula 38, 0:01:31 a 0:01:50).
- Foque 80% do tempo em prática (aula 38, 0:03:15 a 0:03:21).
- Saber fazer abre as perguntas relevantes, que alimentam o ciclo de aprender (aula 38, 0:03:49 a 0:04:14).

Código: nenhum.

Citações (paráfrases de legenda, não verificadas):
- Em programação você não aprende lendo o livro, você aprende programando (aula 38, 0:01:06).
- Não tente entender antes de saber fazer, é melhor você saber fazer (aula 38, 0:03:29).
- Nenhuma criança nasce e sai correndo, a criança aprende passo a passo (aula 38, 0:04:23).

### Aula 39: Sintomas da Patternite
Vídeo: https://www.youtube.com/watch?v=aibuJ2LD2sg · Duração: 1:31

Resumo: Quem estuda design patterns tende a querer aplicar tudo; levado ao extremo, manifesta a patternite [legenda: paternik], querendo montar a arquitetura com todos os padrões antes de escrever código ou resolver o problema (aula 39, 0:00:02 a 0:00:25). Ele responde que padrões são reconhecidos a partir de várias instâncias, com experiência (aula 39, 0:00:27 a 0:00:42), e que a estratégia é resolver o problema primeiro e depois refletir sobre como organizar o código (aula 39, 0:00:45 a 0:00:59).

Linha do tempo:
- [0:00:02] Quem começa a estudar design patterns quer aplicar tudo o que aprendeu.
- [0:00:13] No extremo, os sintomas da patternite: aplicar padrões antes de escrever código.
- [0:00:27] Padrões são reconhecidos a partir de diversas instâncias, com experiência.
- [0:00:45] Estratégia: resolver o problema, ter uma primeira versão funcionando, depois refletir sobre a organização.
- [0:01:01] Os padrões emergem; fluência é detectar relações que um outro padrão articularia melhor.
- [0:01:26] O foco é sempre resolver o problema primeiro.

Princípios:
- Padrões emergem do código; não se impõem antes dele (aula 39, 0:01:01 a 0:01:05).
- Resolva o problema primeiro; só então reflita sobre qual padrão organiza melhor (aula 39, 0:00:45 a 0:00:59 e 0:01:26).

Código: nenhum.

Citações (paráfrases de legenda, não verificadas):
- Antes de resolver o problema você quer aplicar os padrões e montar uma arquitetura mirabolante (aula 39, 0:00:17).
- Os padrões eles emergem (aula 39, 0:01:01).
- O foco é sempre resolver o problema primeiro (aula 39, 0:01:26).

### Aula 40: O que fazer quando seu chefe pede uma mudança "rapidinha"?
Vídeo: https://www.youtube.com/watch?v=VYK-6Y7SwX4 · Duração: 2:37

Resumo: Ele considera que o pedido rápido faz sentido e que cabe ao programador entender a necessidade real por trás (aula 40, 0:00:07 a 0:00:30). Usa a metáfora da sala de emergência do hospital: na emergência se estanca o sangramento, mesmo com procedimentos que deixam cicatriz, e depois vem a cirurgia reparadora planejada (aula 40, 0:00:37 a 0:01:16). O essencial é comunicar o efeito colateral da estratégia adotada e trabalhar a emergência em duas etapas (aula 40, 0:01:20 a 0:01:58).

Linha do tempo:
- [0:00:07] Faz sentido o pedido de mudança rapidinha; cabe avaliar o alinhamento.
- [0:00:24] O pedido esconde uma necessidade real que é preciso compreender.
- [0:00:35] Metáfora da sala de emergência do hospital.
- [0:01:02] Contraste com a cirurgia plástica ou reparadora, marcada com antecedência e estudada.
- [0:01:20] O mais importante é comunicar o efeito colateral e as consequências da estratégia.
- [0:01:45] Duas etapas: estancar o sangramento agora e depois uma cirurgia reparadora.
- [0:02:09] Se o gestor escolher não fazer a segunda etapa, deve ter clareza e arcar com as consequências; a conta técnica chega.
- [0:02:21] Não existe código sempre pronto e resolvido; o código sempre muda.

Princípios:
- Emergência exige procedimento rápido com efeito colateral; trabalho planejado permite fazer sem cicatriz (aula 40, 0:00:44 a 0:01:16).
- Comunique os efeitos colaterais e quantos problemas a estratégia cria (aula 40, 0:01:20 a 0:01:45).
- Tratar a emergência em duas etapas, a segunda reparadora (aula 40, 0:01:45 a 0:01:58).
- Quem decide não fazer a etapa reparadora deve saber que a conta técnica chega (aula 40, 0:02:09 a 0:02:18).

Código: nenhum.

Citações (paráfrases de legenda, não verificadas):
- Um pedido desse esconde na verdade necessidades reais, você precisa compreender (aula 40, 0:00:24).
- O mais importante é comunicar o efeito colateral, quais são as consequências da estratégia (aula 40, 0:01:24).
- Não existe código que está sempre pronto, sempre resolvido, o código sempre muda (aula 40, 0:02:21).

### Aula 41: O conceito de app do Django, atrapalha ou ajuda?
Vídeo: https://www.youtube.com/watch?v=KfIriuMXW5M · Duração: 1:13

Resumo: Ele acha que o conceito de app do Django atrapalha mais do que ajuda (aula 41, 0:00:00 a 0:00:05). Muda a estrutura de diretórios: o projeto é um único pacote e tudo é biblioteca; alguns pacotes são apps, outros são bibliotecas Python simples (aula 41, 0:00:06 a 0:00:27). Não gosta de dividir o sistema em partes do site; trata a app reutilizável como uma biblioteca Python normal, o que dá mais flexibilidade para uma análise fria da saúde do código (aula 41, 0:00:34 a 0:01:12).

Linha do tempo:
- [0:00:00] O conceito de app atrapalha mais do que ajuda.
- [0:00:06] Muda a estrutura de diretórios em relação à documentação; o projeto é um único pacote.
- [0:00:15] Para ele tudo é biblioteca; tem pacotes que são apps e pacotes que são simples bibliotecas.
- [0:00:36] Não gosta de dividir o sistema como partes do site.
- [0:00:42] Critica o sonho antigo da app reutilizável; a maioria acaba copiando o código-fonte para estender.
- [0:01:00] Tratar como biblioteca Python normal dá mais flexibilidade.

Princípios:
- Tudo é biblioteca; o projeto é um pacote (aula 41, 0:00:08 a 0:00:25).
- App reutilizável do Django costuma acabar em cópia do código-fonte; trate como biblioteca Python normal (aula 41, 0:00:51 a 0:01:04).

Código: nenhum.

Citações (paráfrases de legenda, não verificadas):
- Para mim tudo é biblioteca (aula 41, 0:00:15).
- Eu não gosto de dividir o sistema como partes do site (aula 41, 0:00:36).
- Tem que tratar como uma biblioteca Python normal (aula 41, 0:01:00).

### Aula 42: Por que uso Wordpress no meu site, e, não Python e Django
Vídeo: https://www.youtube.com/watch?v=zrkSHO7LYgk · Duração: 2:23

Resumo: A resposta é que tecnologia serve para resolver problemas e o foco é gerar valor (aula 42, 0:00:05 a 0:00:10). Para um site simples já existe solução pronta e um ecossistema de profissionais; refazer é gastar energia repetindo algo resolvido (aula 42, 0:00:15 a 0:00:43). Python e Django ficam para os bastidores, integrações e automações (aula 42, 0:01:07 a 0:01:16). O importante é entender o problema e o negócio (aula 42, 0:01:16 a 0:01:20, 0:02:17).

Linha do tempo:
- [0:00:05] Tecnologia é para resolver problemas; o foco é gerar valor.
- [0:00:15] Um site simples já está pronto; refazer é gastar energia repetindo o que está resolvido.
- [0:00:34] Existe um ecossistema de profissionais (equipe de design, e assim por diante) em torno do WordPress.
- [0:01:07] Nos bastidores usa Python e Django para integrações e automações pequenas, porém importantes.
- [0:01:16] Importante entender que problema se quer resolver e o que se quer alcançar.
- [0:01:44] Exemplo citado: globo.com teria feito um sistema de jornalismo em Python e Django por causa do workflow complexo (ele diz não saber como está hoje).
- [0:02:10] No caso do site, meia dúzia de pessoas dominam a tecnologia e o liberam para o resto.

Princípios:
- Foque em gerar valor, não em refazer o que já está resolvido (aula 42, 0:00:05 a 0:00:19).
- Fazer tudo na mão por querer tecnologia tira o foco de criar soluções que não estão prontas (aula 42, 0:01:22 a 0:01:36).
- Entenda qual é o seu negócio (aula 42, 0:02:17).

Código: nenhum.

Citações (paráfrases de legenda, não verificadas):
- Tecnologia é para resolver problemas, o foco é gerar valor (aula 42, 0:00:05).
- É muito importante entender que problema você está querendo resolver (aula 42, 0:01:16).
- Entenda qual é o teu negócio (aula 42, 0:02:17).

### Aula 43: Dá para programar com uma lógica razoável?
Vídeo: https://www.youtube.com/watch?v=wiZ0SJwZ9nU · Duração: 2:33

Resumo: Ele diz que sim, dá para programar com lógica razoável (aula 43, 0:00:00 a 0:00:07). Todo ser humano compreende lógica e a usa no dia a dia; o que falta é repertório (aula 43, 0:00:11 a 0:00:24). Defende ensinar programação a partir da prática guiada e só depois mostrar como a lógica atua, mostrando o concreto antes de explicar (aula 43, 0:00:46 a 0:01:23). O repertório vem de experimentar, praticar e errar (aula 43, 0:01:48 a 0:01:58).

Linha do tempo:
- [0:00:02] Dá para programar com lógica razoável.
- [0:00:11] O problema não é dificuldade com lógica, e sim falta de repertório.
- [0:00:29] Receio causado por verdadeiro ou falso e proposições enormes de lógica de programação.
- [0:00:46] Deveria ser ao contrário: ensinar programação pela prática guiada e depois mostrar a lógica.
- [0:01:16] Mostra o concreto e depois explica, para despertar curiosidade.
- [0:01:48] O repertório vem de experimentos, exercícios e muito erro.
- [0:02:02] Quem parece mágico ao achar um erro tem repertório de como as coisas se afetam.

Princípios:
- Mostre antes de explicar (aula 43, 0:01:16 a 0:01:21).
- Repertório de programação vem de experimentar e errar, não existe outro caminho (aula 43, 0:01:48 a 0:02:31).

Código: nenhum.

Citações (paráfrases de legenda, não verificadas):
- Todo ser humano compreende lógica, a gente usa isso no dia a dia (aula 43, 0:00:14).
- Mostra o concreto e depois explica (aula 43, 0:01:16) [legenda: do concreto ou abstrato mostra e depois explica].
- Isso só vem com experiências, não tem outra (aula 43, 0:02:29).

### Aula 44: No Code: por que não funciona
Vídeo: https://www.youtube.com/watch?v=vdohSPd0OKs · Duração: 3:40

Resumo: Ele argumenta que, depois de 60 a 70 anos, ainda se programa em modelo textual e que as tecnologias criadas para abstrair a programação, como RAD, não funcionaram como se queria (aula 44, 0:00:14 a 0:00:47). Ferramentas no-code aumentam a produtividade com um fluxo de trabalho pré-estabelecido, mas têm uma opinião embutida e flexibilidade limitada (aula 44, 0:00:48 a 0:01:22). Quando o negócio cresce, o custo de coordenação entre ferramentas explode (aula 44, 0:02:17 a 0:02:37); a infraestrutura vai ficando mais abstrata e barata, e um pouco de código faz mais do que no-code (aula 44, 0:03:05 a 0:03:38).

Linha do tempo:
- [0:00:14] Programação tem 60 a 70 anos e ainda é textual.
- [0:00:25] Tecnologias para evitar programar não funcionaram como se queria (cita RAD; a legenda traz ML [provável mis-hearing]).
- [0:00:48] Ferramentas dão um fluxo de trabalho pré-estabelecido, o que é útil.
- [0:01:02] A ferramenta tem uma opinião e um design de alguém.
- [0:01:22] Relação de amor e ódio com o Zapier [legenda: Zap]: bom para o simples, vira costura no elaborado; ele escreve código e põe na Lambda.
- [0:01:53] Nada é tão poderoso quanto programar.
- [0:02:17] Quando o negócio cresce, o custo de coordenação entre ferramentas que você não controla explode.
- [0:02:43] Pessoas gastam energia adequando o processo interno à restrição da ferramenta, quando poderiam simplificar o processo.
- [0:03:05] A infraestrutura sobe de abstração (servidor físico, depois Lambda) e fica mais barata.
- [0:03:30] Um pouco de conhecimento de código faz coisas mais ousadas do que o no-code.

Princípios:
- A ferramenta no-code traz opinião e flexibilidade limitadas (aula 44, 0:01:02 a 0:01:22).
- Adequar o processo da empresa à ferramenta é custo oculto; simplificar o processo e usar código pode ser melhor (aula 44, 0:02:43 a 0:03:00).
- Sistema ancorado em várias ferramentas externas tem custo de coordenação explosivo (aula 44, 0:02:17 a 0:02:43).

Código: nenhum.

Citações (paráfrases de legenda, não verificadas):
- No final das contas nada vai ser tão poderoso quanto programar (aula 44, 0:01:53).
- O custo de coordenação entre as ferramentas explode (aula 44, 0:02:32).
- Um pouquinho de conhecimento de código faz coisas mais ousadas do que o no-code consegue (aula 44, 0:03:30).

### Aula 45: E quando o programador diz: FUNCIONA NA MINHA MÁQUINA?
Vídeo: https://www.youtube.com/watch?v=rqMpwuChaLc · Duração: 0:51

Resumo: Em relato curto e de legenda ruim, ele conta que começou a tirar prints e gravar vídeos mostrando o sistema funcionando (aula 45, 0:00:00 a 0:00:07) e chama funciona na minha máquina de uma das desculpas mais esfarrapadas de programador (aula 45, 0:00:14 a 0:00:22). O resto da legenda é quase ininteligível; nenhuma conclusão adicional é afirmada.

Linha do tempo:
- [0:00:00] Começou a tirar print e gravar vídeo do sistema funcionando.
- [0:00:09] Entenderam que o colega sempre dizia que funcionava na máquina dele.
- [0:00:14] Chama isso de uma das desculpas mais esfarrapadas de programador.
- [0:00:36] Diz que é um clássico (legenda parcialmente ininteligível entre 0:00:22 e 0:00:34).

Princípios:
- Funcionar só na máquina de quem escreveu é desculpa fraca (aula 45, 0:00:14 a 0:00:22).

Código: nenhum.

Citações (paráfrases de legenda, não verificadas):
- Isso é uma das desculpas mais esfarrapadas dos programadores (aula 45, 0:00:14).
- Ele sempre falava que na minha máquina funciona (aula 45, 0:00:09) [legenda confusa].

### Aula 46: Python é amor
Vídeo: https://www.youtube.com/watch?v=RIzm5jOh4IA · Duração: 0:34 (transcrição Whisper, pt)

Resumo: Em meio minuto ele responde por que Python: a linguagem foi feita por pythonistas para pythonizar o universo e tudo o que nela é pensado serve para facilitar a vida de quem programa (aula 46, 0:00:03 a 0:00:11). As coisas funcionam de forma simples e com elegância (aula 46, 0:00:11). Ele percebe uma cultura que combina estética e função, e vê o Python fazendo isso muito bem: código bonito e eficiente ao mesmo tempo (aula 46, 0:00:16 a 0:00:31).

Linha do tempo:
- [0:00:00] Pergunta e resposta curta: Python é amor.
- [0:00:03] A linguagem foi feita por pythonistas; tudo nela facilita a vida.
- [0:00:11] As coisas funcionam de um jeito simples, com elegância.
- [0:00:16] A cultura combina estética e função.
- [0:00:28] Código bonito e eficiente ao mesmo tempo.

Princípios:
- Estética e função andam juntas: código bonito e eficiente ao mesmo tempo (aula 46, 0:00:18 a 0:00:31).
- A linguagem existe para facilitar a vida de quem a usa; a simplicidade vem com elegância (aula 46, 0:00:07 a 0:00:16).

Código: nenhum.

Citações (paráfrases de legenda, não verificadas): (paráfrases de transcrição automática, não verificadas)
- Python foi feito por pythonistas para pythonizar o universo (aula 46, 0:00:03).
- É o código bonito e eficiente ao mesmo tempo (aula 46, 0:00:28).

### Aula 47: Melhores dicas para aprender a programar
Vídeo: https://www.youtube.com/watch?v=ZGhF7CsKjzs · Duração: 7:54

Resumo: A legenda é ruidosa, mas a estrutura em dicas é identificável. Ele fala da dificuldade de perceber progresso (aula 47, 0:00:31 a 0:00:39) e de aprender com experimentos que preencham lacunas de conhecimento (aula 47, 0:01:18 a 0:01:26). As dicas: rastrear o aprendizado com um diário de hora de início, fim e o que aprendeu (aula 47, 0:01:59 a 0:02:26); planejar o estudo, já que um livro não é um plano de estudo e vale escolher os capítulos essenciais (aula 47, 0:02:41 a 0:03:30); não confundir aprender a programar com construir um portfólio, praticando fundamentos como no esporte (aula 47, 0:03:30 a 0:04:18); dividir um problema em tarefas menores (aula 47, 0:04:43 a 0:05:38); e não se espalhar, guardando achados em um arquivo de referências (aula 47, 0:05:43 a 0:06:15).

Linha do tempo:
- [0:00:31] Fala da dificuldade de perceber progresso na habilidade de programar.
- [0:01:18] Estratégia: experimentos corretos que preencham lacunas de conhecimento.
- [0:01:59] Dica de rastreamento: diário com hora de início, de término e o que aprendeu.
- [0:02:41] Planejar: livro não é plano de estudo; selecionar os capítulos essenciais.
- [0:03:30] Terceira dica: não confundir aprender a programar com desenvolver um portfólio de software.
- [0:04:04] Analogia com esporte: treinar fundamentos, mas sem só fundamentos.
- [0:04:21] Time-box: meia hora para tentar progredir; se travar, dividir em tarefas menores.
- [0:05:04] Exemplo da planilha: ler a planilha e automatizar o download em projetos separados, depois combinar.
- [0:05:43] Não se espalhar: guardar o que acha interessante em um arquivo de referências com link e motivo.
- [0:07:07] Fecha dizendo que a sensação de que o problema é maior do que você é falsa e é só estratégia.

Princípios:
- Rastreie o seu aprendizado com evidências (aula 47, 0:01:59 a 0:02:26).
- Um livro não é um plano de estudo; planeje e foque no essencial (aula 47, 0:02:41 a 0:03:30).
- Aprenda em problemas simples focados em fundamentos, não em projeto complexo de portfólio (aula 47, 0:03:30 a 0:04:01).
- Divida o problema em partes menores quando travar (aula 47, 0:04:43 a 0:05:38).
- Não se disperse; registre achados em um arquivo de referências (aula 47, 0:05:43 a 0:06:15).

Código: nenhum.

Citações (paráfrases de legenda, não verificadas):
- O livro não é um plano de estudo (aula 47, 0:02:46) [legenda: o livro não é um plano de estudo polêmico].
- Eu começo pegando o problema e dividindo em tarefas menores (aula 47, 0:04:45).
- É só uma sensação falsa de que o problema é muito maior do que você consegue resolver (aula 47, 0:07:07).

### Aula 48: Não se distraia com "software de verdade"
Vídeo: https://www.youtube.com/watch?v=KXc8RJ2bjxk · Duração: 2:46

Resumo: A legenda é ruidosa. Ele alerta para a cilada de querer fazer software de verdade e desviar a atenção do essencial, que é resolver o problema (aula 48, 0:00:00 a 0:00:15; 0:00:15 a 0:00:49). Cada época teve seu imaginário do que é programa de sucesso, do Windows à internet e ao celular (aula 48, 0:00:28 a 0:00:43). Recomenda começar por problemas pequenos (aula 48, 0:01:24), conta o caso de um conhecido com sistema de loja (aula 48, 0:01:28 a 0:01:58, legenda confusa) e diz que a curva de aprendizagem não é linear (aula 48, 0:02:25 a 0:02:33).

Linha do tempo:
- [0:00:00] A atenção sai do essencial quando se tenta alcançar uma ferramenta sem vínculo com o problema.
- [0:00:15] Existe a cilada de querer só fazer software de verdade.
- [0:00:28] Quando começou, programa de sucesso era Windows; depois internet, depois celular.
- [0:00:59] Software bacana é aquele que resolve o seu problema (legenda confusa nesse trecho).
- [0:01:24] Ao começar, trabalhe com problemas pequenos.
- [0:01:28] Caso de um conhecido com sistema de loja e conferência de entregas (legenda confusa).
- [0:02:25] A curva de aprendizagem não é linear.

Princípios:
- Não deixe o imaginário de software de verdade desviar sua atenção do problema (aula 48, 0:00:00 a 0:00:15; 0:00:52 a 0:01:13).
- Comece por problemas pequenos (aula 48, 0:01:24).
- A curva de aprendizagem não é linear (aula 48, 0:02:25 a 0:02:33).

Código: nenhum.

Citações (paráfrases de legenda, não verificadas):
- Você tira a atenção das coisas mais essenciais, que é resolver o problema (aula 48, 0:00:00).
- Quando eu comecei a programar, programa de sucesso era Windows (aula 48, 0:00:28).
- A curva de aprendizagem não é linear (aula 48, 0:02:27).

### Aula 49: "Não adianta tentar programar.., tem que aprender lógica primeiro!" SERÁ MESMO?
Vídeo: https://www.youtube.com/watch?v=Jfqs9yzxe0w · Duração: 4:39 (transcrição Whisper)

Resumo: Ele reage a quem diz a iniciantes que primeiro tem que aprender lógica (aula 49, 0:00:17 a 0:00:28), dizendo que a lógica vem com a prática e que fatiar a experiência em conteúdos, como na escola, desconsidera o interesse da pessoa (aula 49, 0:00:37 a 0:01:09, 0:01:27 a 0:01:38). Usa a analogia de querer tocar uma música específica na guitarra (aula 49, 0:01:47 a 0:02:08). Orienta duas perguntas: o que você quer programar e qual é a menor versão disso (aula 49, 0:02:12 a 0:02:38). O exemplo é o médico que automatizou laudos cardiológicos e foi evoluindo (aula 49, 0:02:38 a 0:03:42). Pede que se ajude as pessoas a fazer o que querem (aula 49, 0:03:51 a 0:04:27).

Linha do tempo:
- [0:00:17] Cita a resposta comum de que primeiro tem que aprender lógica.
- [0:00:32] A lógica vem com a prática; critica a educação que fatia a experiência em conteúdos.
- [0:01:09] O maior obstáculo ao aprendizado é o ensino prescritivo que ignora indivíduo, interesses e talentos.
- [0:01:47] Analogia da guitarra: quer tocar uma música, não ser guitarrista.
- [0:02:12] Primeira pergunta: o que você quer programar? Segunda: qual é a menor versão disso, a mais simples.
- [0:02:38] Exemplo do Bernardo, médico, que automatizou a criação de laudos de exame cardiológico.
- [0:03:09] Ele evoluiu: otimizou, melhorou a legibilidade, aprendeu padrões, exceções, console e interface gráfica.
- [0:03:51] Pede para ajudar as pessoas a alcançarem o que querem, em vez de impor o caminho ideal.

Princípios:
- A lógica vem da prática (aula 49, 0:00:37 a 0:00:42).
- Parta do interesse do aprendiz e da menor versão do que ele quer fazer (aula 49, 0:02:12 a 0:02:38).
- Evoluir um problema real faz aprender padrões, exceções e mais lógica (aula 49, 0:03:09 a 0:03:42).
- Ajude a pessoa a chegar aonde quer, não imponha o caminho ideal (aula 49, 0:04:18 a 0:04:27).

Código: nenhum; ele só descreve a evolução do código do exemplo (aula 49, 0:03:09 a 0:03:33).

Citações (paráfrases de legenda, não verificadas):
- A lógica vem com a prática (aula 49, 0:00:37).
- Qual é a menor versão disso, a coisa mais simples, mais trivial (aula 49, 0:02:29).
- O que importa é ajudar o colega a chegar onde ele quer, e não arrumar o caminho ideal (aula 49, 0:04:18).

### Aula 50: Devo programar na mão ou usar um framework?
Vídeo: https://www.youtube.com/watch?v=9j88xEQMuFE · Duração: 2:48

Resumo: A legenda é muito ruidosa. Ele aponta a cilada de querer desenvolver o framework em vez do sistema: quem quer fazer um jogo faz a ferramenta que faz o jogo (aula 50, 0:00:14 a 0:00:29). Como Django é software livre, é possível ler o código para entender como funciona por dentro, o que ele chama de libertador (aula 50, 0:00:46 a 0:01:06). Fazer tudo na mão custa tempo e esforço e pode tirar a atenção (aula 50, 0:01:11 a 0:01:33). Explorar o funcionamento do framework é bom para estudo (aula 50, 0:01:35 a 0:01:54), mas não se deve limitar a ser usuário nem partir da independência total (aula 50, 0:01:56 a 0:02:08).

Linha do tempo:
- [0:00:14] Cilada comum: querer desenvolver o framework em vez do sistema que se quer entregar.
- [0:00:25] Exemplo: para fazer um jogo, faz-se a ferramenta que faz o jogo.
- [0:00:46] Django é software livre; dá para ler o código e entender como funciona por dentro.
- [0:00:59] Entender como funciona é libertador.
- [0:01:11] Fazer na mão custa tempo e esforço e pode tirar a atenção do que se quer.
- [0:01:35] Explorar como o framework funciona é interessante para estudo.
- [0:01:56] Não se limite a ser usuário, nem parta do extremo de não querer depender de nada.
- [0:02:08] Com tempo e maturidade se desenvolvem habilidades técnicas.

Princípios:
- Não construa a ferramenta antes do sistema que quer entregar (aula 50, 0:00:14 a 0:00:29).
- Leia o código do framework livre para entender como funciona por dentro (aula 50, 0:00:46 a 0:01:06).
- Evite os dois extremos: ser só usuário e não querer depender de nada (aula 50, 0:01:56 a 0:02:08).

Código: nenhum.

Citações (paráfrases de legenda, não verificadas):
- Você tem de fazer um jogo, você faz a ferramenta que faz o jogo (aula 50, 0:00:25).
- É muito libertador entender como ele funciona por dentro (aula 50, 0:00:59) [legenda parcialmente confusa].
- Não se limitar a ser um usuário (aula 50, 0:01:56).

### Aula 51: Mas afinal, o que é um framework?
Vídeo: https://www.youtube.com/watch?v=csiSB336JZ4 · Duração: 2:23

Resumo: A legenda é ruidosa. Ele diz que se confunde Django com a linguagem ou com a ferramenta para fazer sites (aula 51, 0:00:06 a 0:00:23). Um framework reúne os padrões que se repetem em uma área e dá funções de mais alto nível (aula 51, 0:00:26 a 0:00:47). A web, no fundo, é troca de mensagens de texto sobre HTTP, e o framework poupa o que é primitivo para que a atenção vá ao específico do projeto (aula 51, 0:00:57 a 0:01:31). O ganho é agilidade e produtividade, apoiado em experiência coletiva (aula 51, 0:01:36 a 0:01:55).

Linha do tempo:
- [0:00:06] Confunde-se o framework com um produto isolado ou com a linguagem.
- [0:00:20] Django não é a única ferramenta para fazer sites (legenda confusa).
- [0:00:26] Framework é um conjunto que aplica padrões das coisas frequentes de uma área.
- [0:00:44] Dá funções de mais alto nível.
- [0:01:00] A web é troca de mensagens de texto via protocolo HTTP.
- [0:01:20] O framework retira a estrutura comum para você dedicar atenção ao que é específico do projeto.
- [0:01:36] Ganha-se agilidade e produtividade.
- [0:01:49] O framework reúne experiência coletiva sobre como criar um sistema web.

Princípios:
- Framework é um conjunto de padrões recorrentes de uma área, com funções de alto nível (aula 51, 0:00:26 a 0:00:47).
- Use framework para dedicar atenção ao que é específico da sua ideia (aula 51, 0:01:20 a 0:01:34).
- Frameworks encapsulam experiência coletiva (aula 51, 0:01:49 a 0:01:55).

Código: nenhum.

Citações (paráfrases de legenda, não verificadas):
- A web funciona transitando mensagens de texto uma em cima da outra, via protocolo HTTP (aula 51, 0:01:03).
- Dedicar a grande maioria da atenção ao que é específico do seu projeto (aula 51, 0:01:29).
- É muito importante você ganhar agilidade e produtividade (aula 51, 0:01:39).

### Aula 52: Qual a diferença entre Pyenv e Virtualenv?
Vídeo: https://www.youtube.com/watch?v=DSNokXsZ9Xk · Duração: 2:07

Resumo: As duas ferramentas são complementares apesar de fazerem coisas diferentes (aula 52, 0:00:08 a 0:00:12). O `pyenv` serve para instalar e controlar quais interpretadores Python há na máquina, como 3.7 e 2.7 ou Anaconda (aula 52, 0:00:25 a 0:01:12). O `virtualenv` isola as dependências do projeto e evita conflito de versões de bibliotecas, como versões diferentes do Django (aula 52, 0:00:19 a 0:00:24; 0:01:15 a 0:01:48). Ele também diz que não é legal usar o Python do sistema (aula 52, 0:00:40 a 0:00:46).

Linha do tempo:
- [0:00:08] Comum confundir as duas ferramentas pelo nome; são complementares.
- [0:00:14] O `virtualenv` já vem disponível com o Python e isola dependências do projeto.
- [0:00:25] O `pyenv` permite instalar e controlar mais facilmente os interpretadores Python da máquina.
- [0:00:40] Não é legal usar o Python do sistema.
- [0:00:49] Exemplo: ter 3.7 e 2.7 instalados; também Anaconda.
- [0:01:15] O `virtualenv` é focado no projeto: cria-se um por projeto, sobre o interpretador escolhido.
- [0:01:38] Evita conflito de versões das bibliotecas entre projetos (exemplo com o Django).

Princípios:
- `pyenv` gerencia interpretadores; `virtualenv` gerencia dependências por projeto (aula 52, 0:00:19 a 0:00:32; 0:01:15 a 0:01:38).
- Não use o Python do sistema para trabalhar (aula 52, 0:00:40 a 0:00:46).
- Um ambiente virtual por projeto evita conflito de versões (aula 52, 0:01:38).

Código: nenhum.

Citações (paráfrases de legenda, não verificadas):
- É muito comum confundir essas duas ferramentas pelo nome, elas são complementares (aula 52, 0:00:08).
- Não é legal usar o Python do sistema (aula 52, 0:00:43).
- Isso evita conflito de versões (aula 52, 0:01:38).

### Aula 53: Não economize pull request
Vídeo: https://www.youtube.com/watch?v=ilqsg9SXXKA · Duração: 4:32

Resumo: Como mantenedor de projetos open source, ele recebeu um e-mail de alguém com uma ideia e uma necessidade específica que queria só mandar o pull request, não abrir uma discussão (aula 53, 0:00:14 a 0:00:52). Ele considera essa visão limitada: só consegue avaliar a ideia com código e não vê sentido em economizar o esforço de abrir uma issue pública para discutir (aula 53, 0:00:53 a 0:01:46). Vê a postura como utilitarista e como otimização de esforço que joga trabalho para os outros (aula 53, 0:02:10 a 0:03:20). A reflexão final é que quem usa um projeto deve se responsabilizar pelo que usa e não pode economizar esse esforço (aula 53, 0:03:50 a 0:04:26).

Linha do tempo:
- [0:00:14] Recebeu e-mail de alguém sobre uma biblioteca dele.
- [0:00:42] A pessoa tem uma ideia e uma necessidade, mas só quer mandar o pull request.
- [0:00:53] Vê essa visão como limitada e equivocada sobre como funciona o open source.
- [0:01:37] Sugere abrir a ideia publicamente para discutir, em vez de e-mail pessoal.
- [0:02:07] Percebe a postura como utilitarista: ele só mandaria o código se ele aceitasse a mudança.
- [0:02:17] Se o pull request não for aceito e resolver o problema, a pessoa usa a própria versão.
- [0:02:50] Vê otimização de esforço que gera trabalho para os outros.
- [0:03:50] Reflexão: temos que nos responsabilizar pelas coisas que usamos.
- [0:04:07] Constrói-se em cima do que os outros fizeram colaborativamente, mas o responsável pelo projeto é quem o mantém.
- [0:04:23] Se eximir de responsabilidade não rola.

Princípios:
- Discuta a ideia publicamente antes ou junto com o código; evite só despejar um pull request (aula 53, 0:01:37 a 0:01:46).
- Quem usa software de terceiros deve se responsabilizar pelo que usa (aula 53, 0:03:50 a 0:03:57).
- Não há como economizar o esforço de manter; o mantenedor também tem trabalho (aula 53, 0:04:12 a 0:04:16).

Código: nenhum.

Citações (paráfrases de legenda, não verificadas):
- Eu só consigo avaliar a ideia com código, não só com um conceito legal (aula 53, 0:01:06) [legenda: avaliar o código com código].
- A gente tem que se responsabilizar pelas coisas que está usando (aula 53, 0:03:50).
- Eximir de responsabilidade não rola (aula 53, 0:04:23).

## 6. Princípios que atravessam toda a série

Dezoito regras que ele formula na fala. Nenhuma é inferência deste documento. Em aulas de legenda ruidosa (47, 48, 50, 51, 52) o princípio vem do que a legenda deixa ler.

#### 1. Rodar cedo e iterar

A pior coisa que se faz com o código é não botar para rodar, porque a primeira versão nunca é boa (aula 1, 0:00:06). A qualidade veio por interação e lapidação (aula 1, 0:01:24). Se o caminho está difícil, volta e simplifica (aula 1, 0:00:44 a 0:00:46).

#### 2. Até funcionar, tudo é hipótese

Não dá para achar que se sabe algo até o código funcionar (aula 3, 0:00:33). Tudo que se acha sobre a solução só é aprovado com o código rodando vivo (aula 15, 0:03:38 a 0:03:51). A técnica serve ao ciclo de feedback (aula 3, 0:00:48 a 0:00:56).

#### 3. Ponta a ponta antes de genérico e bonito

O objetivo é fazer alguma coisa, não terminar tudo (aula 13, 0:00:09). Faz de ponta a ponta, o genérico bonito não importa (aula 13, 0:02:27). O tempo é uma restrição de escopo (aula 13, 0:02:04). Primeiro o caso de sucesso rodando, depois melhorar (aula 16, 0:00:17 a 0:00:33), com o escopo mínimo que entrega os 20 por cento (aula 16, 0:00:48).

#### 4. Cresça de um caso simples e não prepare o futuro

Uma música, depois duas e três, aumentando a heurística (aula 15, 0:01:08). Não gastar energia preparando um futuro que ainda não chegou (aula 15, 0:02:29). Começar pelo núcleo e pela heurística, sem dependências pesadas (aula 14, 0:02:18 a 0:02:27).

#### 5. Modele o negócio com objetos simples e deixe o banco para depois

Começar pelo teste e por uma lista em memória (aula 4, 0:02:29 a 0:02:47). Modelar a lógica de negócio com objetos simples e só depois trocar por modelos (aula 4, 0:03:15 a 0:03:30). Começar pelo banco é olhar para o estado, e o que importa são as transições (aula 4, 0:03:41 a 0:04:15). Camadas com contrato estável deixam mexer no armazenamento sem tocar a regra (aula 4, 0:04:45 a 0:05:31).

#### 6. O teste mais simples primeiro, junto da solução

Começar com um assert no arquivo e completar a função até passar (aula 7, 0:00:51 a 0:01:07). Desenvolver em cima do mesmo teste, sem trocar de arquivo (aula 7, 0:01:23 a 0:01:52).

#### 7. A dificuldade do teste revela o que não se sabe

O teste dói porque revela o que não se sabe (aula 10, 0:00:34). Fazer o teste primeiro obriga outro design, pode custar de quatro a cinco vezes mais tempo e mostra os limites das camadas (aula 10, 0:00:44 a 0:01:07). O teste exige código passível de mudança (aula 10, 0:01:32 a 0:01:37).

#### 8. Errado é o problema errado, não o código feio

É muito mais caro fazer a coisa errada do que não fazer nada (aula 11, 0:01:54 a 0:02:05). O errado é gastar energia no problema errado, uma falha de percepção de valor (aula 11, 0:02:07 a 0:02:22).

#### 9. Sem regra fixa para testar, bom senso e previsibilidade

Não há regra, há bom senso da experiência (aula 18, 0:00:13). Função chamada em muitos lugares precisa de comportamento previsível (aula 18, 0:01:24 a 0:01:48). Prefere código plano e linear (aula 18, 0:00:54). A unidade de teste é dinâmica e cresce com o código (aula 18, 0:02:23 a 0:02:35).

#### 10. O código abraça a mudança e a negocia com o passado

Código que abraça a mudança, com esforço localizado (aula 2, 0:00:28 a 0:00:53). Não comprar mudança com casos especiais que violem o design (aula 2, 0:01:28 a 0:01:33). Cada mudança negocia com o passado em prol de um futuro (aula 30, 0:01:38 a 0:01:54).

#### 11. Fazer funcionar, fazer direito, fazer rápido se precisar

Nessa ordem (aula 30, 0:01:59 a 0:02:08). Parar em fazer funcionar acumula débito técnico (aula 30, 0:02:08 a 0:02:18). Subir ao nível simbólico, compreender a execução e o impacto, em vez de colecionar ferramentas (aula 30, 0:02:44 a 0:03:09).

#### 12. Tratar a urgência em duas etapas e comunicar o efeito colateral

Estancar o sangramento agora e fazer a cirurgia reparadora depois (aula 40, 0:01:45 a 0:01:58). O mais importante é comunicar o efeito colateral da estratégia (aula 40, 0:01:20 a 0:01:45). Quem decide não reparar sabe que a conta técnica chega (aula 40, 0:02:09 a 0:02:18).

#### 13. Reescrever é outro projeto

Mudar tecnologia, arquitetura e escopo é fazer outro projeto, com planilha e orçamento (aula 31, 0:00:52 a 0:02:21). Jogar o legado fora e recomeçar do zero é muito caro (aula 27, 0:02:19 a 0:02:23). O trabalho do programador é gerenciar risco (aula 31, 0:02:49 a 0:03:00).

#### 14. A menor mudança que aumenta a capacidade

A menor mudança possível para aumentar a capacidade sem aumentar a quantidade de código (aula 27, 0:01:41 a 0:01:58). Entender o problema do cliente antes de executar o pedido (aula 27, 0:01:15 a 0:01:36).

#### 15. Exceção específica, bloco pequeno

Tratar a exceção mais específica possível, nunca a base, por causa da hierarquia (aula 20, 0:01:13 a 0:01:47). Diminuir o corpo do bloco de tratamento (aula 20, 0:01:57 a 0:02:13). Com exceções o código fica mais linear (aula 20, 0:00:50 a 0:01:11).

#### 16. Migração caminha junto com o código

Esquema e estado do banco são parte do código (aula 22, 0:00:42 a 0:00:53). Gerar a migração antes do commit, casada com a mudança (aula 22, 0:02:57 a 0:03:23).

#### 17. Use o framework, não o abstraia

A vantagem do desacoplamento é intervir, não trocar (aula 33, 0:00:17 a 0:00:29). Abstrair o framework é o que ele não faz de jeito nenhum (aula 33, 0:01:28 a 0:01:41). Tudo é biblioteca (aula 41, 0:00:15). Não construir o framework antes do sistema (aula 50, 0:00:14 a 0:00:29).

#### 18. Padrões emergem, o problema vem primeiro

Resolver o problema, ter uma primeira versão funcionando e depois refletir sobre a organização (aula 39, 0:00:45 a 0:00:59). Os padrões emergem (aula 39, 0:01:01). O foco é sempre resolver o problema primeiro (aula 39, 0:01:26).

Princípios de ofício e de carreira que não viram regra de código, mas que ele formula com a mesma firmeza: assumir mais responsabilidade, ampliar a capacidade e renegociar quando a função prometida não é a real (aula 29, 0:01:37 a 0:02:23); subir a abstração e resolver o problema das pessoas, em vez de competir com a máquina (aula 32, 0:02:41 a 0:05:05); registrar o trabalho na hora (aula 6, 0:00:42 a 0:00:56); alternar foco e desfoco (aula 9, 0:00:39 a 0:00:54); escrever requisito em frases curtas (aula 17, 0:00:47 a 0:00:55); praticar em 80 por cento do tempo (aula 38, 0:03:15 a 0:03:21); começar da menor versão do que se quer (aula 49, 0:02:12 a 0:02:38); responsabilizar-se pelo que se usa (aula 53, 0:03:50 a 0:03:57).

## 7. Citações-chave do curso

Paráfrases de legenda automática, sem aspas e não verificadas contra o vídeo.

| Aula | Timestamp | Paráfrase |
|---|---|---|
| #1 | 0:00:06 | a pior coisa que você pode fazer com o código é não botar para rodar porque a primeira nunca é boa |
| #2 | 0:00:28 | eu preciso fazer um código que abraça a mudança |
| #3 | 0:00:33 | não dá para achar que sabe nada sobre hipótese até o código funcionar |
| #4 | 0:03:54 | começar um projeto pelo banco de dados é olhar para o estado |
| #5 | 0:02:09 | o que gera liderança é presença |
| #6 | 0:00:31 | a memória não é um HD, ela é relacional |
| #10 | 0:00:34 | teste dói para fazer porque ele revela tudo que você não sabe |
| #10 | 0:01:44 | se você não tem tempo para fazer bem feito, quando você vai arrumar tempo para fazer de novo |
| #11 | 0:01:54 | é muito mais caro fazer a coisa errada do que não fazer nada |
| #13 | 0:02:27 | faz de ponta a ponta, não importa se está genérico e bonito |
| #15 | 0:03:40 | tudo que eu acho que sei sobre a solução é uma mera hipótese, só aprovada com o código rodando vivo |
| #18 | 0:00:13 | não tem uma regra, mas existe um bom senso que você adquire com a experiência |
| #20 | 0:01:29 | é importante ser muito específico, porque existe uma hierarquia de exceções |
| #21 | 0:00:22 | encapsulamento é um conceito à parte |
| #22 | 0:03:19 | eu não faço isso depois, eu faço combinado, casadinho |
| #25 | 0:01:16 | usar Mock demais é sinal de código muito acoplado |
| #27 | 0:01:49 | qual a menor mudança que aumenta a capacidade do software sem aumentar a quantidade de código |
| #29 | 0:01:35 | quanto mais responsabilidade você assumir, melhor |
| #30 | 0:01:38 | cada vez que você muda um código, você negocia com o passado em prol de um futuro |
| #31 | 0:04:17 | o software não é legado, ele só está dando dinheiro há muito tempo |
| #32 | 0:04:55 | o trabalho do programador é resolver o problema das pessoas, não escrever código |
| #33 | 0:00:17 | a vantagem de ser desacoplável é poder intervir, não trocar as coisas |
| #34 | 0:00:49 | você não começa do zero, você começa de onde está |
| #38 | 0:01:06 | em programação você aprende programando, não lendo o livro |
| #39 | 0:01:01 | os padrões emergem |
| #40 | 0:01:24 | o mais importante é comunicar o efeito colateral |
| #44 | 0:01:53 | nada vai ser tão poderoso quanto programar |
| #49 | 0:02:29 | qual é a menor versão disso, a coisa mais simples |
| #53 | 0:03:50 | temos que nos responsabilizar pelas coisas que usamos |

## 8. A evolução técnica, aula a aula

A série não segue uma ordem didática; as aulas são recortes avulsos. A tabela agrupa por tema, na ordem em que aparecem.

| Etapa | O que é feito | Conceito ou ferramenta | O que isso destrava |
|---|---|---|---|
| **#1 a #3** | Rodar cedo, mudança, hipótese (0:00:06 a 0:01:36) | frozenset [leitura], iteração, ciclo de feedback | Primeira versão ruim é normal; tudo é hipótese (aula 3, 0:00:33) |
| **#4 a #8** | Modelagem por testes, iniciativa, registro, testes em desafios, plano que muda (0:00:16 a 0:06:35) | lista em memória, assert, camada de serviço | Banco depois; teste junto da solução (aula 4, 0:03:15; aula 7, 0:01:23) |
| **#9 a #14** | Foco, teste que dói, errado é caro, aprender sem resultado, ponta a ponta, bagagem (0:00:09 a 0:03:43) | convergência e divergência, pomodoro, time-box de horas | Escopo mínimo de ponta a ponta (aula 13, 0:02:27) |
| **#15 a #18** | Hipótese, 20 por cento, português, o que testar (0:00:05 a 0:05:41) | heurística, frases curtas, árvore de execução | Crescer de um caso; código linear e previsível (aula 15, 0:01:08; aula 18, 0:00:54) |
| **#19 a #21** | Linguagem nova, exceções, controle de acesso (0:00:26 a 0:03:47) | variabilidade, hierarquia de exceções, encapsulamento | Exceção específica; risco de aprender dentro do projeto (aula 20, 0:01:13; aula 19, 0:00:32) |
| **#22 a #26** | Migrações, escala, Decouple, Mock, pensamento Pythônico (0:00:06 a 0:02:54) | migrations, cache, CDN, Redis, Mock | Migração casada; perfil de uso; API simples (aula 22, 0:03:19; aula 23, 0:00:32; aula 24, 0:00:18) |
| **#27 a #31** | Software vivo, views, responsabilidade, mudança, reescrita (0:00:14 a 0:04:28) | metáfora do médico, dívida técnica, testes de regressão | Menor mudança possível; reescrever é outro projeto (aula 27, 0:01:41; aula 31, 0:00:52) |
| **#32 a #36** | Python para iniciantes, Django desacoplável, idade, operação, interior (0:00:00 a 0:05:10) | garbage collector, ORM, pytest, Heroku | Subir a abstração; usar o framework; plataforma como serviço (aula 32, 0:03:51; aula 33, 0:01:28; aula 35, 0:01:30) |
| **#37 a #41** | Rotas, estudo errado, patternite, mudança rapidinha, app (0:00:00 a 0:04:23) | urlpatterns, classe de URL, cirurgia em duas etapas | Rotas compostas pelo modelo; padrões emergem (aula 37, 0:01:03; aula 39, 0:01:01) |
| **#42 a #46** | WordPress, lógica, no-code, funciona na minha máquina, Python é amor (0:00:03 a 0:03:38) | Zapier, Lambda, prints e vídeos | Valor antes de tecnologia; custo de coordenação (aula 42, 0:00:05; aula 44, 0:02:17) |
| **#47 a #49** | Dicas de estudo, software de verdade, lógica primeiro (0:00:31 a 0:07:07) | diário de estudo, arquivo de referências | Menor versão do que se quer (aula 49, 0:02:12) |
| **#50 a #53** | Framework, pyenv e virtualenv, pull request (0:00:08 a 0:04:26) | HTTP, pyenv, virtualenv, issue e pull request | Não construir o framework antes; responsabilidade sobre o que se usa (aula 50, 0:00:14; aula 53, 0:03:50) |

## 9. Arsenal técnico demonstrado no curso

Nenhuma ferramenta é mostrada na tela de forma audível; o arsenal é o que ele nomeia ou descreve.

| Técnica ou recurso | Para que ele usa | Aula e timestamp |
|---|---|---|
| frozenset [legenda: Frozen sete] | Estrutura imutável, escolhida depois de achar ruim o caminho com dicionários | #1, 0:01:06 a 0:01:19 |
| assert no arquivo [teste de pobre] | Primeiro teste, desenvolvido junto da função | #7, 0:00:51 a 0:01:23 |
| Lista em memória | Guardar recursos sem banco, para focar na regra | #4, 0:02:29 a 0:02:47 |
| Registro de trabalho | Cinco a dez minutos antes do fim para sintetizar decisões | #6, 0:00:42 |
| Pomodoro com ritual | Ajudar a criar o hábito | #11, 0:01:16 |
| Exceção específica | Evitar capturar a base e controlar o corpo do bloco | #20, 0:01:13 a 0:02:13 |
| Migração gerada antes do commit | Alinhar a versão do código com a do banco | #22, 0:02:57 a 0:03:23 |
| Ferramenta de testes sem migrações [legenda: Jungle Test Without Migrations] | Rodar testes sem aplicar as migrações | #22, 0:02:57 a 0:03:06 |
| Cache do que é público, CDN, índices, Redis para sessão | Escalar com uso eficiente de recursos | #23, 0:01:19 a 0:01:51 |
| Decouple | Biblioteca de configuração que ele criou, com API simples e extensível | #24, 0:00:00 a 0:00:27 |
| Mock | Fingir um objeto e registrar chamadas, valores e alterações | #25, 0:00:49 a 0:01:03 |
| Script Python que inicializa o Django | Processamento em segundo plano, no lugar de comandos de gerenciamento | #33, 0:00:38 a 0:01:01 |
| pytest | Em vez do framework de testes padrão | #33, 0:01:06 a 0:01:13 |
| ORM com SQL direto quando preciso | Usar o ORM sempre, estendendo-o | #33, 0:01:47 a 0:02:15 |
| Classe que compõe urlpatterns | Um objeto representa muitas rotas | #37, 0:00:49 a 0:01:38 |
| Copiar código linha por linha | Estudar rodando, sem copiar e colar | #38, 0:02:22 a 0:02:53 |
| Lambda e Zapier | Código na Lambda quando o Zapier vira costura | #44, 0:01:22 |
| Prints e vídeos do sistema funcionando | Responder ao funciona na minha máquina | #45, 0:00:00 a 0:00:14 |
| Diário de estudo e arquivo de referências | Rastrear aprendizado e guardar achados com link e motivo | #47, 0:01:59 a 0:02:26; 0:05:43 a 0:06:15 |
| Time-box de meia hora | Tentar progredir; se travar, dividir | #47, 0:04:21 |
| pyenv | Instalar e controlar os interpretadores da máquina | #52, 0:00:25 a 0:01:12 |
| virtualenv | Um ambiente por projeto, evitando conflito de versões | #52, 0:01:15 a 0:01:48 |
| Heroku ou plataforma como serviço | Delegar a operação em equipe pequena | #35, 0:01:30 |
| Issue pública antes do pull request | Discutir a ideia em aberto | #53, 0:01:37 |

## 10. Glossário do curso

| Termo | Significado no contexto da série | Onde |
|---|---|---|
| **Variabilidade** | A distância entre a necessidade do projeto e a bagagem de quem o faz | #19, 0:00:26 a 0:00:42 |
| **Programação com sotaque** | Código em uma linguagem com cacoetes de outra | #19, 0:04:13 |
| **Encapsulamento** | Conceito à parte do controle de acesso | #21, 0:00:20 a 0:00:34 |
| **Controle de acesso** | Público, privado e protegido; origem na venda de componentes sem código-fonte | #21, 0:00:56 a 0:01:56 |
| **Perfil de uso** | Natureza, comportamento no tempo e relação com os usuários, com sazonalidade e picos | #23, 0:00:32 a 0:01:07 |
| **Lei de Zawinski** | Todo software cresce ao ponto de ser capaz de mandar e-mail; ele a cita ao resistir a inflar o Decouple | #24, 0:02:04 a 0:02:22 |
| **Nível sintático, semântico e simbólico** | Níveis de compreensão da programação | #26, 0:00:13 a 0:00:44; #30, 0:02:44 |
| **Software vivo** | Software com gente usando, sem reboot nem reset | #27, 0:00:54 a 0:01:06 |
| **Débito técnico** | O que se acumula parando em fazer funcionar | #30, 0:02:08 a 0:02:18 |
| **Legado** | Software que dá dinheiro há muito tempo | #31, 0:04:17 |
| **Patternite** | Querer aplicar padrões antes de resolver o problema. A legenda ouve paternik | #39, 0:00:02 a 0:00:25 |
| **Cirurgia reparadora** | A segunda etapa de uma emergência, planejada | #40, 0:01:02 a 0:01:58 |
| **Repertório** | O que falta a quem diz não ter lógica; vem de experimentar e errar | #43, 0:00:11 a 0:00:24; 0:01:48 |
| **Custo de coordenação** | O que explode entre ferramentas externas que não se controlam | #44, 0:02:17 a 0:02:37 |
| **Software de verdade** | O imaginário da época do que é um programa de sucesso, que desvia o foco | #48, 0:00:15 a 0:00:43 |
| **Framework** | Conjunto de padrões recorrentes de uma área, com funções de mais alto nível | #51, 0:00:26 a 0:00:47 |
| **Funciona na minha máquina** | Uma das desculpas mais esfarrapadas do programador | #45, 0:00:14 a 0:00:22 |

## 11. Perguntas e respostas que o curso responde

#### Qual a pior coisa que se pode fazer com um código?

Não botar para rodar, porque a primeira versão nunca é boa (aula 1, 0:00:06).

#### Como tratar o que se acha que se sabe?

Como hipótese até o código funcionar (aula 3, 0:00:33; aula 15, 0:03:38).

#### Por onde começar um sistema com banco?

Pelo teste e por objetos simples em memória, deixando o banco para depois (aula 4, 0:02:29, 0:03:15).

#### Existe regra para identificar o código que precisa de teste?

Não, existe bom senso da experiência; função chamada em muitos lugares precisa ser previsível (aula 18, 0:00:13, 0:01:24).

#### Como usar tratamento de exceção do jeito certo?

Específico, nunca a base, com bloco pequeno (aula 20, 0:01:13 a 0:02:13).

#### Python sem controle de acesso quer dizer sem encapsulamento?

Não. Encapsulamento é um conceito à parte (aula 21, 0:00:20 a 0:00:34).

#### Como trabalhar com migrações?

Tratar o esquema como parte do código e gerar a migração antes do commit (aula 22, 0:00:42, 0:02:57).

#### O que fazer para um sistema Django não sair do ar com muitos acessos?

Conhecer o perfil de uso, cachear o público, usar CDN, índices e Redis (aula 23, 0:00:32, 0:01:19).

#### Como verificar um efeito colateral que não aparece na saída?

Com um Mock, sem abusar, porque muito Mock indica acoplamento (aula 25, 0:00:49, 0:01:16).

#### As views do Django são controllers?

A analogia só vale como alegoria; view controla o conteúdo, template a apresentação, e a view fica pequena (aula 28, 0:00:08, 0:00:42, 0:01:18).

#### Como lidar com mudanças no código?

Negociar com o passado, fazer funcionar, fazer direito, fazer rápido se precisar (aula 30, 0:01:38, 0:01:59).

#### Sistema velho precisa ser refeito?

Reescrever é outro projeto, com orçamento e risco; para o legado há regressão, refatoração e intervenções pontuais (aula 31, 0:00:52, 0:03:51).

#### Faz sentido trocar partes no Django?

O valor é intervir, não trocar; ele não abstrai o framework nem o ORM (aula 33, 0:00:17, 0:01:28).

#### O que fazer quando o chefe pede uma mudança rapidinha?

Entender a necessidade, comunicar o efeito colateral e tratar em duas etapas (aula 40, 0:00:24, 0:01:20, 0:01:45).

#### Por que ele usa WordPress no site?

Tecnologia é para resolver problema; um site simples já está resolvido, e Python e Django ficam para os bastidores (aula 42, 0:00:05, 0:01:07).

#### É preciso aprender lógica antes de programar?

A lógica vem da prática; parta do que se quer fazer e da menor versão disso (aula 49, 0:00:37, 0:02:12; aula 43, 0:00:11).

#### Devo programar na mão ou usar um framework?

Não construir o framework antes do sistema, ler o código livre para entender, evitar os dois extremos (aula 50, 0:00:14, 0:00:46, 0:01:56).

#### Qual a diferença entre pyenv e virtualenv?

O pyenv controla os interpretadores; o virtualenv isola as dependências por projeto (aula 52, 0:00:25, 0:01:15).

#### Quem tem 30 anos começa tarde?

Ninguém começa do zero, começa de onde está; nunca é tarde (aula 34, 0:00:49, 0:01:57).

#### Posso mandar só o pull request?

Ele vê a postura como limitada; abrir a ideia publicamente e se responsabilizar pelo que usa (aula 53, 0:00:53, 0:01:37, 0:03:50).

## 12. Repositórios e recursos

| Recurso | Onde encontrar | Observação |
|---|---|---|
| Playlist completa (fonte desta documentação) | [Dicas de Programação](https://www.youtube.com/playlist?list=PLeKXYyZCJHxdnGoV8TBYzKqsm8p3PIEeQ) | 53 vídeos. Os ids estão em `playlist.json` e nos links da seção 5. |
| Canal | [HB Network](https://www.youtube.com/@hbnetworkoficial) | |
| Decouple | sem URL nesta fala | Aula 24, 0:00:00 a 0:02:22: biblioteca dele, publicada como Django Decoupled e depois generalizada para Flask por conselho de Felipe Cruz (0:01:08 a 0:01:26). O digest do repositório está em `kb/repos/python-decouple.md`. |
| Ferramenta de testes sem migrações | sem URL nesta fala | Aula 22, 0:02:57 a 0:03:06: nome ouvido como Jungle Test Without Migrations, leitura não confirmada. O digest do repositório está em `kb/repos/django-test-without-migrations.md`. |
| Servidor para os alunos [legenda: Heriki] | citado, sem URL | Aula 24, 0:01:31 a 0:01:53: um servidor com a dinâmica do Heroku, para os alunos publicarem a aplicação no primeiro dia. Grafia incerta. |
| Curso de Python (legenda: Pythonando) | citado, sem URL | Aula 20, 0:02:44: ele indica a aula do curso sobre modelagem mental de objetos e tratamento de exceção. Nome do curso incerto. |
| Zawinski, Netscape | citado, sem URL | Aula 24, 0:02:04 a 0:02:22. Referência a uma lei, sem título de texto. |
| Comunidade de Belém | citada, sem URL | Aula 36, 0:00:19 a 0:00:28. Nomes incertos na legenda. |

Repositórios do curso: **nenhum URL nesta série**. Esta documentação não foi ao GitHub procurá-los.

## 13. Análise linha a linha do código real

O curso não publica código com caminho, commit ou URL, portanto não há análise de código real. Nenhuma aula mostra código na tela de forma audível (partes 1 a 3 do passo por aula: o campo de código de cada lição diz nenhum, ou descreve só uma ideia). Limites que ficam registrados:

- A aula #1 menciona um frozenset [legenda: Frozen sete] e um Frozen dict, sem trecho reconstruível (0:01:06, 0:01:16).
- A aula #7 descreve asserts no começo do arquivo e não dita sintaxe (0:00:51, 0:00:59 a 0:01:04).
- A aula #20 cita o padrão de pegar a exceção base, sem soletrar nome de classe [legenda: base deck 7] (0:01:20).
- A aula #37 descreve uma classe que computa as URLs a partir do modelo, só por ideia (0:01:03 a 0:01:38).
- Os repositórios que ele cita (Decouple, aula 24; ferramenta de testes sem migrações, aula 22) têm digest em `kb/repos/`, mas esta documentação não os lê a partir do curso.

## 14. Execução real dos testes

O curso não publicou código nem suíte. Não há o que rodar. Nenhuma reconstrução de código foi feita nesta documentação, porque nenhuma aula dita sintaxe suficiente para isso.

---

Documentação elaborada a partir das transcrições das 53 aulas da playlist Dicas de Programação, de Henrique Bastos (HB Network), playlist `PLeKXYyZCJHxdnGoV8TBYzKqsm8p3PIEeQ`, legendas capturadas em 2026-10-10. Quarenta e duas aulas vêm de legenda automática em português (pt-orig); as aulas 22 a 26, 30, 32, 33, 38, 46 e 49 vêm de transcrição Whisper pontuada. As aulas 47, 48, 50, 51 e 52 têm legenda ruidosa e vêm sinalizadas onde são usadas. As citações são paráfrases das transcrições, não verificadas contra o vídeo (`verified: false`), renderizadas sem aspas e com os erros de reconhecimento anotados entre colchetes quando precisam aparecer. O curso não publica código nem URL de repositório nesta transcrição. Datas de publicação e visualizações não foram coletadas. Conteúdo de caráter educativo.
