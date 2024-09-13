def count_char(argstr:str):
    dict_char = {}
    for char in argstr:
        x=char
        y=argstr.count(char)
        dict_char[x]= y
    print(dict_char)


count_char('hello')