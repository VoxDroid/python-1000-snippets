# 0501-Performance-Profiling Cheatsheet

- Run sample scripts:
  - `python3 python-1000-snippets/0501-Performance-Profiling/SAMPLES/sample1.py`
  - `python3 python-1000-snippets/0501-Performance-Profiling/SAMPLES/sample2.py`
  - `python3 python-1000-snippets/0501-Performance-Profiling/SAMPLES/sample3.py`
- Profile output file path: `python-1000-snippets/temp/0501_profile.stats`
- Inspect stats:
  - `python3 - <<'PY'
import pstats
pstats.Stats('python-1000-snippets/temp/0501_profile.stats').sort_stats('cumulative').print_stats(20)
PY`

