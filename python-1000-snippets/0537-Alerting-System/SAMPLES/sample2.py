# sample2.py
# Threshold alerting for memory usage.


def memory_alert(used_mb, limit_mb=1024):
    if used_mb > limit_mb:
        return {'status': 'alert', 'message': 'Memory threshold exceeded'}
    return {'status': 'ok'}


if __name__ == '__main__':
    print(memory_alert(1536))
