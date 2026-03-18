# GraphQL Mutation Design

## Description
Demonstrates how to define and execute GraphQL mutations using `strawberry`.

## Requirements
- Python 3.8+
- `strawberry-graphql` Python package (`pip install strawberry-graphql`)

## Code
```python
import strawberry


@strawberry.type
class Item:
    id: int
    name: str


@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_item(self, name: str) -> Item:
        # In a real application, persist the item to a database.
        return Item(id=1, name=name)


@strawberry.type
class Query:
    ping: str = "pong"


schema = strawberry.Schema(query=Query, mutation=Mutation)


query = """
mutation {
  createItem(name: \"Widget\") {
    id
    name
  }
}
"""

result = schema.execute_sync(query)
print(result.data)
```

## Output
```
{'createItem': {'id': 1, 'name': 'Widget'}}
```

## Explanation
- **GraphQL Mutation**: Used to modify server-side data.
- **Strawberry**: A Python GraphQL library that uses type annotations.
- **Logic**: Define a mutation and execute it via the schema.
- **Use Case**: APIs that create or update resources (e.g., create a user or post a comment).
- **Best Practice**: Validate inputs, handle errors, and avoid exposing sensitive data.
