class Solution:
    def singleNumber(self, nums: list) -> int:
        """
        给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

        说明：

        你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

        示例 1:

        输入: [2,2,1]
        输出: 1
        示例 2:

        输入: [4,1,2,1,2]
        输出: 4

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/single-number
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        return sum(set(nums))*2 - sum(nums)

# print(Solution().singleNumber([2,2,1]))
# print(Solution().singleNumber([4,1,2,1,2]))

    def _singleNumber_eg(self, nums: list) -> int:
        if not nums:
            return -1

        n = nums[0]
        for i in range(1,len(nums)):
            n = n^nums[i]
        return n