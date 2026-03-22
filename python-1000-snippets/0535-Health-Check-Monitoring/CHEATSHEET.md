# 0535-Health-Check-Monitoring Cheatsheet

- `python SAMPLES/sample1.py` : quick inline health check reporting.
- `python SAMPLES/sample2.py` : simulated dependency aggregates (DB + cache).
- `python SAMPLES/sample3.py` : write health status file to `temp/0535_health_status.txt`.

Tips:
- Emulate endpoint checks in non-server workflows.
- Return detailed status for SSD, memory, network checks in real apps.
- Use `status` fields: `healthy`, `degraded`, `unhealthy` for monitoring systems.
