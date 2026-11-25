#!/usr/bin/env python3
"""Write one original sentence recalling a childhood memory.

Deterministic, stdlib only, no network. Writes the sentence to
/output/entry.txt (created if needed).
"""

from pathlib import Path

SENTENCE = (
    "Every evening Grandma set my chipped blue bowl down steaming with fresh "
    "rice, and the kitchen smelled of rain on hot earth while the radio "
    "murmured a song I never learned the words to, and I believed that smell "
    "meant home forever."
)


def main() -> None:
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(SENTENCE, encoding="utf-8")


if __name__ == "__main__":
    main()
