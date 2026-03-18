# 0415-GraphQL-Mutation-Design Cheatsheet

## Quick start
1. Install the dependency:
   ```bash
   pip install strawberry-graphql
   ```
2. Run a sample:
   ```bash
   python SAMPLES/sample1.py
   ```

## Key concepts
- **Mutation**: A GraphQL operation that modifies state and can return a payload.
- **Input types**: Use `@strawberry.input` to define structured mutation inputs.
- **Context**: Pass `context_value` into `schema.execute_sync` to share request-scoped data.

## Notes
- These samples execute mutations in-process (no HTTP server required).
- For a real API, integrate Strawberry with an ASGI framework (FastAPI, Starlette, etc.).
