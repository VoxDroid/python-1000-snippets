# sample3.py
# Demonstrate early return for input validation.

def process(value):
    if value is None:
        return "No value provided"
    return f"Processed {value}"

if __name__ == '__main__':
    print(process(None))
    print(process(42))

