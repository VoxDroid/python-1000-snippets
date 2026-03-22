# sample2.py
# Toggle feature at runtime and report status.

FEATURE_FLAGS = {'new_ui': False}


def set_feature(feature_name, enabled):
    FEATURE_FLAGS[feature_name] = enabled


def status(feature_name):
    return FEATURE_FLAGS.get(feature_name, False)


if __name__ == '__main__':
    set_feature('new_ui', True)
    print('new_ui status:', status('new_ui'))
