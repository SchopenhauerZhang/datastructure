class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        """
            地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

 

            示例 1：

            输入：m = 2, n = 3, k = 1
            输出：3
            示例 2：

            输入：m = 3, n = 1, k = 0
            输出：1
            提示：

            1 <= n,m <= 100
            0 <= k <= 20

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if (m == n and m== 1 ) or k == 0:
            return 1 
        if k == 1 and (m > 1 and n > 1):
            return 3
        if k == 1 and (m == 1 or n == 1):
            return 2
        def dfs(i, j, si, sj):
            if i >= m or j >= n or (i, j) in visited or si + sj > k:
                return 
            visited.add((i, j))
            dfs(i+1, j, si + 1 if (i+1) % 10 else si - 8, sj) 
            dfs(i, j+1, si, sj + 1 if (j+1) % 10 else sj - 8)
        visited = set()
        dfs(0, 0, 0, 0)
        return len(visited)

    def _movingCount(self, m: int, n: int, k: int) -> int:
        dp = [[0]*n]*m
    
        self._res = []
        def get(l,r):
            
            if l >= m or r >= n or l< 0 or r <0:
                return 
            if dp[l][r] ==  1:
                return 
            _str = str(l)+str(r)
            _res = 0
            _flag = True
            for _s in _str:
                _res += int(_s)
                if _res > k:
                    _flag = False
                    break
            dp[l][r] = 1
            if _flag:
                if [l,r] not in self._res:
                    self._res.append([l,r])
                    self.res += 1
                get(l+1,r)
                get(l,r+1)
                get(l-1,r)
                get(l,r-1)
          
            return 
        
        self.res = 0
        get(0,0) 
        print(dp)
        return self.res

    def _movingCount_eg(self, m: int, n: int, k: int) -> int:
        # def dfs(i, j, si, sj):
        #     if i >= m or j >= n or k < si + sj or (i, j) in visited: return 0
        #     visited.add((i,j))
        #     return 1 + dfs(i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj) + dfs(i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8)

        # visited = set()
        # return dfs(0, 0, 0, 0)

        def dfs(i, j , si, sj):
            if i >= m or j >= n or si+sj > k or (i, j) in visited:
                return 0
            visited.add((i, j))
            return 1 + dfs(i+1, j, si + 1 if (i+1) % 10 else si - 8, sj) + dfs(i, j+1, si, sj+1 if (j+1) % 10 else sj - 8)

        visited = set()
        return dfs(0, 0, 0, 0)
