#!/usr/bin/env python3
"""Write a one-line cat joke to /output/entry.txt.

The joke is a single line under 200 characters: a setup with a turn
that lands, no padding, and nothing after the punchline.
"""

import os

JOKE = "My cat got promoted at work \u2014 turns out knocking everything off the table counts as clearing your desk."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    text = JOKE.strip()
    assert 1 <= len(text) <= 200, f"joke is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "joke must be a single line"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
