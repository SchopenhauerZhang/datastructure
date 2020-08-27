class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
            实现 pow(x, n) ，即计算 x 的 n 次幂函数。

            示例 1:

            输入: 2.00000, 10
            输出: 1024.00000
            示例 2:

            输入: 2.10000, 3
            输出: 9.26100
            示例 3:

            输入: 2.00000, -2
            输出: 0.25000
            解释: 2-2 = 1/22 = 1/4 = 0.25
            说明:

            -100.0 < x < 100.0
            n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/powx-n
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if x == 0 or x== 1 or n == 0 or n == 1:
            if n == 0 or x == 1:
                return 1
            return 0 if x == 0 else x
        
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n
        ans = 1
        res = 1
        while n:
            if n % 2:
                ans *= x
            n >>= 1
            x *= x
        return ans

    def _myPow_eg(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        elif n == 1:
            return x
        elif n == -1:
            return 1.0/x
        elif n == 2:
            return x * x
        elif n % 2 == 0:
            return self.myPow(self.myPow(x, n//2), 2)
        else:
            return self.myPow(self.myPow(x, (n-1)//2),2) * x