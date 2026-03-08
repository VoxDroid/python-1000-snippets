# sample1.py
# naming convention enforcement (from README)

class NamingMeta(type):
    def __new__(cls, name, bases, attrs):
        for key in attrs:
            if not key.startswith("_") and not key[0].isupper():
                raise ValueError(f"Attribute '{key}' must start with uppercase")
        return super().__new__(cls, name, bases, attrs)

class MyClass(metaclass=NamingMeta):
    Name = "Test"
    Value = 42

if __name__ == '__main__':
    print(MyClass.Name, MyClass.Value)   
