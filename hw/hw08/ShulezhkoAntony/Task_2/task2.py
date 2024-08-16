import re
def password_checker(password):
  if not re.search(r"[a-z]", password):
    return False
  if not re.search(r"[A-Z]", password):
    return False
  if not re.search(r"[$#@]", password):
    return False
  if not re.search(r"[0-9]", password):
    return False
  if len(password) < 6 or len(password) > 16:
    return False
  return True

password = input("Enter your password: ")
if password_checker(password):
    print("Password is valid.")
else:
    print("Password is invalid.")