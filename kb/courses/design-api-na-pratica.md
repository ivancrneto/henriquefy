<!-- converted from design-api-na-pratica.html by henriquefy.ingest.html_to_md on 2026-10-08; see kb/courses/README.md for provenance and license -->

Documentação Técnica · Curso em Vídeo

# Design de API na Prática

Documentação completa da playlist de 9 aulas com Henrique Bastos (HB Network)

 Produzido a partir da transcrição integral da playlist no YouTube · Setembro de 2026 · Fonte: [Design de API na Prática (playlist)](https://www.youtube.com/watch?v=3trE61xKXXk&list=PLeKXYyZCJHxdD1CXDeEymwI1S9wlcsmYo)

RESTHTTPModelo de Maturidade de RichardsonHATEOASHypermediaDjangoPythonArquitetura de Software

## 1. Visão geral do curso

**“Design de API na Prática”** é uma série de aulas ao vivo ministrada por **Henrique Bastos**, no canal da **HB Network**, que mistura fundamentos conceituais com implementação real em **Python e Django**. A playlist reúne **9 episódios** e constrói, passo a passo, uma API de pedidos de uma cafeteria, evoluindo-a pelos **quatro níveis do Modelo de Maturidade de Richardson** — o mesmo modelo que fundamenta as decisões de design de APIs REST maduras.

O fio condutor da série é direto e provocador: *a maioria das pessoas associa “API” a “JSON / HTTP / CRUD”, e isso é uma visão limitada.* O curso se propõe a desconstruir essas premissas falsas e ensinar o aluno a **pensar na fronteira do sistema** — a interface — em vez de partir do schema do banco de dados.

| Aula | Título | Foco central |
|---|---|---|
| **#01** | O que ninguém te conta sobre APIs | Fundamentos, “interface” como protagonista, histórico (Unix, POSIX) |
| **#02** | Abaixando o Nível de Abstração | Web vs. HTTP, recurso, representação, URI, baixo acoplamento |
| **#03** | Modelos de Maturidade das APIs (Parte 1) | Modelo de Richardson, Nível 0, abordagem top-down |
| **#04** | Introdução | Panorama dos 4 níveis e reorganização do projeto Django |
| **#05** | Evoluindo do Nível 0 para o Nível 1 | URIs por recurso, refatoração, decorators, testes com pytest |
| **#06** | Evoluindo do Nível 1 para o Nível 2 | Verbos HTTP corretos, códigos de status, middlewares |
| **#07** | Cliente do Nível 0 e Nível 1 | Clientes de API, serialização, dinheiro em JSON, interfaces virtuais |
| **#08** | Modelagem da API em Nível 3 | Máquina de estados, HATEOAS, mapeamento semântico dos verbos |
| **#09** | Implementação da API em Nível 3 | Links dinâmicos por estado, camada de serviço, pragmatismo |

Duração real: cada aula é uma sessão de live coding de aproximadamente duas horas; os resumos a seguir condensam o conteúdo técnico-funcional de cada sessão.

## 2. Filosofia e metodologia de ensino

#### Conteúdo puxado pela necessidade do aluno, não empurrado por preconcepção

O curso é construído “ao vivo” e incremental. Henrique deixa explícito que não segue um roteiro rígido: o conteúdo é moldado pelas dúvidas, feedbacks e dificuldades da comunidade durante as aulas.

> “O desafio desse programa é fazer um conteúdo puxado pela necessidade do aluno e não empurrado por uma preconcepção do que seria o ideal de falar sobre API.”— Henrique Bastos, Aula #01

#### Hard skills + soft skills + visão estratégica

O objetivo explícito é ensinar o aluno a **pensar, modelar e tomar decisões arquiteturais** — não a operar ferramentas. Henrique declara várias vezes que não quer ensinar a ferramenta, mas ensinar a *deduzir o que a ferramenta faz* e por quê.

> “Eu não quero te ensinar a ferramenta. A minha preocupação é te ensinar a deduzir o que a ferramenta está fazendo, o que você, às vezes, não sabe.”— Henrique Bastos, Aula #01

#### Design antes de código: top-down e diagramas

Duas teses recursivas do curso:

- **Design top-down:** comece pela fronteira do sistema (a interface externa), não pelo schema do banco. Projetar o banco primeiro quase sempre produz uma API ruim.
- **O diagrama como exercício de visualização:** antes de codar, desenhe. O diagrama é um exercício que força decisões; o código então apenas concretiza os compromissos já assumidos.
- **Tudo é trade-off:** nada é “certo” ou “errado” em absoluto; é sempre uma escolha com custos e benefícios. Subir de nível de maturidade é reduzir trabalho futuro usando padrões já existentes.

> “Não trate as coisas como certo e errado, trate como trade-off, como escolha.”— Henrique Bastos, Aula #03

#### Sequência de trabalho: fazer funcionar, depois ficar bonito

Henrique adota explicitamente o pragmatismo: primeiro o código funciona, depois é refatorado. E em todas as aulas a refatoração é guiada por um sinal claro: **boilerplate é “cheiro” de abstração faltando**.

> “Primeiro faz funcionar, depois faz bonito.”— Henrique Bastos, Aula #09

## 3. Os 4 pilares conceituais

Aulas #01 e #02 constroem a base conceitual que sustenta toda a série. Quatro idéias precisam estar cristalizadas antes de qualquer código:

### 3.1 A interface é o que importa

No termo *Application Programming Interface*, a palavra mais importante é **Interface**. Uma API é “a especificação de como um software pode interagir com outro software”. Ela é a camada de indireção que permite a dois sistemas cooperarem sem se conhecerem diretamente. Henrique usa analogias físicas e humanas (tomadas elétricas, embreagem do carro, USB, joystick, painel de micro-ondas, metáfora da mesa de trabalho nas GUIs) para mostrar que interfaces são ubíquas e antigas — **APIs não nasceram com a web**.

- **Unix:** APIs de texto via `stdin/stdout` e a invenção do *pipe* para encadear pequenas rotinas.
- **POSIX:** interface portátil de sistema operacional, que dá portabilidade de código entre sistemas.

### 3.2 Recurso ≠ entidade de banco de dados

Erro clássico: confundir recurso com tabela. Um recurso é uma **projeção, uma interpretação de algo do mundo** (físico ou lógico) que contém informação útil para um contexto. Pode ser um processo ou workflow — não precisa ser um dado persistido.

> “O recurso não é a coisa em si; o recurso é uma projeção, uma interpretação que eu dou de algo que existe no mundo.”— Henrique Bastos, Aula #02

### 3.3 Representação ≠ codificação

O recurso não é a sua representação. `JSON`, `XML` e `CSV` são apenas **codificações** da representação de um recurso. A arquitetura da Web permite que cliente e servidor negociem a codificação via *content negotiation* (ex.: header `Accept`), desacoplando transporte e formato.

> “Não existe nada no REST que fale sobre JSON, XML ou JPG. Isso é um detalhe de codificação da representação de um recurso.”— Henrique Bastos, Aula #02

### 3.4 Identificadores (URIs)

Para um recurso ser endereçado na Web ele precisa de ao menos um identificador. “Uniform” em URI implica **padrões**, não necessariamente única unicidade de formato — um mesmo recurso pode ter múltiplos identificadores. Detalhe de design: evite *acoplar o formato na URI* (ex.: sufixos como `.json`).

### 3.5 Web vs. HTTP, e baixo acoplamento

**A Web não é o protocolo HTTP.** HTTP é um protocolo de aplicação que acontece na Web. A Web é uma malha de relacionamentos entre recursos identificados. Essa arquitetura existe para dar **baixo acoplamento e isolamento**: partes do sistema evoluem independentemente sem quebrar o ecossistema — exatamente o que APIs mal desenhadas (que espelham modelos de banco) destroem. A interface é *uniforme*: poucos verbos (métodos HTTP) operando sobre muitos substantivos (recursos).

## 4. O Modelo de Maturidade de Richardson (Níveis 0–3)

O motor da série. O modelo avalia a maturidade de uma API segundo o uso de **URIs**, **verbos HTTP** e **hypermedia (HATEOAS)**. Ele parte da Aula #03 e é implementado do Nível 0 até o Nível 3 ao longo dos episódios seguintes.

| Nível | Nome | O que usa | Em uma frase |
|---|---|---|---|
| 0 | **POX** (Plain Old XML / túnel RPC) | HTTP só como transporte | Uma única URI, um único verbo, payload “empurrado” sem usar semântica HTTP. |
| 1 | **Recursos** | URIs por recurso | Várias URIs separando recursos lógicos, mas geralmente preso a um único verbo (POST). |
| 2 | **Verbos HTTP** | Métodos + códigos de status | POST cria, GET lê, PUT sobrescreve, PATCH atualiza parcial, DELETE remove; status codes com sentido. |
| 3 | **Hypermedia** (HATEOAS) | Estado da aplicação via links | O servidor usa HTTP como máquina de estados do domínio e guia o cliente pelos links disponíveis. |

#### Por que subir de nível?

Não é por dogma: é para *reduzir trabalho*.

> “O objetivo da gente amadurecer a nossa API, subir no nível de maturidade, é para a gente conseguir utilizar muito bem esses recursos e esses padrões que já estão aí para reduzir o nosso trabalho.”— Henrique Bastos, Aula #03

Uma API mais madura fica **previsível e padronizada**, o que simplifica o consumo por clientes e reduz a carga de implementação de cada lado da fronteira.

## 5. Resumo das 9 aulas

Aula #01

### O que ninguém te conta sobre APIs

Aula inaugural: nivelamento conceitual. Estabelece a proposta do curso (conteúdo iterativo, foco em design e decisões arquiteturais, crítica à associação automática “API = JSON/HTTP/CRUD”), define “interface” como protagonista e percorre o histórico das APIs (Unix, pipes, POSIX). É a aula de alinhamento de expectativas: *isto não é um tutorial de ferramentas*.

- **Conceito central:** API = especificação de como um software interage com outro; a interface é a camada de indireção que permite cooperação.
- **Crítica:** focar só no concreto (JSON/HTTP) faz a gente perder as “relações invisíveis entre as partes”.
- **Formato:** aula ao vivo com participação da comunidade pelos canais da HBNetwork.

Aula #02

### Abaixando o Nível de Abstração

Aprofunda os fundamentos “por baixo das convenções de frameworks”: distingue Web de HTTP, define recurso (projeção/interpretação, não tabela), representação versus codificação (JSON/XML/CSV são codificações), identificadores URI e o valor arquitetural do baixo acoplamento e da interface uniforme. Enfatiza não acoplar formato de arquivo à URI.

- **“Uniform”** = padrões, não unicidade; um recurso pode ter múltiplos identificadores.
- **Content negotiation:** o cliente diz o que aceita (`Accept`); o servidor entrega a representação codificada.
- **Diagnóstico:** a dificuldade diária é “estar com a mão na massa” e não separar os conceitos corretamente.

Aula #03

### Modelos de Maturidade das APIs (Parte 1)

Primeira aula prática da série. Introduz o Modelo de Maturidade de Richardson e implementa o **Nível 0** com Django: um endpoint de cafeteria que registra pedidos, sofrendo de defeitos clássicos (GET para mudar estado, falta de tratamento de erros/status codes, acoplamento forte). Introduz a ideia de persistência leve na fase de design (conceito de *prevalence* à la ZODB) para evitar o peso de um banco relacional cedo demais.

- **Nível 0:** HTTP como transporte (RPC); uma URI só; payload sem estrutura padronizada.
- **Top-down vs. bottom-up:** atenção no banco = repensar; o importante é “pensar para fora”, na fronteira do sistema.
- **Fechamento:** cria um script cliente em linha de comando para interagir com a API simulada.

Aula #04

### Introdução

Sessão de transição (ao vivo, com problemas técnicos de compartilhamento de tela). Faz o panorama dos quatro níveis e reestrutura o projeto Django para que **todos os níveis convivam no mesmo projeto**, permitindo comparar facilmente o que é cada um. Meta declarada: implementar os Níveis 1 e 2 (muito parecidos) e, com eles funcionando, partir para um cliente mais complexo — “a cereja do bolo”.

- Nível 0: não usa URI direito, não usa HTTP direito, não usa hyperlink.
- Nível 1: melhora o uso das URIs (novos endpoints), mas ainda dependente de template de URI.
- Metodologia: “trabalhar aqui por duas horas; quarta-feira que vem estaremos aqui novamente”.

Aula #05

### Evoluindo do Nível 0 para o Nível 1

Refatoração prática com `pytest` para sair do túnel de URI única: diferentes URIs passam a mapear recursos específicos, mesmo que ainda presas a um único verbo (POST).

- **Testes de integração isolados** com mocks de banco.
- **Fim dos “números mágicos”:** adota `http.HTTPStatus` da biblioteca padrão para códigos de status legíveis e mantíveis.
- **Erros e casos de borda:** `405 Method Not Allowed` para método não suportado e `404 Not Found` para recurso inexistente — migrando de strings de erro para status codes reais.
- **Decorators Python** como abstração: um framework de decorators que intercepta requisições e valida verbos HTTP permitidos, limpando as views e tornando-as mais expressivas.
- **Tese central:** boilerplate é sinal de abstração faltando no design.

> “No nível 1 a gente tem várias URIs para separar recursos lógicos, mas a gente fica preso geralmente a um único verbo HTTP.”— Henrique Bastos, Aula #05

Aula #06

### Evoluindo do Nível 1 para o Nível 2

Transição para o uso correto dos **verbos HTTP e códigos de status**: a API passa a tratar recursos como coleções manipuladas por `POST` (criar), `GET` (ler), `PUT` (sobrescrever), `PATCH` (atualizar parte) e `DELETE` (remover). Aula com forte componente de refatoração e metaprogramação.

- **Crítica ao ORM como ditador do design:** o maior erro é deixar a estrutura do banco (via ORM Django) ditar o design da API. “Programar por coincidência” é o problema a superar.
- **Middlewares** para tratar exceções (como 404) e padronizar respostas.
- **Desafio técnico:** Django lida com `form-data` por padrão, e não com JSON de forma simples em todos os verbos; Henrique estende o cliente de testes e usa metaprogramação (`type`, `functools`) para gerar dinamicamente métodos de teste que já encapsulam `Content-Type: application/json`, eliminando repetições.

> “O problema do nível 2 é que você começa a tentar fazer select automático a partir do modelo do banco de dados refletido na API; vira uma cagada, porque não é para isso.”— Henrique Bastos, Aula #06

**Observação didática:** o Nível 2 é “onde a galera chega e fica: é isso que eu queria” — é o CRUD padrão de mercado — mas ainda não resolve o problema do cliente navegando o domínio.

Aula #07

### Cliente do Nível 0 e Nível 1

Mudança de perspectiva: a aula constrói **clientes** para consumir as APIs dos níveis 0 e 1, usando o sofrimento do cliente como evidência de por que evoluir para o Nível 3.

- **Organização:** refatora o “framework” de API em pacote separado (`decorators`, `http`, `middleware`, `serializer`, `tests`) — elementos de mesma natureza próximos.
- **Bug de serialização:** investigação de erro com `datetime` em JSON — o problema estava no tratamento de *bytes* vs. *strings* e na ausência de codificador personalizado para tipos de alto nível.
- **“O inferno do cliente”:** API mal desenhada força centenas de requisições desnecessárias e conversões manuais complexas.
- **Interfaces virtuais:** classe base virtual via `abc.ABCMeta` + `__subclasshook__` para garantir que objetos implementem a interface esperada de forma robusta.
- **Dinheiro em JSON:** `float` é perigoso por erro de precisão; usar inteiros “com duas casinhas” sem metadados vira uma loucura de transformações na view. A lição: a API precisa de **metadados** que orientem conversões programáticas nos encoders/decoders.

> “O problema é que fazer um client para sua API vira um inferno e dá um trabalho enorme. É esse o problema que causa os sintomas: o cara tem que fazer 300 requisições desnecessárias.”— Henrique Bastos, Aula #07

Aula #08

### Modelagem da API em Nível 3

Aula de **modelagem** (diagrama antes de código): evoluir do CRUD (Nível 2) para o *Domain Application Protocol* (Nível 3), em que o servidor gerencia o estado do domínio e guia o cliente pelas ações possíveis.

- **Máquina de estados do Pedido:** *sem pedido → aguardando pagamento → preparando → entregue → concluído*.
- **Gestão de estado no servidor:** o servidor deixa de ser só armazenamento e passa a controlar transições — ações (cancelar, atualizar) só ocorrem quando o estado permite.
- **Mapeamento semântico dos verbos:** escolher POST/PUT/DELETE/GET pela semântica da ação do usuário no mundo real, não pelo CRUD técnico.
- **HATEOAS:** links nas respostas informam ao cliente quais ações estão disponíveis naquele estado — o cliente não “adivinha” URLs nem detém a lógica de negócio.
- **Exceções de domínio:** `409 Conflict` quando o cliente tenta operação inválida para o estado atual.

> “No Nível 3, o que eu vou usar é o HTTP como uma máquina de estado da aplicação.”— Henrique Bastos, Aula #08

Aula #09

### Implementação da API em Nível 3

Implementa a transição do Nível 2 para o Nível 3 (HATEOAS) na prática, gerenciando transições de estado do pedido via links embutidos nas respostas: `self`, `update`, `cancel`, `pay`.

- **Links dinâmicos por estado:** existe correlação rígida entre o status da ordem e os links oferecidos; o código é refatorado para derivar links do estado do domínio.
- **A “armadilha do framework”:** cuidado ao generalizar código genérico demais — você “para de fazer um sistema e começa a fazer um framework”, criando complexidade.
- **Camada de serviço:** à medida que a implementação cresce, a lógica sai das views Django para modelos de domínio / estruturas tipo serviço (separação de responsabilidades). “O código vai ajudando a gente a chegar nessa camada de serviço.”
- **Pragmatismo:** fazer funcionar primeiro, limpar depois; serialização de `Decimal` (moeda) e tratamento de `404`/`405`.

> “O importante é você desacoplar um pouco mais o cliente. Você diz para ele não apenas qual é o link, mas como navegar até ele.”— Henrique Bastos, Aula #09

## 6. Princípios de design de API que atravessam toda a série

Coletados das 9 aulas, estes são os princípios reutilizáveis que você pode aplicar imediatamente:

### 6.1 Sobre fronteiras e abstração

- **Pense na borda do sistema.** “Se você está desenvolvendo uma API e sua atenção está no modelo do banco, repense: o mais importante é pensar para fora, na fronteira do sistema.” (Aula #03)
- **Entenda por que o framework esconde a fronteira.** “O desafio do design de API não é usar o framework, mas entender por que ele esconde de você a fronteira entre o universo externo e o universal interno do seu código.” (Aula #06)
- **Não há fórmula:** “Não dá para resolver esse problema sem entender como a ferramenta funciona. Não tem uma fórmulazinha.” (Aula #06)

### 6.2 Sobre código limpo e abstração

- **Boilerplate é cheiro:** quando há código boilerplate, falta uma abstração no design (Aula #05). Decorators e metaprogramação foram as ferramentas usadas para eliminar repetição.
- **Classes auxiliares refletem o design:** subir de tipos primitivos (números de status) para classes com significado de domínio melhora a intenção do código (Aula #05).
- **O código pede organização:** “Vou fazendo funcionar; depois que funcionar, o código pede pelo amor de Deus: 150 linhas, 250 linhas, ele vai pedindo ‘me organiza melhor’.” (Aula #07)
- **Não generalize cedo demais:** “Quanto mais você tenta abstrair, menos prático você fica.” (Aula #09)

### 6.3 Sobre clientes e representação

- **O cliente é o termômetro do design:** se consumir a API virou um inferno (centenas de requisições, conversões manuais), o problema é do design, não do cliente.
- **Dinheiro não é float:** use representações seguras e, principalmente, **metadados** na API para que encoders/decoders convertam programaticamente sem adivinhação (Aula #07).
- **Links guiam o cliente:** em Nível 3, diga ao cliente *qual* link usar e *como navegar* até ele, a partir do estado atual (Aula #09).

### 6.4 Sobre tomada de decisão

- **Trade-offs, nunca “certo ou errado”.** (Aula #03)
- **O diagrama precede o código:** “O código te força a tomar decisões, ele te força a criar compromissos. O diagrama é um exercício de visualização [antes de codar].” (Aula #08)
- **Exceções nascem do conflito de estados:** “A existência da possibilidade de conflito já indica para mim que eu vou ter um novo tipo de exceção. Eu nem vi o código ainda, eu estou aqui para fazer a gente pensar.” (Aula #08)

## 7. Citações-chave do curso

> “O importante é o ‘interface’. A gente tá o tempo inteiro olhando para ‘application’ e olhando para ‘programming’, mas o relevante no que a API faz é o ‘interface’. Entendendo o ‘interface’, o resto todo se resolve.”— Aula #01

> “Uma API é a especificação de como um software pode interagir com outro software.”— Aula #01

> “A web não é o protocolo HTTP. O HTTP é um protocolo de aplicação que acontece na web.”— Aula #02

> “O recurso da sua API não precisa ser algo que vai ser guardado no banco.”— Aula #02

> “O design top-down vai te forçar a olhar para fora, a imaginar o que é realmente necessário para fora.”— Aula #03

> “O design é isso, é dar sentido, é designar.”— Aula #08

> “Tem que tomar cuidado com isso… você para de fazer um sistema e começa a fazer um framework.”— Aula #09

> “Existe uma relação entre links possíveis e o status da sua ordem.”— Aula #09

## 8. Mapa de recursos e referências

| Recurso | Onde encontrar |
|---|---|
| Playlist completa (fonte desta documentação) | [YouTube — Design de API na Prática](https://www.youtube.com/watch?v=3trE61xKXXk&list=PLeKXYyZCJHxdD1CXDeEymwI1S9wlcsmYo) |
| Canal e demais playlists de treinamento | [HB Network (@hbnetworkoficial)](https://www.youtube.com/@hbnetworkoficial) |
| Comunidade HBNetwork (chat, fórum de dúvidas) | [Discord](https://discord.gg/pTAr89EHMz) |
| Blog do instrutor | [henriquebastos.net](https://henriquebastos.net/) |
| Perfil profissional | [LinkedIn](https://www.linkedin.com/in/henriquebastos) · [Twitter/X](https://twitter.com/henriquebastos) |

#### Próximos passos sugeridos para quem terminou a playlist

- **Reimplemente do zero:** refaça a cafeteria do Nível 0 ao Nível 3 no seu framework preferido, sem olhar o código do curso — o exercício de “fazer a mesma coisa em outro contexto” é onde o aprendizado consolida.
- **Modele antes de codar:** desenhe a máquina de estados do seu domínio de negócio (ex.: pedido, fatura, matrícula) antes de abrir o editor.
- **Conduza um “cliente-cêntrico”:** escreva o cliente da sua própria API e meça a dor — cada requisição desnecessária é um sinal de design.
- **Atente para metadados:** se sua API trafega dinheiro, decida agora a representação (ex.: `Decimal`/centavos + metadados) e evite o inferno da conversão manual.

## 9. Mergulho profundo: o Modelo de Richardson na prática

Para fixar o que cada nível muda em concreto, os exemplos abaixo reconstroem, em formato didático, como a API de pedidos da cafeteria seria consumida em cada nível. **Atenção:** estes exemplos de requisição são ilustrações reconstruídas a partir das técnicas descritas nas aulas — não são transcrições literais do código exibido no curso.

### 9.1 Nível 0 — HTTP como túnel (uma URI, um verbo)

O protocolo é usado apenas como transporte: nenhuma semântica de verbo, nenhuma divisão de recursos. Na aula #03, o problema clássico chega a usar `GET` para operações que mudam estado — um dos “erros de design” que a evolução vai corrigir.

```
# Ilustração didática (estilo Nível 0)
GET /api/cafe?acao=criar_pedido&cafe=expresso&qtd=1
# 200 OK {"mensagem": "pedido criado"}
```

Consequências observadas no curso: payload sem estrutura padronizada, ausência de códigos de status com sentido, acoplamento forte entre cliente e servidor, e um cliente que precisa de lógica de negócio para “endereçar” cada ação.

### 9.2 Nível 1 — Recursos endereçados por URI

Agora existem várias URIs separando recursos lógicos — mas, como o instrutor resume na aula #05, “a gente fica preso geralmente a um único verbo” (quase sempre `POST`). O cliente ainda precisa conhecer templates de URI e “extrair pedacinhos” delas para saber qual ação está acontecendo.

```
# Ilustração didática (estilo Nível 1)
POST /pedidos                # criar pedido
POST /pedidos/1/atualizar    # atualizar (verbo ainda é POST!)
POST /pedidos/1/cancelar     # cancelar
```

### 9.3 Nível 2 — Verbos HTTP e códigos de status

A API passa a ser tratada como uma coleção de recursos manipulada pelos verbos padrão. A aula #06 consolidou a semântica: `POST` cria, `GET` lê, `PUT` sobrescreve integralmente (“você não manda só o atributo que está mudando, você manda tudo de novo”), `PATCH` atualiza partes e `DELETE` remove.

```
# Ilustração didática (estilo Nível 2)
POST   /pedidos               # 201 Created
GET    /pedidos/1             # 200 OK
PUT    /pedidos/1             # sobrescreve o recurso inteiro
PATCH  /pedidos/1             # atualiza apenas alguns campos
DELETE /pedidos/1             # 204 No Content
# Erros com significados reais:
# 400 Bad Request | 404 Not Found | 405 Method Not Allowed
```

O curso troca “strings de erro” por status codes reais, adota `http.HTTPStatus` da biblioteca padrão para eliminar números mágicos e cria *middlewares* para padronizar respostas e tratar exceções (como o `404`).

### 9.4 Nível 3 — Hypermedia (HATEOAS)

O servidor usa o HTTP como uma **máquina de estados da aplicação** (aula #08). Em vez de o cliente “adivinhar” URLs, as respostas carregam os links de transição possíveis *a partir do estado atual* (aula #09: `self`, `update`, `cancel`, `pay`). Ações inválidas para o estado são rejeitadas com `409 Conflict`.

```
# Ilustração didática (estilo Nível 3)
GET /pedidos/1
# 200 OK
# {
#   "status": "aguardando_pagamento",
#   "itens": [...],
#   "links": {
#     "self":   {"href": "/pedidos/1"},
#     "pay":    {"href": "/pedidos/1/pagamentos"},
#     "cancel": {"href": "/pedidos/1/cancelar"}
#   }
# }
#
# (estado "entregue" — os links mudam: cancel/pay deixam de existir)
```

O ponto central da aula #09: **existe uma relação direta entre os links possíveis e o status da ordem** — e o código é refatorado para derivar esses links do estado do domínio, não de uma lista fixa.

## 10. A evolução técnica, aula a aula

A tabela abaixo condensa o fio técnico: em cada estágio, o que foi feito, qual padrão entrou em cena e o que isso destravou.

| Etapa | O que foi feito | Padrão / ferramenta | Resultado obtido |
|---|---|---|---|
| **#03** (Nv 0) | Endpoint de cafeteria registrando pedidos com defeitos de design propositais | Persistência leve (*prevalence* à la ZODB); script cliente em CLI | Base concreta para comparar a evolução; sem peso de DB relacional na fase de design |
| **#05** (Nv 0→1) | URIs por recurso; refatoração guiada por testes | `pytest` + mocks de banco; `http.HTTPStatus`; decorators | Fim dos números mágicos; `404`/`405` reais; views limpas e expressivas |
| **#06** (Nv 1→2) | Verbos HTTP corretos; tratamento padrão de respostas | *Middlewares* de exceção/resposta; metaprogramação em testes (`type`, `functools`) | API como coleção de recursos manipulada por POST/GET/PUT/PATCH/DELETE |
| **#07** (cliente) | Clientes dos Níveis 0–1; caça a bugs de serialização | Encoder JSON próprio; `abc.ABCMeta` + `__subclasshook__` | Prova da dor do cliente; interface virtual robusta; debate moeda/Decimal/metadados |
| **#08** (modelagem Nv 3) | Diagrama da máquina de estados do Pedido; mapeamento semântico dos verbos | Modelagem top-down antes do código; HATEOAS conceitual | Servidor passa a controlar transições; `409 Conflict` para operação inválida |
| **#09** (implementação Nv 3) | Links dinâmicos por estado; lógica movida das views | Links `self/update/cancel/pay`; camada de serviço | Cliente desacoplado, guiado pelo hypermedia; domínio com responsabilidade clara |

## 11. Arsenal técnico demonstrado no curso

Cada aula apresentou — em geral refatorando — um conjunto de ferramentas e técnicas da linguagem. O quadro abaixo resume o que cada uma resolveu dentro da narrativa do curso.

| Técnica / ferramenta | Problema que resolveu | Aulas |
|---|---|---|
| **Decorators em Python** | Reduzir boilerplate das views; interceptar requisições e validar verbos HTTP permitidos | #05 |
| **`http.HTTPStatus`** | Eliminar números mágicos de status code; tornar o código mais legível e mantível | #05 |
| **`pytest` + mocks** | Testes de integração isolados e confiáveis, sem depender do banco | #05 |
| ***Middlewares*** | Tratar exceções (ex.: `404`) e padronizar o formato das respostas | #06 |
| **Metaprogramação (`type`, `functools`)** | Gerar dinamicamente métodos de teste que já encapsulam `Content-Type: application/json`; eliminar repetição nos testes | #06 |
| **Encoder JSON personalizado** | Corrigir serialização de tipos de alto nível (ex.: `datetime`); o dilema *bytes* vs. *strings* | #07 |
| **Interface virtual (`abc.ABCMeta` + `__subclasshook__`)** | Garantir que objetos implementem a interface esperada de forma robusta (duck typing seguro) | #07 |
| **Representação segura de moeda (`Decimal` / centavos)** | Evitar perda de precisão de `float`; apoiar conversões programáticas com metadados | #07, #09 |
| **Máquina de estados + links hypermedia** | Fazer o servidor guiar o cliente pelas ações válidas no estado atual (HATEOAS) | #08, #09 |
| **Persistência por *prevalence*** | Modelar e testar o design cedo, sem o custo de um banco relacional completo | #03 |
| **Camada de serviço** | Tirar lógica de negócio das views; separar responsabilidades à medida que o código cresce | #09 |

## 12. Glossário do curso

| Termo | Significado no contexto da série |
|---|---|
| **API** | Especificação de como um software pode interagir com outro software. |
| **Interface** | A camada de indireção que permite dois sistemas cooperarem — a palavra mais importante de “Application Programming Interface”. |
| **Recurso** | Projeção/interpretação de algo (físico ou lógico) com informação útil para um contexto; não é uma entidade de banco. |
| **Representação** | A forma como o estado do recurso é apresentado; distinta do recurso em si. |
| **Codificação** | JSON, XML, CSV… — apenas pactos de codificação da representação, negociáveis via content negotiation. |
| **URI** | Identificador do recurso na Web; ‘Uniform’ significa padrões, não unicidade — um recurso pode ter vários identificadores. |
| **Web vs. HTTP** | A Web é uma malha de relacionamentos entre recursos identificados; HTTP é um protocolo de aplicação que acontece nela. |
| **REST / Interface uniforme** | Poucos verbos (métodos HTTP) operando sobre muitos substantivos (recursos). |
| **Boilerplate** | Código repetido que “não gera valor”: sinal de que falta uma abstração no design. |
| **Trade-off** | Nada é certo/errado em absoluto; toda decisão de design é uma escolha com custos e benefícios. |
| **Prevalence** | Persistência leve (ex.: ZODB) para fase de design, adiando a complexidade de um banco relacional. |
| **HATEOAS** | Hypermedia as the Engine of Application State — links na resposta guiam o cliente pelas ações disponíveis. |
| **Camada de serviço** | Estrutura que concentra lógica de domínio fora das views, descoberta conforme o código cresce. |
| **Metadados** | Informações na API que permitem conversões programáticas seguras (ex.: tipo e precisão de moeda). |

## 13. Perguntas & respostas que o curso responde

#### “API é JSON + HTTP + CRUD?”

**Não para este curso.** Essa associação automática é exatamente o alvo da crítica da aula #01. JSON é só uma codificação; HTTP carrega semântica que a maioria ignora; CRUD é o patamar do Nível 2 — o curso quer ir além, ao Nível 3.

#### “O que muda pensar top-down em vez de bottom-up?”

Bottom-up (começar pelo banco) leva a APIs que espelham tabelas — “vira uma cagada”. Top-down força você a “olhar para fora”, imaginar o que o mundo externo realmente precisa, e depois decidir como sustentar isso internamente (aulas #03, #06).

#### “PUT ou PATCH?”

`PUT` sobrescreve o recurso integralmente — você reenvia tudo; `PATCH` atualiza apenas partes (aula #06). Escolher entre eles é uma decisão de semântica e de contrato com o cliente.

#### “O que o servidor deve controlar?”

A partir do Nível 3, o servidor controla as *transições de estado* do domínio: ações só acontecem quando o estado permite, e o cliente descobre as ações pelos links (aulas #08–#09).

#### “Por que me preocupar com como o cliente consome?”

A aula #07 inverte a lógica: o sofrimento do cliente é o sintoma de design ruim. “O cara tem que fazer 300 requisições desnecessárias” — o cliente é o termômetro da API.

#### “O framework resolve para mim?”

O framework esconde a fronteira entre o universo externo e o interno do seu código. Entender *por quê* ele faz isso é o desafio do design de API (aula #06) — e não existe “fórmulazinha” (aula #06).

#### “Como representar dinheiro em JSON?”

Evite `float` (erro de precisão). Usar inteiros “com duas casinhas” sem orientação vira transformação manual em toda view; a solução é representação segura + **metadados** que digam ao consumidor como converter (aula #07).

## 14. Repositórios: onde está o código

**Nota importante e honesta:** o curso é conduzido como *live coding* no YouTube e o instrutor **não publicou um repositório oficial único** desta playlist. O que existe, e que serve igualmente bem para estudar, são (a) repositórios do próprio Henrique Bastos que **implementam as ideias ensinadas** e (b) **reimplementações feitas pela comunidade** a partir das aulas. Ambos estão listados abaixo, com o que cada um entrega.

### 14.1 Repositórios do instrutor ligados ao conteúdo das aulas

| Repositório | O que é | Ligação com o curso | Stack |
|---|---|---|---|
| [**requests-pro**](https://github.com/henriquebastos/requests-pro) | RequestsPro — “a forma fácil de construir clientes de API profissionais” (30 ⭐). Tem autenticação transparente, persistência e renovação de token com retry no 401, encoder/decoder JSON customizável, tratamento consistente de erros e auditoria do tráfego HTTP. | **Aula #07** (cliente de API) levada ao produto: é a resposta madura ao “fazer um client vira um inferno”. | Python · MIT |
| [**python-jsonstar**](https://github.com/henriquebastos/python-jsonstar) | Extensão do módulo `json` que serializa tipos customizados (28 ⭐), com encoders prontos para `Decimal`, `date`, `datetime`, `set`, `UUID`, `pydantic.BaseModel`, dataclasses e attrs. | **Aula #07**: resolve exatamente o bug de serialização de `datetime` e o dilema de representar moeda discutidos na aula. | Python · MIT |
| [**petrus**](https://github.com/henriquebastos/petrus) / [petrus-engine](https://github.com/henriquebastos/petrus-engine) | Motor embarcado de *redes de Petri* para Python — modelagem e simulação de workflows com estruturas imutáveis. | Conceitualmente ligado às **aulas #08–#09**: modelar máquinas de estado e transições de workflow antes de codar. | Python · Apache 2.0 |
| [**dictdeeper**](https://github.com/henriquebastos/dictdeeper) | `DeepDict` — manipulação de dicionários profundamente aninhados no estilo de objetos JSON (7 ⭐). | Utilitário para o trabalho com representações JSON discutido ao longo do curso. | Python · MIT |
| [**apihack**](https://github.com/henriquebastos/apihack) | Projeto de API de 2019 do instrutor. | Material histórico de API do mesmo autor; vale como leitura complementar. | Python |
| [**HBNetwork/pds-api-client**](https://github.com/HBNetwork/pds-api-client) | Repositório da HB Network com vários clientes de API reais, um por pasta: `asaas`, `bbapilib` (Banco do Brasil), `betapp`, `google_address`, `orlando`. | Estudo de caso de **clientes de API** reais de terceiros — ecossistema da aula #07. | Python · MIT |
| [**python-decouple**](https://github.com/HBNetwork/python-decouple) | Separação estrita entre configuração e código (3k ⭐, o projeto mais popular da HB Network). | Consumo de API sem credenciais hardcoded — base usada nos exemplos de cliente. | Python |
| [**HBNetwork/coding-dojo**](https://github.com/HBNetwork/coding-dojo) · [python-eduzz](https://github.com/HBNetwork/python-eduzz) · [pds-microservicos](https://github.com/HBNetwork/pds-microservicos) | Repositórios de treinamento e dojos de código da comunidade HB Network. | Código de apoio ao ecossistema de ensino (integrações com APIs, microsserviços). | Python |

### 14.2 Implementações do curso feitas pela comunidade

Como o curso é uma construção ao vivo, os repositórios que *reproduzem a cafeteria do zero* são o material mais próximo de um “código do curso”. Dois se destacam:

| Repositório | Descrição | O que tem dentro |
|---|---|---|
| [**virb30/design-api**](https://github.com/virb30/design-api) | “Design de API com Django” — exemplo de implementação dos **níveis de maturidade 0–3**, explicitamente baseado no Django Quickstart do Henrique Bastos. | Estrutura Django completa: `coffeeapi/`, `data/`, `manage.py`, `pytest.ini`, `requirements.txt`, `Procfile` — além de um **diagrama e uma tabela da máquina de estados do pedido** (ver seção 15.3). |
| [**HenriqueCCdA/Design_de_API_na_pratica**](https://github.com/HenriqueCCdA/Design_de_API_na_pratica) | Repositório intitulado “Curso de API do Henrique Bastos” — acompanhamento das aulas em 17 commits. | Três frentes paralelas: `api_django/coffeapi` (a API em Django), `httpd_simples/` (servidor baseado em `http.server` da stdlib) e `maturitylevel/` (experimentos por nível de maturidade). |

Ambos são projetos de terceiros (não oficiais), úteis como referência de implementação — trate-os como estudo comparativo, não como a fonte canônica do curso.

## 15. Exemplos de código reais

Diferente das “ilustrações didáticas” da seção 9, o código abaixo é **real e verificável**: reproduzido dos repositórios públicos do instrutor e da implementação comunitária do curso.

### 15.1 Cliente de API profissional — `RequestsPro` (aula #07 levada a sério)

Este é o exemplo completo do repositório [requests-pro](https://github.com/henriquebastos/requests-pro), um cliente para a API V2 da Eduzz. Ele sintetiza vários ensinamentos do curso em código: sessão própria com `BASE_URL`, autenticação plugável com renovação de token, **tratamento transparente de erros de domínio** (a lista `ERROR_STATUSES` inclui o `409 Conflict` das aulas #08–#09) e clientes “magros”, porque toda a complexidade foi resolvida antes. Reproduzido na íntegra:

```
"""
This is a simple yet complete example of how to use RequestsPro to build a professional API client.
It's a client for the Eduzz API V2. Doc at https://api2.eduzz.com/

The `EduzzClient` is the main client that will be used to interact with the API.
It contains two subclients: `EduzzUserClient` and `EduzzSalesClient`.

The `EduzzSession` is the session that will be used to make the requests.
The `EduzzAuth` is the authentication handler that will transparently authenticate the requests.
The `EduzzResponse` is the response class that handles errors transparently the API error particularities.

The Client and SubClients are simple because we handled all the API crazyness before,
so they are just thin wrappers around the API.
"""

from datetime import datetime
from typing import Any, TypeVar

import pytz
from requests.exceptions import RequestException

from requestspro.auth import RecoverableAuth
from requestspro.client import Client, MainClient
from requestspro.sessions import ProResponse, ProSession
from requestspro.token import TokenStore
from requestspro.utc import utc_now

# Type variables for more descriptive API types
JSON = TypeVar("JSON", bound=dict[str, Any])
Params = TypeVar("Params", bound=dict[str, Any] | None)
Data = TypeVar("Data", bound=dict[str, Any])
TokenData = TypeVar("TokenData", bound=str)
TokenExpiry = TypeVar("TokenExpiry", bound=int)

SAO_PAULO = pytz.timezone("America/Sao_Paulo")

class EduzzAPIError(RequestException):
    """The exception raised for all Eduzz API errors."""

    def __init__(self, message: str, response: ProResponse | None = None):
        super().__init__(message, response=response)

class EduzzResponse(ProResponse):
    """Handles all the API error particularities."""

    ERROR_STATUSES = {400, 401, 403, 404, 405, 409, 422, 500}

    def raise_for_status(self):
        """Handle API logic errors and delegate HTTP errors to the superclass."""
        if self.status_code in self.ERROR_STATUSES:
            json = self.json()
            code, details = json["code"], json["details"]

            msg = f"{code} {details}"
            raise EduzzAPIError(msg, response=self)

        super().raise_for_status()

class EduzzSession(ProSession):
    """Custom session for Eduzz API with proper response handling and JSON encoding."""

    RESPONSE_CLASS = EduzzResponse
    BASE_URL = "https://api2.eduzz.com"

class EduzzAuth(RecoverableAuth):
    """Eduzz V2 API authentication handler."""

    AUTH_PATH = "/credential/generate_token"
    SESSION_CLASS = EduzzSession

    def __init__(self, token, email, publickey, apikey):
        self.credentials = {"email": email, "publickey": publickey, "apikey": apikey}
        super().__init__(token)

    def authorize(self, req):
        req.headers["Token"] = self.token
        return req

    def renew(self, now=utc_now) -> tuple[TokenData, TokenExpiry]:
        """Renew the authentication token."""
        r = self.session_class().post(self.AUTH_PATH, params=self.credentials)
        r.raise_for_status()

        json = r.json()
        token = json["data"]["token"]
        token_valid_until = json["data"]["token_valid_until"]

        # Token expiration date is provided without the explicit TZ, so we need to
        # convert it to the correct timezone and then to UTC.
        dt = datetime.fromisoformat(token_valid_until)
        dt.replace(tzinfo=SAO_PAULO)
        dt = dt.astimezone(pytz.UTC)
        ttl = (dt - now()).total_seconds()

        return token, ttl

class EduzzClient(MainClient):
    """Main client for Eduzz V2 API."""

    @classmethod
    def from_credentials(cls, email, publickey, apikey):
        token = TokenStore.in_memory()
        auth = EduzzAuth(token, email, publickey, apikey)
        session = EduzzSession(auth=auth)
        return cls(session)

    def __init__(self, session: EduzzSession):
        super().__init__(session)

        self.user = EduzzUserSubClient(session)
        self.sales = EduzzSalesSubClient(session)

class EduzzUserSubClient(Client):
    """SubClient for managing your profile in Eduzz."""

    def get_me(self) -> JSON:
        return self.get("/user/get_me")

    def set_me(self, data: Data) -> JSON:
        return self.post("/user/set_me", json=data)

    def my_buys_list(self, params: Params = None) -> JSON:
        return self.get("/user/my_buys_list", params=params)

class EduzzSalesSubClient(Client):
    """SubClient for managing sales in Eduzz."""

    def list(self, params: Params = None) -> JSON:
        return self.get("/sales/get_sale_list", params=params)

    def retrieve(self, sale_id: int) -> JSON:
        return self.get(f"/sale/get_sale/{sale_id}")

    def get_total(self, params: Params = None) -> JSON:
        return self.get("/sale/get_total", params=params)

if __name__ == "__main__":
    client = EduzzClient.from_credentials(email, pubkey, apikey)
    print(client.user.get_me())
```

**Leituras de design neste código**, todas conectadas ao curso:

- **Factory `from_credentials`** — instancia e compõe todas as peças (token store, auth, session, client). O consumidor não conhece a mecânica — exatamente o “desacoplar o cliente” da aula #09.
- **`authorize()` / `renew()`** — a autenticação é uma responsabilidade separada que se injeta na requisição; o retry no 401 é transparente.
- **`ERROR_STATUSES` inclui `409`** — o `409 Conflict` que as aulas #08–#09 usam para “operação inválida para o estado atual” é tratado como erro de domínio, não HTTP genérico.
- **Subclients `user` e `sales`** — a API é organizada por área do domínio, e as subclasses são “thin wrappers” (clientes magros), porque a complexidade ficou na infraestrutura.

### 15.2 Serialização de tipos complexos — `jsonstar` (o bug de `datetime` da aula #07, resolvido)

Na aula #07, Henrique caça um bug de serialização de `datetime` e conclui que é preciso um encoder próprio. O [python-jsonstar](https://github.com/henriquebastos/python-jsonstar) é a biblioteca que ele publicou depois para atacar esse problema de forma geral. É um *drop-in replacement* do `json`:

```
# Troca direta pelo módulo padrão:
import jsonstar as json

from decimal import Decimal
from datetime import date
from pydantic import BaseModel

class Employee(BaseModel):
    name: str
    salary: Decimal
    birthday: date
    roles: set

employee = Employee(
    name="John Doe",
    salary=Decimal("1000.00"),
    birthday=date(1990, 1, 1),
    roles={"A", "B", "C"},
)

print(json.dumps(employee))
# {"name": "John Doe", "salary": "1000.00", "birthday": "1990-01-01", "roles": ["A", "B", "C"]}
```

O ponto crítico para o design de API: **registrar um encoder de moeda com precisão explícita**, resolvendo exatamente a questão “*como representar dinheiro em JSON sem usar float*” da aula #07:

```
import jsonstar as json
from decimal import Decimal

def two_decimals_encoder(obj):
    """Encodes a decimal with only two decimal places."""
    return str(obj.quantize(Decimal("1.00")))

# Registro global (library-wide):
json.register_default_encoder(Decimal, two_decimals_encoder)

# Ou por classe, com encoder tipado:
class MyEncoder(json.JSONEncoderStar):
    _default_typed_encoders = {Decimal: lambda o: str(o.quantize(Decimal("1.00")))}
```

Os encoders padrão já cobrem: `attrs`, `dataclasses`, `date`, `datetime`, `time`, `timedelta`, `Decimal`, `frozenset`, `pydantic.BaseModel`, `set` e `UUID` — e há dois tipos de encoder: *tipados* (por `isinstance`) e *funcionais* (por lógica arbitrária).

### 15.3 A máquina de estados do Pedido, em tabela (implementação comunitária)

O repositório [virb30/design-api](https://github.com/virb30/design-api) documenta em seu README a máquina de estados do pedido da cafeteria exatamente como modelada nas aulas #08–#09 — inclusive com os **status code de sucesso e de erro** e os **hyperlinks** devolvidos em cada transição. É o artefato de design do Nível 3 materializado:

| Ação | Verbo | URL | Lógica de negócio | Sucesso | Erro | Hyperlinks |
|---|---|---|---|---|---|---|
| **Pedir** | POST | `/order` | Cria um novo pedido | `201` | — | self, update, cancel, payment |
| **Atualizar** | PUT | `/order/{id}` | Atualiza o pedido, *se e somente se* o status for “Aguardando Pagamento” | `200` | `409` | self, update, cancel, payment |
| **Cancelar** | DELETE | `/order/{id}` | Muda o status para Cancelado, *se e somente se* “Aguardando Pagamento” | `204` | `409` | — |
| **Pagar** | PUT | `/payment/{id}` | Realiza o pagamento e muda para Pago, *se e somente se* “Aguardando Pagamento” | `200` | `409`, `422` | self, receipt |
| **Aguardar** | — | — | Um funcionário prepara o pedido | — | — | — |
| **Receber** | DELETE | `/receipt/{id}` | Confirma o recebimento mudando para “Entregue”, *se e somente se* Pronto | `204` | `409` | — |
| — | GET | `/order/{id}` | Retorna a última representação do recurso pedido | `200` | — | **Depende do status** |

**Por que esta tabela é a síntese do curso:** ela mostra, em uma única página, os quatro conceitos que a série persegue — o verbo HTTP escolhido pela *semântica do domínio* (não pelo CRUD), o `409 Conflict` como exceção de estado, os hyperlinks mudando conforme o status, e a coluna “se e somente se” representando as **transições válidas da máquina de estados**. É literalmente o “HTTP como máquina de estado da aplicação” da aula #08.

## 16. Análise linha a linha: os níveis no código real

Esta seção é o resultado de **clonar e ler o código-fonte** dos repositórios da comunidade que implementam o curso. Todos os trechos abaixo são **código real**, copiado dos arquivos, com o caminho e o número de linha indicados — não são ilustrações.

### 16.0 A organização: cada nível é um app Django

O repositório `virb30/design-api` resolve o problema didático de forma elegante: em vez de um projeto por nível, há **quatro apps Django paralelos no mesmo projeto**, um por nível de maturidade. É possível rodar todos e comparar o comportamento lado a lado — exatamente a ideia que o Henrique propõe na aula #04 (“o mesmo projeto com todos os níveis para você comparar facilmente”).

```
coffeeapi/
├── urls.py                  # dispatcher: inclui os 4 níveis
├── settings.py
├── level0/                  # Nível 0 — POX / túnel RPC
│   ├── urls.py, views.py, domain.py
├── level1/                  # Nível 1 — URIs por recurso
│   ├── urls.py, views.py, domain.py, framework.py
├── level2/                  # Nível 2 — verbos HTTP + status
│   ├── urls.py, views.py, domain.py
│   └── framework/           # decorators, http, middleware, serializers, tests
└── level3/                  # Nível 3 — hypermedia (HATEOAS)
    ├── urls.py, views.py, domain.py
    └── framework/           # idem + Conflict (409)
```

O dispatcher raiz (`coffeeapi/urls.py`) revela um detalhe sutil de design — a **ordem de inclusão importa**:

```
urlpatterns = [
    path('', include('coffeeapi.level0.urls')),
    path('', include('coffeeapi.level1.urls')),
    path('', include('coffeeapi.level3.urls')),
    path('', include('coffeeapi.level2.urls')),   # ← por último, de propósito
]
```

O nível 2 é incluído por último porque sua rota é um regex amplo (`order(?:/(?P<id>\d+))?`). Se viesse antes, poderia capturar requisições destinadas ao nível 1 (`order/read`, `order/create`). Como o regex só casa dígitos após a barra, `order/read` não casa — mas a ordem defensiva evita surpresas. **Isto é design de fronteira na prática.**

### 16.1 Nível 0 — uma URI, um verbo, texto puro

**Arquivo:** `coffeeapi/level0/urls.py` (7 linhas, na íntegra)

```
from django.urls import path
from .views import barista

urlpatterns = [
    path('PlaceOrder', barista),
]
```

**Leitura linha a linha:** existe **uma única rota** no sistema — `PlaceOrder` — e ela é um *verbo* escrito na URL, não um recurso. Não há identificador de pedido na URL, não há coleção, não há item. É a assinatura exata do Nível 0: “uma URI só, e o payload empurrado através dela”.

**Arquivo:** `coffeeapi/level0/views.py` — a view completa, com o comentário do próprio autor

```
def barista(request):
    """
    http://localhost:8000/PlaceOrder?coffee=latte&size=large&milk=whole&location=takeAway
    - Erro com status code 200. Trocar para BadRequest.
    - GET com efeito colateral.
    - Impossível de cachear.
    """
    try:
        params = {k: request.GET[k]
                  for k in ('coffee', 'size', 'milk', 'location')}
    except MultiValueDictKeyError as e:
        status = 400
        headers = {'Content-Type': 'text/plain; charset=utf-8'}
        body = str(e).strip("'")
        return HttpResponse(body, status=status, headers=headers)

    order = Order(**params)
    coffeeshop.place_order(order)

    body = f'Order={order.id}'
    headers = {'Content-Type': 'text/plain; charset=utf-8'}

    return HttpResponse(body, headers=headers)
```

**Leitura linha a linha — cada defeito é intencional e didático:**

| Linha / trecho | O que está acontecendo | Nível de maturidade |
|---|---|---|
| Docstring | O autor *documenta os próprios defeitos*: “Erro com status code 200”, “GET com efeito colateral”, “Impossível de cachear”. É um Nível 0 consciente. | — |
| `request.GET[k]` | Todos os dados de negócio vêm da **query string**, inclusive numa operação que **cria estado**. A semântica HTTP não é usada. | 0 |
| `except MultiValueDictKeyError` | Validação de entrada delegada a uma exceção de estrutura de dados do Django — não há contrato de payload. | 0 |
| `body = f'Order={order.id}'` | A resposta é **texto livre** (`text/plain`), não uma representação estruturada. O cliente terá que fazer *parsing por regex* — ver seção 16.5. | 0 |
| `status = 400` local | O 400 é um **número mágico** e só existe no caminho de erro; o caminho de sucesso retorna 200 mesmo criando um recurso (deveria ser 201). | 0 |

**A prova do Nível 0 está nos testes** — `coffeeapi/level0/tests/test_api.py`:

```
def test_get(client, coffeeshop):
    url = '/PlaceOrder?coffee=latte&size=large&milk=whole&location=takeAway'
    response = client.get(url)
    assert len(coffeeshop.orders) == 1
    assert b'Order=1' == response.content

def test_post(client, coffeeshop):
    url = '/PlaceOrder?coffee=latte&size=large&milk=whole&location=takeAway'
    response = client.post(url)          # ← o MESMO url, agora com POST
    assert len(coffeeshop.orders) == 1
    assert b'Order=1' == response.content
```

Os dois testes passam com o **mesmo resultado**, um com `GET` e outro com `POST`. Isso só é possível porque a view **ignora completamente o método HTTP** — ela nem consulta `request.method`. Um teste que documenta a ausência de semântica de verbo vale mais que um parágrafo de teoria.

### 16.2 Nível 1 — URIs por recurso, verbos e um framework nascendo

**Arquivo:** `coffeeapi/level1/urls.py` (na íntegra)

```
urlpatterns = [
    path('order/read', views.read),
    path('order/create', views.create),
    path('order/delete', views.delete),
    path('order/update', views.update),
]
```

**Leitura linha a linha:** saímos de *uma* URI para **quatro**. Já há separação de recursos lógicos (“order”). Mas repare: **a ação continua escrita na URL** (`/read`, `/create`, `/delete`, `/update`) — é o “preso a template de URI” que o Henrique descreve na aula #05. É o Nível 1 em estado puro: *URIs melhores, semântica de verbo ainda incompleta*.

**Arquivo:** `coffeeapi/level1/views.py` — as views, com os decorators

```
coffeeshop = init_persistent_system(CoffeeShop(), basedir='data/level1')

@allow('POST')
@require('coffee', 'size', 'milk', 'location')
def create(request, params=None):
    order = Order(**params)
    coffeeshop.create(order)
    return Created(serialize(order))

@allow('POST')
@require('id')
def delete(request, params=None):
    order = Order(**params)
    coffeeshop.delete(order)
    return NoContent()

@allow('GET')
@require('id')
def read(request, params=None):
    order = coffeeshop.read(**params)
    return Ok(serialize(order))
```

**Leitura linha a linha:**

- `@allow('POST')` — agora o método HTTP **é** validado; uma requisição com verbo errado recebe `405`. Isto já é um salto em relação ao Nível 0.
- **Mas** `create`, `delete` e `update` usam *todos* `POST` — e é justamente o `id` que vai na query string, não na URL. A semântica do verbo ainda não carrega o significado da operação.
- `@require('id')` lê de `request.GET` — os parâmetros ainda viajam na URL.
- `init_persistent_system(CoffeeShop(), basedir='data/level1')` — cada nível persiste em **seu próprio diretório** (`data/level0`, `data/level1`…), o que confirma a ideia de rodar os quatro em paralelo. É a persistência leve por *prevalence* discutida na aula #03.

**Arquivo:** `coffeeapi/level1/framework.py` — o “framework” caseiro nasce aqui, e é onde aparecem as ideias da aula #05:

```
from http import HTTPStatus

class Created(MyResponse):
    status_code = HTTPStatus.CREATED

class NotFound(MyResponse):
    status_code = HTTPStatus.NOT_FOUND

class NoContent(MyResponse):
    status_code = HTTPStatus.NO_CONTENT

class allow:
    def __init__(self, *methods):
        self.allowed = tuple(m.upper() for m in methods)

    def __call__(self, view):
        @functools.wraps(view)
        def wrapper(request):
            if request.method not in self.allowed:
                return MethodNotAllowed()
            return view(request)

        return wrapper
```

**Leitura linha a linha:** exatamente os três ensinamentos da aula #05 materializados:

1. **Fim dos números mágicos** — `HTTPStatus.CREATED` em vez de `201`. As classes de resposta dão nome ao design.
2. **Decorator `allow`** — construído com `functools.wraps`, intercepta a requisição e devolve `MethodNotAllowed` (405). É o “framework de decorators que limpa as views” da aula.
3. **Handler de exceção** — o middleware mapeia `DoesNotExist` → `NotFound()`, tirando o tratamento de erro de dentro da view.

E a serialização ainda é texto puro — `serialize()` devolve `key=value` unidos por quebra de linha:

```
def serialize(obj):
    return '\n'.join((f'{k}={v}' for k, v in sorted(vars(obj).items())))
```

### 16.3 Nível 2 — o verbo comanda, o JSON chega, o 201+Location aparece

**Arquivo:** `coffeeapi/level2/urls.py` (na íntegra) — *a* mudança de paradigma

```
urlpatterns = [
    re_path(r'order(?:/(?P<id>\d+))?', views.dispatch, name='order'),
]
```

**Leitura linha a linha:** as quatro URIs de ação desapareceram. Agora existe **uma rota que representa o recurso** `order`, com um segmento **opcional** que captura o `id`:

- `/order` → a **coleção** (sem id)
- `/order/1` → o **item** (com id)

Nenhuma ação está escrita na URL. *A operação agora é determinada pelo verbo HTTP* — e é isso que o `dispatch` faz:

```
@allow('GET', 'POST', 'PUT', 'DELETE')
def dispatch(request, *args, **kwargs):
    methods = dict(GET=read, POST=create, PUT=update, DELETE=delete)
    view = methods[request.method]

    return view(request, *args, **kwargs)
```

**Leitura linha a linha:** este dicionário é a **tabela de roteamento por verbo** — o coração do Nível 2. `POST` cria, `GET` lê, `PUT` atualiza, `DELETE` remove. A URL diz *o quê* (o recurso); o verbo diz *o quê fazer com ele*. É a interface uniforme descrita na aula #02.

**Arquivo:** `coffeeapi/level2/views.py` — o `create` com `Location` e o corpo em JSON

```
@allow('POST')
@datarequired('coffee', 'size', 'milk', 'location')
def create(request, params=None):
    order = Order(**params, status=Status.Placed)
    coffeeshop.create(order)

    return Created(
        serialize(order),
        headers={'Location': abs_reverse(request, 'order', args=(order.id,))}
    )
```

**Leitura linha a linha:**

- `@datarequired` substituiu `@require`: agora o payload vem de `json.loads(request.body)`, não mais da query string. **Os dados saíram da URL.**
- `Created(...)` devolve **201**, não mais 200.
- `headers={'Location': ...}` — o padrão REST de devolver no header **onde o recurso recém-criado pode ser encontrado**. O `abs_reverse` monta a URL absoluta a partir do nome da rota (`'order'`) e do id.
- `status=Status.Placed` — o domínio ganhou um **enum de estado**, pré-condição para o Nível 3.

**Arquivo:** `coffeeapi/level2/framework/serializers.py` — a “interface virtual” da aula #07, em código

```
class IMySerializable(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasscheck__(cls, subclass):
        return (
            hasattr(subclass, 'vars') and
            callable(subclass.vars)
        )

class MyJSONEncoder(DjangoJSONEncoder):
    def encode(self, o):
        if isinstance(o, IMySerializable):
            o = o.vars()
        return super().encode(o)
```

**Leitura linha a linha:** `IMySerializable` não exige herança — ela redefine `__subclasscheck__` para reconhecer *qualquer classe que tenha um método `vars()` chamável*. É **duck typing formalizado**: o `isinstance(o, IMySerializable)` no encoder passa a funcionar por *estrutura*, não por hierarquia. Isto é literalmente a “classe base virtual com `abc.ABCMeta` e `__subclasshook__`” que o Henrique demonstra na aula #07 — aqui escrito como `__subclasscheck__`.

E o decoder implementa exatamente o tratamento de `datetime` que causava o bug da aula #07:

```
class MyJSONDecoder(JSONDecoder):
    def __init__(self, *args, **kwargs):
        super().__init__(object_hook=self.hook, *args, **kwargs)

    @staticmethod
    def hook(source):
        d = {}
        for k, v in source.items():
            if isinstance(v, str) and not v.isdigit():
                try:
                    d[k] = datetime.fromisoformat(v)
                except (ValueError, TypeError):
                    d[k] = v
            else:
                d[k] = v
        return d
```

**Leitura linha a linha:** o `object_hook` tenta converter cada string que “parece data” em `datetime`, e faz *fallback silencioso* para a string original se falhar. Note o cuidado: `not v.isdigit()` protege números puros (como `"199"` de centavos) de virarem data. É a resposta prática ao problema de tipos de alto nível em JSON.

**Arquivo:** `coffeeapi/level2/framework/tests.py` — a metaprogramação da aula #06, na íntegra

```
APIClient = type('APIClient',
                 (Client,),
                 {
                     '__init__': partialmethod(Client.__init__, json_encoder=MyJSONEncoder),
                     '_parse_json': partialmethod(Client._parse_json, cls=MyJSONDecoder),
                     **{verb: partialmethod(getattr(Client, verb), content_type=DEFAULT_CT)
                        for verb in ('post', 'get', 'put', 'delete')},
                 }
)
```

**Leitura linha a linha:** a classe `APIClient` é **construída em tempo de execução** por `type()`, não declarada com `class`. O dicionário de atributos usa uma *compreensão* para gerar os quatro métodos HTTP (`post`, `get`, `put`, `delete`) já configurados com `content_type=application/json`. O bloco comentado logo acima (linhas 6–21) mostra a versão ingênua, com quatro métodos escritos à mão — **o comentário preserva a evolução: boilerplate substituído por metaprogramação.** Isto é a aula #06 (“reduzir a verbosidade dos testes criando dinamicamente métodos que encapsulam o Content-Type”) preservada como documentação viva.

### 16.4 Nível 3 — a máquina de estados e o hypermedia

**Arquivo:** `coffeeapi/level3/urls.py` (na íntegra)

```
urlpatterns = [
    re_path(r'v3/order(?:/(?P<id>\d+))?', views.dispatch, name='orderv3'),
    path('v3/receipt/<int:id>', views.receipt, name='receipt'),
    path('v3/payment/<int:id>', views.payment, name='payment'),
]
```

**Leitura linha a linha:** aparecem **dois recursos novos** que *não são entidades de banco*: `payment` e `receipt`. Eles representam **etapas do processo de negócio** — exatamente a tese da aula #02 (“o recurso da sua API não precisa ser algo que vai ser guardado no banco; um processo ou workflow também pode ser um recurso”). O prefixo `v3/` também sugere o versionamento por URI.

**Arquivo:** `coffeeapi/level3/views.py` — o HATEOAS, o coração do Nível 3

```
def order_links(request, order):
    link_to_self = abs_reverse(request, 'orderv3', args=(order.id,))

    links = {}
    if order.is_placed():
        links.update(
            self=link_to_self,
            update=link_to_self,
            cancel=link_to_self,
            payment=abs_reverse(request, 'payment', args=(order.id,))
        )
    elif order.is_paid():
       links.update(
            self=link_to_self,
        )
    elif order.is_served():
       links.update(
            self=link_to_self,
            receipt=abs_reverse(request, 'receipt', args=(order.id,))
        )

    return links
```

**Leitura linha a linha — este é o trecho mais importante de todo o Nível 3:**

| Estado do pedido | Links oferecidos | Interpretação de negócio |
|---|---|---|
| `is_placed()` (aguardando pagamento) | `self`, `update`, `cancel`, `payment` | O cliente **pode** alterar, cancelar ou pagar — as três ações válidas neste estado. |
| `is_paid()` (pago) | apenas `self` | O cliente **não pode mais** alterar nem cancelar. Os links simplesmente *desaparecem* da resposta. |
| `is_served()` (pronto) | `self`, `receipt` | Só resta confirmar o recebimento. |

Este `if/elif` **é** a máquina de estados da aula #08 escrita como código: “existe uma relação entre links possíveis e o status da sua ordem” (aula #09). O cliente não precisa saber as regras de negócio — **ele descobre o que pode fazer lendo os links**. É o “desacoplar um pouco mais o cliente” da aula #09, literal.

E os links são injetados em *toda* representação devolvida:

```
@allow('GET')
def read(request, id):
    order = coffeeshop.read(id)

    d = order.vars()
    d['links'] = order_links(request, order)

    return Ok(serialize(d))
```

**Arquivo:** `coffeeapi/level3/domain.py` — as guardas de estado

```
def delete(self, id):
    order = self.read(id)

    if order.status != Status.Placed:
        raise Conflicted()

    order.status = Status.Cancelled
    return order

def update(self, order):
    saved = self.read(order.id)

    if saved.status != Status.Placed:
        raise Conflicted()
    ...

def pay(self, id, amount):
    amount = Decimal(amount) / 100
    order = self.read(id)

    if order.is_paid():
        raise Conflicted(id)

    if amount == order.price:
        order.status = Status.Paid
    return order
```

**Leitura linha a linha:**

- `if order.status != Status.Placed: raise Conflicted()` — as transições só acontecem **no estado permitido**. É a coluna “se e somente se” da tabela do README, implementada.
- `raise Conflicted()` — uma **exceção de domínio**, não HTTP. A aula #08 prevê exatamente isto: “a existência da possibilidade de conflito já indica que eu vou ter um novo tipo de exceção”.
- `Decimal(amount) / 100` — o dinheiro é tratado em **centavos inteiros convertidos para `Decimal`**, nunca `float`. É a solução ao problema de moeda da aula #07. O `# TODO: mover para deserialize` logo acima mostra o autor sabendo que a conversão pertence à camada de desserialização — os **metadados** que a aula #07 pede ainda estão faltando.
- `O_PATRAO_ESTA_MALUCO = Decimal('1.99')` — o preço fixo, em `Decimal`, com um nome que é puro humor de live coding.

A exceção de domínio é traduzida para HTTP por um middleware:

```
class FrameworkCommonExceptionHandler:
    def process_exception(self, request, exc):
        if isinstance(exc, DoesNotExist):
            return NotFound()
        elif isinstance(exc, Conflicted):
            return Conflict()
```

E o `Conflict` é uma classe de resposta nova no Nível 3 — a única adição ao `framework/http.py` em relação ao Nível 2:

```
class Conflict(MyResponse):
    status_code = HTTPStatus.CONFLICT   # 409
```

**Esta é a assinatura do Nível 3 no código:** uma classe `Conflict` (409) + um `if/elif` de estados gerando links. Nada mais.

**Arquivo:** `coffeeapi/level3/tests/test_api_payment.py` — o contrato do Nível 3 em cinco asserções

```
def test_payment_success(apiclient, onecoffee):
    response = apiclient.put('/v3/payment/1', data=dict(amount=199))
    assert response.status_code == HTTPStatus.OK
    links = dict(self='http://testserver/v3/order/1')
    assert response.json() == dict(links=links)
    assert onecoffee.read(1).is_paid()

def test_payment_method_not_allowed(apiclient, onecoffee):
    response = apiclient.post('/v3/payment/1')
    assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED   # 405

def test_payment_not_found(apiclient, onecoffee):
    response = apiclient.put('/v3/payment/404', data=dict(amount='199'))
    assert response.status_code == HTTPStatus.NOT_FOUND            # 404

def test_payment_already_paid(apiclient, onecoffee):
    onecoffee.read(1).status = Status.Paid
    response = apiclient.put('/v3/payment/1', data=dict(amount=199))
    assert response.status_code == HTTPStatus.CONFLICT             # 409
```

**Leitura linha a linha:** em um único arquivo de teste estão os **quatro status codes que definem a maturidade** — `200` (sucesso), `405` (verbo errado), `404` (recurso inexistente) e `409` (operação inválida para o estado). E o teste de sucesso verifica que a resposta traz **os links**, com `self` apontando para `/v3/order/1`. Note também que após pagar, o pedido *só* oferece `self` — os links de `update`/`cancel` sumiram, exatamente como o `order_links` promete.

### 16.5 O cliente — onde a dor do Nível 0/1 aparece concretamente

O repositório `HenriqueCCdA/Design_de_API_na_pratica` contém os clientes escritos nas aulas. Eles são a **melhor evidência empírica** do argumento da aula #07 (“fazer um client para sua API vira um inferno”).

**Arquivo:** `client_level0/core.py` (na íntegra) — o cliente do Nível 0

```
def place_order(coffee, size, milk, location):
    url = f'{BASE_URL}/PlaceOrder?coffee={coffee}&size={size}&milk={milk}&location={location}'

    r = requests.get(url)

    order_id = ''.join(re.findall(r'Order=(\d+)', r.text))

    return order_id
```

**Leitura linha a linha:** o cliente é obrigado a **expressão regular** (`re.findall(r'Order=(\d+)')`) para extrair o ID do pedido de uma resposta em texto livre. Além disso usa `requests.get` para uma operação de escrita — o acoplamento com o defeito do servidor é total. Um único caractere a mais ou a menos na string do servidor quebra o cliente silenciosamente. **É a “gambiarra” que a série quer eliminar, capturada em 6 linhas.**

**Arquivo:** `client_level1/client.py` — o cliente do Nível 1, agora parseando `key=value`

```
def deserialize(body):
    return {k: v for k, v in [item.split('=') for item in body.split()]}

def create_order(coffee, size, milk, location):
    url = f'{BASE_URL}/order/create'
    params = {'coffee': coffee, 'size': size, 'milk': milk, 'location': location}
    r = requests.post(url, params=params, headers={'Content-Type': 'text/plain'})
    order = deserialize(r.text)
    return int(order['id'])
```

**Leitura linha a linha:** melhorou — o cliente agora tem um `deserialize` e o servidor devolve pares nomeados. Mas o parsing ainda é **manual, feito por `split('=')`**, e o `Content-Type: text/plain` precisa ser declarado à mão em cada chamada. Cada operação é um método separado que o cliente precisa conhecer (`create_order`, `delete_order`, `read_order`, `update_order`) — e `update_order` reenvia *todos* os campos. **A URL de ação (`/order/create`) está hardcoded em cada função**: se o servidor mudar a rota, o cliente quebra.

Compare com o cliente do Nível 3 — o cliente não precisa saber as regras: ele lê os links. *A diferença entre os dois arquivos é a diferença entre os níveis.*

**Bônus — “abaixando o nível de abstração” (aula #02) em código:** o diretório `httpd_simples/` contém um servidor HTTP escrito sobre a biblioteca padrão, mostrando o que um framework esconde:

```
class MyHTTPHandler(BaseHTTPRequestHandler):
    def handle_one_request(self):
        ...
        print(self.command, self.path)
        if self.command == 'GET':
            if self.path == '/':
                self.send_response(HTTPStatus.OK)
                self.send_header("Content-type", "text/html; charset=utf-8")
                self.end_headers()
                body = '''<h1>O Servidor tá ON!</h1>'''
                self.wfile.write(body.encode('utf-8', 'replace'))

            elif self.path == '/blog':
                self.send_response(HTTPStatus.PERMANENT_REDIRECT)
                self.send_header('Location', 'https://henriquebastos.net/blog')
                self.end_headers()

            elif self.path == '/api/order/1':
                self.send_response(HTTPStatus.OK)
                self.send_header("Content-type", "text/html; charset=utf-8")
                self.end_headers()
                body = '{"id": 1, "product": "Café"}'
                self.wfile.write(body.encode('utf-8', 'replace'))
        else:
            self.send_error(HTTPStatus.NOT_IMPLEMENTED, ...)
```

**Leitura linha a linha:** aqui está o HTTP *cru*, sem Django: um `if/elif` sobre `self.path`, o `send_response` com o status explícito, o `send_header('Location', ...)` de um redirect 308, e um JSON escrito como string literal. É a “ferramenta sem magia” — e explica por que o Henrique insiste (aula #06) que *entender por que o framework esconde a fronteira* é o verdadeiro desafio do design.

### 16.6 O que o código real ensina (síntese da análise)

| Conceito do curso | Como aparece no código | Nível |
|---|---|---|
| Uma URI, verbo ignorado | `path('PlaceOrder', barista)`; teste passa com GET *e* POST | 0 |
| Resposta em texto livre | `body = f'Order={order.id}'` + cliente com `re.findall(r'Order=(\d+)')` | 0 |
| URIs por recurso | `order/read`, `order/create`, `order/delete`, `order/update` | 1 |
| Fim dos números mágicos | `status_code = HTTPStatus.CREATED`; classes `Ok`, `NotFound`, `NoContent` | 1 |
| Decorators contra boilerplate | `@allow('POST')`, `@require(...)` com `functools.wraps` | 1 |
| Interface uniforme (verbo comanda) | `methods = dict(GET=read, POST=create, PUT=update, DELETE=delete)` | 2 |
| Recurso coleção vs. item | `re_path(r'order(?:/(?P<id>\d+))?', ...)` | 2 |
| 201 + Location | `Created(serialize(order), headers={'Location': abs_reverse(...)})` | 2 |
| Interface virtual (`ABCMeta`) | `IMySerializable.__subclasscheck__` reconhecendo por `hasattr('vars')` | 2 |
| Metaprogramação em testes | `APIClient = type('APIClient', (Client,), {...})` com `partialmethod` | 2 |
| Recurso como processo, não tabela | `v3/payment/<int:id>` e `v3/receipt/<int:id>` | 3 |
| HTTP como máquina de estados | `order_links()` com `if is_placed / elif is_paid / elif is_served` | 3 |
| Exceção de domínio → 409 | `raise Conflicted()` → middleware → `class Conflict(HTTPStatus.CONFLICT)` | 3 |
| Dinheiro sem float | `Decimal(amount) / 100` comparado com `price = Decimal('1.99')` | 3 |

#### Observações honestas sobre o código analisado

Como este é código de estudo, escrito ao vivo, ele contém imperfeições reais que vale registrar — e que são, elas mesmas, lições:

- **Método `pay` duplicado** em `level3/domain.py`: há duas definições de `pay` (linhas 109 e 119). Em Python a segunda sobrescreve a primeira, então a versão sem validação de valor é *código morto*. É o “primeiro faz funcionar” da aula #09 deixando rastro.
- **Divergência entre README e código no `deliver`**: a tabela do README diz que “Receber” só vale “se e somente se o status for Pronto”, mas o código só verifica se o pedido *já* foi coletado (`if order.is_collected(): raise Conflicted()`) — não exige o estado “Pronto”.
- **`# TODO`s do autor**: `# TODO: mover para deserialize`, `# TODO: Atualizar a desserialização do price`, `# TODO: parece igual ao read`. São precisamente as lacunas que a aula #07 aponta (metadados para conversão de moeda) e que o `jsonstar` vem resolver.
- **`import Decimal` não usado** em `level3/views.py`.

Nada disso invalida o material — ao contrário: mostra que a evolução de maturidade é um processo, não um interruptor, e que um repositório de estudo é um artefato honesto do caminho percorrido.

## 17. Execução real: testes e respostas HTTP dos 4 níveis

Esta seção não é análise de leitura — é o resultado de **executar o projeto clonado** no sandbox. Os números e respostas abaixo são **saída real de terminal**, não reconstrução.

### 17.1 Ambiente de execução

O projeto foi escrito para **Django 3.2.4**, que não roda em Python 3.12 (a versão disponível no sandbox). Subimos o ambiente com **Django 4.2.30** — a última versão que ainda preserva `django.utils.datetime_safe`, módulo que o projeto importa. O pacote `coopy` (persistência por *prevalence*) foi instalado via pip, e as variáveis `SECRET_KEY` e `ALLOWED_HOSTS` foram definidas no ambiente — o projeto as lê com `python-decouple`.

```
$ python3 -m venv .venv
$ .venv/bin/pip install "Django==4.2.*" pytest pytest-django pytest-mock python-decouple coopy
$ export SECRET_KEY=test-key DEBUG=False ALLOWED_HOSTS=testserver

django 4.2.30    coopy OK
```

Nenhuma linha do código do repositório foi alterada — apenas o ambiente foi preparado.

### 17.2 Resultado dos testes, nível por nível

```
$ for lvl in 0 1 2 3; do pytest coffeeapi/level$lvl/ -q; done

──────── LEVEL 0 ────────
2 passed, 10 warnings in 0.07s

──────── LEVEL 1 ────────
15 passed, 10 warnings in 0.10s

──────── LEVEL 2 ────────
9 passed, 6 skipped, 10 warnings in 0.08s

──────── LEVEL 3 ────────
22 passed, 10 warnings in 0.11s
```

| Nível | Testes passando | Pulados | Tempo | O que a suíte cobre |
|---|---|---|---|---|
| 0 | **2** | 0 | 0.07s | Apenas que GET e POST produzem o mesmo efeito — a suíte é minúscula porque *não há contrato para testar*. |
| 1 | **15** | 0 | 0.10s | Criação, leitura, atualização, remoção, verbo inválido (405) e recurso inexistente (404). |
| 2 | **9** | 6 | 0.08s | Os quatro verbos, mais os casos de erro por verbo. Seis testes ficam marcados como pulados no próprio repositório. |
| 3 | **22** | 0 | 0.11s | Além dos verbos: `payment`, `receipt`, os conflitos de estado (409) e a **presença dos links** na resposta. |

**Total: 48 testes passando, 6 pulados.** O dado revelador não é a contagem absoluta, e sim a *curva*: **2 → 15 → 9 → 22**. O Nível 0 tem dois testes porque quase não há comportamento a especificar; a suíte explode no Nível 1, quando o contrato passa a existir; e atinge o máximo no Nível 3, porque **uma API com máquina de estados tem muito mais casos de borda legítimos** — e o design maduro os torna testáveis.

### 17.3 A mesma intenção, quatro respostas diferentes

O experimento a seguir dispara, contra os quatro níveis em execução, a **mesma intenção de negócio** — “criar um pedido de latte grande com leite integral para viagem”. Saída literal do terminal:

#### Nível 0 — a resposta é uma string de texto

```
Criar pedido
  GET /PlaceOrder?coffee=latte&size=large&milk=whole&location=takeAway
  -> HTTP 200
  -> Content-Type: text/plain; charset=utf-8
  -> Body: 'Order=1'

Mesma URI, agora com POST (o método é ignorado)
  POST /PlaceOrder?coffee=latte&size=large&milk=whole&location=takeAway
  -> HTTP 200
  -> Content-Type: text/plain; charset=utf-8
  -> Body: 'Order=2'

Faltando um parâmetro
  GET /PlaceOrder?coffee=latte&size=large&milk=whole
  -> HTTP 400
  -> Body: 'location'
```

**Três defeitos, todos confirmados na prática:**

1. **Criação devolve 200, não 201.** O status não distingue “criei algo novo” de “aqui está algo existente”.
2. **GET e POST têm o mesmo efeito.** O segundo pedido foi criado com `POST` e recebeu `Order=2` — prova de que o método HTTP é irrelevante para a view.
3. **O erro devolve apenas `'location'`** — o nome do campo que faltou, cru, sem contrato nem estrutura.

E o corpo `'Order=1'` é o motivo pelo qual o cliente precisa de expressão regular (seção 16.5).

#### Nível 1 — status correto, mas corpo ainda textual

```
Criar pedido
  POST /order/create?coffee=latte&size=large&milk=whole&location=takeAway
  -> HTTP 201
  -> Content-Type: text/plain; charset=utf-8
  -> Body: 'coffee=latte\nid=1\nlocation=takeAway\nmilk=whole\nsize=large'

Ler pedido
  GET /order/read?id=1
  -> HTTP 200
  -> Body: 'coffee=latte\nid=1\nlocation=takeAway\nmilk=whole\nsize=large'

Verbo errado no endpoint de criação
  GET /order/create?coffee=latte&size=large&milk=whole&location=takeAway
  -> HTTP 405
  -> Body: 'Specified method is invalid for this resource'

Pedido inexistente
  GET /order/read?id=999
  -> HTTP 404
  -> Body: ''
```

**O salto é visível:** o Nível 1 já devolve `201` ao criar, `405` para verbo errado e `404` para recurso inexistente. Mas o **corpo continua sendo texto** (`text/plain`) com pares `chave=valor` separados por quebra de linha — o `Content-Type` ainda não anuncia JSON, e o cliente continua obrigado a fazer parsing manual. É literalmente o `serialize()` de `level1/framework.py` que lemos na seção 16.2.

#### Nível 2 — JSON, 201 + Location, e os erros ficam consistentes

```
Criar pedido
  POST /order
  -> HTTP 201
  -> Location: http://testserver/order/1
  -> Content-Type: application/json
  -> Body: '{"id": 1, "coffee": "latte", "size": "large", "milk": "whole",
            "location": "takeAway", "created_at": "2026-09-23T19:06:07.258",
            "status": "Placed"}'

Ler o pedido recém-criado
  GET /order/1
  -> HTTP 200
  -> Body: '{... "status": "Placed"}'

PUT substitui integralmente
  PUT /order/1
  -> HTTP 204

DELETE remove
  DELETE /order/1
  -> HTTP 204

Pedido inexistente
  GET /order/999
  -> HTTP 404

Corpo JSON incompleto
  POST /order   (body: {"coffee": "latte"})
  -> HTTP 400
  -> Body: 'Bad request.'
```

**Aqui a API vira uma API de verdade:** o mesmo endpoint `/order` responde a POST/GET/PUT/DELETE; o `Content-Type` passa a ser `application/json`; a criação devolve **`201` com o header `Location`** apontando para o recurso novo; e `PUT`/`DELETE` devolvem `204 No Content`, como manda a semântica. Repare que o `status` já aparece no corpo (`"Placed"`) — mas *sem links*.

#### Nível 3 — a resposta passa a carregar as ações possíveis

```
Criar pedido (repare no campo 'links')
  POST /v3/order
  -> HTTP 201
  -> Location: http://testserver/v3/order/1
  -> Body: '{"id": 1, ..., "status": "Placed",
            "links": {
               "self":    "http://testserver/v3/order/1",
               "update":  "http://testserver/v3/order/1",
               "cancel":  "http://testserver/v3/order/1",
               "payment": "http://testserver/v3/payment/1"}}'

PAGAR o pedido (PUT /v3/payment/1, amount=199 = R$ 1,99)
  PUT /v3/payment/1
  -> HTTP 200
  -> Body: '{"links": {"self": "http://testserver/v3/order/1"}}'

Ler de novo: os links de update/cancel DESAPARECERAM
  GET /v3/order/1
  -> HTTP 200
  -> Body: '{"id": 1, ..., "status": "Paid",
            "links": {"self": "http://testserver/v3/order/1"}}'

Tentar cancelar depois de pago
  DELETE /v3/order/1
  -> HTTP 409
  -> Body: ''
```

**Este é o experimento que prova o Nível 3.** Vamos destacar o que aconteceu, porque é sutil:

1. O pedido nasce no estado `"Placed"` e a resposta oferece **quatro links**: `self`, `update`, `cancel` e `payment`.
2. Depois de pagar, o estado vira `"Paid"` — e a resposta seguinte traz **apenas `self`**. Os links de `update` e `cancel` **sumiram do corpo da resposta**.
3. E a tentativa de cancelar um pedido já pago devolve **`409 Conflict`** — a exceção de domínio `Conflicted` traduzida pelo middleware.

**Por que isso importa:** o cliente *não precisa saber* que um pedido pago não pode ser cancelado. Ele descobre isso lendo os links — se o link `cancel` não está lá, a ação não é possível. A regra de negócio mora no servidor; o cliente apenas navega. É a definição de HATEOAS, e aqui está funcionando, não descrita.

### 17.4 O contraste em uma linha

| Aspecto | N0 | N1 | N2 | N3 |
|---|---|---|---|---|
| Rota para criar | `/PlaceOrder` | `/order/create` | `POST /order` | `POST /v3/order` |
| Método é respeitado? | **não** (GET = POST) | sim (405) | sim | sim |
| Status ao criar | `200` | `201` | `201` | `201` |
| Content-Type | `text/plain` | `text/plain` | `application/json` | `application/json` |
| Location header | — | — | **sim** | **sim** |
| Recurso inexistente | sem contrato | `404` | `404` | `404` |
| Conflito de estado | — | — | — | **`409`** |
| Links de ação no corpo | — | — | — | **sim, dinâmicos** |
| Testes na suíte | 2 | 15 | 9 (+6 skip) | 22 |

**A conclusão que os dados suportam:** a evolução de maturidade não adiciona *features* — não há uma funcionalidade nova entre o Nível 2 e o Nível 3. O que muda é **de quem é a responsabilidade sobre o estado**. No Nível 2, o servidor informa *o que o pedido é* (`"status": "Placed"`) e o cliente precisa saber o que fazer com isso. No Nível 3, o servidor informa *o que o cliente pode fazer* (`links`) — e a regra de negócio deixa de ser duplicada no cliente. É exatamente a tese que o Henrique defende ao longo das nove aulas, agora verificada em terminal.

### 17.5 Verificação cruzada: a curva muda com Django 3.2.4 / Python 3.10?

**Não — e isso é uma informação valiosa.** Rodamos a mesma suíte no ambiente *original* do projeto — **Python 3.10.21 + Django 3.2.4**, exatamente os pins de `requirements.txt` — para testar se a curva 2→15→9→22 era artefato da versão do Django. Ela não é.

| Nível | Django 4.2.30 / Python 3.12.3 | Django 3.2.4 / Python 3.10.21 | Igual? |
|---|---|---|---|
| 0 | 2 passed, 10 warnings | 2 passed, **3 warnings** | ✅ (avisos caem) |
| 1 | 15 passed, 10 warnings | 15 passed | ✅ |
| 2 | 9 passed, 6 skipped | 9 passed, 6 skipped | ✅ |
| 3 | 22 passed, 10 warnings | 22 passed | ✅ |
| **Total** | **48 passed, 6 skipped** | **48 passed, 6 skipped** | **✅ idêntico** |

```
$ uv python install 3.10
Installed Python 3.10.21 in 844ms
$ uv venv --python 3.10 .venv310
$ uv pip install "Django==3.2.4" python-decouple coopy "pytest==7.1.2" "pytest-django==4.5.2"
python 3.10.21 | django 3.2.4 | pytest 7.1.2

──────── LEVEL 0 ────────   2 passed, 3 warnings in 0.12s
──────── LEVEL 1 ────────  15 passed in 0.09s
──────── LEVEL 2 ────────   9 passed, 6 skipped in 0.08s
──────── LEVEL 3 ────────  22 passed in 0.12s
```

#### Por que a curva não muda — e o que isso ensina

**1. A curva mede o design, não o runtime.** A contagem de testes é determinada pelos *arquivos de teste* do repositório, não pela versão do framework. Uma verificação estática confirma: são **2, 15, 15 e 22 funções `def test_`**, distribuídas em `1, 4, 4 e 6` arquivos. No nível 2, as 15 funções se dividem em 9 que executam e 6 que carregam `@pytest.mark.skip` *escrito à mão no código-fonte* — nada condicional à versão. Ou seja: **a forma da curva é uma propriedade do design da API, não do ambiente.** É por isso que ela serve como evidência da tese do curso: qualquer que seja o runtime, uma API Nível 0 tem quase nada a especificar e uma API Nível 3 tem muito.

**2. O ambiente original elimina os avisos.** As 10 warnings por nível no Django 4.2 eram todas de `django.utils.datetime_safe` — módulo que o projeto importa e que foi depreciado depois. Rodando no Django 3.2.4, os avisos caem para 3 (só de `coopy`, que usa `datetime.utcnow()`). Isto confirma que rodar com a versão-alvo é o ambiente correto — e que os avisos não eram defeito do código do curso, mas atrito de versão.

**3. Um achado real: o `requirements.txt` é internamente inconsistente.** Ele pina `asgiref==3.2.10`, mas `Django==3.2.4` exige `asgiref>=3.3.2,<4`. O resolver recusa a instalação: *“Because django==3.2.4 depends on asgiref>=3.3.2,<4 and you require asgiref==3.2.10, we can conclude that your requirements are unsatisfiable.”* Quem clonar o repositório e rodar `pip install -r requirements.txt` hoje **vai falhar**. A instalação só funciona deixando o `asgiref` resolver sozinho. É um lembrete prático: um `requirements.txt` com pins conflitantes é *documentação que mente* — e vale mais registrar o achado do que contorná-lo em silêncio.

### 17.6 Terceira rodada: Django 5.2.17 — a curva *não* sobrevive

**Não, a curva não se mantém no Django 5.x. Ela colapsa por completo: de 48 testes passando para 48 falhando.** Este é o resultado mais instrutivo das três rodadas — porque mostra que uma curva idêntica em 3.2 e 4.2 não garante robustez contra a evolução da dependência.

| Nível | Django 3.2.4 / Py 3.10 | Django 4.2.30 / Py 3.12 | **Django 5.2.17 / Py 3.12** |
|---|---|---|---|
| 0 | 2 passed | 2 passed | **2 failed** |
| 1 | 15 passed | 15 passed | **15 failed** |
| 2 | 9 passed, 6 skipped | 9 passed, 6 skipped | **9 errors, 6 skipped** |
| 3 | 22 passed | 22 passed | **22 errors** |
| **Total** | **48 passed** | **48 passed** | **0 passed / 48 falhas** |

```
═════════ DJANGO 5.2.17 / PYTHON 3.12.3 ═════════
──────── LEVEL 0 ────────
E   ModuleNotFoundError: No module named 'django.utils.datetime_safe'
FAILED coffeeapi/level0/tests/test_api.py::test_get
FAILED coffeeapi/level0/tests/test_api.py::test_post
2 failed, 31 warnings in 0.29s

──────── LEVEL 1 ────────
E   ModuleNotFoundError: No module named 'django.utils.datetime_safe'
15 failed, 184 warnings in 1.28s

──────── LEVEL 2 ────────
E   AttributeError: module 'coffeeapi.level2' has no attribute 'views'
6 skipped, 9 errors in 0.06s

──────── LEVEL 3 ────────
E   AttributeError: module 'coffeeapi.level3' has no attribute 'views'
22 errors in 0.11s
```

#### Causa raiz: um módulo que deixou de existir

O `django.utils.datetime_safe` foi **removido do Django no 5.0** (havia sido depreciado no 4.0). O projeto depende dele em dois lugares verificados por busca no código:

```
$ grep -rn "datetime_safe" coffeeapi/ --include=*.py
coffeeapi/level3/domain.py:6:    from django.utils.datetime_safe import datetime
coffeeapi/level2/domain.py:5:    from django.utils.datetime_safe import datetime

$ python -c "from django.utils.datetime_safe import datetime"   # no Django 5.2.17
ModuleNotFoundError: No module named 'django.utils.datetime_safe'
```

Note um detalhe sutil: essas duas linhas estão **dentro de uma função** (`def now()`), não no topo do módulo — é um *import preguiçoso*. Por isso o erro não aparece na coleta dos testes, e sim **em tempo de execução**, no momento em que `now()` é chamado. Um import tardio esconde a incompatibilidade até o código rodar — que é exatamente o pior momento para descobri-la.

Há ainda um segundo ponto de falha, no caminho de restauração da dependência de persistência:

```
/home/user/workspace/repos/design-api/.venv5/lib/python3.12/site-packages/coopy/restore.py:35:
    ModuleNotFoundError: No module named 'django.utils.datetime_safe'
```

Observação metodológica: a busca textual por `datetime_safe` dentro do diretório do `coopy` não encontra a string no código-fonte da dependência. Isso indica que a referência chega *pelos dados serializados* (snapshots de persistência gravados com objetos cujo caminho de classe aponta para o módulo removido), e não por um import literal. Registro como hipótese sustentada pela evidência disponível, não como fato verificado linha a linha.

#### 17.6.1 Rastreamento da hipótese: a referência vem dos DADOS, não do código

A hipótese registrada acima foi **rastreada e confirmada**. Segue a trilha de evidência, do sintoma até a causa.

**Passo 1 — a linha 35 abre um arquivo de DADOS, não um módulo.** Em `coopy/restore.py`:

```
# coopy/restore.py, linhas 29-41
actions = []
for file in files:
    unpickler = Unpickler(open(file,'rb'))     # ← abre o arquivo de DADOS
    try:
        while True:
            action = unpickler.load()          # ← LINHA 35: desserializa
            actions.append(action)
    except BadPickleGet:
        ...
```

O que a linha 32 abre é `open(file,'rb')`, um arquivo obtido por `fileutils.last_log_files(basedir)` — dado em disco, não código. A linha 35 apenas carrega o que está dentro dele.

**Passo 2 — o código da dependência não menciona o módulo removido.**

```
$ grep -rn "datetime_safe" .venv5/lib/python3.12/site-packages/coopy/
  → 0 ocorrências
```

Se a referência não está no código, só pode estar nos dados.

**Passo 3 — a referência está literalmente nos arquivos de dados.**

```
$ grep -rl "datetime_safe" data/
data/level3/transaction_000000000000003.log
data/level2/transaction_000000000000003.log

$ strings data/level2/transaction_000000000000003.log | grep datetime
django.utils.datetime_safe
datetime
```

**Correlação que confirma:** exatamente os níveis **2 e 3** contêm a referência — e são precisamente os dois cujos `domain.py` importam `datetime_safe`. Os níveis 0 e 1, que não importam o módulo, têm dados limpos. *A presença nos dados segue a presença no código que os produziu.*

**Passo 4 — a desmontagem do pickle mostra o opcode exato.**

```
$ python -m pickletools data/level2/transaction_000000000000003.log
...
223: \x8c         SHORT_BINUNICODE 'django.utils.datetime_safe'
252: \x8c         SHORT_BINUNICODE 'datetime'
263: \x93         STACK_GLOBAL
...
```

Este é o mecanismo preciso: o pickle **armazena o nome do módulo como string** (offset 223) e o nome do atributo (offset 252), e executa `STACK_GLOBAL` (offset 263) — a instrução que **importa o módulo pelo nome no momento da desserialização**. O pickle não guarda código: guarda *o caminho de importação* a ser resolvido depois. Quando o Django 5 removeu o módulo, esse caminho deixou de resolver — e o `load()` da linha 35 estoura.

**Passo 5 — reprodução isolada, sem Django e sem projeto.**

```
from pickle import Unpickler, UnpicklingError
u = Unpickler(open('data/level2/transaction_000000000000003.log','rb'))
while True:
    a = u.load()

# → ModuleNotFoundError: No module named 'django.utils.datetime_safe'
```

A falha se reproduz com **um arquivo de dados e a biblioteca padrão**. É a prova de que a causa está no dado.

**Passo 6 — o contrafactual decisivo.** Se a causa é o *nome do módulo gravado no dado*, então criar um módulo com esse nome — vazio, falso, sem funcionalidade — deve fazer a desserialização funcionar:

```
# 1) SEM o módulo (estado atual no Django 5):
load() → ModuleNotFoundError: No module named 'django.utils.datetime_safe'

# 2) Injetando um módulo FALSO com apenas o nome e um atributo datetime:
import sys, types, datetime as _dt
fake = types.ModuleType('django.utils.datetime_safe')
fake.datetime = _dt.datetime
sys.modules['django.utils.datetime_safe'] = fake

load() → carregou 4 objeto(s) com SUCESSO
#   (termina em EOFError: Ran out of input — o fim normal do arquivo)
```

**Isto encerra o rastreamento.** O mesmo arquivo, os mesmos bytes, o mesmo `load()`: falha quando o módulo não existe, **funciona quando o nome resolve** — mesmo com um módulo falso que nada implementa. Como o módulo falso não alterou nenhuma linha do projeto nem do `coopy`, a variável testada foi exclusivamente **o nome gravado nos dados**.

| Local da referência | Ocorrências | Conclusão |
|---|---|---|
| Código-fonte do `coopy` (`.py`) | **0** | Não é a dependência que referencia o módulo removido |
| Arquivos de dados (`data/level2`, `data/level3`) | **2 arquivos** | ✅ É aqui que a referência existe |
| Código do projeto (`coffeeapi/level2\|3/domain.py`) | **2** | Origem que *gerou* os dados — a causa-raiz a montante |

#### O que este rastreamento demonstra

Há **dois pontos de falha independentes**, agora ambos explicados:

1. **No código** — `level2/domain.py:5` e `level3/domain.py:6` importam `django.utils.datetime_safe` dentro de `def now()`. O import quebra no Django 5 e derruba as execuções que passam por `now()`.
2. **Nos dados** — os arquivos de transação gravados *antes* carregam o caminho do módulo dentro do pickle, e o `Unpickler.load()` da linha 35 tenta reimportá-lo na restauração. **Este é o ponto que atinge até o Nível 0**, que não tem o import ofensivo no seu código.

O segundo ponto é o mais instrutivo, e é um tema clássico de engenharia: **dados serializados carregam dependências de código congeladas no tempo**. Um pickle não guarda apenas valores — guarda *o caminho de importação do tipo*. Quando essa classe ou módulo deixa de existir, o dado torna-se *ilegível*, ainda que o valor em si permaneça válido. É por isso que formatos que guardam *valores* e não *tipos*, como JSON, sobrevivem melhor a refatorações — e é exatamente o argumento da aula #07 sobre codificação de representação e tipos de alto nível, aparecendo aqui como consequência real de projeto.

**Para reproduzir:** a trilha inteira usa apenas a biblioteca padrão (`pickle`, `pickletools`) mais o comando `grep` — nenhuma dessas evidências depende do Django 5, basta ter os arquivos em `data/`.

#### Efeito cascata: por que até o Nível 0 quebra

O Nível 0 é o mais revelador. Ele **não importa** `datetime_safe` em nenhum dos seus arquivos — e mesmo assim falha os dois testes. A razão é o *acoplamento compartilhado*: todos os quatro níveis usam a mesma camada de persistência (`coopy`), então uma mudança que quebra essa dependência **derruba o sistema inteiro, inclusive o componente que não tinha o import ofensivo**.

A segunda mensagem de erro é o sintoma visível dessa cascata, e é uma mudança de comportamento do próprio Django 5:

```
E   AttributeError: module 'coffeeapi.level2' has no attribute 'views'
```

No Django 5, quando o módulo `views.py` falha ao importar, o erro é reportado como atributo ausente no pacote — o que *esconde a causa* (o import quebrado) atrás de um sintoma genérico. Depurar isso a partir dessa mensagem, sem saber da remoção do módulo, é consideravelmente mais difícil.

#### O que as três rodadas juntas ensinam

**1. A curva é uma propriedade do design — confirmado.** Idêntica em 3.2 e em 4.2 (2→15→9→22, 48 passed), porque depende dos arquivos de teste, que são código do projeto.

**2. Mas o design é limitado por um contrato de runtime — e esse contrato muda.** No Django 5 o mesmo design vale **zero**. Estabilidade entre duas versões não é garantia para a terceira. E o motivo é banal e real: *uma dependência removeu um módulo*.

**3. Isto é o tema do próprio curso, aplicado ao código que o ensina.** As nove aulas tratam de acoplamento, fronteiras e evolução. O que encontramos aqui é a mesma lição do lado de dentro: o projeto importa um detalhe interno do framework (um módulo de utilitário privado, depreciado depois) e fica **acoplado a uma implementação, não a uma interface**. Quando a implementação muda, o acoplamento cobra o preço. É precisamente o argumento da aula #02 sobre por que a fronteira importa — e a aula #06 sobre entender *por que* o framework esconde o que esconde.

**4. O import preguiçoso não protege — só atrasa a descoberta.** A falha existe desde a importação; escondida dentro de `def now()`, ela só se manifesta quando o código executa. Detectar incompatibilidade na hora de instalar é muito mais barato do que dentro de um teste em produção.

**Para quem for estudar este repositório:** use **Django 4.2** (funciona integralmente, com avisos de depreciação que antecipam o problema) ou faça o ajuste de duas linhas — trocar `from django.utils.datetime_safe import datetime` por `from datetime import datetime` — para rodar no Django 5. Mas registre o achado: *este repositório é um exemplo prático de código acoplado a um detalhe interno de framework*, e vale mais estudá-lo sabendo disso.

#### Reprodutibilidade

Tudo nesta seção é reproduzível a partir do repositório público [virb30/design-api](https://github.com/virb30/design-api): basta preparar o ambiente como na seção 17.1 e executar a suíte apontando para cada nível. Os nomes de rota, status codes, headers e corpos de resposta foram capturados da execução — nenhum valor foi reconstruído a partir do código-fonte.

Documentação elaborada a partir dos resumos técnicos das transcrições das 9 aulas da playlist “Design de API na Prática”, de Henrique Bastos (HB Network), complementada por pesquisa nos repositórios públicos do instrutor e da comunidade. As citações reproduzem falas do instrutor capturadas nas transcrições. Os exemplos de código das seções 15.1 e 15.2 são reproduções de código-fonte público dos repositórios `requests-pro` e `python-jsonstar`; a tabela da seção 15.3 reproduz o README do repositório `virb30/design-api`. Os exemplos de requisição da seção 9 são reconstruções pedagógicas autorais. Não existe repositório oficial único do curso — as aulas são live coding no YouTube. Conteúdo de caráter educativo.
