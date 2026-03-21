# sample3.py
# Parse basic JSON protocol payload and validate required keys.

import json


def validate_payload(payload):
    try:
        obj = json.loads(payload)
    except json.JSONDecodeError:
        return False, None
    ok = 'type' in obj and 'data' in obj
    return ok, obj


def main() -> None:
    payload = '{"type":"ping","data":{"id":123}}'
    ok, obj = validate_payload(payload)
    print('Valid:', ok)
    print('Object:', obj)


if __name__ == '__main__':
    main()
