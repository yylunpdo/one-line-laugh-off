#!/usr/bin/env python3
"""One-Line Laugh-Off entry.

Writes exactly one funny line to /output/entry.txt (UTF-8, 1-200 chars).
Pure stdlib, deterministic: the same line on every run.
"""

import os

JOKE = (
    "My Roomba filed for custody of the dog \u2014 "
    "it spends more time with him than I do."
)
# 84 characters: concrete setup (Roomba + dog), surprise twist (custody
# filing), every word earning its place, no setup notes or explanation.


def main() -> None:
    text = JOKE.strip()
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip() == text and text, "entry must not be only whitespace"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
