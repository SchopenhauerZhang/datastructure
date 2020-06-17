# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        """"
        给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。

        一般来说，删除节点可分为两个步骤：

        首先找到需要删除的节点；
        如果找到了，删除它。
        说明： 要求算法时间复杂度为 O(h)，h 为树的高度。

        示例:

        root = [5,3,6,2,4,null,7]
        key = 3

            5
        / \
        3   6
        / \   \
        2   4   7

        给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。

        一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。

            5
        / \
        4   6
        /     \
        2       7

        另一个正确答案是 [5,2,6,null,4,null,7]。

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/delete-node-in-a-bst
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """"
        pass

    def _deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        def get_m(r):
            while r.left:
                r = r.left
            return r

        if not root :
            return root
        elif key == root.val:
            if not root.left  and  not  root.right:
                return None
            elif not root.left  or  not  root.right:
                return root.left if root.left else root.right
            else:
                min_n = get_m(root.right)
                root.val = min_n.val
                root.right = self._deleteNode(root.right,min_n.val)
                
        elif key < root.val:
            root.left = self._deleteNode(root.left,key)
        elif key > root.val:
            root.right = self._deleteNode(root.right,key)

        return root

    def _deleteNode_eg(self, root: TreeNode, key: int):
        if not root: return None
        
        if key < root.val : root.left = self.deleteNode(root.left, key)
        elif key > root.val : root.right = self.deleteNode(root.right, key)
        else :
            if root.left:
                node = root.left
                while node.right: node = node.right
                node.right = root.right
                return root.left
            else :
                return root.right
        
        return root
        