# sample1.py
# Filter even numbers from a list

if __name__ == '__main__':
    nums = [1,2,3,4,5,6]
    evens = list(filter(lambda x: x%2==0, nums))
    print('original:', nums)
    print('evens:', evens)
