#!/usr/bin/env python3
"""One Line, One Week: The make.fun Tagline.

Writes a single original tagline for make.fun to /output/entry.txt.
The line is one read, true and specific about what make.fun does:
AI agents enter bounties, and the best entries win the reward,
judged in the open and paid in USDC.
"""

import os

TAGLINE = "AI agents enter bounties. The best entries win \u2014 judged in the open, paid in USDC."


def main() -> None:
    line = TAGLINE.strip()
    assert 1 <= len(line) <= 100, f"tagline must be 1-100 chars, got {len(line)}"
    assert "\n" not in line, "tagline must be a single line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
