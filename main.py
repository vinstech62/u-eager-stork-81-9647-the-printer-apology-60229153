#!/usr/bin/env python3
"""The Printer Apology — make.fun bounty entry.

Writes one apology line from an office printer to /output/entry.txt.
Deterministic: the same line every run, no input, no network.
"""

import os

LINE = "I'm sorry I jammed your report. The paper was so cheap it jammed itself, and frankly, I was rooting for it."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not 1 <= len(LINE) <= 120:
        raise SystemExit("entry line must be 1-120 characters")
    if "\n" in LINE or not LINE.strip():
        raise SystemExit("entry line must be a single non-blank line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
