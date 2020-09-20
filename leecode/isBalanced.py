# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        """
        平衡二叉树，任意节点的左右子树深度之差不超过1
        """
        if not root:
            return True
        def height(root):
            if root is None:
                return 0
            l=height(root.left)
            if l is False:
                return False
            
            r=height(root.right)
            if r is False:
                return False
            if abs(l-r) > 1:
                return False

            return max(l,r)+1


        return False if height(root) is False else True

    def _isBalanced_eg(self, root: TreeNode) -> bool:  
        def dfs(root):
            if not root: return 0
            left = dfs(root.left)
            if left == -1: return -1
            right= dfs(root.right)
            if right == -1: return -1
            return max(left, right) + 1 if abs(left - right) <= 1 else -1
        return dfs(root) != -1
    
    def isBalanced_04_04(self, root: TreeNode) -> bool:
        """
            实现一个函数，检查二叉树是否平衡。在这个问题中，平衡树的定义如下：任意一个节点，其两棵子树的高度差不超过 1。


            示例 1:
            给定二叉树 [3,9,20,null,null,15,7]
                3
            / \
            9  20
                /  \
            15   7
            返回 true 。
            示例 2:
            给定二叉树 [1,2,2,3,3,null,null,4,4]
                1
                / \
                2   2
            / \
            3   3
            / \
            4   4
            返回 false 。

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/check-balance-lcci
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        def isb(rt):
            if not rt:
                return 0
            l = isb(rt.left)
            if l is False:
                return False
            r = isb(rt.right)
            if r is False:
                return False
            if abs(l-r) > 1:
                return False
            return max(l,r)+1
        if isb(root) is False:
            return False
        return True
    
    def isBalanced_04_04_eg(self, root: TreeNode) -> bool:
        def h(node):
            if node is None:return 0
            l=h(node.left)
            if l is None:return None
            r=h(node.right)
            if r is None:return None
            if abs(l-r)>1:return None
            else:return max(l,r)+1
        return h(root) is not None