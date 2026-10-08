---
repo: henriquebastos/django-aggregate-if
commit: 588c1487bc88a8996d4ee9c2c9d50fa4a4484872
era: 2012 to 2022
license: MIT
class: his
---
# django-aggregate-if

**What it is.** A single-module Django extension that adds an `only=Q(...)` condition to
`Sum`, `Count`, `Avg`, `Max` and `Min`, so one query answers "how many offers, and how many of
them are open, revoked, paid" instead of eight (`README.rst:41-81`). 164 lines of library code,
688 lines of tests borrowed from Django's own aggregation suite, Django 1.4 to 1.7, Python 2.7
and 3.4. Created 2012-12-26; the last commit is 2014-11-20 ("Fixing travis"); version 0.5.
It pre-dates Django 1.8's native conditional aggregates and was written to be thrown away when
they arrived (`README.rst:104-106`). Of the 79 reachable commits (shallow clone), 66 are his;
the rest are six contributors listed in the README (`:114-124`). MIT: excerpts are full.

**Layout.**

```
django-aggregate-if/
├── aggregate_if.py        the library: SqlAggregate family plus Aggregate family
├── setup.py               setuptools, py_modules, six as the only dependency
├── tox.ini                18 envs: py27/py34 x django1.4..1.7 x sqlite/postgres/mysql
├── .travis.yml            the same matrix as env vars with excludes
├── runtests.py            optparse --settings, asks Django for its runner
├── README.rst             problem, solution, install, inspiration, limitations, contributors, changelog
├── LICENSE                MIT
├── .gitignore             *.pyc, .tox, dist/, .idea, .DS_Store
└── tests/
    ├── __init__.py
    ├── test_sqlite.py     settings module per backend
    ├── test_postgres.py
    ├── test_mysql.py
    └── aggregation/       a throwaway Django app
        ├── models.py      Author, Publisher, Book, Store (Django's own aggregation models)
        ├── fixtures/aggregation.json
        └── tests.py       BaseAggregateTestCase, 30 methods
```

**How he tests.** Django's runner, invoked by a hand-written `runtests.py` that takes
`--settings` and lets Django pick the runner:

```python
def get_runner(settings_module):
    '''
    Asks Django for the TestRunner defined in settings or the default one.
    '''
    os.environ['DJANGO_SETTINGS_MODULE'] = settings_module

    import django
    from django.test.utils import get_runner
    from django.conf import settings

    if hasattr(django, 'setup'):
        django.setup()

    return get_runner(settings)
```
(`runtests.py:24-37`; `:40-44` builds `TestRunner(verbosity=1, interactive=True, failfast=False)`
and exits with its result). One settings module per database backend (`tests/test_sqlite.py`,
`test_postgres.py`, `test_mysql.py`, each 21 lines, in-memory sqlite or a database named
`aggregation`). The tests themselves are one `TestCase` with a JSON fixture
(`tests/aggregation/tests.py:22-23`) and thirty methods that assert whole result dicts:

```python
    def test_single_aggregate(self):
        vals = Author.objects.aggregate(Avg("age"))
        self.assertEqual(vals, {"age__avg": Approximate(37.4, places=1)})
        vals = Author.objects.aggregate(Sum("age", only=Q(age__gt=29)))
        self.assertEqual(vals, {"age__sum": 254})
```
(`tests.py:32-36`). The models and most tests are Django's aggregation suite with `only=`
added, as the README states (`README.rst:104-105`); the fix for quoting came with its own
regression test, `test_quote_escape` (`tests.py:28-30`, commit `e2512fd`, "Add
test_quote_escape to avoid sql injection", contributed). Tests that no longer pass are kept
as string literals inside the class (`tests.py:138-143, 151-161, 169-178`). The matrix is the
real test: tox creates and drops the postgres and mysql databases around each run
(`tox.ini:45-48, 55-58`), and Travis repeats the matrix with `DJANGO` and `DB` env vars plus
eight excludes for Python 3.4 (`.travis.yml:8-39`).

**How he handles errors.** No exception is declared or caught, except an `ImportError` shim
for `Approximate` moving between Django versions (`tests.py:9-14`). Behavior across versions is
selected by comparing `VERSION = django.VERSION[:2]` (`aggregate_if.py:19, 30, 123-136`), with
one-line comments on why: "setup_joins have different returns in Django 1.5 and 1.6, but the
order of what we need remains." (`:128`). The one defensive note is a property with a warning:

```python
    @property
    def has_condition(self):
        # Warning: bool(QuerySet) will hit the database
        return self.condition is not None
```
(`aggregate_if.py:49-52`). Bad input reaches Django's own errors; the library adds none.

**Naming and interface.** The public names are Django's names, so adoption is an import
swap: `from aggregate_if import Count, Sum` (`README.rst:71`) in place of
`from django.db.models import Count, Sum` (`:52`). Each public class is three lines:

```python
class Sum(Aggregate):
    name = 'Sum'
    sql_klass = SqlSum
```
(`aggregate_if.py:142-144`, repeated for `Count`, `Avg`, `Max`, `Min`, `:147-164`). The only
new parameter is `only` (`:106`). The SQL side mirrors Django's internal names (`SqlAggregate`,
`SqlSum`, `SqlCount`, `:22, 78, 82`) and its template vocabulary (`conditional_template`,
`sql_function`, `is_ordinal`, `:23, 79, 83`). Two helpers are underscored, `_condition_as_sql`
and `_get_fields_from_Q` (`:54, 111`); `escape` is a closure inside the first (`:58-70`).
Module docstring credits the four sources the code was built from (`:2-11`).

**Packaging, config, tooling (2014).** `setup.py` with setuptools: version `'0.5'` as a
literal (`setup.py:7`), `py_modules=['aggregate_if']` (`:12`), `install_requires=['six>=1.6.1']`
(`:13-15`), `long_description` read from `README.rst` (`:9`), classifiers for 2.7 and 3
(`:27-28`), `zip_safe=False`. Python 2 and 3 through `six` and `from __future__ import
unicode_literals` (`aggregate_if.py:12-13`), `# coding: utf-8` on every file. No
`requirements.txt`: he removed it in favor of tox deps (commit `779945e`, "Remove
requirements.txt", 2014-03-23) and each tox env pins its own Django (`tox.ini:36-37`). CI is
Travis with `pip install -q Django==$DJANGO --use-mirrors` (`.travis.yml:48`). Lint: none; the
README carries a landscape.io badge (`README.rst:8-10`). Docs are the README: badges for
Travis, landscape, PyPI version and downloads (`:4-18`), and the changelog is a section of the
README (`:126-148`). `.gitignore:9` ignores `dist/`.

**README voice.** One line of what, then the problem in the reader's terms: "*Aggregate-if*
adds conditional aggregates to Django." (`README.rst:20`), "Conditional aggregates can help
you reduce the ammount of queries to obtain aggregated information, like statistics for
example." (`:22-23`). A model, four questions (`:41-46`), the eight-query answer, then "With
conditional aggregates you can get it all with only **1 query**:" (`:65`). The "Inspiration"
section is first person and tells the truth about origin: "Using Django 1.6, I still wanted to
avoid creating custom queries for very simple conditional aggregations. So I've cherry picked
those ideas and others from the internet and built this library." (`:100-102`), and about
lifespan: "This library uses the same API and tests proposed on `ticket 11305`_, so when the
new feature is available you can easily replace ``django-aggregate-if``." (`:104-106`).
"Limitations" names what does not work and links the issue (`:108-112`). `setup.py:8` pitches
it as "Conditional aggregates for Django, just like the famous SumIf in Excel." His commit
messages are short and plain, with one celebration: "Bump version to 0.5 \o/" (`4d3d24d`).

**What this repo adds to the KB.**
- `a-interface-e-o-que-importa`: the public API is Django's API plus one keyword
  (`aggregate_if.py:106, 142-164`; `README.rst:70-81`), designed so the library can be removed.
- `postergue-decisoes`: he reuses the test suite and API of the pending Django ticket instead
  of inventing his own (`README.rst:104-106`), so the decision stays with upstream.
- `pragmatismo-sobre-pureza`: version differences are handled inline with `VERSION`
  comparisons and a comment each (`aggregate_if.py:123-136`), no compatibility layer.
- `nao-projete-a-generalizacao`: one module, five three-line public classes, no registry or
  plugin point (`aggregate_if.py:142-164`).
- `teste-primeiro-das-folhas`: a bug fix arrives with its regression test
  (`tests/aggregation/tests.py:28-30`); the suite asserts results, not internals.
- Pattern files: none written or amended in this pass.

**Caveats.**
- SQL is assembled by string interpolation with hand-rolled escaping: `sql % tuple(param)`
  after `escape()` doubles quotes and percent signs (`aggregate_if.py:58-75`), instead of
  passing params to the driver. `test_quote_escape` guards it (`tests.py:28-30`), but the
  surface is the kind the API course's error-handling lessons would push to the boundary.
- Dead tests kept as triple-quoted strings inside the test class (`tests.py:138-143, 151-161,
  169-178`): the file says 30 tests, the runner sees 26.
- The README's one-query example has a syntax error: `Sum('price'), only=Q(status=Offer.REVOKED))`
  closes the call early (`README.rst:79-80`).
- `SITE_ID=1,` makes the setting a tuple in all three test settings modules
  (`tests/test_sqlite.py:14` and siblings). Harmless there, still wrong.
- Test models define `__unicode__` only (`tests/aggregation/models.py:11, 18, 32, 42`), so
  under Python 3 they have no readable `str`; the 3.4 envs ran anyway.
- 2014 tooling throughout: `six`, `optparse` (`runtests.py:5`), `MIDDLEWARE_CLASSES`,
  `--use-mirrors`. This is where `era` applies; the design above is not dated.
