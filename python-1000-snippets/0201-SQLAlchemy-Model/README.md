# SQLAlchemy Model

## Description
This snippet demonstrates defining and using a SQLAlchemy model to interact with a database.

## Code
```python
# Note: Requires `sqlalchemy`. Install with `pip install sqlalchemy`
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)

engine = create_engine("sqlite:///example.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
session.add(User(name="Alice"))
session.commit()
user = session.query(User).first()
print("User:", user.name)
session.close()
```

## Output
```
User: Alice
```

## Explanation
- **SQLAlchemy Model**: Defines a `User` model and performs CRUD operations.
- **Logic**: Creates a table, adds a user, and queries the first user.
- **Complexity**: O(1) for single-row operations.
- **Use Case**: Used for database interactions in web or data applications.
- **Best Practice**: Commit transactions; handle session lifecycle; index frequently queried columns.