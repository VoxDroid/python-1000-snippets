# IMAP Email

## Description
This snippet demonstrates how to connect to an IMAP server using Python's built-in `imaplib` and fetch messages.

## Setup
A minimal in-process IMAP server is started by the sample scripts to allow testing without an external IMAP service. The server listens on `localhost:1143` and supports a small subset of IMAP commands (`LOGIN`, `LIST`, `SELECT`, `SEARCH`, `FETCH`, `LOGOUT`).

## Code
```python
# Run the sample scripts in python-1000-snippets/0224-IMAP-Email/SAMPLES/
# They start a minimal IMAP server and query it using imaplib.
```

## Output
The sample scripts print information about the messages fetched from the server (subject, sender, body, etc.).

## Explanation
- **imaplib**: Standard library for IMAP client operations.
- **IMAP Server**: For testing, a simple server is implemented in Python that responds to basic IMAP commands.
- **Logic**: The client logs in, selects a mailbox, searches for messages, and fetches raw data.
- **Use Case**: Automating email reading or monitoring.
- **Best Practice**: Use SSL/TLS for real IMAP servers and handle large mailboxes with paging.
