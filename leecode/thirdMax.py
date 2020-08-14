from typing import List
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        """
            给定一个非空数组，返回此数组中第三大的数。如果不存在，则返回数组中最大的数。要求算法时间复杂度必须是O(n)。

            示例 1:

            输入: [3, 2, 1]

            输出: 1

            解释: 第三大的数是 1.
            示例 2:

            输入: [1, 2]

            输出: 2

            解释: 第三大的数不存在, 所以返回最大的数 2 .
            示例 3:

            输入: [2, 2, 3, 1]

            输出: 1

            解释: 注意，要求返回第三大的数，是指第三大且唯一出现的数。
            存在两个值为2的数，它们都排第二。

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/third-maximum-number
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        nums = list(set(nums))
        a = sorted(nums)[::-1][2:3] if len(nums) >= 3 else sorted(nums)[::-1] 
        return a[0] if len(a) == 1 else a[0]

    def _thirdMax_eg(self, nums: List[int]) -> int:
        nums.sort()
        nums.reverse()
        i=0
        while i+1<len(nums) and nums[i]==nums[i+1]:
            i+=1
        if i+1>=len(nums):
            return nums[0]
        i+=1
        while i+1<len(nums) and nums[i]==nums[i+1]:
            i+=1
        if i+1>=len(nums):
            return nums[0]
        return nums[i+1]



