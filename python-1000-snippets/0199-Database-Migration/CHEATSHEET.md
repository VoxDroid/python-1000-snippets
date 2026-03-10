# 0199-Database-Migration Cheatsheet

* Use Alembic with SQLAlchemy for schema migrations.
* Commands: `alembic init`, `alembic revision --autogenerate -m "msg"`, `alembic upgrade head`.
* Migration scripts import SQLAlchemy models and use `op` to alter tables.
* Always version control `migrations/` directory.
* Test migrations on staging database.

