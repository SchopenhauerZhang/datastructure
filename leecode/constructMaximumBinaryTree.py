# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        def BinaryTree(num,s,r):
            if not num:
                return None
      

            _max_i = s
            for _i in range(s,r+1,1):
                if num[_i] > num[_max_i]:
                    _max_i = _i
            print(_max_i)
            node = TreeNode(num[_max_i])
            if s < _max_i:
                node.left = BinaryTree(num,s,_max_i-1)
            if _max_i < r:
                node.left = BinaryTree(num,_max_i+1,r)

            return node

        return BinaryTree(nums,0,len(nums)-1)