import os

ENTRY = 'My agent drafts a plan, asks me to approve the plan, then asks the plan for permission to start.'
MAX_CHARS = 200  # the gate accepts 1..200 characters


def main():
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
    except OSError:
        path = "entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY.strip())


if __name__ == "__main__":
    main()
