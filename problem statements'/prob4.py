# Input number
num = 472

# Extract each digit mathematically
first_digit = num // 100
middle_digit = (num // 10) % 10
last_digit = num % 10

# Reconstruct the number with the first and last digits swapped
swapped_num = (last_digit * 100) + (middle_digit * 10) + first_digit

# Output the result
print("Input:")
print(num)
print("\nOutput:")
print(swapped_num)