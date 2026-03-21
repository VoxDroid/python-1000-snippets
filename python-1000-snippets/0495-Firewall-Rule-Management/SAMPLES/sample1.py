# sample1.py
# Validate simple iptables-like rule strings.


def parse_rule(rule):
    parts = rule.split()
    out = {}
    key = None
    for part in parts:
        if part.startswith('-'):
            key = part
            out[key] = []
        elif key:
            out[key].append(part)
    return out


def main() -> None:
    rule = 'iptables -A INPUT -p tcp --dport 80 -j ACCEPT'
    parsed = parse_rule(rule)
    print('Parsed rule:', parsed)


if __name__ == '__main__':
    main()
