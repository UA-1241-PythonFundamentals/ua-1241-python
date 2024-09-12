def char_count(string):
    count_dict = {}
    
    for char in string:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
            
    return count_dict

print(char_count("hello"))  
