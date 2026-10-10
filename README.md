<p align="center"><img src="assets/logo.svg" alt="henriquefy logo" width="128"></p>

# henriquefy

Claude Code skills that know how [Henrique Bastos](https://github.com/henriquebastos)
([HB Network](https://www.youtube.com/@hbnetworkoficial)) writes Python, designs APIs, models
objects and tests, and that apply those practices to your code. A sentence the skill attributes
to him carries a citation: a lesson, or a path and commit in one of his repositories.

```
uvx henriquefy install
```

That writes the `henriquefy` skill into `~/.claude/skills/`. In Claude Code, run `/henriquefy`,
or ask what Henrique would do with the code in front of you.

`uvx henriquefy@latest update` refreshes an install already on disk. `install --project` writes
into `./.claude/skills/` of the current directory. `install --all` also installs the maintainer
skills `henrique-ingest` and `henrique-watch`.

## Modes

| Mode | What you get |
|---|---|
| `ask` | An answer or a review of a snippet, with a citation on each point |
| `check` | Mechanical findings from the CLI, then judgment findings the rules cannot see |
| `grade` | The Nota mecânica from the CLI, then the Nota do Henrique: 0 to 10 on seven dimensions, and a letter |
| `transform` | A rewrite in his style, one principle per change, tests run between changes |

`ask` and `transform` run in the skill. `check` and `grade` also run as a CLI, with no Claude in the loop:

```
uvx henriquefy check path/
uvx henriquefy grade path/
```

`check` exits 1 when it has findings. The Nota mecânica is deterministic, and it is never his
verdict. The letter that follows it is the skill's judgment, and the skill says so.

## Knowledge base

The skill reads `kb/`. The generated list of every principle, pattern, repository and course is
[kb/INDEX.md](kb/INDEX.md): 34 principles, 15 patterns, 13 repository digests. `kb/repos/drift.md`
dates how his tooling changed. Principle files are in English. Course digests are in Portuguese.

Seven course digests are in `kb/courses/`, written from the automatic captions of the playlists (a few lessons without captions were transcribed with Whisper).
A quote in a digest is a paraphrase of those captions and has not been checked against the video.

| Digest | Course | Lessons |
|---|---|---|
| `oo-na-pratica` | [Orientação a Objetos na Prática](https://www.youtube.com/playlist?list=PLeKXYyZCJHxemNCYYvDUw0wRsMiN7aX1m) | 23 |
| `design-api-na-pratica` | [Design de API na Prática](https://www.youtube.com/playlist?list=PLeKXYyZCJHxdD1CXDeEymwI1S9wlcsmYo) | 9 |
| `refatoracao-na-pratica` | [Refatoração na Prática](https://www.youtube.com/playlist?list=PLeKXYyZCJHxfTqEvicb9dqcbj-eCOFhhj) | 34 |
| `raio-x-da-oo` | [Raio X da Orientação a Objetos](https://www.youtube.com/playlist?list=PLeKXYyZCJHxdT8vUW3x9bd7B8PnwnHINW) | 5 |
| `procedural-para-oo` | [Transforme seu código Procedural em Orientado a Objetos](https://www.youtube.com/playlist?list=PLeKXYyZCJHxeKQ13fuBUuLyfeOK9Jr8t7) | 10 |
| `raio-x-do-tdd` | [Raio-X do Test-Driven Development](https://www.youtube.com/playlist?list=PLeKXYyZCJHxe1X_B-o5bMDyNLxIBQB1q7) | 5 |

The playlist inventory, including what is still queued, is [state/playlists.json](state/playlists.json).
The plan is [PLAN.md](PLAN.md).

## License

Independent project, not affiliated with or endorsed by Henrique Bastos or HB Network. Published
with his permission. See [NOTICE.md](NOTICE.md).

Code is MIT. Knowledge-base prose is [CC BY 4.0](kb/LICENSE), except the course digests, which
stay all rights reserved until he confirms a license in writing.
