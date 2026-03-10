# 0198-Shelve-Usage Cheatsheet

* `shelve.open('dbname')` returns dict-like object.
* Use `with` statement to auto-close.
* Keys must be strings; values pickled.
* `db.sync()` to flush to disk.
* Iterate over keys: `for k in db:`.
* Data stored in underlying dbm file (.db).

