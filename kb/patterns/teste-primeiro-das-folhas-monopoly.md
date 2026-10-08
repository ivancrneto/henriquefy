---
id: teste-primeiro-das-folhas-monopoly
title: One test per behavior, starting at the leaf
principle: teste-primeiro-das-folhas
category: testing
frameworks:
  python: {origin: his, repo: henriquebastos/monopoly, path: tests/test_player.py, commit: bffb0c269b00836066d0bb064ca4e38a80cad210}
---
**What.** The test file for a leaf entity is a list of flat functions, one per behavior, each
named `test_<message>` or `test_<message>_<outcome>`, each building its object inline, sending
one message and asserting one thing: the return value, the state after it, or the exception by
name. The values sit on the boundary of the rule, so the rule can be read from the test without
opening the implementation. A mock appears only where the code is non-deterministic. It applies
to the first files of a project, the entities with one responsibility and few relations, which
is where he starts: "comendo pelas beiradas, indo pelas folhas do sistema" (lesson 18 at 0:16,
`verified: false`, transcript paraphrase, principle file).

## python
`tests/test_player.py` at commit `bffb0c2`, lines 48 to 57:

```python
def test_invest_demanding():
    p = Player(100, strategy=Demanding())
    assert p.invest(price=100, rent=51) == 100
    assert p.balance == 0

def test_invest_demanding_abort():
    p = Player(100, strategy=Demanding())

    with pytest.raises(AbortInvestment):
        p.invest(price=100, rent=50)
```

And the body of `test_invest_gambler_abort(mocker)`, lines 80 to 82:

```python
    mocker.patch('random.choice', return_value=False)
    with pytest.raises(AbortInvestment):
        p.invest(price=100, rent=10)
```

What to notice. `rent=51` buys and `rent=50` aborts, so the pair states the rule `rent > 50`
of `monopoly/player.py` line 25 more precisely than the transcript does; `test_invest_cautious`
and its `_abort` twin (lines 59 to 68) fix `balance - price >= 80` the same way, with balances
180 and 100 against a price of 100. The happy path checks both the return (`== 100`, because
`pay` returns the amount) and the state (`balance == 0`); the failure is asserted by name with
`pytest.raises`, the same name `board.py` later catches. Fifteen tests in the file, no fixture,
no class, no setup (course digest section 19.7). The only mock in the whole project is
`random.choice`, patched on lines 73 and 80 for the `Gambler` strategy, because it is the only
non-deterministic decision. `test_player.py` imports nothing from the board or the game: it is
a leaf, and it was written before the board existed (digest section 2.2).

## Bad
A test that runs code and asserts nothing, and an integration test written before any leaf
exists:

```python
def test_player():
    p = Player(100, strategy=Demanding())
    p.invest(price=100, rent=51)        # green with any implementation

def test_simulation_runs():             # the first test in the project
    sim = Simulation(1000)
    sim.run()
    assert sim.stats                    # which rule broke? nobody can tell
```

The first passes whatever `invest` does; rule `testing.no-assert` catches it. The second needs
every class to exist before it can fail for a reason, and when it fails it does not say which
rule, in which object, is wrong.
