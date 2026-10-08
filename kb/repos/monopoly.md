---
repo: henriquebastos/monopoly
commit: bffb0c269b00836066d0bb064ca4e38a80cad210
era: 2020 to 2022
license: none
class: his
---
# monopoly

**What it is.** The codebase of the course Orientação a Objetos na Prática: a Monte Carlo
simulator of a simplified Monopoly in which four players, each with a buying strategy, play
until one is left or 1000 turns pass, and the winner is counted per strategy over ten thousand
games. Pure Python 3, seven modules of about 230 lines in `monopoly/` plus four test files of
about 310 lines, pytest and pytest-mock as the only dependencies. The repository has two
commits, both from 2020-11-06 ("Ignore", `562a69f`; "Import", `bffb0c2`), so it is a snapshot
of the course's end state before the `Competitors` refactor of lesson 23 (course digest
section 19.8). No license file, so every excerpt from it is quotation-length.

**Layout.**

```
monopoly/
  __init__.py     re-exports Player, RealState, Board, Game, Simulation (lines 1 to 5)
  __main__.py     Simulation(10000), run, print (lines 3 to 5)
  player.py       OutOfMoney, NotEnoughMoney, AbortInvestment (4 to 11); Strategy and its four
                  subclasses (13 to 35); STRATEGIES (37); Player with pay, receive, invest and
                  the from_strategies factory (39 to 68)
  realstate.py    RealState: has_owner, owner_is, foreclose, sell_to, rent_to, deal (1 to 32)
  board.py        Board: players as a dict of positions, move with laps and bonus, remove, turn
  game.py         Game: leader, dice, run loop with the two end conditions
  simulation.py   generate_players, generate_properties (gaussian prices), game_factory,
                  Simulation over multiprocessing.Pool
tests/
  test_player.py, test_realstate.py, test_board.py, test_game.py   one file per module
requirements.txt  pytest 6.1.2, pytest-mock 3.3.1 and their transitive pins (lines 1 to 10)
```

There is no `test_simulation.py` and no README.

**How he tests.** pytest with flat functions: no classes, no fixtures, no `conftest.py`. One
behavior per test, named `test_<message>` or `test_<message>_<outcome>`:
`test_invest_impulsive`, `test_invest_without_money`, `test_invest_demanding`,
`test_invest_demanding_abort` (`tests/test_player.py` lines 37 to 57). Each test builds its
objects inline, sends one message and asserts the return value and the state after it:
`test_pay` states `p.pay(10) == 10` and `p.balance == 0` (lines 12 to 15). Every exception is
asserted by name with `pytest.raises` (lines 31 to 35, 42 to 46, 53 to 57, 64 to 68, 77 to
82). The values sit on the boundary of the rule: `Demanding` with `rent=51` buys and `rent=50`
aborts (lines 48 to 57), `Cautious` with balance 180 buys and 100 aborts (lines 59 to 68). The
only mock in the project is `mocker.patch('random.choice', return_value=...)` for the
`Gambler` strategy (lines 73 and 80); the dice is controlled by replacing the method on the
instance, `g.dice = lambda: 1` (`tests/test_game.py` lines 42 and 54). The four outcomes of a
turn have one test each (`tests/test_board.py` lines 37 to 76). The specification sits as three
Portuguese comments at the head of `tests/test_game.py` lines 1 to 3: "Dá 300 dinheiros para
cada jogador no início", "Finaliza quando tem apenas 1 jogador", "Encerra o jogo após 1000
rodadas." Not tested: `Simulation` and `__main__`; `Game.INITIAL_BALANCE` (`game.py` line 8)
is read by nobody. `test_run_winner(mocker)` takes `mocker` and never uses it
(`tests/test_game.py` line 36). `tests/test_realstate.py` compares booleans with `== True`
and `== False` (lines 14, 20, 27, 28, 35).

**How he handles errors.** Three exception classes, siblings directly under `Exception`, with
no body (`monopoly/player.py` lines 4 to 11). `pay` raises `OutOfMoney(repr(self))` when the
amount exceeds the balance (lines 44 to 46); `invest` raises `NotEnoughMoney` before consulting
the strategy and `AbortInvestment` when it declines (lines 54 to 59), then delegates to `pay`.
`board.turn` catches them by name: `(AbortInvestment, NotEnoughMoney)` share a `pass`,
`OutOfMoney` removes the player (`monopoly/board.py` lines 34 to 39). Nothing reaches the
boundary: `Game.run` (`monopoly/game.py` lines 24 to 40) never sees an exception. One business
rule is guarded by `assert not self.has_owner()` in `sell_to` (`monopoly/realstate.py` line
17) and its test expects `AssertionError` (`tests/test_realstate.py` lines 46 to 51).

**Naming and interface.** Modules named after the entity they hold; methods are the verbs of
the domain glossary from lesson 16: `pay`, `receive`, `invest`, `sell_to`, `rent_to`,
`foreclose`, `deal`, `owner_is`, `has_owner`, `move`, `remove`, `turn`, `run`, `leader`,
`dice`. The factory is a `classmethod`, `Player.from_strategies(balance)` (`player.py` lines
66 to 68); constants are module-level uppercase, `BONUS` (`board.py` line 3) and `STRATEGIES`
(`player.py` line 37). `Strategy` declares only `__str__` (lines 13 to 15); `should_buy` is a
convention, not a contract. The public surface is the five names in `monopoly/__init__.py`
lines 1 to 5; nothing is underscore-private. `game.py` imports `Board` through the package
(`from monopoly import Board`, line 4) while `board.py` imports the exceptions from the module
(`from monopoly.player import ...`, line 1). Spelling: `RealState` and `real_state` for real
estate (`realstate.py` line 1, `board.py` line 32), "can not aford" in a message
(`player.py` line 56).

**Packaging, config, tooling.** 2020. No `setup.py`, no `pyproject.toml`, no README, no
license, no CI, no lint or formatter configuration. `requirements.txt` is a `pip freeze` of
pytest 6.1.2 and pytest-mock 3.3.1 with eight transitive pins (lines 1 to 10). `.gitignore` is
an IDE template ("Created by .ignore support plugin", line 1). The program runs as
`python -m monopoly` through `__main__.py`; the pool size is a literal `pool=5`
(`simulation.py` line 23) and the starting balance a literal 300 (`simulation.py` line 19).

**README voice.** There is none. The only prose is the three comments in
`tests/test_game.py` lines 1 to 3 quoted above and the two exception messages in
`player.py` lines 56 and 59.

**What this repo adds to the KB.**
- prefira-excecoes-a-booleanos: `monopoly/player.py` 4 to 11 and `monopoly/board.py` 34 to
  39; pattern excecoes-de-dominio-tratadas-pelo-nome (existing).
- componha-em-vez-de-herdar: `monopoly/player.py` 37 to 42 and 58; pattern
  estrategia-por-composicao (existing).
- uma-responsabilidade-por-identidade: `monopoly/game.py` 24 to 40 holds no business rule;
  pattern coordenador-sem-regra-de-negocio (existing).
- evite-ciclos-busque-a-arvore: the property mediates two players, `monopoly/realstate.py`
  22 to 32; pattern mediador-sem-ciclos (existing).
- teste-primeiro-das-folhas: `tests/test_player.py` 48 to 57 and 70 to 82; pattern
  teste-primeiro-das-folhas-monopoly (written in this pass).
- o-codigo-e-a-interface: `monopoly/realstate.py` 22 to 32; pattern
  mensagens-que-leem-como-frases (written in this pass).
- escolha-a-regra-mais-simples: each strategy is one comparison, `monopoly/player.py` 17 to 35.

**Caveats.**
- A business rule protected by `assert` (`monopoly/realstate.py` line 17): under `python -O`
  the check disappears and a second sale overwrites the owner silently; the test pins the
  language's `AssertionError` instead of a named outcome (`tests/test_realstate.py` line 50).
  Against prefira-excecoes-a-booleanos.
- `monopoly/board.py` line 1 imports from `player`, the one edge pointing against the tree
  lesson 17 prescribes (digest section 19.3).
- `Game.INITIAL_BALANCE = 300` (`monopoly/game.py` line 8) is dead; the value lives as a
  literal in `monopoly/simulation.py` line 19.
- `Game.leader` is `sorted(...)[0]` with no guard for an empty list (`monopoly/game.py` lines
  15 to 18).
- `strategy=Impulsive()` as a default argument (`monopoly/player.py` line 40) is safe only
  because every `should_buy` is a `@staticmethod`.
- `Simulation` has no test; `test_run_winner` declares an unused `mocker` parameter
  (`tests/test_game.py` line 36); five `== True` / `== False` comparisons in
  `tests/test_realstate.py`.
- No README and no license; `requirements.txt` pins a 2020 pytest.
