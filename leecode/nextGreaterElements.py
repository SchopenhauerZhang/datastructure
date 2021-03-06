class Solution:
    def nextGreaterElements(self, nums: list) -> list:
        """
        给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。数字 x 的下一个更大的元素是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1。

        示例 1:

        输入: [1,2,1]
        输出: [2,-1,2]
        解释: 第一个 1 的下一个更大的数是 2；
        数字 2 找不到下一个更大的数； 
        第二个 1 的下一个最大的数需要循环搜索，结果也是 2。
        注意: 输入数组的长度不会超过 10000。

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/next-greater-element-ii
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        pass

    def _nextGreaterElements(self, nums : list) -> list:
        # 非循环搜索
        if len(nums) <= 1:
            return nums
        if len(nums) <= 2:
            return  [nums[1],-1] if nums[0] < nums[1] else [-1,nums[0]]
        l = len(nums)-1
        stack = list()
        res = list()
        for _ in range(l+1):
            res.append(-1)

        while nums:
            _data = nums.pop()
            while stack and stack[len(stack)-1] <= _data:
                stack.pop()
            #res.append(stack[len(stack)-1] if stack else -1)
            res[l] = stack[len(stack)-1] if stack else -1
            stack.append(_data)
            l -= 1

        return res
#print(Solution()._nextGreaterElements([1,2,1]))

    def _nextGreaterElements_circle(self, nums : list) -> list:
        # 循环搜索
        if not nums:
            return []
        if len(nums) <= 1:
            return [-1]
        if len(nums) <= 2:
            if nums[0] == nums[1]: return [-1,-1]
            return  [nums[1],-1] if nums[0] < nums[1] else [-1,nums[0]]

        ol = len(nums)
        l = (len(nums)-1)
        stack = list()
        res = list()
        for _ in range(l+1):
            res.append(-1)
        
        for i in range(len(nums)*2,0,-1):
            while stack and stack[len(stack)-1] <= nums[i%ol]:
                stack.pop()
            #res.append(stack[len(stack)-1] if stack else -1)
            res[i%ol] = stack[len(stack)-1] if stack else -1
            stack.append(nums[i%ol])
        
        return res
#print(Solution()._nextGreaterElements_circle([1,2,1]))
#print(Solution()._nextGreaterElements_circle([1,2,3,4,3]))

    def _nextGreaterElements_eg(self, nums : list) -> list:
        n = len(nums)
        stack = []
        res = [-1] * n
        for i in range(n):
            while stack and nums[i] > nums[stack[-1]]:
                res[stack.pop()] = nums[i]
            stack.append(i)

        for i in range(n):
            while stack and nums[i] > nums[stack[-1]]:
                res[stack.pop()] = nums[i]

        return res







