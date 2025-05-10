# Problem 168

columnNumber = 701

final = ''

while columnNumber > 0:
    char_N = (columnNumber - 1 )% 26
    char = chr(ord('A') + char_N)
    final = char + final
    columnNumber = (columnNumber - 1) // 26


print(final)