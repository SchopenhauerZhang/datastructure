from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
            给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

 

示例：

给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if len(nums) <= 3:
            return [] if len(nums) <= 2 or nums[0]+nums[1]+nums[2] != 0 else   [nums]
        # 双指针
        num = sorted(nums)
        if num[0] > 0 :
            return []
        res = []
        l,r = 0,len(num)-1
        for i in range(len(num)-2):
            l = i+1
            r = len(num)-1
            while l < r:
                if num[i] + num[l] + num[r] == 0:
                    if [num[i] , num[l] , num[r]] not in res:
                        res.append([num[i] , num[l] , num[r]])
                        while l < r and num[l] == num[l+1]: 
                            l += 1
                        while l < r and num[r] == num[r-1]: 
                            r -= 1
                    r -= 1
                    l += 1 
                else:
                    if num[i] + num[l] + num[r] > 0:
                        r -= 1
                    elif num[i] + num[l] + num[r] < 0:
                        l += 1
        return res
    
    def _threeSum_eg(self, nums: List[int]) -> List[List[int]]:
        ans = []
        counts = {}
        for i in nums:
            counts[i] = counts.get(i, 0) + 1

        nums = sorted(counts)

        for i, num in enumerate(nums):
            if counts[num] > 1:
                if num == 0:
                    if counts[num] > 2:
                        ans.append([0, 0, 0])
                else:
                    if -num * 2 in counts:
                        ans.append([num, num, -2 * num])
            if num < 0:
                two_sum = -num
                left = bisect.bisect_left(nums, (two_sum - nums[-1]), i + 1)
                for i in nums[left: bisect.bisect_right(nums, (two_sum // 2), left)]:
                    j = two_sum - i
                    if j in counts and j != i:
                        ans.append([num, i, j])

        return ans