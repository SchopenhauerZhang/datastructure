from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        """
            给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。对于数组中的任意一个整数，你都可以从 + 或 -中选择一个符号添加在前面。

            返回可以使最终数组和为目标数 S 的所有添加符号的方法数。

             

            示例：

            输入：nums: [1, 1, 1, 1, 1], S: 3
            输出：5
            解释：

            -1+1+1+1+1 = 3
            +1-1+1+1+1 = 3
            +1+1-1+1+1 = 3
            +1+1+1-1+1 = 3
            +1+1+1+1-1 = 3

            一共有5种方法让最终目标和为3。

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/target-sum
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        n = len(nums)
        sumation = 0
        for num in nums:
            sumation += num
        if abs(sumation) < abs(S): return 0
        length = (2 * sumation) + 1
        dp = [[0 for _ in range(length)] for _ in range(n)]
        dp[0][sumation + nums[0]] = 1
        dp[0][sumation - nums[0]] += 1
        print(dp)
        for i in range(1, n):
            for j in range(length):
                l = dp[i - 1][j - nums[i]] if 0 <= j - nums[i] < length else 0
                r = dp[i - 1][j + nums[i]] if 0 <= j + nums[i] < length else 0
                dp[i][j] = l + r
        print(dp)
        return dp[n - 1][sumation + S] 
    
    def _findTargetSumWays_eg(self, nums: List[int], S: int) -> int:
        sums = sum(nums)
        if sums < S or (S + sums)%2 != 0:
            return 0

        target = (S + sums) // 2
        dp = [0]*(target + 1)
        dp[0] = 1
        for num in nums:
            for i in range(target, num-1, -1):
                dp[i] += dp[i - num]
        return dp[-1]
         
        
