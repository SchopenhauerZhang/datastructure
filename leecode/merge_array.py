class Solution:
    def merge_array(self, nums1: list, m: int, nums2: list, n: int) -> None:
        """
        给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
        说明:

        初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
        你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
         

        示例:

        输入:
        nums1 = [1,2,3,0,0,0], m = 3
        nums2 = [2,5,6],       n = 3

        输出: [1,2,2,3,5,6]

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/merge-sorted-array
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2[:n]
        nums1.sort()

#print(Solution().merge_array([1,2,3,0,0,0],3,[2,5,6],3))

    def _merge_eg(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2, p = m-1, n-1, m+n-1
        while p1 >= 0 and p2 >= 0:
            if(nums1[p1] < nums2[p2]):
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1
        nums1[:p2 + 1] = nums2[:p2 + 1]

