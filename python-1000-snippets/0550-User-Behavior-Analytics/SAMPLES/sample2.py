# sample2.py
# Compute per-user click rate and print sample analytics.


def user_click_stats(events):
    clicks = {}
    sessions = {}
    for e in events:
        u = e['user']
        sessions.setdefault(u, 0)
        clicks.setdefault(u, 0)
        sessions[u] += 1
        if e['action'] == 'click':
            clicks[u] += 1
    return {u: clicks[u] / sessions[u] for u in sessions}


if __name__ == '__main__':
    events = [{'user': 1, 'action': 'click'}, {'user': 1, 'action': 'view'}, {'user': 2, 'action': 'click'}, {'user': 2, 'action': 'click'}]
    print('User click rates:', user_click_stats(events))
