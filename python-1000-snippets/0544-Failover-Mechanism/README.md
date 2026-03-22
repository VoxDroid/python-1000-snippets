# Failover Mechanism

## Description
Implements primary-to-backup failover behavior.

## Samples
- `SAMPLES/sample1.py`: choose active server.
- `SAMPLES/sample2.py`: failover decision based on health.
- `SAMPLES/sample3.py`: log selected server to `temp/0544_failover.log`.

## Output
Selected service endpoint and log file.

## Explanation
Automated failover minimizes downtime and requires detection, selection, and recovery steps.
