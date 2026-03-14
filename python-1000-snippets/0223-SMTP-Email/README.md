# SMTP Email

## Description
This snippet demonstrates sending email via a local SMTP server using Python's built-in `smtplib`.

## Setup
A local SMTP server is started in-process for testing using `aiosmtpd`. It runs on `localhost:1025` and accepts messages without authentication.

## Code
```python
# Run the sample scripts in python-1000-snippets/0223-SMTP-Email/SAMPLES/
# They start an in-process SMTP server and send messages to it.
```

## Output
The sample scripts print the number of messages received by the local server and some metadata about the first message.

## Explanation
- **smtplib**: Provides a client interface for SMTP.
- **aiosmtpd**: A lightweight SMTP server used here to receive test messages.
- **Logic**: Start a local SMTP server, send a message, and inspect the received envelope.
- **Use Case**: Useful for testing email sending logic without relying on an external SMTP provider.
- **Best Practice**: Use TLS and proper authentication in production; keep credentials secure.
