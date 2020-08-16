class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        """
                两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。

给出两个整数 x 和 y，计算它们之间的汉明距离。

注意：
0 ≤ x, y < 231.

示例:

输入: x = 1, y = 4

输出: 2

解释:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

上面的箭头指出了对应二进制位不同的位置。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/hamming-distance
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if x == y:
            return 0
        x = bin(x)
        y = bin(y)
        x = str(x).lstrip('0b')
        y = str(y).lstrip('0b')
        if len(str(x)) < len(str(y)):
            l = len(str(y))
            x = (l - len(str(x))) * '0' +str(x)
        elif len(str(x)) > len(str(y)):
            l = len(str(x))
            y = (l - len(str(y))) * '0' +str(y)
        else:
            l = len(str(x))

        _l = 0
        _x = list(str(x))
        _y = list(str(y))
        for i in range(l):
            if _x[i]!= _y[i]:
                _l += 1

        return _l 
    def _hammingDistance_eg(self, x: int, y: int) -> int:
        """
            精彩
        """
        return bin(x^y).count('1')
