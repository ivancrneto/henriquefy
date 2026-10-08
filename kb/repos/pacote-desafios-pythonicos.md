---
repo: henriquebastos/pacote-desafios-pythonicos
commit: ae90952cdaa7690a31e62f4715f0bd60600213b3
era: 2020 to 2023
license: none
class: his
---
# pacote-desafios-pythonicos

**What it is.** A kit of fourteen beginner Python exercises, one file each, plus three text
fixtures (`alice.txt`, `letras.txt`, `small.txt`). No README, no package, no dependencies:
every file is a Portuguese spec in a docstring, an empty function to fill in, and a built-in
checker. Three commits, all his, 2020-03-21 to 2020-04-01 ("Initial commit", "import",
"Melhorias"); 224 forks on GitHub, which is why it sits in the manifest as calibration
material. The exercise set, the function names, the sample inputs and the fixture files match
Google's Python Class basic exercises (string1, string2, list1, list2, wordcount, mimic),
translated to Portuguese; the clone has no attribution file at this commit. Unlicensed:
excerpts below are quotation-length.

**Layout.**

```
pacote-desafios-pythonicos/
├── .gitignore            *pyc, __pycache__, .idea
├── 01_donuts.py          string from a count, 'many' from 10 up
├── 02_both_ends.py       first two and last two characters
├── 03_fix_start.py       replace later occurrences of the first character
├── 04_mix_up.py          swap the first two characters of two words
├── 05_verbing.py         append 'ing' or 'ly'
├── 06_not_bad.py         replace 'not ... bad' with 'good'
├── 07_front_back.py      interleave halves of two strings
├── 08_match_ends.py      count words whose ends match
├── 09_front_x.py         sort with 'x' words first
├── 10_sort_last.py       sort tuples by last element
├── 11_remove_adjacent.py collapse adjacent duplicates
├── 12_linear_merge.py    merge two sorted lists in one pass
├── 13_wordcount.py       --count and --topcount over a file (skeleton with main())
├── 14_mimic.py           Markov-style text imitation (skeleton with main())
├── alice.txt             3600 lines of input for 13 and 14
├── letras.txt            the README example for 13 ("A a C c c B b b B")
└── small.txt             five lines for 14
```

**How he tests.** No runner. Each of files 01 to 12 ends with the same checker and a
`__main__` block that calls it with three or four cases:

```python
def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}({in_!r}) retornou {out!r} {info}')
```
(`01_donuts.py:19-33`), called as `test(donuts, 10, 'Number of donuts: many')`
(`01_donuts.py:36-41`, under "Testes que verificam o resultado do seu código em alguns
cenários."). Two-argument exercises take a tuple and splat it, `out = f(*in_)`
(`04_mix_up.py:27`, `07_front_back.py:25`, `12_linear_merge.py:24`). The cases include the
edge the spec names: `'a'` gives `''` for `both_ends` (`02_both_ends.py:38`), `'do'` is left
alone by `verbing` (`05_verbing.py:41`), the empty list for `remove_adjacent`
(`11_remove_adjacent.py:39`). The checker is copied into every file rather than imported, so
`python 05_verbing.py` runs with nothing else present. Files 13 and 14 have no checker: they
ship a `main()` that parses `sys.argv` and calls the functions the student must write
(`13_wordcount.py:63-76`, `14_mimic.py:60-66`). The spec is written before the code, and the
code is a stub: `def donuts(count): # +++ SUA SOLUÇÃO +++ return` (`01_donuts.py:12-14`).

**How he handles errors.** Nothing is raised. The two command-line skeletons print usage and
exit: `print('Utilização: ./13_wordcount.py {--count | --topcount} file')` then `sys.exit(1)`
(`13_wordcount.py:64-66`), and `print('unknown option: ' + option)` then `sys.exit(1)`
(`:74-76`). A wrong answer in files 01 to 12 is reported with ❌ and the process still exits 0
(`01_donuts.py:29-33`); the checker informs, it does not fail.

**Naming and interface.** Files are `NN_name.py`, numbered in the order to be done; the
function inside carries the same name (`donuts`, `both_ends`, `fix_start`, `mix_up`,
`verbing`, `not_bad`, `front_back`, `match_ends`, `front_x`, `sort_last`, `remove_adjacent`,
`linear_merge`, `print_words`/`print_top`, `mimic_dict`/`print_mimic`). The checker's second
parameter is `in_` with a trailing underscore to avoid the keyword (`01_donuts.py:19`).
Parameters are named by role, `words`, `nums`, `tuples`, `list1`, `list2`, `filename`
(`08_match_ends.py:11`, `11_remove_adjacent.py:11`, `10_sort_last.py:12`,
`12_linear_merge.py:12`, `14_mimic.py:46`). The public surface of each file is one function
plus `test`; there is nothing private.

**Packaging, config, tooling (2020).** None: no `setup.py`, no `requirements.txt`, no CI, no
lint, a three-line `.gitignore`. The only version signal is syntax: f-strings
(`01_donuts.py:31, 33`) require Python 3.6 or newer, and the emoji in the output expects a
UTF-8 terminal. This is a kit to be copied, not installed.

**README voice.** There is no README; the module docstrings are the voice. Each starts with
the number and name, then a spec in the second person with an example: "Dado um contador
inteiro do numero de donuts, retorne uma string com o formato 'Number of donuts: <count>'"
(`01_donuts.py:4-5`), "Exemplo: 'babble' retorna 'ba**le'" (`03_fix_start.py:8`). Hints are
labeled "Dica:" and point at the method to use (`03_fix_start.py:12-13`, `09_front_x.py:10-11`,
`10_sort_last.py:10`). The longest docstring, in `13_wordcount.py:1-52`, shows the expected
shell session (`:18-21`, `:34-37`) and closes with method advice: "Não construa todo o
programade uma vez. Faça por partes executando e conferindo cada etapa do seu progresso."
(`13_wordcount.py:50-51`). Every file marks where the student's work begins, "# +++ SUA SOLUÇÃO
+++" (`01_donuts.py:13`), and where it ends, "# --- Daqui para baixo são apenas códigos
auxiliáries de teste. ---" (`:17`).

**What this repo adds to the KB.**
- `teste-primeiro-das-folhas`: the spec and the cases exist before any implementation; the
  function body is `return` (`01_donuts.py:12-14, 36-41`). Each file is one leaf.
- `o-codigo-e-a-interface`: the checker's output is a sentence about the call,
  `donuts(10) retornou None e o correto é 'Number of donuts: many'` (`01_donuts.py:33`).
- `escolha-a-regra-mais-simples`: "Faça por partes executando e conferindo cada etapa"
  (`13_wordcount.py:50-51`) is the working rule the OO course applies in its implementation
  lessons.
- Pattern files: none written or amended in this pass. A `his` rendition candidate is the
  self-contained checker (`test(f, in_, expected)`) as the smallest possible test harness.

**Caveats.**
- The checker reports but never fails: a wrong solution prints ❌ and exits 0
  (`01_donuts.py:26-33`). The courses use `assert` and `pytest.raises` so a wrong answer stops
  the run (`kb/courses/oo-na-pratica.md:834`).
- The same fourteen lines are pasted into twelve files (`01_donuts.py:19-33` and the eleven
  copies). Deliberate, so each file stands alone, but a bug in the checker needs twelve fixes.
- `14_mimic.py` is indented with two spaces (`:46-70`) while the placeholder comments inside
  it use four (`:49, 55`) and every other file uses four; `dict = mimic_dict(sys.argv[1])`
  shadows the builtin (`:65`).
- Docstring typos: "auxiliáries" (`01_donuts.py:17` and copies), "parêmatros" and
  "programade" (`13_wordcount.py:49-50`), "parêtros" (`:62`).
- No attribution to the original exercise set, no license, no README at this commit.
