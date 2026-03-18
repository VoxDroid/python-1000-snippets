# 0412-Cassandra-Data-Modeling Cheatsheet

## Quick start
1. Install dependencies:
   ```bash
   pip install cassandra-driver pyyaml
   ```
2. Run a sample:
   ```bash
   python SAMPLES/sample1.py
   ```

## Key concepts
- **Keyspace**: similar to a database namespace; defined with a replication strategy.
- **Table (Column Family)**: defined with a primary key; choose partition keys wisely.
- **CQL**: Cassandra Query Language, similar to SQL for write/reads.

## Tips
- Use `SimpleStrategy` replication for single-node local testing.
- In production, use `NetworkTopologyStrategy` and multiple nodes.
- Data modeling in Cassandra focuses on query patterns; design tables for reads.

