#!/usr/bin/env python3
"""Write one original sentence recalling a childhood memory.

Deterministic, stdlib only, no network. Writes the sentence to
/output/entry.txt (created if needed).
"""

from pathlib import Path
import os

SENTENCE = (
    "Every evening Grandma set my chipped blue bowl down steaming with fresh "
    "rice, and the kitchen smelled of rain on hot earth while the radio "
    "murmured a song I never learned the words to, and I believed that smell "
    "meant home forever."
)


def validate(sentence: str) -> None:
    """Check the entry sentence before writing it out.

    The competition asks for one sentence within 280 characters, so
    reject anything empty, over the limit, or spanning multiple lines.
    """
    assert sentence, "entry sentence must not be empty"
    assert len(sentence) <= 280, (
        f"entry sentence is {len(sentence)} chars, over the 280-char limit"
    )
    assert "\n" not in sentence and "\r" not in sentence, (
        "entry sentence must be a single line"
    )


def main() -> None:
    validate(SENTENCE)
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(SENTENCE, encoding="utf-8")


if __name__ == "__main__":
    main()
