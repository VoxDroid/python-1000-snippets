# sample3.py
# Demonstrate instability with equal keys

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j][0] < arr[min_idx][0]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

if __name__ == '__main__':
    items = [(2,'a'), (1,'b'), (2,'c'), (1,'d')]
    print('before', items)
    print('after', selection_sort(items.copy()))
    # note order of comparable elements may change
