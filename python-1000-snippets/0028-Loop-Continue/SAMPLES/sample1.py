# sample1.py
# Skip negative numbers when printing a list.

def main():
    nums = [-1, 0, 5, -2, 3]
    for n in nums:
        if n < 0:
            continue
        print(n)

if __name__ == '__main__':
    main()

