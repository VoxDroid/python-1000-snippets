# 0416-REST-API-Pagination Cheatsheet

## Quick start
1. Install dependencies:
   ```bash
   pip install flask requests
   ```
2. Run a sample:
   ```bash
   python SAMPLES/sample1.py
   ```

## Key concepts
- **Offset pagination**: Use `page` and `size` query parameters to fetch slices of results.
- **Cursor pagination**: Use an opaque cursor token to fetch the next page.
- **Stateless clients**: Pass paging parameters on each request.

## Notes
- The sample scripts start a local Flask server on a random free port and shut it down after the request.
- For production APIs, include metadata like `total`, `has_more`, or `next_cursor`.
