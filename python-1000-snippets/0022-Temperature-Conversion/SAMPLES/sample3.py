# sample3.py
# Interactive loop converting temperatures until user types 'quit'.

def convert(value, unit):
    if unit == 'C':
        return (value * 9/5) + 32
    elif unit == 'F':
        return (value - 32) * 5/9
    return None

if __name__ == '__main__':
    while True:
        inp = input("Enter temp and unit (e.g. 32 F) or 'quit': ")
        if inp.lower() == 'quit':
            break
        parts = inp.split()
        if len(parts) != 2:
            print("Invalid input")
            continue
        val, unit = parts
        try:
            val = float(val)
        except ValueError:
            print("Invalid number")
            continue
        unit = unit.upper()
        res = convert(val, unit)
        if res is None:
            print("Invalid unit")
        else:
            print(res)

