# Problem 242 - anagram

s = "anagram"
t = "nagaram"

if len(s) != len(t):
    print('false')

ss = sorted(s)
tt = sorted(t)
print(sorted(s))
print(ss == tt)

