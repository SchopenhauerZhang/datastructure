class Solution:
    def reverse(self, x: int) -> int:
        """
        给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

        示例 1:

        输入: 123
        输出: 321
        """
        rev = 0
        num = abs(x)

        while num >0:
            temp = num%10
            rev = rev*10 +temp
            num = num // 10
        
        if x < 0 and rev <= 2147483647:
            return 0-rev
        elif x > 0 and rev < 2147483647:
            return rev
        else:
            return 0

    def reverse_(self, x: int) -> int:
        negative_flag = 1
        if x < 0:
            x = abs(x)
            negative_flag = -1
        res = tmp = 0
        while x:
            tmp = x % 10
            x = x//10
            res = res*10 + tmp
        result = negative_flag*res
        return result if -2**31 < result < 2**31-1 else 0
        
print(Solution().reverse(1534236469))