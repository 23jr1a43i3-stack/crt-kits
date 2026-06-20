# Input number
num = 246

first_digit = num // 100
middle_digit = (num // 10) % 10
last_digit = num % 10

digit_sum = first_digit + middle_digit + last_digit

digit_average = digit_sum // 3

# Output the result
print("Input:")
print(num)
print("\nOutput:")
print(digit_average)