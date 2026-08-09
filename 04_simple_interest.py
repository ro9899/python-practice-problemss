# Python Program for Simple Interest

# Formula:
# Simple Interest = (P * T * R) / 100


# Method 1: Using Function
def simple_interest(p, t, r):
    return (p * t * r) / 100


p = 1000
t = 2
r = 5

result = simple_interest(p, t, r)

print("Simple Interest:", result)


# Method 2: Using Lambda Function
si = lambda p, t, r: (p * t * r) / 100

print("Simple Interest:", si(1000, 2, 5))


# Method 3: Using Direct Formula
p = 1000
t = 2
r = 5

result = (p * t * r) / 100

print("Simple Interest:", result)
