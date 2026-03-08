# 0164-Observer-Pattern Cheatsheet

- **Purpose**: allow objects (observers) to be notified when another object (subject) changes state.
- **Structure**: Subject keeps list of observers; observers implement an `update` (or similarly named) method.
- **Attach/Detach**: subject has methods to add/remove observers to support dynamic subscriptions.
- **Notification**: subject loops through observers and calls their update, optionally with data.
- **Use cases**: event listeners, MVC frameworks, pub/sub systems.
- **Variation**: use callback functions instead of observer objects.

```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```
