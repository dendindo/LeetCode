# Problem 219

nums = [1,0,1,1]
k = 1


        
seen = {}

for index, num in enumerate(nums):
    if num in seen:
        if abs(index - seen[num]) <= k:
            print('True')
            break
        else:
            seen[num] = index
    else:
        seen[num] = index
        
print('False')
            
        