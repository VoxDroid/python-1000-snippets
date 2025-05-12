# GraphQL Mutation Design

## Description
This snippet demonstrates a GraphQL mutation using `strawberry`.

## Code
```python
# Note: Requires `strawberry-graphql`. Install with `pip install strawberry-graphql`
try:
    import strawberry
    @strawberry.type
    class Mutation:
        @strawberry.mutation
        def create_item(self, name: str) -> str:
            return f"Created {name}"
    
    print("Mutation defined")
except ImportError:
    print("Mock Output: Mutation defined")
```

## Output
```
Mock Output: Mutation defined
```
*(Real output with `strawberry`: Configures GraphQL mutation)*

## Explanation
- **GraphQL Mutation Design**: Defines a mutation to create an item.
- **Logic**: Uses `strawberry` to define a mutation returning a string.
- **Complexity**: O(1) for definition.
- **Use Case**: Used for updating data in GraphQL APIs.
- **Best Practice**: Validate inputs; handle errors; document schema.