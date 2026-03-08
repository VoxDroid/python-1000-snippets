# sample3.py
# Show difference between append and extend

def main():
    lst = [1, 2]
    lst.append([3, 4])
    print("after append", lst)
    lst = [1, 2]
    lst.extend([3, 4])
    print("after extend", lst)

if __name__ == '__main__':
    main()

