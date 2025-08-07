# Problem 345

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

s = "IceCreAm"

word = list(s)

temp = []
for letter in word:
    if letter in vowels:
        temp.insert(0, letter)
    else:
        continue

# temp.reverse()
print(temp)
# j = 0
# for index in range(len(word)):
#     x = word[index]
#     if x in temp:
#         word.pop(index)
#         word.insert(index, temp[j])
#         j += 1

#     else:
#         continue

# final = ''
# for a in word:
#     final += a

# print(final)




