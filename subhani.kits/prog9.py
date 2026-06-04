# Read three integer values
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# Find the middle number
if (a > b and a < c) or (a < b and a > c):
    middle = a
elif (b > a and b < c) or (b < a and b > c):
    middle = b
else:
    middle = c

print("Middle number =", middle)