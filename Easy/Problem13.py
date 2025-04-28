# Problem 13

class Solution:
    def romanToInt(self, s: str) -> int:

        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        total = 0
        sub = 0

        for i in range(len(list(s)) - 1):
            current = roman[s[i]]
            next = roman[s[i+1]]
            if current < next:
                total += next - current
                sub += next

            else:
                total += current

        total += roman[s[-1]]
        return total - sub

