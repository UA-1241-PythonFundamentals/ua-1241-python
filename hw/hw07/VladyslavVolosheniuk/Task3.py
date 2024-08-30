#Task3. Write a function that calculates the number of characters
#included in a given string
#• input: "hello"
#• output: {"h":1, "e":1,"l":2,"o":1}
def count_characters(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
result = count_characters("hello")
print(result)