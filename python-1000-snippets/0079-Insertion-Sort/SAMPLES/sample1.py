# sample1.py
# Basic insertion sort on random list

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

if __name__ == '__main__':
    data = [9, 5, 1, 4, 3]
    print('before', data)
    print('after', insertion_sort(data))
