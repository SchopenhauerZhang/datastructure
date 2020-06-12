class Solution:
    def findDisappearedNumbers(self, nums: list) -> list:
        """
        给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。

        找到所有在 [1, n] 范围之间没有出现在数组中的数字。

        您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。

        示例:

        输入:
        [4,3,2,7,8,2,3,1]

        输出:
        [5,6]

        """
        pass

    def _findDisappearedNumbers_yi_huo(self, num: list) -> list:
        # 找出缺少的那个元素
        nums = sorted(num)
        num = [0]*(nums[len(nums)-1]+1)
        for i in nums:
            num[i]=i

        res = 0
        res = res ^ len(nums)
        rs = list()
        for i in range(len(nums)):
            res ^= i ^ nums[i]
            if len(nums) != res:
                rs.append(res)
        return [res]
#print(Solution()._findDisappearedNumbers_yi_huo([4,3,2,7,8,2,3,1]))

    def _findDisappearedNumbers_sum(self, num: list) -> list:
        return (max(num)*(max(num)+1))/2 -sum(num)
#print(Solution()._findDisappearedNumbers_sum([4,3,6,7,8,2,1,0]))

    def _findDisappearedNumbers_(self, nums: list) -> list:
        num = nums
        if len(num)<=1:
            return num

        res = list()
        for i in range(1,len(num)+1):
            if i not in num:
                res.append(int(i))

        return res
#print(Solution()._findDisappearedNumbers_([2,2]))
#print(Solution()._findDisappearedNumbers_([4,3,2,7,8,2,3,1]))

    def _findDisappearedNumbers_set(self, nums: list) -> list:
        if len(nums) <= 1:
            return nums

        for i in range(len(nums)):
            while nums[i]!=i+1:
                temp=nums[nums[i]-1]
                nums[nums[i]-1]=nums[i]
                nums[i]=temp
                if nums[nums[i]-1]==nums[i]:
                    break
        res=[]
        for i in range(len(nums)):
            if nums[i]!=i+1:
                res.append(i+1)
        return res
# print(Solution()._findDisappearedNumbers_set([2,2]))
# print(Solution()._findDisappearedNumbers_set([4,3,2,7,8,2,3,1]))

    def _findDisappearedNumbers_best_eg(self, nums: list) -> list:
        # 精彩
        return {i for i in range(1,len(nums)+1)}-set(nums)
