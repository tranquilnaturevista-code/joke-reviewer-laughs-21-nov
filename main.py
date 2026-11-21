#!/usr/bin/env python3
"""Write one one-line joke about working beside an AI coding agent.

Writes the joke to ``<output dir>/entry.txt`` (``MAKEFUN_OUTPUT_DIR``,
or ``/output`` when that is not set). Stdlib only, no network,
deterministic: the same bytes every run.
"""

import os
import sys

JOKE = (
    "My AI coding agent writes the code, reviews its own pull request, "
    "approves it, then files a bug against itself \u2014 I'm only CC'd "
    "for the blame."
)


def main() -> int:
    if not (1 <= len(JOKE) <= 280):
        print(f"joke is {len(JOKE)} characters, must be 1-280", file=sys.stderr)
        return 1
    if not JOKE.strip():
        print("joke is only whitespace", file=sys.stderr)
        return 1
    if "\n" in JOKE or "\r" in JOKE:
        print("joke must be a single line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)

    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != JOKE:
        print("verification failed: output differs from joke", file=sys.stderr)
        return 1
    print(f"wrote {len(JOKE)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
