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

# print(Solution().missingNumber([0,1,2,3,4,5,6,7,9]))
# print(Solution().missingNumber([0,1,2,3,4,5,6,7,8,9,10,11,13]))
# print(Solution().missingNumber([0,1,2]))

    def missingNumber_1704(self, nums: List[int]) -> int:
        if not nums or len(nums) == 1:
            return 0 if (nums and nums[0]!= 0) or not nums else 1
        i = 0
        while True:
            if i not in nums:
                return i
            else:
                i += 1
        
    def missingNumber_1704(self, nums: List[int]) -> int:
        total=(0+len(nums))*(len(nums)+1)/2
        actual=0
        for i in range(len(nums)):
            actual=actual+nums[i]
        output=int(total-actual)
        return output

    def missingNumber_268(self, nums: List[int]) -> int:
        """
            给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。

             

            示例 1:

            输入: [3,0,1]
            输出: 2
            示例 2:

            输入: [9,6,4,2,3,5,7,0,1]
            输出: 8

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/missing-number
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        n = len(nums)
        return int(n*(n+1)/2-sum(nums))
    
    def missingNumber_268_eg(self, nums: List[int]) -> int:
        nums_total = sum(nums)
        length = len(nums)
        total = (length * (length+1)) // 2
        return total - nums_total
