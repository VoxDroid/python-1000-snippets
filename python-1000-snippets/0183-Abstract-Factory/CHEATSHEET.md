# 0183-Abstract-Factory Cheatsheet

- **Purpose**: create families of related or dependent objects without specifying their concrete classes.
- **Components**: abstract factory interface with creation methods, concrete factories, abstract product interfaces, and concrete products.
- **Usage**: client is given a factory instance and calls its methods; factory handles product instantiation.
- **Variants**: can combine with Builder or Prototype for complex products.
- **Tip**: switching families is as simple as passing a different factory object.

```bash
python3 SAMPLES/sample1.py
python3 SAMPLES/sample2.py
python3 SAMPLES/sample3.py
```
