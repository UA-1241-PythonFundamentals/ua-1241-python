#Task2.
#Write a Python program to check the validity of a password (input from users).
#Validation :
#At least 1 letter between [a-z] and 1 letter between [A-Z].
#At least 1 number between [0-9].
#At least 1 character from [$#@].
#Minimum length 6 characters.
#Maximum length 16 characters.

#Install /// pip install password-validator ///
from password_validator import PasswordValidator
# Create a schema
schema = PasswordValidator()
# Add properties to it
schema \
    .min(6)\
    .max(16)\
    .has().uppercase() \
    .has().lowercase() \
    .has().no().spaces() \
    .has().symbols() \
    .has().digits() \

user_password = input("Enter your password:")

if schema.validate(user_password):
    print("Password correct!")
else:
    print("Read validation and try again!")
