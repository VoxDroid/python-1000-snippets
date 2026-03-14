# 0229-OAuth2-Authentication Cheatsheet

## Goal
Demonstrate an OAuth2 **Client Credentials** flow using a local OAuth2 token server.

## Run
1. Change into the snippet folder:
   ```bash
   cd python-1000-snippets/0229-OAuth2-Authentication/SAMPLES
   ```
2. Run a sample script:
   ```bash
   python sample1.py
   python sample2.py
   python sample3.py
   ```

## What it does
- Starts a local Flask OAuth2 token endpoint at `http://localhost:5001/token`
- Obtains an access token using client credentials (`client_id/client_secret`)
- Uses access token to call a protected endpoint at `http://localhost:5001/resource`

## Notes
- For real deployments, use HTTPS and secure secret storage.
- This example uses a fixed access token and simple in-process server for learning purposes.
