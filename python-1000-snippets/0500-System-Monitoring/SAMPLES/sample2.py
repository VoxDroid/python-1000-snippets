# sample2.py
# Monitor disk usage of root path.

import shutil


def main() -> None:
    total, used, free = shutil.disk_usage('/')
    print('Disk usage: total={}GB used={}GB free={}GB'.format(
        round(total / (1024**3), 2),
        round(used / (1024**3), 2),
        round(free / (1024**3), 2),
    ))


if __name__ == '__main__':
    main()
