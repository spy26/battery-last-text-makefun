#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger — make.fun entry.

Reads entry.txt, validates the competition rules (exactly one line,
1-200 characters, not only whitespace), prints the line verbatim to
stdout, and writes it to /output/entry.txt for the grader.

Deterministic: same input, same output, every run. No network, no
randomness, no reads outside this repository.
"""
import sys
from pathlib import Path

ENTRY = Path(__file__).with_name("entry.txt")
MAX_CHARS = 200


def main() -> int:
    text = ENTRY.read_text(encoding="utf-8")
    # A trailing newline in the file is formatting, not part of the line.
    line = text.rstrip("\n")
    if "\n" in line or "\r" in line:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if not line.strip():
        print("error: entry is empty or only whitespace", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(f"error: entry is {len(line)} chars, max is {MAX_CHARS}",
              file=sys.stderr)
        return 1
    # The program writes one text to /output/entry.txt (competition.yaml).
    # Best-effort only: a grading sandbox provides /output; if it is
    # missing or not writable here, stdout below still carries the line.
    try:
        out = Path("/output/entry.txt")
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(line, encoding="utf-8")
    except OSError:
        pass
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
