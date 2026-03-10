# 0171-Facade-Pattern Cheatsheet

- **Purpose**: provide a simplified interface to a set of interfaces in a subsystem.
- **Structure**: one Facade class holds references to subsystem classes and implements easy-to-use methods.
- **Benefits**: reduces coupling between client and subsystem, improves readability.
- **Common scenario**: system startup/shutdown procedures, API adapters.
- **Tip**: facade can be layered; use when subsystems are complex or frequently used together.

```bash
python3 SAMPLES/sample1.py
python3 SAMPLES/sample2.py
python3 SAMPLES/sample3.py
```
