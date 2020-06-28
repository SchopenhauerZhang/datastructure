# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

        百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

        例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]

        示例 1:

        输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
        输出: 3
        解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
        示例 2:

        输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
        输出: 5
        解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
         

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        pass

    def _lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        if p.val == root.val or q.val == root.val:
            return root 

        def list_tree(node,p,q):
            if not node: 
                return None
            if node.val == q.val or node.val == p.val:
                return node
                
            left = list_tree(node.left,p,q)
            right = list_tree(node.right,p,q)
            if left and right:
                return node
            elif not left and not right:
                return None
            else:
                return left if left else right

        return list_tree(root,p,q)

    def _lowestCommonAncestor_eg(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root == p or root == q:return root
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if left and right: return root
        if not left: return right
        if not right: return left