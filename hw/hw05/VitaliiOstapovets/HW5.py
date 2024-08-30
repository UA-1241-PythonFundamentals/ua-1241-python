#Task1
list_int = [0,1,2,3,4,5,6,7,8,9,10]
list_int2 = []
for i in list_int:
    list_int2.append(float(i))
list_int = list_int2
print(list_int)


#Task2
num = int(input('Until what number to display the list of Fibonacci numbers?'))
sum = None
fibn_list = []
for y in range(0,num):
    if y == 0:
        fibn_list.append(1)
    elif y == 1:
        fibn_list.append(1)
    elif y > 1:
        sum = fibn_list[y-2]+fibn_list[y-1]
        if sum > num:
            break
        else:
            fibn_list.append(sum)
print(fibn_list)

#Task3
rec_nb = int(input("Input number for recursion"))
if rec_nb == 0:
    recursion = 1
    print(f"recursion number {rec_nb}! = {recursion}")
elif rec_nb == 1:
    recursion = 1
    print(f"recursion number {rec_nb}! = {recursion}")
else:
    product_rcn = 1
    for o in range(1,rec_nb+1):
        product_rcn =product_rcn * o
    print(f"recursion number {rec_nb}! = {product_rcn}")
