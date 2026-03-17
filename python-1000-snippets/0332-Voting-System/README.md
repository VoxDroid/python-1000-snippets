# Voting System

## Description
This snippet demonstrates simple voting systems for aggregating preferences.

## Files
- `SAMPLES/sample1.py`: Plurality (first-past-the-post) voting.
- `SAMPLES/sample2.py`: Instant-runoff voting (IRV) / ranked-choice voting.
- `SAMPLES/sample3.py`: Borda count voting.

## Quick start
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Expected output (example)
```
Plurality winner: A
IRV winner: B
Borda winner: C
```

## Explanation
- **Plurality**: Candidate with most first-place votes wins.
- **IRV**: Iteratively eliminate the lowest candidate and redistribute preferences.
- **Borda count**: Points assigned based on ranking positions.
