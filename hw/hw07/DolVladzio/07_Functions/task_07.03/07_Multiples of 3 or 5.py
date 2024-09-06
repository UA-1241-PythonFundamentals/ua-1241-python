def solution(number):
    result = 0
    
    i = 0
    
    while i < int(number):
        if i % 3 == 0 or i % 5 == 0:
            result += i
        
        elif i == 0:
            return 0
        
        i += 1
    return result
  