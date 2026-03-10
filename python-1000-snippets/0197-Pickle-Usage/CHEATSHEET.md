# 0197-Pickle-Usage Cheatsheet

* Serialize objects: `pickle.dump(obj, file)` or `pickle.dumps(obj)`.
* Deserialize: `pickle.load(file)` or `pickle.loads(bytes)`.
* Choose protocol version; default is highest.
* Warning: unpickle untrusted data is unsafe.
* Use `with open(..., 'wb')` for safety.

