# sample3.py
# Save cloud storage check result to temp file.

import os

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), '../../temp/0513_cloud_storage_status.txt')


def check_boto3():
    try:
        import boto3
        return 'boto3 available'
    except ImportError:
        return 'boto3 not installed'


if __name__ == '__main__':
    status = check_boto3()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w') as f:
        f.write(status + '\n')
    print('Wrote status:', OUTPUT_PATH)
