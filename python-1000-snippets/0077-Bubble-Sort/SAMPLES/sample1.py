# sample1.py
# Basic bubble sort on list of integers

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == '__main__':
    nums = [5, 3, 8, 1, 2]
    print('before', nums)
    print('after', bubble_sort(nums))
