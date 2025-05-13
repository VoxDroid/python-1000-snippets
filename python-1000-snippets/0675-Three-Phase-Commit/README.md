# Three-Phase Commit

## Description
This snippet demonstrates a three-phase commit (3PC) protocol for an e-commerce platform, enhancing 2PC with a pre-commit phase to reduce blocking.

## Code
```python
# Three-phase commit for order and inventory
try:
    from enum import Enum
    from typing import List

    # Commit phases
    class Phase(Enum):
        PREPARE = "prepare"
        PRE_COMMIT = "pre_commit"
        COMMIT = "commit"
        ABORT = "abort"

    # Simulated resource manager
    class ResourceManager:
        def __init__(self, name: str):
            self.name = name
            self.prepared = False
            self.pre_committed = False

        def prepare(self) -> bool:
            # Simulate preparation
            self.prepared = True
            return True

        def pre_commit(self) -> bool:
            # Simulate pre-commit
            if self.prepared:
                self.pre_committed = True
                return True
            return False

        def commit(self) -> bool:
            # Simulate commit
            return self.pre_committed

        def abort(self) -> bool:
            # Simulate rollback
            self.prepared = False
            self.pre_committed = False
            return True

    # Three-phase commit coordinator
    def three_phase_commit(order_id: str, resources: List[ResourceManager]) -> str:
        # Phase 1: Prepare
        for rm in resources:
            if not rm.prepare():
                for rm in resources:
                    rm.abort()
                return f"Transaction {order_id} aborted"
        # Phase 2: Pre-commit
        for rm in resources:
            if not rm.pre_commit():
                for rm in resources:
                    rm.abort()
                return f"Transaction {order_id} aborted in pre-commit"
        # Phase 3: Commit
        for rm in resources:
            if not rm.commit():
                return f"Transaction {order_id} failed during commit"
        return f"Transaction {order_id} committed"

    # Example usage
    order_rm = ResourceManager("order_db")
    inv_rm = ResourceManager("inventory_db")
    result = three_phase_commit("O001", [order_rm, inv_rm])
    print("Three-phase commit:", result)
except ImportError:
    print("Mock Output: Three-phase commit: Transaction O001 committed")
```

## Output
```
Mock Output: Three-phase commit: Transaction O001 committed
```
*(Real output: `Three-phase commit: Transaction O001 committed`)*

## Explanation
- **Purpose**: Three-phase commit reduces blocking in distributed transactions by adding a pre-commit phase, improving fault tolerance over 2PC.
- **Real-World Use Case**: In an e-commerce platform, 3PC ensures atomic updates to order and inventory databases, minimizing downtime during coordinator failures.
- **Code Breakdown**:
  - The `ResourceManager` class supports prepare, pre-commit, commit, and abort operations.
  - The `three_phase_commit` function coordinates three phases, aborting on any failure.
  - The output confirms the transaction outcome.
- **Challenges**: Increased complexity, handling timeouts, and ensuring recovery mechanisms.
- **Integration**: Works with Two-Phase Commit (Snippet 674) and Distributed Transaction (Snippet 673) for atomicity.
- **Complexity**: O(n) for n resource managers.
- **Best Practices**: Implement recovery logs, use timeouts, test failure scenarios, and monitor performance.