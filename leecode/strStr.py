class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle or needle == haystack:
            return 0
        if not haystack or needle not in haystack:
            return -1
        pos = -1
        for i in range(len(haystack)):
            if haystack[i] in needle and haystack[i:i+len(needle)] == needle:
                pos = i
                break

        return pos

#print(Solution().strStr("aaaaa","bba"))

    def strStr(self, haystack: str, needle: str) -> int:
        #使用内置函数
        #return haystack.find(needle)
        #区间查找
        if len(needle) == 0:
            return 0
        
        i = 0
        while i <= len(haystack) - len(needle):  #区间移动次数 0 ~ h-n
            if haystack[i: i + len(needle)] == needle:   #区间匹配
                return i
            i += 1
        return -1
    def strStr_kmp(self, haystack: str, needle: str) -> int:
        def kmp(ls,s):
            _next = get_next(s)
            print(_next)
            l,r = 0,0
            ll = len(ls)
            while r < ll and l < len(s):
                if l == -1 or ls[r] == s[l]:
                    r += 1
                    l += 1
                else:
                    l = _next[l]
            
            if l == len(s):
                return r -l
            else:
                return -1


        def get_next(short):
            res = [0]*(len(short)+1)
            res[0] = -1
            slow,i = -1,0
            ll = len(short)
            while i < ll:
                if slow == -1 or short[i] == short[slow] :
                    i += 1
                    slow += 1
                    res[i] = slow
                else:
                    slow = res[slow] 
            return res
        return kmp(haystack,needle)
