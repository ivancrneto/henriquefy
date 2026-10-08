---
id: representacao-nao-e-codificacao
title: Representação não é codificação
category: api
weight: 4
detectable: partial
era: timeless
scope: api
sources:
  - type: course
    course: design-api-na-pratica
    lesson: null
    section: "3.3"
    timestamp: null
  - type: course
    course: design-api-na-pratica
    lesson: null
    section: "3.4"
    timestamp: null
  - type: course
    course: design-api-na-pratica
    lesson: null
    section: "6.3"
    timestamp: null
  - type: course
    course: design-api-na-pratica
    lesson: null
    section: "15.2"
    timestamp: null
  - type: course
    course: design-api-na-pratica
    lesson: 2
    section: "5"
    timestamp: null
  - type: course
    course: design-api-na-pratica
    lesson: 7
    section: "5"
    timestamp: null
  - type: course
    course: design-api-na-pratica
    lesson: 9
    section: "5"
    timestamp: null
---
**Rule.** A resource has representations, and a representation has encodings. JSON, XML and CSV
are encodings negotiated between client and server, never part of the resource or of its
identifier. Types the encoding cannot carry natively (money, dates, sets, identifiers) get an
explicit representation plus metadata, so encoders and decoders convert programmatically and
views never guess.

**Why Henrique says so.** Não existe nada no REST que fale sobre JSON, XML ou JPG; isso é um
detalhe de codificação da representação de um recurso (lesson #2, no timestamp,
`verified: false`, digest section 3.3). Content negotiation through `Accept` is how the web
decouples transport from format, and the digest adds the design corollary from lesson 2: do not
couple the format into the URI, as a `.json` suffix does (section 3.4; section 5, lesson #2).
Lesson 7 shows what happens when the layers blur: a `datetime` that would not serialize, traced
to bytes versus strings and to the lack of an encoder for higher-level types; and the money
debate, where `float` is dangerous for precision and integers com duas casinhas without
metadata turn every view into a pile of conversions (digest section 5, lesson #7). His
conclusion is that the API needs metadata that lets encoders and decoders convert without
guessing (section 6.3).

**Looks like.** His `python-jsonstar` library is the lesson 7 encoder generalized: `Decimal`
becomes a string, `datetime` an ISO string, `set` a list, each conversion registered once by
type (digest section 15.2; pattern serializacao-de-tipos). Lesson 9 closes the course
serializing `Decimal` for the order's price in the level 3 API (digest section 5, lesson #9).
Bad: `price = float(data["price"])` in a view, `"created_at": str(order.created_at)` with the
format decided at each call site, and `/orders/1.json` as a URL.

**How to detect.** Partial. Mechanical candidates: `FloatField` or `float(` applied to names
such as `price`, `amount`, `total` (rule `api.money-as-float`); URL patterns ending in `.json`
or `.xml` (rule `api.format-in-uri`); `json.dumps(..., default=str)`, one lossy conversion for
every unsupported type. Judgment: `str()` and `isoformat()` calls scattered through views
instead of one encoder; response shapes that change with `Accept` beyond the encoding itself.

**How to fix.** Pick one encoder and one decoder for the whole API and register the conversions
by type there. Represent money as `Decimal` inside and as a string with a fixed scale on the
wire, and say so in the API's metadata or documentation. Keep URIs free of format; let `Accept`
and `Content-Type` carry it. Then delete the per-view conversions.
