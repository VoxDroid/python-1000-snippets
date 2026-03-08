# sample2.py
# Map a named function to convert Celsius to Fahrenheit

def c_to_f(c):
    return (c * 9/5) + 32

if __name__ == '__main__':
    ctemps = [0, 20, 37]
    ftemps = list(map(c_to_f, ctemps))
    print('Celsius:', ctemps)
    print('Fahrenheit:', ftemps)
