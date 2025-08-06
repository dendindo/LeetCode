# Problem 3

s = "dvdf"


# temp = []
# temp_strings = []
# if len(s) == 1:
#     print(1)
# else:
#     for char in s:
#         print("char:", char, "temp:", temp)
#         if char in temp:
#             temp_strings.append(len(temp))
#             temp = [char]
#         else:
#             temp.append(char)

#     temp_strings.append(len(temp))
#     temp_strings.sort()
#     if temp_strings:
#         print(temp_strings[-1])
#     else:
#         print(0)

temp = []
tempi = []
temp_strings = []
for i, char in enumerate(s):
    print(i, char)
    if char in temp:
        temp_strings.append(temp)
        index = temp.index(char)
        new = tempi[index]
    else:
        temp.append(char)
        tempi.append(i)