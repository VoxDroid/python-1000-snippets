# sample2.py
# Batch convert a list of Celsius values to Fahrenheit.

def convert_c_to_f(c):
    return (c * 9/5) + 32

if __name__ == '__main__':
    temps_c = [0, 20, 100]
    temps_f = [convert_c_to_f(t) for t in temps_c]
    print("Celsius:", temps_c)
    print("Fahrenheit:", temps_f)

