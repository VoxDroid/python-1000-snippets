# sample1.py
# Check for optional dependency and handle missing package

try:
    import numpy as np  # type: ignore
    print("numpy is available", np.__version__)
except ImportError:
    print("numpy is not installed; install it with `pip install numpy`")
