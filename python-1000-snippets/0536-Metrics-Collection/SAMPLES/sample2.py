# sample2.py
# Simulate metrics computations for latency and throughput.


def compute_latency(raw_ms):
    return sum(raw_ms) / len(raw_ms)


def compute_throughput(count, duration):
    return count / duration if duration > 0 else 0


if __name__ == '__main__':
    lat = compute_latency([120, 135, 110, 100])
    tps = compute_throughput(1000, 60)
    print(f'Latency: {lat:.2f} ms, Throughput: {tps:.2f} req/s')
