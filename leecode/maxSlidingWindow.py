from typing import List
class Solution:
    def maxSlidingWindow(self, nums: list, k: int) -> list:
        """
        给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

        返回滑动窗口中的最大值。

         

        进阶：

        你能在线性时间复杂度内解决此题吗？

         

        示例:

        输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
        输出: [3,3,5,5,6,7] 
        解释: 

        滑动窗口的位置                最大值
        ---------------               -----
        [1  3  -1] -3  5  3  6  7       3
        1 [3  -1  -3] 5  3  6  7       3
        1  3 [-1  -3  5] 3  6  7       5
        1  3  -1 [-3  5  3] 6  7       5
        1  3  -1  -3 [5  3  6] 7       6
        1  3  -1  -3  5 [3  6  7]      7
         

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/sliding-window-maximum
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        pass

    def _maxSlidingWindow(self, nums, k) -> list:
        if k <= 0  or len(nums) <= 0 or k> len(nums):
            return []
        if k == 1:
            return nums

        window = []
        res = list()
        s = k
        for i in range(len(nums)):
            if i <= s-1:
                window.append(nums[i])
            else:
                res.append(max(window))
                window.pop(0)
                window.append(nums[i])
        res.append(max(window))
        return res

#print(Solution()._maxSlidingWindow([1,3,-1,-3,5,3,6,7],3))

    def _maxSlidingWindow_time_limit(self, nums, k) -> list:
        if k <= 0  or len(nums) <= 0 or k> len(nums):
            return []
        if k == 1:
            return nums
        
        def _push(win,i):
            if win:
                while win and win[len(win)-1] < i:
                    win.pop()
            win.append(i)
        def _max(win):
            return win[0]
        def _pop(win,i):
            if win:
                while win and win[0] == i:
                    win.pop(0)
                    break
                
        window = []
        res = list()
        s = k
        for i in range(len(nums)):
            if i < s-1:
                _push(window,nums[i])
            else:
                _push(window,nums[i])
                res.append(_max(window))
                _pop(window,nums[i-s+1])
                
        return res
# print(Solution()._maxSlidingWindow_time_limit([-7,-8,7,5,7,1,6,0],4))
# print(Solution()._maxSlidingWindow_time_limit([1,3,-1,-3,5,3,6,7],3))
# print(Solution()._maxSlidingWindow_time_limit([9,7,1,3,-1,-3,5,3,6,7],3))
# print(Solution()._maxSlidingWindow_time_limit([7,2,4],2))

    def _maxSlidingWindow_eg(self, nums, k) -> list:
        if k==1:
            return nums
        n=len(nums)
        
        tmp=[nums[0]]
        for i in range(1,k):
            if nums[i]>tmp[-1]:
                tmp.append(nums[i])
        res=[tmp[-1]]
        for i in range(k,n):
            if nums[i-k]>=tmp[0]:
                tmp.pop(0)
            if tmp==[]:
                tmp.append(max(nums[i-k+1:i+1]))
            elif nums[i]>tmp[-1]:
                tmp.append(nums[i])

            res.append(tmp[-1])
        return res
    
    def _maxSlidingWindow_59(self, nums: List[int], k: int) -> List[int]:
        """
                给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。

            示例:

            输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
            输出: [3,3,5,5,6,7] 
            解释: 

            滑动窗口的位置                最大值
            ---------------               -----
            [1  3  -1] -3  5  3  6  7       3
            1 [3  -1  -3] 5  3  6  7       3
            1  3 [-1  -3  5] 3  6  7       5
            1  3  -1 [-3  5  3] 6  7       5
            1  3  -1  -3 [5  3  6] 7       6
            1  3  -1  -3  5 [3  6  7]      7

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not nums or k >= len(nums) or  k == 0 or k == 1:
            return nums if  not nums or k == 0 or k == 1 else  max(nums)
        
        l,r = 0,len(nums)-1
        tmp = []
        res = []
        while l <= r:
            if len(tmp) <k:
                tmp.append(nums[l])
                l += 1
            elif len(tmp) ==k:
                res.append(max(tmp))
                tmp.pop(0)

        if len(tmp) ==k:
                res.append(max(tmp))
        return res

    def _maxSlidingWindow_59_eg(self, nums: List[int], k: int) -> List[int]:
        if nums==[]:
            return []
        if k==0:
            return
        res = [0]*(len(nums)-k+1)
        left,m,right=0,0,k-1
        for i in range(k):
            if nums[i]>=nums[m]:
                m=i
        res[0] = nums[m]
        for i in range(1,len(nums)-k+1):
            left+=1
            right+=1
            if nums[right]>=nums[m]:
                m=right
            if m==left-1:
                m=left
                for j in range(left,right+1):
                    if nums[j]>=nums[m]:
                        m=j
            res[i]=nums[m]
        return res
            


        






