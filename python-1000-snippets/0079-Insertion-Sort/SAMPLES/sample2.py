# sample2.py
# Show performance on nearly sorted list

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
    almost = [1,2,3,5,4,6,7]
    print('almost sorted before', almost)
    print('after', insertion_sort(almost))
