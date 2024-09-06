def count_sheeps(sheep):
    count_sheeps = 0
    
    for x in sheep:
        if x == True:
            count_sheeps += 1
        else:
            continue
            
    return count_sheeps