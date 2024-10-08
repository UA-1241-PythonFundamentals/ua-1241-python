import re

pas = input("Пожалуйста, введите пароль длинной 6-16 символов обязательно с:\n"
            "- одной маленькой латинской буквой от a до z;\n"
            "- одой заглавной латинской буквой от A до Z;\n"
            "- одной цифрой от 0 до 9;\n"
            "- одним специальным символом: $#@\n"
            "Пароль: ")

if len(pas) < 6:
    print("Вы ввели слишком короткий пароль.")
elif len(pas) > 16:
    print("Вы ввели слишком длинный пароль.")
elif not re.search("[$@#]", pas):
    print("В пароле Вы не использовали специальный символ: $@#.")
elif not re.search("[0-9]", pas):
    print("Вы не использовали в пароле хотя бы одно число: 0-9.")
elif not re.search("[a-z]", pas):
    print("Вы не использовали в пароле хотя бы одну маленькую букву: a-z.")
elif not re.search("[A-Z]", pas):
    print("Вы не использовали в пароле хотя бы одну заглавную букву: A-Z.")
else:
    print("Ваш пароль принят.")