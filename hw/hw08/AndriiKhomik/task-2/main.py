import re


def validate_password():
    password = input('Please, enter password: ')
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@$#])[A-Za-z0-9@$#]{6,16}$'

    isValid = re.match(pattern, password)

    if isValid:
        print('Access allowed')
    else:
        print('Access denied')


validate_password()
