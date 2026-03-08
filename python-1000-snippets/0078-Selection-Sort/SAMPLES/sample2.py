# sample2.py
# Selection sort descending by selecting max

def selection_sort_desc(arr):
    n = len(arr)
    for i in range(n):
        max_idx = i
        for j in range(i+1, n):
            if arr[j] > arr[max_idx]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    return arr

if __name__ == '__main__':
    data = [3, 1, 4, 1, 5, 9]
    print('descending', selection_sort_desc(data))
