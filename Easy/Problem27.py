# Problem 27

nums = [3,2,2,3]
val = 3

for num in nums:
    if num == val:
        nums.remove(num)
        nums.append(num)
    else:
        continue

print(nums)
print(len(nums) - nums.count(val))