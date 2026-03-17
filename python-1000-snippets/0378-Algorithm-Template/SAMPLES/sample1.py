# sample1.py
# Template method organizing a data processing workflow

class DataProcessor:
    def process(self, data):
        data = self.load(data)
        data = self.transform(data)
        return self.save(data)

    def load(self, data):
        return data

    def transform(self, data):
        raise NotImplementedError

    def save(self, data):
        return data


class UppercaseProcessor(DataProcessor):
    def transform(self, data):
        return [item.upper() for item in data]


def main():
    processor = UppercaseProcessor()
    result = processor.process(["a", "b", "c"])
    print(result)


if __name__ == "__main__":
    main()
