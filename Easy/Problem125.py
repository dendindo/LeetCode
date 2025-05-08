# Problem 125

s = " "


an = ''.join([char for char in s.lower() if char.isalnum()])

if an == an[::-1]:
    print('true')
else:
    print('false')
