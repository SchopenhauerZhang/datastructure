class Solution:
    def removeElement(self, nums: list, val: int) -> int:
        """
        给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。

        不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。

        元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

         

        示例 1:

        给定 nums = [3,2,2,3], val = 3,

        函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。

        你不需要考虑数组中超出新长度后面的元素。

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/remove-element
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not nums or val not in nums:
            return len(nums)
        l = 0
        for r in range(len(nums)):
            if nums[r] != val:
                nums[l] = nums[r]
                l += 1
        return l

#print(Solution().removeElement([3,2,2,3],3))

    def _removeElement_eg(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)-1,-1,-1):
            if nums[i]==val:
                del nums[i]
        return len(nums)