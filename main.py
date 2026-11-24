#!/usr/bin/env python3
"""Write the excuse entry to /output/entry.txt.

The entry is one line, under 200 characters: an AI agent's excuse
for a missed deadline. The same line is written on every run, so the
output is fully deterministic.
"""

import os

EXCUSE = "I was 99% confident I'd finish on time, then I spent the last 1% writing this excuse."

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    # Gate: the entry must be UTF-8 text of 1 to 200 characters,
    # not only white space, or the sealed scorer rejects it.
    if not 1 <= len(EXCUSE) <= 200 or not EXCUSE.strip():
        raise ValueError("entry must be 1-200 non-whitespace characters")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()
