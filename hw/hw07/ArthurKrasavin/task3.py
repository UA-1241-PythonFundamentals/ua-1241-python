def num_of_char(str):
    count_dict = {}
    for c in str:
        if c in count_dict:
            count_dict[c] +=1
        else:
            count_dict[c] = 1
    return count_dict

print(num_of_char("hello"))