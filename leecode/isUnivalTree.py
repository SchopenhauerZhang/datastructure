# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    val = float("inf")
    def isUnivalTree(self, root: TreeNode) -> bool:
        """
        如果二叉树每个节点都具有相同的值，那么该二叉树就是单值二叉树。

只有给定的树是单值二叉树时，才返回 true；否则返回 false。

 

示例 1：



输入：[1,1,1,1,1,null,1]
输出：true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/univalued-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not root:
            return True
        if self.val != float("inf") and val != root.val:
            return False
        elif self.val == float("inf"):
            self.val = root.val
        if not self.isUnivalTree(root.left):
            return False
        if not self.isUnivalTree(root.right):
            return False
        return True
    
    def _isUnivalTree(self, root: TreeNode) -> bool:
        if not root: 
            return False
        
        queue = [root]
        value = root.val
        while queue:
            curr = queue.pop()
            if curr:
                if curr.val != value:
                    return False
                else:
                    queue.insert(0,curr.left)
                    queue.insert(0,curr.right)
                
        return True