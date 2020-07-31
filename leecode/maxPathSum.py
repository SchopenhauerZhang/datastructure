# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        """

        给定一个非空二叉树，返回其最大路径和。

        本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。

        示例 1:

        输入: [1,2,3]

            1
            / \
            2   3

        输出: 6
        示例 2:

        输入: [-10,9,20,null,null,15,7]

        -10
        / \
        9  20
            /  \
        15   7

        输出: 42
                """
        self._max = float("-inf")
        def path_sum(h):
            if not h:return 0
            l = path_sum(h.left)
            
            r = path_sum(h.right)
            
            self._max = max(l+r+h.val,self._max)
            return max(l+h.val,r+h.val) if max(l+h.val,r+h.val)> 0 else 0
        path_sum(root)
        return self._max

# s = TreeNode(5)
# s.left = TreeNode(4)
# s.right = TreeNode(8)
# s.left.left = TreeNode(11)
# s.right.left = TreeNode(13)
# s.right.right = TreeNode(4)
# s.left.left.left = TreeNode(7)
# s.left.left.right = TreeNode(2)
# s.right.right.left = TreeNode(1)
# print(Solution().maxPathSum(s))
    def _maxPathSum_eg(self, root: TreeNode) -> int:
        res=float('-inf')
        def dfs(node):
            nonlocal res
            if not node:
                return 0
            lsum=dfs(node.left)
            rsum=dfs(node.right)
            res=max(res,lsum+rsum+node.val)
            return max(0,lsum+node.val,rsum+node.val)
        dfs(root)
        return res