__all__ = ["create_admin"]

def create_admin(name, password):
    print(f"Admin {name} created.")

def delete_admin(name, password):
    print(f"You want to delete admin {name}. Enter 'DELETE {name}' to confirm.")
    confirmation = input("Confirm: ")
    if confirmation == ("DELETE " + name):
        print(f"Admin {name} deleted.")
    else:
        print("Error.")