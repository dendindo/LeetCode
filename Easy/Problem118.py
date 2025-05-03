# Problem 118

numRows = 5



if numRows == 0:
    print([[]])

if numRows == 1:
    print([[1]])

else:
    list = [[1], [1,1]]
    for i in range(2, numRows):
        templist = [1]
        for x in range(len(list[-1]) - 1):
            templist.append(list[-1][x] + list[-1][x+1])
        
        templist.append(1)
        list.append(templist)


    print(list)


