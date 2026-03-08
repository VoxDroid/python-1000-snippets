# sample2.py
# build a comma-separated list from user input

def main():
    items = []
    for _ in range(3):
        item = input("Enter item: ")
        items.append(item)
    result = ", ".join(items)
    print("You entered:", result)

if __name__ == '__main__':
    main()

