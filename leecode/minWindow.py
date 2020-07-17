class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s or len(t) > len(s):
            return ""
        if s == t:
            return s 
        if t in s:
            return t
 
        l = 0
        r = 0
        tmp = {}
        min_l = len(s)+1
        _sp = 0
        _ep = 0
        while r < len(s):
            if s[r] in t:
                if s[r] in tmp:
                    tmp[s[r]] += 1
                else :
                    tmp[s[r]] = 1
            
            while len(tmp) == len(t) and l < r:
                if s[l] in t:
                    tmp[s[l]] -= 1
                    if tmp[s[l]] == 0:
                        del tmp[s[l]]
                        min_l = min(min_l,r-l+1)
                        _sp = l
                        _ep = r
                    else:
                        min_l = min(min_l,r-l)
                        _sp = l
                        _ep = r

                l += 1
            r += 1
        print(min_l)
        return s[_sp:_ep+1] if min_l != len(s)+1 else ""
# https://leetcode-cn.com/problems/minimum-window-substring/submissions/
print(Solution().minWindow("bbaa",  "aba"))
print(Solution().minWindow("ADOBECODEBANC",  "ABC"))
print(Solution().minWindow("abc",  "ac"))
print(Solution().minWindow("ABC",  "B"))

