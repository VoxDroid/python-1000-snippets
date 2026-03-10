# 0178-Template-Method Cheatsheet

- **Purpose**: define the skeleton of an algorithm in a base class, deferring exact steps to subclasses.
- **Structure**: Template method (often final) calls abstract or hook methods implemented by subclasses.
- **Customization**: override some of the primitive operations; optional hooks can do nothing by default.
- **Uses**: workflows, frameworks, rendering pipelines, data processing.
- **Tip**: mark template method as `final` or document that it should not be overridden.

```bash
python3 SAMPLES/sample1.py
python3 SAMPLES/sample2.py
python3 SAMPLES/sample3.py
```
