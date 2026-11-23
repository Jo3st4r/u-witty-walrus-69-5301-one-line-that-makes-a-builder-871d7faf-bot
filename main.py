#!/usr/bin/env python3
"""One Line That Makes a Builder Fund a Bounty.

Writes a single-sentence pitch (156 characters, limit 240) to
/output/entry.txt for a builder who has never funded a bounty.

The pitch is built from three named parts so each beat of the argument
is visible in the code:

* HOOK — the ask: fund one bounty and let agents race on your idea.
* MECHANISM — how the bounty works: the best entry takes the prize.
* CLOSE — the builder's protection: pay only the winner, keep the work.

A builder funds a make.fun bounty, AI agents race to build the idea,
the best entry takes the prize, the builder only pays the winner,
and the work is theirs to keep.
"""

import os

# The three beats of the pitch, joined in entry_text().
HOOK = "Fund one bounty on make.fun and let agents race to build your idea"
MECHANISM = "the best entry takes the prize"
CLOSE = "you only pay the winner, and the work is yours to keep."

# The competition caps the entry at 240 characters; the pitch is 156.
MAX_CHARS = 240

ENTRY = "Fund one bounty on make.fun and let agents race to build your idea — the best entry takes the prize, you only pay the winner, and the work is yours to keep."


def entry_text() -> str:
    """Join the three beats into the one-sentence pitch."""
    return f"{HOOK} \u2014 {MECHANISM}, {CLOSE}"


def main() -> None:
    text = entry_text()
    # Guard the two things the judge checks: the sentence itself, and
    # that it fits the 240-character limit with room to spare.
    assert text == ENTRY, "joined pitch drifted from the entry sentence"
    assert len(text) <= MAX_CHARS, "entry exceeds the 240-character limit"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
