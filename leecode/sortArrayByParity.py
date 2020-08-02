from typing import List
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        """
            给定一个非负整数数组 A，返回一个数组，在该数组中， A 的所有偶数元素之后跟着所有奇数元素。

            你可以返回满足此条件的任何数组作为答案。

             

            示例：

            输入：[3,1,2,4]
            输出：[2,4,3,1]
            输出 [4,2,3,1]，[2,4,1,3] 和 [4,2,1,3] 也会被接受。
             

            提示：

            1 <= A.length <= 5000
            0 <= A[i] <= 5000

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/sort-array-by-parity
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not A or len(A) == 1:
            return A
        l = len(A)
        j =0
        for i in range(l):
            if A[j] % 2 !=0:
                A.append(A[j])
                
                del A[j]
            else:
                j += 1
                
        return A
# print(Solution().sortArrayByParity([3,1,2,4]))
# print(Solution().sortArrayByParity([0,1,2]))

    def _sortArrayByParity_eg(self, A: List[int]) -> List[int]:
        n = len(A)
        B = [0] * n
        i, j = 0, n-1
        for num in A:
            if num%2==0:
                B[i] = num
                i += 1
            else:
                B[j] = num
                j -= 1
        return B
