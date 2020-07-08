# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if not root:
            return 
        if not L and not R:
            return root 
      
        def trim(t,lv,rv):
            if not t:
                return 
            if t.val <L:
                return trim(t.right,lv,rv)
            if t.val > R:
                return trim(t.left,lv,rv)
            return t
        
        return  trim(root,L,R)
    
    def trimBST(self, root, L, R): # recursively trim the current node
        def trimNode(node):
            if not node: return None
            if node.val > R:
                return trimNode(node.left) # search left for the next within boundary node
            elif node.val < L:
                return trimNode(node.right)
            else:
                node.left = trimNode(node.left)
                node.right = trimNode(node.right)
                return node
        return trimNode(root)