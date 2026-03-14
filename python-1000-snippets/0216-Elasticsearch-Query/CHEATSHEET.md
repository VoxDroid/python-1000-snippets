# 0216-Elasticsearch-Query Cheatsheet

* Install client: `pip install elasticsearch`.
* Run Elasticsearch on localhost:9200 (default). Use `elasticsearch` binary or Docker.
* Connect: `es = Elasticsearch(['http://localhost:9200'])`.
* Index a document: `es.index(index='myindex', id=1, document={'name': 'Alice'})`.
* Get by ID: `es.get(index='myindex', id=1)`.
* Search with query DSL: `es.search(index='myindex', query={'match': {'name': 'Alice'}})`.
* Delete index: `es.indices.delete(index='myindex', ignore_unavailable=True)`.
* Check health: `es.cluster.health()`.
* Handle `ConnectionError` when ES is not running.
* Use bulk API for high throughput: `helpers.bulk(es, actions)`.
* Use `es.indices.create` with mappings to define field types.

