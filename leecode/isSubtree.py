# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        """
        给定两个非空二叉树 s 和 t，检验 s 中是否包含和 t 具有相同结构和节点值的子树。s 的一个子树包括 s 的一个节点和这个节点的所有子孙。s 也可以看做它自身的一棵子树。

        示例 1:
        给定的树 s:

            3
            / \
        4   5
        / \
        1   2
        给定的树 t：

        4 
        / \
        1   2
        返回 true，因为 t 与 s 的一个子树拥有相同的结构和节点值。

        示例 2:
        给定的树 s：

            3
            / \
        4   5
        / \
        1   2
            /
        0
        给定的树 t：

        4
        / \
        1   2
        返回 false。

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/subtree-of-another-tree
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not s and not t :
            return True
        if not s or not t:
            return False
        def ubtre(l,r):
            if not l and not r:
                return True
            if not l or not r:
                return False
            if l.val == r.val and ubtre(l.left,r.left) and ubtre(l.right,r.right):
                return True
            return False
        que = list()
        que.append(s)
        while que:
            _t = que.pop(0)
            if _t:
                que.append(_t.left)
                que.append(_t.right)
                if _t.val == t.val and ubtre(_t.left,t.left) and ubtre(_t.right,t.right):
                    return True
        return False

# t = TreeNode(1)
# t.left = TreeNode(2)
# t.right = TreeNode(3)
# t1 = TreeNode(2)
# print(Solution().isSubtree(t,t1))

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        cur = s
        tem = t
        def helper(cur,tem,flag=0):
            if not cur and not tem:
                return True
            elif None in (cur,tem):
                return False
            elif cur and tem:
                if cur.val==tem.val:
                    flag=1
                    if helper(cur.left,tem.left,flag) and helper(cur.right,tem.right,flag):
                        return True
                elif flag==1:
                    return False

                if helper(cur.left,tem,0) or helper(cur.right,tem,0):
                    return True                  
        return helper(cur,tem)
