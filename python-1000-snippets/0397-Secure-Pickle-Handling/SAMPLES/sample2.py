
# sample2.py
# Restrict unpickling by overriding the class lookup.

import io
import pickle

class SafeUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        # Only allow safe built-in types.
        if module == "builtins" and name in {"dict", "list", "str", "int", "float", "bool", "NoneType"}:
            return super().find_class(module, name)
        raise pickle.UnpicklingError(f"Global '{module}.{name}' is not allowed")

def main() -> None:
    data = {"a": 1, "b": 2}
    blob = pickle.dumps(data)

    try:
        unpickler = SafeUnpickler(io.BytesIO(blob))
        restored = unpickler.load()
        print("Restored safely:", restored)
    except pickle.UnpicklingError as e:
        print("Unpickling error:", e)

if __name__ == "__main__":
    main()
