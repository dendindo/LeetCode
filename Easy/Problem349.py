# Problem 349

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

u = []
for num in nums1:
    if num in u:
        continue
    elif num in nums2:
        u.append(num)
    else:
        continue

print(u)
