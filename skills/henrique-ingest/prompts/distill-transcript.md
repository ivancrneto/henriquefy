# distill-transcript

Input: `sources/transcripts/<course>/` with `playlist.json` and one timestamped transcript per
lesson (`NN-<video_id>.md`, lines `[h:mm:ss] text`). Output: `kb/courses/<course>.md` in the
same shape as the two hand-made digests, so citations resolve the same way everywhere.

## What the transcripts are

Automatic YouTube captions in Portuguese: no punctuation, no capitals, names and code mis-heard
(PyCharm became "pai Charme" in one digest). Treat every quote as `verified: false`: render it
without quotation marks, with lesson number and timestamp, and keep an obvious mis-hearing when
you must, annotated in brackets. Never invent a quote. Never clean a quote into something he did
not say.

## Two passes

1. **Per lesson.** For each transcript, in order: the lesson's one-paragraph summary, a
   timeline of 6 to 12 `[h:mm:ss]` entries naming what happens, the principles he states (with
   timestamp), code he writes or shows (reconstructed, marked as reconstruction), and 2 to 4
   quotes with timestamps.
2. **Cross-cutting.** Only after every lesson: the sections below that span the course.

## Digest schema (section numbers, in this order; keep the Portuguese titles)

1. Visão geral do curso (table: lessons, total duration, dates, views, playlist link)
2. Filosofia e método de ensino
3. Pilares conceituais
4. As aulas em uma tabela (number, title, duration, one-line focus)
5. Resumo por aula (the per-lesson pass, one `###` per lesson, with the video link)
6. Princípios que atravessam toda a série (numbered, each with lesson and timestamp)
7. Citações-chave do curso (table: lesson, timestamp, paraphrase)
8. A evolução técnica, aula a aula
9. Arsenal técnico demonstrado no curso
10. Glossário do curso
11. Perguntas e respostas que o curso responde
12. Repositórios e recursos (his only; a community reimplementation may be named as a
    reference, never graded or excerpted)
13. Análise linha a linha do código real (only if he published the code; otherwise say so)
14. Execução real dos testes (only if the code runs; otherwise say so)

Section 6 is what feeds `kb/principles/`: each principle there must be traceable to a lesson
and timestamp. Write in Portuguese, like the existing digests; the KB prose around it is English.

## Rules

- Every claim carries a lesson and a timestamp. A claim with neither does not go in.
- Code: say whether it is reconstructed from what he says, or published by him (repo, path).
- No em-dashes. No [[wikilinks]]. No alumni code.
- Finish with a colophon stating the source (playlist, caption language, fetch date), that quotes
  are unverified transcript paraphrases, and what the course left unpublished.
