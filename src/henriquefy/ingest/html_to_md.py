"""Convert a course digest from its HTML source to markdown under kb/courses/.

Keeps the h2 numbering, tables, code blocks and blockquotes, so citations such as
`section: "12.9"` resolve to heading 12, item 9 of the output. Usage:

    python -m henriquefy.ingest.html_to_md sources/html/<course>.html kb/courses/<course>.md
"""

import re
import sys
from datetime import date
from html.parser import HTMLParser
from pathlib import Path

SKIP = {"style", "script", "nav", "head", "title"}
BLOCK = {"p", "div", "section", "article", "header", "footer", "h1", "h2", "h3", "h4", "li"}
HEADING = {"h1": "#", "h2": "##", "h3": "###", "h4": "####"}


class _Converter(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.out: list[str] = []
        self.skip = 0
        self.pre = False
        self.quote = 0
        self.lists: list[tuple[str, int]] = []
        self.table: list[list[str]] | None = None
        self.row: list[str] | None = None
        self.cell: list[str] | None = None
        self.href: str | None = None

    # -- writing helpers -------------------------------------------------
    def _write(self, text: str) -> None:
        if self.cell is not None:
            self.cell.append(text)
        else:
            self.out.append(text)

    def _newline(self, n: int = 1) -> None:
        if self.cell is not None:
            self.cell.append(" ")
            return
        joined = "".join(self.out[-3:])
        trailing = len(joined) - len(joined.rstrip("\n"))
        if trailing < n:
            self.out.append("\n" * (n - trailing))
        if self.quote and n:
            self.out.append("> " * self.quote)

    # -- tags ------------------------------------------------------------
    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        a = dict(attrs)
        if tag in SKIP:
            self.skip += 1
            return
        if self.skip:
            return
        if tag == "pre":
            self._newline(2)
            self._write("```\n")
            self.pre = True
        elif tag == "br":
            self._write("\n" if self.pre else "  \n")
        elif self.pre:
            return
        elif tag in HEADING:
            self._newline(2)
            self._write(HEADING[tag] + " ")
        elif tag == "blockquote":
            self._newline(2)
            self.quote += 1
            self.out.append("> " * self.quote)
        elif tag in ("ul", "ol"):
            self._newline(2 if not self.lists else 1)
            start = a.get("start") or "1"
            self.lists.append((tag, int(start) - 1 if tag == "ol" and start.isdigit() else 0))
        elif tag == "li":
            kind, n = self.lists[-1] if self.lists else ("ul", 0)
            if self.lists:
                self.lists[-1] = (kind, n + 1)
            self._newline(1)
            # CommonMark nests a list under its parent item's content column: 2 after "- ",
            # 3 after "1. ", 4 after "10. "
            indent = "".join(" " * (len(f"{m}. ") if k == "ol" else 2) for k, m in self.lists[:-1])
            self._write(f"{indent}{n + 1}. " if kind == "ol" else f"{indent}- ")
        elif tag == "table":
            self._newline(2)
            self.table = []
        elif tag == "tr":
            self.row = []
        elif tag in ("td", "th"):
            self.cell = []
        elif tag in ("strong", "b"):
            self._write("**")
        elif tag in ("em", "i"):
            self._write("*")
        elif tag == "code":
            self._write("`")
        elif tag == "a":
            self.href = a.get("href")
            self._write("[")
        elif tag in ("p", "div", "section", "article", "header") and self.cell is None:
            self._newline(2 if tag == "p" else 1)

    def handle_endtag(self, tag: str) -> None:
        if tag in SKIP:
            self.skip = max(0, self.skip - 1)
            return
        if self.skip:
            return
        if tag == "pre":
            self.pre = False
            self._write("\n```\n\n")
        elif self.pre:
            return
        elif tag in HEADING:
            self._newline(2)
        elif tag == "blockquote":
            self.quote = max(0, self.quote - 1)
            self._newline(2)
        elif tag in ("ul", "ol"):
            self.lists.pop()
            self._newline(2 if not self.lists else 1)
        elif tag == "table":
            self._emit_table()
            self.table = None
        elif tag == "tr":
            if self.table is not None and self.row is not None:
                self.table.append(self.row)
            self.row = None
        elif tag in ("td", "th"):
            if self.row is not None and self.cell is not None:
                text = re.sub(r"\s+", " ", "".join(self.cell)).strip().replace("|", "\\|")
                self.row.append(text)
            self.cell = None
        elif tag in ("strong", "b"):
            self._write("**")
        elif tag in ("em", "i"):
            self._write("*")
        elif tag == "code":
            self._write("`")
        elif tag == "a":
            self._write(f"]({self.href})" if self.href else "]")
            self.href = None
        elif tag == "p":
            self._newline(2)

    def handle_data(self, data: str) -> None:
        if self.skip:
            return
        if self.pre:
            self._write(data)
            return
        text = re.sub(r"\s+", " ", data)
        buf = self.cell if self.cell is not None else self.out
        if text.strip() or (buf and not buf[-1].endswith("\n")):
            self._write(text)

    def _emit_table(self) -> None:
        if not self.table:
            return
        width = max(len(r) for r in self.table)
        rows = [r + [""] * (width - len(r)) for r in self.table]
        lines = ["| " + " | ".join(rows[0]) + " |", "|" + "---|" * width]
        lines += ["| " + " | ".join(r) + " |" for r in rows[1:]]
        self.out.append("\n".join(lines) + "\n\n")

    def text(self) -> str:
        md = "".join(self.out)
        md = re.sub(r"[ \t]+\n", "\n", md)
        md = re.sub(r"\n{3,}", "\n\n", md)
        return md.strip() + "\n"


def convert(html: str) -> str:
    conv = _Converter()
    conv.feed(html)
    conv.close()
    return conv.text()


def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    if len(argv) != 2:
        print(__doc__, file=sys.stderr)
        return 2
    src, dest = Path(argv[0]), Path(argv[1])
    body = convert(src.read_text(encoding="utf-8"))
    header = (
        f"<!-- converted from {src.name} by henriquefy.ingest.html_to_md on {date.today()};"
        " see kb/courses/README.md for provenance and license -->\n\n"
    )
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(header + body, encoding="utf-8")
    print(f"{dest}: {len(body.splitlines())} lines")
    return 0


if __name__ == "__main__":
    sys.exit(main())
