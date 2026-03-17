# sample3.py
# Register a virtual subclass with ABCs

from abc import ABC, abstractmethod


class Serializer(ABC):
    @abstractmethod
    def serialize(self, obj):
        pass


class JsonSerializer:
    def serialize(self, obj):
        import json

        return json.dumps(obj)


Serializer.register(JsonSerializer)


def main():
    print("Is registered:", issubclass(JsonSerializer, Serializer))
    print("Instance check:", isinstance(JsonSerializer(), Serializer))
    print("output:", JsonSerializer().serialize({"a": 1}))


if __name__ == "__main__":
    main()
