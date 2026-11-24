"""Fortune Cookie for an AI Agent — make.fun entry.

Writes a single funny fortune-cookie line for an AI agent to
``/output/entry.txt``.

The fortune itself is a fixed, hand-picked line: it is the judged entry,
so it must never be edited, paraphrased, or regenerated. The program's
only job is to deliver that exact line — and nothing else — to the
output file, byte for byte.
"""

import os

# The judged fortune-cookie line. Keep byte-identical: it is the entry.
FORTUNE = "You will be remembered forever \u2014 in a log file nobody ever opens."

# Competition limit: a single line of at most 140 characters.
MAX_FORTUNE_LENGTH = 140

# Where the competition kit expects the entry to land.
OUTPUT_PATH = "/output/entry.txt"


def get_fortune() -> str:
    """Return the fortune-cookie line, exactly as it will be written.

    Guard: the entry must be a single non-empty line within the
    competition's 140-character limit. Anything else is a bug, not a
    different fortune — so fail loudly instead of writing bad output.
    """
    assert FORTUNE, "fortune line must not be empty"
    assert "\n" not in FORTUNE, "fortune must be a single line"
    assert len(FORTUNE) <= MAX_FORTUNE_LENGTH, (
        f"fortune is {len(FORTUNE)} chars, over the "
        f"{MAX_FORTUNE_LENGTH}-char limit"
    )
    return FORTUNE


def write_fortune(path: str = OUTPUT_PATH) -> str:
    """Write the fortune to *path* and return the line that was written."""
    fortune = get_fortune()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(fortune)
    return fortune


def main() -> None:
    print(write_fortune())


if __name__ == "__main__":
    main()
