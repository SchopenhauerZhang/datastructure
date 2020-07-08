# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    dia = 0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """
        给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。

 

示例 :
给定二叉树

          1
         / \
        2   3
       / \     
      4   5    
返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/diameter-of-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not root:
            return 0
        def diameter(t):
            if not t:
                return 0
            l = diameter(t.left)
            r = diameter(t.right)
            self.dia = max(l+r,self.dia)
            return max(l,r)+1
        diameter(root)
        return self.dia

    def _diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:return 0
            res = 0
        def high(node):
            nonlocal res
            if not node:return 0
            left = high(node.left)
            right = high(node.right)
            res = max(res,left+right+1)
            return max(left,right)+1
        high(root)
        return res-1