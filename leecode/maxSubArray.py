from typing import List
class Solution:
    def maxSubArray(self, nums: list) -> int:
        """
        给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

        示例:

        输入: [-2,1,-3,4,-1,2,1,-5,4],
        输出: 6
        解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
        进阶:

        如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/maximum-subarray
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums.pop()
        if len(nums) == 2:
            return nums[0]+nums[1] if nums[0] > 0 and nums[1] > 0 else max(nums[0],nums[1])

        _sum = 0

        res = float("-inf")

        for i in nums:
            _sum = max(i,i+_sum)

            res = max(res,_sum)
        return res

# print(Solution().maxSubArray([1,-1,-2]))
# print(Solution().maxSubArray([-2,-3,-1]))
# print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    
    def _maxSubArray_eg(self, nums: list) -> int:
        temp=nums[0]
        max_=temp
        for i in range(1,len(nums)):
            if temp>0:                
                temp+=nums[i]
                max_=max(max_,temp)

            else:
                temp=nums[i]
                max_=max(max_,temp)
        return max_

    def _maxSubArray_42(self, nums: List[int]) -> int:
        """
        输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

        要求时间复杂度为O(n)。

         

        示例1:

        输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
        输出: 6
        解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not nums or len(nums) <= 2:
            if len(nums) == 2  :
                return sum(nums) if nums[0] > 0  and nums[1] > 0 else max(nums[0],nums[1])
            return nums if len(nums) == 1 else  0
        res = 0

        for i in nums:
            if res + i >= res:
                res = max(res + i,res)
            else:
                res = max(res,i)

        return res

    def _maxSubArray_42_eg(self, nums: List[int]) -> int:
        t = max = -100
        for i in nums:
            if t <= 0:
                t = 0
            t += i
            if t > max:
                max = t
        return max






