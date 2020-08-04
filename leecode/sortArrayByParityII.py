from typing import List
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        """
            给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。

            对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。

            你可以返回任何满足上述条件的数组作为答案。

             

            示例：

            输入：[4,2,5,7]
            输出：[4,5,2,7]
            解释：[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/sort-array-by-parity-ii
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not A:
            return None
        _ord = []
        _ord_ = []
        for  i in A:
            if i %2==0:
                _ord.append(i)
            else:
                _ord_.append(i)
        res = []
        i = len(_ord)
        while i :
            res.append(_ord.pop())
            res.append(_ord_.pop())
            
            i -=1
        return res

#print(Solution().sortArrayByParityII([4,2,5,7]))

    def _sortArrayByParityII_eg(self, A: List[int]) -> List[int]:
        n = len(A)
        i = 1
        for j in range(0, n, 2):
            if A[j] % 2 == 1:
                while A[i] % 2:
                    i += 2
                A[i], A[j] = A[j], A[i]
                
        return A