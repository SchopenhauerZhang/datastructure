class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
            给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

            示例 1:

            输入: 1
            输出: true
            解释: 20 = 1
            示例 2:

            输入: 16
            输出: true
            解释: 24 = 16
            示例 3:

            输入: 218
            输出: false

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/power-of-two
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if n is None or n==0 or n == 1:
            return True if n== 1 else False
        i = 0
        _max = 2 **i
        while _max < n:
            i += 1
            _max = 2 ** i
            if _max == n:
                return True
        return False
    
    def isPowerOfTwo1(self, n: int) -> bool:
        if n <= 0:
            return False
        while n >= 2:
            if n % 2 == 1:
                return False
            n //= 2
        return True

    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n-1) == 0)