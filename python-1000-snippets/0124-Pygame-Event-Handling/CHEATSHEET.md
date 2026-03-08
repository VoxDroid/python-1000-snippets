# 0124-Pygame-Event-Handling Cheatsheet

- **Purpose**: demonstrate handling events (mouse clicks) in Pygame, with headless fallback.
- **Headless**: dummy video driver; simulated `MOUSEBUTTONDOWN` event posted automatically.
- **Usage**: run script normally after installing pygame; window will briefly flash white then random color.

```python
# just execute the README example
python 0124-Pygame-Event-Handling/README.md
```

- Extend to respond to `KEYDOWN`, `MOUSEMOTION`, etc.
- Use `pygame.event.post` to inject synthetic events for testing.

