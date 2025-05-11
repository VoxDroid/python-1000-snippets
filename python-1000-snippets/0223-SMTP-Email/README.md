# SMTP Email

## Description
This snippet demonstrates sending an email using `smtplib`.

## Code
```python
import smtplib
from email.mime.text import MIMEText
try:
    msg = MIMEText("Hello, SMTP!")
    msg["Subject"] = "Test Email"
    msg["From"] = "sender@example.com"
    msg["To"] = "receiver@example.com"
    with smtplib.SMTP("smtp.example.com", 587) as server:
        server.starttls()
        server.login("user", "password")
        server.send_message(msg)
    print("Email sent")
except:
    print("Mock Output: Email sent")
```

## Output
```
Mock Output: Email sent
```
*(Real output with SMTP: `Email sent`)*

## Explanation
- **SMTP Email**: Sends an email using `smtplib` and `MIMEText`.
- **Logic**: Configures an email and sends it via an SMTP server.
- **Complexity**: O(1) for sending (network latency varies).
- **Use Case**: Used for automated notifications or alerts.
- **Best Practice**: Use TLS; secure credentials; handle server errors.