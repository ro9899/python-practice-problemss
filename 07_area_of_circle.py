# Python Program to Find Area of a Circle

# Formula:
# Area = pi * r^2


# Method 1: Using math.pi
import math

r = 5

area = math.pi * (r ** 2)

print("Area of Circle:", area)


# Method 2: Using math.pow()
r = 5

area = math.pi * math.pow(r, 2)

print("Area of Circle:", area)


# Method 3: Using NumPy
import numpy as np

r = 5

area = np.pi * (r ** 2)

print("Area of Circle:", area)


# Method 4: Using Hardcoded PI
PI = 3.142

r = 5

area = PI * (r * r)

print("Area of Circle:", area)
