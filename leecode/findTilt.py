# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        """
        给定一个二叉树，计算整个树的坡度。

一个树的节点的坡度定义即为，该节点左子树的结点之和和右子树结点之和的差的绝对值。空结点的的坡度是0。

整个树的坡度就是其所有节点的坡度之和。

 

示例：

输入：
         1
       /   \
      2     3
输出：1
解释：
结点 2 的坡度: 0
结点 3 的坡度: 0
结点 1 的坡度: |2-3| = 1
树的坡度 : 0 + 0 + 1 = 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-tilt
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """

        def tilt(t):
            if not t:
                return 0,0
            l,vall = tilt(t.left)
            r,valr = tilt(t.right)
            return l+r+t.val,abs(l-r)+vall+valr

        return tilt(root)[1]
 
    def findTilt(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.ans = 0
        def help(root):
            if not root:
                return 0

            left_sum = help(root.left)
            right_sum = help(root.right)

            self.ans += abs(left_sum - right_sum)
            return left_sum + right_sum + root.val
        help(root)
        return self.ans
    

