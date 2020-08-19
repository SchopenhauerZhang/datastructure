from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
            给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

            candidates 中的数字可以无限制重复被选取。

            说明：

            所有数字（包括 target）都是正整数。
            解集不能包含重复的组合。 
            示例 1：

            输入：candidates = [2,3,6,7], target = 7,
            所求解集为：
            [
            [7],
            [2,2,3]
            ]
            示例 2：

            输入：candidates = [2,3,5], target = 8,
            所求解集为：
            [
              [2,2,2,2],
              [2,3,3],
              [3,5]
            ]
             

            提示：

            1 <= candidates.length <= 30
            1 <= candidates[i] <= 200
            candidate 中的每个元素都是独一无二的。
            1 <= target <= 500

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/combination-sum
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not candidates or not target:
            return []
        candidate = sorted(candidates)
        self.res = []
        def combin(nums,tgt,sub,_max):
            if not nums:
                return 
            if tgt == 0:
                self.res.append(sub)
            if tgt < nums[0]:
                return 
            
            for num in nums:
                if num > tgt:
                    return 
                if num < _max:
                    continue
                
                combin(nums,tgt-num,sub+[num],num)
        combin(candidate,target,[],0)
        return self.res

    def _combinationSum_eg(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target + 1)]
        dp[0] = [[]]
        for item in candidates:
            for tar in range(item,target + 1):
                for i in dp[tar - item]:
                    dp[tar].append(i + [item])
        return dp[target]