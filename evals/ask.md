# ask evals

Five questions (three OO, two API) with the expected principle id and citation. The installed
skill must answer each with the expected id and a citation that exists in the KB. CI checks every
id listed here exists under `kb/`; the answers are checked by hand (manual eval).

| question | expected principle id | expected citation |
|---|---|---|
| I have two classes that look alike; should I extract a base class now? | nao-projete-a-generalizacao | oo-na-pratica section 12.2, lesson 7 at 0:26:51 |
| My `charge()` returns False when the balance is short and False when the order is not paid. What would he do? | prefira-excecoes-a-booleanos | oo-na-pratica section 12.9, monopoly player.py at bffb0c2 |
| Should my Player subclass each strategy, or hold a strategy object? | componha-em-vez-de-herdar | oo-na-pratica section 12.8, lesson 18 |
| My Django view does `return JsonResponse(data, status=201)`. Anything he would change? | httpstatus-em-vez-de-numeros-magicos | design-api-na-pratica lesson 5, section 9.3 |
| How does he decide which links an API response should carry? | hypermedia-como-maquina-de-estados | design-api-na-pratica section 9.4, lessons 8 and 9 |
| Does a subclass's `__init__` run the base class's `__init__` automatically in Python, and what does `super()` do? | chame-a-base-explicitamente | raio-x-da-oo lesson 5 at 0:02:09 |
| Why does he insist that instance attributes be initialized in `__init__` instead of inside other methods? | inicialize-o-estado-no-init | raio-x-da-oo lesson 4 at 0:12:51 |
| I was handed a legacy program with no tests. What does he do first, and how does he make it safe to refactor? | execute-antes-de-ler | refatoracao-na-pratica lesson 20 at 0:02:17 and 0:05:08 |
| Why does he delete the `asc` function he just extracted in the wordcount refactoring? | nao-projete-a-generalizacao | refatoracao-na-pratica lesson 24 at 0:02:30 |
