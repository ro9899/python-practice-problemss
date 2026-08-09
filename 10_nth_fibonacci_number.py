# Python Program for nth Fibonacci Number

# Fibonacci sequence:
# 0, 1, 1, 2, 3, 5, 8, 13, ...


# Method 1: Using Iteration
n = 7

a = 0
b = 1

for i in range(n):
    a, b = b, a + b

print("Fibonacci Number:", a)


# Method 2: Using Recursion
def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


n = 7

print("Fibonacci Number:", fibonacci(n))


# Method 3: Using List
n = 7

fib = [0, 1]

for i in range(2, n + 1):
    fib.append(fib[i - 1] + fib[i - 2])

print("Fibonacci Number:", fib[n])
