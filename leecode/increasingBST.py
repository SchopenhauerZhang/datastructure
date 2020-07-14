# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        """
        给你一个树，请你 按中序遍历 重新排列树，使树中最左边的结点现在是树的根，并且每个结点没有左子结点，只有一个右子结点。

         

        示例 ：

        输入：[5,3,6,2,4,null,8,1,null,null,null,7,9]

            5
            / \
            3    6
        / \    \
        2   4    8
         /        / \ 
        1        7   9

        输出：[1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

        1
          \
           2
            \
             3
              \
               4
                \
                 5
                  \
                   6
                    \
                     7
                      \
                       8
                        \
                        9  

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/increasing-order-search-tree
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not root:
            return root 
        new_root = TreeNode(-1)
 
        cur, stack = root, []
        parent = None
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left 
            else:
                cur = stack.pop()
                cur.left = None
                if not parent:
                    parent = cur
                    new_root.right = parent 
                else:
                    parent.right = cur 
                    parent = cur   
                cur = cur.right 
        return new_root.right

    def _increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            node.left = None
            self.cur.right = node
            self.cur = node
            inorder(node.right)

        ans = self.cur = TreeNode(-1)
        inorder(root)
        return ans.right
