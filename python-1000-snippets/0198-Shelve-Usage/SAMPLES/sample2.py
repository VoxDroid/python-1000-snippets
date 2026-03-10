# sample2.py
import shelve
with shelve.open("mystore") as db:
    for k in db:
        print("key", k, "=>", db[k])

