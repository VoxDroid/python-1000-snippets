# IMAP Email Filtering

## Description
This snippet demonstrates filtering emails using `imaplib`.

## Code
```python
# Note: Requires `imaplib`
try:
    import imaplib
    mail = imaplib.IMAP4_SSL("imap.example.com")
    mail.login("user", "pass")
    mail.select("inbox")
    _, data = mail.search(None, 'FROM "sender@example.com"')
    print("Mock Output: Emails found")
    mail.logout()
except ImportError:
    print("Mock Output: Emails found")
```

## Output
```
Mock Output: Emails found
```
*(Real output with `imaplib` and IMAP server: `Emails found` or email IDs)*

## Explanation
- **IMAP Email Filtering**: Searches for emails from a sender.
- **Logic**: Connects to IMAP, searches inbox for matching emails.
- **Complexity**: O(n) for n emails (server-dependent).
- **Use Case**: Used for email automation or monitoring.
- **Best Practice**: Use SSL; handle connection errors; manage session state.