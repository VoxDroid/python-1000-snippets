# sample1.py
# Classify age into adult/teenager/child using if/elif/else

def classify_age(age):
    if age >= 18:
        return "You are an adult."
    elif age >= 13:
        return "You are a teenager."
    else:
        return "You are a child."

if __name__ == '__main__':
    try:
        age = int(input("Enter your age: "))
    except ValueError:
        print("Invalid number")
    else:
        print(classify_age(age))

