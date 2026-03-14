# sample1.py
# Index and retrieve a document in Elasticsearch
from elasticsearch import Elasticsearch, ConnectionError

if __name__ == '__main__':
    es = Elasticsearch(['http://localhost:9200'])
    try:
        es.indices.create(index='python_snippets', ignore=400)
        es.index(index='python_snippets', id=1, document={'name': 'Alice'})
        doc = es.get(index='python_snippets', id=1)
        print('Found:', doc['_source']['name'])
    except ConnectionError as e:
        print('Elasticsearch not available:', e)

