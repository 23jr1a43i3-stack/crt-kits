
num = 572

last_digit = num % 10
middle_digit = (num // 10) % 10
first_digit = num // 100

digit_sum = first_digit + middle_digit + last_digit

print("Input:")
print(num)
print("\nOutput:")
print(digit_sum)