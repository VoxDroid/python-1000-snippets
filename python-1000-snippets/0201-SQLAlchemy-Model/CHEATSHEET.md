# 0201-SQLAlchemy-Model Cheatsheet

* Define models by subclassing `Base = declarative_base()`.
* Fields use `Column` with types (`Integer`, `String`, etc.) and options (`primary_key=True`, `nullable=False`).
* `session.add()` and `session.add_all()` insert objects.
* `session.commit()` persists changes; `session.rollback()` to undo.
* Query with `session.query(Model)`; filter using `.filter()`, `.filter_by()`, or SQL expressions.
* Update by modifying object attributes then `session.commit()`.
* Delete with `session.delete(obj)` then commit.
* Use `.first()`, `.all()`, `.one()` for results; handle `NoResultFound` and `MultipleResultsFound`.
* To create tables: `Base.metadata.create_all(engine)`.
* Common patterns: use context manager (`with Session() as session:`) in SQLAlchemy 2.0+.
* For raw SQL use `session.execute(text("SELECT ..."))` and import `from sqlalchemy import text`.
* Productivity: enable `echo=True` on engine to log SQL; use Alembic for migrations.
* Example:
  ```python
  engine = create_engine('sqlite:///app.db', echo=True)
  Session = sessionmaker(bind=engine)
  with Session() as session:
      user = User(name='X')
      session.add(user)
      session.commit()
  ```
