# 0200-ORM-Setup Cheatsheet

* **create_engine**: accepts a URL (`sqlite:///file.db`, `postgresql://user:pass@host/db`).
* **sessionmaker**: factory bound to engine; call to get `Session` instance.
* **Scoped sessions**: use `from sqlalchemy.orm import scoped_session` for thread-local sessions.
* Always **close** or **rollback** sessions to avoid leaks: `session.close()` or `session.rollback()`.
* **Commit/flush**: changes only persist after `session.commit()`; use `session.flush()` to send SQL without committing.
* **Metadata**: `Base.metadata.create_all(engine)` creates tables defined by declarative models.
* **Engine options**: configure `echo=True` for SQL logging, `pool_size`, `future=True` for 2.0 style.
* **Error handling**: catch `sqlalchemy.exc.SQLAlchemyError` for generic DB errors.
* **Use migrations** (e.g., Alembic) in production; do not call `create_all` on every startup.
* **Example workflow**:
  ```python
  engine = create_engine('sqlite:///app.db')
  Session = sessionmaker(bind=engine)
  session = Session()
  # use session
  session.close()
  ```
