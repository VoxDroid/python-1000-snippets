# sample3.py
# Demonstrates using GraphQL context values inside a mutation resolver.

import strawberry


@strawberry.type
class Mutation:
    @strawberry.mutation
    def echo_with_user(self, info: strawberry.types.Info, message: str) -> str:
        user = info.context.get("user", "anonymous")
        return f"{user} says: {message}"


@strawberry.type
class Query:
    ping: str = "pong"

schema = strawberry.Schema(query=Query, mutation=Mutation)


def main() -> None:
    query = """
    mutation Echo($message: String!) {
      echoWithUser(message: $message)
    }
    """

    variables = {"message": "Hello GraphQL"}

    result = schema.execute_sync(
        query,
        variable_values=variables,
        context_value={"user": "alice"},
    )
    if result.errors:
        raise SystemExit(f"GraphQL errors: {result.errors}")

    print("Mutation result:", result.data)


if __name__ == "__main__":
    main()
