# sample3.py
import json
data = {"foo":"bar"}
with open("data.json","w") as f:
    json.dump(data,f)
with open("data.json") as f:
    print("from file", json.load(f))

