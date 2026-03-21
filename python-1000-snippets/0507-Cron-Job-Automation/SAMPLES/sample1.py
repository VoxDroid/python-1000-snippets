# sample1.py
# Schedule a task every 0.3 seconds 3 times using threading.Timer.

import threading


def job_run(counter=[0]):
    counter[0] += 1
    print(f'Cron task run #{counter[0]}')
    if counter[0] < 3:
        threading.Timer(0.3, job_run).start()


if __name__ == '__main__':
    job_run()
    # wait for all scheduled runs to finish
    threading.Event().wait(1.0)
