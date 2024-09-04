
class CustomException(Exception):
    def __init__(self, data):
        self.data = data
        super().__init__(self.data)
        

def input_age():

    age = None

    try:
        
        try:
            age = int(input("Enter your age: "))
        except ValueError:
            raise ValueError("You haven't entered number")    

        
        if age < 0:
            raise ValueError("Age must be more than zero")

        
        if age % 2 == 0:
            return "Age is even"
        return "Age is odd" 


    except Exception as e:  #catch all exceptions
        raise CustomException(e) 
    

try:
    print(input_age())
except Exception as e:
    print(e)
