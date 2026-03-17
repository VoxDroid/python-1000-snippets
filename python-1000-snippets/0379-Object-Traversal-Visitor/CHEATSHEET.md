# 0379-Object-Traversal-Visitor Cheatsheet

- Visitor separates operations from object structure.
- Elements implement `accept(visitor)` and call `visitor.visit(self)`.
- Use Visitor to add new operations without modifying element classes.
- Common in AST traversal, serialization, and reporting.
