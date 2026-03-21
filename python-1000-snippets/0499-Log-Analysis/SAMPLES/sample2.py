# sample2.py
# Count occurrences of each event type in log lines.


def count_events(lines):
    counts = {}
    for line in lines:
        token = line.split(']')[-1].strip().split(' ',1)[0]
        if token:
            counts[token] = counts.get(token,0)+1
    return counts


def main() -> None:
    lines = [
        '[2026-03-20 08:00:00] login user=alice',
        '[2026-03-20 08:05:00] logout user=alice',
        '[2026-03-20 08:10:00] login user=bob',
        '[2026-03-20 08:15:00] login user=charlie',
    ]
    print('Counts:', count_events(lines))


if __name__ == '__main__':
    main()