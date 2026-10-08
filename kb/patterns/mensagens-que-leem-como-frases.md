---
id: mensagens-que-leem-como-frases
title: Messages that read as sentences
principle: o-codigo-e-a-interface
category: readability
frameworks:
  python: {origin: his, repo: henriquebastos/monopoly, path: monopoly/realstate.py, commit: bffb0c269b00836066d0bb064ca4e38a80cad210}
---
**What.** An interaction between objects is written as the sentence the domain would say:
subject, verb, object, each object answering one message and returning what the next message
needs. No object reads or writes another's attributes; a method that moves a value returns it
so the caller can hand it on; a method that cannot proceed raises, so the sentence carries no
`if`. The test of the method is the same sentence with concrete numbers. It applies whenever a
method is about to call a getter on a collaborator, or to return a flag that says what
happened.

## python
`monopoly/realstate.py` at commit `bffb0c2`, lines 22 to 32:

```python
    def rent_to(self, player):
        if self.owner_is(player):
            return

        self.owner.receive(player.pay(self.rent))

    def deal(self, player):
        if self.has_owner():
            self.rent_to(player)
        else:
            self.sell_to(player)
```

What to notice. Line 26 is three messages in one line: the player pays the rent, the payment
comes back as a value, the owner receives it. The property never touches a balance. `pay` in
`monopoly/player.py` lines 44 to 49 returns the amount precisely so this sentence can be
written, and raises `OutOfMoney` when it cannot pay, so the line needs no check and the board
decides what bankruptcy means. The course digest calls it the most elegant line of the project
(section 19.2). `deal` reads as the rule of lesson 14: with an owner the property is rented,
without one it is sold, and the property decides, not the board. The guard `owner_is(player)`
is a question named as one, using identity. The test says the same sentence with numbers:
`p2.receive(p1.pay(10))` in `tests/test_player.py` line 26, and `test_rent` in
`tests/test_realstate.py` lines 53 to 59 sends `r.rent_to(p2)` and asserts `p1.balance == 5`
and `p2.balance == 0`.

## Bad
The same logic with getters, setters and a flag:

```python
    def rent_to(self, player):
        if self.get_owner() == player:
            return False
        rent = self.get_rent()
        if player.get_balance() < rent:
            return False                        # bankrupt, or just declined?
        player.set_balance(player.get_balance() - rent)
        self.get_owner().set_balance(self.get_owner().get_balance() + rent)
        return True
```

The property now owns a rule about balances that belongs to the player, every caller has to
interpret `False`, and no line says who paid whom.
