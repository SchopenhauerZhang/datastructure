# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    self.d= 0
    def maxDepth(self, root: TreeNode) -> int:
        """
        输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。
        `
        例如：

        给定二叉树 [3,9,20,null,null,15,7]，

            3
        / \
        9  20
            /  \
        15   7
        返回它的最大深度 3 。

         

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/er-cha-shu-de-shen-du-lcof
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。`
        """
        def depth(r):
            if not r:
                return 0
            l = depth(r.left)
            r = depth(r.right)

            return max(l,r)+1

        return depth(root) 

    def _maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        queue, res = [root], 0
        while queue:
            temp = []
            for node in queue:
                if node.left: temp.append(node.left)
                if node.right: temp.append(node.right)
            queue = temp
            res += 1
        return res
    
    

    def _maxDepth_104(self, root: TreeNode) -> int:
        """
        给定一个二叉树，找出其最大深度。

        二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

        说明: 叶子节点是指没有子节点的节点。

        示例：
        给定二叉树 [3,9,20,null,null,15,7]，

            3
        / \
        9  20
            /  \
        15   7
        返回它的最大深度 3 。

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/maximum-depth-of-binary-tree
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not root:
            return 0
        self.d = max(self.maxDepth(root.left),self.maxDepth(root.right))+1
        return self.d

    def _maxDepth_104_eg(self, root: TreeNode) -> int:
        if root is None:
            return 0
        elif root.left is None and root.right is None:
            return 1
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        

    def _maxDepth_dq(self, root: TreeNode) -> int:
        """
        注意pop(0)！！！！
        """
        if not root:
            return 0
        q = [root]
        length = 0
        while q:
            _size = len(q)
            length += 1
            for _ in range(_size):
                data = q.pop(0)
                if data:
                    if data.left:
                        q.append(data.left)
                    if data.right:
                        q.append(data.right)
            
        return length
    def _maxDepth_dq_eg(self,root):
        if root == None:
            return 0
        stack = [root]
        i = 0
        while len(stack) != 0:
            n = len(stack)
            i += 1
            # print(stack)
            for k in range(n):
                temp = stack.pop(0)
                if temp.left:
                    stack.append(temp.left)
                if temp.right:
                    stack.append(temp.right)
        return i 






