# Database Migration

## Description
This snippet demonstrates a simple database migration using `alembic` with SQLite.

## Code
```python
# Note: Requires `alembic` and `sqlalchemy`. Install with `pip install alembic sqlalchemy`
# alembic.ini and migration scripts are typically generated with `alembic init`
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)

# Mock migration script (env.py or revision file)
engine = create_engine("sqlite:///mydb.db")
Base.metadata.create_all(engine)
print("Table created (mock migration)")
```

## Output
```
Table created (mock migration)
```

## Explanation
- **Database Migration**: Simulates an `alembic` migration by creating a `users` table with SQLAlchemy.
- **Logic**: Defines a `User` model and creates the table in SQLite.
- **Complexity**: O(1) for table creation.
- **Use Case**: Used to manage database schema changes in applications.
- **Best Practice**: Use `alembic` for real migrations; version control migration scripts; test migrations.