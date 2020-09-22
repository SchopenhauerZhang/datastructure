# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        """
            给出二叉 搜索 树的根节点，该二叉树的节点值各不相同，修改二叉树，使每个节点 node 的新值等于原树中大于或等于 node.val 的值之和。

            提醒一下，二叉搜索树满足下列约束条件：

            节点的左子树仅包含键 小于 节点键的节点。
            节点的右子树仅包含键 大于 节点键的节点。
            左右子树也必须是二叉搜索树。
             

            示例：



            输入：[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
            输出：[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
             

            提示：

            树中的节点数介于 1 和 100 之间。
            每个节点的值介于 0 和 100 之间。
            给定的树为二叉搜索树。

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/binary-search-tree-to-greater-sum-tree
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not root or (not root.left and not root.right):
            return root
        val_list = []
        def tree(rt):
            if not rt:
                return None
            if rt.left:
                tree(rt.left)
            if rt.val not in val_list:
                val_list.append(rt.val)
            if rt.right:
                tree(rt.right)
            return 
        def _tree(rt):
            if not rt:
                return None
            if rt.left:
                rt.left = _tree(rt.left)
            rt.val = sum(val_list[val_list.index(rt.val):])
            if rt.right:
                rt.right = _tree(rt.right)
            return rt
        tree(root)
        val_list = sorted(val_list)
        _tree(root)
        return root

    def bstToGst(self, root: TreeNode) -> TreeNode:
        cur=0
        def dfs(root):
            nonlocal cur
            if not root:
                return
            dfs(root.right)
            cur+=root.val
            root.val=cur
            dfs(root.left)
        dfs(root)
        return root
