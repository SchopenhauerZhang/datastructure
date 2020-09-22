# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        """
            给定一个二叉树，在树的最后一行找到最左边的值。

            示例 1:

            输入:

                2
            / \
            1   3

            输出:
            1
             

            示例 2:

            输入:

                    1
                / \
                2   3
                /   / \
                4   5   6
                /
                7

            输出:
            7
             

            注意: 您可以假设树（即给定的根节点）不为 NULL。

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/find-bottom-left-tree-value
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not root:
            return 0
        self._dp = 0
        self._val = None
        def find(d,rt):
            if not rt:
                return (d,None)
            d+=1
            if d > self._dp:
                self._dp = d
                self._val = rt.val
            find(d,rt.left)
            find(d,rt.right)
            return 
        find(0,root)

        return self._val
    
    def findBottomLeftValue_eg(self, root: TreeNode) -> int:
        if not root:
            return 
        
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        return node.val