# 0332-Voting-System Cheatsheet

## Quick commands
```bash
python SAMPLES/sample1.py  # Plurality voting
python SAMPLES/sample2.py  # Instant-runoff voting (IRV)
python SAMPLES/sample3.py  # Borda count
```

## Tips
- Plurality selects the candidate with the most first-place votes.
- IRV repeatedly eliminates the candidate with the fewest first-place votes and redistributes their ballots.
- Borda count assigns points based on rank (e.g., 1st=3, 2nd=2, 3rd=1).

## Common patterns
- Count votes using `collections.Counter`.
- Represent ballots as lists of ranked candidates.
- Use loops to update counts and eliminate candidates.
