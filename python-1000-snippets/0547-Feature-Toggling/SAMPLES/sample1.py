# sample1.py
# Feature toggle lookup.

FEATURE_FLAGS = {
    'new_ui': False,
    'beta_search': True
}


def is_enabled(feature_name):
    return FEATURE_FLAGS.get(feature_name, False)


if __name__ == '__main__':
    print('new_ui:', 'enabled' if is_enabled('new_ui') else 'disabled')
    print('beta_search:', 'enabled' if is_enabled('beta_search') else 'disabled')
