# Lamport Timestamp

## Description
This snippet demonstrates Lamport timestamps for ordering events (e.g., inventory updates) in an e-commerce distributed system, ensuring a total order of operations.

## Code
```python
# Lamport timestamp for event ordering
try:
    # Lamport timestamp implementation
    class LamportClock:
        def __init__(self, node_id: str):
            # Initialize clock with node ID and timestamp
            self.node_id = node_id
            self.timestamp = 0

        def increment(self) -> None:
            # Increment timestamp for local event
            self.timestamp += 1

        def update(self, received_ts: int) -> None:
            # Update timestamp with max of local and received
            self.timestamp = max(self.timestamp, received_ts) + 1

        def get_timestamp(self) -> int:
            return self.timestamp

    # Simulate event processing
    def process_inventory_event(node_id: str, event: str, received_clock: 'LamportClock' = None) -> LamportClock:
        # Create or update Lamport clock
        clock = LamportClock(node_id)
        clock.increment()
        if received_clock:
            clock.update(received_clock.get_timestamp())
        return clock

    # Example usage: Two nodes updating inventory
    node1_clock = process_inventory_event("node1", "Stock updated for P001")
    node2_clock = process_inventory_event("node2", "Stock reserved for P001", node1_clock)
    print("Lamport timestamp:", node2_clock.get_timestamp())
except ImportError:
    print("Mock Output: Lamport timestamp: 2")
```

## Output
```
Mock Output: Lamport timestamp: 2
```
*(Real output: `Lamport timestamp: 2`)*

## Explanation
- **Purpose**: Lamport timestamps provide a total ordering of events in distributed systems, ensuring consistent event sequences.
- **Real-World Use Case**: In an e-commerce platform, Lamport timestamps order inventory updates (e.g., stock reduction, reservation) across warehouses, preventing overselling.
- **Code Breakdown**:
  - The `LamportClock` class tracks a node’s timestamp.
  - The `increment` method advances the timestamp for local events.
  - The `update` method synchronizes with a received timestamp, taking the maximum and incrementing.
  - The `process_inventory_event` function simulates an event with timestamp updates.
- **Challenges**: Handling high event rates, resolving ties, and integrating with other ordering mechanisms.
- **Integration**: Works with Vector Clock Synchronization (Snippet 671) and Distributed Transaction (Snippet 673) for event ordering.
- **Complexity**: O(1) for timestamp operations.
- **Best Practices**: Combine with node IDs for tie-breaking, log timestamps, and test under network delays.