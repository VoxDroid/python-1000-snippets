# GraphQL Query

## Description
This snippet demonstrates executing a GraphQL query using `gql`.

## Code
```python
# Note: Requires `gql`. Install with `pip install gql`
try:
    from gql import gql, Client
    from gql.transport.requests import RequestsHTTPTransport
    transport = RequestsHTTPTransport(url="https://graphql.anilist.co")
    client = Client(transport=transport)
    query = gql("""
        query {
            Media(id: 1) {
                title {
                    english
                }
            }
        }
    """)
    result = client.execute(query)
    print("Title:", result["Media"]["title"]["english"])
except ImportError:
    print("Mock Output: Title: Cowboy Bebop")
```

## Output
```
Mock Output: Title: Cowboy Bebop
```
*(Real output with `gql`: `Title: Cowboy Bebop`)*

## Explanation
- **GraphQL Query**: Executes a query against a public GraphQL API using `gql`.
- **Logic**: Queries the `Media` type for a title by ID.
- **Complexity**: O(1) for query execution (network latency varies).
- **Use Case**: Used for flexible data fetching in modern APIs.
- **Best Practice**: Validate query syntax; handle rate limits; secure API keys.