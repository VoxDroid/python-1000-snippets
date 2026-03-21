# 0504-Process-Pool-Management Cheatsheet

- Run the samples:
  - `python3 python-1000-snippets/0504-Process-Pool-Management/SAMPLES/sample1.py`
  - `python3 python-1000-snippets/0504-Process-Pool-Management/SAMPLES/sample2.py`
  - `python3 python-1000-snippets/0504-Process-Pool-Management/SAMPLES/sample3.py`
- Summary file: `python-1000-snippets/temp/0504_process_pool.txt`
- For low-latency tasks, use thread pools; for CPU bound, use process pools.
- If running in WSL or containers, set `if __name__ == '__main__'` guard to avoid re-spawning loops.

