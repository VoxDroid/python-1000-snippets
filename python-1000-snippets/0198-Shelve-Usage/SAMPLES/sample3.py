# sample3.py
import shelve
with shelve.open("mystore") as db:
    db["user1"]["age"] = 26
    db.sync()
print("updated age in db")

