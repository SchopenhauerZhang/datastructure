class Solution:
    def arrangeCoins(self, n: int) -> int:
        """
            你总共有 n 枚硬币，你需要将它们摆成一个阶梯形状，第 k 行就必须正好有 k 枚硬币。

            给定一个数字 n，找出可形成完整阶梯行的总行数。

            n 是一个非负整数，并且在32位有符号整型的范围内。

            示例 1:

            n = 5

            硬币可排列成以下几行:
            ¤
            ¤ ¤
            ¤ ¤

            因为第三行不完整，所以返回2.
            示例 2:

            n = 8

            硬币可排列成以下几行:
            ¤
            ¤ ¤
            ¤ ¤ ¤
            ¤ ¤

            因为第四行不完整，所以返回3.

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/arranging-coins
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not n or n == 1:
            return 1 if n == 1 else 0
        if n ==3 :
            return 2
        _sum = 0
        _res = 0
        for i in range(1,n//2 + 1):
            _sum += i
            _res += 1
            if n - _sum <= i:
                return _res
        return _res
        
    def _arrangeCoins_441_eg(self, n: int) -> int:
        left, right = 0, n
        while left <= right:
            k = (right + left) // 2
            curr = k * (k + 1) // 2
            if curr == n:
                return k
            if n < curr:
                right = k - 1
            else:
                left = k + 1
        return right
