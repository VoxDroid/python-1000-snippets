# 0500-System-Monitoring Cheatsheet

- Use built-ins: `os.cpu_count()`, `os.getloadavg()`, `shutil.disk_usage()`.
- Save snapshots to a file under `temp/`.
- Example:
  - `python3 python-1000-snippets/0500-System-Monitoring/SAMPLES/sample1.py`
  - `python3 python-1000-snippets/0500-System-Monitoring/SAMPLES/sample2.py`
  - `python3 python-1000-snippets/0500-System-Monitoring/SAMPLES/sample3.py`.
- For periodic execution, call in cron: `*/5 * * * * /usr/bin/python3 /path/to/sample3.py`.
- For remote monitoring, push `temp/system_status.txt` to a central collector.
