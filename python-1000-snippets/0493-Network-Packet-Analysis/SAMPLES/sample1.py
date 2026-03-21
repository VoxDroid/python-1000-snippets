# sample1.py
# Parse a text representation of packets and count TCP entries.


def parse_packets(lines):
    packets = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        fields = line.split(',')
        packet = {kv.split('=')[0].strip(): kv.split('=')[1].strip() for kv in fields}
        packets.append(packet)
    return packets


def main() -> None:
    raw = [
        'proto=TCP, src=192.168.0.1, dst=192.168.0.2, len=60',
        'proto=UDP, src=192.168.0.2, dst=192.168.0.3, len=70',
        'proto=TCP, src=10.0.0.1, dst=10.0.0.2, len=52',
    ]
    packets = parse_packets(raw)
    tcp_count = sum(1 for p in packets if p.get('proto') == 'TCP')
    print('TCP packets:', tcp_count)


if __name__ == '__main__':
    main()
