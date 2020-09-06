from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
            给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。

            请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

            你可以假设 nums1 和 nums2 不会同时为空。

             

            示例 1:

            nums1 = [1, 3]
            nums2 = [2]

            则中位数是 2.0
            示例 2:

            nums1 = [1, 2]
            nums2 = [3, 4]

            则中位数是 (2 + 3)/2 = 2.5

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not nums1 or not nums2:
            q = nums1 if not nums2 else nums2
        else:
            q = nums2 + nums1
        
        q = sorted(q)

        while q: 
            if len(q) == 1 or len(q) == 2:
                print(q,sum(q)/2)
                return q[0] if len(q) == 1 else sum(q)/2
            q.pop(0)
            q.pop()
        return 
    
    def _findMedianSortedArrays_eg(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1:
            a=nums2;
        if not nums2:
            a=nums1;
        a=nums1+nums2;
        a.sort()
        c=len(a)
        if c%2==0:
            return (a[int(c/2)]+a[int(c/2)-1])/2;
        else:
            return a[int(c/2)]
        