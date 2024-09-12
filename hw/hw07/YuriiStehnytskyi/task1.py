def largest_number(num1, num2):
    """
    This function takes two numbers as input and returns the larger number.
    
    Parameters:
    num1: First number
    num2: Second number
    
    Returns:
    The larger of the two numbers
    """
    if num1 > num2:
        return num1
    else:
        return num2

# Example usage:
print(largest_number(5, 10))