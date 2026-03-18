# sample1.py
# Demonstrates defining and executing a GraphQL mutation using Strawberry.

import strawberry


@strawberry.type
class Item:
    id: int
    name: str


@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_item(self, name: str) -> Item:
        # In a real app, persist the item to a database or service.
        return Item(id=1, name=name)


@strawberry.type
class Query:
    ping: str = "pong"

schema = strawberry.Schema(query=Query, mutation=Mutation)


def main() -> None:
    query = """
    mutation {
      createItem(name: \"Widget\") {
        id
        name
      }
    }
    """

    result = schema.execute_sync(query)
    if result.errors:
        raise SystemExit(f"GraphQL errors: {result.errors}")

    print("Mutation result:", result.data)


if __name__ == "__main__":
    main()
