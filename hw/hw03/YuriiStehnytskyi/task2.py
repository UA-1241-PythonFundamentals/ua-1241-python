number = 999
product = 1
for digit in str(number):
    product *= int(digit)

reverse_number = int(str(number)[::-1])

sorted_digits = ''.join(sorted(str(number)))

print(f"Product of digits: {product}")
print(f"Reversed number: {reverse_number}")
print(f"Sorted digits: {sorted_digits}")