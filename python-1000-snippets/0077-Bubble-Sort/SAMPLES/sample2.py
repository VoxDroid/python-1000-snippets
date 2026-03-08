# sample2.py
# Optimized bubble sort stops early if already sorted

def bubble_sort_opt(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    print('already sorted before', nums)
    print('after', bubble_sort_opt(nums))
    nums2 = [5,4,3,2,1]
    print('reverse before', nums2)
    print('after', bubble_sort_opt(nums2))
