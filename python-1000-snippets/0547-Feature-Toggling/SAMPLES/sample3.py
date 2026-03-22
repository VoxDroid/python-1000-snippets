# sample3.py
# Save toggle state into temp status file.

import os

OUTPUT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'temp', '0547_toggle_status.txt'))


def save_feature_status(feature_name, enabled):
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'a') as f:
        f.write(f'{feature_name}:{enabled}\n')
    return True


if __name__ == '__main__':
    save_feature_status('new_ui', True)
    print('Saved toggle status to', OUTPUT_PATH)
    with open(OUTPUT_PATH) as f:
        print(f.read().strip())
