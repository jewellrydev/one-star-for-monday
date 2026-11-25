"""One Star for Monday — a make.fun entry.

Prints exactly one line: a one-star review of Monday, at most 25
words, with no explanation attached.
"""

LINE = (
    "One star: advertised as a fresh start, arrived as "
    "the sequel nobody asked for, and the weekend DLC costs extra."
)


def build_line() -> str:
    line = LINE
    assert len(line.split()) <= 25, f"too many words: {len(line.split())}"
    assert "\n" not in line
    return line


if __name__ == "__main__":
    print(build_line())
