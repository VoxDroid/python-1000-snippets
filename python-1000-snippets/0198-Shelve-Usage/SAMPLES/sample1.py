# sample1.py
import shelve
with shelve.open("mystore") as db:
    db["user1"] = {"name":"Alice","age":25}
with shelve.open("mystore") as db:
    print("User1:", db["user1"])

