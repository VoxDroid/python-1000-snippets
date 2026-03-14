# 0224-IMAP-Email Cheatsheet

* Use Python's built-in `imaplib` to interact with IMAP servers.
* Connect with `imaplib.IMAP4(host, port)` or `IMAP4_SSL` for TLS.
* Authenticate with `login(user, password)`.
* Select a mailbox with `select('INBOX')`.
* Search messages with `search(None, 'ALL')` or specific criteria.
* Fetch messages with `fetch(msg_id, '(BODY[])')`.
* Use `email` module to parse raw message bytes.
* For testing, a minimal IMAP server can be implemented in Python using `asyncio`.
