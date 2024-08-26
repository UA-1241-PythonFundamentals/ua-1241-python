def scan(string):
    
    res = {}

    for char in string:
        count =  string.count(char)
        res[char] = count

    return res

string = input("Enter a string to count repeated characters: ")

print(scan(string))