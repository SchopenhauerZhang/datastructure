class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列的长度。

        一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
        例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。两个字符串的「公共子序列」是这两个字符串所共同拥有的子序列。

        若这两个字符串没有公共子序列，则返回 0。

         

        示例 1:

        输入：text1 = "abcde", text2 = "ace" 
        输出：3  
        解释：最长公共子序列是 "ace"，它的长度为 3。
        示例 2:

        输入：text1 = "abc", text2 = "abc"
        输出：3
        解释：最长公共子序列是 "abc"，它的长度为 3。
        示例 3:

        输入：text1 = "abc", text2 = "def"
        输出：0
        解释：两个字符串没有公共子序列，返回 0。

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/longest-common-subsequence
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        n,m = len(text1),len(text2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        
        for  i in range(1,m+1):
            for j in range(1,n+1):
                if text1[j-1] == text2[i-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])

        #print(dp)
        return dp[-1][-1]


# print(Solution().longestCommonSubsequence( "abcde","ace"))
# print(Solution().longestCommonSubsequence( "abcdeegfrabdce","aceece"))
# print(Solution().longestCommonSubsequence( "abc","abc"))
# print(Solution().longestCommonSubsequence( "abc","efg"))
# print(Solution().longestCommonSubsequence( "bsbininm","jmjkbkjkv"))

    def _longestCommonSubsequence_eg(self, text1: str, text2: str) -> int:
        if text1 == text2:
            return len(text1)
        if not set(text1).intersection(text2):
            return 0
        
        d = collections.defaultdict(list)
        m, n = len(text1), len(text2)
        for i in range(n-1, -1, -1):
            d[text2[i]].append(i)
            
        nums = []
        for c in text1:
            if c in d:
                nums.extend(d[c])
        
        ans = []
        for num in nums:
            idx = bisect.bisect_left(ans, num)
            if idx == len(ans):
                ans.append(num)
            else:
                ans[idx] = num
        return len(ans)

