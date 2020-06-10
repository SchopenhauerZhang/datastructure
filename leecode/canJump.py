class Solution:
    def canJump(self, nums: list) -> bool:
        """
        给定一个非负整数数组，你最初位于数组的第一个位置。

        数组中的每个元素代表你在该位置可以跳跃的最大长度。

        判断你是否能够到达最后一个位置。

        示例 1:

        输入: [2,3,1,1,4]
        输出: true
        解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
        示例 2:

        输入: [3,2,1,0,4]
        输出: false
        解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。

        """
        pass

    def _canJump(self, nums: list) -> bool:
        if len(nums) <= 1:
            return True if nums[0] <0  else False 
        if len(nums) == 2:
            return  True if nums[0]>=1  else False
        max_dis = 0
        for i in range(len(nums)-1):
            print(nums[i])
            max_dis = max(max_dis,i+nums[i])
            if max_dis <= i:
                return False
        return True
#print(Solution()._canJump([3,0,1,0,4]))

    def _canJump_better_eg(self, nums: list) -> bool:
        n=len(nums)
        if n<=1 or 0 not in nums:
            return True
        for i in range(n-2,-1,-1):
            if nums[i]==0:
                for j in range(i):
                    if j+nums[j]>i:
                        break
                else:
                    return False
        return True
