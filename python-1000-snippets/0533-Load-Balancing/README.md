# Load Balancing

## Description
This snippet demonstrates round-robin and weighted load balancing for request distribution.

## Code
- `SAMPLES/sample1.py`: basic round-robin across server pool.
- `SAMPLES/sample2.py`: weighted round-robin behavior.
- `SAMPLES/sample3.py`: save selected server history in `temp/0533_load_balancing.txt`.

## Output
- sample1: list of selected servers in rotation.
- sample2: weighted sequence.
- sample3: file written with selection history.

## Explanation
- **Load Balancing**: distributes requests across multiple servers.
- **Logic**: deterministic selection algorithm.
- **Complexity**: O(1) per lookup.
- **Use Case**: distributed service routing.
- **Best Practice**: include health checks, weighted policies, and failure handling.
