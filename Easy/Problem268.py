# Problem 268 - Missing Number

nums = [0,1]

n = len(nums)
print(n)
for i in range(n+1):
    if i in nums:
        continue
    else:
        print(f'{i} not in LIST')