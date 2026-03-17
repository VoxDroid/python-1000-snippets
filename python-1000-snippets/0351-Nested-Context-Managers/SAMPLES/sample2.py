# sample2.py
# Manage multiple resources dynamically with ExitStack

from contextlib import ExitStack


def main():
    resources = ["A", "B", "C"]
    with ExitStack() as stack:
        for name in resources:
            stack.enter_context(_dummy_resource(name))
        print("Inside stacked contexts")


@contextmanager
def _dummy_resource(name):
    print(f"enter {name}")
    try:
        yield
    finally:
        print(f"exit {name}")


if __name__ == "__main__":
    main()
