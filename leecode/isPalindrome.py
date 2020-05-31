class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

        示例 1:

        输入: 121
        输出: true
        """
        if x < 0:
            return False
        elif x== 0:
            return True
        else:
            is_pal = False
            num =x
            num_r = 0
            while num>0:
                temp = num%10
                
                num_r = num_r*10 + temp
                
                num = int(num/10)
            if num_r == x:
                is_pal = True

        return is_pal
#print(Solution().isPalindrome(10))
    def isPalindrome_better(self, x: int) -> bool:
        x = str(x)
        y=x[::-1]

        return x==y
#print(Solution().isPalindrome_better(10))