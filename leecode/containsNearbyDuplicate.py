from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
            给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的 绝对值 至多为 k。

             

            示例 1:

            输入: nums = [1,2,3,1], k = 3
            输出: true
            示例 2:

            输入: nums = [1,0,1,1], k = 1
            输出: true
            示例 3:

            输入: nums = [1,2,3,1,2,3], k = 2
            输出: false


            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/contains-duplicate-ii
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not nums or len(nums) <= 1:
            return False
        pre = -1
        from collections import defaultdict
        tmp = defaultdict(list)
        for i in range(len(nums)):
            if nums[i] not in tmp:
                tmp[nums[i]] = []
            tmp[nums[i]].append(i)
        if tmp:
            print(tmp)
            for _k,_val in tmp.items():
                if len(_val) > 1:
                    pre = 0
                    for i in range(1,len(_val)):
                        
                        if _val[i] - _val[pre] <= k:
                            print(_val,k)
                            return True
                        else:
                            pre = i
        return False

#print(Solution().containsNearbyDuplicate([2,2],3))
#print(Solution().containsNearbyDuplicate([1,0,1,1],1))
#print(Solution().containsNearbyDuplicate([1,2,3,1],3))
#print(Solution().containsNearbyDuplicate([1,2,3,1,2,3],2))
    def _containsNearbyDuplicate_eg(self, nums: List[int], k: int) -> bool:
        numMap = {}
        for i in range(len(nums)):
            index = numMap.get(nums[i])
            if index is not None and  i - index <= k:
                return True
            numMap[nums[i]] = i
        return False