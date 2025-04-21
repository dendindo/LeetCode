# Problem 26

nums = [0,0,1,1,1,2,2,3,3,4]

i = 0

for num in nums:
    if num == nums[i]:
        pass
    else:
        i += 1
        nums[i] = num


print(i+1)
print(nums)


