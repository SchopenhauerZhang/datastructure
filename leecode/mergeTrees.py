# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        """
        给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。

        你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。

        示例 1:

        输入: 
            Tree 1                     Tree 2                  
                1                         2                             
                / \                       / \                            
                3   2                     1   3                        
            /                           \   \                      
            5                             4   7                  
        输出: 
        合并后的树:
                3
                / \
            4   5
            / \   \ 
            5   4   7
        注意: 合并必须从两个树的根节点开始。

        通过次数57,593提交次数75,213

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/merge-two-binary-trees
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        def tree(l:TreeNode,r:TreeNode):
            if not l or not r :
                return l if not r else r
            if l.val and r.val:
                l.val += r.val
            elif  l.val or r.val:
                l.val = r.val if r.val else l.val
            
            l.left = tree(l.left,r.left)
            l.right = tree(l.right,r.right)
            return l

        return tree(t1,t2)
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        # 本题重点是如果某个节点为空, 直接返回另一个节点
        # 递归是人
        if not t1:
            return t2
        if not t2:
            return t1
        t1.val = t1.val + t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1

        # 迭代是神
        # if not t1:
        #     return t2
        # if not t2:
        #     return t1
        # stack = [(t1, t2)]

        # while stack:
        #     t1, t2 = stack.pop()
        #     t1.val += t2.val

        #     if t1.left and t2.left:
        #         stack.append(t1.left, t2.left)
        #     elif t2.left:
        #         t1.left = t2.left

        #     if t1.right and t2.right:
        #         stack.append(t1.right, t2.right)
        #     elif t2.right:
        #         t1.right = t2.right

        # return t1
            
        #     stack.append(t1.left if t1 else None, t2.left if t2 else None)
        #     stack.append(t1.right if t1 else None, t2.right if t2 else None)
        
        # return t1

        