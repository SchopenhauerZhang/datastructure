from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
            给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

        岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。

        此外，你可以假设该网格的四条边均被水包围。

         

        示例 1:

        输入:
        [
        ['1','1','1','1','0'],
        ['1','1','0','1','0'],
        ['1','1','0','0','0'],
        ['0','0','0','0','0']
        ]
        输出: 1
        示例 2:

        输入:
        [
        ['1','1','0','0','0'],
        ['1','1','0','0','0'],
        ['0','0','1','0','0'],
        ['0','0','0','1','1']
        ]
        输出: 3
        解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/number-of-islands
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not grid or (len(grid) == 1 and len(grid[0])== 1):
            return 1 if grid and  len(grid) == 1 and  grid[0][0] != '0'  else 0
        ll,lr = len(grid),len(grid[0])
        def island(i,j):
            if i  < 0 or j < 0 or i >= ll or j >= lr or grid[i][j] == '0':
                return None
            grid[i][j] = '0'
            island(i+1,j)
            island(i-1,j)
            island(i,j+1)
            island(i,j-1)
        res = 0
        for _i in range(ll):
            for _j in range(lr):
                print(grid[_i][_j])
                if grid[_i][_j] == '1':
                    island(_i,_j)
                    res += 1
        return res
    
    def _numIslands_eg(self, grid: List[List[str]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        m, n, count = len(grid), len(grid[0]), 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    count += 1
                    que = [[i,j]]
                    while que:
                        # dp table，拒绝重复遍历
                        nque = []
                        for q in que:
                            ii, jj = q
                            if ii + 1 < m and grid[ii+1][jj] == '1':
                                nque.append([ii+1, jj])
                                grid[ii+1][jj] = '0'
                            if ii - 1 >= 0 and grid[ii-1][jj] == '1':
                                nque.append([ii-1, jj])
                                grid[ii-1][jj] = '0'
                            if jj + 1 < n and grid[ii][jj+1] == '1':
                                nque.append([ii, jj+1])
                                grid[ii][jj+1] = '0'
                            if jj - 1 >= 0 and grid[ii][jj-1] == '1':
                                nque.append([ii, jj-1])
                                grid[ii][jj-1] = '0'
                        que = nque
        return count