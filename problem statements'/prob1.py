def reverse_three_digit_number(num):

    units = num % 10
    tens = (num // 10) % 10
    hundreds = num // 100
    

    reversed_num = (units * 100) + (tens * 10) + hundreds
    return reversed_num

# Test Case
input_num = 483
output_num = reverse_three_digit_number(input_num)
print(f"Input: {input_num}")
print(f"Output: {output_num}")