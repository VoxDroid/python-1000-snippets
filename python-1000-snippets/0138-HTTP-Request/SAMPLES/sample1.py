# sample1.py
# simple GET request to a public API

try:
    import requests
    resp = requests.get('https://jsonplaceholder.typicode.com/todos/1', timeout=3)
    print('Response:', resp.json())
except ImportError:
    print("Mock Response: {'title': 'Test'}")
except Exception as e:
    print('Request failed:', e)
