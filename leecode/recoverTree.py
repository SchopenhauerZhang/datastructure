# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        二叉搜索树中的两个节点被错误地交换。

            请在不改变其结构的情况下，恢复这棵树。

            示例 1:

            输入: [1,3,null,null,2]

               1
              /
             3
              \
               2

            输出: [3,1,null,null,2]

               3
              /
             1
              \
               2

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/recover-binary-search-tree
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
                    Do not return anything, modify root in-place instead.
        """
        node = root
        pre, x, y = None, None, None
        stack = []
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if pre and node.val < pre.val:
                if x:
                    y = node
                    break
                x, y = pre, node
            pre = node
            node = node.right
        x.val, y.val = y.val, x.val

    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        精彩
        """
        prev = node1 = node2 = None
        def inorder(node):
            nonlocal prev,node1,node2
            if not node:
                return
            inorder(node.left)
            if prev is not None and node.val < prev.val:
                if not node1:
                    node1 = prev
                node2 = node
            prev = node
            inorder(node.right)
        
        inorder(root)
        node1.val, node2.val = node2.val, node1.val  











