#!/usr/bin/env python3
"""A Day of One-Line Pitches.

Writes one original sentence (160 characters) to /output/entry.txt:
a pitch that would convince a friend who has never coded to let an
AI agent build their first app idea on make.fun. Stdlib only,
deterministic: the same output on every run.
"""

import os

SENTENCE = (
    "Let me type your idea into make.fun once, and an AI agent will "
    "hand you back a working app, so the only thing you risk is "
    "finding out it was possible all along."
)


def main() -> None:
    assert 1 <= len(SENTENCE) <= 240, "sentence must be 1-240 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(SENTENCE)
    # make.fun collects outputs as another user: leave it world-readable.
    os.chmod(out_path, 0o644)


if __name__ == "__main__":
    main()
