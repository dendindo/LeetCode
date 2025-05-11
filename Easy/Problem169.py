# Problem 169

nums = [2,2,1,1,1,2,2]


# SOLUTION 1

# dict = {}

# for num in nums:
#     if num in dict:
#         dict[num] += 1
#     else:
#         dict.update({num: 1})

# h_value = 0
# h_key = 0
# for key, value in dict.items():
#     if value > h_value:
#         h_value = value
#         h_key = key
#     else:
#         pass

# print(h_key)
# print(h_value)

# SOLUTION 2

# set = set(nums)

# print(set)


# high = 0
# hi_n = 0
# for num in set:
#     count = nums.count(num)
#     if count > high:
#         high = count
#         hi_n = num
#     else:
#         pass

# print(high)
# print(hi_n)


# SOLUTION 3

candidate = None
count = 0


for num in nums:
    if count == 0:
        candidate = num
        count = 1
    else:
        if num == candidate:
            count += 1
        else:
            count -= 1


print(candidate)