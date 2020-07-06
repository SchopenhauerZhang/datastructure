class Solution:
    def lengthOfLIS(self, nums: list) -> int:
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

