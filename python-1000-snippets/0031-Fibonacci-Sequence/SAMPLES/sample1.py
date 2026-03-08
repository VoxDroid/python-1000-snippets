# sample1.py
# Iterative Fibonacci sequence generator.

def fibonacci(n):
    seq = []
    for i in range(n):
        if i < 2:
            seq.append(i)
        else:
            seq.append(seq[i-1] + seq[i-2])
    return seq

if __name__ == '__main__':
    n = int(input("Enter number of terms: "))
    print(fibonacci(n))

