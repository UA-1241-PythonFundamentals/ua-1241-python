a=input()
def num(f):
    r={}
    for i in f:
        if i not in r:
            r[i]=f.count(i)
    return r

print(num(a))