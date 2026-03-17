# sample3.py
# Nested file context managers for reading and writing without leaking handles

import os


def ensure_temp_dir():
    path = os.path.join(os.getcwd(), "temp")
    os.makedirs(path, exist_ok=True)
    return path


def main():
    temp_dir = ensure_temp_dir()
    in_path = os.path.join(temp_dir, "input.txt")
    out_path = os.path.join(temp_dir, "output.txt")

    with open(in_path, "w") as f:
        f.write("hello\nworld\n")

    with open(in_path, "r") as reader:
        with open(out_path, "w") as writer:
            for line in reader:
                writer.write(line.upper())

    print("Wrote:", out_path)


if __name__ == "__main__":
    main()
