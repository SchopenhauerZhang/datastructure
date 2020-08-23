from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

        说明：解集不能包含重复的子集。

        示例:

        输入: nums = [1,2,3]
        输出:
        [
        [3],
          [1],
          [2],
          [1,2,3],
          [1,3],
          [2,3],
          [1,2],
          []
        ]

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/subsets
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        精彩
        """

        if not nums or len(nums) == 1:
            return [] if not nums else [[],[nums[0]]]
        
        
        self.results = []
        self.search(sorted(nums), [], 0)
        return self.results
    
    def search(self, nums, S, index):
        print(S)
        if index == len(nums):
            self.results.append(S)
            return
        
        self.search(nums, S + [nums[index]], index + 1)
        self.search(nums, S, index + 1)
    
    # 回溯 O(N*2^N) O(N*2^N)
    def _subsets_eg(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first = 0, curr = []):
            if len(curr) == k:  
                return output.append(curr[:])
            for i in range(first, n):
                curr.append(nums[i])
                backtrack(i + 1, curr)
                curr.pop()
        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack()
        return output
