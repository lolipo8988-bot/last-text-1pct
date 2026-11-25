"""Last Text at One Percent entry.

Writes a single final text message, in the voice of a phone at one
percent battery, to /output/entry.txt. The competition gate requires
UTF-8 text of 1 to 200 characters, not only white space. The program
is deterministic: every run writes exactly the same bytes.

The message is assembled from the phone's dying confessions, in the
order a phone running out of time would blurt them: the incriminating
history, the charger it deceived, the socket it actually loved, and
one last plea for dignity at the funeral.
"""

import os

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT_PATH", "/output/entry.txt")
MAX_CHARS = 200

OPENING = "1%, final text: "
CONFESSIONS = (
    "delete my search history",
    "tell the nightstand charger I faked every spark \u2014 the kitchen socket was the one",
    "no Face ID at my funeral",
)
CLOSER = "Undignified."


def build_text() -> str:
    """Join the confessions into one punchy, comma-separated text."""
    return OPENING + ", ".join(CONFESSIONS[:-1]) + " \u2014 and " + CONFESSIONS[-1] + ". " + CLOSER


def validate(text: str) -> None:
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry must be 1..{MAX_CHARS} characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> None:
    text = build_text()
    validate(text)
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
