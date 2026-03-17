# sample3.py
# Show how to programmatically install a package (requires pip access)

import subprocess
import sys


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


def main():
    try:
        import requests  # type: ignore
        print("requests already installed")
    except ImportError:
        print("Installing requests...")
        install("requests")
        import requests  # type: ignore
        print("requests installed", requests.__version__)


if __name__ == "__main__":
    main()
