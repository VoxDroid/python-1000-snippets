# sample2.py
# Demonstrates a GraphQL mutation that uses an input object and variables.

import strawberry


@strawberry.input
class CreateItemInput:
    name: str
    quantity: int = 1


@strawberry.type
class Item:
    id: int
    name: str
    quantity: int


@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_item(self, input: CreateItemInput) -> Item:
        # In a real app, you might persist the created item.
        return Item(id=1, name=input.name, quantity=input.quantity)


@strawberry.type
class Query:
    ping: str = "pong"

schema = strawberry.Schema(query=Query, mutation=Mutation)


def main() -> None:
    query = """
    mutation CreateItem($input: CreateItemInput!) {
      createItem(input: $input) {
        id
        name
        quantity
      }
    }
    """

    variables = {"input": {"name": "Gizmo", "quantity": 5}}

    result = schema.execute_sync(query, variable_values=variables)
    if result.errors:
        raise SystemExit(f"GraphQL errors: {result.errors}")

    print("Mutation result:", result.data)


if __name__ == "__main__":
    main()
