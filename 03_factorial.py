# Factorial of a Number in Python

# Method 1: Using math.factorial()
import math

n = 6

print(math.factorial(n))


# Method 2: Using NumPy
import numpy as np

n = 6

if n >= 0:
    print(np.prod(range(1, n + 1)))
else:
    print("Factorial is not defined for negative numbers")


# Method 3: Using For Loop
n = 6

if n < 0:
    print("Factorial is not defined for negative numbers")
else:
    f = 1

    for i in range(1, n + 1):
        f *= i

    print(f)


# Method 4: Using Recursive Function
def fact(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    return 1 if n <= 1 else n * fact(n - 1)


print(fact(6))
print(fact(-3))
