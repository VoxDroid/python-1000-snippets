# IMAP Email

## Description
This snippet demonstrates reading emails using `imaplib`.

## Code
```python
import imaplib
try:
    mail = imaplib.IMAP4_SSL("imap.example.com")
    mail.login("user", "password")
    mail.select("inbox")
    _, data = mail.search(None, "ALL")
    print("Emails found:", len(data[0].split()))
    mail.logout()
except:
    print("Mock Output: Emails found: 1")
```

## Output
```
Mock Output: Emails found: 1
```
*(Real output with IMAP: `Emails found: <number of emails>`)*

## Explanation
- **IMAP Email**: Connects to an IMAP server and counts emails in the inbox.
- **Logic**: Logs in, selects the inbox, and searches for all emails.
- **Complexity**: O(n) for n emails in the search.
- **Use Case**: Used for email automation or monitoring.
- **Best Practice**: Use SSL; handle large mailboxes; secure credentials.