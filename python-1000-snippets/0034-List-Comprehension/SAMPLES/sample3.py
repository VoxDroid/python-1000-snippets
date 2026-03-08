# sample3.py
# Create multiplication table using nested comprehension.

def main():
    table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
    for row in table:
        print(row)

if __name__ == '__main__':
    main()

