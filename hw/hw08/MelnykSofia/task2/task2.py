from password_validator import PasswordValidator

# Створюємо схему перевірки пароля
schema = PasswordValidator()

# Налаштовуємо правила
schema \
    .min(8) \
    .max(16) \
    .has().uppercase() \
    .has().lowercase() \
    .has().digits() \
    .has().no().spaces()

# Перевірка пароля
password = input("Enter your password: ")
if schema.validate(password):
    print("Good!")
else:
    print("Not validate password!")
 