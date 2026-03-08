# 0121-Pygame-Window Cheatsheet

- **Purpose**: create a basic Pygame window; uses `asyncio` for Pyodide/browser.
- **Headless**: sets `SDL_VIDEODRIVER=dummy` if not on Emscripten; runs for a few frames then exits.
- **Usage**: execute script directly (`python window.py`) after installing `pygame`.

```python
# run normally
python 0121-Pygame-Window/README.md
```

- To test in CI, rely on dummy driver; window won’t appear but code executes.
- For real applications, implement event handling and drawing logic in `update_loop`.

