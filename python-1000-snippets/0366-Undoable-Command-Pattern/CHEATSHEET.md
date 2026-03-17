# 0366-Undoable-Command-Pattern Cheatsheet

- Implement `execute()` and `undo()` for each command.
- Keep command state minimal but sufficient for undo.
- Use a stack to track executed commands for undo/redo.
- Ensure undo is called in the reverse order of execution.
