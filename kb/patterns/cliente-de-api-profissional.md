---
id: cliente-de-api-profissional
title: Thin API client over a session that absorbs the protocol
principle: a-interface-e-o-que-importa
category: api
frameworks:
  python:  {origin: his, repo: henriquebastos/requests-pro, path: src/requestspro/client.py, commit: cd280f025041c8352823ee6aa5b77c09ddee3cf0}
---
**What.** The client a consumer sees is a thin set of methods named after what the API does
(`get_me`, `list`, `retrieve`); everything the protocol demands (base URL, authentication and
token renewal, JSON encoding and decoding, error translation, timeouts) is solved once in a
session class underneath. The client becomes the interface of the remote system as the consumer
thinks of it, which is what lesson 7 asks for after showing the pain of clients written against
a bad API (digest section 5, lesson #7; section 6.3), and what his `requests-pro` ships
(section 15.1).

## python
From `requests-pro` (MIT), `src/requestspro/client.py` at commit
`cd280f025041c8352823ee6aa5b77c09ddee3cf0`, lines 6 to 23:

```python
class Client:
    """Base class for all API clients. Use it on your subclients."""

    def __init__(self, session):
        self.session = session

    def request(self, method, url, params=None, json=None, **kwargs):
        response = self.session.request(method, url, params=params, json=json, **kwargs)
        response.raise_for_status()
        return response.json() if response.content else None

    get = partialmethod(request, "GET")
    post = partialmethod(request, "POST")
    put = partialmethod(request, "PUT")
    delete = partialmethod(request, "DELETE")
    head = partialmethod(request, "HEAD")
    options = partialmethod(request, "OPTIONS")
    patch = partialmethod(request, "PATCH")
```

Notice what is not here. `request` is the only real method: it delegates to the session,
raises on error and decodes JSON, and the seven verbs are `partialmethod` over it, so there is
exactly one place where a response is checked. Base URL, custom JSON encoder and decoder,
custom response class and timeout live in `ProSession` (`src/requestspro/sessions.py`, same
commit), composed from one mixin per concern. A concrete client subclasses `Client` with
methods such as `retrieve(self, sale_id)` returning `self.get(f"/sale/get_sale/{sale_id}")`,
and a `from_credentials` factory on the main client assembles token store, auth and session so
the consumer never sees them (section 15.1). The `409` that lessons 8 and 9 use for state
conflicts is among the statuses the example client's response class turns into a domain error
(section 15.1).

## Bad
```python
def get_sale(sale_id, token):
    r = requests.get(
        "https://api.example.com/sale/get_sale/" + str(sale_id),
        headers={"Token": token},
        timeout=10,
    )
    if r.status_code == 401:
        token = renew_token()  # repeated in every function
        r = requests.get("https://api.example.com/sale/get_sale/" + str(sale_id), headers={"Token": token})
    if r.status_code != 200:
        raise Exception(r.text)
    return json.loads(r.text, parse_float=Decimal)
```
