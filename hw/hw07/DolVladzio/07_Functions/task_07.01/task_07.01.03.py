#Task_3
user_input = input("Write a word: ")

def userWord(user_input):
    list_for_letters = []
    
    for x in user_input:
        if not any(f"{x}:" in s for s in list_for_letters):
            letter_count = user_input.count(x)
            list_for_letters.append(f"{x}: {letter_count} time(-s)")
    
    print(list_for_letters)

userWord(user_input)
#==========================================