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

    def _isBalanced_eg(self, root: TreeNode) -> bool:  
        def dfs(root):
            if not root: return 0
            left = dfs(root.left)
            if left == -1: return -1
            right= dfs(root.right)
            if right == -1: return -1
            return max(left, right) + 1 if abs(left - right) <= 1 else -1
        return dfs(root) != -1