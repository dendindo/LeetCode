# Problem 202

n = 19




list_n = list(str(n))

length = len(list_n)

temp = []
while n > 1:
    for i in range(length):
        list_n[i] = int(list_n[i])**2

    n = sum(list_n)
    list_n = list(str(n))
    length = len(list_n)
    if n in temp:
        return False
    else:
        temp.append(n)



return True


    

