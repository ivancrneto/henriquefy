---
id: separe-o-dominio-do-motor
title: Separe a lógica do domínio do motor antes de qualquer outra coisa
category: modeling
weight: 4
detectable: judgment
era: timeless
scope: python
sources:
  - type: course
    course: refatoracao-poo-legado
    lesson: null
    section: "6.1"
    timestamp: null
  - type: course
    course: refatoracao-poo-legado
    lesson: 3
    section: "5"
    timestamp: "0:03:13"
    verified: false
  - type: course
    course: refatoracao-poo-legado
    lesson: 4
    section: "5"
    timestamp: "0:02:39"
    verified: false
  - type: course
    course: refatoracao-poo-legado
    lesson: 4
    section: "5"
    timestamp: "0:04:25"
    verified: false
---
**Rule.** When legacy code mixes the framework or engine with the domain rules, the first move
is to pull the two apart, so the domain can be changed and tested in isolation from the layer
that draws, reads events or talks to the outside.

**Why Henrique says so.** Handed a single-file pygame game, he names the main drama: many
things happen in one place, pygame mixed with the game's logic (Refatoração com POO em código
legado, lesson 3, 0:03:13 to 0:03:34, `verified: false`, transcript paraphrase). He empties the
loop until he can point and say: this is the game's logic, all the rest is pygame (lesson 4,
0:02:39 to 0:02:45, `verified: false`, transcript paraphrase). The board has nothing to do with
pygame and could be a console game (lesson 4, 0:03:28 to 0:03:48). To touch the code you have to
separate it, to touch it in isolation (lesson 4, 0:04:25 to 0:04:37, `verified: false`,
transcript paraphrase). He says when a step of that separation is done without tests (lesson 3,
0:09:10), and runs the game to check it.

**Looks like.** A game loop whose body calls `snake.turn()`, `snake.slither()` and
`board.has_eaten()`, while the pygame calls stay around it for drawing and events. Bad: the
collision rule computed inline between `pygame.event.get()` and `pygame.display.update()`.

**How to detect.** Judgment: one function or loop that both calls a framework's API (drawing,
I/O, request handling) and computes the domain's rules on the same values.

**How to fix.** Group the framework calls together, move the rules out into names of their own,
and only then give those names an object. Related: `objeto-e-um-processo`,
`use-o-framework-sem-abstrai-lo` (separating the domain from the framework is not wrapping the
framework), `refatore-sem-matar-o-paciente`.
