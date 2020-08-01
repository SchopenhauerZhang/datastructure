import collections
from collections import Counter
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
    
    def longestPalindrome_409(self, s: str) -> int:
        """
            给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。

            在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。

            注意:
            假设字符串的长度不会超过 1010。

            示例 1:

            输入:
            "abccccdd"

            输出:
            7

            解释:
            我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/longest-palindrome
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not s or len(s) <= 2:
            if not s:
                return 0
            s= list(s)
            return 2 if len(s) ==2 and s[0] == s[1] else 1
        
        _s = Counter(s)
        l = 0
        for i in _s:
            if _s[i] %2==0:
                l += _s[i]
            else:
                l += (_s[i] //2)*2
            

        return l+1 if l < len(s) else l

# print(Solution().longestPalindrome_409('abccccdd'))
# print(Solution().longestPalindrome_409('ccc'))

    def _longestPalindrome_409_eg(self, s: str) -> int:
        if not s:
            return 0
        dic = collections.Counter(s)
        flag = 0
        ans = 0
        for item in dic:
            if dic[item]&1:
                flag = 1
            ans += (dic[item]//2)*2
        return ans+flag
