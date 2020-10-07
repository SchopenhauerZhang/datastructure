# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        """
            计算给定二叉树的所有左叶子之和。

            示例：

                3
            / \
            9  20
                /  \
            15   7

            在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/sum-of-left-leaves
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        res = 0
        if not root:
            return res
        q = [root]
        q_left = []
        while q:
            _q  = []
            for i in q:
                if not i :
                    continue
                if not i.left and not i.right:
                    continue
                else:
                    q_left.append(i.left)
                    _q.append(i.left)
                    _q.append(i.right)
            if _q:
                q = _q
            else:
                q = []
        for i in q_left:
            if not i:
                continue
            if i.left or i.right:
                continue
            else:
                res+=i.val
                
        return res

    def sumOfLeftLeaves_eg(self, root: TreeNode) -> int:
        if not  root:
            return 0
        tmp = root
        stack = [tmp]
        res = 0
        while stack:
            node = stack.pop()
            if node:
                # 减少了一次迭代遍历
                if node.left and not node.left.left and not node.left.right:
                    res += node.left.val
                stack.append(node.left)
                stack.append(node.right)
        return res
                



