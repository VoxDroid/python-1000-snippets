
# sample1.py
# Create a table, insert a row, and query it.

try:
    from sqlalchemy import Column, Integer, MetaData, String, Table, create_engine, select
except ImportError:
    print("sqlalchemy not installed; install with `pip install sqlalchemy`")
else:
    engine = create_engine("sqlite:///:memory:")
    metadata = MetaData()
    users = Table(
        "users",
        metadata,
        Column("id", Integer, primary_key=True),
        Column("name", String, nullable=False),
    )
    metadata.create_all(engine)

    with engine.connect() as conn:
        conn.execute(users.insert().values(name="Alice"))
        result = conn.execute(select(users)).all()
        print("Rows:", result)
