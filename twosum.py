# Problem 1

nums = [1,3,3]
target = 6
result = []
found = False

while not found:
    for num in nums:
        nums2 = nums.copy()
        nums2.remove(num)
        for num2 in nums2:
            if num2 + num == target:
                id1 = nums.index(num)
                result.append(id1)
                templist = nums[id1+1:]
                id2 = id1 + 1 + templist.index(num2) if num == num2 else nums.index(num2)

                result.append(id2)
                found = True
                break
        if found:
            break
        


print(result)

enumerate       