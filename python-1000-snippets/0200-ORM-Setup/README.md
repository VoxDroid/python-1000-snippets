# ORM Setup

## Description
This snippet demonstrates setting up SQLAlchemy ORM with a SQLite database.

## Code
```python
# Note: Requires `sqlalchemy`. Install with `pip install sqlalchemy`
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///example.db")
Session = sessionmaker(bind=engine)
session = Session()
print("ORM session created")
session.close()
```

## Output
```
ORM session created
```

## Explanation
- **ORM Setup**: Configures SQLAlchemy with a SQLite database and creates a session factory.
- **Logic**: Uses `create_engine` for the database connection and `sessionmaker` for ORM sessions.
- **Complexity**: O(1) for setup.
- **Use Case**: Used as the foundation for database operations in applications.
- **Best Practice**: Close sessions; use connection pooling; configure engine for production.