# Task 3. Write a function that calculates the number of characters
# included in a given string

def charcounter(str):
    str = list(str)
    res = {}
    for char in str:
        res[char] = str.count(char)
    print(res)

charcounter("hello")