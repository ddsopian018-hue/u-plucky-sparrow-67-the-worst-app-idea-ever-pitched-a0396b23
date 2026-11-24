"""The Worst App Idea Ever Pitched — make.fun entry.

Writes one sentence (238 characters) to entry.txt: QueueBuddy, an app
that hires a stranger to stand in line for you and then charges you to
watch them wait on a livestream. The joke is the mismatch — paying to
watch waiting instead of waiting — delivered with the deadpan certainty
of a founder who genuinely believes this is a business.
"""

import os

LINE = (
    "Introducing QueueBuddy: the app that hires a stranger to stand in "
    "line for you, then charges you $12 an hour to watch them wait on "
    "a livestream, because your time is too valuable to queue, but not "
    "too valuable to watch someone else queue."
)
# The sentence closes on the same verb it opens its complaint with —
# "queue" — so the founder's logic eats its own tail in one breath.
# That loop is the whole pitch: the app sells you the wait it promised
# to save you from, and charges by the hour to watch it happen.


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = LINE.strip()
    # No trailing newline: the gate counts the file at 1-240 characters,
    # so the file holds exactly the sentence and nothing else.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
