# sample2.py
# Metaclass that automatically registers its subclasses

class RegistryMeta(type):
    registry = {}

    def __new__(cls, name, bases, attrs):
        new_cls = super().__new__(cls, name, bases, attrs)
        if name != "Base":
            cls.registry[name] = new_cls
        return new_cls


class Base(metaclass=RegistryMeta):
    pass


class PluginA(Base):
    pass


class PluginB(Base):
    pass


def main():
    print("Registered plugins:", list(RegistryMeta.registry.keys()))


if __name__ == "__main__":
    main()
