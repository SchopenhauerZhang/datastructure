# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    self.l = []
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def treepath(r,s):
            if not r:
                return s
            s = s + '->'+str(r.val)
            sl = s + self.binaryTreePaths(r.left)
            if sl:
                self.l.append(sl)
            sr = s + self.binaryTreePaths(r.right)
            if sr:
                self.l.append(sr)
            return s
        s = str(root.val)
        treepath(root.left,s)
        treepath(root.right,s)
        return self.l