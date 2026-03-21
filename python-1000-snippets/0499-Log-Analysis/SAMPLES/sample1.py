# sample1.py
# Simple log parser that reads lines and extracts event types.


def parse_log(lines):
    events = []
    for line in lines:
        line=line.strip()
        if not line:
            continue
        # Expected format: [timestamp] event_type message
        parts=line.split(']',1)
        if len(parts)>1:
            rest=parts[1].strip()
            ev = rest.split(' ',1)[0]
            events.append(ev)
    return events


def main() -> None:
    lines = [
        '[2026-03-20 08:00:00] login user=alice',
        '[2026-03-20 08:05:00] logout user=alice',
        '[2026-03-20 08:10:00] login user=bob',
    ]
    events=parse_log(lines)
    print('Events:', events)


if __name__ == '__main__':
    main()