# Problem 9

class Solution:
    def isPalindrome(self, x: int) -> bool:
        num1 = str(x)
        if num1 == num1[::-1]:
            return True
        else:
            return False