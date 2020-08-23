# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        给定一个二叉树，原地将它展开为一个单链表。

        例如，给定二叉树

            1
        / \
        2   5
        / \   \
        3   4   6
        将其展开为：

        1
        \
        2
        \
            3
            \
            4
            \
                5
                \
                6

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        Do not return anything, modify root in-place instead.
        精彩
        """
        while root:
            if root.left:
                _left = root.left
                right = root.right
                while _left.right:
                    _left = _left.right
                _left.right = right
                root.right = root.left
                root.left = None

            root = root.right

    def _flatten_eg(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root or (not root.left and not root.right):
            return root 
        self.flatten(root.left)
        self.flatten(root.right)
        a1=root.right
        root.right=root.left
        root.left=None 
        while root.right:
            root=root.right
        root.right=a1
        return root 