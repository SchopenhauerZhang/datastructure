class Solution:
    def getNoZeroIntegers(self, n: int) ->list:
        """
        「无零整数」是十进制表示中 不含任何 0 的正整数。

        给你一个整数 n，请你返回一个 由两个整数组成的列表 [A, B]，满足：

        A 和 B 都是无零整数
        A + B = n
        题目数据保证至少有一个有效的解决方案。

        如果存在多个有效解决方案，你可以返回其中任意一个。

         

        示例 1：

        输入：n = 2
        输出：[1,1]
        解释：A = 1, B = 1. A + B = n 并且 A 和 B 的十进制表示形式都不包含任何 0 。
        示例 2：

        输入：n = 11
        输出：[2,9]
        示例 3：

        输入：n = 10000
        输出：[1,9999]

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        pass

    def _getNoZeroIntegers(self, n: int) ->list:
        res = list()
        for i in range(1,n):
            if '0' not in str(i) and '0' not in str(n-i):
                res.append(i)
                res.append(n-i)
                break

        return res
#print(Solution()._getNoZeroIntegers(1010))

    def _getNoZeroIntegers_eg(self, n: int) ->list:
        import random
        while (True):
            L = random.randint(1, n)
            R = n - L
            if '0' not in str(L) and '0' not in str(R):
                return [L, R]
     