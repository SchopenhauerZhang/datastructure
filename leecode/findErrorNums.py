class Solution:
    def findErrorNums(self, nums: list) -> list:
        """
        集合 S 包含从1到 n 的整数。不幸的是，因为数据错误，导致集合里面某一个元素复制了成了集合里面的另外一个元素的值，导致集合丢失了一个整数并且有一个元素重复。

        给定一个数组 nums 代表了集合 S 发生错误后的结果。你的任务是首先寻找到重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。

        示例 1:

        输入: nums = [1,2,2,4]
        输出: [2,3]

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/set-mismatch
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        pass

    def _findErrorNums(self, nums: list) -> list:
        if len(nums) == 2:
            if nums[0] == nums[1]:
                if 1 in nums:
                    return [1,2]
                else:
                    return [2,1]

        _nums = dict()
        res = []
        for i in range(1,len(nums)+1):
            _nums[i] = len(nums)+1
        for i in nums:
            if _nums[i] != len(nums)+1:
                res.append(i)
            else:
                _nums[i] = i

        for k,v in _nums.items():
            if v == len(nums)+1:
                res.append(k)
        
        return res
#print(Solution()._findErrorNums([1,2,2,4]))

    def _findErrorNums_eg(self, nums: list) -> list:
        #精彩
        return [sum(nums) - sum(set(nums)), sum(range(1, len(nums)+1)) - sum(set(nums))]

