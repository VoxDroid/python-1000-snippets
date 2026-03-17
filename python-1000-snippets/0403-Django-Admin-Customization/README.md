# Django Admin Customization

## Description
Demonstrates customizing the Django admin interface programmatically without running a full Django server.

## Files
- `SAMPLES/sample1.py` — Configure minimal Django settings and create a model table.
- `SAMPLES/sample2.py` — Register a model with a custom `ModelAdmin` class.
- `SAMPLES/sample3.py` — Show `list_display` and `search_fields` configuration.

## Usage
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Notes
- Scripts install `django` automatically if it's missing.
- Uses an in-memory SQLite database, so no external process is required.
