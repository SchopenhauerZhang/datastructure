class Solution:
    def maxCoins(self, nums: list) -> int:
        """
        有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。

        现在要求你戳破所有的气球。每当你戳破一个气球 i 时，你可以获得 nums[left] * nums[i] * nums[right] 个硬币。 这里的 left 和 right 代表和 i 相邻的两个气球的序号。注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。

        求所能获得硬币的最大数量。

        说明:

        你可以假设 nums[-1] = nums[n] = 1，但注意它们不是真实存在的所以并不能被戳破。
        0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
        示例:

        输入: [3,1,5,8]
        输出: 167 
        解释: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
            coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
        没看懂:https://blog.csdn.net/u014626513/article/details/81146851
        """
        # 从中间开始戳气球
        coins = [1] + [i for i in nums if i > 0] + [1]
        n = len(coins)
        max_coins = [[0 for _ in range(n)] for _ in range(n)]
        [1,3,1,5,8,1]
        for k in range(2, n):
            for left in range(n - k):
                right = left + k
                for i in range(left + 1, right):
                    max_coins[left][right] = max(max_coins[left][right], \
                           coins[left] * coins[i] * coins[right] + \
                           max_coins[left][i] + max_coins[i][right])
        print(max_coins)
        return max_coins[0][-1]

    def _maxCoins_eg(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = [1] + nums + [1]
        n = len(nums)

        dp = [[0] * n for _ in range(n)]

        for i in reversed(range(n-2)):
            for j in range(i + 2, n):
                max = 0
                product = nums[i] * nums[j]
                for k in range(i + 1, j):
                    tmp = dp[i][k] + dp[k][j] + nums[k] * product
                    if tmp > max:
                        max = tmp
                
                dp[i][j] = max
                
        return dp[0][n-1]

#print(Solution().maxCoins([3,1,5,8]))
print(Solution().maxCoins([3,1,2,5,4,8]))# 348