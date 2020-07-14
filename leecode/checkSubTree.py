# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def checkSubTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        """

检查子树。你有两棵非常大的二叉树：T1，有几万个节点；T2，有几万个节点。设计一个算法，判断 T2 是否为 T1 的子树。

如果 T1 有这么一个节点 n，其子树与 T2 一模一样，则 T2 为 T1 的子树，也就是说，从节点 n 处把树砍断，得到的树与 T2 完全相同。

示例1:

 输入：t1 = [1, 2, 3], t2 = [2]
 输出：true
示例2:

 输入：t1 = [1, null, 2, 4], t2 = [3, 2]
 输出：false
提示：

树的节点数目范围为[0, 20000]。
        """
        if (not t1 and not t2 ) or (t1 == t2):
            return True
        if not t1 or not t2:
            return False 
        
        def check(l,r):
            if not l and not r:
                return True
            if not l or not r:
                return False

            if l.val == r.val:
                return check(l.left,r.left) or check(l.right,r.right)
            return check(l.left,r) or check(l.right,r)

        return check(t1,t2)
        
# t = TreeNode(1)
# t.left = TreeNode(2)
# t.right = TreeNode(3)
# t1 = TreeNode(2)
# print(Solution().checkSubTree(t,t1))


    def _checkSubTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        if not t2:
            return True
        tv = t2.val
        d = deque()
        d.append(t1)
        while d:
            item = d.popleft()
            if item:
                d.append(item.left)
                d.append(item.right)
                if item.val == tv and self.same(item,t2):
                    return True
        return False

    def same(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t:
            return True
        if not s or not t:
            return False
        if s.val != t.val:
            return False
        return self.same(s.left, t.left) and self.same(s.right, t.right)