# sample2.py
# Shallow vs deep copy demonstration

import copy


def main():
    original = [1, [2, 3]]
    shallow = copy.copy(original)
    deep = copy.deepcopy(original)

    shallow[1].append(4)
    print("original after shallow mutation:", original)
    print("deep after shallow mutation:", deep)


if __name__ == "__main__":
    main()
