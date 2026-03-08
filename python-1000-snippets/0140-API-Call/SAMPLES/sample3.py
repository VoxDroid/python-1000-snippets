# sample3.py
# demonstrate timeout handling

import requests

if __name__ == '__main__':
    try:
        # endpoint delays 5 seconds; set timeout shorter to trigger exception
        r = requests.get('https://httpbin.org/delay/5', timeout=1)
        print(r.status_code)
    except requests.Timeout:
        print('timeout occurred')
    except requests.RequestException as e:
        print('request error', e)
