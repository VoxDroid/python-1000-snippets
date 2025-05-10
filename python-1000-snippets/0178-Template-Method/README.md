# Template Method

## Description
This snippet implements the Template Method pattern to define an algorithm’s skeleton with customizable steps.

## Code
```python
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

processor = CSVProcessor()
processor.process()
```

## Output
```
Loading data
Transforming CSV data
Saving data
```

## Explanation
- **Template Method**: `DataProcessor.process` defines the algorithm; subclasses override `transform_data`.
- **Logic**: Ensures a fixed sequence while allowing customization.
- **Complexity**: O(1) for the process call.
- **Use Case**: Used in frameworks or workflows with fixed steps.
- **Best Practice**: Make template method final; document customizable methods.