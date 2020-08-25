from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        网格中的障碍物和空位置分别用 1 和 0 来表示。

        说明：m 和 n 的值均不超过 100。

        示例 1:

        输入:
        [
          [0,0,0],
          [0,1,0],
          [0,0,0]
        ]
        输出: 2
        解释:
        3x3 网格的正中间有一个障碍物。
        从左上角到右下角一共有 2 条不同的路径：
        1. 向右 -> 向右 -> 向下 -> 向下
        2. 向下 -> 向下 -> 向右 -> 向右

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/unique-paths-ii
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not obstacleGrid or (len(obstacleGrid) == 1 and len(obstacleGrid[0]) == 1):
            return 1 if (len(obstacleGrid) == 1 and len(obstacleGrid[0]) == 1) and 1 not in obstacleGrid[0]  else 0
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        dp = [[0]*col for _ in range(row)]
        if obstacleGrid[0][0] == 0:
            dp[0][0] = 1
           
        for i in range(row):
            for j in range(col):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                elif i==0 and j>0:
                    dp[i][j] = dp[i][j-1]
                elif j==0 and i>0:
                    dp[i][j] = dp[i-1][j]
                elif j==0 and i==0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
        return dp[row-1][col-1] 

    def _uniquePathsWithObstacles_eg(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0]==1:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        grid = []
        for i in range(m):
            grid.append([])
            for j in range(n):
                grid[i].append(1)
        

        for i in range(1,m):
            if obstacleGrid[i][0]==1 or grid[i-1][0]==0:
                grid[i][0]=0
        
        for j in range(1,n):
            if obstacleGrid[0][j]==1 or grid[0][j-1]==0:
                grid[0][j]=0

        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]==1:
                    grid[i][j]=0
                else:
                    grid[i][j] = grid[i-1][j] + grid[i][j-1]

        print(grid)
        return grid[m-1][n-1]