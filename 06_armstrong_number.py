# Python Program to Check Armstrong Number

# Example:
# 153 = 1^3 + 5^3 + 3^3 = 153


# Method 1: Using Mathematical Approach
n = 153

t = n
p = len(str(n))
s = 0

while t > 0:
    d = t % 10
    s += d ** p
    t //= 10

if s == n:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")


# Method 2: Using String Conversion
n = 153

p = len(str(n))
s = sum(int(d) ** p for d in str(n))

if s == n:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")


# Method 3: Using map() and lambda
n = 153

p = len(str(n))
s = sum(map(lambda d: int(d) ** p, str(n)))

if s == n:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")


# Method 4: Using Recursion
n = 153
p = len(str(n))


def arm(x):
    if x == 0:
        return 0

    return (x % 10) ** p + arm(x // 10)


if arm(n) == n:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
