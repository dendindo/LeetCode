# Problem 119

rowIndex = 3

if rowIndex == 0:
    print([1])

if rowIndex == 1:
    print([1,1])

else:
    list = [[1], [1,1]]
    for i in range(2, rowIndex+1):
        templist = [1]
        for x in range(len(list[-1]) - 1):
            templist.append(list[-1][x] + list[-1][x+1])
        
        templist.append(1)
        list.append(templist)

    print(list[rowIndex])