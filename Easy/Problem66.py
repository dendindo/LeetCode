# Problem 66

digits = [9]
number = int(''.join(map(str, digits)))
newnum = number + 1
final = [int(x) for x in list(str(newnum)) if x]
print(final)
