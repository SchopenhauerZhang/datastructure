# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        """
            给定一个二叉树，返回所有从根节点到叶子节点的路径。

            说明: 叶子节点是指没有子节点的节点。

            示例:

            输入:

            1
            /   \
            2     3
            \
            5

            输出: ["1->2->5", "1->3"]

            解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/binary-tree-paths
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not root or (not root.left and not root.right):
            return [] if not root else [''+str(root.val)+'']
        def tree(node,_res):
            if not node:
                return None
      
            _res = str(node.val) if not _res else _res+'->'+str(node.val)
            if node.left:
                tree(node.left,_res)
            if node.right :
                tree(node.right,_res)
            if not node.left and not node.right:
                if not _res:
                    return 
                print(res)
                res.append(_res)
            return 
        
        res = []
        tree(root,'')
        return res

    def binaryTreePaths_eg(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        res=[]
        def dfs(root,path):
            path+=str(root.val)
            if not root.left and not root.right:
                res.append(path)
            elif not root.left:
                dfs(root.right,path+'->')
            elif not root.right:
                dfs(root.left,path+'->')
            else:
                dfs(root.right,path+'->')
                dfs(root.left,path+'->')


        dfs(root,'')
        return res