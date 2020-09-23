from typing import List
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        """
            给你一个 m * n 的矩阵 mat 和一个整数 K ，请你返回一个矩阵 answer ，其中每个 answer[i][j] 是所有满足下述条件的元素 mat[r][c] 的和： 

            i - K <= r <= i + K, j - K <= c <= j + K 
            (r, c) 在矩阵内。
             

            示例 1：

            输入：mat = [[1,2,3],[4,5,6],[7,8,9]], K = 1
            输出：[[12,21,16],[27,45,33],[24,39,28]]
            示例 2：

            输入：mat = [[1,2,3],[4,5,6],[7,8,9]], K = 2
            输出：[[45,45,45],[45,45,45],[45,45,45]]
             

            提示：

            m == mat.length
            n == mat[i].length
            1 <= m, n, K <= 100
            1 <= mat[i][j] <= 100

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/matrix-block-sum
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
            超出时间限制
        """
        if not mat or not K:
            return mat
        _c,_r = len(mat),len(mat[0])
        dp = [[[0] for _ in range(_r) ] for _ in range(_c)]
        def _val(l,r):
            
            if l < 0 or l >=_c or r < 0 or r >= _r :
                return 0
            
            return mat[l][r]
        def get_val(_i,_j):
            if _i < 0 or _i >=_c or _j < 0 or _j >= _r :
                return 0
            _res = 0
            for _indexi in range(-K,K+1):
                for _indexj in range(-K,K+1):
                    #_res+=_val(_i-_indexi,_j)+_val(_i-_indexi,_j-_indexj)+_val(_i,_j-_indexj)+_val(_i+_indexi,_j)+_val(_i,_j+_indexj)+_val(_i+_indexi,_j+_indexj)+_val(_i+_indexi,_j-_indexj)+_val(_i-_indexi,_j+_indexj)
                    _res += _val(_i+_indexi,_j+_indexj)

            return _res

        for i in range(_c):
            for j in range(_r):
                dp[i][j] = get_val(i,j)
        mat = dp
        print(dp)
        return mat 

    def _matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        if not mat or not K:
            return mat
        _c,_r = len(mat),len(mat[0])
        dp = [[[0] for _ in range(_r) ] for _ in range(_c)]
        for i in range(_c):
            for j in range(_r):
                _j_min = j - K if j - K >= 0  else 0
                _j_max = j + K if j + K < _r else _r
                _i_min = i - K if i - K >= 0  else 0
                _i_max = i + K if i + K < _c else _c
                
                _mat = [x[_j_min:_j_max+1] for x in mat[_i_min:_i_max+1]]
                dp[i][j] = sum([ sum(_l) for _l in _mat])
        mat = dp
        
        return mat
    
    def matrixBlockSum_eg(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        dp = [ [0] * n for _ in range(m)]
        for j in range(n):
            t = min(m,K+1)
            t2 = max(1,m-K)
            dp[0][j] = sum([mat[x][j] for x in range(t)])
            for i in range(1,min(t,t2)):
                dp[i][j] = dp[i-1][j] + mat[i+K][j]
            if t2 > t:
                for i in range(t,t2):
                    dp[i][j] = dp[i-1][j] + mat[i+K][j] - mat[i-K-1][j]
            else:
                for i in range(t2,t):
                    dp[i][j] = dp[i-1][j] 
            for i in range(max(t2,t),m):
                dp[i][j] = dp[i-1][j] - mat[i-K-1][j]
        print(dp)
        dp2 = [ [0] * n for _ in range(m)]
        for i in range(m):
            t = min(n,K+1)
            t2 = max(1,n-K)
            dp2[i][0] = sum(dp[i][:t])
            for j in range(1,min(t,t2)):
                dp2[i][j] = dp2[i][j-1] + dp[i][j+K]
            if n-K > t:
                for j in range(t,t2):
                    dp2[i][j] = dp2[i][j-1] + dp[i][j+K] - dp[i][j-K-1]
            else:
                for j in range(t2,t):
                    dp2[i][j] = dp2[i][j-1] 
            for j in range(max(t2,t),n):
                dp2[i][j] = dp2[i][j-1] - dp[i][j-K-1]
        return dp2