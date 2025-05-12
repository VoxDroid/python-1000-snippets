# SQLAlchemy Query Optimization

## Description
This snippet demonstrates optimized querying with `sqlalchemy`.

## Code
```python
# Note: Requires `sqlalchemy`. Install with `pip install sqlalchemy`
try:
    from sqlalchemy import create_engine, Column, Integer, select
    from sqlalchemy.orm import declarative_base, Session
    Base = declarative_base()
    
    class Item(Base):
        __tablename__ = "item"
        id = Column(Integer, primary_key=True)
    
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        stmt = select(Item).limit(10)
        print("Query prepared")
except ImportError:
    print("Mock Output: Query prepared")
```

## Output
```
Mock Output: Query prepared
```
*(Real output with `sqlalchemy`: `Query prepared`)*

## Explanation
- **SQLAlchemy Query Optimization**: Prepares an optimized query with a limit.
- **Logic**: Uses `select` and `limit` to constrain query results.
- **Complexity**: O(1) for query preparation.
- **Use Case**: Used for efficient database querying in applications.
- **Best Practice**: Use indexing; limit results; profile queries.