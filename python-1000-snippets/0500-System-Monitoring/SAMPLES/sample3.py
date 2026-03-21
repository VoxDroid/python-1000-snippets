# sample3.py
# Write a system status snapshot to temp/system_status.txt.

import os
import platform
import shutil

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), '../../temp/system_status.txt')


def main() -> None:
    if hasattr(os, 'getloadavg'):
        load = os.getloadavg()
    else:
        load = (0.0, 0.0, 0.0)

    total, used, free = shutil.disk_usage('/')
    lines = [
        f'Platform: {platform.system()} {platform.release()}',
        f'CPU count: {os.cpu_count()}',
        f'Load avg: {load[0]:.2f}, {load[1]:.2f}, {load[2]:.2f}',
        'Disk total: {:.2f}GB used: {:.2f}GB free: {:.2f}GB'.format(
            total / (1024**3), used / (1024**3), free / (1024**3)),
    ]
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w') as f:
        f.write('\n'.join(lines) + '\n')
    print('Wrote system status to', OUTPUT_PATH)


if __name__ == '__main__':
    main()
