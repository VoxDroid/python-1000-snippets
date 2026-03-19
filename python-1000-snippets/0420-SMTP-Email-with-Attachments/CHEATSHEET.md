# 0420 - SMTP Email with Attachments Cheatsheet

## Quick Facts
- Uses `aiosmtpd` to run a local SMTP server for testing.
- Uses Python's built-in `smtplib` to send email messages.
- Emails are captured to files under `temp/` so you can inspect the MIME payload.

## Run Samples
```bash
python python-1000-snippets/0420-SMTP-Email-with-Attachments/SAMPLES/sample1.py
python python-1000-snippets/0420-SMTP-Email-with-Attachments/SAMPLES/sample2.py
python python-1000-snippets/0420-SMTP-Email-with-Attachments/SAMPLES/sample3.py
```

## Key Concepts
- `EmailMessage` builds MIME messages (body + attachments).
- `smtplib.SMTP` sends messages to an SMTP server.
- `aiosmtpd.controller.Controller` provides an in-process SMTP server for testing.

## Tip
To inspect the raw MIME message, open the `.eml` file created under `temp/` after running a sample.
