# sample2.py
# Show worst-case behavior on already sorted input

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]  # bad pivot choice
    left = [x for x in arr[1:] if x < pivot]
    middle = [pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quick_sort(left) + middle + quick_sort(right)

if __name__ == '__main__':
    sorted_list = list(range(10))
    print('sorted input ->', quick_sort(sorted_list))
