<!-- written by the henrique-ingest distiller on 2026-10-22 from sources/transcripts/ia-como-veiculo-de-expressao/; see kb/courses/README.md for provenance and license -->

Canal Henrique Bastos · Documentação de episódio

# IA como veículo de expressão, mais do que ferramenta

Um único vídeo, lido a partir da legenda automática: a primeira conversa gravada entre Henrique Bastos e Alisson Vale, que conversam há 20 anos, sobre o que cada um tem feito com IA. Não é aula nem curso de código. Henrique conta o estado atual dos agentes dele (agentes duráveis, um proxy de MCP com um toolkit por agente, code mode, um home lab que concentra fatos numa timeline) e insiste que o que importa são os padrões, não as ferramentas nem os produtos. Alisson dá nome aos conceitos: a floresta contra o zoológico, a IA como veículo de expressão, inteligência composicional, o centro estável, o campo agêntico. Os dois terminam num problema em aberto: como pessoas e agentes trabalham juntos.

Conversa: **Henrique Bastos** e **Alisson Vale** · Canal [Henrique Bastos](https://www.youtube.com/channel/UCaL1P7zI_1B6mRjMqcxq0Yg) · Vídeo: [#1 IA como veículo de expressão, mais do que ferramenta](https://www.youtube.com/watch?v=2VQ58dqC12k) · Repositório: nenhum (a conversa não tem código)

Documento elaborado a partir da transcrição do vídeo (legenda automática em português, pt-orig, capturada em 2026-10-22). O vídeo é do canal pessoal dele, não do HB Network, e não pertence a playlist; é tratado como lição 1 de um curso de uma lição só, e todo timestamp neste documento se refere a ele. São **duas vozes**, e só a fala de Henrique é atribuída a ele em princípios e citações. A legenda marca a troca de turno com `>>`; a atribuição seguiu essas marcas e o conteúdo (Alisson se apresenta em 0:00:30, Henrique o chama pelo nome em 0:33:35, e cada um descreve o próprio ambiente). Trechos de Henrique: 0:02:23 a 0:03:24, 0:03:32 a 0:05:58 (com uma intervenção de Alisson em 0:03:59), 0:06:04 a 0:07:43, 0:08:20 a 0:08:40, 0:08:56 a 0:12:14, 0:16:56 a 0:22:31, 0:24:59 a 0:27:57, 0:33:35 a 0:39:52, 0:41:45 a 0:42:36, 0:49:02 a 0:54:34, 0:57:23 a 1:01:38, 1:02:00 a 1:04:14, 1:08:43 e 1:08:46 a 1:08:52, 1:11:13 a 1:12:21, 1:13:18 a 1:16:36 e 1:17:37 a 1:23:06 (com uma pergunta de Alisson em 1:22:18). Os trechos de 0:00:00 a 0:00:29 são recortes do próprio episódio, usados como abertura, e repetem falas de 0:51:31, 0:17:37, 1:17:41, 0:30:46 e 1:15:03. O trecho de 1:16:37 a 1:16:57 tem a troca de turno incerta e não é citado. Familiares de Henrique aparecem só pelo papel.

## 1. Visão geral do curso

É um vídeo de **5.017 segundos, 1 hora, 23 minutos e 37 segundos**, gravado em 18 de outubro de 2026 e publicado em 21 de outubro de 2026, segundo a descrição. Alisson abre propondo um centro mais estável de conversas num ambiente volátil (0:01:10 a 0:01:33). Henrique começa pelo estado atual: agentes duráveis mudaram tudo nas últimas duas semanas (0:04:13 a 0:05:20). A conversa passa pela floresta contra o zoológico (0:12:16 a 0:19:55), pela IA como arte (0:23:14 a 0:33:33), pelos padrões que Henrique extrai do home lab (0:33:35 a 0:39:52), pela inteligência composicional (0:44:52 a 0:45:19), pelo centro estável (0:54:34 a 0:57:22), pela linguagem de domínio (0:59:43 a 1:04:14) e pelo campo agêntico (1:04:35 a 1:11:13), e fecha no caso Amp de pessoas e agentes trabalhando juntos (1:17:37 a 1:23:29).

| Dimensão | Valor | Observação |
|---|---|---|
| Lições | 1 | Vídeo avulso, numerado #1 no título; a descrição diz que é a primeira de uma série de conversas. |
| Duração total | 5.017 s (1h 23min 37s) | Metadado do vídeo. |
| Data | gravado em 2026-10-18, publicado em 2026-10-21 | Descrição e `upload_date`. |
| Visualizações | 130 | Na captura de 2026-10-22, um dia após a publicação. |
| Transcrição | 1 de 1 disponível | Legenda automática (pt-orig). A descrição traz 21 capítulos e uma lista de links na ordem em que aparecem. |
| Formato | conversa entre dois | Sem slides nem código na tela citados na fala; Henrique menciona um diagrama que publicou no X (0:20:35 a 0:20:41). |
| Versão em áudio | podcast Segue o Flow, de Alisson | Link na descrição. |
| Legenda ruidosa | nomes de ferramentas | pi-durable sai Pi Durable, PyTurbel, pai turbo, pai do Rubo e PyTorch (0:04:32; 0:08:59; 0:10:05; 0:20:15; 0:43:56); Petrus sai Petros e Petrous (0:05:23; 0:44:00); Amp sai Emp e REM (0:19:13; 0:00:14); Mirror sai Miro (0:22:39); Ariad sai Ariadne (1:02:02). Lista completa na seção 13. |
| Código | nenhum | Não há código escrito nem mostrado. As seções 13 e 14 dizem que não há o que analisar nem rodar. |

Nota de método: cada afirmação traz timestamp. As citações são paráfrases de legenda, sem aspas, não verificadas contra o vídeo. Mis-hearings ficam entre colchetes. Ideias de Alisson são atribuídas a ele pelo nome e não entram como princípios de Henrique. Nomes de ferramentas seguem a lista de links da descrição quando a legenda os deforma.

## 2. Filosofia e método de ensino

### 2.1 Uma conversa entre dois modos de pensar

A descrição define os papéis: Alisson pensa de cima para baixo, dá nome aos conceitos e desenha mapas; Henrique pensa de baixo para cima, experimenta, constrói e procura o padrão que aparece no fazer. A conversa confirma a divisão. Henrique diz que funciona todo embolado e que, compartilhando os padrões, talvez Alisson consiga destilar conceitos mais claros (0:34:12 a 0:34:23). Ele explica por que quis a conversa: sente falta de conversar com as pessoas para além das tools, num mar de ferramentas e produtos, e gosta de entender como a coisa funciona, para onde vai e o que faz sentido para ele (0:02:23 a 0:02:45). As conversas dos dois exploram ângulos diferentes com uma certa coesão de princípios e valores (0:02:47 a 0:03:02).

### 2.2 A própria prática como evidência

Henrique fala do próprio ambiente o tempo todo, com números: usa três ou quatro assinaturas que a empresa liberou, com um budget que ele aumenta e diminui (0:03:37 a 0:03:46); no mês anterior foram 16 bilhões de tokens, o que, diz ele, não significa nada, porque importa o que se produz com isso (0:03:53 a 0:04:05); classificou 3.000 e-mails numa execução só (0:10:52 a 0:12:01); mede a caixa d'água de casa com ultrassom a cada 5 minutos (0:35:53 a 0:36:01).

### 2.3 Experimentar, depois parar e procurar o padrão

Henrique diz que esfriou o uso depois de meses muito intensos de experimentação (0:03:12 a 0:03:24), que o foco não são os tokens e sim entender em que momento se está (0:04:05 a 0:04:15), e que desacelerou porque testava várias coisas ao mesmo tempo, estudando o design do que cada produto queria fazer (0:18:53 a 0:19:03). O que o encanta é buscar e analisar os padrões espalhados nas instâncias (0:39:18 a 0:39:52).

## 3. Pilares conceituais

### 3.1 Padrões, não produtos

O pilar de Henrique na conversa: os padrões são o que importa (0:33:57 a 0:34:04). Eles estão espalhados e instanciados, e o desafio é extraí-los; não são ferramenta nem produto, podem ser uma biblioteca, um trechinho de código, uma estratégia de código (0:39:20 a 0:39:36). O que vale alcançar é quais padrões fazem a diferença no universo com IA (0:39:36 a 0:39:49). Quando se repete, ele percebe: eu já fiz isso antes, e recruta das experiências anteriores primitivas, building blocks, legozinhos que se compõem e se rearrumam depois (0:52:12 a 0:52:41).

### 3.2 Floresta contra zoológico

Alisson propõe a floresta: em vez de ferramenta pontual, a IA é companhia contínua, e o esforço passa a ser organizar a floresta em que ela vive, com os projetos como trilhas (0:13:47 a 0:16:54). Henrique responde com o zoológico: as empresas estão todas tentando criar um produto para você viver dentro dele, e você sempre esbarra em limitações (0:17:37 a 0:17:49); o zoológico é fechado e pré-definido (0:17:59 a 0:18:07). Todo produto tem pressupostos de workflow, a adesão vira tudo ou nada, e o corner case do seu projeto vira workaround para se adequar ao design que alguém pré-concebeu (0:19:18 a 0:19:53).

### 3.3 O centro estável é uma estrutura feita para mudar

Henrique: a única constante é que muda muito, então a pergunta é como fazer as coisas privilegiando a mudança (0:53:42 a 0:53:57). Ele busca isso há mais de 20 anos, desde que tomou consciência da programação funcional, para trabalhar com a entropia, e agora virou pré-requisito na forma de usar IA (0:54:08 a 0:54:30). Alisson chama isso de referência de centro: uma estrutura estável por onde se passa, aberta para acoplar cada novidade (0:54:34 a 0:57:16). Alisson retoma no fim: o centro dele está estável mesmo que a tecnologia gire, ela só vai acoplando, encaixando, e Henrique concorda (1:11:06 a 1:11:15).

### 3.4 Antropocêntrico: como eu funciono é a base

Henrique diz que a prática dele é antropocêntrica: não está preocupado em aprender ferramenta para ser mais produtivo (0:25:17 a 0:25:30). Como ele funciona é a base onde as coisas começam (0:26:07 a 0:26:20): é péssimo para lembrar, precisa que as coisas cheguem até ele, é excelente quando muita gente o demanda e péssimo quando precisa verificar o que os outros fazem para coordenar (0:26:30 a 0:26:45). Isso dá o shape da solução, que tem de encaixar nele, e por isso só faz sentido compartilhar um conjunto de primitivas (0:26:47 a 0:27:12).

### 3.5 Sustentar a pergunta

Henrique tenta resistir ao máximo a fechar uma conclusão e quer sustentar a pergunta, coisa que influencia também na empresa (0:49:20 a 0:49:49). Ninguém tem a resposta de como encaixar a IA no que já se tem; o momento é pré-paradigmático, como quando se descobria qual era a forma certa de fazer software (0:49:51 a 0:50:39). Manter a pergunta aberta exige disciplina na execução dos experimentos, para que se adaptem e mudem, senão se passa o tempo inteiro refazendo tudo (0:51:12 a 0:51:26).

## 4. As aulas em uma tabela

| # | Título | Duração | Foco em uma linha |
|---|---|---|---|
| 1 | #1 IA como veículo de expressão, mais do que ferramenta | 1:23:37 | Agentes duráveis, toolkits por agente, timeline de fatos, floresta contra zoológico, centro estável, linguagem de domínio, caso Amp (0:04:15; 0:09:36; 0:34:25; 0:17:59; 0:53:54; 1:02:21; 1:17:41). |

## 5. Resumo por aula

### Aula 1: #1 IA como veículo de expressão, mais do que ferramenta

Vídeo: https://www.youtube.com/watch?v=2VQ58dqC12k

Resumo: depois da abertura de Alisson (0:00:30 a 0:02:21), Henrique diz que tudo mudou nas últimas duas semanas com o lançamento do pi-durable: agora há infraestrutura de agente durável, com o que o design de sistemas distribuídos exige (resiliência a falhas, continuar de onde parou, retries, policies), algo que antes existia só para workflows, como no Temporal (0:04:13 a 0:05:20). Isso alinha com o que ele fazia no Petrus, sistema de workflows duráveis para trabalhar com agentes (0:05:21 a 0:05:30); leu o código, está atualizando o Petrus para usá-lo e construiu o assistente pessoal com a biblioteca de dentro do pacote, em poucas linhas e com APIs bem feitas (0:06:08 a 0:06:47). O foco do Petrus deveria ser coletar o estado do mundo para o agente trabalhar, porque o incomoda profundamente queimar token para pegar informação que já deveria estar pronta, só esperando ser analisada e julgada (0:06:49 a 0:07:08). A virada é sair do joga tudo no agente, com todas as permissões, que ele achava horrível, para trabalhar o encanamento em volta e fazer um ou mais agentes focados que cuidam do julgamento (0:07:09 a 0:07:34). Troca-se o polling, turno atrás de turno, por reagir a uma mensagem que chega (0:08:21 a 0:08:37). Ele combina isso com o Executor, um proxy de MCP: em vez de configurar cada agente com e-mail e serviços, conecta tudo no proxy e monta toolkits, um só de leitura de e-mail, outro de leitura e pesquisa, outro só de envio, e cada agente recebe a URL de MCP do seu toolkit (0:09:05 a 0:10:04). O code mode deixa o agente escrever um script determinístico que roda numa VM JavaScript em memória, combina várias tools e chamadas de modelo, e devolve só o resultado, sem o vai e volta de cada chamada pelo turno da LLM (0:10:09 a 0:10:51). Com isso classificou 3.000 e-mails entre marketing e não marketing e recebeu só a lista de domínios, numa tacada só, em paralelo (0:10:52 a 0:12:01). Alisson descreve a passagem da IA como ferramenta para a IA como companhia e a floresta (0:12:16 a 0:16:54). Henrique responde com o zoológico, conta que parou de usar o aplicativo desktop da OpenAI depois do último lançamento porque tudo ficava lá dentro, e voltou ao home lab (0:17:37 a 0:18:53); todo produto tem pressupostos de workflow (0:19:18 a 0:19:53). Não gosta de fazer ferramentas, mas não deu jeito: agora tem daemons, agentes configurados para uma tarefa, 50 na mesma máquina, cada um com a permissão de que precisa (0:20:00 a 0:20:33). Descreve o home lab: Tailnet, WhatsApp baixado pelo WAHA e exposto por MCP via Executor, áudios transcritos para o banco, IoT, sensores e servidores num log concentrado, Grafana, o agente mandando print no WhatsApp; é observabilidade de sistema aplicada à vida, com Open Finance a caminho, e a interface pode ser qualquer uma (0:20:46 a 0:22:31). Alisson traz a analogia da arte (0:23:14 a 0:24:57). Henrique fala da ansiedade das pessoas por ferramentas, da prática antropocêntrica e de que adoção na empresa muda processo, cultura e relação entre pessoas, não só ferramenta (0:24:59 a 0:26:07); lembra que Mailchimp, Drip e ActiveCampaign forçavam um workflow que não era natural para ele nem para a equipe (0:27:17 a 0:27:49). Alisson desenvolve fotografia, pintura e Picasso, e a IA como veículo novo de expressão (0:28:29 a 0:33:33). Henrique descreve os padrões que extrai: a timeline de fatos unitários, camadas de fatos derivados, o agente acionado na percepção de uma diferença, o concentrador de eventos externos (0:33:35 a 0:39:52). Explica que precisa de sensores porque funciona bem quando as demandas chegam até ele (0:41:45 a 0:42:36). Depois do trecho de Alisson sobre agency, inteligência composicional e roadmap movido a entusiasmo (0:42:37 a 0:49:01), Henrique fala de sustentar a pergunta, da disciplina nos experimentos e de privilegiar a mudança (0:49:02 a 0:54:34). Alisson fala do centro estável (0:54:34 a 0:57:22). Henrique conta que lê devagar, que recarregar contexto o cansava, e que pôs camadas de comunicação por cima, inclusive a regra de que a IA termina com uma página (0:57:23 a 1:00:04); diz que a IA não monta essa estrutura sozinha, como erra na arquitetura de software, e que é preciso desenhar limites e criar linguagem de domínio com ela (1:00:38 a 1:01:24). Usa o Ariad, de Alisson, para gerir meta-contexto (1:02:00 a 1:02:20) e dá nome às coisas antes de construir: um glossário do Obsidian antes da extensão, e o código refletindo o glossário, sempre (1:02:21 a 1:04:14). Alisson fala de campo agêntico e da jornada de saúde que virou prontuário; Henrique observa que é a timeline outra vez (1:04:35 a 1:08:52). Henrique sugere o proxy de MCP para as jornadas do Mirror, com cada agente carregando só as ferramentas de que precisa (1:11:13 a 1:12:21). Conta o desafio da esposa, rainha do papel, e diz que tem de funcionar para ele e ter interface positiva com ela; o risco, numa casa ou numa empresa, é se fechar em um é assim que funciona e transformar a pessoa em engrenagem (1:13:18 a 1:16:36). Alisson pergunta pela colaboração entre humanos e agentes (1:16:59 a 1:17:35); Henrique responde com o Amp e com o próprio problema: quer agentes reativos (1:17:37 a 1:23:06).

Linha do tempo:

- [0:00:30] Alisson abre: sense making de experiências fragmentadas
- [0:02:23] Henrique: falta conversar para além das tools
- [0:04:13] pi-durable: infraestrutura de agente durável
- [0:06:49] Petrus deveria coletar o estado do mundo; queimar token para buscar informação incomoda
- [0:09:05] Executor, proxy de MCP, toolkit por agente
- [0:10:09] code mode e os 3.000 e-mails
- [0:17:37] o zoológico: produtos para você viver dentro
- [0:20:19] daemons, 50 agentes por máquina, cada um com a sua permissão
- [0:33:57] os padrões são o que importa: timeline, fatos derivados, concentrador de eventos
- [0:49:20] sustentar a pergunta em vez de fechar uma conclusão
- [0:53:42] privilegiar a mudança
- [1:00:42] a IA não monta a estrutura sozinha; linguagem de domínio
- [1:13:18] a rainha do papel e a interface com quem pensa diferente
- [1:17:41] o caso Amp

Princípios que ele enuncia:

- [0:06:58] Não queime token para pegar informação que já deveria estar pronta, esperando só ser analisada e julgada.
- [0:07:20] Trabalhe o encanamento em volta do agente e deixe agentes focados com o julgamento, em vez de jogar tudo, com todas as permissões, num agente só.
- [0:09:53] Cada agente recebe só o toolkit de que precisa; a configuração do agente é uma URL de MCP.
- [0:34:42] Guarde fatos unitários numa timeline, sem conclusões, e tire as conclusões depois, cruzando uma fatia de tempo.
- [0:36:48] O agente é acionado na percepção de uma diferença e responde a uma pergunta: essa diferença é significativa?
- [0:37:59] Um concentrador de eventos garante todos os fatos até o momento, cobrindo webhook perdido, duplicado, fora de ordem ou que parou de chegar.
- [0:53:51] Faça as coisas privilegiando a mudança.
- [1:02:31] Antes de construir, dê nome às coisas, e faça o código refletir esses nomes, sempre.

Código: nenhum código escrito ou mostrado.

Citações:

- [0:03:57] 16 bilhões de tokens no mês, e isso não significa nada
- [0:20:00] eu não quero fazer uma ferramenta, eu gosto de fazer as coisas que eu quero fazer
- [0:39:27] eles não são ferramenta, eles não são produto
- [0:53:51] como é que você faz as coisas privilegiando a mudança

## 6. Princípios que atravessam toda a série

São só de Henrique; as ideias de Alisson ficam na seção 3 e no glossário, com o nome dele.

1. **Padrões, não ferramentas.** O que se compartilha e se extrai são padrões, que podem ser biblioteca, trecho ou estratégia de código; produtos e ferramentas mudam (0:39:20 a 0:39:49). Só faz sentido compartilhar um conjunto de primitivas, porque o encaixe é muito pessoal (0:27:04 a 0:27:16).
2. **Informação pronta antes do agente.** Coletar fatos não é trabalho do agente; queimar token para buscar o que já devia estar pronto é desperdício (0:06:58 a 0:07:08). O agente recebe um catálogo de informações disponíveis e vai direto ao processo (0:38:49 a 0:39:03).
3. **Menor privilégio por agente.** Um toolkit por agente, com só as ferramentas da tarefa (0:09:36 a 0:10:04), cada daemon com a permissão de que precisa (0:20:28 a 0:20:31); carregar todas as ferramentas em todos os agentes consome contexto (1:11:50 a 1:11:58).
4. **Fatos antes de conclusões.** A timeline guarda fatos unitários sem significado atribuído (0:34:42 a 0:35:04); camadas de fatos derivados vêm por cima (0:35:29 a 0:35:38); a conclusão é trabalho posterior (0:35:06 a 0:35:20).
5. **Reagir a eventos, não fazer polling, e ainda assim reconciliar.** Trocar o turno atrás de turno pelo chegou uma mensagem (0:08:21 a 0:08:37), mas não confiar no webhook: perdido, duplicado, fora de ordem ou parado, e por isso uma ação complementar pergunta de tempos em tempos se há diferença (0:37:31 a 0:37:57).
6. **Privilegiar a mudança.** A única constante é a mudança; a estrutura tem de permitir mudar sem refazer tudo (0:53:42 a 0:53:57; 0:51:20 a 0:51:26).
7. **Nomear antes de construir, e o código reflete os nomes.** Criar nome é difícil, e nomear dá contorno ao problema e comunicação concisa (1:02:31 a 1:02:47; 1:03:41 a 1:03:50); o código reflete isso sempre, inclusive na organização (1:03:50 a 1:04:01).
8. **A arquitetura é humana.** A IA erra na arquitetura de software; é preciso desenhar limites e conceituar com ela (1:00:48 a 1:01:05).
9. **Sustentar a pergunta, com disciplina nos experimentos.** Resistir a fechar conclusão num momento pré-paradigmático (0:49:30 a 0:50:39), com experimentos feitos para se adaptar (0:51:12 a 0:51:26).

## 7. Citações-chave do curso

Só falas de Henrique. Paráfrases de legenda, não verificadas.

| Lição | Timestamp | Paráfrase |
|---|---|---|
| 1 | 0:03:53 | No mês passado foram 16 bilhões de tokens, e isso não significa nada. |
| 1 | 0:06:58 | Me incomoda profundamente queimar token para pegar informação que já deveria estar pronta, esperando só ser analisada e julgada. |
| 1 | 0:10:02 | A configuração do agente é uma URL de MCP. |
| 1 | 0:17:37 | É como se as empresas estivessem todas tentando criar um produto para você viver dentro dele. |
| 1 | 0:19:18 | Todos os produtos têm pressupostos de workflow, e a adesão a um produto vira tudo ou nada. |
| 1 | 0:20:00 | Eu não quero fazer uma ferramenta; eu gosto de fazer as coisas que eu quero fazer. |
| 1 | 0:34:42 | Eu não quero conclusões; tirei uma foto e a CPU do servidor está em 80, o que significa não importa. |
| 1 | 0:39:27 | Eles não são ferramenta, eles não são produto. |
| 1 | 0:49:47 | Eu quero sustentar a pergunta em vez de fechar uma conclusão. |
| 1 | 0:51:31 | Alguém disse que a IA tornou a gente preguiçoso de pensar; eu não, estou tendo que fazer outras coisas para parar de pensar. |
| 1 | 0:53:51 | Como é que você faz as coisas privilegiando a mudança. |
| 1 | 1:00:45 | A IA não consegue montar essa estrutura sozinha. |
| 1 | 1:02:35 | Criar nome é difícil. |
| 1 | 1:15:03 | Eu tenho dois agentes na minha vida: a LLM e a minha mulher. |

## 8. A evolução técnica, aula a aula

Uma lição só; a evolução que Henrique narra é a do próprio ambiente:

- **Antes:** agentes que precisavam ser agendados e cutucados para rodar, e paravam (0:05:37 a 0:05:48); a lógica de jogar tudo no agente com todas as permissões (0:07:13 a 0:07:18); semanas testando produtos (0:18:58 a 0:19:15).
- **A virada:** agentes duráveis com o pi-durable, operando sem loop gastando energia (0:05:48 a 0:05:58); o Petrus atualizado para usá-lo (0:06:11 a 0:06:14).
- **Depois:** daemons por tarefa com permissões próprias (0:20:19 a 0:20:33), o Executor com toolkits (0:09:05 a 0:10:04), o code mode (0:10:09 a 0:10:51), e o home lab concentrando fatos (0:21:36 a 0:22:15).
- **A organização que veio depois do crescimento:** começou instalando por SSH, chegou a 30 coisas rodando sem lembrar onde estava o quê, e precisou de Terraform, deploy, uma forma padrão de coletar informação e, por fim, Kubernetes, para permitir a mudança (0:52:42 a 0:53:40).
- **Camada de comunicação:** diagramas, vídeo, imagem e a regra de uma página, porque ele lê devagar e recarregar contexto o cansava (0:57:34 a 0:59:58).

## 9. Arsenal técnico demonstrado no curso

Nada é mostrado na tela segundo a fala; tudo é relato.

| Peça | O que faz no ambiente dele | Timestamp |
|---|---|---|
| pi-durable (Pi) | Infraestrutura de agente durável; base do assistente pessoal | 0:04:28 a 0:06:47 |
| Petrus | Runtime dele de workflows duráveis para agentes, sendo atualizado | 0:05:21 a 0:06:14 |
| Executor | Proxy de MCP com toolkits por agente | 0:09:05 a 0:10:04 |
| Code mode | Script determinístico numa VM JavaScript em memória | 0:10:09 a 0:10:51 |
| Jev (TypeSafe) | Classificador usado nos 3.000 e-mails [legenda: o dev, o zero] | 0:11:03 a 0:11:41 |
| WAHA | Baixa as mensagens do WhatsApp para acesso por MCP [legenda: Warga] | 0:20:54 a 0:21:05 |
| Tailnet, Grafana | Rede do home lab e painéis que o agente fotografa | 0:20:49 a 0:21:58 |
| Obsidian | Interface de comunicação; extensão em construção | 0:22:28; 1:03:15 a 1:03:29 |
| Ariad | Gestão de meta-contexto do home lab, feito por Alisson | 1:02:00 a 1:02:20 |
| Skill de Matt Pocock | Glossário antes de construir [legenda: Building with Blocks; a descrição liga grill-with-docs] | 1:03:03 a 1:03:12 |
| Terraform, Docker, Kubernetes | Organização do home lab para permitir mudança | 0:53:11 a 0:53:30 |
| Amp | Referência de colaboração entre humanos e agentes | 1:17:41 a 1:22:43 |

## 10. Glossário do curso

- **Agente durável:** agente que resiste a falhas, continua de onde parou e tem retries e policies (Henrique, 0:04:32 a 0:05:16).
- **Tirar a gente do loop:** o agente opera sem o humano agendando e cutucando (Henrique e Alisson, 0:05:51 a 0:06:04).
- **Toolkit:** recorte de ferramentas de um proxy de MCP entregue a um agente (Henrique, 0:09:36 a 0:10:01).
- **Code mode:** o agente escreve um script que combina tools e devolve só o resultado (Henrique, 0:10:09 a 0:10:51).
- **Daemon:** agente configurado especificamente para uma tarefa, com a permissão de que precisa (Henrique, 0:20:19 a 0:20:31).
- **Timeline:** registro de fatos unitários, sem conclusões (Henrique, 0:34:25 a 0:35:04).
- **Fatos derivados:** camadas de agregação sobre a timeline (Henrique, 0:35:29 a 0:35:38).
- **Concentrador de eventos:** representação dos eventos externos que garante todos os fatos até o momento (Henrique, 0:37:20 a 0:38:15).
- **Floresta:** o ambiente que cada um compõe para a IA viver (Alisson, 0:14:58 a 0:16:54).
- **Zoológico:** o produto fechado e pré-definido para você viver dentro (Henrique, 0:17:59 a 0:18:07).
- **Inteligência composicional:** a terceira coisa criada pela associação da inteligência da pessoa com a da IA (Alisson, 0:45:05 a 0:45:19).
- **Centro estável:** a estrutura que não muda e acopla cada novidade (Alisson, 0:54:34 a 0:57:16).
- **Campo agêntico:** o que o agente vê, como a luz de uma lanterna (Alisson, 1:05:00 a 1:05:38).
- **Jornada:** a unidade em que Alisson organiza o campo agêntico no Mirror (Alisson, 1:05:46 a 1:05:52).

## 11. Perguntas e respostas que o curso responde

- **Por que agentes duráveis mudam o jogo?** Porque o agente para de depender de agendamento e loop, e o que se gerencia passa a ser eventos (Henrique, 0:05:32 a 0:05:58; 0:08:21 a 0:08:37).
- **Como dar a cada agente só o que ele precisa?** Um proxy de MCP com um toolkit por agente (0:09:36 a 0:10:04).
- **Como processar milhares de itens sem estourar tokens?** Code mode: o agente escreve um script que roda tudo em paralelo e devolve só o resultado (0:10:09 a 0:12:01).
- **Por que ele não adota um produto de IA?** Porque todo produto tem pressupostos de workflow e a adesão vira tudo ou nada (0:19:18 a 0:19:53).
- **O que o agente deve fazer, se não coletar dados?** Responder se uma diferença percebida é significativa (0:36:48 a 0:37:05).
- **Por que não confiar só em webhook?** Ele pode se perder, duplicar, chegar fora de ordem ou parar; uma ação complementar reconcilia (0:37:31 a 0:37:57).
- **A IA consegue montar essa estrutura sozinha?** Não; está no nível da arquitetura de software, em que ela erra (1:00:42 a 1:01:05).
- **Como pessoas e agentes trabalham juntos?** Pergunta em aberto; Henrique aponta o Amp como vanguarda, com threads multiplayer, VMs efêmeras e deploy monitorado por feature flag, mas com pressupostos de workflow que travam projetos legados (1:17:41 a 1:21:25).

## 12. Repositórios e recursos

| Recurso | Relação | Timestamp |
|---|---|---|
| [Petrus](https://petrus.run) (henriquebastos/petrus) | Dele; digerido em `kb/repos/petrus.md` | 0:05:21 |
| [pi-durable](https://www.npmjs.com/package/@earendil-works/pi-durable) | Terceiro, usado por ele | 0:04:28 |
| [Executor](https://github.com/RhysSullivan/executor) | Terceiro, de Rhys Sullivan [legenda: Reis] | 0:09:05 |
| [Code Mode (Cloudflare)](https://blog.cloudflare.com/code-mode/) | Conceito de terceiro | 0:10:11 |
| [Jev (TypeSafe)](https://typesafe.ai/blog/introducing-system-one-models-and-jev) | Terceiro | 0:11:03 |
| [WAHA](https://waha.devlike.pro) | Terceiro | 0:20:56 |
| [Obsidian](https://obsidian.md) | Terceiro | 0:22:28 |
| [Mirror](https://github.com/mirror-mind-ai/mirror) | De Alisson | 0:22:39 |
| [grill-with-docs](https://github.com/mattpocock/skills/tree/main/skills/engineering/grill-with-docs) | Skill de Matt Pocock | 1:03:03 |
| [Ariad](https://github.com/mirror-mind-ai/ariad) | De Alisson, usado por Henrique | 1:02:02 |
| [Amp](https://ampcode.com) | Produto de terceiro | 1:17:47 |

Repositórios de Henrique citados: **Petrus**. O assistente pessoal e o home lab não são publicados.

## 13. Análise linha a linha do código real

A conversa não publica nem mostra código. Não há análise de código real. Limites da legenda que ficam registrados:

- pi-durable aparece como Pi Durable (0:04:32), PyTurbel (0:08:59), pai turbo (0:10:05), pai do Rubo (0:20:15) e PyTorch (0:43:56 a 0:44:04); a descrição lista pi-durable.
- Petrus sai Petros (0:05:23; 0:06:12) e Petrous (0:44:00); Amp sai REM (0:00:14) e Emp (0:19:13; 1:17:44); Executor sai Xecutor (0:21:07); WAHA sai Warga (0:20:56); Mirror sai Miro (0:22:39; 1:05:49); Ariad sai Ariadne (1:02:02); o classificador sai o dev e o zero (0:11:03; 0:11:38) [provável: Jev]; a skill de Matt Pocock sai The Skill do Building with Blocks (1:03:03) [a descrição liga grill-with-docs].
- Os produtos que ele cita em 0:17:26 a 0:17:30 e 0:19:09 (Grok Bot, Dotes da OpenAI, Deep Seek) são leituras de legenda não confirmadas.
- Em 1:18:00, Watson faz o deploy [provável: o agente faz o deploy]; em 1:16:37, no mundo da ESA [provável: da IA].
- O diagrama do agente que ele diz ter postado no X (0:20:35 a 0:20:41) não foi coletado.

## 14. Execução real dos testes

A conversa não publicou código nem suíte. Não há o que rodar.

---

Documentação elaborada a partir da transcrição do vídeo #1 IA como veículo de expressão, mais do que ferramenta, conversa entre Henrique Bastos e Alisson Vale no canal pessoal de Henrique Bastos, vídeo `2VQ58dqC12k`, legenda automática em português (pt-orig) capturada em 2026-10-22. As citações são paráfrases da transcrição, não verificadas contra o vídeo (`verified: false`), renderizadas sem aspas e com os erros de reconhecimento anotados entre colchetes quando precisam aparecer. A fala de Alisson Vale é atribuída a ele pelo nome e não entra como princípio de Henrique; a atribuição segue as marcas de turno da legenda e é aproximada. Familiares aparecem só pelo papel. A conversa não tem código, repositório próprio além do Petrus, nem suíte; o diagrama publicado no X não foi coletado. Conteúdo de caráter educativo.
