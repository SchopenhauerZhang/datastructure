class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
            示例 1:

            输入: m = 3, n = 2
            输出: 3
            解释:
            从左上角开始，总共有 3 条路径可以到达右下角。
            1. 向右 -> 向右 -> 向下
            2. 向右 -> 向下 -> 向右
            3. 向下 -> 向右 -> 向右
            示例 2:

            输入: m = 7, n = 3
            输出: 28

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/unique-paths
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not m or not n or m <= 1 or n<=1:
            return 0 if not m or not n or m==0 or n == 0 else 1
        dp = [[0]*m ]*n
        dp[0]=[1]*m
        for i in range(n):
            dp[i][0] = 1
        for i in range(1,n):
            for j in range(1,m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[n-1][m-1]

    def _uniquePaths_eg(self, m: int, n: int) -> int:
        dp = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]