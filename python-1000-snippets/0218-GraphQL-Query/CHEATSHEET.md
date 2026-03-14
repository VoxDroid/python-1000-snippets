# 0218-GraphQL-Query Cheatsheet

* Install client: `pip install gql requests`.
* Create a transport: `RequestsHTTPTransport(url='https://example.com/graphql')`.
* Use `Client(transport=transport, fetch_schema_from_transport=True)` to enable schema introspection.
* Define queries with `gql("""...""")`.
* Execute with `client.execute(query, variable_values={'id': 1})`.
* For mutations, send `mutation` operations similarly.
* Handle errors by catching `TransportQueryError` or `TransportServerError`.
* Use `asyncio` with `AIOHTTPTransport` for async queries.
* Respect rate limits and caching policies of GraphQL endpoints.
* Example query:
  ```python
  query = gql('''
  query ($id: Int) { Media(id: $id) { title { english } } }
  ''')
  ```

