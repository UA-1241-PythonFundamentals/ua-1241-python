
class CustomException(Exception):
    def __init__(self, data):
        self.data = data
        super().__init__(self.data)
        

DAYS_OF_WEEK = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}

def input_number():

    num = None

    try:
        
        try:
            num = int(input("Enter number: "))
        except ValueError:
            raise ValueError("You haven't entered number")    

        
        if num < 1 or num > 7:
            raise ValueError("Number must be between 1 and 7")

        return DAYS_OF_WEEK[num] 

    except Exception as e:  #catch all exceptions
        raise CustomException(e) 
    



try:
    print(input_number())
except Exception as e:
    print(e)