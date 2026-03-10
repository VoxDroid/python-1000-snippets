# 0177-Memento-Pattern Cheatsheet

- **Purpose**: capture and externalize an object’s internal state so it can be restored later without violating encapsulation.
- **Roles**: `Originator` creates mementos and restores state; `Memento` holds the state; `Caretaker` keeps mementos but does not inspect them.
- **Usage**: useful for undo/redo, checkpoints, or rollbacks.
- **Immutability**: memento should not allow state changes from outside originator.

```bash
python3 SAMPLES/sample1.py
python3 SAMPLES/sample2.py
python3 SAMPLES/sample3.py
```
