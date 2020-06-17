# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        """
        给定二叉搜索树（BST）的根节点和一个值。 你需要在BST中找到节点值等于给定值的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 NULL。

            例如，

            给定二叉搜索树:

            4
            / \
            2   7
            / \
            1   3

            和值: 2
            你应该返回如下子树:

            2     
            / \   
            1   3
            在上述示例中，如果要找的值是 5，但因为没有节点值为 5，我们应该返回 NULL。

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/search-in-a-binary-search-tree
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        pass

    def _searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None
        elif root.val == val:
            return root
        elif root.val < val:
            return self._searchBST(root.right,val)
        elif root.val > val:
            return self._searchBST(root.left,val)
        else:
            return None
    def _searchBST_eg(self, root: TreeNode, val: int) -> TreeNode:
        #iteration
        stack = []
        if not root:
            return None
        stack.append(root)
        #search 和 traversal 不同的在于，只用取一半！
        #preorder 
        while stack:
            for node in stack:
                stack.pop()
                if node:
                    if node.val == val:
                        return node
                    elif node.val < val:
                        stack.append(node.right)
                    elif node.val > val:
                        stack.append(node.left)
        return
        #inorder
        # while stack or root:
        #     if root:
        #         stack.append(root)
        #         root = root.left
        #     else:
        #         tempNode = stack.pop()
        #         # print(tempNode)
        #         if tempNode.val == val:
        #             return tempNode
        #         else:
        #             #不是直接放入stack，而是转当前节点的有右节点为root
        #             root = tempNode.right
                    
        return 
        
        #recursion
        # if not root:
        #     return None
        # cur_val = root.val
        # if val == cur_val:
        #     return root
        # elif val < cur_val:
        #     return self.searchBST(root.left, val)
        # else: # val > cur_val:
        #     return self.searchBST(root.right, val)