a=int(input())
b=int(input())

class polygon:
    def __init__(self, w=0,h=0):
        self.width = w
        self.height = h
        self.area=w*h

class rectangle(polygon):
    pass

pr = rectangle(a,b)
print(pr.area)