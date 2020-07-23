class Solution:
    def mySqrt(self, x: int) -> int:
        """
        实现 int sqrt(int x) 函数。

        计算并返回 x 的平方根，其中 x 是非负整数。

        由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

        示例 1:

        输入: 4
        输出: 2
        示例 2:

        输入: 8
        输出: 2
        说明: 8 的平方根是 2.82842..., 
             由于返回类型是整数，小数部分将被舍去。

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/sqrtx
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if x <= 1:
            return x
        
        for i in range(1,1+x//2):
            if i*i > x:
                return i -1
        return x//2

# print(Solution().mySqrt(1))
# print(Solution().mySqrt(0))
# print(Solution().mySqrt(2))
# print(Solution().mySqrt(6))
# print(Solution().mySqrt(11))

    def _mySqrt_eg(self, x: int) -> int:
        if x == 0:
            return x
        
        C, X_cur = float(x), float(x)

        while True:
            X_next = 0.5 * (X_cur + C / X_cur)
            print(X_cur)
            print(X_next)
            if abs(X_cur - X_next) < 1e-7:
                #1*10的-7次方
                break
            X_cur = X_next
        
        return int(X_cur)
print(Solution()._mySqrt_eg(11))