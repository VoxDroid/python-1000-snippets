# 0502-Memory-Leak-Detection Cheatsheet

- Run the samples:
  - `python3 python-1000-snippets/0502-Memory-Leak-Detection/SAMPLES/sample1.py`
  - `python3 python-1000-snippets/0502-Memory-Leak-Detection/SAMPLES/sample2.py`
  - `python3 python-1000-snippets/0502-Memory-Leak-Detection/SAMPLES/sample3.py`
- Snapshot file: `python-1000-snippets/temp/0502_mem_snapshot.txt`
- See memory usage differences with `traceback` filtering:
  - `tracemalloc.Filter(False, '<frozen importlib._bootstrap>')`

