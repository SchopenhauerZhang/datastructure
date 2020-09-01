from typing import List
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        """
            输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

            序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

             

            示例 1：

            输入：target = 9
            输出：[[2,3,4],[4,5]]
            示例 2：

            输入：target = 15
            输出：[[1,2,3,4,5],[4,5,6],[7,8]]
             

            限制：

            1 <= target <= 10^5

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if target is None or target == 0:
            return [] if target is None else []
        if target <= 3:
            return [[1,2]] if target == 3 else []
        dp = [i for i in range(1,target)]
        
        l,r = 0,1
        res = []
        while l < r and r < target:
            
            if sum(dp[l:r+1]) < target:
                r = r+1
            elif sum(dp[l:r+1]) == target:
                if dp[l:r+1] not in res:
                    res.append(dp[l:r+1])
                r += 1
            else:
                while l < r:
                    l += 1
                    if sum(dp[l:r+1]) < target:
                        break
                    elif sum(dp[l:r+1]) == target:
                        
                        if dp[l:r+1] not in res:
                            res.append(dp[l:r+1])
        return list(res)
    
    def _findContinuousSequence_eg(self, target: int) -> List[List[int]]:
        if target <= 2:
            return []
        res = []
        for i in range(2, target + 1):
            linshi = target - i * (i - 1) // 2
            if linshi <= 0:
                break
            if not linshi % i:
                start = linshi // i
                res.append([start+j for j in range(i)])
        return res[::-1]