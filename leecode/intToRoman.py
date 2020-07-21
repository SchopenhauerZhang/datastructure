class Solution:
    def intToRoman(self, num: int) -> str:
        # https://leetcode-cn.com/problems/integer-to-roman/
        roman = {
            '1':'I',
            '5':'V',
            '10':'X',
            '50':'L',
            '100':'C',
            '500':'D',
            '1000':'M'
            }
        import math
        while num > 10:
            _len = len(num)
            num = num - math.pow(10,_len-1)

print(Solution().intToRoman(1994))
print(Solution().intToRoman(58))