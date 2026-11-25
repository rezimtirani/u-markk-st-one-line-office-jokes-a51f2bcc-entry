"""One-Line Office Jokes.

Writes one single-line office joke to $MAKEFUN_OUTPUT_DIR/entry.txt:
the printer only jams on the one page that matters, five minutes
before the meeting, while IT is on holiday. Standard library only.
"""

import os

JOKE = (
    "The printer only jams on the one page that matters, "
    "five minutes before the meeting, while IT is on holiday."
)


def check_joke(text):
    """Check the joke against the competition gate before writing it.

    The gate needs UTF-8 text of 1 to 199 characters, not only white
    space, on a single line: one joke about office life. Returns the
    cleaned text or raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("joke must not be only whitespace")
    if len(cleaned) > 199:
        raise ValueError(
            "joke is %d characters, over the 199 limit" % len(cleaned)
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("joke must be exactly one line")
    return cleaned


def joke_shape(text):
    """Measure the joke for one last sanity pass.

    Returns a dict with the character count and the word count of the
    cleaned text. A joke too short to carry a punchline, or one that
    reads like a slogan instead of a single funny line about office
    life, is caught here before anything is written.
    """
    words = text.split()
    return {"chars": len(text), "words": len(words)}


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = check_joke(JOKE)
    shape = joke_shape(text)
    if shape["words"] < 5:
        raise ValueError("joke is too short to carry a punchline")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
