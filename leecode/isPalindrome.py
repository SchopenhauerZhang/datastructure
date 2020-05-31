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
    def isPalindrome_nums_str(self, s: str) -> bool:
        """
        给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

        说明：本题中，我们将空字符串定义为有效的回文串。
        """
        if not s:
            return True
        import re
        strs = s.lower().strip()
    
        strs = re.findall('[a-zA-Z0-9]',strs)
        if strs == strs[::-1]:
            return True
        return False

#print(Solution().isPalindrome_nums_str("A man, a plan, #$@!a canal: Panama"))
    def isPalindrome_nums_str_better(self, s: str) -> bool:
        alpha_filter = filter(str.isalnum,s)
        strs = "".join(alpha_filter)
        strs1=strs[::-1]
        if strs.upper()==strs1.upper():
            return True
        return False