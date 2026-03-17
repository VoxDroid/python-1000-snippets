# 0400-Complex-ORM-Relationships Cheatsheet

- Use SQLAlchemy ORM classes and relationships (`relationship`, `ForeignKey`) to model related objects.
- One-to-many: `relationship("Child", back_populates="parent")` + `ForeignKey("parent.id")`.
- Many-to-many: use an association table with `Table(...)` and `secondary=`.
- Eager loading: `joinedload()` or `selectinload()` reduces round trips.
- Use an in-memory SQLite engine for small demos: `create_engine("sqlite:///:memory:")`.
- Example install: `python -m pip install sqlalchemy`.
