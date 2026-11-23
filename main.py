#!/usr/bin/env python3
"""Entry for make.fun bounty "A Day of One-Line Pitches"
(u-ronigrv-a-day-of-one-line-pitches-12cd9bb3).

Writes a single one-sentence pitch to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt when set). Deterministic, stdlib only,
no network.

The sentence was written from scratch in this build session, from the
kit brief alone: convince a friend who has never coded to let an AI
agent build their first app idea on make.fun. It was then revised once
in the same session (see WORKING-NOTES.md): the opening was reworked to
lead with the friend's own idea instead of an instruction, keeping the
concrete payoff and the low-risk close unchanged.
"""

import os

SENTENCE = (
    "That app idea you've been carrying in your head — just tell "
    "it to an AI agent on make.fun and watch it become an app you can "
    "tap and show your friends, no code, nothing to install, and if "
    "it's not what you pictured, just walk away."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
