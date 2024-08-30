__all__ = ["create_user"]

def create_user(name, age, email):
    print(f"User {name} created")

def change_user_info(name):
    print("Choose, what kind of info you want to change:"
          " \n 1) user name - 'name' \n 2) user age - 'age' \n 3) user email - 'email'")
    choise = input("Your choise here: ")
    match choise:
        case "name":
            new_name = input("Enter new name: ")
            print(f"User name changed to {new_name}")
        case "age":
            new_age = input("Enter new age: ")
            print(f"Age of user {name} changed to {new_age}")
        case "email":
            new_email = input("Enter new email: ")
            import re
            if re.match("[a-z]+[A-Z]*[.]*\d*@.{3,}[.].{3}", new_email):
                print(f"Email for user {name} changed.")
            else:
                print("Invalid email.")
        case _:
            print("Unknown option.")

def delete_user(name):
    print(f"You want to delete user {name}. Enter 'DELETE {name}' to confirm.")
    confirmation = input("Confirm: ")
    if confirmation == "DELETE " + name:
        print(f"User {name} deleted.")
    else:
        print("Error.")
