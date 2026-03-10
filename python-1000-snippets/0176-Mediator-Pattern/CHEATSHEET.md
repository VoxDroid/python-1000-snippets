# 0176-Mediator-Pattern Cheatsheet

- **Purpose**: centralize complex interactions between components by having them communicate via a mediator rather than directly.
- **Components**: `Mediator` class with `register`, `notify` methods; participant objects maintain reference to mediator.
- **Usage**: participants call `mediator.notify(self, msg)`; mediator decides who to notify.
- **Variants**: chat room, dialog boxes, aircraft communication, event buses.
- **Tip**: mediator can also maintain state or translate messages.

```bash
python3 SAMPLES/sample1.py
python3 SAMPLES/sample2.py
python3 SAMPLES/sample3.py
```
