---
repo: henriquebastos/django-test-without-migrations
commit: b665a0d203cb615a1a923caf06cff298bf73707e
era: 2014 to 2022
license: MIT
class: his
---
# django-test-without-migrations

**What it is.** A `manage.py test` extension that adds `--nomigrations` (alias `-n`) so the
test database is built straight from the models, skipping Django 1.7's migration system, and
from 0.6 the same flag on `testserver`. Eighty-two lines of library code in three modules, a
test app, tox and Travis. Created 2014-12-13, last commit 2017-04-12 ("Improve handling
testserver"), 46 commits of which 37 are his, the rest from five contributors (nose support,
the `-n` alias, a Django 1.10 fix). It is the library he used in his own course project:
`eventex/requirements.txt:12` pins `django-test-without-migrations==0.6` and
`eventex/eventex/settings.py:44` installs it. MIT: excerpts are full.

**Layout.**

```
django-test-without-migrations/
├── setup.py                     setuptools, explicit packages list, no dependencies
├── setup.cfg                    [bdist_wheel] universal = 1
├── build.sh                     clean, then sdist bdist_wheel
├── requirements.txt             Django 1.11, django-nose, nose, tox, wheel (dev pins)
├── tox.ini                      py27/py36 x django17..111, nose pinned
├── .travis.yml                  2.7 and 3.6 through tox-travis
├── runtests.py                  runs django-admin test four times via subprocess
├── README.rst                   what, why, install, usage, inspiration, author, license
├── LICENSE                      MIT
├── test_without_migrations/
│   ├── __init__.py
│   └── management/commands/
│       ├── _base.py             DisableMigrations, CommandMixin, base command lookup
│       ├── test.py              class Command(CommandMixin, TestCommand): pass
│       └── testserver.py        class Command(CommandMixin, TestServerCommand): pass
└── tests/
    ├── settings.py              sqlite :memory:, the app under test, SECRET_KEY 'secret'
    ├── nose_settings.py         same plus django_nose runner and the command override
    └── myapp/
        ├── models.py            Person(name, age)
        ├── migrations/__init__.py   empty package: there are no migrations on purpose
        ├── fixtures/fixture.json
        ├── tests.py             PersonTest on TestCase
        └── nose_tests.py        plain class for the nose runner, checks the runner class
```

**How he tests.** The thing under test is a command-line flag, so the test is to run the
command. `runtests.py` sets `DJANGO_SETTINGS_MODULE` and calls `django-admin test` through
`subprocess`, once per spelling of the flag, then again with the nose settings:

```python
    # We need to use subprocess.call instead of django's execute_from_command_line
    # because we can only setup django's settings once, and it's bad
    # practice to change them at runtime
    subprocess.call(['django-admin', 'test', '--nomigrations'])
    subprocess.call(['django-admin', 'test', '-n'])

    # Test using django_nose.NoseTestSuiteRunner
    os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.nose_settings'
```
(`runtests.py:19-26`; the nose runs add `--pdb`, a nose-only flag, to prove the base command
was swapped, `:35-37`). What the inner tests check is that a table exists although
`tests/myapp/migrations/` is an empty package:

```python
class PersonTest(TestCase):
    """
    Uses a model to ensure the table exist, even with no migrations available.
    """
    def setUp(self):
        self.person = Person.objects.create(name='Arthur', age=18)

    def test_instance(self):
        assert isinstance(self.person, Person)
```
(`tests/myapp/tests.py:6-14`, plain `assert` inside a `TestCase`). The nose variant is a
plain class with the same three tests plus `test_is_nose_runner`, which asserts the configured
runner is `NoseTestSuiteRunner` (`tests/myapp/nose_tests.py:25-28`). `tox.ini:1-19` runs
`python runtests.py` for py27 and py36 against Django 1.7 to 1.11 with `django-nose==1.4.4`
and `nose==1.3.7`; `.travis.yml:6-8` installs `tox-travis` and runs `tox`. Not tested: the
`DisableMigrations` object on its own, the `optparse` branch for Django 1.7
(`_base.py:48-57`), and, see Caveats, whether the inner runs failed at all.

**How he handles errors.** None declared. The base command is resolved at import time from a
setting with a default:

```python
TestCommand = import_string(getattr(
    settings,
    'TEST_WITHOUT_MIGRATIONS_COMMAND',
    'django.core.management.commands.test.Command'))
```
(`_base.py:12-15`), so a wrong dotted path fails when Django loads the command, with
Django's `ImportError`. `DisableMigrations` is a stand-in for the `MIGRATION_MODULES` dict
that answers every lookup (`__contains__` returns `True`, `_base.py:29-30`) and returns the
value each Django version tolerates, with the reason in a comment: "django 1.9 takes None,
1.7/8 has an error here, so use a dummy value" (`:33-38`). `handle` removes the flag from
`sys.argv` before delegating, because the wrapped command would otherwise see an unknown
option (`:70-73`).

**Naming and interface.** The module that holds the logic is `_base.py` (`:1`): the leading
underscore keeps it out of Django's command discovery, which lists commands by file name, so
the only commands exposed are `test` and `testserver`, each an empty subclass:

```python
class Command(CommandMixin, TestCommand):
    pass
```
(`test.py:4-5`, `testserver.py:4-5`). `CommandMixin` carries the flag (`_base.py:41-78`) and
`DisableMigrations` the trick (`:27-38`); `HELP` is a module constant reused by both option
APIs (`:9, 56, 68`). The user-facing names are the flag, `--nomigrations`/`-n`, and one
setting, `TEST_WITHOUT_MIGRATIONS_COMMAND` (`README.rst:60-68`). The mixin's base is chosen at
runtime, so it composes over whatever `test` command the project already has (django-nose's,
for instance, `tests/nose_settings.py:26`).

**Packaging, config, tooling (2014 to 2017).** `setup.py:6-34`: version `'0.6'` literal, an
explicit `packages` list of the three modules (`:12-16`), `install_requires=[]` (`:17`),
`zip_safe=True`, classifiers for 2.7 and 3 (`:29-30`), `long_description` from `README.rst`.
`setup.cfg:1-2` asks for a universal wheel; `build.sh:4-6` is the release: `python setup.py
clean`, remove `dist/ build/ *.egg-info`, `python setup.py sdist bdist_wheel`.
`requirements.txt:1-5` is a development pin set (Django 1.11, django-nose, nose, tox 2.3.1,
wheel 0.26.0), not runtime dependencies. Configuration is a Django setting with a default
(`_base.py:12-15`). CI: Travis 2.7 and 3.6 (`.travis.yml:3-4`) delegating to tox with the
`[tox:travis]` map (`tox.ini:5-7`). Lint: none; landscape.io badge (`README.rst:8-10`) and
four more badges (`:4-23`), including the license badge. `# coding: utf-8` headers, `object`
base classes, `super(CommandMixin, self)` (`_base.py:44, 60, 78`): Python 2 kept alive to the
end.

**README voice.** Definition first: "*Test Without Migrations* is a `manage.py test` command
extension." (`README.rst:25`). Then the pain, in two sentences: "The new Django 1.7 and 1.8
migration backend demands that you create a migration every time you change a model. This can
be inconvenient when you're just trying to explore your models code." (`:27-29`), the
precedent ("In older Django versions, with `South` we could use the `SOUTH_TEST_MIGRATIONS`
settings", `:31`), and the promise in one line (`:33`). Installation and Usage are commands you
can paste (`:45, 51-54, 78, 84, 90`), with a warning about ordering in `INSTALLED_APPS`
(`:56-58`). "Inspiration" credits the gist it came from (`:95`). Commit messages are terse
and sometimes misspelled ("Bumb vertion to 0.3", `f65ccfc`; "Fixes #9 #10 adding support for
testserver", `56d8840`).

**What this repo adds to the KB.**
- `configuracao-fora-do-codigo`, 2010s form: the base command comes from a setting with a
  sensible default, read once at module level (`_base.py:12-15`; `README.rst:60-68`).
- `componha-em-vez-de-herdar`: a mixin applied over a base chosen at runtime, so the extension
  stacks on any project's existing `test` command (`_base.py:41, 12-15`; `test.py:4`;
  `tests/nose_settings.py:26`).
- `pragmatismo-sobre-pureza`: three version branches, each with a comment on which Django
  needs it (`_base.py:18-24, 33-38, 46-57`), and an `argv` edit rather than an argument-parser
  rewrite (`:70-73`).
- `nao-projete-a-generalizacao`: one flag, one setting, empty command subclasses
  (`test.py:4-5`).
- `o-codigo-e-a-interface`: the whole public surface is readable from the README's three
  commands (`README.rst:45, 78, 90`).
- Pattern files: none written or amended in this pass.

**Caveats.**
- `runtests.py` discards every return code: `subprocess.call(...)` on lines 22, 23, 36 and 37
  is never checked and the script never calls `sys.exit` with a failure, so tox and Travis
  report green even when the inner `django-admin test` fails. A test that cannot fail is not a
  test; this contradicts the courses' whole use of tests as the signal.
- The inner tests use bare `assert` inside `TestCase` (`tests/myapp/tests.py:14, 17, 20`),
  which `python -O` strips; the OO digest notes the same hazard in `monopoly`
  (`kb/courses/oo-na-pratica.md:1333`).
- `handle` mutates `sys.argv` (`_base.py:70-73`): global state edited to satisfy the wrapped
  command. Commented, deliberate, still a global edit.
- `SITE_ID=1,` is a tuple in both test settings (`tests/settings.py:17`, `tests/nose_settings.py:16`).
- `requirements.txt:1-5` mixes the framework with build tools; nothing says which are
  runtime. (`install_requires=[]` in `setup.py:17` is the actual answer.)
- The `optparse` branch for Django 1.7 (`_base.py:46-57`) stayed after tox dropped
  py36-django17 and Travis stopped testing 1.7 on 3.x (`tox.ini:2`).
