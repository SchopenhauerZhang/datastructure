
from typing import List
class Solution:
    def twoSum(self, numbers: list, target: int) -> list:
        """
         给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

        函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

        说明:

        返回的下标值（index1 和 index2）不是从零开始的。
        你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
        示例:

        输入: numbers = [2, 7, 11, 15], target = 9
        输出: [1,2]
        解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        l,r = 0,len(numbers)-1
        for r in range(len(numbers)-1,0,-1):
            tmp = target-numbers[r]
            if tmp < numbers[0]:
                continue
            l = 0
            while l < r:
                if numbers[l] == tmp:
                    break
                else:
                    l += 1
            if l < r:
                break

        return (l+1,r+1) if l < r  else (-1,-1)

# print(Solution().twoSum([2, 7, 11, 15],17))
# print(Solution().twoSum([2, 7, 11, 15],9))
# print(Solution().twoSum([0,0,3,4],0))
# print(Solution().twoSum([12,13,23,28,43,44,59,60,61,68,70,86,88,92,124,125,136,168,173,173,180,199,212,221,227,230,277,282,306,314,316,321,325,328,336,337,363,365,368,370,370,371,375,384,387,394,400,404,414,422,422,427,430,435,457,493,506,527,531,538,541,546,568,583,585,587,650,652,677,691,730,737,740,751,755,764,778,783,785,789,794,803,809,815,847,858,863,863,874,887,896,916,920,926,927,930,933,957,981,997],542))

    def _twoSum(self, numbers: list, target: int) -> list:
        i = 0
        j = len(numbers)-1
        while j>i:
            if numbers[i]+numbers[j]==target:
                return [i+1, j+1]
            elif numbers[i]+numbers[j]<target:
                i+=1;
            else:
                j-=1
        return []

    def _twoSum_57(self, nums: List[int], target: int) -> List[int]:
        """
            输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。

             

            示例 1：

            输入：nums = [2,7,11,15], target = 9
            输出：[2,7] 或者 [7,2]
            示例 2：

            输入：nums = [10,26,30,31,47,60], target = 40
            输出：[10,30] 或者 [30,10]

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/he-wei-sde-liang-ge-shu-zi-lcof
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        i,r = 0,len(nums)-1
        while l < r:
            if target-nums[i] in nums[i+1:]:
                return [nums[i],target-nums[i]]
            else:
                i += 1
            if target-nums[r] in nums[:r]:
                return [nums[r],target-nums[r]]
            else:
                r -= 1
        
    def _twoSum_57_eg(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1
        split_index = (j + i) >> 1
        
        while i < j - 1:
            if nums[j] + nums[i] > target:            
                if nums[split_index] + nums[i] > target:
                    j = split_index - 1
                    split_index = (j + i) >> 1
                elif nums[split_index] + nums[i] < target:
                    j -= 1
                    split_index = (j + split_index) >> 1
                else:
                    return [nums[i], nums[split_index]]
            elif nums[j] + nums[i] < target:   
                if nums[split_index] + nums[j] < target:
                    i =  split_index + 1
                    split_index = (j + i) >> 1   
                elif nums[split_index] + nums[j] > target:
                    i += 1
                    split_index = (i + split_index) >> 1
                else:
                    return [nums[j], nums[split_index]]
            else:
                return [nums[i], nums[j]]

        if i == j - 1 and nums[j] + nums[i] == target:
            return [nums[i], nums[j]]
        else:
            return []

       