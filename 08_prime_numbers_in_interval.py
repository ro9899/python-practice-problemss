# Python Program to Print All Prime Numbers in an Interval

# Example:
# Range: 2 to 7
# Output: 2, 3, 5, 7


# Method 1: Using Sieve of Eratosthenes
x, y = 2, 7

primes = [True] * (y + 1)

# 0 and 1 are not prime
primes[0] = False
primes[1] = False

for i in range(2, int(y ** 0.5) + 1):
    if primes[i]:
        for j in range(i * i, y + 1, i):
            primes[j] = False

result = [i for i in range(x, y + 1) if primes[i]]

print("Sieve:", result)


# Method 2: Using Trial Division
x, y = 2, 7

result = []

for n in range(x, y + 1):

    if n <= 1:
        continue

    is_prime = True

    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        result.append(n)

print("Trial Division:", result)


# Method 3: Using SymPy
# Install first:
# pip install sympy

from sympy import primerange

x, y = 2, 7

primes = list(primerange(x, y + 1))

print("SymPy:", primes)


# Method 4: Using Naive Approach
x, y = 2, 7

result = []

for i in range(x, y + 1):

    if i <= 1:
        continue

    for j in range(2, i // 2 + 1):

        if i % j == 0:
            break

    else:
        result.append(i)

print("Naive:", result)
