import os

TEXT = (
    "When the client says 'make the logo bigger' for the third time, "
    "don't nod \u2014 ask what they're actually afraid of.\n"
    "That question turned a fussy client into a three-year retainer, "
    "and I never touched a logo again without asking why first."
)


def main():
    assert 1 <= len(TEXT) <= 280 and TEXT.strip()
    assert TEXT.count("\n") == 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
