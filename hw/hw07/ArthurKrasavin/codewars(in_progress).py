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