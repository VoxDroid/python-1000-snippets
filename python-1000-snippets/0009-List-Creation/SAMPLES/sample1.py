# sample1.py
# Manage a simple shopping list: add, remove, display.

def main():
    shopping = []
    shopping.append("milk")
    shopping.append("bread")
    shopping.append("eggs")
    print("Initial list:", shopping)
    shopping.remove("bread")
    print("After removing bread:", shopping)
    shopping[0] = "almond milk"
    print("After modification:", shopping)

if __name__ == '__main__':
    main()

