from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
            给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

            你的算法时间复杂度必须是 O(log n) 级别。

            如果数组中不存在目标值，返回 [-1, -1]。

            示例 1:

            输入: nums = [5,7,7,8,8,10], target = 8
            输出: [3,4]
            示例 2:

            输入: nums = [5,7,7,8,8,10], target = 6
            输出: [-1,-1]

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if target not in nums or not nums or  target  is None or len(nums) <=  2:
            
            if len(nums) == 2 and target in nums:
                return [0,1] if nums[0] == target and nums[1] == target else [nums.index(target),nums.index(target)]
            
            return [0,0] if len(nums) == 1 and nums[0] == target else [-1,-1]
        
        return [nums.index(target),len(nums)-1-nums[nums.index(target)+1:][::-1].index(target)    ] if target in nums[nums.index(target)+1:][::-1] else  [nums.index(target),nums.index(target)]

    def helper(self, nums, target, isLeft):
        low = 0
        high = len(nums) - 1
        while(high >= low):
            mid = (high + low) // 2
            #print(nums[low], nums[high], nums[mid])
            # 如何寻找最左边的target，碰见了以后依然往左递归。
            if nums[mid] > target or (isLeft and nums[mid] == target):
                high = mid - 1
            else:
                low = mid + 1
        return low

    def _searchRange_eg(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0: return [-1,-1]
        left = self.helper(nums, target, True)
        # 找不到
        if left == len(nums) or nums[left] != target:
            return [-1,-1]
        return [left, self.helper(nums, target, False)-1]