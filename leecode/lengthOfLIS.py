class Solution:
    def lengthOfLIS(self, nums: list) -> int:
        """
        给定一个无序的整数数组，找到其中最长上升子序列的长度。

        示例:

        输入: [10,9,2,5,3,7,101,18]
        输出: 4 
        解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
        说明:

        可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
        你算法的时间复杂度应该为 O(n2) 。
        进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/longest-increasing-subsequence
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if len(nums)<= 1:
            return 1 if  nums else 0
        if len(nums) == 2:
            return 2 if nums[1] > nums[0] else 1
         
        dp = [0]*len(nums)
        for i in range(len(nums)):
            max_v = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    max_v = max(max_v,dp[j])
            dp[i] = max_v+1
        print(dp)
        return max(dp)
#print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18]))

    def _lengthOfLIS(self, nums: list) -> int:
        n=len(nums)
        if n<2:
            return n
        tail=[nums[0]]
        for i in range(1,n):
            if nums[i]>tail[-1]:
                tail.append(nums[i])
            # 如果新来的数比末尾的小，开始二分查找
            left=0
            right=len(tail)-1
            while left<right:
                mid=(left+right)>>1
                if tail[mid]<nums[i]:
                    left=mid+1
                else:
                    right=mid
            tail[left]=nums[i]
        return len(tail)

