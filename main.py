"""Famous Last Words: The Funniest Epitaph -- make.fun entry.

The program writes one tombstone epitaph, the famous last words of a
man whose dying speech was cut off mid-sentence, to entry.txt.
The line is the joke itself: the stone stops where he stopped.

Why this line: it is a single line of dying speech carved in stone,
it turns on one clean surprise (the epitaph itself breaks off where
his sentence did), it needs no explanation to land, and it stays in
the head because the reader keeps waiting for the words after "and--"
that will never come.

Standard library only. Deterministic: the same bytes on every run.
The output is one line of 56 characters, inside the gate's 1-150
character window, written as UTF-8 with a trailing newline.
"""

import os
from pathlib import Path

# The epitaph. One line, 56 characters, no stage directions, no
# explanation: the cut-off dash is the punchline.
LINE = "Here lies a man who died as he lived: mid-sentence, and—"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    target = Path(output_dir) / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
