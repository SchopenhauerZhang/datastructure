class Solution:
    def hammingWeight(self, n: int) -> int:
        """
            编写一个函数，输入是一个无符号整数，返回其二进制表达式中数字位数为 ‘1’ 的个数（也被称为汉明重量）。

 

            示例 1：

            输入：00000000000000000000000000001011
            输出：3
            解释：输入的二进制串 00000000000000000000000000001011 中，共有三位为 '1'。
            示例 2：

            输入：00000000000000000000000010000000
            输出：1
            解释：输入的二进制串 00000000000000000000000010000000 中，共有一位为 '1'。

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/number-of-1-bits
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not n or n == 0 or n ==1:
            return 0 if n != 1 else 1
        return bin(n & 0xffffffff).count('1')
    
    def _hammingWeight_eg(self, n: int) -> int:
        count = 0
        while n:
            count += (n & 1)
            n = n >> 1
        return count
    
    def _hammingWeight_15(self, n: int) -> int:
        """
                请实现一个函数，输入一个整数，输出该数二进制表示中 1 的个数。例如，把 9 表示成二进制是 1001，有 2 位是 1。因此，如果输入 9，则该函数输出 2。

            示例 1：

            输入：00000000000000000000000000001011
            输出：3
            解释：输入的二进制串 00000000000000000000000000001011 中，共有三位为 '1'。
            示例 2：

            输入：00000000000000000000000010000000
            输出：1
            解释：输入的二进制串 00000000000000000000000010000000 中，共有一位为 '1'。
            示例 3：

            输入：11111111111111111111111111111101
            输出：31
            解释：输入的二进制串 11111111111111111111111111111101 中，共有 31 位为 '1'。

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if n == 0 or n ==1:
            return 0 if n != 1 else 1
        _res  = 0
        dict_2 = {
            2:1,
            4:1,
            8:1,
            16:1
        }
        if n in dict_2:
            return  dict_2[n]

        for i in list(str(bin(n)))[2:]:
            _res += 1 if i == '1' else 0
        return _res
    
    def _hammingWeight_15_eg(self, n: int) -> int:
        res = 0
        while n:
            res += n % 2
            n >>= 1
        return res