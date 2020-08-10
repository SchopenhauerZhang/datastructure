from typing import List
class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        """
            个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。

 

            示例 1：

            输入：nums = [4,1,4,6]
            输出：[1,6] 或 [6,1]
            示例 2：

            输入：nums = [1,2,10,4,1,4,3,3]
            输出：[2,10] 或 [10,2]

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not nums or len(nums) <= 2:
            return [] if not nums  or len(nums) == 2 and nums[0] == nums[-1] else nums
        _res = []
        pre = None
        flag = False
        print(sorted(nums))
        for _num in sorted(nums):
            if pre and flag and _num != pre:
                _res.append(pre)
                pre = _num
                flag = True
            elif not pre and not flag:
                pre = _num
                flag = True
            elif pre and flag and _num == pre:
                pre = None
                flag = False
        if pre and flag and pre:
            _res.append(pre)
    
        return _res

    def _singleNumbers_eg(self, nums: List[int]) -> List[int]:
        val_dict = dict()
        for val in nums:
            if val in val_dict:
                del val_dict[val]
            else:
                val_dict[val] = 1
        return list(val_dict.keys())

#print(Solution().singleNumbers([1,2,4,5,4,5]))