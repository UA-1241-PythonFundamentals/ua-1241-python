class MyError(Exception):
    def __init__(self, data):
        self.data = data

def check_odd_age(age):
    try:
        age = int(age)
        if age > 0:            
            if age %2 == 0:
                return "Entered age is even"
            else:
                return "Entered age is odd"
        elif age < 0:
            raise MyError("Error! Age is negative")    
    except (ValueError, TypeError):
        return "Error type: ValueError!"
    except MyError as e:
        return e
    

age = input("Enter your age: ")
print(check_odd_age(age))