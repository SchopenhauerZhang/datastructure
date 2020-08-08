# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
                给定一个二叉树，返回它的中序 遍历。

            示例:

            输入: [1,null,2,3]
            1
                \
                2
                /
            3

            输出: [1,3,2]
            进阶: 递归算法很简单，你可以通过迭代算法完成吗？

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/binary-tree-inorder-traversal
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        retv = []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            retv.append(root.val)
            root = root.right
        return retv

    def _inorderTraversal_eg(self, root: TreeNode) -> List[int]:
        # res = []
        # def dfs(root):
        #     if not root:return None
        #     dfs(root.left)
        #     res.append(root.val)
        #     dfs(root.right)
        # dfs(root)
        # return res

        if not root:return []
        cur,stack,res = root, [],[]
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            temp = stack.pop()
            res.append(temp.val)
            cur = temp.right
        return res
            
                

