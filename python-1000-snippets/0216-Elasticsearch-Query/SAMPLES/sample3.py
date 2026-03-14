# sample3.py
# Demonstrate deleting an index and handling missing index
from elasticsearch import Elasticsearch, NotFoundError, ConnectionError

if __name__ == '__main__':
    es = Elasticsearch(['http://localhost:9200'])
    try:
        es.indices.delete(index='python_snippets', ignore=[400, 404])
        print('Deleted index if existed')
    except ConnectionError as e:
        print('Elasticsearch not available:', e)

