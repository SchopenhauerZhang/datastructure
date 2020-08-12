class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

 

        示例：

        s = "leetcode"
        返回 0

        s = "loveleetcode"
        返回 2

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/first-unique-character-in-a-string
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not s or len(s) == 1:
            return -1 if not s else 0
        for i in range(len(s)):
            if s[i] not in s[i+1:] and s[i] not in s[:i]:
                return i
        return -1

# print(Solution().firstUniqChar('leetcode'))#0
# print(Solution().firstUniqChar('loveleetcode'))#2
# print(Solution().firstUniqChar('cc'))#
    def _firstUniqChar_eg(self, s: str) -> int:
        min_char=len(s)
        for c in "abcdefghijklmnopqrstuvwxyz":
            i=s.find(c)
            if i!=-1 and i==s.rfind(c):
                min_char=min(min_char,i)
        return min_char if min_char!=len(s) else -1

    def _firstUniqChar_50(self, s: str) -> str:
        """
                在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

                示例:

                s = "abaccdeff"
                返回 "b"

                s = "" 
                返回 " "
                 

                来源：力扣（LeetCode）
                链接：https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof
                著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not s:
            return " "
        if len(s) == 1:
            return s
        s = list(s)
        tmp = []
        for i in range(len(s)):
            if s[i] not in tmp and s[i] not in s[i+1:] and i != len(s)-1:
                return s[i]
            elif s[i] in s[i+1:]:
                tmp.append(s[i])

        return s[i]  if s[i] not in tmp else " "

    def _firstUniqChar_50_eg(self, s: str) -> str:
        """
            精彩
        """
        unique = list()
        multi = set()
        for c in s:
            if c in multi:
                continue
            elif c in unique:
                multi.add(c)
                unique.remove(c)
            else:
                unique.append(c)
        return unique[0] if len(unique) > 0 else ' '


print(Solution()._firstUniqChar_50("aadadaad"))
print(Solution()._firstUniqChar_50("dddccdbba"))
