# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        """
        给定一个二叉树，检查它是否是镜像对称的。

 

        例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
        """
        if not root:
            return True
        else:
            def is_sym(nodel,noder):
                if not nodel and not noder:
                    return True
                elif not nodel or  not noder:
                    return False
                elif  nodel.val != noder.val:
                    return False
                else:
                    return is_sym(nodel.left,noder.right) and is_sym(nodel.right,noder.left)

            return is_sym(root.left,root.right) 

#print(Solution().isSymmetric(1534236469))
    def isSymmetric_(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.judge(root.left,root.right)

    def judge(self,node1,node2):
        if not node1 and not node2:
            return True
        if node1 and node2:
            if node1.val==node2.val:
                return self.judge(node1.left,node2.right) and self.judge(node1.right,node2.left)
            
        return False
    
    def isSymmetric_28(self,root:TreeNode):
        """
        判断二叉树是否是镜像对称，内存节约多
        """
        if not root:
            return True
        
        def is_requal(l,r):

            if not l or not r:
                return False
            elif not l and not r:
                return False
            elif l.val != r.val:
                return False
            else:
                return is_requal(l.left,r.right) and is_requal(l.right,r.left)
        return is_requal(root.left,root.right)

    def isSymmetric_min_time(self, root: TreeNode) -> bool:
        """
        判断二叉树是否是镜像对称，时间节约多
        """
        if not root:return True
        def ismirror(p,q):
            if not p and not q:return True
            if not p or not q:return False
            if p.val == q.val:
                return ismirror(p.left,q.right) and ismirror(p.right,q.left)
            else:
                return False
        return ismirror(root,root)


