# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        """
        在二叉树中，根节点位于深度 0 处，每个深度为 k 的节点的子节点位于深度 k+1 处。

如果二叉树的两个节点深度相同，但父节点不同，则它们是一对堂兄弟节点。

我们给出了具有唯一值的二叉树的根节点 root，以及树中两个不同节点的值 x 和 y。

只有与值 x 和 y 对应的节点是堂兄弟节点时，才返回 true。否则，返回 false。

 

示例 1：


输入：root = [1,2,3,4], x = 4, y = 3
输出：false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/cousins-in-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        pass

    x_dp = 0
    y_dp = 0
    x_p = None
    y_p = None
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if not root:
            return False
        def cousins(r,dp,x,y,p):
            if not r:
                return 0
            if r.val == x :
                self.x_dp = dp
                self.x_p = p
            elif r.val == y:
                self.y_dp = dp
                self.y_p = p
            else:
                cousins(r.left,dp+1,x,y,r.val)
                cousins(r.right,dp+1,x,y,r.val)
        cousins(root.left,1,x,y,root.val)
        cousins(root.right,1,x,y,root.val)    
        return self.x_dp == self.y_dp and (self.x_p != self.y_p)  
        
    def _isCousins(self, root: TreeNode, x: int, y: int) -> bool:  
        def dfsFind(root,x,y,level):
            if not root:
                return []
            r1 = []
            if root.left and (root.left.val == x or root.left.val == y) or (root.right and (root.right.val == x or root.right.val == y)) :
                r1 =  [(root.val,level)]
            return dfsFind(root.left,x,y,level+1) + r1 + dfsFind(root.right,x,y,level+1)
        r1= dfsFind(root,x,y,0)
        if len(r1) < 2:
            return False
        if r1[0][0] == r1[1][0] or r1[0][1] != r1[1][1]:
            return False
        return True