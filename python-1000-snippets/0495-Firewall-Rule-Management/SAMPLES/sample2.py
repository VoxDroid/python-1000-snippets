# sample2.py
# Maintain an in-memory firewall rule list and apply add/remove operations.


def apply_rules(ops):
    rules = []
    for op in ops:
        if op.startswith('ADD '):
            rules.append(op[4:])
        elif op.startswith('REMOVE '):
            rule = op[7:]
            if rule in rules:
                rules.remove(rule)
    return rules


def main() -> None:
    ops = [
        'ADD iptables -A INPUT -p tcp --dport 80 -j ACCEPT',
        'ADD iptables -A INPUT -p tcp --dport 22 -j ACCEPT',
        'REMOVE iptables -A INPUT -p tcp --dport 80 -j ACCEPT',
    ]
    final = apply_rules(ops)
    print('Active rules:', final)


if __name__ == '__main__':
    main()
