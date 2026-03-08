# sample2.py
# Recursive binary search implementation

def binary_search_rec(arr, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_rec(arr, target, mid+1, right)
    else:
        return binary_search_rec(arr, target, left, mid-1)

if __name__ == '__main__':
    arr = [2,4,6,8,10]
    print('search 6 ->', binary_search_rec(arr, 6, 0, len(arr)-1))
    print('search 5 ->', binary_search_rec(arr, 5, 0, len(arr)-1))
