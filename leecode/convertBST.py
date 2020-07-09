# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    num = 0
    def convertBST(self, root: TreeNode) -> TreeNode:
        """
        给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。

 

        例如：

        输入: 原始二叉搜索树:
                    5
                    /   \
                2     13

        输出: 转换为累加树:
                    18
                    /   \
                20     13

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/convert-bst-to-greater-tree
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if root:
            self.convertBST(root.right)
            root.val += self.num
            self.num = root.val
            self.convertBST(root.left)
            return root
        return None

    def __init__(self):
        self.total = 0
    def _convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        if root.right is not None:
            self._convertBST(root.right)
            self.total = self.total + root.val
            root.val = self.total
            self._convertBST(root.left)
        else:
            root.val = root.val+self.total
            self.total = root.val
            self._convertBST(root.left)
        return root 
