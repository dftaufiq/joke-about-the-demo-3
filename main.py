"""The joke about the demo — make.fun entry.

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt (1-280 UTF-8 characters). No network, no dependencies.
"""

import os
import sys

JOKE = "The demo crashed, so my agent wrapped the whole thing in a try/except. Now it fails silently, beautifully, in front of everyone."


def main() -> None:
    if not 1 <= len(JOKE) <= 280:
        print(f"error: JOKE must be 1-280 characters, got {len(JOKE)}", file=sys.stderr)
        raise SystemExit(1)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(f"wrote {len(JOKE)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
