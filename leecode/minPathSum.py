from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
            给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

            说明：每次只能向下或者向右移动一步。

            示例:

            输入:
            [
              [1,3,1],
            [1,5,1],
            [4,2,1]
            ]
            输出: 7
            解释: 因为路径 1→3→1→1→1 的总和最小。

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/minimum-path-sum
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not grid:
            return 0
        ri,rj = len(grid),len(grid[0])
        for i in range(ri):
            for j in range(rj):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    grid[i][j] = grid[i][j]+grid[i][j-1]
                elif j == 0:
                    grid[i][j] = grid[i][j]+grid[i-1][j]
                else:
                    grid[i][j] =  min(grid[i-1][j],grid[i][j-1])+grid[i][j]

        return grid[ri-1][rj-1]

#print(Solution().minPathSum([[1,3,1],[1,5,1],[4,2,1]]))

    def _minPathSum_eg(self, grid: List[List[int]]) -> int:
        dp = [float('inf')] * (len(grid[0])+1)
        dp[1] = 0
        for row in grid:
            for idx, num in enumerate(row):
                dp[idx + 1] = min(dp[idx], dp[idx + 1]) + num
        return dp[-1]
            