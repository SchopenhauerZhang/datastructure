class Solution:
    def containsDuplicate(self, nums: list) -> bool:
        """

            给定一个整数数组，判断是否存在重复元素。

            如果任意一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。

            

            示例 1:

            输入: [1,2,3,1]
            输出: true
            示例 2:

            输入: [1,2,3,4]
            输出: false
            示例 3:

            输入: [1,1,1,3,3,4,3,2,4,2]
            输出: true
        """
        return True if abs(sum(set(nums))) <= abs(sum(nums)) and len(nums) > len(set(nums))   else False
        
#print(Solution().containsDuplicate([1,2,3,1]))
#print(Solution().containsDuplicate([0,4,5,0,3,6]))
#print(Solution().containsDuplicate([-1200000005,-1200000005]))

    def _containsDuplicate_eg(self, nums: list) -> bool:
        my_set = set()
        for i in range(len(nums)):
            if nums[i] in my_set:
                return True
            else:
                my_set.add(nums[i])
        return False