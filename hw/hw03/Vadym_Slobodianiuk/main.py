# Task #1 Find, Display and Replace text

philosophy = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

print(">>>>>>>>>>>>>>>> Start <<<<<<<<<<<<<<<<<")
print(">>>>>>>>>>>>>>>> Task 1 <<<<<<<<<<<<<<<<<\n")
# Task 1.1 Find Occurrences in Philosphy
print("Occurrences of 'better' is:", philosophy.lower().count("better"))
print("Occurrences of 'never' is:", philosophy.lower().count("never"))
print("Occurrences of 'is' is:", philosophy.lower().count("is"))

# Task 1.2 Display Text in Uppercase and replace I<>&
print("Modified text:\n\n", philosophy.upper().replace('I', '&'))

# Task 1.3 Int manipulations
print("\n>>>>>>>>>>>>>>>> Task 2 <<<<<<<<<<<<<<<<<\n")

number = 1234

product = 1
for digit in str(number):
    product *= int(digit)
print("Product of the digits is: ", product)

print("Reversed number: ", int(str(number)[::-1]))

print("Sorted digits: ", ''.join(sorted(str(number))))

print("\n>>>>>>>>>>>>>>>> Task 3 <<<<<<<<<<<<<<<<<\n")

# Interchange
a = 5
b = 10

a, b = b, a

print("After interchange, a:", a, "b:", b)
