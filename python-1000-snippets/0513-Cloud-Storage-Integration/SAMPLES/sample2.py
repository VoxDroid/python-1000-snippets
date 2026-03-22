# sample2.py
# Demonstrate S3 list keys if boto3 installed, otherwise print clean fallback.

try:
    import boto3
except ImportError:
    boto3 = None


def list_buckets():
    if boto3 is None:
        return 'boto3 not installed'
    try:
        s3 = boto3.client('s3')
        buckets = s3.list_buckets().get('Buckets', [])
        return [b['Name'] for b in buckets]
    except Exception as e:
        return f'list failed: {e}'


if __name__ == '__main__':
    print('S3 buckets:', list_buckets())
