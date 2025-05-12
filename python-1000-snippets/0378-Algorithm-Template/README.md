# Algorithm Template

## Description
This snippet demonstrates the template method pattern for algorithms.

## Code
```python
class Algorithm:
    def template_method(self):
        self.step1()
        self.step2()
    
    def step1(self):
        pass
    
    def step2(self):
        pass

class ConcreteAlgorithm(Algorithm):
    def step1(self):
        print("Step 1")
    
    def step2(self):
        print("Step 2")

algo = ConcreteAlgorithm()
algo.template_method()
```

## Output
```
Step 1
Step 2
```

## Explanation
- **Algorithm Template**: Defines a skeleton for an algorithm with customizable steps.
- **Logic**: `template_method` orchestrates steps implemented by subclasses.
- **Complexity**: O(1) per call (step complexity varies).
- **Use Case**: Used for workflows or processing pipelines.
- **Best Practice**: Define clear steps; ensure flexibility; document template.