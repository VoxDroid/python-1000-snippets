# sample2.py
# Simulate local invocation of serverless function with list events.

def lambda_handler(event, context):
    value = event.get('value', 0)
    return {'statusCode': 200, 'body': value * 2}


def run_batch(events):
    return [lambda_handler(event, {})['body'] for event in events]


if __name__ == '__main__':
    events = [{'value': i} for i in range(5)]
    print('Batch results:', run_batch(events))
