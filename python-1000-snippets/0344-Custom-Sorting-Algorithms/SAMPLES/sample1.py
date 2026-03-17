# sample1.py
# Selection sort implementation

def selection_sort(arr):
    arr = list(arr)
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def main():
    data = [5, 2, 9, 1, 5, 6]
    print("before:", data)
    print("after:", selection_sort(data))


if __name__ == "__main__":
    main()
