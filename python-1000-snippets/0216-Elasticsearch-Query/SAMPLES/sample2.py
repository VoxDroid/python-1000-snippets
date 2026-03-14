# sample2.py
# Search for documents using query DSL
from elasticsearch import Elasticsearch, ConnectionError

if __name__ == '__main__':
    es = Elasticsearch(['http://localhost:9200'])
    try:
        res = es.search(index='python_snippets', query={'match_all': {}})
        hits = res.get('hits', {}).get('hits', [])
        print('Hit count:', res.get('hits', {}).get('total', {}).get('value'))
        for hit in hits:
            print(' -', hit['_source'])
    except ConnectionError as e:
        print('Elasticsearch not available:', e)

