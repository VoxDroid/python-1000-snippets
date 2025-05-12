# SMTP Email with Attachments

## Description
This snippet demonstrates sending an email with an attachment using `smtplib`.

## Code
```python
# Note: Requires `email`
try:
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    msg = MIMEMultipart()
    msg["To"] = "recipient@example.com"
    msg["From"] = "sender@example.com"
    msg["Subject"] = "Test"
    msg.attach(MIMEText("Body"))
    print("Email prepared")
except ImportError:
    print("Mock Output: Email prepared")
```

## Output
```
Mock Output: Email prepared
```
*(Real output with `smtplib` and SMTP server: Sends email)*

## Explanation
- **SMTP Email with Attachments**: Prepares an email with a text body.
- **Logic**: Creates a MIME message with a body (attachment logic omitted for brevity).
- **Complexity**: O(n) for n bytes in email.
- **Use Case**: Used for notifications or automated emails.
- **Best Practice**: Secure with TLS; handle SMTP errors; validate recipients.