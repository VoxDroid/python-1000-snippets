# 0370-Virtual-Proxy Cheatsheet

- Proxy defers creation of an expensive object until it is needed.
- Proxy can also add access control, caching, or logging.
- Keep proxy interface identical to real subject for transparency.
- Ensure proxy is thread-safe if used in concurrent contexts.
