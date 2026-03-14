# sample1.py
# Execute a GraphQL query against a public GraphQL endpoint
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

if __name__ == '__main__':
    transport = RequestsHTTPTransport(url='https://graphql.anilist.co', verify=True, retries=3)
    # Avoid schema introspection issues by disabling schema fetching
    client = Client(transport=transport, fetch_schema_from_transport=False)

    query = gql('''
        query ($id: Int) {
            Media(id: $id) {
                title {
                    english
                }
            }
        }
    ''')

    result = client.execute(query, variable_values={'id': 1})
    print('Title:', result['Media']['title']['english'])

