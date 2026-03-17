
# sample3.py
# Use SQLAlchemy reflection to inspect the current schema.

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

    # Reflect existing schema into a new MetaData object.
    reflected = MetaData()
    reflected.reflect(bind=engine)
    print("Reflected tables:", list(reflected.tables.keys()))
    print("Columns for 'users':", [c.name for c in reflected.tables["users"].columns])
