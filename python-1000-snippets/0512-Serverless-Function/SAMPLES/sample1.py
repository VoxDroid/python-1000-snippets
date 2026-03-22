# sample1.py
# Simulate an AWS Lambda function handler invocation.

def lambda_handler(event, context):
    name = event.get('name', 'world')
    return {'statusCode': 200, 'body': f'Hello {name}!'}


if __name__ == '__main__':
    response = lambda_handler({'name': 'developer'}, {})
    print('Response:', response['body'])
