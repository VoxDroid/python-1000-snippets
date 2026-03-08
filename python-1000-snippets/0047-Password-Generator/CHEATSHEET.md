# Password Generator Cheatsheet

## Character sets
- `string.ascii_letters`, `string.digits`, `string.punctuation`
- Combine to build pool: `chars = ''.join([...])`

## Random modules
- `random.choice` – fine for examples.
- `secrets.choice` – use for real passwords.

## Tips
- Minimum length 8+ recommended.
- Avoid ambiguous characters (e.g., `l`, `I`, `0`, `O`) if sharing.

## Running samples
Activate venv and run `SAMPLES/sample*.py`.
