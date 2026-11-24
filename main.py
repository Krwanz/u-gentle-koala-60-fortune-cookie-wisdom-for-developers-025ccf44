"""Fortune Cookie Wisdom for Developers — entry program.

Writes one original fortune-cookie line for a software developer to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
"""

import os

FORTUNE = (
    "A bug found in review is a gift; "
    "a bug found in production is the same gift, unwrapped by strangers."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    # Clear only the contents of the output dir, never the dir itself.
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isfile(path):
            os.remove(path)
    line = FORTUNE.strip()
    assert "\n" not in line, "fortune must be a single line"
    assert 1 <= len(line) <= 120, f"line is {len(line)} chars, must be 1-120"
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    # Read it back and confirm exactly what the gate will see.
    with open(target, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == line, "entry.txt does not match the fortune"
    print(f"wrote {len(written)} chars to {target}")


if __name__ == "__main__":
    main()
