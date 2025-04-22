# Problem 35

nums = [1,3,5,6]
target = 2

left, right = 0, len(nums) - 1

if target in nums:
    print(nums.index(target))

else:
    if nums[-1] < target:
        nums.append(target)
        print(nums.index(target))
    
    elif nums[0] > target:
        nums.insert(0, target)
        print(nums.index(target))

    else:
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        print(left)