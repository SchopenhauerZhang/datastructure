# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: list) -> TreeNode:
        """
        给定一个有序整数数组，元素各不相同且按升序排列，编写一个算法，创建一棵高度最小的二叉搜索树。

        示例:
        给定有序数组: [-10,-3,0,5,9],

        一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

                0 
                / \ 
            -3   9 
            /   / 
            -10  5 

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/minimum-height-tree-lcci
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not nums:
            return None
        def ArrayToBST(lists):
            if not lists:
                return None
            m = len(lists)//2
            t = TreeNode(lists[m])
            if len(lists) == 1:
                return t
            t.left = ArrayToBST(lists[:m])
            t.right = ArrayToBST(lists[m+1:])
            
            return t

        return ArrayToBST(nums)

    def _sortedArrayToBST(self, nums: list) -> TreeNode:
        if not nums:
            return
        nums_len = len(nums)
        if nums_len == 1:
            return TreeNode(nums[0])
        root = TreeNode(nums[int(nums_len/2)])
        root.left = self.sortedArrayToBST(nums[:int(nums_len/2)])
        if int(nums_len/2)+1 < nums_len:
            root.right = self.sortedArrayToBST(nums[int(nums_len/2)+1:])
        return root





