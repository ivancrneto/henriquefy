# ask evals

Five questions (three OO, two API) with the expected principle id and citation. The installed
skill must answer each with the expected id and a citation that exists in the KB. CI checks every
id listed here exists under `kb/`; the answers are checked by hand (manual eval).

| question | expected principle id | expected citation |
|---|---|---|
| I have two classes that look alike; should I extract a base class now? | deixe-o-codigo-descansar | oo-na-pratica section 12.1, lesson 23 |
| My `charge()` returns False when the balance is short and False when the order is not paid. What would he do? | prefira-excecoes-a-booleanos | oo-na-pratica section 12.9, monopoly player.py at bffb0c2 |
| Should my Player subclass each strategy, or hold a strategy object? | componha-em-vez-de-herdar | oo-na-pratica section 12.8, lesson 18 |
| My Django view does `return JsonResponse(data, status=201)`. Anything he would change? | httpstatus-em-vez-de-numeros-magicos | design-api-na-pratica lesson 5, section 9.3 |
| How does he decide which links an API response should carry? | hypermedia-como-maquina-de-estados | design-api-na-pratica section 9.4, lessons 8 and 9 |
