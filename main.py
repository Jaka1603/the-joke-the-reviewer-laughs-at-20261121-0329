#!/usr/bin/env python3
"""Write the reviewer's one-line joke to /output/entry.txt.

This program is the whole entry: it holds one fixed joke
about a human approving an AI agent's pull request
without reading it, and writes that exact text to the
file the competition's gate reads. The joke is 77
Unicode code points, one line, plain ASCII, so it sits
far inside the 1-to-280 gate. Nothing is fetched, nothing
is generated at run time; the text is constant, which is
why two runs of the program produce byte-identical output.
"""

from pathlib import Path
import sys

OUT_DIR = Path("/output")
OUT_FILE = OUT_DIR / "entry.txt"
LIMIT = 280

JOKE = "I approved my agent's PR without reading it. In my defence, so did the agent."


def gate_error(text):
    """Name what is wrong with the text, or "" when it passes."""
    if text.strip() == "":
        return "entry is blank"
    if len(text) > LIMIT:
        return "entry is longer than 280 code points"
    if text.count("\n") > 0:
        return "entry spans more than one line"
    return ""


def run():
    error = gate_error(JOKE)
    if error != "":
        print("refusing to write entry.txt: " + error, file=sys.stderr)
        return 2
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text(JOKE, encoding="utf-8")
    if OUT_FILE.read_text(encoding="utf-8") != JOKE:
        print("read-back mismatch in " + str(OUT_FILE), file=sys.stderr)
        return 3
    print("wrote " + str(OUT_FILE) + ": " + str(len(JOKE)) + " code points")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
