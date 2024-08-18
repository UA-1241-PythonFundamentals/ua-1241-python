
def count_letter(my_word):
    """A function that calculates the number of characters included in given string""" 
    result={}
    for i in range(len(my_word)):

        add_letter_to_dict(my_word[i], result)

    return result



def add_letter_to_dict(letter, dict):
    if letter in dict:
        dict[letter] += 1
    else:
        dict[letter] = 1

print (count_letter('hello'))
print (count_letter('pinapple'))
