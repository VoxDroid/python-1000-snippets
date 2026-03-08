# sample3.py
# Bottom-up (iterative) merge sort

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:]); result.extend(right[j:])
    return result

def merge_sort_iter(arr):
    width = 1
    n = len(arr)
    while width < n:
        for i in range(0, n, 2*width):
            left = arr[i:i+width]
            right = arr[i+width:i+2*width]
            arr[i:i+2*width] = merge(left, right)
        width *= 2
    return arr

if __name__ == '__main__':
    arr = [5,2,4,6,1,3]
    print('iter sorted', merge_sort_iter(arr.copy()))
