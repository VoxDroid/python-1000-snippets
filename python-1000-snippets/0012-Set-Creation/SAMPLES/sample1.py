# sample1.py
# Use a set to remove duplicates from a list.

def unique_list(lst):
    return list(set(lst))

if __name__ == '__main__':
    data = [1, 2, 2, 3, 4, 4, 5]
    print("Original:", data)
    print("Unique:", unique_list(data))

