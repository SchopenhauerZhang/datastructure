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