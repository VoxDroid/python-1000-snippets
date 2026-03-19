# 0421 - IMAP Email Filtering Cheatsheet

## Quick Facts
- Uses Python's built-in `imaplib` to search and fetch messages.
- Includes an in-process IMAP server implementation for testing purposes.
- The server supports the IMAP commands used by the samples: `LOGIN`, `SELECT`, `SEARCH`, `FETCH`, and `STORE`.

## Run Samples
```bash
python python-1000-snippets/0421-IMAP-Email-Filtering/SAMPLES/sample1.py
python python-1000-snippets/0421-IMAP-Email-Filtering/SAMPLES/sample2.py
python python-1000-snippets/0421-IMAP-Email-Filtering/SAMPLES/sample3.py
```

## Key imaplib Calls
- `IMAP4(host, port)` - connect to the server.
- `login(user, password)` - authenticate.
- `select(mailbox)` - select a mailbox before searching.
- `search(None, criteria)` - search for messages matching criteria.
- `fetch(msgid, parts)` - fetch parts of a message.
- `store(msgid, command, flags)` - update message flags (e.g., mark as seen).

## Notes
- This sample server is **not** a full IMAP implementation; it implements a minimal subset to make the examples runnable.
