# 0364-Event-Driven-Observer Cheatsheet

- Observers register with a subject and get notified of events.
- Keep observer interface simple (e.g., `update(event)`).
- Use weak references for long-lived subjects to avoid memory leaks.
- Manage registration/unregistration explicitly.
