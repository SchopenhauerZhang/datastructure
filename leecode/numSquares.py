class Solution:
    def numSquares(self, n: int) -> int:
        """
                    给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

        示例 1:

        输入: n = 12
        输出: 3 
        解释: 12 = 4 + 4 + 4.
        示例 2:

        输入: n = 13
        输出: 2
        解释: 13 = 4 + 9.

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/perfect-squares
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        精彩
        """
        if n == 0 or n in (1,2,3):
            return n
        # 四平方定理 任何一个整数都不超过4个数的平方和
        # 当等于4个数的平方和的整数满足n= 4a(8b+7)
        while n%4 == 0:
            n/=4
        if n%8==7:
            return 4
        
        # 暴力寻找1和2
        _n = 0
        while _n**2 < n:
            __n = int((n - _n**2)**0.5)
            # 验证__n是否是一个完全平方数
            if __n **2 + _n **2 == n:
                # 不是1就是2或者0
                return (not not _n) + (not not __n)
            _n += 1

        # 默认是由3个数的平方和求得
        return 3

    def _numSquares_eg(self, n: int) -> int:
        """
            精彩
        """
        if n == 0:
            return 0
        dp = [ i for i in range(n+1)]
        
        num = 2
        num_num = num*num
        while num_num<=n:
            for i in range(num_num,n+1):
                dp[i] = dp[i] if dp[i]<dp[i-num_num]+1 else dp[i-num_num]+1
            num+=1
            num_num = num*num
        return dp[n]