# sample2.py
# Search through list of strings

def linear_search(arr, target):
    for idx, val in enumerate(arr):
        if val == target:
            return idx
    return -1

if __name__ == '__main__':
    words = ['apple','banana','cherry']
    print('banana index', linear_search(words, 'banana'))
    print('orange index', linear_search(words, 'orange'))
