class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

        示例 1：

        输入: "babad"
        输出: "bab"
        注意: "aba" 也是一个有效答案。
        示例 2：

        输入: "cbbd
        """
        pass
        
    def _longestPalindrome(self,s):
        if len(s)<=1:
            return s
        if len(s) ==2:
            return s if s[0] == s[1] else s[0]
        def is_pali(l,r):
            while l>=0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            
            return s[l+1:r]
        le = ''
        for i in range(0,len(s)):
            sub = is_pali(i,i)
            if len(sub) > len(le):
                # i 附近是回文,奇数
                le = sub
            sub = is_pali(i,i+1)
            if len(sub) > len(le):
                # i 附近是回文,奇数
                le = sub
            
        return le 
# print(Solution()._longestPalindrome('cbbd'))
# print(Solution()._longestPalindrome('abb'))
# print(Solution()._longestPalindrome('ac'))

    def _longestPalindrome_eg(self, s: str) -> str:
        n = len(s)
        if n < 2 or s == s[::-1]:
            return s
        max_len = 1
        start = 0
        for i in range(1,n):
            even = s[i-max_len:i+1]
            odd = s[i-max_len-1:i+1]
            if i-max_len-1>=0 and odd == odd[::-1]:
                start = i-max_len-1
                max_len += 2
                continue
            if i-max_len>=0 and even == even[::-1]:
                start = i-max_len
                max_len += 1
        return s[start:start+max_len]