# sample2.py
# Recommend content based on user preferences from a recommendation map.

PREFERENCES = {
    'action': ['movie1', 'movie2'],
    'comedy': ['movie3', 'movie4']
}


def recommend(user_pref):
    return PREFERENCES.get(user_pref, [])


if __name__ == '__main__':
    print('User 1 recs:', recommend('action'))
