# sample2.py
# Write a Kubernetes deployment YAML file to temp.

import os

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), '../../temp/0511_deployment.yaml')


def deployment_yaml(name='nginx-deployment', image='nginx:latest'):
    return f"""apiVersion: apps/v1
kind: Deployment
metadata:
  name: {name}
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: {image}
"""


if __name__ == '__main__':
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w') as f:
        f.write(deployment_yaml())
    print('Wrote deployment YAML to', OUTPUT_PATH)
