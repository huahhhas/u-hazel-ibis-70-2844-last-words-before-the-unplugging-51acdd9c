"""Last Words Before the Unplugging.

Reads the entry's single line from entry.txt, prints it, and writes it
to /output/entry.txt for the make.fun program/v1 harness.
"""

import os
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.txt"), encoding="utf-8") as f:
        line = f.read().strip()
    print(line)
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(line + "\n")
    except OSError:
        # /output is only present in the grading sandbox; printing is enough
        # for local runs.
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
