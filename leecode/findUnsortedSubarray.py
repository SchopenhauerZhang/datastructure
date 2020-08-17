from typing import List
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """
            给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

            你找到的子数组应是最短的，请输出它的长度。

            示例 1:

            输入: [2, 6, 4, 8, 10, 9, 15]
            输出: 5
            解释: 你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
            说明 :

            输入的数组长度范围在 [1, 10,000]。
            输入的数组可能包含重复元素 ，所以升序的意思是<=。

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not nums or len(nums) <= 2:
            return 2 if len(nums) == 2 and nums[0]> nums[1] else 0

        l,r = 0 ,len(nums)-1
        sorted_num = sorted(nums)
        
        l_flag,r_flag = False,False
        while l <= r:
            if sorted_num[l] != nums[l] and not l_flag:
                l_flag = True
            elif not l_flag:
                l += 1
            if sorted_num[r] != nums[r] and not r_flag:
                r_flag = True
            elif not r_flag:
                r -= 1
            if r_flag and l_flag:
                break
        print(l,r)
        return r  - l + 1 if r  - l + 1 > 0 else 0
    
    def _findUnsortedSubarray_eg_0(self, nums: List[int]) -> int:   
        i,j=0,len(nums)-1
        nums1=sorted(nums)
        while i<len(nums) and j>=0:
            if nums[i]==nums1[i]:
                i+=1
            if nums[j]==nums1[j]:
                j-=1
            if i!=len(nums) and j!=0:
                if nums[i]!=nums1[i] and nums[j]!=nums1[j]:
                    break
        return j-i+1 if j-i>0 else 0

    def _findUnsortedSubarray_eg_1(self, nums: List[int]) -> int:   
        p,q=0,0
        for i in range(len(nums)-1):
            if nums[i+1]<nums[i]:
                p=i
                break
        for j in range(len(nums)-1,0,-1):
            if nums[j]<nums[j-1]:
                q=j
                break
        if p==q==0:
            return 0
        minval=max(nums[p:q+1])
        maxval=max(nums[p:q+1])
        for i in range(len(nums[0:p])):
            if nums[i]>minval:
                p=i
                break
        for j in range(len(nums)-1,q,-1):
            if nums[j]<maxval:
                q=j
                break
        return q-p+1

    