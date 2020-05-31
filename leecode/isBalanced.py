# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        """
        平衡二叉树，任意节点的左右子树深度之差不超过1
        """
        if not root:
            return True
        def height(root):
            if root is None:
                return 0
            l=height(root.left)
            if l is False:
                return False
            
            r=height(root.right)
            if r is False:
                return False
            if abs(l-r) > 1:
                return False

            return max(l,r)+1


        return False if height(root) is False else True
