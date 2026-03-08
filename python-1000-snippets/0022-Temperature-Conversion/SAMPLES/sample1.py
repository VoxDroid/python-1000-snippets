# sample1.py
# Basic temperature conversion using user input.

def convert_temperature(value, unit):
    if unit == "C":
        return (value * 9/5) + 32
    elif unit == "F":
        return (value - 32) * 5/9
    else:
        return "Invalid unit"

if __name__ == '__main__':
    value = float(input("Enter temperature: "))
    unit = input("Enter unit (C or F): ").upper()
    result = convert_temperature(value, unit)
    print(f"Result: {result} {'F' if unit == 'C' else 'C'}")

