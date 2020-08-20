from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
            给定一个 没有重复 数字的序列，返回其所有可能的全排列。

            示例:

            输入: [1,2,3]
            输出:
            [
            [1,2,3],
            [1,3,2],
            [2,1,3],
            [2,3,1],
            [3,1,2],
            [3,2,1]
            ]

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/permutations
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        import itertools
        return list(itertools.permutations(nums))
    
    def _permute_eg(self, nums: List[int]) -> List[List[int]]:
        res = []
        def cur(nums, temp):
            if not nums:
                res.append(temp)
                return
            for i in range(len(nums)):
                cur(nums[:i] + nums[i+1:], temp + [nums[i]])
        cur(nums, [])
        return res

     
# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         def backtrack(nums, tmp):
#             if not nums:
#                 res.append(tmp)
#                 return 
#             for i in range(len(nums)):
#                 #print(nums[:i] + nums[i+1:], tmp + [nums[i]], nums[:i],nums[i])
#                 backtrack(nums[:i] + nums[i+1:], tmp + [nums[i]])
#         backtrack(nums, [])
#         return res

#作者：powcai
#链接：https://leetcode-cn.com/problems/permutations/solution/hui-su-suan-fa-by-powcai-2/

#https://leetcode-cn.com/problems/permutations/solution/xiong-mao-shua-ti-python3-di-gui-qiu-jie-8xing-by-/
# 递归和回溯？

#https://leetcode-cn.com/problems/permutations/solution/hui-su-suan-fa-xiang-jie-by-labuladong-2/
#扒一扒回溯算法的裤子？