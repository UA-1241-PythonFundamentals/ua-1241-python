# Jenny's secret message
def greetings(name):
    if name == "Johny":
        return "Hi, dear John"
    else:
        return "Hello, " + name
    
# Simple: Find The Distance Between Two Points
def distance(x1, y1, x2, y2):
    return round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5, 2)

#No yelling!
def filter_words(s):
  return ' '.join(s.split()).capitalize()

#Convert a Number to a String!
def intToStr(i):
    return str(i)

#Reversing Words in a String
def reversed(s):
    words = s.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

#Reverse List Order
def reversed_list(l):
    return l[::-1]

#Multiples of 3 or 5
def multipliers(i):
    if i <=0:
        return 0
    else:
        nums = 8
        for n in range(6,i):
            if (n%3==0) or (n%5==0):
                nums +=n
        return nums
    
#Will you make it?
def pump(i):
    if i<=50:
        return True
    else:
        return False

#Banjo
def banjo(s):
    import re
    name = re.search("^r", s.lower())
    print(f"Are {s} playing banjo?")
    if name:
        return f"{s} plays banjo"
    else:
        return f"{s} does not play banjo"

#Convert boolean values to strings 'Yes' or 'No'.
def boolean_convert(b):
    if b:
        return "Yes"
    else:
        return "No"

#sheeps
def sheeps(s):
    return s.count(True)

#tail
def tail(body, tail):
     return body[-1] == tail