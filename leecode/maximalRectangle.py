from typing import List
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """
            给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

            示例:

            输入:
            [
            ["1","0","1","0","0"],
            ["1","0","1","1","1"],
            ["1","1","1","1","1"],
            ["1","0","0","1","0"]
            ]
            输出: 6

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/maximal-rectangle
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not matrix or (len(matrix) == 1 and len(matrix[0])==1):
            return 1 if matrix and '1' in matrix[0] else 0
        
        
        if len(matrix)==0:
            return 0
        else:
            max1 = 0
            dp = [0 for i in range(len(matrix[0]))]
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if matrix[i][j] == '1':
                        dp[j] += 1
                    else:
                        dp[j] = 0
                if max(dp) > 0:
                    for l in range(max(dp), 0, -1):
                        max2 = 0
                        t1 = -1
                        t2 = -1
                        for k in range(len(dp)):
                            if dp[k] >= l:
                                t2 = k
                                max2 = max(max2, t2 - t1)
                            else:
                                t1 = k
                        max1 = max(max1, l * max2)
        return max1

    def _maximalRectangle_eg(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        nums = [int(''.join(row), base=2) for row in matrix]
        ans, N = 0, len(nums)
        for i in range(N):
            j, num = i, nums[i]
            while j < N:
                num = num&nums[j]
                if not num:
                    break
                width, curnum = 0, num
                while curnum:
                    width += 1
                    curnum = curnum&(curnum>>1)
                ans = max(ans, width*(j-i+1))
                j+=1
        return ans 
