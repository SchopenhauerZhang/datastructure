# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        """
        给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。

示例:

给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回它的最小深度  2.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-depth-of-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        def helper(root):
            if not root:
                return 0
            else:
                if root and root.left and root.right:
                    return min(helper(root.left) + 1, helper(root.right) + 1)
                elif root and root.left and not root.right:
                    return helper(root.left) + 1
                elif root and not root.left and root.right:
                    return helper(root.right) + 1
                elif root and not root.left and not root.right:
                    return 1
                else:
                    return 0
        return helper(root)
        
        