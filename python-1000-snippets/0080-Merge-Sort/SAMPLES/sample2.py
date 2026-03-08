# sample2.py
# Merge sort with key function for stability

def merge_sort(arr, key=lambda x: x):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid], key)
    right = merge_sort(arr[mid:], key)
    return merge(left, right, key)

def merge(left, right, key):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if key(left[i]) <= key(right[j]):
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:]); result.extend(right[j:])
    return result

if __name__ == '__main__':
    words = ['pear', 'apple', 'orange', 'kiwi']
    print('by length', merge_sort(words, key=len))
    print('builtin', sorted(words, key=len))
