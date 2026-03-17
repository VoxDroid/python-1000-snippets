# sample3.py
# Using mixins to add reusable behavior

class JsonMixin:
    def to_json(self):
        import json

        return json.dumps(self.__dict__)


class ReprMixin:
    def __repr__(self):
        return f"<{self.__class__.__name__} {self.__dict__}>"


class User(JsonMixin, ReprMixin):
    def __init__(self, name, email):
        self.name = name
        self.email = email


def main():
    u = User("Alice", "alice@example.com")
    print(u)
    print(u.to_json())


if __name__ == "__main__":
    main()
