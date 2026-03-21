# sample2.py
# Simple signature detection: find suspicious payload patterns.


def detect_suspicious_payload(payloads):
    signatures = ['DROP TABLE', 'UNION SELECT', 'cmd.exe']
    hits = []
    for p in payloads:
        for sig in signatures:
            if sig.lower() in p.lower():
                hits.append((p, sig))
    return hits


def main() -> None:
    payloads = [
        'normal traffic',
        'GET /index.html HTTP/1.1',
        'DROP TABLE users;',
        'Some text with union select exploit',
    ]
    detections = detect_suspicious_payload(payloads)
    print('Detections:', detections)


if __name__ == '__main__':
    main()
