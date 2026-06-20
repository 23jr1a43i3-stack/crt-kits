
num = 234

last_digit = num % 10
middle_digit = (num // 10) % 10
first_digit = num // 100

digit_product = first_digit * middle_digit * last_digit

# Output the result
print("Input:")
print(num)
print("\nOutput:")
print(digit_product)