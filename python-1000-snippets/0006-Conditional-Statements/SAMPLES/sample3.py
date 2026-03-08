# sample3.py
# Assign letter grade based on score

def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

if __name__ == '__main__':
    try:
        s = float(input("Enter score 0-100: "))
    except ValueError:
        print("Invalid score")
    else:
        print("Grade:", grade(s))

