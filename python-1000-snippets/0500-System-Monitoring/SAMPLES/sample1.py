# sample1.py
# Monitor system load averages and CPU count.

import os


def main() -> None:
    cpus = os.cpu_count()
    load = os.getloadavg() if hasattr(os, 'getloadavg') else (0.0, 0.0, 0.0)
    print(f'CPUs: {cpus}, load1/5/15: {load[0]:.2f}/{load[1]:.2f}/{load[2]:.2f}')


if __name__ == '__main__':
    main()
