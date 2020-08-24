from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
            给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

             

            示例:

            输入: [1,2,3,4]
            输出: [24,12,8,6]
             

            提示：题目数据保证数组之中任意元素的全部前缀元素和后缀（甚至是整个数组）的乘积都在 32 位整数范围内。

            说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。

            进阶：
            你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/product-of-array-except-self
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        from functools import reduce
        if not nums or len(nums) <= 2:
            if nums and len(nums)==2:
                return [nums[1],nums[0]]

            return [1] if nums and len(nums)==1 else []
        ll = len(nums)
        i = 0
        res = [0]* ll
        while i < ll:
            res[i] = reduce(lambda x,y:x*y,nums[:i]+nums[i+1:]) 
            i += 1
        return res

    def _productExceptSelf(self, nums: List[int]) -> List[int]:
        """
            精彩
        """
        n = len(nums)
        res = [0] * n
        res[0] = 1
        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]
        right = 1
        for i in range(n - 1, -1, -1):
            res[i] *= right
            right *= nums[i]
        return res
    
    def _productExceptSelf_eg(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answers = [0] * length

        answers[0] = 1
        for i in range(1,length):
            answers[i] = answers[i-1] * nums[i-1]
        
        R = 1
        for i in reversed(range(length)):
            answers[i] = answers[i] * R
            R = nums[i] * R
        return answers