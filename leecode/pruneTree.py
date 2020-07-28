# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        """
        给定二叉树根结点 root ，此外树的每个结点的值要么是 0，要么是 1。

        返回移除了所有不包含 1 的子树的原二叉树。

        ( 节点 X 的子树为 X 本身，以及所有 X 的后代。)

        示例1:
        输入: [1,null,0,0,1]
        输出: [1,null,0,null,1]
        
        解释: 
        只有红色节点满足条件“所有不包含 1 的子树”。
        右图为返回的答案。


        示例2:
        输入: [1,0,1,0,0,0,1]
        输出: [1,null,1,null,1]



        示例3:
        输入: [1,1,0,1,1,0,1,0]
        输出: [1,1,0,1,1,null,1]



        说明:

        给定的二叉树最多有 100 个节点。
        每个节点的值只会为 0 或 1 。

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/binary-tree-pruning
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if root.left:
            root.left = self.pruneTree(root.left)
        if root.right:
            root.right = self.pruneTree(root.right)
        if not root.left and not root.right and root.val ==0:
            return None
        return root
    
    def _pruneTree_eg(self, root):
        """
        :param root: TreeNode
        :return: TreeNode
        """

        def __dfs(root):
            if not root:
                return True

            l_prune = __dfs(root.left)
            r_prune = __dfs(root.right)
            cur_prune = True if root.val == 0 else False

            if l_prune:
                root.left = None
            if r_prune:
                root.right = None

            if cur_prune and l_prune and r_prune:
                return True
            else:
                return False

        if __dfs(root):
            return None
        else:
            return root


