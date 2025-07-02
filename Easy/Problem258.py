# Problem 258 - Add Digits

num = 0

print(list(str(num)))

prd = True

while prd:
    l = list(str(num))
    num = 0
    for n in l:
        num += int(n)
    print(f'New Num: {num}')
    if 10 > num > -1:
        prd = False
    

print(f'final num: {num}')