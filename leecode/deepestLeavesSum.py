# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        """
            给你一棵二叉树，请你返回层数最深的叶子节点的和。
            示例：
            输入：root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
            输出：15
             

            提示：

            树中节点数目在 1 到 10^4 之间。
            每个节点的值在 1 到 100 之间。

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/deepest-leaves-sum
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not root:
            return  0
        self.res = 0
        def deep(rt):
            q = [rt]
            while q:
                _q = []
                for i in q:
                    if not i:
                        continue
                    if i.left:
                        _q.append(i.left)
                    if i.right:
                        _q.append(i.right)
                if not _q:
                    self.res += sum([int(t.val) for t in q])
                q = _q
            
        deep(root)
        return self.res
    
    def deepestLeavesSum_eg(self, root: TreeNode) -> int:
        Sum=0
        flag=True
        if root is None: return Sum
        queue=[root]
        while queue:
            temp=[]
            for node in queue:
                if node.left: 
                    temp.append(node.left)
                    flag= False
                if node.right: 
                    temp.append(node.right)
                    flag= False
                Sum+=node.val
            if flag: return Sum
            flag=True
            Sum=0
            queue=temp
        return Sum