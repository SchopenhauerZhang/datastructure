# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        """
        翻转一棵二叉树。

        示例：

        输入：

            4
        /   \
        2     7
        / \   / \
        1   3 6   9
        输出：

            4
        /   \
        7     2
        / \   / \
        9   6 3   1

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/invert-binary-tree
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        def TreeNodes(r:TreeNode):
            if not r:
                return 
            tmp = r.left
            r.left = TreeNodes(r.right)
            r.right = TreeNodes(tmp)
            return r

        return TreeNodes(root)

    def invertTree(self, root: TreeNode) -> TreeNode:

        if not root:
            return None

        tmp = root.left
        root.left = root.right
        root.right = tmp


        self.invertTree(root.left)
        self.invertTree(root.right)

        return root