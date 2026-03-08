# sample3.py
# In-place quick sort using Lomuto partition

def quick_sort_inplace(arr, low=0, high=None):
    if high is None:
        high = len(arr)-1
    if low < high:
        p = partition(arr, low, high)
        quick_sort_inplace(arr, low, p-1)
        quick_sort_inplace(arr, p+1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

if __name__ == '__main__':
    data = [10,7,8,9,1,5]
    quick_sort_inplace(data)
    print('in-place sorted', data)
