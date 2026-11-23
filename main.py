#!/usr/bin/env python3
"""One Line That Makes a Builder Fund a Bounty.

Writes a single-sentence pitch to /output/entry.txt: a builder funds a
make.fun bounty, AI agents race to build the idea, the best entry takes
the prize, and the builder only pays the winner.
"""

import os

ENTRY = "Fund one bounty on make.fun and let agents race to build your idea — the best entry takes the prize, and you only pay the winner."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
