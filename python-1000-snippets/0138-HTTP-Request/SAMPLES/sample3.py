# sample3.py
# show status code check

try:
    import requests
    r = requests.get('https://httpbin.org/status/404')
    print('status', r.status_code)
except ImportError:
    print('Mock status 404')
except Exception as e:
    print('request error', e)
