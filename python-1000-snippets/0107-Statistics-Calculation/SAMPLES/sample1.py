# sample1.py
# Compute mean, median, variance

def statistics(data):
    n = len(data)
    if n == 0:
        return None, None, None
    mean = sum(data) / n
    sorted_data = sorted(data)
    median = sorted_data[n//2] if n % 2 else (sorted_data[n//2-1] + sorted_data[n//2]) / 2
    variance = sum((x - mean) ** 2 for x in data) / n
    return mean, median, variance

if __name__ == '__main__':
    d=[1,2,3,4,5]
    print(statistics(d))
