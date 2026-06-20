# Input number
num = 684

# Extract each digit mathematically
first_digit = num // 100
middle_digit = (num // 10) % 10
last_digit = num % 10

# Find the largest digit using the built-in max() function
largest_digit = max(first_digit, middle_digit, last_digit)

# Output the result
print("Input:")
print(num)
print("\nOutput:")
print(largest_digit)