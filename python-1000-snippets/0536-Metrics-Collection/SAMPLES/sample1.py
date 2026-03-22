# sample1.py
# Metrics collection with optional prometheus_client, fallback to local counters.


def collect_metrics():
    data = {'requests': 5, 'errors': 1}
    try:
        from prometheus_client import Counter, Gauge
        req_counter = Counter('requests_total', 'Total requests')
        err_counter = Counter('errors_total', 'Total errors')
        req_counter.inc(data['requests'])
        err_counter.inc(data['errors'])
        return {'prometheus': True, 'values': data}
    except ImportError:
        return {'prometheus': False, 'values': data}


if __name__ == '__main__':
    print('Metrics:', collect_metrics())
