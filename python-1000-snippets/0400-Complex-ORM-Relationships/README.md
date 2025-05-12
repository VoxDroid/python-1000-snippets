# Complex ORM Relationships

## Description
This snippet demonstrates a one-to-many relationship using `sqlalchemy`.

## Code
```python
# Note: Requires `sqlalchemy`. Install with `pip install sqlalchemy`
try:
    from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
    from sqlalchemy.orm import relationship, declarative_base
    Base = declarative_base()
    
    class Parent(Base):
        __tablename__ = "parent"
        id = Column(Integer, primary_key=True)
        children = relationship("Child")
    
    class Child(Base):
        __tablename__ = "child"
        id = Column(Integer, primary_key=True)
        parent_id = Column(Integer, ForeignKey("parent.id"))
    
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    print("Tables created")
except ImportError:
    print("Mock Output: Tables created")
```

## Output
```
Mock Output: Tables created
```
*(Real output with `sqlalchemy`: `Tables created`)*

## Explanation
- **Complex ORM Relationships**: Defines a one-to-many relationship.
- **Logic**: Uses `sqlalchemy` to create parent-child tables with a relationship.
- **Complexity**: O(1) for schema definition.
- **Use Case**: Used for relational data modeling in applications.
- **Best Practice**: Define clear relationships; optimize queries; test ORM setup.