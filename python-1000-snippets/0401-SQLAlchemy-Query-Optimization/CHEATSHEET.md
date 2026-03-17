# 0401-SQLAlchemy-Query-Optimization Cheatsheet

- Use `limit()` to avoid returning large datasets when you only need a subset.
- Add indexes (e.g., `Column(String, index=True)`) to speed up filtered queries.
- Use `joinedload()` or `selectinload()` to eager load relationships and reduce query count.
- Build queries with `select()` and use `.where()`, `.order_by()`, and `.limit()`.
- Use `session.execute(select(...))` for more control over results.
