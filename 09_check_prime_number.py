# Python Program to Check Prime Number


# Method 1: Using Flag Variable
n = 11

if n <= 1:
    print("Not a Prime Number")
else:
    prime = True

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            prime = False
            break

    if prime:
        print("Prime Number")
    else:
        print("Not a Prime Number")


# Method 2: Using SymPy isprime()
# Install first:
# pip install sympy

from sympy import isprime

n = 13

if isprime(n):
    print("Prime Number")
else:
    print("Not a Prime Number")


# Method 3: Using Sieve of Eratosthenes
def is_prime(n):
    if n < 2:
        return False

    prime = [True] * (n + 1)
    prime[0] = prime[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if prime[i]:
            for j in range(i * i, n + 1, i):
                prime[j] = False

    return prime[n]


print("Prime Number" if is_prime(31) else "Not a Prime Number")


# Method 4: Using Recursion
from math import sqrt


def check_prime(n, i):
    if n < 2:
        return False

    if i == 1:
        return True

    if n % i == 0:
        return False

    return check_prime(n, i - 1)


n = 13

if check_prime(n, int(sqrt(n))):
    print("Prime Number")
else:
    print("Not a Prime Number")
