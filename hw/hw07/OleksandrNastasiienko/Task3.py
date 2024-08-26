string = input("Enter a string to count repeated characters: ")

res = {}

for char in string:
    count =  string.count(char)
    res[char] = count

print(res)