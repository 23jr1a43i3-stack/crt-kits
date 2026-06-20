num = 684

first_digit = num // 100
middle_digit = (num // 10) % 10
last_digit = num % 10

smallest_digit = min(first_digit, middle_digit, last_digit)

print("Input:")
print(num)
print("\nOutput:")
print(smallest_digit)