# 0123-Pygame-Animation Cheatsheet

- **Purpose**: animate shapes in a Pygame window; uses dummy driver for headless runs.
- **Core idea**: update object positions each frame and call `pygame.display.flip()`.
- **Headless**: environment variable `SDL_VIDEODRIVER=dummy` and limit frames.

```python
# execute as in README
python 0123-Pygame-Animation/README.md
```

- To adapt: replace circle with sprites or images; update positions using velocity.
- Use `clock.tick(FPS)` if you prefer a blocking loop over asyncio.

