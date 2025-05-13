# Two-Phase Commit

## Description
This snippet demonstrates a two-phase commit (2PC) protocol for an e-commerce platform, coordinating order and payment updates across distributed services.

## Code
```python
# Two-phase commit for order and payment
try:
    from enum import Enum
    from typing import List

    # Commit phases
    class Phase(Enum):
        PREPARE = "prepare"
        COMMIT = "commit"
        ABORT = "abort"

    # Simulated resource manager
    class ResourceManager:
        def __init__(self, name: str):
            self.name = name
            self.prepared = False

        def prepare(self) -> bool:
            # Simulate preparation (e.g., lock resources)
            self.prepared = True
            return True

        def commit(self) -> bool:
            # Simulate commit
            return self.prepared

        def abort(self) -> bool:
            # Simulate rollback
            self.prepared = False
            return True

    # Two-phase commit coordinator
    def two_phase_commit(order_id: str, resources: List[ResourceManager]) -> str:
        # Phase 1: Prepare
        for rm in resources:
            if not rm.prepare():
                for rm in resources:
                    rm.abort()
                return f"Transaction {order_id} aborted"
        # Phase 2: Commit
        for rm in resources:
            if not rm.commit():
                return f"Transaction {order_id} failed during commit"
        return f"Transaction {order_id} committed"

    # Example usage
    order_rm = ResourceManager("order_db")
    payment_rm = ResourceManager("payment_db")
    result = two_phase_commit("O001", [order_rm, payment_rm])
    print("Two-phase commit:", result)
except ImportError:
    print("Mock Output: Two-phase commit: Transaction O001 committed")
```

## Output
```
Mock Output: Two-phase commit: Transaction O001 committed
```
*(Real output: `Two-phase commit: Transaction O001 committed`)*

## Explanation
- **Purpose**: Two-phase commit ensures all participants in a distributed transaction agree to commit or abort, maintaining atomicity.
- **Real-World Use Case**: In an e-commerce platform, 2PC ensures that an order is recorded and payment is processed atomically across services.
- **Code Breakdown**:
  - The `ResourceManager` class simulates a database with prepare, commit, and abort operations.
  - The `two_phase_commit` function coordinates the prepare and commit phases, aborting on any failure.
  - The output confirms the transaction outcome.
- **Challenges**: Handling coordinator failures, managing blocking, and ensuring scalability.
- **Integration**: Works with Distributed Transaction (Snippet 673) and Three-Phase Commit (Snippet 675) for atomicity.
- **Complexity**: O(n) for n resource managers.
- **Best Practices**: Implement recovery mechanisms, log phases, test failures, and use timeouts.