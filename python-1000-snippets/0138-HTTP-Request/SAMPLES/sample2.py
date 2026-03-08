# sample2.py
# demonstrate timeout handling

try:
    import requests
    try:
        requests.get('https://httpbin.org/delay/5', timeout=1)
    except requests.exceptions.Timeout:
        print('timed out as expected')
except ImportError:
    print('Mock timeout case')
