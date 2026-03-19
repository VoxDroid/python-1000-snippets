# IMAP Email Filtering

## Description
This snippet demonstrates filtering email messages using Python's built-in `imaplib`.

Because testing against a real IMAP server requires another system, these examples run a small, in-process IMAP server that supports the subset of IMAP commands needed for filtering (LOGIN, SELECT, SEARCH, FETCH).

## Requirements
- Python 3.8+

## Samples
- `SAMPLES/sample1.py`: Search for messages from a specific sender and fetch headers.
- `SAMPLES/sample2.py`: Search by subject and mark a message as seen.
- `SAMPLES/sample3.py`: Search all messages and fetch the full message content.

## Running
```bash
python python-1000-snippets/0421-IMAP-Email-Filtering/SAMPLES/sample1.py
python python-1000-snippets/0421-IMAP-Email-Filtering/SAMPLES/sample2.py
python python-1000-snippets/0421-IMAP-Email-Filtering/SAMPLES/sample3.py
```

## Notes
- These examples do not connect to a real IMAP server; they demonstrate how to use `imaplib` against a compatible server implementation.
- The in-process server is intentionally minimal and implements only the commands used by the samples.
