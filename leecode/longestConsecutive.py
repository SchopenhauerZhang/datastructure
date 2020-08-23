from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
            给定一个未排序的整数数组，找出最长连续序列的长度。

            要求算法的时间复杂度为 O(n)。

            示例:

            输入: [100, 4, 200, 1, 3, 2]
            输出: 4
            解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/longest-consecutive-sequence
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not nums or len(nums) <= 2:
            if nums and len(nums) == 2:
                return 2 if abs(nums[0]-nums[1]) == 1 else 1
            return  0 if not nums else 1
        _length = 0
        for num in nums:
            if num - 1 not in nums:
                __length = 1
                _num = num +1
                while _num in nums:
                    _num += 1
                    __length += 1
                _length = max(_length,__length) 
        return _length
    
    def _longestConsecutive_eg(self, nums: List[int]) -> int:
        max_len = 0
        if not len(nums):
            return 0
        else:
            a = 1
            nums = list(set(nums))
            nums.sort()
            for i in range(1,len(nums)):
                if nums[i] - nums[i-1] != 1:
                    a = 0
                a += 1
                max_len = max(max_len,a)
            max_len = max(max_len,a)
            return max_len
    

