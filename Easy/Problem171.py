# Problem 171

columnTitle = "ZY"


total_value = 0

prev = columnTitle[0]

for letter in columnTitle:
    total_value = total_value * 26
    value = ord(letter) - ord('A') + 1
    prev = letter
    total_value = total_value + value

print(total_value)