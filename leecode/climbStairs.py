import functools
class Solution:
    def climbStairs(self, n: int) -> int:
        """
        假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

            每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

            注意：给定 n 是一个正整数。

            示例 1：

            输入： 2
            输出： 2
            解释： 有两种方法可以爬到楼顶。
            1.  1 阶 + 1 阶
            2.  2 阶
            示例 2：

            输入： 3
            输出： 3
            解释： 有三种方法可以爬到楼顶。
            1.  1 阶 + 1 阶 + 1 阶
            2.  1 阶 + 2 阶
            3.  2 阶 + 1 阶

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/climbing-stairs
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if n == 1:
            return 1

        self.res = 0
        def climb(x):
            if x == 1:
                self.res += 1
                return

            if x ==2:
                self.res += 1
                climb(x-1)
                return

            climb(x-1)
            climb(x-2)

        climb(n)
        return self.res
    
    def _climbStairs(self, n: int) -> int:
        if n<= 2:
            return n

        l,r = 1,2
        for i in range(3,n+1):
            tmp = l+r
            l,r = r,tmp
        return r

    @functools.lru_cache(100)
    def _climbStairs_cache(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.climbStairs(n - 1) + self.climbStairs(n - 2) if n > 2 else n

# print(Solution()._climbStairs(3))
# print(Solution()._climbStairs(2))
# print(Solution()._climbStairs(4))
# print(Solution()._climbStairs(38))

    def _climbStairs_eg(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        old_1 =1
        old_2 =2

        for i in range(3,n+1):
            old_1,old_2 = old_2,old_1+old_2
        return old_2
        # if n<0:
        #     return 0
        # if n == 0:
        #     return 1
        # if n>0:
        #     return self.climbStairs(n-1)+self.climbStairs(n-2)