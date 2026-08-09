# Python Program for Compound Interest

# Formula:
# Amount = P * (1 + R / 100) ** T
# Compound Interest = Amount - P


# Method 1: Using Exponentiation Operator (**)
p = 1200
r = 5.4
t = 2

amount = p * (1 + r / 100) ** t
ci = amount - p

print("Compound Interest:", ci)


# Method 2: Using pow() Function
p = 10000
r = 10.25
t = 5

amount = p * pow((1 + r / 100), t)
ci = amount - p

print("Compound Interest:", ci)


# Method 3: Taking Input from User
p = float(input("Enter Principal Amount: "))
r = float(input("Enter Rate of Interest: "))
t = int(input("Enter Time in Years: "))

amount = p * (1 + r / 100) ** t
ci = amount - p

print("Compound Interest:", ci)


# Method 4: Using For Loop
p = 1200
r = 5.4
t = 2

amount = p

for i in range(t):
    amount = amount * (1 + r / 100)

ci = amount - p

print("Compound Interest:", ci)
