class Solution:
    def jump(self, nums: list) -> int:
        """
        给定一个非负整数数组，你最初位于数组的第一个位置。

        数组中的每个元素代表你在该位置可以跳跃的最大长度。

        你的目标是使用最少的跳跃次数到达数组的最后一个位置。

        示例:

        输入: [2,3,1,1,4]
        输出: 2
        解释: 跳到最后一个位置的最小跳跃数是 2。
             从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
        说明:

        假设你总是可以到达数组的最后一个位置。

        """
        pass

    def _jump(self, nums: list) -> int:
        if len(nums) <= 1:
            return 0
        if len(nums) == 2:
            return 1 
        def dp(p,nums):
           
            if p >= len(nums)-1:
                return 0
            if mem[p] != len(nums):
                return mem[p]
            
            
            for i in range(1,nums[p]+1):
                next_pos = min(mem[p],dp(i+p,nums)+1)
                mem[p] = next_pos

            return mem[p]

        mem = dict()
        for j in range(len(nums)+2):
            mem[j] = len(nums)
        
        return dp(0,nums)
#print(Solution()._jump([7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]))
    
    def _jump_tanxin(self, nums: list) -> int:
        if len(nums) <= 1:
            return 0
        if len(nums) == 2:
            return 1 
        max_steps = 0
        j_step = 0
        x = 0
        for i in range(len(nums)-1):
            max_steps = max(nums[i]+i,max_steps)
            if x == i:
                j_step += 1
                x = max_steps

        return j_step
# print(Solution()._jump_tanxin([7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]))
# print(Solution()._jump_tanxin([2,3,1,1,4]))

    def _jump_tanxin(self, nums: list) -> int:
        reach, end, count = 0, 0, 0
        for i in range(len(nums) - 1):
            if i <= reach:
                reach = max(reach, nums[i] + i)
                if i == end:
                    end =reach
                    count += 1

        return count

