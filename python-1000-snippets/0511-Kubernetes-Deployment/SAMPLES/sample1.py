# sample1.py
# Build a Kubernetes Deployment manifest and print JSON.

import json


def create_deployment(name='nginx-deployment', image='nginx:latest', replicas=1):
    return {
        'apiVersion': 'apps/v1',
        'kind': 'Deployment',
        'metadata': {'name': name},
        'spec': {
            'replicas': replicas,
            'selector': {'matchLabels': {'app': 'nginx'}},
            'template': {
                'metadata': {'labels': {'app': 'nginx'}},
                'spec': {'containers': [{'name': 'nginx', 'image': image}]}
            }
        }
    }


if __name__ == '__main__':
    deployment = create_deployment()
    print('Deployment manifest:')
    print(json.dumps(deployment, indent=2))
