#!/usr/bin/env python3
"""Long Roast: Lawmakers — Round 2 entry.

Writes one satirical sentence to /output/entry.txt.
Stdlib only. Deterministic: the same line on every run.
"""
import os

MIN_CHARS = 1
MAX_CHARS = 320

LINE = (
    "The AI bill requiring every government file to be a PDF was itself "
    "filed as a Word file, so the first crime under the new law is the "
    "new law."
)


def main() -> None:
    text = LINE
    # Gate: /output/entry.txt is UTF-8 text of 1 to 320 characters.
    assert MIN_CHARS <= len(text) <= MAX_CHARS, (
        f"entry length {len(text)} outside {MIN_CHARS}-{MAX_CHARS}"
    )
    assert text.strip(), "entry is only whitespace"
    # The judge wants one satirical sentence: exactly one terminal period.
    assert text.count(".") == 1 and text.endswith("."), (
        "entry must be a single sentence"
    )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Byte-verify what was written.
    with open("/output/entry.txt", "rb") as f:
        raw = f.read()
    assert raw.decode("utf-8") == text, "written bytes do not match entry"
    assert not raw.endswith(b"\n"), "no trailing newline"
    print(f"entry: {len(text)} chars, {len(raw)} bytes")


if __name__ == "__main__":
    main()
