# sample1.py
# Detect SSH attempts from textual packet logs.


def detect_ssh_attempts(events):
    alerts = []
    for e in events:
        if 'proto=tcp' in e and 'dport=22' in e:
            alerts.append('SSH attempt detected: ' + e)
    return alerts


def main() -> None:
    events = [
        'src=10.0.0.1 dst=10.0.0.2 proto=tcp dport=22',
        'src=10.0.0.2 dst=10.0.0.1 proto=tcp dport=80',
    ]
    alerts = detect_ssh_attempts(events)
    print('Alerts:', alerts)


if __name__ == '__main__':
    main()
