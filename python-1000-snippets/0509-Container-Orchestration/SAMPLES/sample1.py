# sample1.py
# Build and print a Kubernetes pod specification.

import json


def create_pod(name='example-pod', image='nginx'):
    return {
        'apiVersion': 'v1',
        'kind': 'Pod',
        'metadata': {'name': name},
        'spec': {'containers': [{'name': name, 'image': image}]},
    }


if __name__ == '__main__':
    pod = create_pod()
    print('Pod definition:', json.dumps(pod, indent=2))
