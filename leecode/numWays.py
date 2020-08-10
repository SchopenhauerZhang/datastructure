class Solution:
    def numWays(self, n: int) -> int:
        """
            一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。

            答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

            示例 1：

            输入：n = 2
            输出：2
            示例 2：

            输入：n = 7
            输出：21
            示例 3：

            输入：n = 0
            输出：1

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if n in (0,1,2):
            return 1 if n == 0 else n
        from collections import defaultdict
        _n = defaultdict(int)
        _n[1] = 1
        _n[2] = 2
        for _i in range(3,n+1):
            if _i not in _n:
                _n[_i] = _n[_i-1]+_n[_i-2]

        return _n[n]%1000000007

    def _numWays_eg(self, n: int) -> int:
        """
            精彩
        """
        if n==0 or n==1:
            return 1
        a=b=1
        for i in range(2,n+1):
            sum=a+b
            a=b
            b=sum
        return sum%1000000007

print(Solution().numWays(44))#134903163
print(Solution().numWays(7))