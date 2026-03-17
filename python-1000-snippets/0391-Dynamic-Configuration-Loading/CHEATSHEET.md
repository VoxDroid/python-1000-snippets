
# 0391-Dynamic-Configuration-Loading Cheatsheet

- Use `json.load()` to read configuration files.
- Provide sensible defaults when the file is missing.
- Use environment variables (`os.getenv`) to override config location.
- Use `argparse` to accept configuration file paths from the command line.
