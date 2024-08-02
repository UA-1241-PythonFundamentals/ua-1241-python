zen_text = (
    "Beautiful is better than ugly."
    "Explicit is better than implicit."
    "Simple is better than complex."
    "Complex is better than complicated."
    "Flat is better than nested."
    "Sparse is better than dense."
    "Readability counts."
    "Special cases aren't special enough to break the rules."
    "Although practicality beats purity."
    "Errors should never pass silently."
    "Unless explicitly silenced."
    "In the face of ambiguity, refuse the temptation to guess."
    "There should be one-- and preferably only one --obvious way to do it."
    "Although that way may not be obvious at first unless you're Dutch."
    "Now is better than never."
    "Although never is often better than *right* now."
    "If the implementation is hard to explain, it's a bad idea."
    "If the implementation is easy to explain, it may be a good idea."
    "Namespaces are one honking great idea -- let's do more of those!"
)

# counter of occurrences of "better", "never", "is"
print("Quantity of occurrances of the words: \n 1) better -", zen_text.count("better"),
      "\n 2) never -", zen_text.count("never"), " \n 3) is -", zen_text.count("is"))

# all zen text in uppercase
print(zen_text.upper())

# replacement of 'i' with '&'
print(zen_text.replace('i', '&'))

# work with four-digit number
num = int(input("Enter a four-digit number: "))
given_number = num
product = 1

# count the product of all the digits in the number
while (given_number != 0):
    product = product * (given_number % 10)
    given_number = given_number // 10

print("Product of the digits of your four-digit number is", product)

# reverse the number
given_number = num 
reversed_num = 0
while (given_number != 0):
    right_digit = given_number % 10
    reversed_num = reversed_num * 10 + right_digit
    given_number = given_number // 10

print("Reversed number is", reversed_num)

# sorted digits in the given number
sort = sorted(str(num))
print("Sorted digits in your number:", sort)

# interchange the values of two variables without using the third one
a = input("Enter the first variable: ")
b = input("Enter the second variable: ")

print(f"{a = }", f"{b = }")
a, b = b, a
print("Swapped variables: \n", f"{a = }", f"{b = }")
