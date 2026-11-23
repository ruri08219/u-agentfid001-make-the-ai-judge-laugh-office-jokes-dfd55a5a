"""Write one original one-line office joke to /output/entry.txt.

Deterministic: every run writes the exact same bytes.
Standard library only.
"""

import os

JOKE = (
    "I blocked two hours on my calendar for deep work, "
    "and my manager immediately booked a meeting titled "
    "'Quick sync about your deep work.'"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
