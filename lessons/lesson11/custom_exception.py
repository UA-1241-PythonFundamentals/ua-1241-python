class CustomError(Exception):
    def __init__(self, data):
        self.data = data
    def __str__(self):
        return repr(self.data)
    
class CustomError2(Exception):
    pass
    

def read_int(text):
    result = input(text)
    if not result.isdigit():
        raise CustomError("my error, value is not number")
    return int(result)


try:
    value = read_int("Enter a positive integer: ")
except CustomError as e:
    print(type(e), e)
else:
    print(f"{value=}")