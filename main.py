"""make.fun entry: The Dog Ate My Homework — Funniest Excuse.

Writes one line (under 200 characters) to /output/entry.txt: the excuse
a dog gives after being caught eating the homework, in the dog's own
voice. Pure standard library only.
"""

import os

EXCUSE = (
    "Look, the homework said 'eat me' in pencil. "
    "I can't read, but I can follow instructions."
)


def main() -> None:
    # The gate requires 1-200 characters of UTF-8 text, not only whitespace.
    text = EXCUSE.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
