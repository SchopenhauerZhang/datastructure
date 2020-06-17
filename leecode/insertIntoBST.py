# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        """
        给定二叉搜索树（BST）的根节点和要插入树中的值，将值插入二叉搜索树。 返回插入后二叉搜索树的根节点。 保证原始二叉搜索树中不存在新值。

        注意，可能存在多种有效的插入方式，只要树在插入后仍保持为二叉搜索树即可。 你可以返回任意有效的结果。

        例如, 

        给定二叉搜索树:

                4
            / \
            2   7
            / \
            1   3

        和 插入的值: 5
        你可以返回这个二叉搜索树:

                4
            /   \
            2     7
            / \   /
            1   3 5
        或者这个树也是有效的:

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/insert-into-a-binary-search-tree
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        pass

    def _insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        elif root.val <= val:
            root.right = self._insertIntoBST(root.right,val)
        elif root.val > val:
            root.left = self._insertIntoBST(root.left,val)

        return root

    def _insertIntoBST_eg(self, root: TreeNode, val: int) -> TreeNode:
        def dfs(root, val):
            if not root:
                return TreeNode(val)
            if root.val < val:
                root.right = dfs(root.right, val)
            elif root.val > val:
                root.left = dfs(root.left, val)
            return root
        return dfs(root, val)