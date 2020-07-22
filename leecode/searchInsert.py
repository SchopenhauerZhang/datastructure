class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        """
        给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

        你可以假设数组中无重复元素。

        示例 1:

        输入: [1,3,5,6], 5
        输出: 2
        示例 2:

        输入: [1,3,5,6], 2
        输出: 1
        示例 3:

        输入: [1,3,5,6], 7
        输出: 4
        示例 4:

        输入: [1,3,5,6], 0
        输出: 0

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/search-insert-position
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not nums or target <= nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        if len(nums) == 1:
            return 0 if nums[0] >= target else 1
        for num in range(1,len(nums)):
            if target <= nums[num]:
                return num

        return len(nums)

# print(Solution().searchInsert([1,3],1))
# print(Solution().searchInsert([1,2,3,5,6],5))
# print(Solution().searchInsert([1,2,3,4,5,6],8))

    def _searchInsert_eg(self, nums: list, target: int) -> int:
        for i in nums:
            if i >= target:
                return nums.index(i)
        return len(nums)

