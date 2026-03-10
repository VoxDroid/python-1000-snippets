# sample1.py
# data processor from README

class DataProcessor:
    def process(self):
        self.load_data()
        self.transform_data()
        self.save_data()
    def load_data(self):
        print("Loading data")
    def transform_data(self):
        pass
    def save_data(self):
        print("Saving data")

class CSVProcessor(DataProcessor):
    def transform_data(self):
        print("Transforming CSV data")

if __name__ == '__main__':
    processor = CSVProcessor()
    processor.process()
