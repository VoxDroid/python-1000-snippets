# Constraint Satisfaction

## Description
This snippet implements a CSP solver for a university, scheduling exams to avoid student conflicts.

## Code
```python
# Constraint Satisfaction: Exam scheduling
# Note: Requires `numpy`. Install with `pip install numpy`
try:
    import numpy as np

    # CSP model
    class ExamScheduler:
        def __init__(self, n_exams: int, n_slots: int, conflicts: np.ndarray):
            # Initialize exams, time slots, and student conflict matrix
            self.n_exams = n_exams
            self.n_slots = n_slots
            self.conflicts = conflicts
            self.schedule = np.random.randint(0, n_slots, n_exams)

        def is_valid(self, exam: int, slot: int, schedule: np.ndarray) -> bool:
            # Check if assigning exam to slot violates conflicts
            for other_exam in range(self.n_exams):
                if self.conflicts[exam, other_exam] and schedule[other_exam] == slot:
                    return False
            return True

        def solve(self, max_attempts: int) -> np.ndarray:
            # Backtracking search
            for _ in range(max_attempts):
                schedule = np.full(self.n_exams, -1)
                if self.backtrack(schedule, 0):
                    return schedule
            return None

        def backtrack(self, schedule: np.ndarray, exam: int) -> bool:
            # Recursive backtracking
            if exam == self.n_exams:
                return True
            for slot in range(self.n_slots):
                if self.is_valid(exam, slot, schedule):
                    schedule[exam] = slot
                    if self.backtrack(schedule, exam + 1):
                        return True
                    schedule[exam] = -1
            return False

    # Run CSP simulation
    def run_exam_scheduling(n_exams: int, n_slots: int, max_attempts: int) -> dict:
        # Schedule exams
        conflicts = np.random.choice([0, 1], (n_exams, n_exams), p=[0.8, 0.2])
        conflicts = np.triu(conflicts, 1) + np.triu(conflicts, 1).T
        np.fill_diagonal(conflicts, 0)
        scheduler = ExamScheduler(n_exams, n_slots, conflicts)
        schedule = scheduler.solve(max_attempts)
        return {'schedule': schedule}

    # Example usage
    result = run_exam_scheduling(n_exams=5, n_slots=3, max_attempts=10)
    print("Constraint satisfaction result:", result['schedule'])  # Exam schedule
except ImportError:
    print("Mock Output: Constraint satisfaction result: [0 1 2 0 1]")
```

## Output
```
Mock Output: Constraint satisfaction result: [0 1 2 0 1]
```
*(Real output with `numpy`: `Constraint satisfaction result: <exam schedule, e.g., [0 1 2 0 1]>`)*

## Explanation
- **Purpose**: Solves exam scheduling using constraint satisfaction.
- **Real-World Use Case**: A university uses this to schedule exams without student conflicts, improving logistics.
- **Code Breakdown**:
  - The `ExamScheduler` class initializes exams, slots, and conflicts.
  - The `is_valid` method checks constraint violations.
  - The `solve` method uses backtracking to find a valid schedule.
  - The `run_exam_scheduling` function returns the schedule.
- **Technical Challenges**: Handling large conflict graphs, ensuring completeness, and optimizing search.
- **Integration**: Complements Satisfiability Testing (Snippet 983) for constraint solving.
- **Scalability**: Exponential complexity; large problems require constraint propagation.
- **Performance Metrics**: Solves small instances (<10 exams) in seconds.
- **Best Practices**: Use constraint propagation, validate with real schedules, and add room constraints.
- **Extensions**: Include room capacities or professor availability.
- **Limitations**: Simplified model; real scheduling involves multiple constraints.