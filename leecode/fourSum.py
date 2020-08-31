from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
            四数之和
            给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

            注意：

            答案中不可以包含重复的四元组。

            示例：

            给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

            满足要求的四元组集合为：
            [
            [-1,  0, 0, 1],
            [-2, -1, 1, 2],
            [-2,  0, 0, 2]
            ]

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/4sum
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
            超出时间限制
        """
        if not nums or target is None:
            return []
        ll =  len(nums)
        nums = sorted(nums)
        res = set()
        for i in range(ll-3):
            if i>= 1 and nums[i-1] == nums[i]:
                continue
            for j in range(i+1,ll-2):
                for k in range(j+1,ll-1):
                    for v in range(k+1,ll):
                        if nums[i] + nums[j] + nums[k] + nums[v] == target and '#'.join([str(nums[i]),str(nums[j]),str(nums[k]),str(nums[v])]) not in res:
                            res.add('#'.join([str(nums[i]),str(nums[j]),str(nums[k]),str(nums[v])]))
        _res = []
        for i in res:
            __res = i.split('#')
            _res.append([int(j) for j in __res])
        print(_res)
        return _res

    