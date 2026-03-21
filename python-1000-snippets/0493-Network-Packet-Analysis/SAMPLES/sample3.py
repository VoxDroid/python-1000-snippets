# sample3.py
# Identify suspicious packet patterns (multiple SYN-like events) in text packet stream.


def detect_syn_flood(events):
    syn_count = 0
    for ev in events:
        parts = {kv.split('=')[0].strip(): kv.split('=')[1].strip() for kv in ev.split(',')}
        if parts.get('flags') == 'SYN':
            syn_count += 1
    return syn_count > 3


def main() -> None:
    events = [
        'src=10.0.0.1,dst=10.0.0.2,flags=SYN',
        'src=10.0.0.1,dst=10.0.0.2,flags=SYN',
        'src=10.0.0.1,dst=10.0.0.2,flags=SYN',
        'src=10.0.0.1,dst=10.0.0.2,flags=SYN',
        'src=10.0.0.3,dst=10.0.0.4,flags=ACK',
    ]
    print('SYN flood suspected:' , detect_syn_flood(events))


if __name__ == '__main__':
    main()
