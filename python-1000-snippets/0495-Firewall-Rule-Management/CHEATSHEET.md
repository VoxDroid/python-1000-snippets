# 0495-Firewall-Rule-Management Cheatsheet

## Quick Start
```bash
python3 python-1000-snippets/0495-Firewall-Rule-Management/SAMPLES/sample1.py
```

## Notes
- `sample1.py`: parse iptables-like rule string.
- `sample2.py`: apply add/remove operations on rules.
- `sample3.py`: check packet allow/deny decisions.

## Tips
- Convert rules into structured objects for safer handling.
- Keep all rule modifications in logs under `temp/` for audit.
