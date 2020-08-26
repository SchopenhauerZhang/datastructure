from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """ 
            给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

 

示例：

输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
 

提示：

3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum-closest
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        
        nums.sort()
   
        res = nums[0] + nums[1] + nums[2]
        
        for i in range(len(nums)-2):
            l, r = i+1, len(nums)-1
            while l<r:
                sum = nums[i] + nums[l] + nums[r]
                if sum == target:
                    return sum
                if abs(res-target)>abs(sum-target):
                    res = sum
                if sum<target:
                    l += 1
                else:
                    r -= 1
        return res
    
    def _threeSumClosest_eg(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = sum(nums[:3])
        for i in range(len(nums)-2):
            if i>1 and nums[i]==nums[i-1]:
                continue
            l, r = i+1, len(nums)-1

            if nums[i]+nums[r-1]+nums[r] <= target:
                l = r-1
            elif nums[i]+nums[l]+nums[i+1] >=target:
                r = l+1
            
            while(l<r):
                cur = nums[i]+nums[l]+nums[r]
                if abs(target-cur) < abs(target- res):
                    res = cur
                if cur>target:
                    r = r-1
                elif cur<target:
                    l = l+1
                else:
                    return target
        return res