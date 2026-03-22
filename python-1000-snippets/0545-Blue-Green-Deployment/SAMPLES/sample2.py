# sample2.py
# Decide traffic routing based on active environment.


def route_traffic(active_env):
    return f'Routing to {active_env} environment'


if __name__ == '__main__':
    print(route_traffic('green'))
