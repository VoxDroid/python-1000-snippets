# sample2.py
# Analyze packet bytes (hex string) and print summary of packet sizes.


def parse_hex_packet(hex_str):
    data = bytes.fromhex(hex_str.replace(' ', ''))
    return len(data), data[:4]


def main() -> None:
    hex_packets = [
        '45 00 00 3c 1c 46 40 00 40 06 b1 e6 c0 a8 00 01 c0 a8 00 02',
        '45 00 00 28 6f 35 40 00 40 11 b8 61 c0 a8 00 01 c0 a8 00 02',
    ]
    for i, h in enumerate(hex_packets, start=1):
        size, hdr = parse_hex_packet(h)
        print(f'Packet {i}: size={size}, hdr={hdr.hex()}')


if __name__ == '__main__':
    main()
