class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
            给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。

            示例 1:

            输入: "aba"
            输出: True
            示例 2:

            输入: "abca"
            输出: True
            解释: 你可以删除c字符。
            注意:

            字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/valid-palindrome-ii
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not s or len(s) <= 3:
            s = list(s)
            return True if not s or len(s) == 1 or (len(s)==3 and s[0] == s[2] ) or (len(s) ==2 ) else False
        l,r = 0, len(s)-1
        s = list(s)
        flag = True
        
        while l < r:
            
            if s[l] == s[r]:
                l += 1
                r -= 1
            elif s[l] != s[r] and flag:
                _l = l + 1
                __r = r
                
                if s[_l] == s[__r]:
                    _l += 1
                    __r -= 1
                    flag = False
                    while _l < __r:
                        if s[_l] != s[__r]:
                            break
                        _l += 1
                        __r -= 1
                    if _l >= __r:
                        return True
                _r = r - 1

                
                if s[_r] == s[l]:
                    flag = False
                    _r -= 1
                    l += 1
                    
                    while l < _r:
                        if s[l] != s[_r]:
                            print(l,_r)
                            return False
                        l += 1
                        _r -= 1
                    return True
                return False
            elif s[l] != s[r] and not flag:
                return False
        return True
    
    def _validPalindrome_eg(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        
        left = 0
        right = len(s) - 1
        step = int(len(s) / 2)
        
        while left < right:
            if s[left:left+step] == s[right:right-step:-1]:
                left += step
                right -= step
                continue
            elif step > 1:
                step = int(step/2)
                continue
                
            temp1 = s[left:right]
            temp2 = s[left+1:right+1]
            return (temp1 == temp1[::-1]) or (temp2 == temp2[::-1])

# print(Solution().validPalindrome("tcaac"))        
# print(Solution().validPalindrome("deeee"))
# print(Solution().validPalindrome("cupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupucu"))