"""Solve the alphametic puzzle SEND + MORE = MONEY using brute-force search."""

import itertools


def solve_alphametic() -> None:
    letters = "SENDMORY"  # distinct letters in the puzzle
    for perm in itertools.permutations('0123456789', len(letters)):
        mapping = dict(zip(letters, perm))
        # Leading letters cannot be zero
        if mapping['S'] == '0' or mapping['M'] == '0':
            continue

        send = int(''.join(mapping[c] for c in 'SEND'))
        more = int(''.join(mapping[c] for c in 'MORE'))
        money = int(''.join(mapping[c] for c in 'MONEY'))

        if send + more == money:
            print(f"SEND + MORE = MONEY solution: {send} + {more} = {money}")
            return

    print("No solution found")


if __name__ == "__main__":
    solve_alphametic()
