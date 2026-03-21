# sample3.py
# Stateful detection of repeated failed login attempts in event logs.


def failed_login_detection(events, threshold=3):
    counts = {}
    alerts = []
    for e in events:
        if 'login failed' in e.lower():
            user = e.split('user=')[1]
            counts[user] = counts.get(user, 0) + 1
            if counts[user] == threshold:
                alerts.append(f'Brute-force suspected for {user}')
    return alerts


def main() -> None:
    events = [
        'user=alice login failed',
        'user=alice login failed',
        'user=bob login success',
        'user=alice login failed',
    ]
    print(failed_login_detection(events))


if __name__ == '__main__':
    main()
