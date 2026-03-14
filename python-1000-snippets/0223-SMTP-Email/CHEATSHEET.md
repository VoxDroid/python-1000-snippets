# 0223-SMTP-Email Cheatsheet

* Use Python's built-in `smtplib` to send emails.
* Create messages with `email.message.EmailMessage`.
* Connect to an SMTP server with `smtplib.SMTP(host, port)`.
* For TLS, call `starttls()` then `login(user, password)`.
* Send messages with `send_message(msg)`.
* For testing, run a local SMTP server using `aiosmtpd.controller.Controller`.
* Keep credentials secret and avoid hardcoding passwords.
