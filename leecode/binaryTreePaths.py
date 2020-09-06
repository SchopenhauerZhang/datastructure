# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List
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
    
    def _binaryTreePaths_257(self, root: TreeNode) -> List[str]:
        if not root or (not root.left and not root.right):
            return [] if not root else [''+str(root.val)+'']
        def tree(node,_res):
            if not node:
                return None
            _resl = tree(node.left,_res+'->'+str(node.val))
            _resr = tree(node.right,_res+'->'+str(node.val))
            if not _resl:
                res.append(_resl)
            if not _resr:
                res.append(_resr)
            if not _resl or not _resr:
                return _res
            return _resl if _resl else _resr
        
        res = []
        res.append(tree(root,''))
        return res 
