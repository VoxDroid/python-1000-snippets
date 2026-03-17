
# sample2.py
# Add a new column to an existing table (SQLite supports limited ALTER TABLE).

try:
    from sqlalchemy import Column, Integer, MetaData, String, Table, create_engine, select, text
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
        # SQLite supports a limited ALTER TABLE statement.
        conn.execute(text("ALTER TABLE users ADD COLUMN email VARCHAR"))

        # Reflect updated schema and query.
        metadata_reflect = MetaData()
        metadata_reflect.reflect(bind=engine)
        users_reflected = metadata_reflect.tables["users"]

        result = conn.execute(select(users_reflected)).all()
        print("Rows after migration:", result)
