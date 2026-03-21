# sample2.py
# Write a Pod manifest to a YAML-like file in temp.

import os

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), '../../temp/0509_pod_manifest.yaml')


def generate_manifest(name='example-pod', image='nginx'):
    return f"""apiVersion: v1
kind: Pod
metadata:
  name: {name}
spec:
  containers:
  - name: {name}
    image: {image}
"""


if __name__ == '__main__':
    manifest = generate_manifest()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w') as f:
        f.write(manifest)
    print('Wrote pod manifest to', OUTPUT_PATH)

    assert 'apiVersion: v1' in manifest
    assert 'kind: Pod' in manifest
