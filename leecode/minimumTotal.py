from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int: 
        """
            给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

            相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。
            例如，给定三角形：

            [
                [2],
                [3,4],
            [6,5,7],
            [4,1,8,3]
            ]
            自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

             

            说明：

            如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/triangle
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not triangle or len(triangle) <= 1:
            return 0 if not triangle else triangle[0][0]
        n = len(triangle)
        i  = 1
        while i < n:
            m = len(triangle[i])
            for j in range(m):
                print(i,j)
                if len(triangle[i-1]) <= j and j > 0 :
                    triangle[i][j] += triangle[i-1][j-1] 
                elif j == 0 :
                    triangle[i][j] += triangle[i-1][j] 
                else:
                    triangle[i][j] += min(triangle[i-1][j],triangle[i-1][j-1]) 

            i += 1
        return min(triangle[-1])

    def minimumTotal_eg(self, triangle: List[List[int]]) -> int:
        l = len(triangle)
        if l == 0:
            return 0
        dp = [[0] * i for i in range(1, l + 1)]
        dp[0][0] = triangle[0][0]
        for i in range(1, l):
            for j in range(i + 1):
                if j == 0:
                    dp[i][j] = triangle[i][j] + dp[i - 1][j]
                elif i == j:
                    dp[i][j] = triangle[i][j] + dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]
        return min(dp[-1])