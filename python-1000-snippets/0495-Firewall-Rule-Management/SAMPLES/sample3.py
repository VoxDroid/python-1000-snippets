# sample3.py
# Evaluate whether incoming packets match active rules (TCP port allow list).


def check_packet(rules, packet):
    # rules are strings with --dport X
    for rule in rules:
        if '--dport' in rule:
            parts = rule.split()
            i = parts.index('--dport')
            port = parts[i+1]
            if packet.get('proto') == 'tcp' and str(packet.get('dport')) == port:
                return True
    return False


def main() -> None:
    rules = ['iptables -A INPUT -p tcp --dport 22 -j ACCEPT']
    packets = [{'proto':'tcp','dport':22},{'proto':'tcp','dport':80}]
    for p in packets:
        print('packet', p, 'allowed?', check_packet(rules,p))


if __name__ == '__main__':
    main()
