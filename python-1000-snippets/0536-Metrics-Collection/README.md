# Metrics Collection

## Description
Collects service metrics and optionally exports to Prometheus.

## Samples
- `SAMPLES/sample1.py`: basic counter/gauge metrics (prometheus fallback).
- `SAMPLES/sample2.py`: latency and throughput calculations.
- `SAMPLES/sample3.py`: write metrics to `temp/0536_metrics.txt`.

## Output
- `sample1.py`: metrics dictionary.
- `sample2.py`: latency and throughput numbers.
- `sample3.py`: file creation in temp.

## Explanation
Metrics collection is critical for observability. Use counters and gauges; retain snapshot data; export to monitoring systems.
