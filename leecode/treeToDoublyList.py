"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        self.left = None
        self.right = None
        def treeToDoubly(h):
            if not h:
                return None
            if h.left:
                l = treeToDoubly(h.left)
                if l :
                    if not self.left :
                        self.left = l
                    h.left = l
                    l.right = h

            if h.right:
                r = treeToDoubly(h.right)
                if r:
                    h.right = r
                    r.left = h
            return h if not h.right else h.right
        treeToDoubly(root)
        return self.left