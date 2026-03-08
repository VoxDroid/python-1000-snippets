# sample1.py
# Search for a target value in a list and break when found.

def find_target(lst, target):
    for item in lst:
        if item == target:
            return True
    return False

if __name__ == '__main__':
    print(find_target([1,2,3,4], 3))
    print(find_target([1,2,3,4], 5))

