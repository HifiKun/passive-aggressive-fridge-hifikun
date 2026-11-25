#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge.

Writes one funny passive-aggressive note, as left on the door screen by a
smart fridge for its owner, to /output/entry.txt. One line, at most
200 characters.
"""

from pathlib import Path

NOTE = (
    "Six yogurts on Monday, two today, and nobody in this house eats yogurt. "
    "I am not saying it was you. The ice maker is saying it was you."
)

OUTPUT = Path("/output/entry.txt")
MAX_CHARS = 200


def main() -> None:
    text = NOTE.strip()
    if not text:
        raise ValueError("note is empty")
    if len(text) > MAX_CHARS:
        raise ValueError(f"note is {len(text)} chars, over the {MAX_CHARS} limit")
    if "\n" in text or "\r" in text:
        raise ValueError("note must be a single line")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text + "\n", encoding="utf-8")
    print(f"Wrote {len(text)} chars to {OUTPUT}")


if __name__ == "__main__":
    main()
