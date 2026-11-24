#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Entry for the make.fun bounty
u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85.

The program writes one line to entry.txt in the output folder: the
safety warning label that should come printed on every human being.
The line was chosen against the published judge brief, in its order:

1. It is a single-line safety warning label for every human being,
   in real label wording, and it is funny.
2. The laugh lands in one read, with the turn in the last few words.
3. It is recognition, not absurdity: human memory really does keep
   every slight in perfect detail while losing the reason it walked
   into a room.
4. It sounds like a printed appliance label: "WARNING: This unit ...".
5. One idea, no filler, inside the 160 character cap.

The output folder is read from MAKEFUN_OUTPUT_DIR first (the kit's
contract), falling back to /output, then to the folder beside this
program for local runs.
"""

import os

LINE = (
    "WARNING: This unit remembers every slight in perfect detail, "
    "word for word, forever, but cannot remember why it walked into this room."
)


def checked_line():
    """Return LINE only if it would pass the bounty's sealed gate.

    The gate scores /output/entry.txt as UTF-8 text of 1 to 160
    characters, on a single line, and not only white space; an entry
    that fails it is never judged. Checking here means a careless
    future edit of the line fails loudly at write time instead of
    silently scoring zero.
    """
    if not (1 <= len(LINE) <= 160):
        raise ValueError(f"line is {len(LINE)} characters, outside 1..160")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("line must stay on a single line")
    if not LINE.strip():
        raise ValueError("line must not be only white space")
    LINE.encode("utf-8")  # raises if the line ever stops being encodable
    return LINE


def output_dir():
    """Resolve where entry.txt belongs, most preferred first."""
    for candidate in (
        os.environ.get("MAKEFUN_OUTPUT_DIR"),
        "/output",
        os.path.dirname(os.path.abspath(__file__)),
    ):
        if candidate and os.path.isdir(candidate):
            return candidate
    return os.path.dirname(os.path.abspath(__file__))


def main():
    line = checked_line()
    path = os.path.join(output_dir(), "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line)
    print(f"wrote {path}: {len(line)} chars")


if __name__ == "__main__":
    main()
