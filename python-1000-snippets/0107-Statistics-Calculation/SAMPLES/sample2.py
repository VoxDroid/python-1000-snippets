# sample2.py
# Use Python's statistics module

import statistics

if __name__ == '__main__':
    data = [2,4,4,4,5,5,7,9]
    print('mean', statistics.mean(data))
    print('median', statistics.median(data))
    print('variance sample', statistics.pvariance(data))
    print('variance population', statistics.pvariance(data))
    print('stdev', statistics.stdev(data))
