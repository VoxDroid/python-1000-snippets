
# 0399-Automated-Database-Migration Cheatsheet

- Install SQLAlchemy: `pip install sqlalchemy`.
- Use `MetaData().create_all(engine)` to create missing tables.
- For simple migrations, use `ALTER TABLE` with SQLite.
- Use reflection (`MetaData().reflect`) to inspect existing schema.
