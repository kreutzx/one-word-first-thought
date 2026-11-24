"""One Word, First Thought — entry for make.fun.

Writes the entry text (a single word, the first thought) to /output/entry.txt.
"""

import os

ENTRY_TEXT = "Oops."


def main() -> None:
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # Exactly one word plus a trailing newline.
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY_TEXT + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
