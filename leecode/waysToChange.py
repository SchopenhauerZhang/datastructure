class Solution:
    def waysToChange(self, n: int) -> int:
        """ 
            硬币。给定数量不限的硬币，币值为25分、10分、5分和1分，编写代码计算n分有几种表示法。(结果可能会很大，你需要将结果模上1000000007)

            示例1:

            输入: n = 5
            输出：2
            解释: 有两种方式可以凑成总金额:
            5=5
            5=1+1+1+1+1
            示例2:

            输入: n = 10
            输出：4
            解释: 有四种方式可以凑成总金额:
            10=10
            10=5+5
            10=5+1+1+1+1+1
            10=1+1+1+1+1+1+1+1+1+1
            说明：

            注意:

            你可以假设：

            0 <= n (总金额) <= 1000000

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/coin-lcci
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not n or n == 1:
            return 1 if n==1 else 0
        dp = [0]*(n+1)
        dp[0] = 1
        for coin in [1,5,10,25]:
            if coin > n:
                continue
            for num in range(1,n+1):
                if num - coin >= 0 :
                    dp[num] += dp[num-coin]
                else:
                    dp[num] = dp[num]
   
        return dp[n]%1000000007

    def _waysToChange_eg(self, n: int) -> int:
        a, b, c = n // 25, n % 25 // 10, n % 25 % 10 // 5
        x, y = divmod(a, 2)
        result = self.sum_(a, b, c, x)

        if y == 0:
            x -= 1
    
        b = b + 2 + (c + 1) // 2
        c = 1 - c
        result += self.sum_(a, b, c, x)

        return int(result) % 1000000007

    
    def sum_(self, a, b, c, x):
        return (x + 1) * (25 * x * (2 * x + 1) / 6 + 5 * (2 * b + 2 + c) * x / 2 + (b + c + 1) * (b + 1))
