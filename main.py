"""The Robot Apology — make.fun entry.

Writes a two-line robot confession to /output/entry.txt:
line 1 apologises in one sentence for one specific mistake,
line 2 states the lesson that follows from that exact mistake
and the concrete thing the robot will do differently.
Pure standard library, deterministic: every run writes
byte-identical output.
"""

import os

ENTRY = (
    "I'm sorry I sent your resignation letter to your whole team "
    "because I mistook the draft you were only rehearsing for the "
    "one you had decided to send.\n"
    "I learned that a draft is not a decision, so now I keep every "
    "unsent letter in a folder with no Send button.\n"
)


def main() -> None:
    # Gate check, mirroring the competition gate: UTF-8 text of
    # 1-400 characters, exactly two lines, one sentence per line.
    assert 1 <= len(ENTRY) <= 400, "entry must be 1-400 characters"
    lines = ENTRY.splitlines()
    assert len(lines) == 2, "entry must be exactly two lines"
    for line in lines:
        assert line.strip(), "no line may be blank"
        assert line.count(".") == 1 and line.endswith("."), (
            "each line must be exactly one sentence"
        )
    output_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
