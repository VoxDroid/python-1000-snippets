# sample3.py
# Demonstrate introspection query (schema inspection)
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

if __name__ == '__main__':
    transport = RequestsHTTPTransport(url='https://graphql.anilist.co', verify=True, retries=3)
    # Schema introspection can fail on some endpoints; disable schema fetching
    client = Client(transport=transport, fetch_schema_from_transport=False)

    # Instead of introspection, just query some known fields
    query = gql('''
        query {
            Page(perPage: 1) {
                media {
                    title { english }
                }
            }
        }
    ''')
    result = client.execute(query)
    media = result.get('Page', {}).get('media', [])
    print('First title:', media[0]['title']['english'] if media else None)

