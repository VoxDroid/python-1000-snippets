# 0297-Game-Engine Cheatsheet

## Quick Start
- Run a sample:
  - `python python-1000-snippets/0297-Game-Engine/SAMPLES/sample1.py`
  - `python python-1000-snippets/0297-Game-Engine/SAMPLES/sample2.py`
  - `python python-1000-snippets/0297-Game-Engine/SAMPLES/sample3.py`

## Concepts
- **Game Loop**: Repeatedly update state and render frames at a target rate.
- **Entities**: Objects with position and behavior updated each frame.
- **Collision**: Simple boundary checks and response (e.g., reflection) keep entities in the world.
- **Tile Maps**: Grid-based world representation for movement and collision.

## Tips
- For interactive games, use a library like Pygame or PySDL2 for rendering and input.
- Decouple game logic (update) from rendering for easier testing.
- Use fixed timestep updates for deterministic behavior.
