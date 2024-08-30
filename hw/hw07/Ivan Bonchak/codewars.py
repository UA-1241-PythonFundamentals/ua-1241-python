#Jenny has written a function that returns a greeting for a user. However, she's in love with Johnny, and would like to greet him slightly different. She added a special case to her function, but she made a mistake.
#Can you help her?
def f_name(name):
    if name == "Johnny":
        return "Hi my love"
    else:
        return f"Hi, {name}!"

print(f_name("Ivan"))
print(f_name("Johnny"))

#Given two ordered pairs calculate the distance between them. Round to two decimal places. This should be easy to do in 0(1) timing.
import math
def dist(point1,point2):
    x1,y1=point1
    x2,y2=point2
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return round(dist,2)

point1 = (3,4)
point2 =(12,90)
print(dist(point1,point2))

def filter_words(str):
    words = str.lower()
    result = ' '.join(words)
    return result.capitalize()


print(filter_words('HELLO CAN YOU HEAR ME'))        # Output: Hello can you hear me
print(filter_words('now THIS is REALLY interesting'))  # Output: Now this is really interesting
print(filter_words('THAT was EXTRAORDINARY!'))      # Output: That was extraordinary!
