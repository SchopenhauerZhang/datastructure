# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        给定一个二叉树，判断其是否是一个有效的二叉搜索树。

        假设一个二叉搜索树具有如下特征：

        节点的左子树只包含小于当前节点的数。
        节点的右子树只包含大于当前节点的数。
        所有左子树和右子树自身必须也是二叉搜索树。
        示例 1:

        输入:
        2
        / \
        1   3
        输出: true
        示例 2:

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/validate-binary-search-tree
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        pass

    def _isValidBST(self, root: TreeNode) -> bool:
        def _isv(r,mi,mx):
            if not r:
                return True
            elif mi and r.val <= mi.val:
                return False
            elif mx and r.val >= mx.val:
                return False
            else:
                return _isv(r.left,mi,r) and _isv(r.right,r,mx)
        
        return _isv(root,None,None)
        
    def _isValidBST_eg(self, root: TreeNode) -> bool:
        if not root:
            return True
        res = []
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            if stack:
                node = stack.pop()
                if res and node.val <= res[-1]:
                    return False
                res.append(node.val)
                node = node.right
        return True
    
    def _isValidBST_0405(self, root: TreeNode,left=float('-inf',right=float('inf'))) -> bool:
        """
                实现一个函数，检查一棵二叉树是否为二叉搜索树。

                示例 1:
                输入:
                    2
                / \
                1   3
                输出: true
                示例 2:
                输入:
                    5
                / \
                1   4
                     / \
                    3   6
                输出: false
                解释: 输入为: [5,1,4,null,null,3,6]。
                     根节点的值为 5 ，但是其右子节点值为 4 。

                来源：力扣（LeetCode）
                链接：https://leetcode-cn.com/problems/legal-binary-search-tree-lcci
                著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not root:
            return True
        if root.val <=left or root.val >=right:
            return False
        else:
            return self._isValidBST_0405(root.left,left,min(right,root.val)) and self._isValidBST_0405(root.right,max(root.val,left),right)
    def __init__(self):
        super().__init__()
        self.pre = None
    def _isValidBST_0405_eg(self, root: TreeNode) -> bool:
        """
        精彩
        """
        if not root:
            return True
        if not self.isValidBST(root.left):
            return False
        if self.pre and root.val <= self.pre.val:
            return False
        self.pre = root
        if not self.isValidBST(root.right):
            return False

        return True