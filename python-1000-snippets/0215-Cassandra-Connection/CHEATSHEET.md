# 0215-Cassandra-Connection Cheatsheet

* Install driver: `pip install cassandra-driver`.
* Start Cassandra (default on localhost:9042). Use `cassandra` or `systemctl start cassandra` if installed.
* Connect: `cluster = Cluster(['127.0.0.1']); session = cluster.connect()`.
* Create keyspace: `session.execute("CREATE KEYSPACE IF NOT EXISTS ks WITH replication = {'class':'SimpleStrategy','replication_factor':1}")`.
* Use keyspace: `session.set_keyspace('ks')`.
* Create table with `CREATE TABLE IF NOT EXISTS`.
* Insert: `session.execute(query, (id, name))`.
* Query: `rows = session.execute('SELECT name FROM users WHERE id=%s', (1,))`.
* Use prepared statements for performance: `ps = session.prepare(query)`.
* Handle `NoHostAvailable` for connection failures.
* Close connection: `cluster.shutdown()`.
* Use consistent data modeling and avoid joins; design around query patterns.

