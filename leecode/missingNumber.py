from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
            一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。

             

            示例 1:

            输入: [0,1,3]
            输出: 2
            示例 2:

            输入: [0,1,2,3,4,5,6,7,9]
            输出: 8

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/que-shi-de-shu-zi-lcof
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if 0 not in nums:
            return 0
        
        return ((1+nums[-1])*(nums[-1])//2) - sum(nums) if ((1+nums[-1])*(nums[-1])//2) != sum(nums)  else nums[-1]+1

    def _missingNumber_eg(self, nums: List[int]) -> int:
        a = len(nums)                                
        for i in range(a):                           
            if i != nums[i]:                       
                if i == 0 and nums[0] == 1:       
                    return 0                     
                else:                             
                    return i                      
        return i+1

print(Solution().missingNumber([0,1,2,3,4,5,6,7,9]))
print(Solution().missingNumber([0,1,2,3,4,5,6,7,8,9,10,11,13]))
print(Solution().missingNumber([0,1,2]))
