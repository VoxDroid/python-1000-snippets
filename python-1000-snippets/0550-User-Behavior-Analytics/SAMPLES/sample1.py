# sample1.py
# Count user click events (pure Python analytics).


def count_clicks(events):
    return sum(1 for e in events if e.get('action') == 'click')


def events_from_pandas():
    try:
        import pandas as pd
        df = pd.DataFrame({'user': [1, 1, 2], 'action': ['click', 'view', 'click']})
        events = df.to_dict('records')
        return events
    except ImportError:
        return [{'user': 1, 'action': 'click'}, {'user': 1, 'action': 'view'}, {'user': 2, 'action': 'click'}]


if __name__ == '__main__':
    events = events_from_pandas()
    print('Click counts:', count_clicks(events))
