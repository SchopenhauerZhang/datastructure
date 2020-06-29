class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

        '.' 匹配任意单个字符
        '*' 匹配零个或多个前面的那一个元素
        所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

        说明:

        s 可能为空，且只包含从 a-z 的小写字母。
        p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
        示例 1:

        输入:
        s = "aa"
        p = "a"
        输出: false
        解释: "a" 无法匹配 "aa" 整个字符串。

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/regular-expression-matching
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        pass

    def _isMatch(self, s: str, p: str) -> bool:
        if not p :
            return not s
        is_ma = bool(s) and p[0] in {s[0],"."}
        if len(p) >=2 and p[1] == "*":
            return self._isMatch(s,p[2:]) or is_ma and  self._isMatch(s[1:],p)

        return is_ma and self._isMatch(s[1:],p[1:])

#print(Solution()._isMatch("aab","c*a*b"))

    def _isMatch_eg(self, text: str, pattern: str) -> bool:
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(pattern):
                    ans = i == len(text)
                else:
                    first_match = i < len(text) and pattern[j] in {text[i], '.'}
                    if j+1 < len(pattern) and pattern[j+1] == '*':
                        ans = dp(i, j+2) or (first_match and dp(i+1, j))
                    else:
                        ans = first_match and dp(i+1, j+1)
                memo[i, j] = ans
            return memo[i, j]
        return dp(0, 0)
