# sample1.py
import pickle
data = {"name":"Bob", "scores":[90,85]}
with open("data.pkl","wb") as f:
    pickle.dump(data,f)
with open("data.pkl","rb") as f:
    print("Loaded:", pickle.load(f))

