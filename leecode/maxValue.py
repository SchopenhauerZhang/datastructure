from typing import List
class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        """
            在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？

            示例 1:

            输入: 
            [
              [1,3,1],
              [1,5,1],
              [4,2,1]
            ]
            输出: 12
            解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物
             

            提示：

            0 < grid.length <= 200
            0 < grid[0].length <= 200

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
            超出时间限制
        """

        if not grid:
            return 0
        n,m=len(grid),len(grid[0])
        self.res = 0
        def _iter(i,j,total):
            if i == n-1 and j == m-1:
                return total + grid[i][j]
            if i< 0 or j < 0 or i >= n or j>= m:
                return total
            
            return max(_iter(i+1,j,total+grid[i][j]),_iter(i,j+1,total+grid[i][j]))
            
        return _iter(0,0,0)
    
    def _maxValue(self, grid: List[List[int]]) -> int:
        """
        """
        if not grid:
            return 0
        n,m=len(grid),len(grid[0])
        for i in range(1,n):
            grid[i][0] += grid[i-1][0]

        for j in range(1,m):
            grid[0][j] += grid[0][j-1]

        for i in range(1,n):
            for j in range(1,m):
                grid[i][j] += max(grid[i-1][j],grid[i][j-1])
        return grid[n-1][m-1]
    def maxValue_eg(self, grid: List[List[int]]) -> int:
        '''
        3行4列
        m = 3
        n = 4
        1 3 1 1
        1 4 3 2
        4 2 1 4
        '''
        m = len(grid)
        n = len(grid[0])
        dp = [0]*n
        for i in range(m):
            dp[0] += grid[i][0]
            for j in range(1, n):
                dp[j] = max(dp[j], dp[j-1]) + grid[i][j]

        return dp[-1]