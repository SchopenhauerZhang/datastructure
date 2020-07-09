# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    node = None
    def convertBiNode(self, roots: TreeNode) -> TreeNode:
        # 先序遍历
        def convert(root):
            if root :
                if not self.node:
                    def get(tt):
                        ll = tt
                        while tt:
                            ll = tt
                            tt = tt.left
                        return ll
                    self.node = get(root)
                l = self.convertBiNode(root.left)
                if l :
                    l.right = root
                    l.left = None
                r = self.convertBiNode(root.right)
                if r :
                    root.right = r
                    return root.right
            return root
        self.convert(roots)

        return self.node 
        
    def _convertBiNode(self, roots: TreeNode) -> TreeNode:
        
        head=TreeNode(None)
        pre=head
        cur=root
        stack=[]
        while cur or stack:
            while cur:
                stack.append(cur)
                cur=cur.left
            cur=stack.pop()
            cur.left=None
            pre.right=cur
            pre=cur
            cur=cur.right
        return head.right

    def _convertBiNode_eg(self, root: TreeNode) -> TreeNode:
        if not root: return None
        def convert(root):
            if not root: return '',''
            begin = end = root
            if root.left:
                begin,end = convert(root.left)
                end.right = root
                end = root
                root.left = None
            if root.right:
                root.right,end = convert(root.right)
            return begin,end
        return convert(root)[0]

# root = TreeNode(4)
# root.left = TreeNode(2)
# root.right = TreeNode(5)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(3)
# root.right.left = None
# root.right.right = TreeNode(6)
# p = Solution()
# t = p.convertBiNode(root)
# #p = root.left.left
# p = p.node
# while p:
#     print(p.val)
#     p = p.right


