# Problem 88

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if m == 0:
            while 0 in nums1:
                nums1.remove(0)
                
            for num in nums2:
                nums1.append(num)

        else:
            while nums1[-1] == 0  and len(nums1) > m:
                nums1.pop()

            for num in nums2:
                for i in range(len(nums1)):
                    if num < nums1[i]:
                        nums1.insert(i, num) 
                        break
                    elif num > nums1[-1] or num == nums1[-1]:
                        nums1.append(num)
                        break
                    elif len(nums1) == 0:
                        nums1.append(num)
                        break
        """
        Do not return anything, modify nums1 in-place instead.
        """

















# while nums1[-1] == 0 and len(nums1) > m:
#     nums1.pop()
#     if len(nums1) == 0:
#         break

# for num in nums2:
#     if len(nums1) == 0:
#         nums1.append(num)
#     else:
#         for i in range(len(nums1)):
#             if num < nums1[i]:
#                 nums1.insert(i, num) 
#                 break
#             elif num > nums1[-1] or num == nums1[-1]:
#                 nums1.append(num)
#                 break




print(nums1)