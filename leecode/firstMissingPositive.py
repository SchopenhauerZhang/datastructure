from typing import List
class Solution:
    def firstMissingPositive(self,nums:List[int]):
        """
            41.给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。
            7,8,9,11,12 => 10
            1,2,0 => 3
        """
        if not nums or len(nums) <= 1:
            return nums[0]-1 if nums[0] > 2 else 1
        num = sorted(nums)
        if num[-1] <= 1 :
            return 1 if num[-1] < 1 else 2
        _min = num[-1]
        for i in num[::-1]:
            if i < 0:
                return _min
            if i >=  2 and i-1 not in num and i != num[0]:
                _min = min([ _min,  i-1])  
        
        if _min == num[-1]:
            _min += 1
        return _min



print(Solution().firstMissingPositive([7,8,9,11,12]))
print(Solution().firstMissingPositive([-1,1,3]))
print(Solution().firstMissingPositive([3,4,-1,1]))
print(Solution().firstMissingPositive([1,2,0]))