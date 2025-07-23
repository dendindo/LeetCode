# Problem 283

nums = [0]

c = nums.count(0)
for i in range(c):
    nums.remove(0)
    nums.append(0)


print(nums)