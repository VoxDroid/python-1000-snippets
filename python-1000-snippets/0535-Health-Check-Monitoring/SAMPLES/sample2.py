# sample2.py
# Run multiple dependency checks and aggregate health state.


def db_check():
    return True


def cache_check():
    return True


def overall_health():
    checks = [db_check(), cache_check()]
    status = 'healthy' if all(checks) else 'unhealthy'
    return {'status': status, 'checks': checks}


if __name__ == '__main__':
    print('Overall health:', overall_health())
