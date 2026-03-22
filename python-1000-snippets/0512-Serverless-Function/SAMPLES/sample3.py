# sample3.py
# Write serverless invocation results to temp file.

import os

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), '../../temp/0512_lambda_results.txt')


def lambda_handler(event, context):
    return {'statusCode': 200, 'body': event.get('message', 'hello')}


if __name__ == '__main__':
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w') as f:
        for m in ['first', 'second', 'third']:
            response = lambda_handler({'message': m}, {})
            f.write(response['body'] + '\n')
    print('Wrote lambda results to', OUTPUT_PATH)
