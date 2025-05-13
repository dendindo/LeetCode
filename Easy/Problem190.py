# Problem 190


n = 43261596


binar = bin(n)[2:]

binar = binar.zfill(32)

rev = binar[::-1]

final = int(rev, 2)

print(final)
