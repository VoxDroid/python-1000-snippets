# SMTP Email with Attachments

## Description
This snippet demonstrates sending emails (plain text, HTML, and attachments) using Python's built-in `smtplib` and a local SMTP receiver.

Each sample starts a local SMTP server (via `aiosmtpd`) to receive the message so the examples run end-to-end without requiring an external mail server.

## Requirements
- Python 3.8+
- `aiosmtpd` (`pip install aiosmtpd`)

## Samples
- `SAMPLES/sample1.py`: Send a plain-text email and inspect the received raw message.
- `SAMPLES/sample2.py`: Send an email with a file attachment.
- `SAMPLES/sample3.py`: Send an HTML email with multiple attachments.

## Running
```bash
python python-1000-snippets/0420-SMTP-Email-with-Attachments/SAMPLES/sample1.py
python python-1000-snippets/0420-SMTP-Email-with-Attachments/SAMPLES/sample2.py
python python-1000-snippets/0420-SMTP-Email-with-Attachments/SAMPLES/sample3.py
```

## Notes
- Emails are stored in a `temp/` folder under the repository root.
- These examples do not deliver mail to an external inbox; they demonstrate how to construct and send MIME messages.
