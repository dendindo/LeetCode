# Problem 14

strs = ["dog","racecar","car"]

first = strs[0]

for index in range(len(strs)):
    word = strs[index]
    while not word.startswith(first):
        first = first[:-1]
        if not first:
            break
            


print(first)
