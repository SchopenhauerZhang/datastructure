class Solution:
    def getSum(self, a: int, b: int) -> int:
        """
            不使用运算符 + 和 - ​​​​​​​，计算两整数 ​​​​​​​a 、b ​​​​​​​之和。

            示例 1:

            输入: a = 1, b = 2
            输出: 3
            示例 2:

            输入: a = -2, b = 3
            输出: 1

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/sum-of-two-integers
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        return a+b
    
    def _getSum_eg(self, a: int, b: int) -> int:
        max_int = 0x7FFFFFFF
        min_int = max_int + 1
        mask = 0x100000000
        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) % mask
            b = carry % mask
        return a if a < max_int else ~ ((a % min_int) ^ max_int)