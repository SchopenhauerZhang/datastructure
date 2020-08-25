from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
            给定两个数组，编写一个函数来计算它们的交集。
            示例 1：

            输入：nums1 = [1,2,2,1], nums2 = [2,2]
            输出：[2]
            示例 2：

            输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
            输出：[9,4]
             

            说明：

            输出结果中的每个元素一定是唯一的。
            我们可以不考虑输出结果的顺序。

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/intersection-of-two-arrays
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not nums1 or not nums2 :
            return []
        if len(nums1) == 1 and len(nums2) == 1:
            return [] if nums1 != nums2 else nums2
        res = []
        for i in set(nums1):
            if i in set(nums2):
                res.append(i)
        return res
    
    def _intersection_eg(self, nums1: List[int], nums2: List[int]) -> List[int]:        
        nums_1, nums_2 = {}, {}
        res = []
            
        for num in nums1:
            if num not in nums_1:
                nums_1[num] = 1
        
        for num in nums2:
            if num not in nums_2:
                nums_2[num] = 1
        
        for num in nums_1:
            if num in nums_2:
                res.append(num)
        
        return res
