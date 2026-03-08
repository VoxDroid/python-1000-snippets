# sample2.py
# Create a list of even numbers between 1 and 10 using a for loop and append.

def main():
    evens = []
    for i in range(1, 11):
        if i % 2 == 0:
            evens.append(i)
    print(evens)

if __name__ == '__main__':
    main()

