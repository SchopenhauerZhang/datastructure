class Solution:
    def fib(self, n: int) -> int:
        """
            写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项。斐波那契数列的定义如下：

            F(0) = 0,   F(1) = 1
            F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
            斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。

            答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

             

            示例 1：

            输入：n = 2
            输出：1
            示例 2：

            输入：n = 5
            输出：5
             

            提示：

            0 <= n <= 100

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        elif not n:
            return 0
        from collections import defaultdict
        dp = defaultdict(int)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        dp[3] = 2
        dp[4] = 3
        def f(x):
            if x in dp:
                return dp[x]
            if x == 0:
                return 0
            elif x == 1:
                return 1
            elif x == 2:
                return 1
            else:
                _res = f(x-1) +f(x-2)
                if x not in dp:
                    dp[x] = _res
                return dp[x]
        res = f(n)    
        return res if res < 1000000007 else res % 1000000007

    def _fib_eg(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        if n == 3:
            return 2
        n1 = 1
        n2 = 2
        for i in range(4,n+1):
            n = n1 + n2
            n1 = n2
            n2 = n
        return n % 1000000007