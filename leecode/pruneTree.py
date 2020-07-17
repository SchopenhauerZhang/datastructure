# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if root and root.val == 1:
            root.left = self.pruneTree(root.left)
            root.right = self.pruneTree(root.right)
            return root
        elif root :
            root.left = self.pruneTree(root.left)
            root.right = self.pruneTree(root.right)
            if (root.left and root.left.val == 1) or (root.right and root.right.val == 1):
                return root

        return None


