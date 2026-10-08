---
id: serializacao-de-tipos
title: One encoder, conversions registered by type
principle: representacao-nao-e-codificacao
category: api
frameworks:
  python:  {origin: his, repo: henriquebastos/python-jsonstar, path: jsonstar/default_encoders.py, commit: 6fb683e8ca6aa53ce24d0c7de36b1b0bc7b62f75}
---
**What.** Types that JSON cannot carry (`Decimal`, `datetime`, `date`, `UUID`, `set`,
dataclasses, pydantic models) are converted by one encoder holding a registry from type to
function. The API decides the wire representation of each type once (`Decimal` as a string,
`datetime` as ISO 8601 with a `Z`), and views never call `str()` or `isoformat()` themselves.
This is the custom encoder lesson 7 arrives at after the `datetime` bug and the money debate
(digest section 5, lesson #7), published as `python-jsonstar` (section 15.2).

## python
From `python-jsonstar` (MIT), `jsonstar/default_encoders.py` at commit
`6fb683e8ca6aa53ce24d0c7de36b1b0bc7b62f75`, lines 62 to 73:

```python
DEFAULT_TYPED_ENCODERS = {
    datetime.datetime: lambda o: o.isoformat(timespec="milliseconds").replace("+00:00", "Z"),
    datetime.date: lambda o: o.isoformat(),
    datetime.time: lambda o: o.isoformat(timespec="milliseconds"),
    datetime.timedelta: encode_timedelta_as_iso_string,
    decimal.Decimal: str,
    uuid.UUID: str,
    set: list,
    frozenset: list,
    **DJANGO_TYPED_ENCODERS,
    **PYDANTIC_TYPED_ENCODERS,
}
```

And the lookup that uses it, `jsonstar/encoder.py`, same commit, lines 84 to 93:

```python
    def default(self, o) -> str:
        for base, encoder in self.typed_encoders.items():
            if isinstance(o, base):
                return encoder(o)

        for encoder in self.functional_encoders:
            with suppress(Exception):
                return encoder(o)

        return super().default(o)
```

The table is the API's representation policy in one place: `Decimal` goes out as a string, so
money keeps its scale and never touches `float`. `default` is the stdlib hook, overridden once;
typed encoders match by `isinstance` (a subclass registered later wins over its base, which
`TypedEncoderRegistry` in the same file guarantees), functional encoders are tried in order. A
project narrows the policy by registering its own function, for instance
`jsonstar.register_default_encoder(lambda o: str(o.quantize(Decimal("1.00"))), Decimal)`, or by
subclassing `JSONEncoderStar`. `import jsonstar as json` is a drop-in for the stdlib module, and
the `ProSession` docstring in his `requests-pro` recommends this encoder for API clients.

## Bad
```python
def read(request, order_id):
    order = shop.get(order_id)
    return JsonResponse({
        "id": order.id,
        "price": float(order.price),  # 1.99 is not representable; the scale is gone
        "created_at": order.created_at.strftime("%Y-%m-%d %H:%M"),
        "tags": list(order.tags),
    })
```
