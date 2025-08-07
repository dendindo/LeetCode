# Problem 350

nums1 = [3,1,2]
nums2 = [1,1]

u = []

if len(nums1) > len(nums2):
    for num in nums2:
        if num in nums1:
            if u.count(num) < nums1.count(num):
                u.append(num)
            else:
                continue
        else:
            continue
else:

    for num in nums1:
        if num in nums2:
            if u.count(num) < nums2.count(num):
                u.append(num)
            else:
                continue
        else:
            continue

print(u)
