class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        """
            给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。

            按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

            "123"
            "132"
            "213"
            "231"
            "312"
            "321"
            给定 n 和 k，返回第 k 个排列。

            说明：

            给定 n 的范围是 [1, 9]。
            给定 k 的范围是[1,  n!]。
            示例 1:

            输入: n = 3, k = 3
            输出: "213"
            示例 2:

            输入: n = 4, k = 9
            输出: "2314"

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/permutation-sequence
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        candidate_digits = list(range(1,n+1))
        # [0!,...,(n-1)!]
        factos = [1] + list(accumulate(candidate_digits[:-1],lambda x,y: x*y))
        res = []
        for f in reversed(factos):
            # 用k除以当前阶乘值即可算出当前应该选哪一个数字
            id = math.ceil(k / f) - 1
            res.append(candidate_digits[id])
            k = k % f
            del candidate_digits[id]
        return ''.join([str(i) for i in res])

    def _getPermutation_eg(self, n: int, k: int) -> str:
        """
            同上，没看懂
        """

        num = [str(i) for i in range(1, n+1)]
        res, n = '', n-1
        import math
        while n > -1:
            t = math.factorial(n)# 6,2,1
            index = math.ceil(k/t) - 1
            res += num[index]
            num.pop(index)
            k %= t
            n -= 1
        return res

    


