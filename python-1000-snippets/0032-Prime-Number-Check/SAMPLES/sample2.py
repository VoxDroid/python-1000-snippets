# sample2.py
# List all prime numbers up to n.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    n = int(input("Enter limit: "))
    primes = [i for i in range(2, n+1) if is_prime(i)]
    print("Primes:", primes)

