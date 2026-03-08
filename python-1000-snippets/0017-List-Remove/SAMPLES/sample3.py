# sample3.py
# Use list comprehension to filter out unwanted values.

def main():
    values = [1, 2, 3, 2, 4]
    filtered = [x for x in values if x != 2]
    print("Filtered list:", filtered)

if __name__ == '__main__':
    main()

