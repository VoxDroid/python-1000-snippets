# sample2.py
# Iterator that returns file-like lines from a list (simulating streaming)

class LineStreamer:
    def __init__(self, lines):
        self._lines = lines
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._lines):
            raise StopIteration
        line = self._lines[self._index]
        self._index += 1
        return line


def main():
    streamer = LineStreamer(["first", "second", "third"])
    for line in streamer:
        print(line)


if __name__ == "__main__":
    main()
