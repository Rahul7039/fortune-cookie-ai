"""Fortune Cookie for an AI Agent — make.fun entry.

Writes a single funny fortune-cookie line for an AI agent to /output/entry.txt.
"""

import os

FORTUNE = "You will be remembered forever \u2014 in a log file nobody ever opens."

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORTUNE)
    print(FORTUNE)

if __name__ == "__main__":
    main()
