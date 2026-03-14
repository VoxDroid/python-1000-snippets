# sample2.py
# Show how to query for multiple items and print them
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

if __name__ == '__main__':
    transport = RequestsHTTPTransport(url='https://graphql.anilist.co', verify=True, retries=3)
    client = Client(transport=transport, fetch_schema_from_transport=False)

    query = gql('''
        query {
            Page(perPage: 2) {
                media(type: ANIME, sort: POPULARITY_DESC) {
                    title {
                        english
                    }
                }
            }
        }
    ''')

    result = client.execute(query)
    titles = [m['title']['english'] for m in result['Page']['media'] if m['title']['english']]
    print('Top titles:', titles)

