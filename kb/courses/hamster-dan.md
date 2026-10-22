<!-- written by the henrique-ingest distiller on 2026-10-22 from sources/transcripts/hamster-dan/; see kb/courses/README.md for provenance and license -->

Canal Henrique Bastos · Documentação de episódio

# Hamster Dan: keeping pull requests moving

Um único vídeo curto, em inglês, narrado por Henrique Bastos: a demonstração do Hamster Dan, o sistema dele que leva um pull request do GitHub até ficar pronto para o merge. Não é aula de código. Um grafo determinístico coordena cinco loops (checks, review, repair, conversation, reminders), e agentes de IA fazem só o que exige julgamento: achar um bug e consertá-lo. Roda sobre o Petrus, o runtime de redes de Petri dele. O código do Hamster Dan está digerido em `kb/repos/hamsterdan.md`; este documento registra só o que o vídeo mostra e diz.

Narração: **Henrique Bastos** · Canal [Henrique Bastos](https://www.youtube.com/channel/UCaL1P7zI_1B6mRjMqcxq0Yg) · Vídeo: [Hamster Dan: keeping pull requests moving](https://www.youtube.com/watch?v=EFzSNLQATqE) · Repositório: [henriquebastos/hamsterdan](https://github.com/henriquebastos/hamsterdan)

Documento elaborado a partir da legenda automática em inglês (en-orig, a língua original do vídeo, capturada em 2026-10-22) e de 30 frames extraídos pelo `/watch`. O vídeo é do canal pessoal dele, não do HB Network, e não pertence a playlist; é tratado como lição 1 de um curso de uma lição só. Só há uma voz, a de Henrique. As paráfrases estão em português. Nomes de pessoas que aparecem na tela (o revisor do PR de demonstração) ficam só pelo papel.

## 1. Visão geral do curso

| Dimensão | Valor | Observação |
|---|---|---|
| Lições | 1 | Vídeo avulso, sem número no título. |
| Duração total | 258 s (4min 18s) | Metadado do vídeo. |
| Data | publicado em 2026-10-12 | `upload_date`; anterior ao #1 (2026-10-21). |
| Transcrição | 1 de 1 disponível | Legenda automática em inglês (en-orig). A descrição traz 10 capítulos. |
| Formato | slides animados e gravação de tela | Slides de título e diagramas; o PR de demonstração `Hamsterdan demo: hero-review #83` no GitHub. |
| Legenda ruidosa | nomes | Hamster Dan sai Hamsterdon (3:31; 3:49); Petrus sai Petras (3:57). Os frames confirmam Hamster Dan, Hamsterdan e `RUNTIME: PETRUS`. |
| Código | só o do PR de demonstração | Três trechos de `scenario-fixtures/hero_review/` aparecem na tela (seção 13). |

## 2. Filosofia e método de ensino

### 2.1 Mostrar com um PR real

Henrique diz que vai usar um pull request para mostrar como tudo se encaixa (0:17 a 0:22) e segue o Dan por um PR real, do pedido de review até a aprovação (1:53 a 3:14). Fecha o PR sem merge porque era uma demonstração (3:12 a 3:16). A descrição do PR diz que é um cenário controlado de qualificação e pede que não seja feito merge automático (frame em 1:56).

## 3. Pilares conceituais

### 3.1 Um grafo coordena, agentes julgam

Um grafo determinístico coordena o trabalho por vários loops, e agentes de IA cuidam dos trabalhos que precisam de julgamento (0:04 a 0:13). No slide, só Review e Repair levam a marca de agente (frame em 0:10). Com uma LLM lendo o GitHub repetidamente e escolhendo o próximo passo, ele gastaria tokens com decisões que o workflow toma a partir do estado que já tem; ele quer os agentes concentrados no que precisa de julgamento, como achar um bug ou chegar a um conserto (3:17 a 3:31).

### 3.2 O tempo entre abrir e mergear um PR tende ao infinito

Cada passo é pequeno (CI, review, pergunta, mudança, main que andou, conflito), mas todo mundo está equilibrando outro trabalho, e a espera entre os passos transforma um PR pequeno em dias de vai e volta (0:22 a 1:07). Checks levam tempo e pessoas precisam de tempo para responder, revisar e decidir; ele quer menos espera entre esses passos e menos acompanhamento que dependa de ele lembrar (1:44 a 1:52).

### 3.3 O resultado pertence a um commit

Se o Dan começa a revisar um commit e chega outro antes de ele terminar, a revisão antiga não descreve mais o código atual; o sistema rastreia a que commit cada resultado pertence e confere isso antes de publicar, enquanto o commit novo passa pelos próprios checks e review (3:43 a 3:59).

### 3.4 O humano decide

Terminar o conserto não substitui a decisão do revisor: o review de código fica limpo e o review humano continua em changes requested até ele aprovar (3:00 a 3:07). A decisão do merge continua sendo nossa (3:12). O aviso de prontidão na tela diz que humanos mantêm a autoridade do merge e que o Dan nunca faz merge (frame em 3:10).

## 4. As aulas em uma tabela

| # | Título | Duração | Foco em uma linha |
|---|---|---|---|
| 1 | Hamster Dan: keeping pull requests moving | 4:18 | Grafo determinístico com cinco loops, agentes só no review e no repair, resultados presos ao commit, merge humano (0:04; 2:08; 3:43; 3:12). |

## 5. Resumo por aula

### Aula 1: Hamster Dan: keeping pull requests moving

Vídeo: https://www.youtube.com/watch?v=EFzSNLQATqE

Resumo: Henrique apresenta o Hamster Dan como um sistema agêntico que empurra PRs até a conclusão, construído com o Petrus, um runtime de redes de Petri que combina grafos determinísticos com agentes de IA (0:00 a 0:17). Descreve a espera que estica um PR (0:22 a 1:07) e o mesmo PR com o Dan: ele percebe o CI que falhou, pode rodar de novo os jobs que falharam e tentar o conserto, e devolve a um humano se não resolver (1:12 a 1:20); aplica sugestões de review pedidas na conversa do GitHub sem que ele faça checkout do branch (1:26 a 1:32); atualiza o branch ou trabalha num conflito quando main andou (1:34 a 1:40); e um lembrete traz de volta um PR parado (1:38 a 1:44). Na demonstração, o Dan posta um resumo que junta CI, a revisão dele e o review humano, e mantém esse mesmo comentário atualizado (1:53 a 2:06). O CI passa, mas o Dan acha três problemas e os posta ao lado das linhas, com explicação e sugestão de mudança (2:08 a 2:35). O revisor pede mudanças, Henrique pede ao `@hamster-dan` na conversa que conserte os três achados, e o Dan empurra um commit de conserto no mesmo branch (2:35 a 2:50). Os seis jobs de CI passam, a nova revisão volta limpa e as três threads se resolvem sozinhas (2:50 a 2:59). O review humano continua pedindo mudanças até o revisor aprovar; aí o resumo fica todo verde e o Dan posta um aviso de prontidão (3:00 a 3:12). Ele fecha com o porquê do grafo (3:17 a 3:43), o caso do commit novo durante uma revisão (3:43 a 3:59) e o que o Petrus libera: concentrar-se nas regras do PR, testar o que acontece quando chega código novo durante um review e inspecionar um PR parado para ver do que ele precisa (3:57 a 4:09).

Linha do tempo (capítulos da descrição):

- [0:00] A graph coordinates the work
- [0:20] Waiting stretches the PR
- [1:53] Summary on GitHub
- [2:08] Review
- [2:35] Repair
- [3:06] Approval
- [3:17] One LLM steering the PR
- [3:31] Loops run in parallel
- [3:43] The PR moves on
- [3:59] Keep the PR moving

Princípios que ele enuncia:

- [0:06] Um grafo determinístico coordena o trabalho; agentes fazem só o que exige julgamento.
- [3:19] Não gaste tokens com decisões que o workflow toma a partir do estado que já tem.
- [3:49] Rastreie a que commit cada resultado pertence e confira antes de publicar.
- [3:12] O merge é decisão humana.

Código: três trechos de um fixture de demonstração, mostrados na tela (seção 13).

Citações:

- [0:22] o tempo entre abrir um pull request e fazer o merge tende ao infinito
- [3:12] a decisão do merge continua sendo nossa
- [4:13] um PR que continua andando enquanto fazemos outro trabalho

## 6. Princípios que atravessam toda a série

1. **Determinismo na coordenação, julgamento nos agentes.** O grafo decide o próximo passo a partir do estado do PR; a LLM fica com achar o bug e consertá-lo (0:04 a 0:13; 3:17 a 3:31). É o mesmo princípio de não queimar token para buscar informação que já devia estar pronta, de `ia-como-veiculo-de-expressao` (0:06:58).
2. **Loops em paralelo.** Checks, reviews e conversa são acompanhados ao mesmo tempo, e um agente segue no conserto enquanto chegam eventos em outro lugar (3:31 a 3:42).
3. **Resultado preso ao commit.** Uma revisão de um commit antigo não é publicada como se fosse do atual (3:43 a 3:59).
4. **Requisitos explícitos.** O workflow torna explícitos os requisitos de resultados atuais e de aprovação humana (4:07 a 4:13).
5. **Humano no merge.** O agente aconselha; quem decide é a pessoa (3:00 a 3:12).

## 7. Citações-chave do curso

Paráfrases da legenda em inglês, traduzidas, não verificadas.

| Lição | Timestamp | Paráfrase |
|---|---|---|
| 1 | 0:22 | O tempo entre abrir um pull request e fazer o merge tende ao infinito. |
| 1 | 1:48 | Quero menos espera entre esses passos e menos acompanhamento que dependa de eu lembrar. |
| 1 | 3:03 | Terminar o conserto não substituiu a decisão do revisor. |
| 1 | 3:12 | A decisão do merge continua sendo nossa. |
| 1 | 3:19 | Com uma LLM lendo o GitHub e escolhendo o próximo passo, eu gastaria tokens com decisões que o workflow toma a partir do estado que já tem. |
| 1 | 3:25 | Quero os agentes concentrados no que precisa de julgamento, como achar um bug ou chegar a um conserto. |
| 1 | 4:13 | Um PR que continua andando enquanto fazemos outro trabalho. |

## 8. A evolução técnica, aula a aula

Uma lição só; a evolução é a do PR de demonstração, lida nos frames:

- **Antes (1:56):** resumo esperando o CI de `d6e2438`; CI não iniciado, Dan revisando, sem review humano, base atual, sem conflitos.
- **Review (2:08 a 2:35):** três achados nas linhas; o revisor pede mudanças.
- **Repair (2:35 a 2:59):** commit `Repair all hero-review findings` (`15b9107`); seis jobs de CI passam; revisão do Dan limpa, zero achados; threads marcadas como outdated e resolvidas.
- **Aprovação (3:00 a 3:16):** o revisor aprova; o resumo diz que todos os gates estão limpos para `15b9107` e que o merge é seu; o PR aparece fechado.

## 9. Arsenal técnico demonstrado no curso

| Peça | O que faz | Timestamp |
|---|---|---|
| Hamster Dan (`hamster-dan[bot]`) | GitHub App que coordena o PR: resumo, review, repair, conversa, lembretes | 0:00 a 4:18 |
| Resumo do Hamsterdan | Um comentário único, editado, com os gates CI checks, Dan's review, Human review, Base e Conflicts | 1:53 a 2:06 |
| Petrus | Runtime de redes de Petri sobre o qual o Dan roda | 0:13 a 0:17; 3:57 |
| GitHub Actions | Os seis jobs de CI do PR | 2:50 |

## 10. Glossário do curso

- **Gate:** cada condição do resumo (CI checks, Dan's review, Human review, Base, Conflicts) (frame em 1:56).
- **Readiness advisory:** aviso de que todos os gates observados estão prontos; não é merge (3:09 a 3:12).
- **Head:** o commit atual do PR, a que cada resultado precisa pertencer (3:43 a 3:59).
- **Loop:** cada frente acompanhada pelo grafo: Checks, Review, Repair, Conversation, Reminders (0:04 a 0:13).

## 11. Perguntas e respostas que o curso responde

- **Por que um grafo e não uma LLM no comando?** Porque o workflow decide o próximo passo a partir do estado que já tem, sem gastar tokens (3:17 a 3:31).
- **O que acontece se o CI falha?** O Dan pode rodar de novo os jobs que falharam e tentar o conserto; se não resolver, devolve a um humano (1:14 a 1:20).
- **E se chega um commit durante a revisão?** A revisão antiga deixa de valer; cada resultado é conferido contra o commit dele antes de ser publicado (3:43 a 3:59).
- **O Dan faz merge?** Não; ele avisa que está pronto, e o merge fica com as pessoas (3:09 a 3:12).

## 12. Repositórios e recursos

| Recurso | Relação | Timestamp |
|---|---|---|
| [hamsterdan](https://github.com/henriquebastos/hamsterdan) | Dele; digerido em `kb/repos/hamsterdan.md` | 0:00 |
| [Petrus](https://petrus.run) (henriquebastos/petrus) | Dele; digerido em `kb/repos/petrus.md` | 0:13; 3:57 |

## 13. Análise linha a linha do código real

O vídeo mostra três trechos de `scenario-fixtures/hero_review/`, um fixture com bugs plantados para a demonstração, e as sugestões do Dan. Lidos dos frames, sem acesso ao arquivo:

- `gate.py:10`, `lease_deadline`: `return issued_at + timedelta(minutes=ttl_seconds)` vira `timedelta(seconds=ttl_seconds)`, porque o parâmetro está em segundos e o lease durava 60 vezes mais (2:18; 2:22).
- `gate.py:16`, `can_release`: `return len(request.approvals) >= required` vira `sum(request.approvals.values()) >= required`, porque contar as entradas do mapeamento aprova também quem rejeitou explicitamente (2:22 a 2:25).
- `cache.py:11`, `lookup_key`: `return f"{repository}#{request_number}"` vira `f"{repository.casefold()}#{request_number}"`, a mesma normalização usada ao gravar, senão repositórios com maiúsculas são gravados numa chave e lidos de outra (2:25 a 2:30).

O vídeo não mostra os testes do fixture. Limites da legenda: Hamster Dan sai Hamsterdon (3:31; 3:49) e Petrus sai Petras (3:57); em 2:23, cache key keys [provável: cache keys].

## 14. Execução real dos testes

O vídeo mostra seis jobs de CI passando (2:50), mas não o que rodam. Não há suíte publicada para este fixture que se possa rodar aqui; o repositório está digerido em `kb/repos/hamsterdan.md`.

---

Documentação elaborada a partir da transcrição e dos frames do vídeo Hamster Dan: keeping pull requests moving, narrado por Henrique Bastos no canal pessoal dele, vídeo `EFzSNLQATqE`, legenda automática em inglês (en-orig) capturada em 2026-10-22. As citações são paráfrases traduzidas da transcrição, não verificadas contra o vídeo (`verified: false`), renderizadas sem aspas. O revisor que aparece na tela fica só pelo papel. Conteúdo de caráter educativo.
