# sample1.py
# Build a temporary file and optionally upload to S3 if boto3 / credentials are available.

import os
import tempfile


def write_temp_file():
    with tempfile.NamedTemporaryFile('w', delete=False, suffix='.txt') as f:
        f.write('cloud storage integration test')
        return f.name


def upload_s3(path, bucket='demo-bucket', key='0513_test.txt'):
    try:
        import boto3
        s3 = boto3.client('s3')
        s3.upload_file(path, bucket, key)
        return 'uploaded'
    except Exception as e:
        return f'upload not possible: {e}'


if __name__ == '__main__':
    filepath = write_temp_file()
    print('Local file created:', filepath)
    status = upload_s3(filepath)
    print(status)
    os.remove(filepath)
