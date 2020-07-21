class Solution:
    def replaceSpace(self, s: str) -> str:
        """
        请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

            示例 1：

            输入：s = "We are happy."
            输出："We%20are%20happy."
             

            限制：

            0 <= s 的长度 <= 10000

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not s:
            return s
        res = ''
        for x in s:
            if x ==' ':
                x = '%20'
            res += x
        return res

#print(Solution().replaceSpace('We are the chame '))

    def _replaceSpace_eg(self, s: str) -> str:
        return ''.join(('%20' if c == ' ' else c for c in s))