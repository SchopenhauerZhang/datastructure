from typing import List
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """ 
            在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。

            示例:

            输入: 

            1 0 1 0 0
            1 0 1 1 1
            1 1 1 1 1
            1 0 0 1 0

            输出: 4

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/maximal-square
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not matrix :
            return 0 
        count = 0
        for i in  matrix:
            if '1' in i:
                count = 1
        if count == 0:
            return count
        ll,lr = len(matrix),len(matrix[0])
        dp = [[0]*lr for _ in range(ll)]
        print(dp)
        squeare = 0
        for i in range(ll):
            for j in range(lr):
                if matrix[i][j] == '0':
                    continue
                if (i == 0 or j==0) and matrix[i][j] == '1':
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                squeare = max(squeare,dp[i][j])
        return squeare**2
    
    def getWidth(self,num):  #步骤3：求一个数中连续最多的1
        w=0
        while num>0:
            num&=num<<1
            w+=1
        return w
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        nums=[int(''.join(n),base=2) for n in matrix]  #步骤1：每一行当作二进制数
        res,n=0,len(nums)
        for i in range(n):   #步骤2：枚举所有的组合，temp存储相与的结果
            temp=nums[i]
            for j in range(i,n):
                temp&=nums[j]
                if self.getWidth(temp)<j-i+1:
                    break
                res=max(res,j-i+1)
        return res*res
        