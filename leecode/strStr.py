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

