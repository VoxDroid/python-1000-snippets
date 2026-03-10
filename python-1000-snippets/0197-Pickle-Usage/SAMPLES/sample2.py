# sample2.py
import pickle
data = [1,2,3]
b = pickle.dumps(data)
print("bytes length", len(b))
print("round-trip", pickle.loads(b))

