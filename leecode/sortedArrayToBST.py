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
    
    def _sortedArrayToBST_108(self, nums: List[int]) -> TreeNode:
        """
            将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。

            本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

            示例:

            给定有序数组: [-10,-3,0,5,9],

            一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

                0
                / \
            -3   9
            /   /
            -10  5

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not nums or len(nums) <= 3 :
            if not nums:
                return None
            if len(nums) == 1:
                return TreeNode(nums[0])
            p = TreeNode(nums[1])
            p.left = TreeNode(nums[0])
            p.right = TreeNode(nums[2]) if len(nums) == 3 else None
            return p
        head = None
        def tree(num):
            if not num:
                return 
            if len(num) == 1:
                return TreeNode(num[0])
            ll = len(num)
            p = TreeNode(num[ll//2])
            p.left = tree(num[:ll//2])
            p.right = tree(num[ll//2+1:])
            return p
        head = TreeNode(nums[len(nums)//2])
        head.left = tree(nums[:len(nums)//2])
        head.right = tree(nums[len(nums)//2+1:])
        return head
    
    def _sortedArrayToBST_108_eg(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        mid = len(nums) // 2
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid+1:])
        return node





