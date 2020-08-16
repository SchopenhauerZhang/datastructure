from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
            给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

            示例:

            输入: [0,1,0,3,12]
            输出: [1,3,12,0,0]
            说明:

            必须在原数组上操作，不能拷贝额外的数组。
            尽量减少操作次数。
            通过次数192,353提交次数310,145

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/move-zeroes
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not nums or len(nums) <= 2:
            if len(nums) == 2 and nums[0]==0 and nums[1] != 0 :
                
                nums[0],nums[1] = nums[1],nums[0]
                print(nums)
        else:
            n = len(nums)-1
            i = 0
            j = 0
            while j < n:
                if nums[i] == 0:
                    nums.append(nums.pop(i))
                else:
                    i += 1
                j += 1
    def _moveZeroes_eg(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if not nums:
            return
        
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1