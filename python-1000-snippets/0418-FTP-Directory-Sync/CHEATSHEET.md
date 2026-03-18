# 0418-FTP-Directory-Sync Cheatsheet

## Quick start
1. Install dependencies:
   ```bash
   pip install pyftpdlib
   ```
2. Run a sample:
   ```bash
   python SAMPLES/sample1.py
   ```

## Key concepts
- **pyftpdlib**: A Python FTP server library used to start an FTP service locally.
- **ftplib**: Standard library FTP client used to upload/download files.
- **Directory sync**: Pull files from the remote FTP server to a local directory, or push local files to the server.

## Notes
- These samples use a temporary directory for the server's file root and clean up on exit.
- For real deployments, use secure transports (FTPS/SFTP) and proper authentication.
