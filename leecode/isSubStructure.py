# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        """
                输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

        B是A的子结构， 即 A中有出现和B相同的结构和节点值。

        例如:
        给定的树 A:

             3
            / \
           4   5
          / \
         1   2
        给定的树 B：

           4 
          /
         1
        返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

        示例 1：

        输入：A = [1,2,3], B = [3,1]
        输出：false
        示例 2：

        输入：A = [3,4,5,1,2], B = [4,1]
        输出：true

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        pass
    def isSubStructure(self, pRoot1: TreeNode, pRoot2: TreeNode) -> bool:

        if not pRoot1 or not pRoot2:
            return False
        return self.isrubtreeequl(pRoot1,pRoot2) or self.isSubStructure(pRoot1.left, pRoot2) or self.isSubStructure(pRoot1.right, pRoot2)
    def isrubtreeequl(self,root1,root2):
        if not root2:
            return True
        if not root1:
            return False
        return root1.val == root2.val and self.isrubtreeequl(root1.left,root2.left) and self.isrubtreeequl(root1.right,root2.right)

    def _isSubStructure_eg(self, A: TreeNode, B: TreeNode) -> bool:
        if not A or not B:
            return False
        ret = False
        if A.val == B.val:
            ret = self.isequal(A,B)
        if not ret:
            ret = self.isSubStructure(A.left,B)# 只有当根节点相同了才能遍历子节点湿粉扑相同否则没法区分是跟节点不同还是子节点不同，递归条件注意区分
        if not ret:
            ret = self.isSubStructure(A.right,B)
        return ret
    def isequal(self,a,b):
        if not b:
            return True
        if not a or a.val != b.val:
            return False
        return self.isequal(a.left,b.left) and self.isequal(a.right,b.right)