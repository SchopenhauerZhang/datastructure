class Solution:
    def generate(self, numRows: int) -> list:
        """
        示例:
            杨辉三角
            输入: 5
            输出:
            [
                [1],
                [1,1],
            [1,2,1],
            [1,3,3,1],
            [1,4,6,4,1]
            ]
        """
        if numRows <= 2:
            if  numRows == 0:
                return []
            return [[1]] if  numRows == 1 else [[1],[1,1]]
        self.res = []
        dp = {}
        dp[1] = [1]
        dp[2] = [1,1]
        def _sum(n):
            if n in dp:
                return dp[n]
            if n == 1:
                return [1]
            elif n==2:
                return [1,1]
            if [1] not in self.res:
                self.res.append([1])
            if [1,1] not in self.res:
                self.res.append([1,1]) 
            tmp = [1]
            for i in range(1,n-1):
                tmp.append(sum(_sum(n-1)[i-1:i+1]))
                
            tmp.append(1)
            if n not in dp:
                dp[n] = tmp
            if tmp not in self.res:
                self.res.append(tmp)
            return tmp
        _sum(numRows)
        return self.res

#print(Solution().generate(15))

# #  [
# #     [1],
# #    [1,1],
# #   [1,2,1],
# #  [1,3,3,1],
# # [1,4,6,4,1]
# #]
    def _generate_eg(self, numRows: int) -> list:
        if numRows == 0:
            return []
        res = [[1]]
        while len(res) < numRows:
            newRow = [a+b for a, b in zip([0]+res[-1], res[-1]+[0])]
            res.append(newRow)
        return res