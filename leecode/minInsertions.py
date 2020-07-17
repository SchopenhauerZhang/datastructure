class Solution:
    def minInsertions(self, s: str) -> int:
        """
        给你一个字符串 s ，每一次操作你都可以在字符串的任意位置插入任意字符。

请你返回让 s 成为回文串的 最少操作次数 。

「回文串」是正读和反读都相同的字符串。

 

        示例 1：

        输入：s = "zzazz"
        输出：0
        解释：字符串 "zzazz" 已经是回文串了，所以不需要做任何插入操作。
        示例 2：

        输入：s = "mbadm"
        输出：2
        解释：字符串可变为 "mbdadbm" 或者 "mdbabdm" 。
        示例 3：

        输入：s = "leetcode"
        输出：5
        解释：插入 5 个字符后字符串变为 "leetcodocteel" 。
        示例 4：

        输入：s = "g"
        输出：0
        示例 5：

        输入：s = "no"
        输出：1

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/minimum-insertion-steps-to-make-a-string-palindrome
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for l in range(1, n):
            i = 0
            for j in range(l, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j - 1])
                i += 1
        print(dp)
        return dp[0][n - 1]


# print(Solution().minInsertions('mbadm'))
# print(Solution().minInsertions('leecode'))
# print(Solution().minInsertions('leetcode'))

    def _minInsertions(self, s: str) -> int:
        # dp
        # 找到最长回文子序列 （---> leetcode 516）
        # 然后用字符串长度减去最长回文子序列的长度就是答案
        def longestPalindromeSubseq(s):
            n = len(s)
            if n <= 1 or s[::-1] == s:
                return n
            dp = [0]*n
            for i in range(n-1, -1, -1):
                temp, dp[i] = 0, 1
                for j in range(i+1, n):
                    if s[i] == s[j]:
                        temp, dp[j] = dp[j], temp + 2
                    else:
                        temp = dp[j]
                        if dp[j-1] > dp[j]:
                            dp[j] = dp[j-1]
            return dp[-1]
        
        return len(s) - longestPalindromeSubseq(s)


print(Solution().minInsertions('mbadm'))