#!/usr/bin/env python3
"""A Day of One-Line Pitches — entry program.

Writes one persuasive sentence (max 240 characters) to /output/entry.txt:
a pitch that convinces a friend who has never coded to let an AI agent
build their first app idea on make.fun.

Python 3.13 standard library only. Deterministic, no network access.
"""

import os

# Chosen pitch (candidate #5, revised after self-critique against the
# judge's criteria): it speaks directly to the non-coder friend, offers a
# concrete low-risk deal — a working first version, free — and the closing
# "nothing to lose" lands warmer than v1's "no risk". Plain words, no
# overpromising, one read.
PITCH = (
    "If you can explain your app idea to a friend, you can build it: "
    "tell it to an AI agent on make.fun and get a working first version "
    "for free, with no coding and nothing to lose if you don't love it."
)


def validate(text: str) -> str:
    """Return the pitch, enforcing the gate: 1-240 chars, not blank."""
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("pitch must not be blank")
    if len(cleaned) > 240:
        raise ValueError(f"pitch is {len(cleaned)} chars, over the 240 limit")
    return cleaned


def main() -> None:
    text = validate(PITCH)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
